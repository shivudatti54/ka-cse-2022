# Security Concepts, Threats, and Attacks - Summary

## Key Definitions and Concepts

- **CIA Triad**: The three foundational principles of information security—Confidentiality (preventing unauthorized access), Integrity (ensuring accuracy and completeness), and Availability (ensuring timely access to information).

- **Authentication**: The process of verifying the identity of a user, system, or entity through credentials like passwords, biometrics, or tokens.

- **Authorization**: Determining what actions an authenticated user is permitted to perform and what resources they can access.

- **Non-repudiation**: Assurance that parties cannot deny their actions or transactions—achieved through digital signatures and audit logs.

- **Threat**: Any potential occurrence that could harm an information system by exploiting vulnerabilities.

- **Vulnerability**: A weakness or flaw in a system's design, implementation, or configuration that can be exploited.

- **Attack**: The actual exploitation of a vulnerability to compromise security.

## Important Formulas and Theorems

- **Attack Surface**: The sum of all entry points (vectors) that attackers can exploit in a system. Reducing the attack surface through network segmentation, firewalls, and disabling unnecessary services enhances security.

- **Security Attack Lifecycle**: Reconnaissance → Scanning → Gaining Access → Maintaining Access → Covering Tracks → Exfiltration.

## Key Points

- The CIA Triad remains the cornerstone model for information security, though modern frameworks expand upon it.

- Threats can originate from internal (insiders) or external (hackers, criminal organizations) sources.

- Malware includes viruses, worms, trojans, ransomware, and spyware—each with distinct propagation and malicious behavior patterns.

- Social engineering exploits human psychology rather than technical vulnerabilities, making technical controls insufficient.

- Passive attacks (eavesdropping) are difficult to detect; active attacks (modification, disruption) cause more damage but are more detectable.

- Common attack vectors include email, websites, USB devices, network connections, and software vulnerabilities.

- SQL injection exploits unsanitized user input in database queries and can be prevented through parameterized queries.

## Common Mistakes to Avoid

1. **Confusing authentication with authorization**: Remember—authentication verifies identity, authorization defines permissions.

2. **Ignoring the human element**: Technical controls alone cannot prevent social engineering attacks; security awareness training is essential.

3. **Underestimating internal threats**: Insiders with legitimate access pose significant risks that external security measures cannot address.

4. **Assuming prevention is sufficient**: Modern security requires detection, response, and recovery capabilities alongside preventive controls.

## Revision Tips

1. Create a comparative table of different attack types (phishing vs vishing vs smishing), (virus vs worm vs trojan), and (DoS vs DDoS).

2. Practice mapping real-world security incidents to the CIA Triad components they violate.

3. Memorize the attack lifecycle sequence—exam questions often ask you to identify stages or suggest countermeasures for each stage.

4. Review case studies of major attacks (WannaCry, Equifax breach, SolarWinds) and identify which concepts they illustrate.