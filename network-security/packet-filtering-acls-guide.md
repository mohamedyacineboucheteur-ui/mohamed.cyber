---
title: "تصفية الحزم باستخدام قوائم التحكم في الوصول (ACLs) وتحليل السجلات"
date: "2026-10-28"
category: "network-security"
author: "Mohamed Yacine"
tags: ["Cisco", "ACL", "Network Security", "SOC"]
---

# 🛡️ تصفية الحزم باستخدام قوائم التحكم في الوصول (ACLs)
**دليل هندسي وتحليلي شامل للتحكم في حركة المرور وتحليل سجلات الأمان في موجهات Cisco**

---

## 1. مفهوم مرشحات الحزم (Packet Filtering)
تعتبر قوائم التحكم في الوصول (**ACLs**) أبسط أنواع جدران الحماية التي تعمل على مستوى الموجه (Router). بدون إعداد هذه القوائم، تمر جميع الحزم عبر الموجه دون أي قيود. عند تطبيق ACL، يُصبح الموجه مرشحاً للحزم يفحص كل حزمة بشكل منفصل ويتخذ قراراً بـ **السماح (Permit)** أو **المنع (Deny)** بناءً على السياسات المحددة:

* **عناوين IP الشبكية (Network Layer):** فحص عناوين المصدر والوجهة (Source & Destination IP في الطبقة الثالثة).
* **أرقام المنافذ وبروتوكولات النقل (Transport Layer):** التمييز بين بروتوكولات الطبقة الرابعة مثل TCP و UDP و ICMP و OSPF.
* **بتات التزامن (TCP Flags):** تحديد منافذ المصدر والوجهة عند استخدام TCP أو UDP (مثل التحقق من بتات `ACK` و `RST` لمنع بدء الاتصالات غير المصرح بها من الخارج على منافذ مثل Port 80, 443, 21).

---

## 2. تطبيق قاعدة بيانات سياسات الوصول (Sample ACL Configuration)
في البيئات المؤسسية، تطبق القوائم للتحكم في الوصول بين شبكة المستخدمين وشبكة الخوادم. التكوين النموذجي التالي يمثل القائمة رقم `100` والمطبقة على الواجهة `GigabitEthernet0/1`:

```text
! Define Access Control List 100
access-list 100 permit tcp any 10.10.10.10 eq www
access-list 100 permit tcp any 10.10.10.10 eq 443
access-list 100 permit tcp any 10.10.10.11 eq www
access-list 100 permit tcp any 10.10.10.11 eq 443
access-list 100 permit tcp any 10.10.10.12 eq ftp
access-list 100 permit tcp any 10.10.10.12 eq ftp-data
access-list 100 deny ip any any log

! Apply ACL to Interface Inbound
interface GigabitEthernet0/1
 ip address 10.1.1.1 255.255.255.0
 ip access-group 100 in
