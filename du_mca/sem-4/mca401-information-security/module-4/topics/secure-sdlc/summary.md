# Secure Software Development Life Cycle (SDLC) - Summary

## Key Definitions and Concepts
- SDLC: Process for planning, creating, testing, deploying software
- Secure SDLC: SDLC with integrated security controls
- STRIDE: Threat classification model (Spoofing, Tampering, etc.)
- SAST/DAST: Static/Dynamic Application Security Testing

## Important Formulas and Theorems
- Vulnerability Reduction Formula: 
  Early fixes = Cost in requirements × 1 vs. Post-deployment × 30 (IBM)
- CVE Scoring: CVSS v3.1 Base Score = Exploitability + Impact

## Key Points
- Security must be "shifted left" to early SDLC phases
- Threat modeling reduces design flaws by 60-70%
- SAST finds 85% code vulnerabilities pre-deployment
- Compliance requires documentation at each SDLC stage
- Incident response plans must be version-controlled
- DevSecOps enables continuous security validation
- Secure SDLC maturity models have 5 levels (BSIMM)

## Common Mistakes to Avoid
- Treating security as final testing phase activity
- Ignoring supply chain risks in third-party components
- Misconfiguring CI/CD pipelines (e.g., disabled SAST)
- Poor secret management in version control

## Revision Tips
1. Memorize OWASP Top 10 2023 with mitigation patterns
2. Practice creating DFDs for threat modeling
3. Study NIST SP 800-218 (SSDF) framework
4. Compare tools: SonarQube (SAST) vs OWASP ZAP (DAST)

Length: 400-800 words