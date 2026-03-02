# Cloud Security Defense Strategies

## Overview

Cloud security defense strategies encompass comprehensive policies, technologies, and practices designed to protect cloud-based systems, data, and infrastructure from threats. Unlike traditional IT security, cloud defense must address multi-tenancy, shared responsibility, distributed architectures, and dynamic resource nature through layered (defense-in-depth), proactive, and integrated approaches.

## Key Points

- **Defense-in-Depth**: Multiple security layers so if one is breached, subsequent layers continue protecting: Physical (datacenter access) → Network (firewalls, VPCs) → IAM (MFA, RBAC) → Application (WAF, secure coding) → Data (encryption, DLP) → Monitoring (SIEM, IDS/IPS)
- **Identity and Access Management (IAM)**: Cornerstone of cloud security with Multi-Factor Authentication (MFA), Role-Based Access Control (RBAC), Principle of Least Privilege, Just-In-Time (JIT) access, and secure service accounts with managed identities
- **Network Security**: Virtual Private Cloud (VPC) for network segmentation, Security Groups/NACLs for traffic rules, Private Endpoints avoiding public internet, DDoS Protection (AWS Shield, Azure DDoS), Web Application Firewall (WAF) for OWASP Top 10 protection
- **Data Protection**: Encryption everywhere (at rest AES-256, in transit TLS 1.2+, in use via confidential computing), Data Classification by sensitivity, Data Loss Prevention (DLP) policies, backup/disaster recovery with geo-redundancy, data masking/tokenization
- **Security Monitoring**: SIEM (CloudTrail + GuardDuty, Azure Sentinel) for log aggregation and correlation, IDS/IPS for suspicious pattern detection, automated alerting for anomalies, documented incident response plan, forensic-ready immutable logs
- **Vulnerability Management**: Regular vulnerability scanning, penetration testing, automated patch management, configuration auditing against CIS Benchmarks
- **Zero Trust Architecture**: Never trust always verify, authenticate every user/device/service, micro-segment networks to limit blast radius, continuously validate trust based on context

## Important Concepts

- Cloud-native security services mapping: AWS IAM ↔ Azure AD, GuardDuty ↔ Sentinel, WAF ↔ WAF, Shield ↔ DDoS Protection, KMS ↔ Key Vault, CloudTrail ↔ Monitor, Config ↔ Policy
- Security automation (DevSecOps) integrates security into CI/CD pipelines with automated testing (SAST, DAST), IaC security scanning, and automated remediation
- Data classification tags (public, internal, confidential, restricted) apply corresponding security controls
- Just-In-Time (JIT) access grants elevated privileges only when needed, automatically revoking after time window
- SIEM systems aggregate logs from all cloud services for correlation, analysis, and real-time threat detection

## Notes

- Know all 6 defense-in-depth layers and be able to give examples of controls at each layer
- IAM concepts (MFA, RBAC, least privilege, JIT access) are frequently tested in exams
- Understand VPCs, security groups, NACLs and the differences between them
- Be able to map AWS and Azure security services to their purposes
- Understand Zero Trust core principles and how they differ from perimeter-based security
- Know key steps in incident response plans for practical security scenarios
- DevSecOps shift-left security: catch vulnerabilities early in development lifecycle
