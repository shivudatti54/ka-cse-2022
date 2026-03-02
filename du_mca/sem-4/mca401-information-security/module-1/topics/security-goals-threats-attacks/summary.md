# Security Goals, Threats, and Attacks - Summary

## Key Definitions and Concepts

- **CIA Triad**: The three fundamental security goals—Confidentiality (preventing unauthorized access), Integrity (ensuring data accuracy), and Availability (ensuring timely access to data).

- **Threat Agent**: Individuals, groups, or entities that cause harm to systems, including insiders, hackers, cybercriminals, nation-states, and malware authors.

- **Attack**: An actual attempt to exploit a vulnerability, categorized as passive (information gathering) or active (system modification/disruption).

- **Vulnerability**: A weakness in system design, implementation, or controls that can be exploited by threats.

- **Risk**: The potential for loss or damage when a threat exploits a vulnerability; calculated as Risk = Threat × Vulnerability × Impact.

## Important Formulas and Relationships

- **Risk Assessment**: Risk = Probability of threat × Potential impact
- **Security Controls**: Mitigate risks by addressing threats, vulnerabilities, or impacts
- **Defense-in-Depth**: Multiple security layers providing redundancy when one fails

## Key Points

- Confidentiality ensures only authorized access; achieved through encryption, access controls, and data classification.
- Integrity guarantees data accuracy and unaltered state; maintained through hashing, checksums, and digital signatures.
- Availability ensures continuous access to resources; protected through redundancy, backups, and DoS mitigation.
- Authentication verifies identity (something you know, have, or are); authorization determines permitted actions.
- Passive attacks gather information without modification; active attacks modify systems or disrupt services.
- Human threats (social engineering, phishing) remain the weakest security link despite technical controls.
- Zero-day exploits target unknown vulnerabilities before patches are available.
- Insider threats bypass perimeter security and cause significant damage due to legitimate access.

## Common Mistakes to Avoid

1. Confusing authentication with authorization—knowing who someone is versus what they can access.
2. Assuming technical controls alone provide sufficient security—human factors are critical.
3. Treating threats and attacks as identical—they differ in that threats are potential, attacks are actual.
4. Overlooking physical security—physical access often bypasses all technical controls.
5. Implementing security without considering usability—overly restrictive controls lead to workarounds.

## Revision Tips

1. Create a matrix mapping attacks to affected CIA triad components for quick recall.
2. Memorize real-world attack examples (phishing, SQL injection, DDoS) and how they work.
3. Practice scenario-based questions by identifying threats, vulnerabilities, and affected security goals.
4. Review case studies of major breaches (Equifax, SolarWinds) to understand attack vectors.
5. Focus on understanding relationships between concepts rather than rote memorization.