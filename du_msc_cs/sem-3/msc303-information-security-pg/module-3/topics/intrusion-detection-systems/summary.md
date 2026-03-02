# Intrusion Detection Systems - Summary

## Key Definitions and Concepts
- **IDS**: System monitoring network/host activities for policy violations
- **HIDS**: Host-based system analyzing local logs and processes
- **NIDS**: Network-based system inspecting packet payloads and headers
- **True Positive Rate**: Proportion of attacks correctly identified
- **Polymorphic Attack**: Malware that changes signature while retaining functionality

## Important Formulas and Theorems
- **Shannon Entropy**: H(X) = -Σp(x_i)log₂p(x_i) (DDoS detection)
- **Snort Rule Syntax**: [Action] [Protocol] [Source] [Destination] [Options]
- **ROC AUC**: Area under Receiver Operating Characteristic curve (performance metric)
- **Mahalanobis Distance**: √((x-μ)ᵀΣ⁻¹(x-μ)) (anomaly detection)

## Key Points
- Signature-based IDS effective for known attacks but vulnerable to zero-days
- Anomaly detection requires clean training data and adaptive thresholds
- Modern IDS use ensemble methods combining multiple detection approaches
- SDN enables dynamic traffic redirection for deep packet inspection
- Federated learning emerging for privacy-preserving distributed IDS
- Quantum computing threatens current encryption but aids pattern detection
- MITRE ATT&CK framework essential for attack pattern recognition

## Common Mistakes to Avoid
- Confusing IDS (detection) with IPS (prevention) capabilities
- Assuming anomaly detection alone suffices for all attack types
- Neglecting time synchronization in distributed IDS architectures
- Overlooking encrypted traffic analysis challenges in TLS 1.3

## Revision Tips
1. Create comparison tables: HIDS vs NIDS, Signature vs Anomaly detection
2. Practice writing Snort rules for various attack scenarios
3. Use Wireshark captures to analyze real detection scenarios
4. Memorize ROC curve interpretation: Upper-left corner = ideal performance
5. Study recent CVE entries to understand modern attack patterns

Length: 650 words