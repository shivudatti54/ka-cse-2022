# Regularization Techniques in Machine Learning

## Introduction
Regularization techniques form the cornerstone of modern machine learning systems, addressing the fundamental challenge of model overfitting. In the context of DU's research-oriented MSc CS program, understanding these methods is crucial for developing robust predictive models that generalize well to unseen data.

The bias-variance tradeoff lies at the heart of regularization theory. Complex models with high variance tend to memorize training data, while oversimplified models suffer from high bias. Regularization introduces controlled constraints to find the optimal balance, enabling models to maintain predictive power while avoiding overfitting to noise in training data.

Current research extends traditional regularization approaches to deep learning architectures, with innovations like adaptive dropout and spectral normalization gaining prominence. These advanced techniques are particularly relevant for DU students working on cutting-edge applications in computer vision and natural language processing.

## Key Concepts

1. **L1 Regularization (Lasso)**
- Adds absolute value of weights to loss function: L = Loss + λΣ|w_i|
- Induces sparsity through feature selection
- Particularly effective for high-dimensional data

2. **L2 Regularization (Ridge)**
- Adds squared magnitude of weights: L = Loss + λΣw_i²
- Prevents extreme weight values through smooth shrinkage
- Closed-form solution: (XᵀX + λI)⁻¹Xᵀy

3. **Elastic Net**
- Hybrid approach combining L1 and L2 penalties
- Loss + λ₁Σ|w_i| + λ₂Σw_i²
- Addresses limitations of pure L1/L2 in correlated features

4. **Dropout (Neural Networks)**
- Randomly deactivates neurons during training
- Forces network to develop redundant representations
- Test-time scaling: Multiply weights by dropout probability

5. **Early Stopping**
- Monitors validation loss during training
- Stops optimization when generalization performance plateaus
- Implicit regularization through optimization trajectory

6. **Data Augmentation**
- Creates synthetic training examples through transformations
- Common in computer vision (rotations, flips) and NLP (synonym replacement)
- Increases effective training data diversity

## Examples

**Example 1: Ridge Regression for Housing Prices**
```python
from sklearn.linear_model import Ridge
import numpy as np

# Synthetic data: 100 samples, 10 features
X = np.random.randn(100, 10)
y = 2*X[:,0] + 0.5*X[:,1] + np.random.normal(0, 0.5, 100)

# Fit with L2 regularization
model = Ridge(alpha=1.0)
model.fit(X, y)
print("Coefficients:", model.coef_)
```
*Solution: The Ridge model shrinks coefficients toward zero while maintaining all features in the model. Compare coefficients with OLS to observe shrinkage effect.*

**Example 2: Feature Selection with Lasso**
```python
from sklearn.linear_model import Lasso

# Create sparse ground truth (only first 2 features relevant)
true_coef = [1.5, -0.7] + [0]*8

model = Lasso(alpha=0.1)
model.fit(X, y)
print("Selected features:", np.nonzero(model.coef_)[0])
```
*Solution: Lasso correctly identifies first two features while zeroing out others. Vary α to observe selection-stability tradeoff.*

**Example 3: Dropout in Neural Networks**
```python
import tensorflow as tf

model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(10)
])
model.compile(optimizer='adam', loss='mse')
```
*Solution: Dropout layer deactivates 50% of neurons randomly during training. Test-time scaling is automatically handled in Keras.*

## Exam Tips
1. Always justify regularization choice: L1 for feature selection, L2 for correlated features
2. Remember Elastic Net's dual λ parameters require careful tuning
3. For neural networks, combine dropout with L2 regularization for enhanced effect
4. Early stopping requires careful validation set design - never use test data
5. In Bayesian interpretation: L2 corresponds to Gaussian prior, L1 to Laplace prior
6. Regularization path analysis (λ vs coefficients) is favorite exam question
7. Recent research focus: Adaptive regularization parameters during training