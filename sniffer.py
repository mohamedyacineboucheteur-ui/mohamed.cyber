from scapy.all import sniff, TCP, UDP, IP, DNS, DNSQR
from collections import defaultdict
import time
import sys

# رموز الألوان الخاصة بالتيرمينال
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

PAYLOAD_SIZE_THRESHOLD = 500  

# قاموس لتتبع تكرار طلبات الـ DNS لكل جهاز
request_tracker = defaultdict(list)

def analyze_packet(packet):
    # 1. تحليل حزم TCP (الحجم والمنافذ المشبوهة)
    if packet.haslayer(IP) and packet.haslayer(TCP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        src_port = packet[TCP].sport
        dst_port = packet[TCP].dport
        
        payload = bytes(packet[TCP].payload)
        payload_len = len(payload)
        
        # [تم إخفاء الطباعة العادية هنا لكي لا تظهر إلا التنبيهات]

        # قاعدة كشف شذوذ الحجم
        if payload_len > PAYLOAD_SIZE_THRESHOLD:
            print(f"{RED}[!] ANOMALY ALERT: Large payload detected ({payload_len} bytes) from {src_ip}:{src_port} --> {dst_ip}:{dst_port}{RESET}")
            
        # فحص المنافذ المشبوهة
        suspicious_ports = [23, 4444, 31337, 4445, 1337]
        if dst_port in suspicious_ports or src_port in suspicious_ports:
            print(f"{RED}[!] ANOMALY ALERT: Traffic on high-risk/suspicious port detected ({src_port} -> {dst_port}) between {src_ip} and {dst_ip}!{RESET}")

    # 2. تحليل حزم DNS (لكشف الـ DNS Tunneling والتكرار)
    elif packet.haslayer(IP) and packet.haslayer(DNS) and packet.haslayer(DNSQR):
        try:
            qname = packet[DNSQR].qname.decode('utf-8')
            src_ip = packet[IP].src
            
            # أ. فحص طول اسم النطاق (Anomaly in length)
            if len(qname) > 50: 
                print(f"{RED}[!] SUSPICIOUS DNS: Long query detected ({len(qname)} chars) from {src_ip}: {qname}{RESET}")
                
            # ب. فحص التكرار (Frequency check)
            current_time = time.time()
            request_tracker[src_ip] = [t for t in request_tracker[src_ip] if current_time - t < 5]
            request_tracker[src_ip].append(current_time)
            
            if len(request_tracker[src_ip]) > 20:
                print(f"{RED}[!] FREQUENCY ALERT: High rate DNS queries from {src_ip} ({len(request_tracker[src_ip])} requests in 5s){RESET}")
        except Exception as e:
            pass

def main():
    print(f"{YELLOW}[*] Sniffer is running in Silent/Alert-Only Mode... Waiting for anomalies.{RESET}")
    print(f"{YELLOW}[*] Press Ctrl+C to stop.{RESET}")
    try:
        sniff(filter="tcp or udp port 53", prn=analyze_packet, store=False)
    except KeyboardInterrupt:
        print(f"\n{YELLOW}[*] Sniffer stopped by user. Exiting cleanly...{RESET}")
        sys.exit(0)

if __name__ == "__main__":
    main()
