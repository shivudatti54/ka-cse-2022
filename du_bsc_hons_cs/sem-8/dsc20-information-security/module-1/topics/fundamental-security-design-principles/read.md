# Fundamental Security Design Principles

## Introduction

Information security is not merely a technical concern but a fundamental aspect of modern computing systems that protects data, maintains privacy, and ensures business continuity. As we navigate an increasingly interconnected digital world, understanding the foundational principles that guide secure system design has become essential for every computer science professional.

The fundamental security design principles, often called "security design principles" or "security engineering principles," provide a systematic framework for building secure systems. These principles have evolved through decades of research, real-world security breaches, and lessons learned from both successful protections and catastrophic failures. Originally articulated by researchers like Jerome Saltzer and Michael Schroeder in their seminal 1975 paper "Protection and the Security Kernel," these principles remain remarkably relevant today, serving as the cornerstone of modern security architecture.

For students preparing for DU examinations, mastering these principles is crucial not only for answering theoretical questions but also for developing the security mindset required in professional practice. Whether designing a simple web application or architecting enterprise-level systems, these principles provide the logical foundation for making informed security decisions.

## Key Concepts

### The CIA Triad

The CIA Triad forms the foundation of information security and comprises three core principles:

**Confidentiality** ensures that information is accessible only to authorized individuals and protected from unauthorized disclosure. This encompasses data classification, access controls, encryption, and proper data handling procedures. For example, patient medical records must remain confidential between healthcare providers and patients.

**Integrity** guarantees that information remains accurate, complete, and unaltered except through authorized changes. This involves mechanisms like checksums, digital signatures, and audit logs that detect and prevent unauthorized modifications to data.

**Availability** ensures that authorized users have reliable access to information and associated resources when needed. This includes redundancy, fault tolerance, denial-of-service protection, and proper maintenance procedures.

### Principle of Least Privilege

The principle of least privilege states that every component, user, and process should operate using the minimum privileges necessary to complete its task. This limits the potential damage from accidental errors, malicious activity, or compromised accounts.

In practice, this means database administrators should not have access to financial systems, developers should not have production server access without justification, and processes should run with restricted permissions rather than administrative rights.

### Defense in Depth

Defense in depth implements multiple layers of security controls throughout a system. If one security mechanism fails, additional layers continue to provide protection. This approach recognizes that no single security measure is foolproof and that overlapping defenses create more robust security.

A practical example includes combining network firewalls, intrusion detection systems, application-level filtering, encryption, access controls, and user authentication—all working together to protect sensitive data.

### Separation of Duties

This principle requires that critical tasks be divided among multiple individuals or processes so that no single entity has complete control over a sensitive operation. This prevents fraud, error, and abuse by ensuring accountability through shared responsibility.

In banking systems, for example, a single employee cannot both approve a loan and disburse funds. Similarly, in software deployment, different personnel might handle code review, testing, and production deployment.

### Fail Secure

Systems should fail in a secure manner, defaulting to a state that denies access when errors occur. Rather than granting access upon failure, secure systems assume that any malfunction could indicate an attack and respond conservatively.

When a firewall encounters an unrecognized packet, it should drop (deny) the packet rather than allow it. When an authentication system fails, it should deny access rather than grant temporary access.

### Economy of Mechanism

Security mechanisms should be as simple as possible. Complex security designs are more likely to contain vulnerabilities, are harder to analyze, and are more prone to configuration errors. "Keep it simple" applies directly to security architecture.

### Complete Mediation

Every access to resources must be checked against the security policy. Systems must not rely on cached permissions or assume that once access is granted, it remains valid. Each request must be validated through the proper authorization mechanism.

### Open Design (Kerckhoffs's Principle)

The security of a system should depend on keeping keys secret, not on keeping the design secret. Security through obscurity—hiding the algorithm or design—is fundamentally flawed because secrets inevitably become known. Openly published and analyzed cryptographic algorithms are considered more secure because they have been subjected to extensive peer review.

