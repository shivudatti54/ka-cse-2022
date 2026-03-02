# **Indicate the Performance of a Model**

### Overview

To evaluate the performance of a machine learning model, we use various metrics that measure how well the model generalizes to unseen data. The choice of metric depends on the type of problem and the characteristics of the data.

### Key Metrics

- **Accuracy**: measures the proportion of correctly classified instances
- **Precision**: measures the proportion of true positives among all positive predictions
- **Recall**: measures the proportion of true positives among all actual positive instances
- **F1-score**: harmonic mean of precision and recall
- **Mean Squared Error (MSE)**: measures the average squared difference between predicted and actual values
- **Mean Absolute Error (MAE)**: measures the average absolute difference between predicted and actual values
- **Root Mean Squared Percentage Error (RMSPE)**: measures the square root of the average squared percentage difference between predicted and actual values

### Important Formulas

- **Accuracy**: P(accuracy) = (TP + TN) / (TP + TN + FP + FN)
- **Precision**: P(precision) = TP / (TP + FP)
- **Recall**: P(recall) = TP / (TP + FN)
- **F1-score**: P(f1-score) = 2 \* (P(precision) \* P(recall)) / (P(precision) + P(recall))
- **MSE**: P(MSE) = Σ (y_true - y_pred)^2 / n
- **MAE**: P(MAE) = Σ |y_true - y_pred| / n
- **RMSPE**: P(RMSPE) = √(Σ (y_true - y_pred)^2 / n)

### Theorems

- **Bayes' Theorem**: P(A|B) = P(A and B) / P(B)
- **Law of Total Probability**: P(A) = P(A|B) \* P(B) + P(A|B') \* P(B')

### Definitions

- **True Positive (TP)**: correctly predicted positive instance
- **False Positive (FP)**: incorrectly predicted positive instance
- **True Negative (TN)**: correctly predicted negative instance
- **False Negative (FN)**: incorrectly predicted negative instance
- **Predicted Probability**: P(y_pred) = P(y_pred|X) \* P(X)

### Revision Tips

- Understand the concept of bias-variance tradeoff
- Familiarize yourself with the importance of overfitting and underfitting
- Know when to use different metrics for classification and regression problems
- Practice calculating metrics for different types of problems

This summary should provide a concise review of the key concepts and formulas for indicating the performance of a machine learning model.
