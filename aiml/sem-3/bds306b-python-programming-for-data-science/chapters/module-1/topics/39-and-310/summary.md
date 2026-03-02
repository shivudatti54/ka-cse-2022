# **Revision Notes: 3.9 and 3.10**

## **Topic Overview**

This section covers the basics of numerical integration and linear least squares regression.

### Numerical Integration

- **Definition:** Numerical integration is a method of approximating the value of a definite integral.
- **Methods:**
  - Trapezoidal Rule: approximates the area under a curve by dividing it into trapezoids.
  - Simpson's Rule: approximates the area under a curve by dividing it into parabolic segments.
- **Formulas:**
  - Trapezoidal Rule: $\int_{a}^{b} f(x) dx \approx \frac{h}{2} (f(a) + 2f(a+h) + 2f(a+2h) + ... + 2f(b-h) + f(b))$
  - Simpson's Rule: $\int_{a}^{b} f(x) dx \approx \frac{h}{3} (f(a) + 4f(a+h) + 2f(a+2h) + ... + 4f(b-h) + f(b))$

### Linear Least Squares Regression

- **Definition:** Linear least squares regression is a method of finding the best-fitting linear line to a set of data points.
- **Method:**
  - Ordinary Least Squares (OLS): minimizes the sum of the squared residuals between the observed and predicted values.
- **Formulas:**
  - OLS: $\hat{y} = \beta_0 + \beta_1 x + \epsilon$
  - Coefficients: $\beta_0 = \bar{y} - \beta_1 \bar{x}$
  - $R^2 = 1 - \frac{\sum_{i=1}^{n} (y_i - \hat{y_i})^2}{\sum_{i=1}^{n} (y_i - \bar{y})^2}$

### Important Theorems

- **Fundamental Theorem of Calculus:** $\int_{a}^{b} f(x) dx = F(b) - F(a)$
- **Linear Independence:** A set of vectors is linearly independent if the only way to express the zero vector as a linear combination of the vectors is with all coefficients equal to zero.
