# LIME & SHAP Attribution Methods

## Introduction
Model interpretability has become critical in AI systems deployed in high-stakes domains like healthcare, finance, and criminal justice. As complex models like deep neural networks achieve state-of-the-art performance, their "black box" nature raises concerns about trust, fairness, and regulatory compliance. 

Local Interpretable Model-agnostic Explanations (LIME) and SHapley Additive exPlanations (SHAP) are two prominent attribution methods that provide post-hoc explanations for individual predictions. LIME approximates complex models locally with interpretable surrogates, while SHAP leverages game-theoretic Shapley values to ensure mathematically consistent feature attributions. These methods address the growing demand for Explainable AI (XAI) in both industry and research contexts.

Recent developments include SHAP's integration with transformer architectures and LIME's applications in multimodal explanations. The 2023 AI Act in the EU and NIST's AI Risk Management Framework have further increased the practical significance of these techniques for model auditing.

## Key Concepts
1. **LIME Framework**:
   - **Local Fidelity**: Creates linear approximations around specific predictions
   - **Perturbation Sampling**: Generates synthetic data points near instance
   - **Interpretable Representation**: Maps features to human-understandable components
   - **Sparsity Constraint**: Uses K-LASSO for feature selection

2. **SHAP Values**:
   - **Shapley Values**: Cooperative game theory concept for fair payoff distribution
   - **Additive Feature Attribution**: ∑φ_i = f(x) - E[f(X)] (efficiency property)
   - **KernelSHAP**: Model-agnostic approximation using weighted linear regression
   - **TreeSHAP**: Polynomial-time algorithm for tree-based models

3. **Theoretical Differences**:
   - LIME minimizes local loss without theoretical guarantees
   - SHAP satisfies uniqueness (from game theory axioms)
   - SHAP values maintain consistency: if model changes increase feature's impact, φ_i never decreases

## Examples

**Example 1: LIME for Image Classification**
```python
import lime
from lime import lime_image

explainer = lime_image.LimeImageExplainer()
explanation = explainer.explain_instance(
    image, 
    model.predict, 
    top_labels=1, 
    hide_color=0,
    num_samples=1000
)

# Show top 5 influential superpixels
temp, mask = explanation.get_image_and_mask(
    explanation.top_labels[0],
    positive_only=True,
    num_features=5
)
```

**Example 2: SHAP for Credit Risk Model**
```python
import shap

# Train XGBoost model
model = xgboost.train(params, dtrain)

# Compute SHAP values
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_test)

# Visualize force plot for high-risk applicant
shap.force_plot(
    explainer.expected_value, 
    shap_values[high_risk_idx,:],
    X_test.iloc[high_risk_idx,:]
)
```

## Exam Tips
1. Always contrast LIME's heuristic approach vs SHAP's axiomatic foundation
2. Remember SHAP's efficiency axiom: sum of SHAP values = model output - baseline
3. For time-constrained scenarios: LIME is faster for high-dimensional data
4. When asked about limitations: mention LIME's instability due to random sampling
5. In case studies, suggest SHAP for feature importance ranking in financial models
6. Know computational complexity: TreeSHAP O(TL2^M) vs KernelSHAP O(2^M)
7. Recent research angle: Discuss causal Shapley values (arXiv:2206.15470)

Length: 2500 words, MSc CS (research-oriented) postgraduate level