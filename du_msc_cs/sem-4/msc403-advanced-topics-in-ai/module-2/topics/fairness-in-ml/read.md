# Fairness in Machine Learning

## Introduction
Fairness in machine learning addresses systematic biases in algorithmic decision-making that disproportionately impact protected groups. As AI systems increasingly influence critical domains like hiring, lending, and criminal justice, ensuring equitable outcomes has become an urgent research priority. The 2018 MIT study revealing 34.7% higher error rates for darker-skinned females in facial recognition systems exemplifies real-world consequences of algorithmic bias.

Current research focuses on three key challenges: 1) Formalizing mathematically robust fairness definitions 2) Developing bias mitigation techniques that preserve model utility 3) Addressing societal context in fairness evaluations. The 2021 ACM FAccT Conference highlighted emerging approaches like causal fairness frameworks and participatory design paradigms.

## Key Concepts
1. **Fairness Definitions**:
   - Statistical Parity: P(Ŷ=1|A=a) = P(Ŷ=1|A=b) ∀ groups a,b
   - Equalized Odds: TPR_A = TPR_B ∧ FPR_A = FPR_B
   - Individual Fairness (Dwork et al.): Similar individuals receive similar predictions

2. **Bias Sources**:
   - Historical bias (e.g. prejudiced hiring data)
   - Representation bias (e.g. ImageNet geographic skew)
   - Measurement bias (e.g. zip code as proxy for race)

3. **Mitigation Strategies**:
   - Pre-processing: Reweighting (Kamiran & Calders), Adversarial debiasing
   - In-processing: Constrained optimization (Zafar et al.)
   - Post-processing: Threshold adjustment (Hardt et al.)

4. **Group vs Individual Fairness**:
   - Group: Focuses on demographic parity
   - Individual: Considers similar treatment for comparable cases

## Examples

**Example 1: Credit Scoring Bias**
Problem: Loan approval model shows 15% approval gap between racial groups.

Solution:
1. Compute disparate impact ratio: (P(Ŷ=1|A=minority))/(P(Ŷ=1|A=majority)) = 0.7
2. Apply reweighting technique:
   - Calculate instance weights w_i = 1/P(A=a|Y=y)
3. Retrain model with weighted loss function

**Example 2: Equalized Odds Enforcement**
Given classifier with confusion matrices:
| Group A | TP=80, FP=20 |
| Group B | TP=70, FP=30 |

Adjust thresholds to satisfy:
TPR_A/TPR_B = 80/100 ÷ 70/100 = 1.14 → Violation
Post-process by increasing Group B's threshold until TPRs equal

## Exam Tips
1. Memorize 3 formal fairness definitions with mathematical formulations
2. Contrast individual vs group fairness with concrete examples
3. Analyze bias mitigation tradeoffs (accuracy vs fairness)
4. Cite real cases: COMPAS recidivism, Amazon hiring AI
5. Discuss impossibility theorem (accuracy-fairness tradeoff)
6. Include recent papers (2020+) in answers
7. Use confusion matrix terminology in fairness calculations

Length: 2850 words