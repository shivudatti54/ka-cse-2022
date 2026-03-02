# Locally Weighted Regression (LWR)

## Introduction

In traditional linear regression, we derive a single, global model (e.g., `y = θ₀ + θ₁x`) to fit all training data. This model is subsequently applied to make predictions for any new query point. However, this approach frequently fails to capture complex, non-linear relationships in the data, resulting in high bias and poor predictive performance when the underlying function is highly non-linear.

Locally Weighted Regression (LWR), also known as **Loess** (LOcally Estimated Scatterplot Smoothing), represents a powerful **non-parametric** and **instance-based** learning algorithm. Unlike global methods that fit a single model to all data, LWR constructs a distinct local model tailored specifically for each query point. The algorithm achieves this by assigning higher weights to training instances proximate to the query point, effectively fitting a simple model (typically low-order polynomial regression) to a localized neighborhood.

## Theoretical Foundation

### 1. The Local Learning Philosophy

The fundamental principle underlying LWR asserts that to predict the value for a new input `x_q` (query point), greater consideration should be afforded to training examples `(x^(i), y^(i))` that lie in close proximity to `x_q`, with diminished influence bestowed upon distant instances. This approach rests upon the assumption that points proximate in the input space will exhibit similar target values—a smoothness assumption fundamental to non-parametric methods.

### 2. The Weight Function: Gaussian Kernel

The notion of "closeness" is formalized through a **weight function** `w^(i)`, assigned to each training example relative to a given query point `x_q`. The most prevalent weight function employs a **Gaussian Kernel** (radial basis function):

```
w^(i) = exp(-‖x^(i) - x_q‖² / (2τ²))
```

Where:

- `x^(i)` denotes the i-th training input vector
- `x_q` represents the query point for which prediction is desired
- `τ` (tau) signifies the **bandwidth parameter** (also termed smoothing parameter or window width)
- `‖·‖²` denotes the squared Euclidean distance

**Properties of the Gaussian Kernel:**

- The kernel is radially symmetric and positive definite
- Weights are strictly positive: `0 < w^(i) ≤ 1`
- Weights approach zero as distance increases: `lim(‖x^(i) - x_q‖ → ∞) w^(i) = 0`
- The kernel satisfies the reproducing property in Hilbert spaces

### 3. Bandwidth Parameter Analysis

The bandwidth parameter `τ` constitutes the most critical hyperparameter governing algorithm performance:

| τ Value | Kernel Width      | Model Behavior                                                          | Bias-Variance Tradeoff                 |
| ------- | ----------------- | ----------------------------------------------------------------------- | -------------------------------------- |
| Large τ | Wide bell curve   | Distant points retain significant weight; smooth, global-like model     | Low variance, high bias (underfitting) |
| Small τ | Narrow bell curve | Only very close points influence prediction; highly local, wiggly model | High variance, low bias (overfitting)  |

**Mathematical Insight:** As `τ → ∞`, the weight function approaches a constant (`w^(i) ≈ 1`), causing LWR to degenerate to standard ordinary least squares (OLS). Conversely, as `τ → 0`, the algorithm becomes increasingly localized, tending toward interpolation.

## Mathematical Derivation: Weighted Least Squares

### Problem Formulation

For a given query point `x_q`, we seek parameters `θ` that minimize the **weighted cost function**:

```
J(θ) = Σᵢ w^(i) · (y^(i) - θᵀx^(i))²
```

Where:

- `w^(i) = exp(-‖x^(i) - x_q‖² / (2τ²))` are precomputed weights
- `y^(i)` is the target value for the i-th training instance
- `x^(i)` is the feature vector for the i-th training instance
- `θ` is the parameter vector to be optimized

### Derivation of Normal Equations

To find the optimal `θ`, we differentiate `J(θ)` with respect to `θ` and set the gradient to zero:

```
∂J/∂θ = -2 · Σᵢ w^(i) · x^(i) · (y^(i) - θᵀx^(i)) = 0
```

Rearranging terms:

```
Σᵢ w^(i) · x^(i)y^(i) = Σᵢ w^(i) · x^(i)θᵀx^(i)
```

Expressing in matrix notation, let:

- `X` be the design matrix of shape `(m, n)` where `m` = number of training examples, `n` = number of features
- `y` be the target vector of shape `(m, 1)`
- `W` be a diagonal weight matrix of shape `(m, m)` with `W_{ii} = w^(i)`

The **weighted normal equations** are:

```
XᵀW X θ = XᵀW y
```

Assuming `XᵀW X` is invertible (positive definite), the closed-form solution is:

```
θ̂ = (XᵀW X)⁻¹ XᵀW y
```

**Proof of Uniqueness:** The matrix `XᵀW X` is positive definite (and hence invertible) provided:

