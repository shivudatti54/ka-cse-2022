# Introduction to Linear Regression

## Introduction

Linear Regression is one of the most fundamental and widely used predictive modeling techniques in machine learning and statistical analysis. It serves as the foundation for understanding supervised learning, where the goal is to predict a continuous output variable based on one or more input features. In the context of the University of Delhi Computer Science curriculum, linear regression represents the gateway to more complex machine learning algorithms and forms an essential part of data science education.

The technique traces its origins to the work of Francis Galton in the late 19th century, who used it to study the relationship between heights of parents and their offspring. Today, linear regression is applied across diverse domains: predicting house prices based on square footage, estimating sales figures from advertising expenditure, forecasting stock prices using historical data, and analyzing the impact of various factors on economic indicators. Its simplicity, interpretability, and computational efficiency make it an indispensable tool for both exploratory data analysis and predictive modeling.

Understanding linear regression is crucial for students because it introduces core machine learning concepts that recur throughout the field: the distinction between training and testing data, the bias-variance tradeoff, model evaluation metrics, and the prevention of overfitting. These concepts form the conceptual foundation upon which more advanced algorithms are built.

## Key Concepts

### Simple Linear Regression

Simple linear regression is the most basic form of regression analysis, involving only one independent variable (feature) and one dependent variable (target). The relationship between the variables is assumed to be linear, represented by the equation of a straight line.

The mathematical form of simple linear regression is:

**y = mx + c**

Where:
- y is the dependent variable (what we want to predict)
- x is the independent variable (the feature used for prediction)
- m is the slope (coefficient indicating the change in y for unit change in x)
- c is the y-intercept (the value of y when x = 0)

In machine learning notation, this is typically written as:

**y = wx + b**

Where w represents the weight (similar to slope) and b represents the bias (similar to intercept).

### Multiple Linear Regression

When we have more than one independent variable, simple linear regression extends to multiple linear regression. This allows us to capture the combined effect of multiple features on the target variable. The equation becomes:

**y = w₁x₁ + w₂x₂ + w₃x₃ + ... + wₙxₙ + b**

In vector form: **y = Xw + b**

Where X is a matrix of features, w is a vector of weights, and b is the bias term. Multiple linear regression is more realistic for real-world problems where outcomes are influenced by multiple factors simultaneously.

### The Cost Function

To find the best values for w and b, we need a way to measure how well our model fits the data. The most common cost function for linear regression is the Mean Squared Error (MSE), defined as:

**MSE = (1/n) Σ(yᵢ - ŷᵢ)²**

Where:
- n is the number of training examples
- yᵢ is the actual value
- ŷᵢ is the predicted value

The MSE penalizes larger errors more heavily because the squared difference grows exponentially with error magnitude. Our goal is to find the parameters that MINIMIZE this cost function.

### The Least Squares Method

The analytical (closed-form) solution for finding optimal parameters uses the ordinary least squares (OLS) approach. For simple linear regression, the formulas are:

**m = Σ(xᵢ - x̄)(yᵢ - ȳ) / Σ(xᵢ - x̄)²**

**c = ȳ - mx̄**

Where x̄ and ȳ are the means of x and y respectively.

For multiple linear regression, the closed-form solution is:

**w = (XᵀX)⁻¹Xᵀy**

This matrix solution works well when the number of features is not too large and the matrix XᵀX is invertible.

### Gradient Descent Optimization

When the analytical solution is computationally expensive or impossible (for example, when the matrix is singular), we use iterative optimization algorithms like gradient descent. The algorithm works as follows:

1. Initialize parameters w and b to small random values
2. Calculate the gradient (partial derivatives) of the cost function with respect to each parameter
3. Update parameters in the direction opposite to the gradient
4. Repeat until convergence

The update rules are:

**w := w - α × (∂MSE/∂w)**

**b := b - α × (∂MSE/∂b)**

Where α is the learning rate, a hyperparameter that controls how big each step is.

### Assumptions of Linear Regression

For linear regression to produce valid results, certain assumptions must hold:

1. **Linearity**: The relationship between independent and dependent variables is linear
2. **Independence**: Observations are independent of each other
3. **Homoscedasticity**: The variance of residuals is constant across all levels of the independent variable
4. **Normality**: The residuals (errors) are normally distributed
5. **No Multicollinearity**: Independent variables are not highly correlated with each other (for multiple regression)

### Evaluation Metrics

Several metrics help assess model performance:

- **R-squared (R²)**: Represents the proportion of variance in the dependent variable explained by the independent variables. Ranges from 0 to 1, with higher values indicating better fit.

- **Adjusted R-squared**: Modified R² that accounts for the number of predictors in the model, preventing overestimation with additional features.

- **Root Mean Squared Error (RMSE)**: The square root of MSE, in the same units as the target variable.

- **Mean Absolute Error (MAE)**: The average absolute difference between predictions and actual values, less sensitive to outliers than MSE.

## Examples

### Example 1: Simple Linear Regression Calculation

A real estate agent wants to predict house prices based on the area (in square feet). Given the following training data:

