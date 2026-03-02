# AI Governance and Fairness in Financial Services: Risk Management Framework - Summary

## Key Definitions and Concepts

- **AI Governance**: Systematic management of AI systems ensuring ethical, legal, and effective operation throughout their lifecycle
- **Model Risk Management (MRM)**: Framework for identifying, assessing, mitigating, and monitoring risks arising from AI/ML models
- **Algorithmic Fairness**: Ensuring AI decisions do not discriminate based on protected attributes like gender, race, or religion
- **Concept Drift**: Changes in the underlying relationship between inputs and outputs that degrade model performance over time

## Important Formulas and Metrics

- **Demographic Parity**: P(Ŷ=1|A=a) = P(Ŷ=1|A=b) for protected groups a and b
- **Equalized Odds**: P(Ŷ=1|A=a,Y=y) = P(Ŷ=1|A=b,Y=y) for y ∈ {0,1}
- **Population Stability Index (PSI)**: Measures data distribution shift between training and production data

## Key Points

1. AI governance in financial services requires policy frameworks, accountability structures, documentation standards, and audit mechanisms

2. The five-pillar risk management framework includes Risk Identification, Assessment, Mitigation, Monitoring, and Governance

3. Fairness metrics like demographic parity, equalized odds, and predictive parity help measure algorithmic discrimination

4. Common bias sources include historical data, proxy variables, sampling methods, and feature measurement

5. RBI and SEBI regulations in India require compliance for AI systems in banking, lending, and trading

6. Model monitoring must track performance drift, data distribution shifts, and fairness metric changes

7. Human-in-the-loop systems provide essential oversight for high-stakes financial decisions

8. Explainable AI techniques (SHAP, LIME) are crucial for regulatory compliance and customer trust

## Common Mistakes to Avoid

- Assuming fairness metrics are interchangeable - each measures different aspects of discrimination
- Neglecting post-deployment monitoring - model performance degrades with data drift
- Treating AI governance as a one-time activity rather than continuous lifecycle management
- Overlooking proxy discrimination - protected attributes can be inferred from other features

## Revision Tips

1. Draw the five-pillar framework diagram repeatedly until memorized

2. Practice explaining each fairness metric with a financial services example

3. Review recent RBI guidelines on digital lending and AI applications

4. Create a checklist of bias sources and corresponding mitigation techniques

5. Understand the connection between model explainability and regulatory compliance