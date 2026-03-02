# Classification Evaluation Metrics - Summary

## Key Definitions and Concepts

- **Confusion Matrix**: A table summarizing classification predictions against actual labels, containing True Positives (TP), True Negatives (TN), False Positives (FP), and False Negatives (FN).
- **Type I Error (False Positive)**: Incorrectly predicting a negative instance as positive.
- **Type II Error (False Negative)**: Incorrectly predicting a positive instance as negative.
- **Precision**: Proportion of correct positive predictions out of all positive predictions made.
- **Recall (Sensitivity/TPR)**: Proportion of actual positives correctly identified.
- **Specificity (TNR)**: Proportion of actual negatives correctly identified.
- **F1-Score**: Harmonic mean of precision and recall, providing a balanced measure.

## Important Formulas and Theorems

- **Accuracy** = (TP + TN) / (TP + TN + FP + FN)
- **Precision** = TP / (TP + FP)
- **Recall** = TP / (TP + FN) = TPR
- **Specificity** = TN / (TN + FP)
- **F1-Score** = 2 × (Precision × Recall) / (Precision + Recall)
- **FPR** = FP / (FP + TN)
- **F-beta** = (1 + β²) × (P × R) / (β² × P + R)
- **MCC** = (TP × TN - FP × FN) / √((TP+FP)(TP+FN)(TN+FP)(TN+FN))

## Key Points

- Accuracy is misleading for imbalanced datasets—a model predicting only the majority class can achieve high accuracy.
- High precision minimizes false positives; high recall minimizes false negatives.
- F1-Score is the harmonic mean, penalizing models that sacrifice one metric for the other.
- ROC curve plots TPR vs FPR across all thresholds; AUC represents discriminative ability.
- AUC of 0.5 indicates random classification; AUC of 1.0 indicates perfect classification.
- Log Loss penalizes confident wrong predictions in probabilistic classifiers.
- Always consider the domain context and cost of errors when selecting evaluation metrics.

## Common Mistakes to Avoid

1. Confusing False Positives with False Negatives—remember FP predicts positive when actual is negative.
2. Using accuracy alone for imbalanced datasets without checking class distribution.
3. Interpreting AUC as accuracy—it is the probability of ranking a positive above a negative.
4. Forgetting that precision and recall have an inverse relationship; improving one may worsen the other.
5. Not specifying which class is "positive" when calculating metrics in multi-class scenarios.

## Revision Tips

1. Practice constructing confusion matrices from raw prediction data.
2. Calculate all metrics (Accuracy, Precision, Recall, F1-Score, Specificity) from the same confusion matrix.
3. Draw and interpret ROC curves—understand how threshold changes affect TPR and FPR.
4. Solve domain-specific problems: identify whether false positives or false negatives are more costly.
5. Compare classifiers using AUC values and understand what the differences mean practically.