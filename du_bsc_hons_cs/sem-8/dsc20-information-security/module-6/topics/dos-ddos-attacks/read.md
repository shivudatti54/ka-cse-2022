# DoS and DDoS Attacks

## Introduction

In today's interconnected digital landscape, where businesses, governments, and individuals rely heavily on internet-based services, the availability of these services has become paramount. Denial of Service (DoS) and Distributed Denial of Service (DDoS) attacks represent one of the most significant threats to service availability, causing substantial financial losses, reputational damage, and disruption to critical infrastructure. These attacks have evolved considerably over the decades, from simple volumetric floods to sophisticated multi-vector assaults that combine various techniques to overwhelm targets.

For students pursuing Computer Science at the University of Delhi, understanding DoS/DDoS attacks is essential not only for acing their Information Security examinations but also for developing a comprehensive understanding of cybersecurity principles. The 2024 NEP curriculum emphasizes practical knowledge combined with theoretical foundations, making this topic particularly relevant. Major incidents like the 2016 Dyn DDoS attack (which disrupted Twitter, Netflix, and Reddit) and the 2023 Reddit outage demonstrate the real-world impact of these attacks. This module will explore the mechanics, types, detection methods, and mitigation strategies for DoS and DDoS attacks, providing you with the knowledge required to analyze and respond to such threats.

## Key Concepts

### Understanding Denial of Service (DoS) Attacks

A Denial of Service (DoS) attack is a malicious attempt to disrupt the normal functioning of a targeted server, service, or network by overwhelming it with a flood of internet traffic or exploiting vulnerabilities that cause system failure. The primary objective is not to steal data but to render the target inaccessible to legitimate users. DoS attacks typically originate from a single source, making them relatively easier to trace and mitigate compared to their distributed counterparts.

The fundamental principle behind most DoS attacks is resource exhaustion. Servers, whether web servers, DNS servers, or application servers, have finite resources including bandwidth, CPU cycles, memory, and connection limits. By consuming these resources faster than they can be replenished, attackers can cause the system to become unresponsive to legitimate requests.

### Types of DoS Attacks

**1. Volumetric Attacks**
These attacks aim to consume the entire bandwidth available to the target by sending massive amounts of data. The goal is to create congestion so severe that legitimate traffic cannot reach the server. Examples include:
- **UDP Flood**: Sends large numbers of User Datagram Protocol (UDP) packets to random ports on the target system, forcing it to check for applications listening at those ports and respond with ICMP Destination Unreachable packets.
- **ICMP Flood (Ping Flood)**: Overwhelms the target with Internet Control Message Protocol (ICMP) echo request packets, consuming both outgoing and incoming bandwidth.
- **Amplification Attacks**: Exploits publicly accessible DNS, NTP, or SNMP servers to reflect and amplify traffic toward the victim. The attacker sends small requests to these servers with the victim's IP address as the source, causing the servers to send much larger responses to the target.

**2. Protocol Attacks**
These attacks exploit weaknesses in layer 3 and layer 4 of the OSI model, consuming server resources or intermediate infrastructure resources like firewalls and load balancers. Examples include:
- **SYN Flood**: Exploits the TCP three-way handshake mechanism. The attacker sends a large number of SYN packets with forged source IP addresses. The server allocates resources for half-open connections, waiting for the final ACK that never arrives, eventually exhausting its connection table.
- **Ping of Death**: Sends IP packets larger than the maximum allowed size (65,535 bytes) via fragmented packets, causing the target system to crash when it attempts to reassemble them.
- **Smurf Attack**: Exploits ICMP by sending spoofed ping packets to network broadcast addresses, causing all hosts on the network to respond to the victim's IP address.

**3. Application Layer Attacks**
These sophisticated attacks target specific applications or services, aiming to exhaust resources by mimicking legitimate user behavior. They are harder to detect because the traffic patterns resemble normal user activity. Examples include:
- **HTTP Flood**: Sends HTTP GET or POST requests that appear legitimate but are designed to consume server resources.
- **Slowloris**: Opens multiple connections to the target server and sends partial HTTP requests at slow intervals, keeping connections open and eventually exhausting the server's maximum concurrent connections.
- **R-U-Dead-Yet (RUDY)**: Similar to Slowloris but uses POST requests with intentionally slow data transmission.

### Distributed Denial of Service (DDoS) Attacks

A Distributed Denial of Service (DDoS) attack amplifies the impact of a DoS attack by using multiple compromised systems (often called a botnet or zombie army) to launch the attack simultaneously. This distribution makes DDoS attacks far more powerful and significantly harder to mitigate because:
- The attack traffic comes from thousands or even millions of unique IP addresses
- Distinguishing malicious traffic from legitimate traffic becomes extremely challenging
- Tracing the actual source is complicated by the multiple layers of compromised systems

Botnets are typically created by spreading malware through phishing emails, malicious websites, or software vulnerabilities. Once infected, these compromised devices (including computers, IoT devices, and servers) can be controlled remotely by the attacker to participate in DDoS attacks.

