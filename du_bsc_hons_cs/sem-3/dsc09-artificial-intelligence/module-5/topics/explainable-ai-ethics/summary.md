# Explainable AI and Ethics - Summary

## Key Definitions and Concepts

- **Explainable AI (XAI)**: Techniques and methods that make AI decision-making processes understandable to humans
- **Black Box Problem**: The opacity of complex neural networks whose internal operations are incomprehensible even to developers
- **Interpretability**: The degree to which a human can understand how an AI system arrives at its decisions
- **LIME (Local Interpretable Model-agnostic Explanations)**: Explains individual predictions by approximating complex models locally with simpler interpretable models
- **SHAP (SHapley Additive exPlanations)**: Assigns feature importance using Shapley values from game theory; provides both local and global explanations
- **Counterfactual Explanations**: Describe how input would need to change to alter the prediction ("what-if" scenarios)

## Important Formulas and Theorems

- **Shapley Values**: ϕᵢ(v) = ∑(S⊆N\{i}) (|S|!(n-|S|-1)!/n!) × [v(S∪{i}) - v(S)]
- Fairness Metrics: Demographic Parity, Equalized Odds, Individual Fairness

## Key Points

- The interpretability-accuracy trade-off is fundamental: complex models perform better but are less interpretable
- Post-hoc explanation techniques (LIME, SHAP) extract explanations from already-trained complex models
- AI bias originates from historical data, underrepresentation, measurement inconsistencies, model aggregation, and evaluation benchmarks
- Fairness metrics can conflict—improving one may worsen another (fairness impossibility theorem)
- Key ethical principles: Fairness, Transparency, Accountability, Privacy
- GDPR establishes "right to explanation"; EU AI Act uses risk-based regulatory approach
- Real-world biased AI examples: COMPAS recidivism, Amazon hiring, facial recognition disparities
- Counterfactual explanations are particularly valuable for actionable user guidance

## Common Mistakes to Avoid

- Confusing interpretability with explainability—they are related but distinct concepts
- Assuming more complex models always outperform simpler ones—interpretable models can be competitive for structured data
- Treating fairness as a single metric—there are multiple, sometimes conflicting, fairness definitions
- Believing bias removal is one-time—bias auditing must be continuous throughout AI lifecycle
- Overlooking the business case for XAI—explainability also aids debugging, trust, and regulatory compliance

## Revision Tips

1. For each XAI technique (LIME, SHAP, counterfactuals), remember one concrete application example
2. Memorize the five sources of AI bias with real-world instances for each
3. Practice mapping ethical principles to specific AI scenarios (healthcare, hiring, finance)
4. Review the EU AI Act risk categories—know which applications are high-risk
5. Understand why counterfactual explanations are considered user-friendly and actionable
6. Be prepared to discuss how you would audit an AI system for bias at each development stage