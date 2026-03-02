# Logistic Regression

## Introduction

Logistic regression is a supervised learning algorithm used for **classification** tasks, despite the word "regression" in its name. It models the probability that an input belongs to a particular class using the logistic (sigmoid) function.

## Why Not Linear Regression for Classification?

Linear regression can predict values outside [0, 1], making it unsuitable for modeling probabilities. Logistic regression solves this by applying the sigmoid function to map the linear output to a probability.

## The Sigmoid (Logistic) Function

σ(z) = 1 / (1 + e^(-z))

**Properties**:

- Output range: (0, 1) - interpretable as probability
- σ(0) = 0.5 (decision boundary)
- σ(z) → 1 as z → +∞
- σ(z) → 0 as z → -∞
- Smooth and differentiable everywhere

## Model Formulation

### Binary Logistic Regression

P(Y = 1 | X) = σ(b₀ + b₁X₁ + b₂X₂ + ... + bₙXₙ) = 1 / (1 + e^(-(b₀ + b₁X₁ + ... + bₙXₙ)))

The model computes a linear combination of features, then passes it through the sigmoid function to get a probability.

### Decision Rule

- If P(Y = 1 | X) ≥ 0.5 → predict class 1
- If P(Y = 1 | X) < 0.5 → predict class 0

The threshold 0.5 can be adjusted based on application requirements.

## Odds and Log-Odds

### Odds

odds = P(Y=1) / P(Y=0) = P / (1-P)

### Log-Odds (Logit)

logit(P) = ln(P / (1-P)) = b₀ + b₁X₁ + ... + bₙXₙ

Logistic regression models the **log-odds** as a linear function of features. This is why it is called a **generalized linear model**.

### Coefficient Interpretation

- Each coefficient bᵢ represents the change in **log-odds** for a one-unit increase in Xᵢ
- e^(bᵢ) gives the **odds ratio**: the factor by which odds are multiplied for a unit increase in Xᵢ
- bᵢ > 0: increasing Xᵢ increases the probability of class 1
- bᵢ < 0: increasing Xᵢ decreases the probability of class 1
- bᵢ = 0: Xᵢ has no effect

## Cost Function

### Why Not MSE?

Using MSE with the sigmoid function creates a non-convex optimization surface with multiple local minima, making optimization unreliable.

### Log-Loss (Binary Cross-Entropy)

L(b) = -(1/m) Σ [yᵢ · log(ŷᵢ) + (1-yᵢ) · log(1-ŷᵢ)]

**Properties**:

- Convex function → guaranteed global minimum
- Heavily penalizes confident wrong predictions
- When y=1: loss = -log(ŷ) (penalizes low predicted probability)
- When y=0: loss = -log(1-ŷ) (penalizes high predicted probability)

### Maximum Likelihood Estimation (MLE)

Minimizing log-loss is equivalent to maximizing the log-likelihood of the observed data. MLE finds the coefficients that make the training data most probable.

## Optimization

### Gradient Descent

Since there is no closed-form solution for logistic regression, we use iterative optimization:

∂L/∂bⱼ = (1/m) Σ (ŷᵢ - yᵢ) · xᵢⱼ

Update rule: bⱼ = bⱼ - α · ∂L/∂bⱼ

Where α is the learning rate.

## Decision Boundary

The decision boundary is where P(Y=1|X) = 0.5, which occurs when:

b₀ + b₁X₁ + ... + bₙXₙ = 0

This is a **linear boundary** in the feature space (a line in 2D, a plane in 3D, a hyperplane in higher dimensions).

## Multi-Class Logistic Regression

### One-vs-Rest (OvR)

- Train K binary classifiers (one per class)
- Each classifier distinguishes one class from all others
- Predict the class with highest probability

### Multinomial (Softmax Regression)

- Directly models all K classes simultaneously
- Uses softmax function: P(Y=k|X) = e^(z_k) / Σe^(z_j)
- All probabilities sum to 1

## Regularization

### L2 Regularized (Ridge)

Minimize: L(b) + λΣbᵢ²

- Prevents overfitting by shrinking coefficients
- No feature elimination

### L1 Regularized (Lasso)

Minimize: L(b) + λΣ|bᵢ|

- Performs feature selection (drives some coefficients to 0)

## Evaluation Metrics

| Metric    | Formula               | Use Case                       |
| --------- | --------------------- | ------------------------------ |
| Accuracy  | (TP+TN)/(TP+TN+FP+FN) | Balanced classes               |
| Precision | TP/(TP+FP)            | When FP cost is high           |
| Recall    | TP/(TP+FN)            | When FN cost is high           |
| F1-Score  | 2·(P·R)/(P+R)         | Balance precision & recall     |
| AUC-ROC   | Area under ROC curve  | Overall discrimination ability |

## Advantages and Limitations

### Advantages

- Simple, fast to train, and interpretable
- Outputs calibrated probabilities
- Works well for linearly separable data
- Easy to regularize

### Limitations

- Assumes linear decision boundary
- Cannot capture complex non-linear patterns without feature engineering
- Sensitive to multicollinearity
- May underfit for complex problems

## Exam Tips

- Know the sigmoid function and its properties
- Be able to derive log-loss and explain why MSE is not suitable
- Understand odds ratios and coefficient interpretation
- Know the difference between OvR and Softmax for multi-class
- Understand the decision boundary is linear

### Example Use Cases

- **Spam vs. Not Spam Emails**: Logistic regression can be used to classify emails as spam or not spam based on features such as the presence of certain keywords, sender reputation, and email content.
- **Credit Risk Assessment**: Logistic regression can be used to predict the probability of a customer defaulting on a loan based on features such as credit score, income, and debt-to-income ratio.
- **Medical Diagnosis**: Logistic regression can be used to predict the probability of a patient having a certain disease based on features such as symptoms, medical history, and test results.

### Code Example

```python
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Load iris dataset
iris = load_iris()
X = iris.data[:, :2] # we only take the first two features.
y = iris.target

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train logistic regression model
logreg = LogisticRegression()
logreg.fit(X_train, y_train)

# Predict on test set
y_pred = logreg.predict(X_test)

# Print accuracy
print("Accuracy:", logreg.score(X_test, y_test))
```
