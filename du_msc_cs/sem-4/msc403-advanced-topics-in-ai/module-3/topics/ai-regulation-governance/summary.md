# AI Regulation and Governance - Summary

## Key Definitions and Concepts
- **High-Risk AI**: Systems used in critical infrastructure, education, employment, etc. (EU AI Act)
- **Algorithmic Accountability**: Legal obligation to explain AI system decisions
- **Conformity Assessment**: Process to ensure AI meets regulatory requirements
- **Right to Explanation**: Legal right to meaningful information about algorithmic decisions

## Important Formulas and Theorems
- **Disparate Impact Ratio**: (P(Y=1|D=unprivileged)/P(Y=1|D=privileged)) ≥ 0.8 (US EEOC guideline)
- **Differential Privacy**: ε ≈ ln(P[M(D) ∈ S]/P[M(D') ∈ S])
- **Shapley Values**: φ_i(v) = ∑_{S⊆N\{i}} (|S|!(|N|-|S|-1)!)/|N|! (v(S∪{i}) - v(S))

## Key Points
- EU AI Act establishes 4 risk categories with corresponding obligations
- Model documentation must include training methodologies and validation results
- Third-party auditing is mandatory for certain high-risk AI systems
- India's DPDP Act 2023 introduces significant data governance requirements
- Technical safeguards (homomorphic encryption, federated learning) aid compliance
- Incident reporting timelines vary by jurisdiction (72 hours in GDPR)
- Ongoing research focuses on automated compliance checking using formal methods

## Common Mistakes to Avoid
- Confusing data protection regulations with AI-specific laws
- Overlooking post-market monitoring requirements
- Assuming technical fairness metrics equal legal compliance
- Neglecting cross-border data transfer restrictions in model training

## Revision Tips
- Create comparative tables of GDPR vs EU AI Act vs India's DPDP Act
- Practice drafting technical documentation for sample AI systems
- Follow ongoing OECD.AI policy observatory updates
- Use the NIST AI Risk Management Framework as study guide
- Analyze recent AI audit reports from MITRE or Algorithmic Justice League

Length: 650 words