# Linux System Hardening & Security Audit Project

## 🎯 Project Overview
This project demonstrates a practical security audit and system hardening lifecycle. Using **Lynis** as an auditing framework, the system's baseline security posture was evaluated, vulnerabilities were systematically remediated, and the overall hardening index was successfully improved.

---

## 🛠️ Tools & Technologies Used
* **Auditing Framework:** Lynis
* **Firewall Management:** UFW (Uncomplicated Firewall)
* **Intrusion Prevention:** Fail2Ban
* **Remote Access Security:** OpenSSH Server

---

## 🚀 Implementation Phases

### 1. Baseline Security Audit
* Executed an initial automated audit using Lynis to identify configuration gaps, exposed services, and permission weaknesses.

### 2. Remediation & Hardening Steps
* **SSH Hardening:** 
  * Disabled direct root login by setting `PermitRootLogin no` in `/etc/ssh/sshd_config` to mitigate brute-force risks against administrative accounts.
* **Firewall Implementation (UFW):**
  * Configured default policies to deny all incoming traffic and allow outgoing traffic (`default deny incoming`, `default allow outgoing`).
  * Explicitly allowed administrative remote access (`ufw allow ssh`) and enabled the firewall.
* **Brute-Force Protection (Fail2Ban):**
  * Deployed and configured `fail2ban` to monitor system logs for suspicious authentication failures and dynamically ban malicious IP addresses.

### 3. Verification & Results
* Re-ran the Lynis security audit to measure the impact of the applied security controls.
* **Hardening Index Achieved:** **65 / 100**

---

## 📈 Conclusion
Through systematic hardening—addressing remote access vectors, enforcing strict packet filtering, and implementing automated intrusion prevention—the system's overall security posture was significantly elevated from its initial baseline.
