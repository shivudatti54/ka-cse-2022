# Model Evaluation Metrics - Summary

## Key Definitions and Concepts

- **Confusion Matrix**: A table showing TP, TN, FP, FN values for evaluating classification models
- **Precision**: Correctness of positive predictions = TP/(TP+FP)
- **Recall (Sensitivity)**: Ability to find all positive instances = TP/(TP+FN)
- **F1-Score**: Harmonic mean of precision and recall = 2×(P×R)/(P+R)
- **ROC Curve**: Plots TPR vs FPR across classification thresholds
- **AUC**: Area under ROC curve; measures discriminative ability (0.5=random, 1.0=perfect)
- **Log Loss**: Penalizes confident wrong predictions in probabilistic classifiers
- **MAE**: Mean absolute error = average absolute difference
- **MSE**: Mean squared error = average squared difference
- **RMSE**: Root mean squared error = √MSE
- **R-squared**: Proportion of variance explained by the model

## Important Formulas and Theorems

- Accuracy = (TP+TN)/(TP+TN+FP+FN)
- F1-Score = 2 × Precision × Recall / (Precision + Recall)
- TPR (Recall) = TP/(TP+FN), FPR = FP/(FP+TN)
- Total Error = Bias² + Variance + Irreducible Error

## Key Points

1. Accuracy is misleading for imbalanced datasets; use precision, recall, F1-score instead
2. High precision means low false positives; high recall means low false negatives
3. F1-score balances precision and recall when costs of errors are similar
4. AUC is threshold-independent and works well for imbalanced data
5. Log loss heavily penalizes confident wrong predictions
6. RMSE penalizes large errors more than MAE due to squaring
7. R² can increase with added predictors; use Adjusted R² for multi-linear regression
8. K-fold cross-validation provides more reliable estimates than single train-test split
9. Stratified K-fold maintains class distribution in imbalanced datasets
10. Model selection should consider both performance metrics and business requirements

## Common Mistakes to Avoid

1. Using accuracy alone for imbalanced classification problems
2. Confusing precision and recall definitions in exam questions
3. Forgetting that F1-score is the harmonic mean, not arithmetic mean
4. Interpreting RMSE in the same units as the target variable (it's squared)
5. Selecting a model with highest accuracy instead of domain-appropriate metric

## Revision Tips

1. Practice calculating all metrics from confusion matrix values until automatic
2. Draw ROC curves and visualize how threshold changes affect TPR and FPR
3. Solve at least 3-4 numerical problems from previous year question papers
4. Create a decision tree for metric selection based on problem type and data balance
5. Memorize the bias-variance tradeoff formula and understand its graphical representation