# Interpretability Methods - Summary

## Key Definitions and Concepts
- **Interpretability**: Degree to which humans can understand model decisions
- **Fidelity**: How accurately explanation matches model behavior
- **Counterfactual**: Minimal changes needed to alter model output
- **Shapley Value**: Fair allocation of payoff based on cooperative game theory

## Important Formulas and Theorems
- **SHAP Value**: ϕᵢ = Σ_{S⊆N\{i}} [|S|!(M−|S|−1)!)/M!] (f(S∪{i}) − f(S))
- **LIME Objective**: minₛₗ [𝔼ₓ[πₓ(z)] (f(z) - g(z))² + Ω(g)]
- **Integrated Gradients**: IGᵢ(x) = (xᵢ - x'ᵢ) × ∫₀¹ ∂F(x'+α(x-x'))/∂xᵢ dα

## Key Points
- Interpretability is crucial for trust, debugging, and regulatory compliance
- Post-hoc methods explain existing models; intrinsic methods design transparent models
- SHAP provides theoretically grounded feature attribution
- Counterfactuals align with human reasoning but may not be unique
- Attention weights in transformers offer layer-wise linguistic insights
- Trade-off exists between model complexity and interpretability
- Current research focuses on quantifying explanation uncertainty

## Common Mistakes to Avoid
1. Confusing model accuracy with interpretability
2. Assuming feature importance implies causality
3. Overlooking computational complexity of SHAP (O(2ᴹ))
4. Applying vision methods directly to NLP tasks without adaptation

## Revision Tips
1. Create comparison tables: LIME vs SHAP vs Grad-CAM
2. Practice implementing SHAP force plots using sample datasets
3. Study landmark papers: "Why Should I Trust You?" (LIME), SHAP (2017)
4. Relate methods to DU curriculum areas: ML (msc301), Ethics (msc402)