# Decision Trees

## What are Decision Trees?
Decision Trees are supervised learning algorithms that make predictions by learning simple decision rules from features. They create a tree-like model of decisions, where each internal node tests a feature, each branch represents an outcome, and each leaf node contains a prediction.

## Key Concepts

### Structure
- **Root Node**: Top node, represents the entire dataset
- **Internal Nodes**: Test a feature and split the data
- **Branches**: Outcomes of the test (e.g., yes/no, <= threshold)
- **Leaf Nodes**: Terminal nodes with final predictions

### Types
- **Classification Trees**: Predict categorical outcomes (class labels)
- **Regression Trees**: Predict continuous values

## Splitting Criteria

### For Classification

**Gini Impurity**
Measures the probability of misclassification:
```
Gini = 1 - SUM(p_i^2)
```
Where p_i is the probability of class i. Range: [0, 0.5] for binary.

**Entropy / Information Gain**
```
Entropy = -SUM(p_i * log2(p_i))
Information Gain = Entropy(parent) - weighted_avg(Entropy(children))
```

### For Regression

**Mean Squared Error (MSE)**
```
MSE = (1/n) * SUM((y_i - mean(y))^2)
```
Split to minimize MSE in child nodes.

**Mean Absolute Error (MAE)**
More robust to outliers than MSE.

## Tree Building Algorithm (ID3/C4.5/CART)

1. Start with all data at root
2. For each feature:
   - Calculate impurity reduction for all possible splits
3. Select feature and split with maximum gain
4. Recursively apply to child nodes
5. Stop when:
   - Max depth reached
   - Min samples per node
   - No information gain
   - Node is pure (single class)

## Complexity Analysis
| Operation | Time Complexity | Space Complexity |
|-----------|-----------------|------------------|
| Training | O(n * d * log(n)) | O(n) |
| Prediction | O(log(n)) to O(n) | O(1) |

Where n = samples, d = features

## Preventing Overfitting

### Pre-pruning (Early Stopping)
- Set max_depth
- Set min_samples_split
- Set min_samples_leaf
- Set max_features

### Post-pruning
- Build full tree, then remove branches
- Cost-complexity pruning (alpha parameter)
- Reduced error pruning

## Advantages
- Easy to understand and interpret
- Handles both numerical and categorical data
- Requires little data preprocessing
- Feature importance built-in
- Handles non-linear relationships

## Disadvantages
- Prone to overfitting
- Unstable (small changes in data cause large tree changes)
- Greedy algorithm may not find global optimum
- Biased toward features with more levels

## Real-World Applications
- Medical diagnosis
- Credit scoring
- Customer segmentation
- Fraud detection
- Recommendation systems

## Summary
- Decision trees split data recursively based on feature tests
- Use Gini impurity or entropy for classification
- Use MSE/MAE for regression
- Prone to overfitting; use pruning or ensembles
- Foundation for Random Forest and Gradient Boosting
