# Network Attacks and Countermeasures - Summary

## Key Definitions and Concepts

- **Network Attack**: Any deliberate attempt to compromise the confidentiality, integrity, or availability of network resources and data
- **Passive Attack**: Unauthorized monitoring of network traffic to gather information without altering data (e.g., sniffing, eavesdropping)
- **Active Attack**: Attempts to alter system resources or affect their operation (e.g., DoS, MITM, data modification)
- **DoS (Denial of Service)**: Attack that makes a system unavailable to legitimate users by consuming resources
- **DDoS (Distributed DoS)**: Coordinated attack from multiple sources targeting a single victim
- **SYN Flood**: DoS attack exploiting TCP three-way handshake by sending SYN packets without completing handshake
- **MITM (Man-in-the-Middle)**: Attack where attacker secretly intercepts communications between two parties
- **ARP Spoofing**: Falsifying ARP messages to associate attacker's MAC with victim's IP
- **DNS Cache Poisoning**: Inserting false DNS records into resolver cache to redirect traffic
- **Port Scanning**: Systematic scanning of target systems to identify open ports and services

## Important Formulas and Techniques

- **TCP Three-Way Handshake**: SYN → SYN-ACK → ACK (vulnerable to SYN floods)
- **SYN Cookie Mechanism**: Stores half-open connection state in initial sequence number
- **Defense-in-Depth**: Multiple layered security controls (perimeter, network, application, data)
- **RATE Limiting**: Restricting request rate to mitigate flooding attacks

## Key Points

1. Network attacks are categorized as passive (information gathering) or active (resource disruption/data modification)
2. DoS attacks aim to exhaust system resources; DDoS uses multiple sources making mitigation harder
3. SYN flood exploits TCP handshake by initiating but never completing connections
4. MITM attacks intercept communications; ARP spoofing is common in LAN environments
5. DNS attacks exploit trust in DNS infrastructure—cache poisoning redirects users to malicious sites
6. Firewalls provide perimeter security; IDS/IPS detect and prevent threats based on signatures or anomalies
7. Network segmentation limits attack spread; VLANs provide logical isolation of network segments
8. Encryption (TLS, VPN, SSH) protects data confidentiality during transmission
9. Port scanning is reconnaissance—understanding these techniques helps in vulnerability assessment
10. No single countermeasure is sufficient; defense-in-depth requires multiple layered protections

## Common Mistakes to Avoid

- Confusing DoS with DDoS—understand that DDoS involves multiple coordinated attack sources
- Thinking firewalls alone are sufficient—modern attacks require layered security approaches
- Overlooking the importance of encryption—unencrypted protocols remain vulnerable to sniffing
- Neglecting internal network security—attacks like ARP spoofing target internal networks
- Ignoring the human factor—many attacks succeed through social engineering combined with technical exploits

## Revision Tips

1. Create a table mapping each attack type to its OSI layer, attack vector, and countermeasure
2. Practice drawing and explaining the TCP three-way handshake and where vulnerabilities exist
3. Review case studies of major attacks (Mirai botnet, Dyn DNS attack) to understand real-world impact
4. Use packet capture tools like Wireshark to observe network traffic and identify attack patterns
5. Focus on understanding the "why" behind each countermeasure—exam questions often test application not just memorization