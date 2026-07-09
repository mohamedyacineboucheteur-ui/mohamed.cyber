# Network Scanner Tool (ARP)
Custom Python tool for network auditing and device discovery.

## Features
- Fast device discovery using ARP requests.
- Maps IP addresses to MAC addresses.
- Useful for home and office network security auditing.

## Implementation Result
![Network Scan Results](Scan%20Results.png)

## Languages
- **English**: Developed a custom scanner to increase visibility of connected assets.
- **Français**: Développement d'un outil de scan réseau pour la détection d'appareils actifs.

## 🔍 Security Analysis: Endpoint Network Verification
Documenting the process of validating active network connections to identify potential anomalies.

### Analysis Details
- **Tool:** Sysinternals TCPView
- **Objective:** Verify process integrity and validate destination endpoints.
- **Methodology:**
    1. Identification of active outbound connections via `chrome.exe` on port 443.
    2. Execution of real-time WHOIS lookup on suspected remote IP addresses.
    3. Cross-referencing destination domains (e.g., `facebook.com`) against known infrastructure metadata.
- **Finding:** The connection originated from a trusted domain (Facebook/Meta infrastructure). The traffic pattern is consistent with standard browser activity.
- ![TCPView Analysis](Screenshot%202026-07-09%20003125.png)

---
*Key Insight: Continuous validation of remote endpoints is critical for minimizing the risk of unauthorized data exfiltration.*
