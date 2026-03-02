# Network, Host, and Application Security in Cloud Computing - Summary

## Key Definitions and Concepts

- **Network Security**: Technologies and policies protecting cloud network infrastructure and data in transit, including VPNs, security groups, NACLs, and DDoS protection.
- **Host Security**: Measures protecting virtual machines, containers, and operating systems running cloud workloads through hardening, patching, and isolation.
- **Application Security**: Practices ensuring cloud-hosted applications are free from vulnerabilities through secure development, WAFs, authentication, and encryption.
- **Shared Responsibility Model**: Security obligations divided between CSPs (physical infrastructure, hypervisor) and customers (data, applications, identity management) based on service model.
- **Defense-in-Depth**: Layered security approach implementing multiple controls across network, host, and application layers.
- **Security Groups**: Stateful virtual firewalls at instance level controlling inbound/outbound traffic.
- **WAF (Web Application Firewall)**: Filter protecting web applications against OWASP Top 10 vulnerabilities.
- **Container Security**: Four pillars—image scanning, runtime protection, orchestration security, and secrets management.

## Important Formulas and Techniques

- **Least Privilege Principle**: Grant minimum necessary permissions to users and processes.
- **Encryption Standards**: AES-256 for data at rest, TLS 1.2+ for data in transit.
- **Rate Limiting**: Block IPs exceeding defined request thresholds (e.g., 100 requests/minute).
- **Network Policy**: Kubernetes YAML defining pod-to-pod communication rules.

## Key Points

1. In IaaS, customers manage OS, middleware, and runtime; in PaaS, only applications and data; in SaaS, nearly everything is provider-managed.

2. Security groups are stateful (return traffic auto-allowed) while NACLs are stateless (require explicit rules for both directions).

3. AWS Shield, Azure DDoS Protection, and Google Cloud Armor provide managed DDoS mitigation.

4. Container hardening includes running as non-root, read-only filesystems, and minimal base images.

5. WAFs defend against SQL injection, XSS, CSRF, and other OWASP Top 10 vulnerabilities.

6. Managed identity services (AWS IAM Roles, Azure Managed Identities, GCP Service Accounts) eliminate credential embedding risks.

7. Customer-managed keys (CMK) provide greater control but require proper key lifecycle management.

8. CIS Benchmarks provide industry-standard hardening guidelines for cloud instances.

9. Binary Authorization in GCP ensures only trusted container images are deployed.

10. Cloud-native SIEM tools (Azure Sentinel, AWS Security Hub) provide centralized security monitoring.

## Common Mistakes to Avoid

1. **Over-permissive Security Groups**: Allowing 0.0.0.0/0 for all traffic instead of specific IP ranges.

2. **Exposing Credentials in Code**: Hardcoding API keys or passwords instead of using IAM roles or secrets management.

3. **Skipping Image Scanning**: Deploying containers without vulnerability scanning, leading to vulnerable workloads.

4. **Ignoring Egress Traffic**: Only configuring inbound rules while neglecting outbound traffic control.

5. **Disabling Encryption for Performance**: Sacrificing security for performance without proper risk assessment.

## Revision Tips

1. Create comparison tables: Security Groups vs NACLs, IaaS vs PaaS vs SaaS responsibilities.

2. Practice configuring security groups through AWS/Azure console simulations or hands-on labs.

3. Memorize OWASP Top 10 vulnerabilities and corresponding cloud mitigation strategies.

4. Review case studies of major cloud breaches (Capital One, misconfigured S3 buckets) to understand real-world implications.

5. Use cloud provider documentation to reinforce concepts with practical configuration examples.