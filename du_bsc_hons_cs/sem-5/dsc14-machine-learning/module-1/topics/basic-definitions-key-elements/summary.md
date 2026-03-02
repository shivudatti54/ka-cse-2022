# Basic Definitions and Key Elements of Machine Learning - Summary

## Key Definitions and Concepts

- **Machine Learning**: The study of algorithms that improve automatically through experience and data. Tom M. Mitchell's definition: "A computer program learns from experience E with respect to task T if its performance at T, measured by P, improves with experience E."
- **Supervised Learning**: Learning from labeled data to predict outputs; includes classification (categorical) and regression (continuous) tasks
- **Unsupervised Learning**: Learning from unlabeled data to find hidden patterns; includes clustering and dimensionality reduction
- **Reinforcement Learning**: Learning through interaction with an environment, maximizing cumulative rewards

## Important Formulas and Metrics

- **Classification Metrics**: Accuracy = (TP + TN) / (TP + TN + FP + FN); Precision = TP / (TP + FP); Recall = TP / (TP + FN); F1 = 2 × (Precision × Recall) / (Precision + Recall)
- **Regression Metrics**: MSE = (1/n) × Σ(yᵢ - ŷᵢ)²; RMSE = √MSE; R² = 1 - (SS_res / SS_tot)

## Key Points

1. Machine learning differs from traditional programming by learning patterns from data rather than following explicit rules
2. Data quality and quantity are fundamental to ML success—garbage in, garbage out
3. Features are measurable properties; feature engineering converts raw data into meaningful inputs
4. Models range from simple (Linear Regression) to complex (Deep Neural Networks)
5. Training involves optimization—minimizing error between predictions and actual values
6. Generalization to unseen data is the ultimate goal, not just training performance
7. Overfitting: model performs well on training but poorly on test data
8. Underfitting: model is too simple to capture patterns in data
9. Typical split: 70-80% training, 20-30% testing; use validation set for tuning

## Common Mistakes to Avoid

- Confusing classification with regression—classification predicts categories, regression predicts continuous values
- Treating test data as part of training—information leakage leads to inflated performance estimates
- Ignoring data preprocessing—missing values and outliers must be handled appropriately
- Choosing wrong evaluation metric—accuracy is misleading with imbalanced classes

## Revision Tips

1. Practice drawing and explaining the machine learning workflow diagram
2. Memorize Mitchell's definition word-for-word as it frequently appears in exams
3. For each ML type, recall one real-world application example
4. Understand bias-variance tradeoff conceptually, not just definitions
5. Review evaluation metrics for both classification and regression problems