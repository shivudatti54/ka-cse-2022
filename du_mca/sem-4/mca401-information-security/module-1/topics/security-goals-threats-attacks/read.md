# Security Goals, Threats, and Attacks

## Introduction
Information security forms the backbone of modern digital systems. With increasing cyber threats, understanding security goals (CIA triad), threat vectors, and attack methodologies is critical for designing robust systems. For MCA students at DU, this knowledge is essential for careers in cybersecurity, system architecture, and IT governance.

The CIA triad - Confidentiality, Integrity, and Availability - serves as the foundation for security frameworks. Threats like malware, phishing, and insider risks exploit system vulnerabilities, while attacks such as DDoS and SQL injection target these weaknesses. Recent incidents like the AIIMS ransomware attack (2022) demonstrate real-world impacts of security breaches.

This topic bridges theoretical concepts with practical implementations. Students will learn to analyze attack surfaces, implement security controls, and develop threat mitigation strategies aligned with industry standards like ISO 27001 and NIST frameworks.

## Key Concepts
1. **Security Goals (CIA Triad):**
   - **Confidentiality:** Ensuring data access only to authorized entities (e.g., encryption)
   - **Integrity:** Maintaining data accuracy and consistency (e.g., hash functions)
   - **Availability:** Guaranteeing resource accessibility (e.g., redundancy)

2. **Threats:**
   - **Passive Threats:** Eavesdropping, traffic analysis
   - **Active Threats:** Masquerade, replay attacks
   - **Insider Threats:** Privilege misuse by employees

3. **Attack Types:**
   - **Interruption:** DoS attacks disrupting services
   - **Interception:** Man-in-the-middle attacks
   - **Modification:** Data tampering in transit
   - **Fabrication:** Fake data insertion

4. **Attack Vectors:**
   - Phishing emails
   - Malware (worms, trojans)
   - Zero-day exploits
   - Social engineering

## Examples

**Example 1: Eavesdropping Attack**
*Scenario:* Alice sends encrypted credit card details to Bob. Eve intercepts the communication.
*Solution:*
1. Implement TLS 1.3 for encrypted channels
2. Use certificate pinning
3. Monitor for abnormal traffic patterns

**Example 2: SQL Injection**
*Scenario:* Attacker inputs `' OR 1=1;--` into login form
*Mitigation:*
1. Parameterized queries: 
   ```python
   cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
   ```
2. Web Application Firewalls (WAF)
3. Regular vulnerability scanning

**Example 3: DDoS Mitigation**
*Scenario:* A university portal faces 10 Gbps traffic flood
*Response:*
1. Deploy cloud-based scrubbing centers
2. Configure BGP flowspec
3. Implement rate limiting on edge routers

## Exam Tips
1. Always define CIA triad first in 5-mark questions
2. Differentiate between threats (potential dangers) and attacks (executed actions)
3. Use NIST SP 800-30 framework for risk assessment questions
4. For case studies, follow STRIDE model (Spoofing, Tampering, Repudiation, etc.)
5. Memorize OWASP Top 10 attack vectors for application security questions
6. Compare symmetric vs asymmetric encryption in context of confidentiality
7. Discuss Kerckhoffs' Principle when analyzing system security

Length: 2200 words, MCA PG level