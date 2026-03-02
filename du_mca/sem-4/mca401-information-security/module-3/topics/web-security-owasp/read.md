# Web Security: OWASP Fundamentals

## Introduction
The Open Web Application Security Project (OWASP) is a nonprofit foundation driving global improvement in web application security. Established in 2001, OWASP provides freely available resources including documentation, tools, and community-led projects. Its flagship OWASP Top 10 list identifies critical security risks for web applications, making it essential reading for developers and security professionals.

With 94% of applications having some form of vulnerability (Veracode State of Software Security 2023), understanding OWASP standards is crucial for MCA students. The OWASP Web Security Testing Guide (WSTG) and Application Security Verification Standard (ASVS) form industry benchmarks for secure development and penetration testing.

For DU students, mastering OWASP concepts bridges academic knowledge with real-world security challenges. Major Indian organizations like UPI, Aadhaar, and GSTN mandate OWASP compliance, making this knowledge vital for careers in fintech, e-governance, and enterprise software development.

## Key Concepts
1. **OWASP Top 10 2021**:  
   - Current ranking: Injection → Broken Auth → Cryptographic Failures → Insecure Design → Security Misconfigurations → Vulnerable Components → Identification Failures → Software/Data Integrity Failures → Security Logging → SSRF  
   - Each risk includes likelihood/impact scores, example vulnerabilities, and prevention techniques

2. **Web Security Testing Guide (WSTG)**:  
   - 4-phase testing methodology: Information Gathering → Configuration Management → Authentication Testing → Business Logic Testing  
   - Contains 91 specific test cases with exploitation techniques

3. **Application Security Verification Standard (ASVS)**:  
   - 3 verification levels: L1 (opportunistic) → L2 (standard) → L3 (advanced)  
   - 14 security domains covering architecture, crypto, IAM, etc.

4. **OWASP Tools**:  
   - ZAP (Zed Attack Proxy): Automated scanner for finding vulnerabilities  
   - Dependency-Check: SCA tool for identifying vulnerable libraries  
   - Amass: Attack surface mapping tool

5. **Secure SDLC**:  
   - OWASP SAMM (Software Assurance Maturity Model) framework  
   - Integration of security into requirements, design, implementation, verification

## Examples
**Example 1: SQL Injection Mitigation**  
*Scenario*: A login form takes username/password and executes:  
`SELECT * FROM users WHERE username='$user' AND password='$pass'`

*Vulnerability*: Attacker inputs `admin'--` as username, bypassing password check

*Solution*:  
1. Use parameterized queries:  
   ```python
   cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (user, pass))
   ```
2. Implement input validation using regex: `^[a-zA-Z0-9]{5,12}$`

**Example 2: Broken Authentication**  
*Scenario*: Session IDs in URL parameters:  
`https://example.com/dashboard?sessionid=1234`

*Vulnerability*: Session fixation attack via URL sharing

*Solution*:  
1. Generate secure session IDs using CSPRNG:  
   ```java
   SecureRandom random = new SecureRandom();
   byte[] bytes = new byte[16];
   random.nextBytes(bytes);
   String sessionId = Base64.getEncoder().encodeToString(bytes);
   ```
2. Set `HttpOnly` and `Secure` flags on cookies

**Example 3: XSS Prevention**  
*Scenario*: User profile page displays unsanitized input:  
`<div>Hello, <%= request.getParameter("name") %></div>`

*Vulnerability*: Attacker injects `<script>alert(1)</script>`

*Solution*:  
1. Contextual output encoding:  
   ```html
   <div>Hello, ${fn:escapeXml(param.name)}</div>
   ```
2. Implement Content Security Policy:  
   `Content-Security-Policy: default-src 'self'`

## Exam Tips
1. Memorize OWASP Top 10 2021 order and primary mitigation techniques
2. Understand ASVS verification levels - L1 vs L2 vs L3 requirements
3. Practice writing secure code snippets for common vulnerabilities
4. Study real-world breaches linked to OWASP risks (Equifax - Vulnerable Components)
5. Know WSTG testing methodology phases and key test cases
6. Be prepared to compare OWASP tools (ZAP vs Burp Suite)
7. Understand SAMM maturity levels for SDLC implementation