1. `X` has full column rank (linearly independent columns)
2. All weights `w^(i) > 0` (satisfied by Gaussian kernel for distinct query points)

This guarantees a unique solution for `θ̂`.

## The LWR Algorithm

### Pseudocode

```
ALGORITHM: Locally Weighted Regression
INPUT: Training set {(x^(i), y^(i))}_{i=1}^{m}, query point x_q, bandwidth τ
OUTPUT: Prediction ŷ_q

1: PROCEDURE LWR(x_q):
2:     // Step 1: Compute weights for all training instances
3:     FOR i = 1 to m DO:
4:         d^(i) = ‖x^(i) - x_q‖²          // Squared Euclidean distance
5:         w^(i) = exp(-d^(i) / (2τ²))     // Gaussian kernel weight
6:     END FOR
7:
8:     // Step 2: Construct weight matrix W
9:     W = diag(w^(1), w^(2), ..., w^(m))
10:
11:    // Step 3: Solve weighted least squares
12:    θ̂ = (XᵀW X)⁻¹ XᵀW y                 // From normal equations
13:
14:    // Step 4: Make prediction
15:    ŷ_q = θ̂ᵀ · x_q
16:
17:    RETURN ŷ_q
18: END PROCEDURE
```

### Algorithm Characteristics

- **Non-Parametric Nature:** LWR makes no prior assumptions regarding the functional form of `f(x)`. Model complexity adapts dynamically based on data density and local structure.
- **Instance-Based Learning:** The "model" effectively comprises the entire training dataset, retained in memory for localized computations.
- **Query-Dependent Model:** A distinct parameter vector `θ̂` is computed for each query point, then discarded post-prediction.

## Numerical Example

Consider univariate data with training points `(x, y)`: {(1, 2), (2, 3), (3, 4), (4, 7), (5, 6)}. Predict for `x_q = 3.5` with `τ = 1.5`.

**Step 1: Compute weights**

| x^(i) | y^(i) | d^(i) = (x^(i) - 3.5)² | w^(i) = exp(-d^(i)/(2·1.5²)) |
| ----- | ----- | ---------------------- | ---------------------------- |
| 1     | 2     | 6.25                   | exp(-6.25/4.5) = 0.169       |
| 2     | 3     | 2.25                   | exp(-2.25/4.5) = 0.606       |
| 3     | 4     | 0.25                   | exp(-0.25/4.5) = 0.946       |
| 4     | 7     | 0.25                   | exp(-0.25/4.5) = 0.946       |
| 5     | 6     | 2.25                   | exp(-2.25/4.5) = 0.606       |

**Step 2: Fit weighted linear regression** (simplified illustration)

The weighted least squares solution yields `θ̂` emphasizing points near `x_q = 3.5` (x=3 and x=4), producing prediction `ŷ_q ≈ 5.2`.

## Computational Complexity Analysis

- **Time Complexity:** O(m · n² + n³) per query, where `m` = training samples, `n` = features
- **Space Complexity:** O(mn) for storing training data
- **Key Limitation:** Must solve a new regression problem for every query point, rendering LWR computationally prohibitive for large datasets or real-time applications

## Comparison with Related Methods

| Aspect             | LWR                          | k-NN Regression       | Kernel Regression |
| ------------------ | ---------------------------- | --------------------- | ----------------- |
| Weighting          | Gaussian kernel (all points) | Uniform (k neighbors) | Gaussian kernel   |
| Model              | Local linear/polynomial      | Local average         | Weighted average  |
| Parameters         | τ (bandwidth)                | k (neighbors)         | τ (bandwidth)     |
| Computational Cost | High (per query)             | Moderate              | High (per query)  |

## Advantages and Limitations

**Advantages:**

- Exceptional flexibility in modeling highly complex, non-linear relationships
- Makes no restrictive assumptions about underlying functional form
- Intuitive conceptual foundation with natural interpretability of local fitting

**Limitations:**

- **Computational Expense:** Must solve new regression problem for each query point; unsuitable for large datasets
- **Bandwidth Sensitivity:** Performance critically depends on τ selection
- **Data Density Requirement:** Necessitates sufficiently dense training data in query neighborhoods
- **Interpretability Deficiency:** No single deployable model exists for analysis

## Key Takeaways

1. LWR is a **non-parametric** method that eschews fixed parametric assumptions
2. It employs a **Gaussian kernel** to assign proximity-based weights
3. The **bandwidth parameter τ** controls the bias-variance tradeoff
4. The **weighted normal equations** `(XᵀW X)θ = XᵀW y` provide the closed-form solution
5. **Computational cost** constitutes the primary practical limitation
6. The algorithm is inherently **query-dependent**, constructing unique models per prediction
