# Bias, Fairness, and Accountability in AI Systems

## Introduction
Modern AI systems increasingly influence high-stakes decision-making domains including criminal justice, healthcare, and employment. However, numerous studies (Buolamwini & Gebru, 2018; Obermeyer et al., 2019) have revealed systemic biases in these systems, leading to growing concerns about algorithmic fairness. The University of Delhi's MSc CS curriculum emphasizes understanding both technical measures of fairness and socio-technical aspects of accountability.

This topic bridges statistical learning theory with ethical AI implementation. Current research focuses on three key challenges: 1) Formalizing fairness metrics for non-binary protected attributes 2) Developing auditable machine learning pipelines 3) Creating accountability frameworks under India's Digital Personal Data Protection Act 2023.

## Key Concepts
1. **Algorithmic Bias Types**:
   - Historical Bias: Pre-existing societal inequalities in training data
   - Representation Bias: Under-sampling of marginalized groups
   - Measurement Bias: Flawed proxy variables (e.g., zip code as poverty indicator)

2. **Fairness Metrics**:
   - Demographic Parity: P(Ŷ=1|A=0) = P(Ŷ=1|A=1)
   - Equalized Odds: TPR_A=0 = TPR_A=1 ∧ FPR_A=0 = FPR_A=1
   - Counterfactual Fairness: Ŷ(a) = Ŷ(a') ∀ individual a,a'

3. **Accountability Mechanisms**:
   - Model Cards (Mitchell et al., 2019)
   - Right to Explanation under GDPR Article 22
   - Indian context: RBI guidelines for AI in banking (2023)

## Examples

**Example 1: Loan Approval Bias Mitigation**
Problem: A bank's ML model approves 75% male vs 48% female applicants. Training data reflects historical gender disparities.

Solution:
1. Pre-processing: Apply reweighting using 𝕎(x) = 1/P(A=a|X=x)
2. In-processing: Add fairness constraint 𝔼[Ŷ|A=0] ≥ 0.95𝔼[Ŷ|A=1]
3. Post-processing: Threshold adjustment per group to equalize FPR

**Example 2: COMPAS Recidivism Analysis**
Replicate ProPublica's analysis showing higher false positive rates for Black defendants:
```python
from fairlearn.metrics import equalized_odds_difference
eo_diff = equalized_odds_difference(y_true, y_pred, sensitive_features=race)
assert abs(eo_diff) < 0.1  # Fairness constraint
```

## Exam Tips
1. Memorize formal definitions of 3+ fairness metrics with mathematical notation
2. Contrast individual vs group fairness using Indian caste data examples
3. Analyze trade-offs between accuracy and fairness using ROC curves
4. Discuss legal implications of AI accountability in Indian context
5. Prepare case studies: Amazon hiring tool (gender), Aadhaar authentication errors
6. Understand bias propagation through ML pipeline phases
7. Practice calculating disparate impact ratio: (PR_A=1 / PR_A=0)