### DDoS Attack Vectors

Modern DDoS attacks often combine multiple attack vectors to overwhelm defenses. The Mirai botnet, responsible for some of the largest DDoS attacks in history, primarily exploited IoT devices like cameras and routers. Other notable DDoS attack methods include:

- **Memcached Amplification**: Exploits misconfigured Memcached servers to amplify traffic by factors of up to 51,000x
- **CLDAP (Connection-less Lightweight Directory Access Protocol) Reflection**: Uses misconfigured LDAP servers to reflect and amplify attack traffic
- **Application-layer multi-vector attacks**: Combines HTTP flood with other techniques to bypass rate limiting and web application firewalls

### Detection and Mitigation

Detecting DoS/DDoS attacks requires continuous monitoring of network traffic patterns and system performance. Key indicators include:
- Unusually slow network performance
- Unavailability of a particular website or service
- Sudden spike in spam emails
- Multiple failed connection attempts from a single IP or IP range

Mitigation strategies include:
- **Traffic Scrubbing**: Diverting traffic through specialized cleaning centers that filter out malicious packets
- **Rate Limiting**: Limiting the number of requests from a single IP address
- **Content Delivery Networks (CDNs)**: Distributing traffic across multiple servers geographically
- **DDoS Protection Services**: Using cloud-based services like Cloudflare, Akamai, or AWS Shield
- **Network Segmentation**: Isolating critical services from public-facing infrastructure

## Examples

### Example 1: SYN Flood Attack Analysis

Consider a web server with a maximum of 65,536 TCP connections available in its backlog queue. In a SYN flood attack:

**Step 1**: Attacker sends 100,000 SYN packets with spoofed source IP addresses to the web server.

**Step 2**: For each SYN packet, the server allocates memory for a Transmission Control Block (TCB) and sends back a SYN-ACK response, waiting for the final ACK to complete the handshake.

**Step 3**: The attacker never sends the final ACK, leaving all 100,000 connections in half-open state.

**Step 4**: After 65,536 connections fill the backlog queue, legitimate users attempting to connect receive no response.

**Solution**: Modern servers implement SYN cookies, where the server doesn't allocate resources until the complete three-way handshake is finished. The server encodes connection information in the sequence number, allowing it to verify the final ACK without maintaining state.

### Example 2: Application-Layer HTTP Flood

An e-commerce website experiences degraded performance during peak hours. Analysis reveals:

**Attack Pattern**: 5,000 requests per second from 50,000 different IP addresses, each requesting the search database query page.

**Why It's Effective**: Each search query requires CPU-intensive database operations. The server processes each request legitimately, but the volume exhausts database connections.

**Detection Challenge**: Each IP makes only 0.1 requests per second—well below typical rate limiting thresholds. The attack appears as legitimate high traffic.

**Mitigation**: Implement behavior-based analysis that identifies abnormal query patterns, use CAPTCHA for automated requests, and implement database query caching.

### Example 3: Real-World DDoS Incident

The 2016 Dyn DNS attack demonstrates the cascading impact of DDoS:

**Target**: Dyn, a major DNS provider
**Method**: Mirai botnet attacking DNS infrastructure
**Impact**: Major websites (Twitter, Netflix, Reddit, CNN) became unreachable for hours
**Botnet Size**: 100,000+ compromised IoT devices
**Traffic Volume**: Over 1 Tbps at its peak

**Key Lesson**: Attackers targeted the DNS infrastructure rather than individual websites, affecting all domains using Dyn's DNS services. This highlighted the importance of infrastructure diversity and redundancy.

## Exam Tips

For your DU Information Security examination, keep these essential points in mind:

1. **Distinguish between DoS and DDoS**: Remember that DoS originates from a single source while DDoS uses multiple distributed sources (botnets). This distinction is crucial for both written answers and practical scenarios.

2. **Understand the OSI layer classification**: Know that volumetric attacks target Layer 3/4, while application-layer attacks target Layer 7. This classification helps in selecting appropriate mitigation strategies.

3. **Memorize key attack types and their mechanisms**: Be prepared to explain how SYN floods exploit the TCP handshake, how amplification attacks work, and the difference between reflection and amplification.

4. **Know modern mitigation approaches**: Cloud-based DDoS protection services, traffic scrubbing, and content delivery networks are industry-standard solutions—make sure you can explain their working.

5. **Real-world examples matter**: Referring to incidents like Mirai botnet or the Dyn attack demonstrates deeper understanding and is often rewarded in examinations.

6. **Connection between botnets and DDoS**: Understand how attackers create botnets using malware and why IoT devices are particularly vulnerable.

7. **Protocol vulnerabilities**: Be clear about which protocols are exploited and why (e.g., UDP's connectionless nature makes it vulnerable to spoofing).

8. **Defense in depth**: Remember that no single solution is sufficient—effective defense requires multiple layers including network filtering, server hardening, and incident response planning.