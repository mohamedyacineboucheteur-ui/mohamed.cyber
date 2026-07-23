from scapy.all import sniff, TCP

# دالة سيتم استدعاؤها مع كل حزمة يتم التقاطها
def packet_callback(packet):
    # التحقق مما إذا كانت الحزمة تحتوي على طبقة TCP
    if packet.haslayer(TCP):
        src_ip = packet[0][1].src
        dst_ip = packet[0][1].dst
        sport = packet[TCP].sport
        dport = packet[TCP].dport
        
        print(f"[+] TCP Packet: {src_ip}:{sport} --> {dst_ip}:{dport}")
        
        # التحقق مما إذا كانت الحزمة تحتوي على بيانات نصية (Payload)
        if packet.haslayer('Raw'):
            payload = packet['Raw'].load
            print(f"    Payload: {payload}")

print("[*] Starting packet capture... Press Ctrl+C to stop.")
# التقاط الحزم المرتبطة بالمنفذ 4444 فقط
sniff(filter="tcp port 4444", prn=packet_callback, store=False, iface="lo")
