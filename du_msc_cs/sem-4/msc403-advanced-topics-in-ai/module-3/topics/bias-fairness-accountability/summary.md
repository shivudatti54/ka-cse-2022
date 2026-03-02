# Bias, Fairness, and Accountability - Summary

## Key Definitions and Concepts
- **Disparate Impact**: Neutral policies disproportionately harming protected groups
- **Fairness Through Unawareness**: Flawed approach of excluding protected attributes
- **Proxy Discrimination**: Using variables correlating with protected attributes
- **Algorithmic Impact Assessment**: Systematic risk evaluation of AI systems

## Important Formulas and Theorems
- **Demographic Parity**: (P(Ŷ=1|A=0))/(P(Ŷ=1|A=1)) ≥ 0.8 (80% rule)
- **Equalized Odds**: TPR_A=0 = TPR_A=1 ∧ FPR_A=0 = FPR_A=1
- **Counterfactual Fairness**: 𝔼[Ŷ_a|X=x] = 𝔼[Ŷ_{a'}|X=x] ∀ a ≠ a'

## Key Points
- Bias can emerge at data collection, modeling, and deployment stages
- No single fairness metric fits all contexts - choice depends on legal requirements
- Indian DPDP Act mandates data fiduciary responsibilities for AI developers
- Adversarial debiasing achieves fairness via minimax optimization
- Model cards must document intended uses, training data, and fairness analysis
- Caste and linguistic biases require novel mitigation approaches in Indian AI
- Audit trails must preserve model versions and decision logs for 5+ years

## Common Mistakes to Avoid
- Assuming "fairness through unawareness" eliminates bias
- Confusing statistical parity with substantive fairness
- Ignoring intersectional biases (gender+caste+region)
- Overlooking deployment context in fairness evaluations
- Treating fairness metrics as binary constraints rather than continuous optimization

## Revision Tips
1. Create comparison tables: Fairness definitions vs legal standards
2. Practice with AI Fairness 360 toolkit on UCI Adult dataset
3. Memorize 3 Indian case laws related to algorithmic discrimination
4. Diagram bias propagation through neural network layers
5. Write pseudocode for rejection option classification (post-processing)