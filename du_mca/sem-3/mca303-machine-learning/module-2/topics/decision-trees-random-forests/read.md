# Decision Trees & Random Forests

## Introduction
Decision Trees are versatile supervised learning algorithms used for both classification and regression tasks. Their tree-like structure mimics human decision-making processes, making them interpretable and valuable for business applications. At DU's MCA program, understanding these algorithms forms the foundation for more complex ensemble methods.

Random Forests address Decision Trees' tendency to overfit by combining multiple decorrelated trees through bagging and feature randomness. This ensemble technique significantly improves generalization while maintaining reasonable interpretability. These methods are particularly valuable in industries like banking (credit scoring), healthcare (diagnosis systems), and e-commerce (recommender systems).

The importance of these algorithms lies in their balance between performance and interpretability. While deep learning models act as "black boxes," decision trees provide clear decision rules compliant with regulations like GDPR's right to explanation. Random Forests add robustness while preserving this explainability through feature importance metrics.

## Key Concepts
1. **Decision Tree Components**:
   - Root Node: Initial feature split
   - Internal Nodes: Decision points with splitting criteria
   - Leaves: Terminal nodes with class labels/probabilities
   - Splitting Criteria: Gini Impurity (1 - Σp_i²), Entropy (-Σp_i log₂p_i), Information Gain

2. **Tree Construction**:
   - Recursive binary splitting (ID3/C4.5/CART algorithms)
   - Pre-pruning (max_depth, min_samples_split)
   - Post-pruning (cost complexity pruning)

3. **Random Forest Mechanics**:
   - Bagging (Bootstrap Aggregating): Training multiple trees on random subsets of data
   - Feature Randomness: √n features considered per split (for n total features)
   - Out-of-Bag (OOB) Error: Unseen data evaluation without separate validation set

4. **Advanced Concepts**:
   - Feature Importance Calculation: Mean decrease in impurity
   - Partial Dependence Plots: Visualizing feature effects
   - Extremely Randomized Trees (ExtraTrees): Additional randomization in splits

## Examples

**Example 1: Building Decision Tree for Play Tennis Dataset**
*Dataset*: 14 instances with Outlook, Temp, Humidity, Wind attributes

**Step 1**: Calculate root node using Information Gain:
- Original Entropy: - (9/14)log₂(9/14) - (5/14)log₂(5/14) = 0.940
- Outlook (Sunny/Overcast/Rain) gives highest IG (0.246)

**Step 2**: Split on Outlook. Sunny branch:
- New Entropy: 0.971 (3 instances: 2 No, 1 Yes)
- Next best split: Humidity (IG=0.971-0.667=0.304)

**Step 3**: Repeat until pure leaves or stopping criteria

**Example 2: Random Forest on Iris Dataset**
```python
from sklearn.ensemble import RandomForestClassifier
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target)

rf = RandomForestClassifier(n_estimators=100, oob_score=True)
rf.fit(X_train, y_train)
print(f"OOB Score: {rf.oob_score_:.2f}")
print(f"Feature Importances: {rf.feature_importances_}")
```

**Example 3: Hyperparameter Tuning Comparison**
Compare accuracy of:
1. Single Decision Tree (max_depth=5)
2. Random Forest (n_estimators=50)
3. Random Forest (n_estimators=200)

Using 10-fold CV on Breast Cancer dataset:
- Single Tree: 92.3% ± 1.2
- RF-50: 96.1% ± 0.8
- RF-200: 96.4% ± 0.7

## Exam Tips
1. Always mention both Gini and Entropy when discussing splitting criteria, noting Gini is faster computationally
2. For "Advantages of Random Forest", emphasize error reduction through variance decrease (bagging) and bias control (feature randomness)
3. When asked about overfitting, contrast pre-pruning vs post-pruning in Decision Trees
4. In numerical problems, derive Information Gain step-by-step using Entropy calculations
5. For feature importance questions, explain the mean decrease in impurity across all trees
6. Remember Random Forest's OOB error can replace cross-validation in some scenarios
7. When comparing algorithms, mention Random Forest's parallelizability vs single tree limitations