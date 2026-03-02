# Network Attacks and Firewalls

## Introduction

In today's interconnected digital landscape, network security has become a paramount concern for organizations and individuals alike. The exponential growth of the internet, coupled with the proliferation of cloud services and remote work arrangements, has created an expanded attack surface for malicious actors. Network attacks pose significant threats to confidentiality, integrity, and availability of information systems. According to the Indian Computer Emergency Response Team (CERT-In), India witnessed over 14 lakh cybersecurity incidents in 2022 alone, highlighting the critical need for robust network security measures.

Firewalls serve as the first line of defense against network-based threats, acting as a barrier between trusted internal networks and untrusted external networks. Understanding network attacks and firewall mechanisms is essential for any Computer Science graduate, particularly in the context of the University of Delhi's Information Security curriculum. This topic covers the classification of network attacks, their mechanisms, and the defensive strategies employed by modern firewalls to mitigate these threats.

## Key Concepts

### Classification of Network Attacks

Network attacks can be broadly categorized into two types: **passive attacks** and **active attacks**. Passive attacks involve unauthorized monitoring of network traffic to gather information, while active attacks involve attempting to alter system resources or affect their operation. Understanding this distinction is crucial for designing appropriate security controls.

**Denial of Service (DoS) Attacks** represent one of the most prevalent forms of network attacks. In a DoS attack, the attacker overwhelms the target system with traffic or requests, rendering it unavailable to legitimate users. Distributed Denial of Service (DDoS) attacks amplify this threat by coordinating multiple compromised systems (botnets) to launch a coordinated attack. Common types include SYN flood, ICMP flood, and UDP flood attacks. The 2016 Dyn DDoS attack, which disrupted major websites including Twitter and Netflix, demonstrated the devastating scale of such attacks.

**Man-in-the-Middle (MITM) Attacks** occur when an attacker secretly intercepts and potentially alters communications between two parties who believe they are communicating directly. This attack is particularly dangerous on unsecured Wi-Fi networks and can lead to theft of sensitive information like login credentials and financial data. Session hijacking is a related attack where an attacker takes over an established session between a user and a server.

**Injection Attacks** target application-layer vulnerabilities. **SQL Injection** occurs when malicious SQL code is inserted into application queries through user input fields, potentially allowing attackers to access, modify, or delete database contents. **Cross-Site Scripting (XSS)** involves injecting malicious scripts into web pages viewed by other users, enabling session theft, defacement, or redirection to malicious sites.

**Port Scanning and Reconnaissance** attacks precede many other attack types. Attackers use tools like Nmap to discover live hosts, open ports, and running services, gathering intelligence for targeted attacks. Understanding reconnaissance techniques helps security professionals anticipate and prevent attacks.

### Firewall Fundamentals

A firewall is a network security device or software that monitors and controls incoming and outgoing network traffic based on predetermined security rules. Firewalls establish a barrier between trusted internal networks and untrusted external networks, examining each packet of data against security policies.

The core functions of a firewall include:
- **Packet Filtering**: Examining individual packets without considering the context of the connection
- **State Tracking**: Maintaining information about active connections (stateful inspection)
- **Application-Level Control**: Understanding specific protocols and applications
- **Logging and Alerting**: Recording security events for analysis and forensics

### Types of Firewalls

**Packet Filtering Firewalls** operate at the Network Layer (Layer 3) of the OSI model. They examine each packet independently, filtering based on source/destination IP addresses, ports, and protocols. These firewalls are fast and transparent but cannot filter based on application content or detect sophisticated attacks that span multiple packets.

**Stateful Inspection Firewalls**, also known as dynamic packet filtering firewalls, track the state of active connections. They maintain a state table that records connection details (source IP, destination IP, ports, sequence numbers). Only packets matching known valid connections are allowed, providing better security than simple packet filtering. Most modern enterprise firewalls use this approach.

**Proxy Firewalls** operate at the Application Layer (Layer 7), acting as an intermediary between internal clients and external servers. They inspect entire application-level communications, providing deep packet inspection and the ability to cache content for performance. Proxy firewalls provide strong security but may introduce latency due to processing overhead.

