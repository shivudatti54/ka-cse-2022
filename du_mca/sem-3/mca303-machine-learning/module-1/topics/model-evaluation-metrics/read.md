# Model Evaluation Metrics

## Introduction
Model evaluation metrics are quantitative measures used to assess the performance of machine learning models. In real-world applications, simply training a model is insufficient - we must rigorously evaluate its effectiveness using appropriate statistical measures. Different types of problems (classification, regression, clustering) require different evaluation metrics, and choosing the wrong metric can lead to misleading conclusions about model performance.

The importance of evaluation metrics extends beyond academic exercises. In industry applications, these metrics directly impact business decisions - from medical diagnosis systems requiring high recall to financial fraud detection needing precision. Understanding metrics helps in model comparison, hyperparameter tuning, and meeting regulatory requirements in sensitive domains.

## Key Concepts
1. **Classification Metrics**:
   - Accuracy: (TP+TN)/(TP+TN+FP+FN) - Overall correctness
   - Precision: TP/(TP+FP) - Quality of positive predictions
   - Recall/Sensitivity: TP/(TP+FN) - Coverage of actual positives
   - F1-Score: 2*(Precision*Recall)/(Precision+Recall) - Harmonic mean
   - ROC-AUC: Area under Receiver Operating Characteristic curve
   - Cohen's Kappa: Agreement adjusted for chance
   - Matthews Correlation Coefficient (MCC): Balanced measure for binary classes

2. **Regression Metrics**:
   - MSE (Mean Squared Error): Average squared difference
   - RMSE: Root of MSE - interpretable in target units
   - MAE: Mean Absolute Error - robust to outliers
   - R²: Coefficient of determination - explained variance
   - Adjusted R²: Penalized for unnecessary features

3. **Probabilistic Metrics**:
   - Log-Loss: Cross-entropy loss for probability calibration
   - Brier Score: Mean squared difference in probabilities

4. **Advanced Concepts**:
   - Confusion Matrix Analysis
   - Precision-Recall Tradeoff
   - Bias-Variance Decomposition
   - Cross-Validation Strategies
   - Statistical Significance Testing (McNemar's Test)

## Examples

**Example 1: Medical Diagnosis (Classification)**
Problem: Evaluate a COVID-19 detection model with:
- True Positives = 950
- False Positives = 50
- False Negatives = 150
- True Negatives = 850

Solution:
1. Accuracy = (950+850)/2000 = 0.9
2. Precision = 950/(950+50) = 0.95
3. Recall = 950/(950+150) = 0.8636
4. F1 = 2*(0.95*0.8636)/(0.95+0.8636) = 0.905

**Example 2: House Price Prediction (Regression)**
Actual prices: [200, 300, 400]
Predicted: [210, 290, 390]

1. MAE = (10+10+10)/3 = 10
2. MSE = (100+100+100)/3 = 100
3. RMSE = √100 = 10
4. R² = 1 - (300)/(Total variance)

**Example 3: Fraud Detection (ROC Analysis)**
Calculate TPR and FPR at different thresholds:
- Threshold 0.5: TP=80, FP=20, FN=20, TN=880
- TPR = 80/100 = 0.8
- FPR = 20/900 = 0.022
Plot multiple points to create ROC curve, calculate AUC

## Exam Tips
1. Memorize formulas for F1-score, precision, recall with mnemonics
2. Understand when to use ROC-AUC vs Precision-Recall curves (class imbalance)
3. Practice calculating metrics from confusion matrices
4. Know limitations: Accuracy is misleading for imbalanced data
5. Interpret R² values: 0.7 means 70% variance explained
6. Remember MAE vs RMSE: RMSE penalizes large errors more
7. For clustering, understand silhouette score calculation
8. Always consider business context when choosing metrics