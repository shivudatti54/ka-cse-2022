# Linear Regression with One Variable
## Machine Learning - BSc (H) Computer Science | Delhi University (NEP 2024 UGCF)

### Introduction
Linear Regression with One Variable (also called Univariate Linear Regression) is the foundational supervised learning algorithm used for predicting continuous numerical outcomes. It establishes a linear relationship between a single input feature (independent variable) and the target output (dependent variable). This technique forms the basis for understanding more complex machine learning models and is essential for the Delhi University ML syllabus.

### Key Concepts

**1. Definition & Application**
- Supervised learning algorithm for regression tasks
- Predicts continuous value outputs
- Example: Predicting house prices based on area, or sales based on advertising budget

**2. Hypothesis Function**
- Represented as: **h(x) = θ₀ + θ₁x**
- θ₀ (theta zero) = y-intercept (bias term)
- θ₁ (theta one) = slope (weight for feature x)
- x = input feature variable

**3. Cost Function (Mean Squared Error)**
- Formula: **J(θ₀,θ₁) = (1/2m) Σ[h(x⁽ⁱ⁾) - y⁽ⁱ⁾]²**
- Measures difference between predicted and actual values
- Objective: Minimize the cost function
- m = number of training examples

**4. Gradient Descent Algorithm**
- Iterative optimization technique to minimize cost function
- Update rules:
  - θ₀ := θ₀ - α × (1/m) × Σ[h(x⁽ⁱ⁾) - y⁽ⁱ⁾]
  - θ₁ := θ₁ - α × (1/m) × Σ[h(x⁽ⁱ⁾) - y⁽ⁱ⁾] × x⁽ⁱ⁾
- α (alpha) = learning rate (step size)
- Converges to global minimum for linear regression

**5. Normal Equation (Analytical Solution)**
- Direct closed-form solution: **θ = (XᵀX)⁻¹Xᵀy**
- No need for iterative gradient descent
- Suitable for smaller datasets
- Computational complexity: O(n³)

**6. Feature Scaling**
- Normalize features using mean normalization or standardization
- Accelerates gradient descent convergence
- Formula: xᵢ = (xᵢ - μᵢ) / σᵢ

**7. Model Evaluation**
- **R² (Coefficient of Determination)** – explains variance in data
- **Root Mean Squared Error (RMSE)** – average prediction error
- **Mean Absolute Error (MAE)** – average absolute differences

### Conclusion
Linear Regression with One Variable is the entry point to machine learning, demonstrating core concepts like hypothesis representation, cost function minimization, and parameter optimization. Mastery of gradient descent and the normal equation is crucial for exams. Understanding these fundamentals prepares students for multivariate regression and advanced ML algorithms in the Delhi University curriculum.

---
*Revision Tip: Remember the hypothesis function, cost function formula, and gradient descent update rules — these are frequently tested in University exams.*