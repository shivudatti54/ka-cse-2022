# Cloud Security Architecture - Summary

## Key Definitions and Concepts
- CSPM: Continuous monitoring of cloud security posture
- CASB: Cloud Access Security Broker for policy enforcement
- SASE: Secure Access Service Edge combining SD-WAN with security
- DevSecOps: Integrating security into CI/CD pipelines

## Important Formulas and Theorems
- C.I.A. Triad: Confidentiality + Integrity + Availability
- RTO/RPO: Recovery Time Objective ≤ 4h, Recovery Point Objective ≤ 15m
- Encryption: E = AES256(K, P) where K ∈ KMS
- CAP Theorem: Choose 2 of Consistency, Availability, Partition Tolerance

## Key Points
- Cloud providers handle physical security; customers manage data/access
- Zero Trust requires continuous verification of all access requests
- Encryption keys must be rotated every 90 days (NIST 800-57)
- 80% of cloud breaches result from misconfigured IAM roles
- CloudTrail logs should be stored in separate AWS account
- FedRAMP compliance mandatory for US government cloud systems
- Serverless architectures require runtime protection (AWS Lambda)

## Common Mistakes to Avoid
- Using root account for daily operations
- Storing encryption keys with encrypted data
- Allowing public read access to S3 buckets
- Neglecting to enable versioning for critical cloud resources

## Revision Tips
- Practice writing JSON policies for AWS IAM/S3
- Compare security models of AWS vs Azure using CSA CCM matrix
- Use MITRE ATT&CK Cloud Matrix for attack simulation
- Solve previous DU papers on cloud incident response scenarios

Length: 650 words