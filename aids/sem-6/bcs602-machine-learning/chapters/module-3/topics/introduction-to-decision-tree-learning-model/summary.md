# Introduction to Decision Tree Learning Model - Summary

## Key Definitions and Concepts

- **Decision Tree**: A supervised learning algorithm that uses a tree-structured model of decisions based on feature values to predict class labels or continuous outcomes
- **Root Node**: The topmost node representing the entire dataset and the first split decision
- **Internal Node**: A decision node that tests a feature and has multiple branches
- **Leaf Node**: Terminal node that provides the final prediction (class label)
- **Entropy**: Measure of randomness or impurity in a dataset; ranges from 0 (pure) to 1 (maximum impurity)
- **Information Gain**: Reduction in entropy achieved by splitting on a particular feature; the algorithm selects the feature with highest Information Gain
- **Gini Impurity**: Alternative measure of impurity used by CART algorithm; ranges from 0 to 0.5
- **Pruning**: Technique to reduce tree complexity by removing sections that provide little classification power

## Important Formulas and Theorems

- **Entropy**: Entropy(S) = -Σ pᵢ log₂(pᵢ) where pᵢ is the proportion of instances in class i
- **Information Gain**: IG(S, A) = Entropy(S) - Σ (|Sv|/|S|) × Entropy(Sv)
- **Gini Impurity**: Gini(S) = 1 - Σ pᵢ²
- **Splitting Criterion**: Select the feature that maximizes Information Gain (or minimizes Gini Impurity) at each node

## Key Points

- Decision trees mimic human decision-making and provide interpretable models
- ID3 uses Information Gain, C4.5 uses Gain Ratio, and CART uses Gini Impurity for splitting
- Trees can handle both categorical and numerical (continuous) features
- Overfitting is a major concern; addressed through pre-pruning (max depth, min samples) and post-pruning
- The algorithm is recursive: each node becomes root of a subtree for remaining features
- Decision trees require no feature scaling or normalization
- Trees are unstable—small changes in data can result in completely different trees
- Leaf nodes represent final class predictions; path from root to leaf represents a classification rule

## Common Mistakes to Avoid

- Confusing Information Gain with Entropy—they are related but different concepts
- Forgetting that entropy is 0 for pure nodes and maximum when classes are equally distributed
- Overlooking the fact that decision trees can overfit easily with deep trees
- Assuming decision trees always produce optimal trees—they use greedy approach locally

## Revision Tips

- Practice calculating Entropy and Information Gain with small datasets by hand
- Draw decision trees for simple classification problems to understand the flow
- Remember the tradeoffs between different splitting criteria (Entropy vs Gini)
- Focus on understanding why overfitting occurs and how pruning helps
- Review the differences between ID3, C4.5, and CART algorithms