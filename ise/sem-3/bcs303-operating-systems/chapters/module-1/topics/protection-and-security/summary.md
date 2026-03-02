# Protection and Security - Summary

## Key Definitions and Concepts

- Protection: Internal OS mechanisms controlling access to resources by users and processes
- Security: External measures defending against unauthorized access and external threats
- Access Matrix: Two-dimensional model defining rights subjects have over objects
- Access Control Lists (ACLs): Object-centric protection storing permissions with each resource
- Capability Lists: Subject-centric protection storing authorized resources with each user
- Authentication: Verifying user identity through passwords, biometrics, or tokens
- Authorization: Determining permitted actions for authenticated users
- Encryption: Transforming data to prevent unauthorized reading without decryption keys

## Important Formulas and Techniques

- UNIX permission bits: Read=4, Write=2, Execute=1 (owner/group/others)
- Access matrix verification: Check subject-object pair for requested right
- Bell-LaPadula: No read up, No write down (confidentiality)
- Biba Model: No read down, No write up (integrity)

## Key Points

- Protection operates internally within the OS; security handles external threats
- ACLs simplify revocation but increase lookup overhead; capabilities provide faster access checking but complicate revocation
- Multi-factor authentication combines multiple verification methods for enhanced security
- The principle of least privilege minimizes damage by granting minimum necessary permissions
- The Bell-LaPadula model prioritizes confidentiality for military/government applications
- The Biba model prioritizes integrity, preventing contamination of trusted data
- UNIX file permissions follow owner-group-others hierarchy with read-write-execute bits
- Defense in depth combines multiple security layers for comprehensive protection

## Common Mistakes to Avoid

- Confusing protection with security; they address different threat models
- Confusing authentication (who you are) with authorization (what you can do)
- Believing encryption alone provides complete security; key management is equally important
- Underestimating the importance of user education in security implementation

## Revision Tips

- Create comparison tables for ACLs vs capabilities, Bell-LaPadula vs Biba
- Practice interpreting UNIX permission strings (rwxr-x---) and determining access outcomes
- Memorize the core principles: least privilege, separation of privilege, defense in depth
- Review how modern OSes (Linux, Windows) implement these concepts differently