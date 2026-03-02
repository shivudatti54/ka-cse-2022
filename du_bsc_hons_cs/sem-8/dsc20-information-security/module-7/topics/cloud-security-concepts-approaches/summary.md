# Cloud Security Concepts and Approaches - Summary

## Key Definitions and Concepts

- **Cloud Computing:** On-demand network access to shared configurable computing resources with minimal management effort (NIST definition).
- **IaaS (Infrastructure as a Service):** Provides virtualized computing resources; customer manages OS, applications, and data.
- **PaaS (Platform as a Service):** Provides development/deployment environment; provider manages infrastructure, customer manages applications and data.
- **SaaS (Software as a Service):** Delivers software applications; provider manages nearly all security aspects.
- **Shared Responsibility Model:** Security obligations divided between cloud provider and customer based on service model.
- **Zero Trust Security:** "Never trust, always verify" approach requiring continuous authentication and authorization.
- **CSPM (Cloud Security Posture Management):** Tools that continuously monitor and remediate cloud misconfigurations.

## Important Formulas and Theorems

There are no specific formulas in this topic, but the following principles guide implementation:

- **Least Privilege Principle:** Users should have only the minimum access required for their job functions
- **Defense in Depth:** Multiple layers of security controls protecting each asset
- **Zero Trust Principles:** Verify explicitly, use least privilege access, assume breach

## Key Points

- Cloud service models (IaaS, PaaS, SaaS) define different security responsibility boundaries between provider and customer
- In IaaS, customers bear maximum security responsibility; in SaaS, providers manage most security aspects
- Major cloud security challenges include data breaches, insecure APIs, identity theft, lack of visibility, and compliance complexity
- Zero Trust architecture has become the foundational approach for cloud security
- Encryption (at rest and in transit) is mandatory for protecting sensitive cloud data
- Multi-factor authentication should be enforced for all cloud access points
- CSPM tools help identify and remediate cloud misconfigurations automatically
- Compliance frameworks like SOC 2, ISO 27001, and CSA STAR provide security assurance for cloud services
- Common breaches result from misconfigurations rather than provider failures
- Incident response procedures must account for cloud-specific forensic and retention capabilities

## Common Mistakes to Avoid

- Assuming the cloud provider secures everything—misunderstanding the shared responsibility model is the most frequent error
- Using root accounts for daily operations instead of IAM users with specific roles
- Enabling public access to storage buckets without proper validation
- Neglecting to implement MFA for administrative access
- Failing to configure logging and monitoring in cloud environments
- Not understanding data residency and compliance requirements for specific geographic regions

## Revision Tips

1. Create a comparison table showing IaaS, PaaS, and SaaS with their respective security responsibilities clearly listed
2. Practice explaining the shared responsibility model until you can do so confidently in exam conditions
3. Review real cloud security incidents (Capital One, Google Docs exposure) to understand practical implications
4. Memorize the five core Zero Trust principles and be able to explain each with examples
5. Understand the difference between encryption at rest versus in transit and when each applies
6. Focus on understanding "why" certain controls are important rather than just memorizing lists