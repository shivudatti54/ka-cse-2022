# Basic Learning Theory

## Overview

Computational learning theory studies the theoretical foundations of learning algorithms, providing mathematical frameworks that characterize when learning is possible and quantify the resources required. It answers fundamental questions about what can be learned, how much data is needed, and how complex hypotheses can be.

## Key Points

- **Hypothesis Space (H)**: Set of all possible functions a learning algorithm can consider; determined before seeing data based on algorithm design
- **Version Space**: Subset of H consistent with all training examples; shrinks as more data arrives; bounded by most general and most specific hypotheses
- **Sample Complexity**: Minimum training examples needed to learn reliably; higher accuracy and confidence require more samples; m >= (1/epsilon)(ln|H| + ln(1/delta))
- **PAC Learning**: Concept is learnable if with probability (1-delta), hypothesis has error at most epsilon; connects data amount, accuracy, and confidence
- **VC Dimension**: Measures expressive power of hypothesis class; largest number of points H can shatter; linear classifiers in 2D have VC=3, d-dimensional have VC=d+1
- **No Free Lunch Theorem**: No single algorithm is universally best; algorithm selection must be guided by problem characteristics

## Important Concepts

- Shattering: H shatters set S if for every possible labeling, some h in H perfectly classifies them
- VC dimension connects to generalization: m >= (1/epsilon)(VC(H)\*log(1/epsilon) + log(1/delta))
- Occam's Razor: Prefer simplest hypothesis consistent with data; simpler models less likely to overfit
- Inductive Bias types: Restriction bias (limits hypothesis space), Preference bias (prefers certain hypotheses), Search bias (affects exploration)
- PAC parameters: epsilon (max acceptable error), delta (max failure probability), (1-epsilon) is accuracy, (1-delta) is confidence

## Notes

- Define PAC learning clearly with both epsilon and delta probability inequality
- VC dimension of linear classifiers in 2D = 3 - most commonly asked specific value
- Explain shattering with diagram showing all 2^n labelings
- Know difference: hypothesis space (all possible) vs version space (consistent with data)
- Link inductive bias to specific algorithms: KNN (locality), linear (linearity), Naive Bayes (independence)
- No Free Lunch practical implication: always try multiple algorithms and validate
