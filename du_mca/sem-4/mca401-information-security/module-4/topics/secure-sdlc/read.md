# Secure Software Development Life Cycle (SDLC)

## Introduction
Secure SDLC is a systematic approach integrating security practices throughout software development phases. Unlike traditional SDLC which treats security as an afterthought, Secure SDLC embeds security controls from requirements gathering to maintenance. With 84% of software breaches originating from application layer vulnerabilities (OWASP 2023), this methodology is critical for developing robust systems.

The process aligns with major security standards like ISO 27001 and NIST SP 800-64. For MCA students, understanding Secure SDLC is crucial as organizations face increasing regulatory pressures (GDPR, DPDP Act 2023) and sophisticated cyber threats. Real-world implementations have shown 40% reduction in vulnerabilities when adopted early (IBM Cost of Data Breach Report 2023).

## Key Concepts
1. **Security Requirements Analysis**: 
   - Identify confidentiality, integrity, and availability (CIA) requirements
   - Use security user stories and abuse cases
   - Example: "As a user, I want MFA to prevent unauthorized access"

2. **Threat Modeling (Design Phase)**:
   - STRIDE methodology (Spoofing, Tampering, Repudiation, Info Disclosure, DoS, Elevation of Privilege)
   - DFD-based analysis using tools like Microsoft Threat Modeling Tool

3. **Secure Coding Practices**:
   - OWASP Top 10 mitigation (SQLi, XSS, CSRF)
   - Memory-safe languages (Rust, Go)
   - Static Application Security Testing (SAST) using SonarQube

4. **Security Testing**:
   - Dynamic Analysis (DAST) with OWASP ZAP
   - Penetration testing frameworks (PTES)
   - Fuzz testing using AFL

5. **Secure Deployment**:
   - Infrastructure as Code (IaC) security with Checkov
   - Container security scanning (Trivy)
   - Runtime Application Self-Protection (RASP)

## Examples

**Example 1: Banking Application Threat Modeling**
```
Problem: Design auth system for mobile banking
Solution:
1. Create DFD for login flow
2. Identify threats using STRIDE:
   - Spoofing: Fake login screen
   - Tampering: Credential interception
3. Controls: Implement FIDO2 WebAuthn + TLS 1.3
```

**Example 2: E-Commerce SAST Integration**
```
Problem: Prevent SQLi in product search
Solution:
1. Add SAST to CI/CD pipeline
2. Rule: Detect unsanitized inputs
3. Code Fix:
   // Vulnerable
   query = "SELECT * FROM products WHERE name = '" + input + "'";
   
   // Secure
   use parameterized queries with PDO
```

**Example 3: Healthcare App Incident Response**
```
Problem: Ransomware attack during maintenance
Process:
1. Isolate affected systems
2. Activate DR plan from SDLC documentation
3. Forensic analysis using audit logs
4. Patch CVE-2023-12345 identified in RCA
```

## Exam Tips
1. Compare and contrast traditional SDLC vs Secure SDLC phases
2. Draw and explain DFD for threat modeling scenarios
3. Write secure code snippets for common vulnerabilities
4. Interpret SAST/DAST report findings
5. Design compliance checklist for GDPR-aware SDLC
6. Explain DevSecOps toolchain components
7. Case study analysis of real breaches (Equifax, Log4j)

Length: 1500-3000 words, MCA (Master of Computer Applications) PG level