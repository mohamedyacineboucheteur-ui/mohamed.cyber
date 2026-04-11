import scapy.all as scapy

def scanner(ip):
    # إنشاء حزمة ARP للكشف عن الأجهزة في الشبكة
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    request = broadcast / arp_request
    
    # إرسال الحزمة واستلام الردود
    answered_list = scapy.srp(request, timeout=1, verbose=False)[0]

    print("\n[+] الأجهزة المتصلة بالشبكة حالياً:")
    print("-----------------------------------------")
    print("IP Address\t\tMAC Address")
    print("-----------------------------------------")
    
    for element in answered_list:
        print(element[1].psrc + "\t\t" + element[1].hwsrc)

# قم بتغيير العنوان أدناه حسب نطاق شبكتك (غالباً 192.168.1.1/24)
try:
    scanner("192.168.1.1/24")
except PermissionError:
    print("[-] خطأ: يرجى تشغيل السكربت بصلاحيات المسؤول (Run as Administrator)")