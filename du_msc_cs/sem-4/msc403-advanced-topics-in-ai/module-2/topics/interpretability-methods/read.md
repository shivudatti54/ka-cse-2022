# Interpretability Methods in AI Systems

## Introduction
Interpretability in AI refers to the ability to explain or present AI model decisions in understandable terms to humans. As AI systems increasingly impact critical domains like healthcare diagnostics, financial risk assessment, and criminal justice, understanding model behavior becomes crucial for ethical deployment, regulatory compliance, and system improvement. The European Union's GDPR Article 22 specifically mandates "right to explanation" for automated decisions, making interpretability a legal requirement in many applications.

Current research focuses on two main approaches: intrinsic interpretability (designing transparent models) and post-hoc explanations (explaining black-box models). The field draws from cognitive psychology, information theory, and human-computer interaction. Recent breakthroughs include the development of SHAP (SHapley Additive exPlanations) values and counterfactual explanations that align with human reasoning patterns.

## Key Concepts
1. **Local Interpretable Model-agnostic Explanations (LIME)**
   - Approximates complex models with locally faithful linear models
   - Generates perturbations around a prediction instance
   - Mathematical formulation: ξ(x) = argminₛₗ [L(f, g, πₓ) + Ω(g)]

2. **SHAP Values**
   - Game-theoretic approach based on Shapley values
   - Satisfies efficiency, symmetry, dummy, and additivity properties
   - Equation: ϕᵢ = Σ_{S⊆N\{i}} [|S|!(M−|S|−1)!)/M!] (f(S∪{i}) − f(S))

3. **Saliency Maps (Computer Vision)**
   - Visual explanation through gradient-based attribution
   - Includes Guided Backpropagation and Grad-CAM variants
   - Computes ∂y^c/∂x for class score y^c w.r.t input pixels

4. **Counterfactual Explanations**
   - "What-if" scenarios showing minimal changes needed for different outcomes
   - Formalized as: argmin_{x'} d(x,x') s.t. f(x')=y', x'∈X

5. **Attention Mechanisms (NLP)**
   - Transformer models provide self-attention weights as explanations
   - Multi-head attention allows analysis of different interpretation aspects

## Examples

**Example 1: LIME for Image Classification**
Problem: Explain ResNet-50's prediction of "African Elephant"
Solution:
1. Generate 1000 perturbed images by masking random superpixels
2. Get ResNet predictions for perturbed samples
3. Train weighted linear model on perturbations
4. Top positive weights indicate influential superpixels (tusks, trunk shape)

**Example 2: SHAP for Credit Risk Model**
Problem: Explain why loan application was rejected
Solution:
1. Compute SHAP values for all features
2. Identify top negative contributors:
   - Debt-to-income ratio: ϕ = -0.32
   - Recent defaults: ϕ = -0.28
3. Present additive explanation: base value + Σϕᵢ = rejection threshold

**Example 3: Counterfactual for Loan Approval**
Problem: Generate "What if" scenario for rejected applicant
Solution:
1. Maintain: Employment sector (IT), education (Masters)
2. Modify: Credit score from 650 → 720
3. Reduce debt ratio from 45% → 35%
4. New prediction: Approved with 82% probability

## Exam Tips
1. Always distinguish between local vs global interpretability methods
2. For comparison questions, use criteria: faithfulness, stability, comprehensibility
3. Remember SHAP's mathematical properties from cooperative game theory
4. When discussing limitations, mention the "Rashomon Effect" (multiple valid explanations)
5. For ethics questions, link to AI accountability frameworks (EU AI Act, NITI Aayog guidelines)
6. Recent research angles: Quantum-inspired explanations, neuro-symbolic integration
7. Case study approach works well for 10-mark questions (e.g., medical diagnosis systems)