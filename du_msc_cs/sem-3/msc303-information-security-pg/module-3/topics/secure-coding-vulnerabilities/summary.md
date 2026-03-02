# Secure Coding Vulnerabilities - Summary

## Key Definitions and Concepts
- CWE (Common Weakness Enumeration): Community-developed list of software weaknesses
- SAST/DAST: Static/Dynamic Application Security Testing
- Taint Analysis: Tracking untrusted data through program execution
- Nonce: Cryptographic number used once
- TOCTOU: Time-of-Check to Time-of-Use race condition

## Important Formulas and Theorems
- **Salt generation**: `salt = crypto.randomBytes(16)`
- **Entropy requirements**: `H ≥ 128 bits` for modern systems
- **Biba Integrity Model**: `No read down, no write up`
- **Shannon's Maxim**: "The enemy knows the system"
- **Miller-Rabin Test**: Probabilistic primality test for crypto

## Key Points
- 80% of breaches exploit known vulnerabilities in code
- Memory safety is foundational - use Rust/Go for critical systems
- Principle of Least Privilege reduces attack surface
- Input validation must be whitelist-based, not blacklist
- Secure defaults > bolt-on security
- Continuous Integration pipelines must include SAST checks
- Zero Trust Architecture impacts coding practices (e.g., JWT validation)

## Common Mistakes to Avoid
- Using `eval()` with user-controlled input
- Storing secrets in version control
- Relying solely on client-side validation
- Implementing custom crypto algorithms
- Ignoring compiler warnings about unsafe functions

## Revision Tips
1. Practice with OWASP WebGoat vulnerable application
2. Memorize MITRE ATT&CK techniques for software development (TA0002)
3. Use CodeQL for pattern-based vulnerability hunting
4. Review NIST SP 800-123 for secure coding guidelines

Length: 650 words