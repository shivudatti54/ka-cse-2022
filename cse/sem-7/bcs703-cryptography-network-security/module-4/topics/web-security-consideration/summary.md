# Web Security Considerations - Summary

## Key Definitions

- **XSS (Cross-Site Scripting)**: Attacks injecting malicious scripts into web pages viewed by other users, exploiting unvalidated user input inclusion.
- **SQL Injection**: Code injection technique exploiting unsanitized database queries to manipulate application data or execute unauthorized commands.
- **CSRF (Cross-Site Request Forgery)**: Attack tricking authenticated users into submitting malicious requests without their consent.
- **Session Hijacking**: Unauthorized acquisition of valid session identifiers to impersonate legitimate users.
- **TLS (Transport Layer Security)**: Cryptographic protocol providing encryption, authentication, and data integrity for network communications.
- **CSP (Content Security Policy)**: HTTP header controlling resource loading to prevent XSS and data injection attacks.

## Important Formulas

- **Cookie Security Attributes**: Secure + HttpOnly + SameSite (Strict/Lax) + Path + Max-Age
- **TLS Handshake**: ClientHello → ServerHello → Certificate → Key Exchange → Finished
- **XSS Prevention**: Input Validation + Context-Aware Output Encoding + CSP Implementation
- **SQL Injection Prevention**: Parameterized Queries + Stored Procedures + Least Privilege

## Key Points

1. HTTP transmits all data in plaintext, requiring TLS encryption for secure communication.
2. Cookie security requires the Secure, HttpOnly, and SameSite attributes to prevent theft and CSRF attacks.
3. XSS attacks exploit insufficient input validation and improper output encoding—defense requires multiple layers.
4. Parameterized queries eliminate SQL injection vulnerabilities by separating code from data.
5. CSRF attacks exploit browser behavior sending authentication credentials automatically with requests.
6. Multi-factor authentication significantly reduces risk from credential theft compared to password-only systems.
7. Content Security Policy provides declarative control over acceptable content sources, reducing attack surfaces.
8. Perfect Forward Secrecy ensures session keys cannot be compromised even if long-term keys are exposed.
9. Regular security assessments and penetration testing are essential for identifying vulnerabilities.
10. Defense-in-depth strategies implement multiple overlapping security controls for comprehensive protection.

## Common Mistakes

1. **Assuming HTTPS alone is sufficient**: TLS must be properly configured with strong ciphers and valid certificates—misconfiguration creates false security.

2. **Relying solely on input validation for XSS prevention**: Input validation is easily bypassed; output encoding and CSP provide necessary defense layers.

3. **Using string concatenation for SQL queries**: This creates injection vulnerabilities regardless of input sanitization attempts.

4. **Ignoring cookie expiration**: Persistent cookies with excessive lifespans increase exposure to session hijacking.

5. **Implementing custom cryptographic solutions**: Using non-standard or proprietary security mechanisms often introduces vulnerabilities compared to established protocols.

6. **Neglecting third-party dependencies**: Web applications frequently incorporate vulnerable libraries requiring regular updates and security patches.