# Linear & Logistic Regression

## Introduction
Linear and logistic regression form the foundation of supervised learning in machine learning. Linear regression models continuous outcomes through linear relationships between variables, while logistic regression predicts categorical outcomes using probabilistic methods. These algorithms are essential for understanding more complex ML concepts and widely used in industry for tasks like sales forecasting (linear) and customer churn prediction (logistic).

In DU's MCA program, mastery of these techniques is critical for implementing predictive analytics solutions. Linear regression helps analyze variable relationships in domains like economics and engineering, while logistic regression forms the basis for classification systems in healthcare diagnostics and fraud detection. Both methods emphasize the importance of proper feature engineering and model validation - skills highly valued in industry roles.

## Key Concepts
1. **Linear Regression**
- Hypothesis Function: hθ(x) = θ₀ + θ₁x₁ + ... + θₙxₙ
- Cost Function: Mean Squared Error (MSE) = 1/(2m) Σ(hθ(xⁱ) - yⁱ)²
- Gradient Descent: Simultaneous update of θⱼ := θⱼ - α ∂/∂θⱼ J(θ)
- Assumptions: Linear relationship, multivariate normality, no multicollinearity

2. **Logistic Regression**
- Sigmoid Function: g(z) = 1/(1+e⁻ᶻ)
- Decision Boundary: Threshold (typically 0.5) for classification
- Maximum Likelihood Estimation: Optimize log-likelihood function
- Regularization: L1/L2 penalties to prevent overfitting

3. **Model Evaluation**
- R² Score and RMSE for linear regression
- Confusion Matrix, ROC-AUC for logistic regression
- Bias-Variance Tradeoff analysis

## Examples

**Example 1: Linear Regression Implementation**
```python
# House Price Prediction
import numpy as np
X = np.array([[1, 2104], [1, 1416], [1, 1534]])  # Features with bias term
y = np.array([460, 232, 315])
theta = np.linalg.inv(X.T @ X) @ X.T @ y
print("Optimal parameters:", theta)  # Output: [ 1.125e+02  1.806e-01]
```

**Example 2: Logistic Regression Decision Boundary**
```python
# Student Admission Prediction
from sklearn.linear_model import LogisticRegression
X = [[85], [72], [95], [60]]  # Exam scores
y = [1, 0, 1, 0]
model = LogisticRegression().fit(X, y)
print("Admission probability at 80:", model.predict_proba([[80]])[0][1])
# Output: 0.78 (78% chance of admission)
```

**Example 3: Regularized Logistic Regression**
```python
# Fraud Detection with L2 Regularization
from sklearn.linear_model import LogisticRegression
model = LogisticRegression(penalty='l2', C=0.1)
model.fit(X_train, y_train)
print("Feature coefficients:", model.coef_)
# Shows how regularization shrinks coefficients
```

## Exam Tips
1. Always check linear regression assumptions before interpreting results
2. For logistic regression, remember the decision boundary is at 0.5 by default
3. Use regularization (λ > 0) when dealing with high-dimensional data
4. Matrix form (Xθ = y) is crucial for computational efficiency
5. ROC curve analysis is better than accuracy for imbalanced datasets
6. Understand the difference between closed-form solution and gradient descent
7. Multicollinearity affects coefficient stability in linear regression