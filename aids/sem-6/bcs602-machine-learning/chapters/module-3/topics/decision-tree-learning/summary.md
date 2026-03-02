# Decision Tree Learning - Summary

## Key Definitions and Concepts

- **Decision Tree**: A hierarchical structure with root node (starting point), internal nodes (attribute tests), and leaf nodes (class labels)

- **Entropy**: Measure of impurity in a dataset, calculated as Σᵢ pᵢ × log₂(pᵢ), ranging from 0 (pure) to 1 (maximally impure for binary)

- **Information Gain**: Reduction in entropy achieved by splitting on an attribute; attribute with HIGHEST gain is selected

- **Gini Index**: Alternative impurity measure used by CART; Gini = 1 - Σᵢ pᵢ²

- **Gain Ratio**: Modification of information gain used by C4.5 to handle attributes with many values

## Important Formulas and Theorems

- **Entropy Formula**: Entropy(S) = -Σᵢ pᵢ × log₂(pᵢ)

- **Information Gain Formula**: Gain(S, A) = Entropy(S) - Σᵥ (|Sᵥ|/|S|) × Entropy(Sᵥ)

- **Gini Index Formula**: Gini(S) = 1 - Σᵢ pᵢ²

- **Gain Ratio**: GainRatio(S, A) = Gain(S, A) / SplitInformation(S, A)

## Key Points

- Decision trees provide interpretable white-box models easy to visualize and explain

- Top-down induction (TDIDT) is the greedy approach used by ID3, C4.5, and CART

- ID3 selects attribute with HIGHEST information gain; C4.5 uses gain ratio to avoid bias toward multi-valued attributes

- Continuous attributes require finding optimal split points by evaluating thresholds

- Overfitting occurs when trees are too complex; addressed through pre-pruning (early stopping) or post-pruning (reduced error pruning)

- ID3 handles only categorical attributes; C4.5 handles both categorical and continuous

- CART uses Gini index and produces binary trees; suitable for both classification and regression

## Common Mistakes to Avoid

- Using natural logarithm instead of log base 2 in entropy calculations

- Selecting attribute with LOWEST information gain instead of HIGHEST

- Forgetting that entropy is 0 when all examples belong to one class

- Confusing gain ratio with information gain - gain ratio divides by split information

- Not showing calculation steps in exam problems, leading to loss of partial marks

## Revision Tips

1. Practice calculating entropy and information gain for at least 3 different datasets before the exam

2. Memorize that entropy = 0 means pure, entropy = 1 means maximally impure for binary classification

3. Remember the attribute selection rule: ID3/C4.5 pick HIGHEST information gain, CART picks LOWEST Gini

4. Understand the tree-building process: Start at root → calculate gains for all attributes → split on best attribute → repeat recursively

5. Review the differences between ID3, C4.5, and CART algorithms as this is a common exam question