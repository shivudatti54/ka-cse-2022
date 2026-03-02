# Security of Database Services

Securing cloud database services is critical as organizations migrate data to the cloud under the shared responsibility model. The cloud provider secures the physical infrastructure and hypervisor, while customers must protect their data, configure access controls, manage identities, and secure database instances.

Key security mechanisms include network security through Virtual Private Clouds (VPC) placing databases in private subnets with Security Groups and Network ACLs acting as virtual firewalls; data encryption both at rest using transparent data encryption (TDE) with keys managed via AWS KMS, Azure Key Vault, or Google Cloud KMS, and in transit using SSL/TLS protocols; Identity and Access Management (IAM) enforcing the principle of least privilege with fine-grained permissions and multi-factor authentication; and database auditing using CloudTrail and native audit logs for compliance and threat detection. Common threats include misconfiguration (publicly exposed ports, default credentials), data breaches requiring strong encryption and monitoring, denial-of-service attacks mitigated by DDoS protection services, and SQL injection prevented through parameterized queries.

## Key Takeaways

- Shared responsibility model: provider secures infrastructure, customer secures data and access
- Defense in depth combines network isolation, encryption, IAM, and comprehensive auditing
- Principle of least privilege grants only minimum necessary permissions via IAM
- Encryption is essential for both data at rest and data in transit with proper key management
