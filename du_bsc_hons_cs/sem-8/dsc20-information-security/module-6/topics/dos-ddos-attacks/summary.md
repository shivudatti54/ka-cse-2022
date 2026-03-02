# DoS and DDoS Attacks - Summary

## Key Definitions and Concepts

- **Denial of Service (DoS)**: An attack that disrupts normal functioning of a targeted server, service, or network by overwhelming it with traffic or exploiting vulnerabilities, rendering it unavailable to legitimate users
- **Distributed Denial of Service (DDoS)**: A DoS attack launched from multiple distributed sources (typically a botnet) to amplify its impact and make mitigation extremely difficult
- **Botnet**: A network of compromised computers (zombies) controlled remotely by an attacker to launch coordinated attacks
- **Amplification Attack**: Exploits publicly accessible servers to reflect and magnify attack traffic toward the victim

## Important Formulas and Concepts

- **Amplification Factor**: The ratio of response size to request size (e.g., DNS amplification can achieve 50x+ amplification)
- **Backlog Queue**: TCP servers maintain limited queue for half-open connections—SYN floods exploit this limit
- **SYN Cookies**: A mitigation technique where servers encode connection state in sequence numbers rather than storing it locally

## Key Points

- DoS attacks are classified into three categories: Volumetric (bandwidth consumption), Protocol (layer 3/4 exploits), and Application Layer (targeting specific applications)
- SYN floods exploit the TCP three-way handshake by sending SYN packets without completing the handshake, exhausting server connection tables
- DDoS attacks use botnets to generate traffic from thousands of IP addresses, making detection and blocking extremely challenging
- Modern DDoS attacks exceed 1 Tbps in volume and often combine multiple attack vectors (multi-vector attacks)
- IoT devices are particularly vulnerable to botnet recruitment due to weak security and default credentials
- Cloud-based DDoS protection services (Cloudflare, Akamai) are the primary defense against large-scale attacks
- The 2016 Dyn attack demonstrated how targeting DNS infrastructure can affect millions of users simultaneously

## Common Mistakes to Avoid

- Confusing DoS with DDoS—remember distributed means multiple sources
- Thinking that blocking a few IP addresses will stop a DDoS—botnets contain thousands of sources
- Underestimating application-layer attacks—they mimic legitimate traffic and bypass traditional filtering
- Ignoring the importance of DNS infrastructure in DDoS preparedness

## Revision Tips

1. Create a table comparing attack types (volumetric vs protocol vs application) with examples
2. Practice explaining how SYN cookies work as a defense mechanism
3. Remember that amplification = reflection + magnification
4. Review the Mirai botnet case study to understand real-world DDoS evolution
5. Focus on understanding why IoT devices are preferred targets for botnets