# Fairness in ML - Summary

## Key Definitions and Concepts
- Disparate Impact: Systematic adverse outcomes for protected groups
- Counterfactual Fairness: Predictions unchanged under protected attribute manipulation
- Adversarial Debiasing: Neural network training with fairness constraints

## Important Formulas and Theorems
- Demographic Parity: |P(Ŷ=1|A=0) - P(Ŷ=1|A=1)| ≤ ε
- Equal Opportunity Difference: TPR_A - TPR_B
- Bias-Variance-Fairness Tradeoff: L(f) = E[(y-f(x))²] + λ·Unfairness(f)

## Key Points
- No single fairness definition suits all contexts
- Pre-processing works best with known bias patterns
- Fairness constraints often reduce model accuracy
- Causal graphs help identify legitimate proxies
- Indian context requires caste/religion-aware fairness
- EU AI Act mandates fairness assessments
- Open-source tools: AIF360, Fairlearn, SHAP

## Common Mistakes to Avoid
- Assuming fairness metrics are interchangeable
- Ignoring intersectional bias (gender+caste)
- Using protected attributes without legal review
- Overlooking human-in-the-loop requirements

## Revision Tips
1. Practice threshold adjustment on COMPAS dataset
2. Memorize confusion matrix-based fairness metrics
3. Compare 3 papers from FAccT 2023 proceedings
4. Create cheat sheet of fairness/accuracy tradeoff curves

Length: 650 words