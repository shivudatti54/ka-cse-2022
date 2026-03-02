# Database Security Needs — Quick Revision Summary

## Introduction
Database Security involves protecting the database from unauthorized access, modification, disclosure, or destruction. As organizations increasingly rely on data-driven decisions, securing databases has become a critical component of Information Security. For the Delhi University NEP 2024 syllabus, understanding database security needs is essential for safeguarding sensitive information and maintaining business continuity.

## Key Concepts

**1. Need for Database Security**
- **Confidentiality:** Prevents unauthorized disclosure of sensitive data (e.g., personal records, financial information)
- **Integrity:** Ensures data accuracy and prevents unauthorized modifications
- **Availability:** Guarantees authorized users can access data when needed
- **Compliance:** Meets legal requirements (GDPR, IT Act 2000, India)

**2. Common Threats**
- **SQL Injection:** Malicious code insertion into queries
- **Privilege Abuse:** Legitimate users misusing permissions
- **Insider Threats:** Employees with authorized access causing harm
- **Data Leakage:** Unauthorized data extraction or exposure
- **Denial of Service (DoS):** Disrupting database availability

**3. Access Control Mechanisms**
- **Discretionary Access Control (DAC):** Owners control resource permissions
- **Mandatory Access Control (MAC):** System-enforced security labels (used in defence)
- **Role-Based Access Control (RBAC):** Permissions assigned based on job functions
- **Principle of Least Privilege:** Users get minimum necessary access

**4. Security Measures & Techniques**
- **Authentication:** Verifying user identities (strong passwords, multi-factor authentication)
- **Encryption:** Protecting data at rest (TDE) and in transit (TLS/SSL)
- **Database Auditing:** Tracking user activities and changes
- **Intrusion Detection Systems (IDS):** Monitoring for suspicious activities
- **Data Masking & Tokenization:** Obscuring sensitive data

**5. Secure Database Design**
- **Normalization:** Reduces data redundancy and improves integrity
- **Views and Stored Procedures:** Limit direct table access
- **Input Validation:** Prevents injection attacks

**6. Backup & Recovery Security**
- Encrypted backups
- Secure offsite storage
- Regular testing of recovery procedures

## Conclusion
Database security is not optional—it's a necessity. Protecting data assets requires a layered approach combining access controls, encryption, monitoring, and employee awareness. For exams, remember the CIA triad, RBAC, SQL injection prevention, and compliance frameworks as core pillars of database security.