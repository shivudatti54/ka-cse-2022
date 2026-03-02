# Ensemble Methods: Boosting

## Introduction
Boosting is a powerful ensemble technique that combines multiple weak learners to create a strong learner. Unlike bagging methods that process models in parallel, boosting builds models sequentially where each subsequent model focuses on correcting errors of its predecessor. This approach has revolutionized machine learning by achieving state-of-the-art results in various domains from Kaggle competitions to industrial applications.

The importance of boosting lies in its ability to handle complex datasets through adaptive learning. Algorithms like AdaBoost (1997) laid the foundation, while modern implementations like XGBoost (2016) and LightGBM (2017) dominate real-world applications such as credit risk modeling and recommendation systems. For DU MCA students, understanding boosting is crucial as it's frequently asked in technical interviews and used in India's growing AI/ML sector.

## Key Concepts
1. **Weak Learners**: Base estimators (typically decision trees with depth=1-3) that perform slightly better than random guessing
2. **Error Correction**: Sequential focus on misclassified instances through:
   - Instance re-weighting (AdaBoost)
   - Residual minimization (Gradient Boosting)
3. **Additive Model**: Final prediction = Σ(weight * base_learner_prediction)
4. **Loss Functions**:
   - Exponential loss (AdaBoost)
   - Custom differentiable losses (Gradient Boosting)
5. **Regularization**:
   - Learning rate (shrinkage)
   - Subsampling (Stochastic GB)
   - Tree constraints (depth, leaf nodes)

**Mathematical Foundation**:
AdaBoost weight update:
α_t = 0.5 * ln((1 - err_t)/err_t)
w_i^(t+1) = w_i^(t) * e^(-α_t y_i h_t(x_i))

Gradient Boosting pseudoresiduals:
r_i = -∂L(y_i,F(x_i))/∂F(x_i)

## Examples

**Example 1: AdaBoost Classification**
Dataset: 3 instances with initial weights [1/3, 1/3, 1/3]
1. First weak classifier misclassifies instance 3 → error=1/3
2. α = 0.5 * ln(2) ≈ 0.3466
3. New weights: [0.25, 0.25, 0.5]
4. Second classifier focuses on instance 3

**Example 2: Gradient Boosting Regression**
Predict house prices (target y) using square footage (x):
1. Initial model F0(x) = mean(y)
2. Calculate residuals r1 = y - F0(x)
3. Train h1(x) on (x, r1)
4. Update: F1(x) = F0(x) + η*h1(x) (η=0.1)
5. Repeat for M iterations

**Example 3: XGBoost Optimization**
Objective function = ΣL(y_i,ŷ_i) + ΣΩ(f_k)
Where Ω(f) = γT + 0.5λ||w||² (T=leaves, w=leaf scores)
Uses 2nd-order Taylor approximation for efficient computation

## Exam Tips
1. Always mention the difference between bagging vs boosting in answers
2. Memorize AdaBoost weight update formula and its derivation
3. Practice writing gradient boosting pseudocode from scratch
4. Understand XGBoost's regularization techniques (exam frequently asks comparison with GB)
5. Be prepared to explain bias-variance tradeoff in boosting context
6. Remember real-world applications: fraud detection, customer churn prediction
7. Study the role of learning rate (shrinkage) in model convergence