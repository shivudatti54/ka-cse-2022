# Identity and Credential Management - Summary

## Key Definitions and Concepts

- **Digital Identity**: Collection of attributes (username, role, biometrics) representing a user in digital systems
- **Authentication Factors**: Something you know (password), something you have (token), something you are (biometrics)
- **Credential**: Evidence verifying identity—passwords, certificates, tokens, biometric templates
- **RBAC**: Role-Based Access Control—assigning permissions to roles rather than individual users
- **Identity Federation**: Cross-organizational trust enabling SSO using protocols like SAML, OAuth, OIDC

## Important Formulas and Techniques

- **Password Hashing**: Use bcrypt, Argon2, or PBKDF2 with salt; never store plaintext
- **Key Derivation**: Iterative hashing (PBKDF2 uses 100,000+ iterations) to increase attack cost
- **Session Security**: Regenerate session ID after authentication; set secure, HttpOnly cookies

## Key Points

- Identity management answers "who are you?", authentication proves "are you really who?", authorization determines "what can you access?"
- Multi-factor authentication combining different factor types provides significantly stronger security than single-factor
- Password storage must use salted hashes via modern algorithms—SHA-256 alone is insufficient
- RBAC simplifies administration by managing permissions through roles rather than individual users
- OAuth 2.0 provides authorization, OpenID Connect adds authentication layer on OAuth
- Credential lifecycle includes creation, secure storage, rotation, and prompt revocation upon termination
- Common attacks include phishing, credential stuffing, brute-force, and man-in-the-middle—mitigate through MFA, rate limiting, and secure protocols

## Common Mistakes to Avoid

- Confusing authentication with authorization—these are distinct security concepts
- Storing passwords with simple hashing without salting—vulnerable to rainbow table attacks
- Using SMS-based 2FA—vulnerable to SIM swapping attacks
- Failing to revoke credentials immediately upon employee termination
- Implementing security questions as sole recovery mechanism—easily bypassed through social engineering

## Revision Tips

1. Create a comparison table of authentication factors, their security strengths, and vulnerabilities
2. Practice drawing OAuth 2.0 and OpenID Connect authorization flows—frequently tested in exams
3. Remember: RBAC assigns permissions to roles, users are assigned roles—distinguish this from ABAC which uses attributes
4. Review recent security breaches related to credential theft to understand real-world implications
5. Memorize key properties: bcrypt includes salt, Argon2 is memory-hard, PBKDF2 is iterative—all resist brute-force