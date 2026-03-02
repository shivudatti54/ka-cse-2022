# Module 3: Regression Analysis in Machine Learning

## 1. Introduction

Regression Analysis is a foundational supervised learning technique used to predict a continuous numerical outcome (dependent variable) based on the value of one or more input features (independent variables). Unlike classification, which predicts discrete labels, regression predicts a quantity. It is ubiquitous in engineering applications, from predicting house prices and stock trends to estimating the strength of a material or the energy consumption of a system.

## 2. Core Concepts

### A. Simple Linear Regression

This is the simplest form of regression, modeling the relationship between two variables by fitting a linear equation to the observed data.
*   **Equation:** `y = β₀ + β₁x + ε`
    *   `y`: Dependent variable (target we want to predict).
    *   `x`: Independent variable (feature we use for prediction).
    *   `β₀`: y-intercept (value of `y` when `x` is 0).
    *   `β₁`: Slope (change in `y` for a one-unit change in `x`).
    *   `ε`: Random error term (accounts for noise).

The goal is to find the "best-fit" line that minimizes the difference between the predicted values and the actual data points.

### B. Cost Function: Mean Squared Error (MSE)

How do we find this "best-fit" line? We use a **cost function** to measure the error of our model. The most common cost function for regression is the **Mean Squared Error (MSE)**.

`MSE = (1/n) * Σ(yᵢ - ŷᵢ)²`

*   `n`: Number of data points.
*   `yᵢ`: Actual value for the i-th data point.
*   `ŷᵢ`: Predicted value for the i-th data point.

MSE calculates the average of the squares of the errors. We square the errors to emphasize larger errors and to make the function differentiable.

### C. Optimization: Gradient Descent

To find the parameters (`β₀` and `β₁`) that minimize the MSE cost function, we use an optimization algorithm called **Gradient Descent**.

1.  **Initialize** the parameters (`β₀`, `β₁`) with random values.
2.  **Calculate** the gradient (partial derivatives) of the cost function with respect to each parameter. The gradient points in the direction of the steepest ascent.
3.  **Update** the parameters by taking a small step (defined by the **learning rate**, `α`) in the *opposite* direction of the gradient (steepest descent).
    *   `β_j := β_j - α * (∂/∂β_j) MSE`
4.  **Repeat** steps 2 and 3 until the cost function converges to a minimum.

**Learning Rate (`α`)** is a crucial hyperparameter:
*   Too small: The algorithm takes too long to converge.
*   Too large: The algorithm might overshoot the minimum and fail to converge.

### D. Multiple Linear Regression

In real-world engineering problems, an outcome is rarely influenced by just one factor. **Multiple Linear Regression** extends the concept to multiple independent variables.

*   **Equation:** `y = β₀ + β₁x₁ + β₂x₂ + ... + βₙxₙ + ε`
*   Here, we are fitting a hyperplane in an n-dimensional space instead of a line in 2D. The core concepts of MSE and Gradient Descent remain the same, but the calculations involve vectors and matrices for efficiency.

### E. Model Evaluation Metrics

How do we know if our regression model is good?
*   **Mean Absolute Error (MAE):** `(1/n) * Σ|yᵢ - ŷᵢ|` - The average absolute difference between actual and predicted values. Easier to interpret.
*   **Root Mean Squared Error (RMSE):** `√(MSE)` - The square root of MSE. It is in the same units as the target variable, making it more interpretable than MSE. It penalizes larger errors more heavily.
*   **R-squared (R²) Score:** Represents the proportion of the variance in the dependent variable that is predictable from the independent variables. It ranges from 0 to 1 (or 0% to 100%), where a higher value indicates a better fit.

**Example:** Predicting the price of a laptop (`y`) based on its RAM (`x₁`) and SSD size (`x₂`).
`Price = 20000 + 5000 * (RAM_in_GB) + 100 * (SSD_in_GB)`

## 3. Key Points & Summary

*   **Purpose:** Predict a continuous numerical value.
*   **Core Idea:** Find a mathematical relationship (linear or non-linear) between input features and a continuous target variable.
*   **Simple vs. Multiple:** Simple uses one feature; multiple uses many.
*   **Cost Function:** Mean Squared Error (MSE) is most common, quantifying the prediction error.
*   **Optimization:** Gradient Descent is the workhorse algorithm for finding the parameters that minimize the cost function.
*   **Evaluation:** Use metrics like RMSE, MAE, and R² to evaluate model performance on unseen data.
*   **Assumptions:** Linear regression assumes a linear relationship, among other things (e.g., independence of errors, homoscedasticity). Real-world data often requires more advanced techniques like **Polynomial Regression** (which fits a curved line) or **Regularization** (Lasso/Ridge regression) to prevent overfitting.