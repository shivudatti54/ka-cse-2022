# Cloud Security Risks and Privacy

## Overview

Cloud security is the top concern for organizations adopting cloud computing due to relinquishing direct physical control over data and trusting third-party providers. The shift from perimeter-based security to a shared responsibility model (security duties divided between provider and customer) necessitates understanding risks, threats, and mitigation strategies for successful cloud deployment.

## Key Points

- **Data Breaches**: Unauthorized access to sensitive data from misconfigured storage buckets, compromised credentials, or multi-tenant vulnerabilities
- **Data Loss**: Permanent loss from accidental deletion, ransomware attacks, or provider failure where data is destroyed rather than stolen
- **Account Hijacking**: Attackers gain cloud account control through phishing, credential stuffing, or weak passwords to access data and manipulate services
- **Insecure APIs**: Poorly designed, unauthenticated, or vulnerable APIs serve as entry points since every cloud service exposes an API
- **Malicious Insiders**: Employees or contractors (customer or provider) who misuse authorized access to steal or damage data
- **Shared Technology Vulnerabilities**: Multi-tenant vulnerabilities in hypervisor, shared storage, or networking allowing potential cross-tenant access (VM escape attacks)
- **Privacy Impact Assessment (PIA)**: Systematic process evaluating how systems collect, use, share, and protect personal information; identifies privacy risks and recommends mitigations

## Important Concepts

- Cloud Security Alliance (CSA) Treacherous Twelve includes data breaches, weak identity/access management, insecure APIs, system vulnerabilities, account hijacking, malicious insiders, APTs, data loss, insufficient due diligence, abuse of cloud services, DoS/DDoS, shared technology issues
- PIA is critical for data sovereignty (compliance with local data protection laws like GDPR), third-party processing (data controller vs. data processor), transparency, and multi-tenancy risks
- PIA steps: Identify need → Describe information flow → Identify privacy risks → Assess and mitigate risks → Document and review → Integrate with development
- Key regulatory frameworks: GDPR (EU DPIAs for high-risk processing), HIPAA (US health data), SOC 2 (audit framework for providers), ISO 27001/27017/27018 (international standards)

## Notes

- Be able to list and describe at least 5-6 major cloud security risks from CSA list for exams
- Always frame security discussions within the shared responsibility model (who is responsible for what)
- Memorize PIA process steps and be able to apply them to cloud scenarios
- Understand data sovereignty: why physical location of data matters for privacy and compliance
- Know key regulatory frameworks (GDPR, HIPAA, ISO 27001) and their relevance to cloud security
- Understand that insufficient due diligence before migration exposes organizations to unanticipated risks
