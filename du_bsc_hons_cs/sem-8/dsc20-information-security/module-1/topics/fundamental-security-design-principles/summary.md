# Fundamental Security Design Principles - Summary

## Key Definitions and Concepts

- **CIA Triad**: Core security model consisting of Confidentiality (data protection from unauthorized access), Integrity (accuracy and completeness of data), and Availability (reliable authorized access)
- **Least Privilege**: Users and processes receive minimum permissions necessary for their function
- **Defense in Depth**: Multiple layered security controls where if one fails, others provide protection
- **Separation of Duties**: Critical tasks divided among multiple entities to prevent fraud and error
- **Fail Secure**: Systems default to deny access when errors occur
- **Complete Mediation**: Every resource access is validated against security policy
- **Economy of Mechanism**: Security mechanisms should be as simple as possible
- **Open Design/Kerckhoffs's Principle**: Security relies on secret keys, not secret algorithms
- **Least Common Mechanism**: Minimize sharing of mechanisms between users to prevent covert channels
- **Psychological Acceptability**: Security should not unnecessarily impede legitimate users

## Important Formulas and Theorems

There are no mathematical formulas in this topic, but key theorems include:
- **Kerckhoffs's Principle**: "The security of a cryptographic system should depend only on keeping the key secret"
- **Defense in Depth Strategy**: Layered security = Perimeter + Network + Host + Application + Data

## Key Points

- CIA Triad forms the foundation of all security considerations
- No single security measure is sufficient—multiple layers provide robust defense
- Fail secure systems deny access by default; fail open systems allow access by default
- Security through obscurity is fundamentally flawed—algorithms should be open for review
- Complete mediation prevents bypass attacks by checking authorization every time
- Complex security mechanisms are more likely to contain vulnerabilities
- User cooperation requires security measures that don't severely impact usability

## Common Mistakes to Avoid

- Confusing least privilege with separation of duties
- Confusing fail secure with fail open (remember: secure = closed = deny)
- Believing that obscurity provides real security
- Implementing single-point security rather than layered defense
- Assuming one security measure is sufficient

## Revision Tips

1. Create a comparison table of all 10 principles with definitions
2. Practice identifying principles in given scenarios
3. Remember: "fail secure" = "fail closed" = default deny
4. Connect real security breaches to principle violations
5. Focus on understanding WHY each principle exists, not just memorizing definitions