### Least Common Mechanism

Sharing of mechanisms between users should be minimized, as it provides a potential path for information flow that could be exploited. Each user should have as isolated an environment as possible to prevent covert channels.

### Psychological Acceptability

Security mechanisms should not unnecessarily impede legitimate users. If security is too cumbersome, users will find ways to bypass it. Effective security requires user cooperation, which is achieved only when security measures are intuitive and do not significantly impact usability.

### Audit and Accountability

Systems should maintain logs of security-relevant events that allow reconstruction of activities and detection of intrusions. These logs must be protected from tampering and regularly reviewed.

## Examples

### Example 1: Banking Application Security Architecture

Consider designing a secure online banking application:

**Applying Least Privilege**: The web server runs with limited OS privileges, the database connection uses a service account with restricted database permissions, and each API key has specific scope limitations.

**Applying Defense in Depth**: Implement SSL/TLS encryption (transport layer), input validation and parameterized queries (application layer), database access controls (data layer), and network segmentation (infrastructure layer).

**Applying Separation of Duties**: Separate personnel handle:
- Transaction approval workflows
- System administration
- Audit log review
- Customer data access

**Applying Fail Secure**: If the session management system fails, all sessions are terminated rather than allowing anonymous access. If database connection fails, the application shows an error rather than bypassing authentication.

### Example 2: University Examination System

A DU examination portal implements security principles as follows:

**Confidentiality**: Student grades and personal information are encrypted using AES-256, with access restricted through role-based access control (RBAC).

**Complete Mediation**: Every page load verifies the user's session and permissions before displaying content. URLs cannot be manipulated to access other students' results.

**Psychological Acceptability**: The login process uses a simple single-sign-on rather than requiring multiple authentication factors for every action, while sensitive operations (grade changes) require additional verification.

**Audit Trail**: All access to examination papers, grade modifications, and administrative actions are logged with timestamps and user identification.

### Example 3: Corporate Network Security

A company implements defense in depth through multiple layers:
1. **Perimeter**: Firewall blocks unauthorized network traffic
2. **Network**: Intrusion detection system monitors for anomalies
3. **Segment**: VLANs separate sensitive departments
4. **Endpoint**: Antivirus and endpoint detection on workstations
5. **Data**: Encryption protects sensitive files at rest
6. **Application**: Web application firewall protects web services

If a phishing attack compromises an employee's workstation, the intrusion detection system may detect lateral movement, the network segmentation limits access to other systems, and encrypted data remains protected even if the attacker reaches the file servers.

## Exam Tips

1. **Understand CIA Triad thoroughly**: This appears frequently in exams. Be able to define each component and provide real-world examples for each.

2. **Differentiate between similar principles**: Students often confuse least privilege with separation of duties. Remember: least privilege limits what you can do; separation of duties divides what needs to be done.

3. **Know why "security through obscurity" is discouraged**: Connect this to Kerckhoffs's principle and the open design concept. Modern security relies on secret keys, not secret algorithms.

4. **Fail secure vs. fail open**: This is a common exam question. Remember that fail secure means default-deny, while fail open means default-allow—secure systems fail closed (deny).

5. **Apply principles to scenarios**: Exam questions often present scenarios asking which principle applies. Practice analyzing case studies and identifying the relevant principle.

6. **Defense in depth is always relevant**: This principle can be applied to almost any system design question. Remember to mention multiple layers of security.

7. **Connect principles to real incidents**: Understanding how breaches occur due to principle violations demonstrates deep understanding. The Equifax breach (2017) resulted from failure to apply patches—violating defense in depth and complete mediation.

8. **Balance security with usability**: Remember psychological acceptability. The most secure system that no one uses is ineffective.

9. **Complete mediation in practice**: Explain how this prevents privilege escalation attacks and ensures consistent enforcement.

10. **Answer with principle names correctly**: Use exact terminology—economy of mechanism, not "keep it simple"; least common mechanism, not "minimize sharing."