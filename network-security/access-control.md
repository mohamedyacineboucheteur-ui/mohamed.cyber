# Access Control in Cybersecurity: Models & Principles

## 1. Introduction to Access Control
Access control includes control over access to network resources, information, systems, and data. It is crucial for an organization to implement proper access controls to protect its resources and information. A security analyst must understand the different basic models for implementing access controls used within the organization.

---

## 2. Three Core Access Control Models

### A. Mandatory Access Control (MAC)
* **Overview:** The strictest control model, primarily designed and used by government and military entities. It enforces system-administrator-defined access controls across all controlled resources.
* **How it works:** MAC assigns a **security label** to each resource (containing classifications like *Top Secret*, *Secret*, *Confidential*, and categories like department numbers or project names). User accounts are assigned matching properties. Access is granted only if the user's credentials strictly match the resource's security label.
* **Drawbacks:** High system management overhead due to frequent updates needed for new data, users, and classification changes.

### B. Discretionary Access Control (DAC)
* **Overview:** A flexible model where the **owners** of information control access permissions at their discretion.
* **How it works:** Instead of security labels, each resource has an **Access Control List (ACL)** associated with it. The ACL defines authorized users/groups and their specific access levels (e.g., *Read-Only*, *Full Control*).
* **Example:** File system permissions, where the owner of a file or folder decides who can access it.
* **Drawbacks:** Increases the risk of data exposure to unauthorized users due to decentralized permission management.

### C. Non-Discretionary Access Control (NDAC)
* **Overview:** Access decisions are based on an individual's roles, responsibilities, and job functions within the organization (Role-Based or Rule-Based).
* **How it works:** The corporation or agency owns the system objects, and access is allowed or denied based on a centralized set of rules defined by a system administrator.
* **Example:** Permitting a security analyst to **only read** firewall logs while blocking them from changing any firewall configurations.

---

## 3. Basic Access Control Principles

* **Principle of Least Privilege:** Grants users and processes the minimum necessary access rights for the shortest time required to complete a task. This limits potential damage from accidental or malicious attacks.
* **Separation of Duties:** Requires more than one person to complete a critical task by dividing authority, creating internal controls to prevent fraud and errors.