**Next-Generation Firewalls (NGFW)** combine traditional firewall capabilities with additional features like:
- Intrusion Prevention System (IPS)
- Application awareness and control
- User identity integration
- SSL/SSH decryption
- Advanced threat protection
- Geolocation-based filtering

### Firewall Architecture

**Screened Subnet (DMZ)** architecture creates a demilitarized zone between the internal network and the external network. Public-facing services are placed in the DMZ, isolated from the internal network. This architecture limits damage if the DMZ is compromised while maintaining accessibility to external users.

**Multi-tiered Firewall Architecture** employs multiple firewall layers for defense in depth. Traffic must pass through multiple checkpoints, each providing different security controls. This approach significantly increases the difficulty for attackers to reach critical resources.

## Examples

### Example 1: SYN Flood Attack Analysis

Consider a SYN flood attack where an attacker sends a large number of TCP SYN packets to a target server but never completes the three-way handshake.

**Step 1**: Attacker sends SYN packets with spoofed source IP addresses to target server's port 80.

**Step 2**: Server allocates resources (memory for connection queue) for each half-open connection and sends SYN-ACK responses.

**Step 3**: Legitimate users cannot establish connections as the server's connection table becomes full.

**Defense Mechanism**: Implement SYN cookies, which encode connection information in the initial sequence number rather than storing state. When the client completes the handshake, the server validates the cookie and only then allocates resources.

### Example 2: Firewall Rule Configuration

Given a corporate network scenario, configure rules for a web server in the DMZ:

| Rule | Action | Source | Destination | Port | Protocol |
|------|--------|--------|-------------|------|----------|
| 1 | Allow | Any | DMZ-WebServer | 80 | TCP |
| 2 | Allow | Any | DMZ-WebServer | 443 | TCP |
| 3 | Allow | DMZ-WebServer | Internal-DB | 5432 | TCP |
| 4 | Allow | Internal-Network | DMZ-WebServer | Any | Any |
| 5 | Deny | Any | Any | Any | Any |

Rule 1-2 allow HTTP/HTTPS traffic to the web server. Rule 3 permits database queries from the web server to the internal database. Rule 4 allows management access from the internal network. The final deny rule ensures all other traffic is blocked.

### Example 3: SQL Injection Attack

Consider a login form with the following vulnerable SQL query:
```sql
SELECT * FROM users WHERE username = '" + username + "' AND password = '" + password + "'"
```

An attacker enters: `' OR '1'='1` as username and password.

The resulting query becomes:
```sql
SELECT * FROM users WHERE username = '' OR '1'='1' AND password = '' OR '1'='1'
```

Since '1'='1' is always true, the attacker gains unauthorized access without valid credentials.

**Defense**: Use parameterized queries (prepared statements) that treat user input as data, not executable code:
```python
cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
```

## Exam Tips

1. **Remember the OSI Model Layers**: Firewalls operate at different OSI layers—Packet filtering (Layer 3), Stateful inspection (Layer 4), Proxy (Layer 7). This is frequently tested in DU exams.

2. **Difference Between DoS and DDoS**: Emphasize that DDoS uses multiple compromised systems (botnets) and is harder to mitigate due to distributed nature.

3. **Stateful vs Stateless Filtering**: Stateful firewalls maintain connection state tables and are more secure; stateless firewalls check packets individually.

4. **DMZ Purpose**: The DMZ isolates public services from internal network; understand why this architecture limits damage during attacks.

5. **Defense in Depth**: Explain that multiple security layers (firewall, IDS, antivirus, encryption) provide better protection than single solutions.

6. **Attack Prevention**: For each major attack type (MITM, SQL Injection, XSS), remember at least one prevention mechanism.

7. **Firewall Rule Ordering**: The rule order matters—specific rules should come before general rules. The implicit deny rule at the end is crucial.

8. **Application Security**: Remember that application-layer attacks (SQLi, XSS) often bypass network firewalls, requiring application-level security measures.