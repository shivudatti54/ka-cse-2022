# Revision Notes: Discriminant Analysis - Covariance Matrix, Fisher's Linear Discriminant

===========================================================

**Key Points**

- **Covariance Matrix**
  - Definition: Matrix representing the covariance between random variables
  - Formula: Σ = [cov(x, y), cov(x, z), ..., cov(x, m)]^T
- **Fisher's Linear Discriminant**
  - Definition: Linear combination of features that maximizes between-class variance and minimizes within-class variance
  - Formula: w = argmax (w^T Σ w) subject to w^T π = 0
- **Generalized Linear Models (GLMs)**
  - Definition: GLMs are a type of regression model that includes linear regression as a special case
  - Formula: g(μ) = Xβ + ε (where g is the link function)
- **Interpreting Results**
  - Definition: Clustering: groups similar samples together
  - Definition: Discrimination: separates classes based on the predicted values

**Important Formulas and Theorems**

- **Covariance Matrix Inversion**: Σ^-1 = (1 / (n - k)) \* (I - (1 / n) \* 1^T)
- **Fisher's Linear Discriminant Theorem**: w = (Σ \* π)^-1 \* Σ \* x

**Key Concepts**

- **Random Samples**: multiple sets of data used to estimate population parameters
- **Training and Testing Sets**: used to evaluate model performance
