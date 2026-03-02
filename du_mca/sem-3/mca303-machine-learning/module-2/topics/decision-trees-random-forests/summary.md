# Decision Trees and Random Forests - Summary

## Key Definitions and Concepts

- **Decision Tree**: A supervised learning algorithm that creates a hierarchical tree-like model of decisions based on feature values, with internal nodes representing tests on features and leaf nodes representing class labels
- **Entropy**: A measure of randomness or impurity in a dataset, calculated as $H(S) = -\sum_{i=1}^{c} p_i \log_2(p_i)$
- **Information Gain**: The reduction in entropy achieved by splitting data on a feature; the feature with maximum information gain is selected for splitting
- **Gini Index**: An alternative impurity measure used by CART algorithm: $Gini(S) = 1 - \sum_{i=1}^{c} p_i^2$
- **Random Forest**: An ensemble method combining multiple decision trees through bagging and feature randomness to improve prediction accuracy
- **Bagging (Bootstrap Aggregating)**: Training each tree on a bootstrap sample (random sampling with replacement) from the original dataset

## Important Formulas and Theorems

- **Entropy**: $H(S) = -\sum_{i=1}^{c} p_i \log_2(p_i)$ — ranges from 0 (pure) to $\log_2(c)$ (maximum impurity)
- **Information Gain**: $IG(S, A) = H(S) - \sum_{v \in Values(A)} \frac{|S_v|}{|S|} H(S_v)$ — selects feature with highest value
- **Gini Index**: $Gini(S) = 1 - \sum_{i=1}^{c} p_i^2$ — computationally simpler than entropy
- **Random Forest Classification**: Majority voting across all trees
- **Random Forest Regression**: Average of all tree predictions
- **OOB Error**: Validation error estimated using out-of-bag samples (~36.8% of data not used in each tree's training)

## Key Points

- Decision trees are highly interpretable but prone to overfitting, especially with deep trees
- ID3 uses information gain while CART uses Gini Index for selecting split features
- Information gain favors features with more unique values, potentially causing overfitting
- Pruning (pre-pruning or post-pruning) is essential to prevent overfitting
- Random Forests achieve lower variance than single decision trees through ensemble averaging
- Feature randomness (typically $\sqrt{p}$ features at each split) decorrelates trees
- Random Forests require more computational resources but provide better generalization
- OOB error provides built-in model validation without separate test data
- The number of trees in Random Forest is a hyperparameter that doesn't cause overfitting (unlike tree depth)

## Common Mistakes to Avoid

- Confusing entropy with information gain — entropy measures impurity while information gain measures reduction in entropy
- Using information gain without considering feature cardinality — features with more values artificially inflate information gain
- Setting tree depth too high causes overfitting; too low causes underfitting
- Assuming more trees always means better performance — diminishing returns occur after a point

## Revision Tips

- Practice calculating entropy and information gain with numerical examples until you can do them quickly
- Memorize the key differences between ID3 (entropy), CART (Gini), and Random Forest (ensemble)
- Understand why Random Forests reduce variance: diversity through bootstrap and feature randomness
- Review the mathematical formulas for entropy, Gini, and information gain before the exam
- Know the trade-off: Decision Trees = interpretable but higher variance; Random Forests = less interpretable but lower variance