# Cloud Security Approaches
*Ge8A Information Security - BSc Physical Science (CS), Delhi University, NEP 2024*

---

## Introduction

Cloud computing has revolutionized IT infrastructure by offering scalable, on-demand resources over the internet. However, it introduces unique security challenges due to shared responsibility models, multi-tenancy, and data breaches. Understanding cloud security approaches is essential for protecting sensitive information and ensuring compliance in cloud environments.

---

## Key Cloud Security Approaches

### 1. **Identity and Access Management (IAM)**
- Implements **least privilege principle** – users get minimum permissions needed
- Enforces **multi-factor authentication (MFA)** for secure access
- Uses role-based access control (RBAC) and attribute-based access control (ABAC)
- Centralizes user identity management across cloud services

### 2. **Data Security Measures**
- **Data Encryption**: Data at rest (stored) and in transit (moving) using AES, TLS/SSL protocols
- **Tokenization & Masking**: Replaces sensitive data with unique identifiers
- **Data Loss Prevention (DLP)**: Monitors and controls data transfer
- **Key Management**: Secure storage and rotation of encryption keys

### 3. **Network Security**
- **Virtual Private Cloud (VPC)**: Isolates cloud resources in private networks
- **Security Groups & Firewalls**: Controls inbound/outbound traffic
- **VPN & Direct Connect**: Secure connectivity to cloud infrastructure
- **Web Application Firewall (WAF)**: Protects against web-based attacks

### 4. **Cloud Deployment Models & Security**
- **Public Cloud**: Shared responsibility – provider secures infrastructure, user secures data
- **Private Cloud**: Dedicated resources with enhanced control
- **Hybrid Cloud**: Combines on-premise and public cloud, requiring unified security policies

### 5. **Compliance & Governance**
- Follows standards: **ISO 27001, SOC 2, GDPR, HIPAA**
- Regular **audits** and **security assessments**
- Implements **cloud security posture management (CSPM)** for continuous monitoring
- Maintains **incident response plans** for breach scenarios

### 6. **Virtualization Security**
- Secures hypervisors and virtual machines
- Isolation between tenants in multi-tenancy environments
- Regular patching and vulnerability management

### 7. **Zero Trust Architecture**
- "Never trust, always verify" principle
- Continuous authentication and validation
- Micro-segmentation for granular security

---

## Conclusion

Cloud security requires a multi-layered approach combining identity management, encryption, network controls, and compliance measures. As organizations migrate to cloud environments, implementing these security approaches is critical to protect data, maintain trust, and meet regulatory requirements. Understanding these concepts prepares students to address real-world security challenges in cloud computing.

---

*Revision Note: Focus on understanding shared responsibility model, encryption types, IAM best practices, and compliance frameworks for exam success.*