# Hyperparameter Tuning and Cross-Validation - Summary

## Key Definitions and Concepts

- **Hyperparameters**: Configuration settings set before training (e.g., learning rate, tree depth, number of clusters) that control the learning process. Unlike model parameters, they are not learned from data.
- **Model Parameters**: Weights and coefficients learned automatically during training (e.g., regression coefficients, neural network weights).
- **Cross-Validation**: A resampling technique that partitions data into complementary subsets, training on some and validating on others to assess generalization performance.
- **Grid Search**: Exhaustive search over all possible hyperparameter combinations in a predefined grid.
- **Random Search**: Randomly samples hyperparameter combinations from specified distributions, often more efficient than grid search.
- **Stratified K-Fold**: Cross-validation that preserves class proportions in each fold, essential for imbalanced datasets.
- **Nested Cross-Validation**: Two-layer CV where inner loop tunes hyperparameters and outer loop evaluates model performance.

## Important Formulas and Theorems

- **Grid Search Complexity**: O(Π|param_i| × K), where Π is the product of options for each hyperparameter and K is the number of CV folds.
- **Bias-Variance Tradeoff in CV**: E[error] = Bias² + Variance + Irreducible Error. Larger K reduces bias but increases variance in performance estimates.
- **Standard K-Fold**: Data divided into K equal folds; model trained K times using K-1 folds for training, 1 for validation; average performance reported.

## Key Points

1. Hyperparameters control model complexity—too complex leads to overfitting, too simple causes underfitting.
2. Grid Search is exhaustive but computationally expensive; Random Search is often more efficient.
3. K=10 is a standard choice for K-Fold CV, balancing bias and variance effectively.
4. Always use Stratified K-Fold for classification with imbalanced classes to maintain representative folds.
5. Time series data requires temporal cross-validation, not random splitting, to prevent data leakage.
6. Nested cross-validation provides unbiased performance estimates during hyperparameter tuning.
7. Bayesian Optimization builds probabilistic models to intelligently select promising hyperparameter combinations.
8. The test set should never influence hyperparameter selection—only final model evaluation.
9. Regularization hyperparameters (C, alpha, lambda) control model complexity and prevent overfitting.
10. Computational cost increases dramatically with more hyperparameters—consider starting with a small search space.

## Common Mistakes to Avoid

- **Using the same data for both hyperparameter tuning and evaluation**: This causes data leakage and overly optimistic estimates.
- **Ignoring class imbalance**: Standard K-Fold can produce folds with no examples of minority classes.
- **Choosing K too small**: K=2 leads to high bias in performance estimates; K=n (LOOCV) has high variance.
- **Not using stratified sampling**: For classification problems, always preserve class distribution across folds.
- **Assuming more complex models are better**: Without proper tuning, complex models overfit training data.

## Revision Tips

1. Practice implementing GridSearchCV and RandomizedSearchCV on standard datasets like Iris or Titanic.
2. Memorize when to use each CV strategy: Stratified for classification, Time Series for temporal data.
3. Understand the computational tradeoffs: Grid vs Random vs Bayesian optimization.
4. Review Scikit-Learn documentation for practical implementation details.
5. Solve previous year DU exam questions on hyperparameter tuning to understand the expected answer format.