| Area (sq ft) | Price (lakhs) |
|-------------|---------------|
| 1000        | 25            |
| 1500        | 35            |
| 2000        | 48            |
| 2500        | 55            |
| 3000        | 72            |

Calculate the linear regression parameters and predict the price for a 2800 sq ft house.

**Step 1: Calculate means**
x̄ = (1000 + 1500 + 2000 + 2500 + 3000) / 5 = 10000 / 5 = 2000
ȳ = (25 + 35 + 48 + 55 + 72) / 5 = 235 / 5 = 47

**Step 2: Calculate slope (m)**
m = Σ(xᵢ - x̄)(yᵢ - ȳ) / Σ(xᵢ - x̄)²

Numerator: (1000-2000)(-22) + (1500-2000)(-12) + (2000-2000)(1) + (2500-2000)(8) + (3000-2000)(25)
= (-1000)(-22) + (-500)(-12) + (0)(1) + (500)(8) + (1000)(25)
= 22000 + 6000 + 0 + 4000 + 25000 = 57000

Denominator: (-1000)² + (-500)² + (0)² + (500)² + (1000)²
= 1000000 + 250000 + 0 + 250000 + 1000000 = 2500000

m = 57000 / 2500000 = 0.0228

**Step 3: Calculate intercept (c)**
c = ȳ - m × x̄ = 47 - 0.0228 × 2000 = 47 - 45.6 = 1.4

**Step 4: Regression equation**
Price = 0.0228 × Area + 1.4

**Step 5: Prediction for 2800 sq ft**
Price = 0.0228 × 2800 + 1.4 = 63.84 + 1.4 = 65.24 lakhs

### Example 2: Multiple Linear Regression

A marketing analyst wants to predict monthly sales based on advertising spend on TV and social media. Given:

| TV Ad Spend (lakhs) | Social Media (lakhs) | Sales (lakhs) |
|--------------------|---------------------|---------------|
| 2                  | 1                   | 15            |
| 3                  | 2                   | 22            |
| 1                  | 0.5                 | 10            |
| 4                  | 3                   | 28            |
| 2.5                | 1.5                 | 20            |

Using gradient descent or normal equations, we would find:
Sales = 5.2 + 3.1 × (TV) + 2.8 × (Social Media)

For a new campaign with TV spend of 3.5 lakhs and social media spend of 2 lakhs:
Predicted Sales = 5.2 + 3.1(3.5) + 2.8(2) = 5.2 + 10.85 + 5.6 = 21.65 lakhs

### Example 3: Gradient Descent Walkthrough

Given data points: x = [1, 2, 3, 4, 5], y = [2, 4, 5, 4, 5]

Using gradient descent with learning rate α = 0.01, initial parameters w = 0, b = 0:

**Iteration 1:**
Predictions: [0, 0, 0, 0, 0]
Errors: [2, 4, 5, 4, 5]
Gradients: dw = -2/5 × Σx(e) = -2/5 × (1×2 + 2×4 + 3×5 + 4×4 + 5×5) = -2/5 × 70 = -28
db = -2/5 × Σe = -2/5 × 20 = -8

Update: w = 0 - 0.01(-28) = 0.28, b = 0 - 0.01(-8) = 0.08

After many iterations, parameters converge to approximately w = 0.7, b = 1.5, giving the line y = 0.7x + 1.5.

## Exam Tips

1. REMEMBER THE CORE EQUATION: The fundamental linear regression equation is y = wx + b (or y = mx + c in traditional notation). Always identify which variable is the predictor and which is the response.

2. UNDERSTAND THE COST FUNCTION: Know that MSE measures the average squared difference between predictions and actual values. The goal is ALWAYS to minimize this, not maximize it.

3. DISTINGUISH BETWEEN SIMPLE AND MULTIPLE: Simple linear regression has one feature; multiple has many. The concepts are the same, but multiple requires matrix notation for the closed-form solution.

4. GRADIENT DESCENT LEARNING RATE (α) controls: The learning rate step size. If too small, convergence is slow; if too large, the algorithm may not converge and may oscillate or diverge.

5. INTERPRET R-SQUARED: R² values closer to 1 indicate better models. However, in multiple regression, use adjusted R² when comparing models with different numbers of predictors.

6. ASSUMPTIONS MATTER: In exams, when asked about the validity of linear regression, ALWAYS check whether the assumptions (linearity, independence, homoscedasticity, normality) are satisfied.

7. SOLVE BOTH ANALYTICAL AND NUMERICAL: Be prepared to calculate regression coefficients using the least squares formulas AND explain how gradient descent works iteratively.

8. REAL-WORLD INTERPRETATION: When interpreting coefficients, remember that in multiple regression, the coefficient of one variable shows its effect HOLDING OTHER VARIABLES CONSTANT.

9. OVERFITTING AWARENESS: Adding more features always increases (or maintains) R² on training data but may decrease test performance. This is why adjusted R² penalizes unnecessary complexity.

10. WRITE NEAT SOLUTIONS: For numerical problems, show all calculation steps clearly, including mean calculations, summations, and final parameter values. examiners appreciate well-organized work.