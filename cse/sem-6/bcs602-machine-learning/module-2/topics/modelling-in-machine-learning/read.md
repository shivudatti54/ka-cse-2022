# Modelling in Machine Learning

## 1. Introduction and Formal Definitions

A **model** in machine learning is a mathematical representation that captures the underlying relationship between input features and output predictions. Formally, given an input feature vector **x** ∈ ℝⁿ, the model produces an output **y** through a learned function f: ℝⁿ → ℝ (for regression) or f: ℝⁿ → {0, 1} (for classification). This relationship is expressed as **y = f(x; θ)**, where θ represents the model parameters learned from training data.

The **hypothesis space** H (denoted as 𝒣) is the set of all possible functions that a learning algorithm can represent. For instance, in linear regression, 𝒣 = {h(x) = wᵀx + b : w ∈ ℝⁿ, b ∈ ℝ}. The learning problem seeks to find the hypothesis h\* ∈ 𝒣 that minimizes the **expected risk** (or true error):

$$R(h) = \mathbb{E}_{(x,y) \sim P}[L(y, h(x))]$$

Since the underlying distribution P is unknown, we minimize **empirical risk** on training data:

$$\hat{R}(h) = \frac{1}{m}\sum_{i=1}^{m}L(y_i, h(x_i))$$

where m is the number of training samples.

## 2. Types of Models: Parametric vs Non-Parametric

### 2.1 Parametric Models

Parametric models assume a **fixed functional form** with a finite number of parameters, regardless of training data size.

**Definition:** A model is parametric if its hypothesis space has bounded VC dimension and the number of parameters is independent of n (training size).

**Mathematical Form:**

$$h(x; \theta) = f(x; \theta_1, \theta_2, ..., \theta_k)$$

where k ∈ ℕ is fixed.

**Proof of Fixed Parameter Count:**
Given training data D = {(x₁,y₁), ..., (xₘ,yₘ)}, parametric models satisfy:

$$\lim_{m \to \infty} \text{VCdim}(H) = O(1)$$

This ensures that the model's capacity remains bounded, leading to faster convergence.

### 2.2 Non-Parametric Models

Non-parametric models make **no fixed assumption** about functional form; complexity grows with data.

**Definition:** A model is non-parametric if the number of effective parameters grows with sample size m: k(m) → ∞ as m → ∞.

**Formal Characterization:**

- **K-Nearest Neighbors (KNN):** Effective parameters = k (the number of neighbors), which determines local neighborhoods
- **Decision Trees:** Number of nodes grows with data complexity
- **Kernel Methods:** Number of support vectors scales with data

### 2.3 Comparative Analysis

| Aspect             | Parametric          | Non-Parametric     |
| ------------------ | ------------------- | ------------------ |
| Assumptions        | Strong (fixed form) | Weak (data-driven) |
| Parameters         | Fixed k             | k(m) → ∞ as m → ∞  |
| Sample Complexity  | O(k)                | O(k log k)         |
| Computational Cost | O(md + k³)          | O(md × iterations) |
| Risk               | Underfitting        | Overfitting        |
| Interpretability   | High                | Moderate to Low    |

**Theorem (No Free Lunch):** No model universally dominates others across all problems. The choice depends on:

1. Sample size m
2. Intrinsic dimensionality d
3. Noise level σ²
4. True function complexity

## 3. Hypothesis Space and Risk Minimization

### 3.1 Empirical Risk Minimization (ERM)

Given hypothesis space 𝒣 and loss function L, ERM selects:

$$h^* = \arg\min_{h \in \mathcal{H}} \hat{R}_m(h) = \arg\min_{h \in \mathcal{H}} \frac{1}{m}\sum_{i=1}^{m}L(y_i, h(x_i))$$

### 3.2 Proof: Optimal Linear Regression Solution

For linear regression with MSE loss, we derive the normal equations:

**Given:** Training data {(x₁,y₁), ..., (xₘ,yₘ)}, model h(x) = Xw where X ∈ ℝ^(m×n)

**Objective:** Minimize J(w) = ||Xw - y||²

**Proof:**
$$\nabla_w J(w) = 2X^T(Xw - y) = 0$$

This yields the **normal equations**:
$$X^T X w^* = X^T y$$

**Solution:**
$$w^* = (X^T X)^{-1} X^T y$$

This is the **Ordinary Least Squares (OLS)** estimator, which is:

- Unbiased: E[w*] = w (under assumptions)
- Consistent: w\* → w as m → ∞
- Minimum variance among linear unbiased estimators (Gauss-Markov theorem)

### 3.3 Regularization Context

To prevent overfitting in high-dimensional settings, we add regularization:

**Ridge Regression (L2):**
$$w^* = \arg\min_w ||Xw - y||^2 + \lambda ||w||_2^2 = (X^T X + \lambda I)^{-1}X^T y$$

**Lasso Regression (L1):**
$$w^* = \arg\min_w \frac{1}{2m}||Xw - y||_2^2 + \lambda ||w||_1$$

## 4. Model Complexity and the Bias-Variance Tradeoff

### 4.1 Formal Decomposition

For regression with squared error loss, the expected prediction error at x₀ is:

$$\mathbb{E}[(y - \hat{f}(x_0))^2] = \text{Bias}^2(\hat{f}) + \text{Var}(\hat{f}) + \sigma^2$$

**Proof of Decomposition:**

Let f(x) be the true function and ε ~ N(0, σ²) be irreducible noise, where y = f(x) + ε.

