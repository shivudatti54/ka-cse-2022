# Network Attacks and Firewalls - Summary

## Key Definitions and Concepts

- **Network Attack**: Any deliberate attempt to compromise the confidentiality, integrity, or availability of network resources and data.
- **DoS (Denial of Service)**: Attack that overwhelms target systems with traffic, making them unavailable to legitimate users.
- **DDoS (Distributed Denial of Service)**: Coordinated attack using multiple compromised systems (botnet) to overwhelm target.
- **MITM (Man-in-the-Middle)**: Attack where attacker secretly intercepts communications between two parties.
- **SQL Injection**: Code injection attack targeting database queries through unsanitized user input.
- **XSS (Cross-Site Scripting)**: Injection of malicious scripts into web pages viewed by other users.
- **Firewall**: Network security device that monitors and controls incoming/outgoing traffic based on security rules.
- **DMZ (Demilitarized Zone)**: Network segment separating internal trusted network from external untrusted network.

## Important Formulas and Theorems

- **Defense in Depth**: Multiple layers of security controls provide better protection than single solutions.
- **Principle of Least Privilege**: Users and processes should have only minimum necessary access rights.
- **Implicit Deny**: Any traffic not explicitly allowed should be denied by default.

## Key Points

- Network attacks are classified as passive (monitoring) or active (modifying/altering systems).
- DoS attacks flood targets with traffic; DDoS uses botnets for amplified, distributed attacks.
- Firewall types: Packet filtering (Layer 3), Stateful inspection (Layer 4), Proxy (Layer 7), Next-Generation (multi-layer).
- Stateful firewalls maintain connection state tables and are more secure than stateless packet filters.
- DMZ architecture isolates public-facing services from internal networks.
- Application-layer attacks (SQLi, XSS) often bypass network firewalls, requiring application-level security.
- Firewall rule order matters—specific rules must precede general rules.
- Common defenses: SYN cookies for SYN flood, input validation for SQL injection, content sanitization for XSS.

## Common Mistakes to Avoid

- Confusing DoS with DDoS—remember the distributed nature of DDoS using botnets.
- Believing firewalls provide complete security—application-layer attacks can bypass them.
- Placing the firewall rule in wrong order—specific rules must come before general rules.
- Forgetting the implicit deny rule at the end of firewall configuration.
- Overlooking that proxy firewalls add latency but provide better content inspection.

## Revision Tips

1. Create a comparative table of firewall types, noting their OSI layer, advantages, and limitations.
2. For each major attack type, memorize at least one corresponding defense mechanism.
3. Practice drawing and explaining DMZ architecture—frequently asked in exams.
4. Remember the sequence: Reconnaissance → Scanning → Gaining Access → Maintaining Access → Covering Tracks.
5. Review past DU question papers to understand the pattern and depth of questions asked on this topic.