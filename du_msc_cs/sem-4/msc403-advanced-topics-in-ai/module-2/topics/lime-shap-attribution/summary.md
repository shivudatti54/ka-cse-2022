# LIME & SHAP Attribution - Summary

## Key Definitions and Concepts
- **LIME**: Local linear approximation of complex models using perturbed samples
- **SHAP**: Game-theoretic approach assigning feature importance via Shapley values
- **Infidelity**: Metric measuring explanation robustness to input perturbations
- **Shapley Axioms**: Efficiency, Symmetry, Dummy, Additivity

## Important Formulas and Theorems
- Shapley Value: φ_i = ∑_{S⊆N\{i}} [|S|!(M-|S|-1)!)/M!] (v(S∪{i}) - v(S))
- LIME Objective: argmin_{g∈G} [L(f,g,π_x) + Ω(g)]
- SHAP Kernel Weight: π_{x'}(z') = (M-1)/(C(M,|z'|)|z'|(M-|z'|))

## Key Points
- SHAP provides theoretically consistent attributions; LIME offers flexibility
- TreeSHAP reduces complexity from O(2^M) to O(TL2^M) for tree depth L
- Integrated Gradients (IG) is path-based; SHAP is value-based
- LIME explanations can vary with different perturbation distributions
- SHAP values enable global interpretability through local value aggregation
- Counterfactual explanations complement attribution methods
- Recent work combines SHAP with causal graphs (D-SHAP)

## Common Mistakes to Avoid
- Confusing local vs global feature importance
- Treating SHAP values as causal effects
- Ignoring baseline selection impact in SHAP calculations
- Using default 1000 samples for LIME in high-dimensional data

## Revision Tips
1. Practice SHAP value calculations for small feature sets manually
2. Use SHAP's `summary_plot` to identify global feature trends
3. Implement LIME for text data using `LimeTextExplainer`
4. Study the connection between Shapley values and Integrated Gradients

Length: 650 words