$$\mathbb{E}[(y - \hat{f})^2] = \mathbb{E}[(f + \varepsilon - \hat{f})^2]$$
$$= \mathbb{E}[(f - \hat{f})^2] + \mathbb{E}[\varepsilon^2] + 2\mathbb{E}[\varepsilon(f - \hat{f})]$$

Since E[ε] = 0 and ε is independent of (f - \hat{f}):
$$= \mathbb{E}[(f - \hat{f})^2] + \sigma^2$$

Now, decompose E[(f - \hat{f})²]:
$$= \mathbb{E}[(f - \mathbb{E}[\hat{f}] + \mathbb{E}[\hat{f}] - \hat{f})^2]$$
$$= (f - \mathbb{E}[\hat{f}])^2 + \mathbb{E}[(\mathbb{E}[\hat{f}] - \hat{f})^2]$$
$$= \text{Bias}^2(\hat{f}) + \text{Var}(\hat{f})$$

Where:

- **Bias²:** (f - E[ŵ])² — measures how well the average model fits the true function
- **Variance:** E[(E[ŵ] - ŵ)²] — measures model sensitivity to training data

### 4.2 Implications for Model Selection

| Model Type              | Bias | Variance  | Typical Behavior                  |
| ----------------------- | ---- | --------- | --------------------------------- |
| Linear Regression       | High | Low       | Underfits                         |
| KNN (k=1)               | Low  | High      | Overfits                          |
| KNN (k large)           | High | Low       | Underfits                         |
| Decision Tree (shallow) | High | Low       | Underfits                         |
| Deep Neural Network     | Low  | Very High | Overfits (without regularization) |

**Optimal Complexity:** Choose model complexity that balances:
$$\text{Complexity}^* = \arg\min \text{Bias}^2 + \text{Var} + \text{Irreducible Error}$$

## 5. Loss Functions and Their Properties

### 5.1 Regression: Mean Squared Error (MSE)

$$L(y, \hat{y}) = (y - \hat{y})^2$$

**Properties:**

- Differentiable everywhere
- Penalizes large errors quadratically
- Not robust to outliers

### 5.2 Classification: Cross-Entropy Loss

For binary classification with sigmoid σ(z) = 1/(1+e⁻ᶻ):

$$L(y, p) = -[y \log p + (1-y) \log(1-p)]$$

**Proof of Gradient (Logistic Regression):**
Given h(x) = σ(wᵀx + b), for a single sample:

$$\frac{\partial L}{\partial w_j} = (h(x) - y)x_j$$

This gradient drives updates toward minimizing prediction error.

## 6. Model Selection Criteria

### 6.1 Information Criteria

**Akaike Information Criterion (AIC):**
$$\text{AIC} = 2k - 2\ln(\hat{L})$$

**Bayesian Information Criterion (BIC):**
$$\text{BIC} = k\ln(m) - 2\ln(\hat{L})$$

Where k = number of parameters, m = sample size, \hat{L} = maximized likelihood.

**Selection Rule:** Lower AIC/BIC indicates better model. BIC penalizes complexity more heavily for large m.

### 6.2 Cross-Validation

**k-Fold Cross-Validation:**

1. Split data into k folds
2. Train on k-1 folds, validate on 1 fold
3. Repeat k times, average validation error
4. Select model with minimum average error

**Bias-Variance Tradeoff in CV:**

- Low k (e.g., 2): Low bias, high variance in estimate
- High k (e.g., 10): Higher bias, lower variance

## 7. Practice Problems

### Multiple Choice Questions (Hard)

**Question 1:** A researcher has m=100 training samples with n=50 features. Comparing linear regression (LR) vs KNN (k=5), which statement is TRUE?

A) LR will always outperform KNN due to lower variance
B) KNN will always outperform LR due to flexibility
C) LR is preferred if the true relationship is approximately linear
D) Neither model can be applied due to n > m

**Answer: C** — When n > m, regularized LR (ridge/lasso) is preferred. KNN fails in high dimensions due to curse of dimensionality. LR captures linear relationships well if assumptions hold.

---

**Question 2:** Given training MSE = 0.1 and test MSE = 2.5 for a polynomial regression of degree 10 trained on 50 samples, the model exhibits:

A) High bias, underfitting
B) Low bias, high variance (overfitting)
C) Optimal generalization
D) Irreducible error dominance

**Answer: B** — Large gap between train and test error indicates overfitting (high variance). Degree 10 polynomial with 50 samples has effective parameters >> 50, leading to memorization.

---

**Question 3:** For ridge regression with λ → ∞, the model approaches:

A) Zero variance
B) Zero bias
C) Predicting the mean of training labels
D) Perfect interpolation

**Answer: C** — As λ → ∞, coefficients shrink to zero: ŵ → 0, so ŷ → b (mean of y).

---

**Question 4:** A linear model has 10,000 parameters and is trained on 1 million samples. The AIC value is dominated by:

A) Likelihood term
B) Number of parameters
C) Sample size
D) Neither; AIC is undefined

**Answer: B** — With m = 10⁶, k = 10⁴, the penalty term 2k = 20,000 dominates unless likelihood is astronomically high. Complex models are penalized heavily.

---

**Question 5:** Which model has effective degrees of freedom closest to m (training size)?

A) Linear regression with 5 features
B) KNN with k=1
C) KNN with k=m
D) Ridge regression with λ=0

**Answer: B** — KNN with k=1 has effective degrees of freedom ≈ m (each training point influences one prediction). KNN with k=m has df ≈ 1 (global mean).
