# Firewalls: Characteristics & Types

## Introduction
A firewall is a network security device or software that monitors and controls incoming and outgoing network traffic based on predetermined security rules. It establishes a barrier between trusted internal networks and untrusted external networks (like the Internet), serving as the first line of defense in information security.

---

## Key Characteristics of Firewalls

- **Packet Filtering**: Examines packets (data units) and allows or blocks them based on source/destination IP, port numbers, and protocols
- **Stateful Inspection**: Tracks active connections and makes decisions based on the context of the traffic
- **Application-Level Control**: Controls access to specific applications and services
- **NAT (Network Address Translation)**: Hides internal IP addresses from external networks
- **Logging and Auditing**: Records security events for monitoring and analysis
- **VPN Support**: Enables secure remote access through encrypted tunnels
- **Intrusion Prevention**: Detects and blocks malicious activities

---

## Types of Firewalls

### 1. Based on Filtering Method

- **Packet Filtering Firewall**
  - Operates at Network Layer (Layer 3)
  - Examines packet headers only
  - Fast but limited security
  - Cannot filter content

- **Stateful Inspection Firewall**
  - Operates at Transport & Network Layers
  - Tracks connection state (NEW, ESTABLISHED, RELATED)
  - More secure than packet filtering
  - Example: Cisco ASA, Check Point

- **Proxy Firewall (Application-Level Gateway)**
  - Operates at Application Layer (Layer 7)
  - Acts as intermediary between internal and external systems
  - Provides deep packet inspection
  - Types: HTTP proxy, FTP proxy, SMTP proxy
  - Example: Squid, Microsoft Forefront TMG

### 2. Based on Architecture

- **Hardware Firewall**
  - Dedicated physical device
  - High performance
  - Suitable for large networks
  - Example: Cisco PIX, Fortinet FortiGate

- **Software Firewall**
  - Installed on operating systems
  - Used for endpoint protection
  - Example: Windows Firewall, iptables (Linux)

### 3. Next-Generation Firewall (NGFW)

- Combines traditional firewall with advanced features
- Includes: Application awareness, Intrusion Prevention System (IPS), User identity integration, SSL/SSH inspection, Advanced malware protection
- Example: Palo Alto Networks, FortiGate NGFW

### 4. Cloud Firewall (Firewall-as-a-Service)

- Delivered as cloud service
- Scalable and flexible
- Example: AWS Security Groups, Azure Firewall

---

## Conclusion

Firewalls are fundamental to network security, providing critical protection against unauthorized access. Understanding their characteristics and types is essential for implementing effective security policies. For the Delhi University (NEP 2024) syllabus, focus on distinguishing between packet filtering, stateful inspection, and proxy firewalls, along with NGFW features—common exam topics.

**Key Exam Points**: Remember the OSI layer at which each firewall type operates, their advantages/disadvantages, and real-world examples.