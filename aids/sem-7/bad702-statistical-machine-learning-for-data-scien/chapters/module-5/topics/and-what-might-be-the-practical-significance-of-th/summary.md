# Revision Notes: Estimating Mean Salary of Software Engineers

===========================================================

### Overview

---

The task is to estimate the mean salary of software engineers in a country using statistical machine learning. We'll focus on practical significance of findings.

### Key Concepts

---

- **Discriminant Analysis**: A supervised learning technique used for classification problems.
- **Covariance Matrix**: A square matrix that summarizes the variability of a multivariate distribution.
- **Fisher's Linear Discriminant**: A linear combination of features that maximizes the separation between classes.
- **Generalized Linear Models (GLMs)**: A framework for modeling the relationship between a dependent variable and one or more independent variables.

### Notation and Definitions

---

- **μ**: Mean of a distribution
- **σ^2**: Variance of a distribution
- **Cov(A, B)**: Covariance between features A and B
- **D**: Discriminant function
- **GLM**: Generalized Linear Model

### Theorems and Formulas

---

- **Cramer's Rule**: For GLMs, the coefficients are calculated using the inverse of the Hessian matrix.
- **Wishart Distribution**: A distribution used to model the covariance matrix of a multivariate distribution.

### Practical Significance

---

- **Estimating Mean Salary**: Use GLMs to model the relationship between salary and relevant features (e.g., experience, location).
- **Covariance Matrix Estimation**: Use the sample covariance matrix as an estimate of the population covariance matrix.
- **Fisher's Linear Discriminant**: Use FLD to identify the most informative features for class separation.

### Formula for Estimating Mean Salary

---

- **GLM**: y = β0 + β1x1 + β2x2 + … + βnxn + ε, where y is the response variable, x is the design matrix, β is the coefficient matrix, and ε is the error term.

Note: This summary is a condensed version of key concepts, notation, and formulas. It's intended to be a quick revision guide before exams.
