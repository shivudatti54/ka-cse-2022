# Decision Trees - Summary

## Key Definitions and Concepts

- **Decision Tree**: A supervised learning algorithm that creates a flowchart-like model of decisions based on feature values
- **Root Node**: Topmost node representing the entire dataset and first decision point
- **Leaf Node**: Terminal node representing final class label or prediction value
- **Entropy**: Measure of randomness/impurity in data; ranges from 0 (pure) to 1 (maximum impurity)
- **Information Gain**: Reduction in entropy achieved by splitting on an attribute; higher is better
- **Gini Impurity**: Alternative to entropy used in CART; measures misclassification probability
- **Overfitting**: When tree becomes too complex capturing noise; solved by pruning

## Important Formulas and Theorems

- **Entropy**: Entropy(S) = -Σ pᵢ log₂(pᵢ)
- **Information Gain**: IG(S, A) = Entropy(S) - Σ(|Sᵥ|/|S|) × Entropy(Sᵥ)
- **Gini Impurity**: Gini(S) = 1 - Σ(pᵢ)²
- **ID3 Algorithm**: Uses entropy and information gain; selects attribute with highest IG
- **CART Algorithm**: Uses Gini impurity; produces binary trees for classification/regression

## Key Points

1. Decision trees handle both categorical and numerical features without extensive preprocessing
2. The attribute with highest information gain is always chosen for splitting at each node
3. Entropy is 0 when all samples belong to one class, maximum when equally distributed
4. CART algorithm uses binary splits (exactly two branches) while ID3 can have multiple branches
5. Pre-pruning stops tree growth early using constraints like maximum depth or minimum samples
6. Post-pruning grows full tree then removes non-contributory branches
7. Decision trees are interpretable and allow visualization of decision logic
8. They can capture non-linear relationships without explicit feature transformation

## Common Mistakes to Avoid

1. Confusing entropy with information gain - they are related but different measures
2. Forgetting that entropy is maximum (1) when classes are equally distributed
3. Selecting attribute with lowest information gain instead of highest
4. Not considering overfitting - always apply pruning techniques
5. Using classification tree for continuous target variable

## Revision Tips

1. Practice calculating entropy, Gini impurity, and information gain with different probability distributions
2. Remember the selection rule: Highest Information Gain → Root/Node Split
3. Review the differences between ID3 (entropy-based) and CART (Gini-based) algorithms
4. Understand when to apply pre-pruning vs post-pruning for overfitting control
5. Be ready to draw or interpret a small decision tree from a given dataset
6. Know real-world applications: medical diagnosis, credit scoring, spam detection