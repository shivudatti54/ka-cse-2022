# Web Security: OWASP - Summary

## Key Definitions and Concepts
- **OWASP**: Open community improving software security through projects/tools
- **Top 10**: Prioritized list of critical web app security risks
- **ASVS**: Standard containing security requirements for app verification
- **WSTG**: Comprehensive manual for web app penetration testing
- **CSP**: Content Security Policy mitigates XSS/data injection

## Important Formulas and Theorems
- **Session ID Entropy**: H = log2(N^L) where N=character set size, L=length
- **CSP Header Syntax**: `Content-Security-Policy: <directive> <source>`
- **Password Complexity**: Minimum 12 chars with 4 character types (NIST 800-63B)

## Key Points
- Injection flaws remain #1 risk in OWASP Top 2021
- ASVS Level 2 requires threat modeling and secure design principles
- ZAP's AJAX Spider effectively crawls modern SPAs
- Secure cookies require HttpOnly, Secure, SameSite attributes
- 78% of apps have at least one flaw in OWASP Top 10 (2023 Data)
- SAMM defines 4 maturity levels across 15 security practices
- India's CERT-In mandates OWASP compliance for critical infrastructure

## Common Mistakes to Avoid
- Confusing XSS prevention (output encoding) with SQLi prevention (parameterization)
- Overlooking third-party dependencies in software composition analysis
- Using weak RNGs (like `Math.random()`) for cryptographic operations
- Missing `Secure` flag on cookies when using HTTPS

## Revision Tips
1. Create flashcards for OWASP Top 10 risks → mitigations
2. Practice writing CSP headers for different scenarios
3. Use OWASP Cheat Sheets for quick code references
4. Analyze NSE 5.0 sample questions on web security
5. Set up ZAP and test DU's student portal (ethical hacking)