# Security Policies and Models - Summary

## Key Definitions and Concepts

- **Security Policy:** A formal statement of rules and practices defining how an organization protects its information assets
- **Security Model:** A formal mathematical/logical representation of security requirements and enforcement mechanisms
- **Bell-LaPadula Model:** A confidentiality-focused model based on mandatory access control with security labels
- **Biba Model:** An integrity-focused model preventing unauthorized modification of data
- **Clark-Wilson Model:** A commercial integrity model using well-formed transactions and separation of duties
- **Access Control Matrix:** A fundamental model representing rights between subjects (rows) and objects (columns)

## Important Properties

**Bell-LaPadula (Confidentiality):**
- Simple Security Property: No read up (subject level ≥ object level)
- Star Property: No write down (object level ≥ subject level)

**Biba (Integrity):**
- Simple Integrity Property: No read down (subject level ≤ object level)
- Star Integrity Property: No write up (object level ≥ subject level)

## Key Points

- Security policies are hierarchical, ranging from enterprise-level to system-specific policies
- Bell-LaPadula prevents unauthorized disclosure of confidential information in military/government systems
- Biba prevents unauthorized modification of data by ensuring data integrity levels
- Clark-Wilson uses Transformation Procedures (TPs) to maintain integrity through certified operations
- The Access Control Matrix is conceptually simple but scalable implementations use ACLs or capability lists
- Real-world systems may combine multiple models or use components from each

## Common Mistakes to Avoid

- Confusing the direction of the properties in Bell-LaPadula (reading goes up, writing goes down)
- Confusing Bell-LaPadula with Biba — remember: Bell-LaPadula = Confidentiality (Ladder), Biba = Integrity (Food chain analogy)
- Treating security policies and security models as the same thing — policies are organizational rules, models are technical implementations
- Forgetting that Clark-Wilson is designed for commercial applications, not military systems

## Revision Tips

1. Create a comparison table between Bell-LaPadula and Biba models, noting their purposes, properties, and directions of allowed access
2. Practice mapping real-world scenarios to appropriate security models (e.g., banking systems → Clark-Wilson)
3. Remember the hierarchy: Bell-LaPadula read direction flows up the hierarchy, write flows down; Biba is the opposite
4. Review the components of a security policy and be able to list them from memory