# Network Attacks & Countermeasures

## Introduction
Network security forms the backbone of modern information systems. With increasing reliance on distributed systems and cloud infrastructure, understanding network attacks and their mitigation has become critical for cybersecurity professionals. The average cost of a data breach reached $4.45 million in 2023 (IBM Report), making this knowledge essential for protecting organizational assets.

This topic covers both offensive techniques used by malicious actors and defensive strategies employed by security professionals. From reconnaissance attacks to advanced persistent threats, we analyze the attack lifecycle and corresponding defense-in-depth approaches. The content is particularly relevant for MCA students aiming for roles in network security engineering, SOC operations, and cybersecurity architecture.

## Key Concepts

1. **Attack Taxonomy**
   - **Passive Attacks**: Eavesdropping (e.g., packet sniffing using Wireshark)
   - **Active Attacks**: MITM (ARP spoofing), DDoS (SYN Flood), DNS Spoofing
   - **Insider Threats**: Privilege escalation, data exfiltration

2. **Common Attack Vectors**
   - **Phishing**: Business Email Compromise (BEC) attacks
   - **Zero-Day Exploits**: Log4j vulnerability (CVE-2021-44228)
   - **Wireless Attacks**: Evil Twin AP, KRACK (Key Reinstallation Attack)

3. **Countermeasure Framework**
   - **Prevention**: Firewalls (Stateful vs. Next-Gen), IDS/IPS (Snort rules)
   - **Detection**: Network Behavior Analysis (NBA), SIEM (Splunk queries)
   - **Response**: Incident Response Playbooks, Network Segmentation

4. **Protocol-Specific Protections**
   - DNSSEC for DNS integrity
   - SSH instead of Telnet
   - MACsec for layer 2 security

## Examples

**Example 1: Mitigating SYN Flood Attack**
1. **Attack Mechanism**: Attacker sends TCP SYN packets with spoofed IPs
2. **Detection**: Monitor half-open connections (netstat -n -p tcp | grep SYN_RECV)
3. **Mitigation**:
   - Implement SYN cookies in Linux kernel
   - Configure threshold limits on firewall (e.g., 100 SYN/sec)
   - Use cloud-based DDoS protection (AWS Shield)

**Example 2: Detecting ARP Spoofing**
1. **Attack Scenario**: Attacker sends fake ARP replies to redirect traffic
2. **Detection Tool**: Arpwatch (monitors MAC-IP binding changes)
3. **Prevention**:
   - Enable DHCP snooping on switches
   - Implement static ARP entries for critical servers
   - Use 802.1X port authentication

**Example 3: Phishing Campaign Analysis**
1. **Indicators**: Misspelled domain (paypa1.com instead of paypal.com)
2. **Header Analysis**:
   - Check SPF/DKIM/DMARC records
   - Analyze X-Originating-IP header
3. **User Training**: Conduct simulated phishing tests using KnowBe4

## Exam Tips
1. Focus on OSI layer-specific attacks (e.g., Layer 2: MAC flooding, Layer 7: HTTP Slowloris)
2. Memorize RFC standards: 793 (TCP) for SYN flood context, 4953 (SMTP) for email security
3. Understand cryptographic countermeasures: IPsec vs SSL/TLS
4. Practice writing Snort IDS rules for given attack patterns
5. Study NIST SP 800-61 incident handling phases
6. Compare stateful vs stateless firewall architectures
7. Know cloud-specific defenses: AWS Security Groups, Azure NSGs