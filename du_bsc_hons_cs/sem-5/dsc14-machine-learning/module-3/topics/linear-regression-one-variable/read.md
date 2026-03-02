# Linear Regression with One Variable

## A Comprehensive Study Material for BSc (Hons) Computer Science — Delhi University (NEP 2024 UGCF)

---

## 1. Introduction and Real-World Relevance

**Linear Regression with One Variable** (also known as *Simple Linear Regression*) is one of the most fundamental and widely used predictive modeling techniques in Machine Learning. It forms the foundation for understanding more complex algorithms and serves as a powerful tool for solving real-world problems where we need to predict a continuous outcome based on a single predictor variable.

### What is Linear Regression?

Linear Regression is a supervised learning algorithm that establishes a **linear relationship** between a dependent variable (also called the target or output variable, denoted as *y*) and an independent variable (also called the feature or input variable, denoted as *x*). The goal is to find the best-fitting straight line that minimizes the difference between the predicted values and the actual values.

### Real-World Applications

Linear Regression with one variable has numerous practical applications across various domains:

| Domain | Application | Example |
|--------|-------------|---------|
| **Economics** | Predicting GDP growth | Using unemployment rate to predict GDP |
| **Real Estate** | House price prediction | Using square footage to predict house prices |
| **Healthcare** | Patient outcome prediction | Using patient age to predict recovery time |
| **Finance** | Stock price forecasting | Using trading volume to predict stock prices |
| **Marketing** | Sales forecasting | Using advertising spend to predict sales |
| **Education** | Performance prediction | Using study hours to predict exam scores |

### Delhi University Syllabus Context

This topic aligns with the **Machine Learning** paper under the NEP 2024 UGCF curriculum for BSc (Hons) Computer Science. Students are expected to understand the mathematical foundations, implementation using Python, and evaluation metrics for Simple Linear Regression.

---

## 2. Mathematical Foundation

### The Hypothesis Function

In Linear Regression with one variable, we represent the relationship between the input variable *x* and output variable *y* using the equation of a straight line:

$$h_\theta(x) = \theta_0 + \theta_1 x$$

Where:
- $h_\theta(x)$ is the **hypothesis function** (predicted value)
- $\theta_0$ is the **y-intercept** (also called bias term)
- $\theta_1$ is the **slope** (coefficient for feature x)
- $x$ is the input feature

Our goal is to find the values of $\theta_0$ and $\theta_1$ that make the predicted values as close as possible to the actual values in the training data.

### Cost Function (Mean Squared Error)

To measure how well our hypothesis fits the training data, we use a **Cost Function**. For Linear Regression, the most commonly used cost function is the **Mean Squared Error (MSE)**:

$$J(\theta_0, \theta_1) = \frac{1}{2m} \sum_{i=1}^{m} (h_\theta(x^{(i)}) - y^{(i)})^2$$

Where:
- $m$ is the number of training examples
- $h_\theta(x^{(i)})$ is the predicted value for the $i^{th}$ training example
- $y^{(i)}$ is the actual value for the $i^{th}$ training example

The factor of $\frac{1}{2}$ is included purely for mathematical convenience (it cancels out when taking the derivative during gradient descent).

**Why MSE?**
- It penalizes larger errors more heavily (due to squaring)
- It is always non-negative
- It is differentiable, allowing us to use gradient descent

---

## 3. Gradient Descent Algorithm

**Gradient Descent** is an optimization algorithm used to find the values of parameters ($\theta_0$, $\theta_1$) that minimize the cost function $J(\theta_0, \theta_1)$.

### Intuition

Imagine you are standing on a foggy mountain (the cost function landscape). You want to reach the lowest point (the minimum). You can feel the slope of the ground under your feet and take small steps in the direction of the steepest descent. This is exactly what gradient descent does!

### The Algorithm

Repeat until convergence:
$$\theta_j := \theta_j - \alpha \frac{\partial}{\partial \theta_j} J(\theta_0, \theta_1)$$

For our simple linear regression with two parameters, this becomes:

**For j = 0:**
$$\theta_0 := \theta_0 - \alpha \frac{1}{m} \sum_{i=1}^{m} (h_\theta(x^{(i)}) - y^{(i)})$$

**For j = 1:**
$$\theta_1 := \theta_1 - \alpha \frac{1}{m} \sum_{i=1}^{m} (h_\theta(x^{(i)}) - y^{(i)}) \cdot x^{(i)}$$

Where:
- $\alpha$ is the **learning rate** (step size)
- The update should happen **simultaneously** for both $\theta_0$ and $\theta_1$

### Key Points About Learning Rate

- **Too small α**: Gradient descent will be slow; it may take many iterations to converge
- **Too large α**: Gradient descent may overshoot the minimum, fail to converge, or even diverge
- **Convergence**: When the change in the cost function is very small between iterations, we say gradient descent has converged

### Gradient Descent for Simple Linear Regression

The partial derivatives for our specific cost function are:

$$\frac{\partial}{\partial \theta_0} J(\theta_0, \theta_1) = \frac{1}{m} \sum_{i=1}^{m} (h_\theta(x^{(i)}) - y^{(i)})$$

$$\frac{\partial}{\partial \theta_1} J(\theta_0, \theta_1) = \frac{1}{m} \sum_{i=1}^{m} (h_\theta(x^{(i)}) - y^{(i)}) \cdot x^{(i)}$$

### Convergence Plot

A well-functioning gradient descent should show:
1. Cost function $J(\theta)$ decreasing with each iteration
2. Eventually leveling off as it approaches the minimum

---

## 4. Normal Equation (Analytical Solution)

While Gradient Descent is an iterative approach, there exists a **closed-form solution** (analytical approach) to find the optimal parameters directly. This is known as the **Normal Equation**.

### The Formula

For linear regression, the normal equation is:

$$\theta = (X^T X)^{-1} X^T y$$

Where:
- $X$ is the design matrix (includes a column of ones for the bias term)
- $y$ is the vector of target values
- $\theta$ is the vector of parameters $[\theta_0, \theta_1]^T$

### Comparison: Gradient Descent vs Normal Equation

| Aspect | Gradient Descent | Normal Equation |
|--------|------------------|-----------------|
| **Approach** | Iterative | Analytical (closed-form) |
| **Learning Rate** | Requires choosing α | No learning rate needed |
| **Iterations** | Requires many iterations | No iteration needed |
| **Computational Complexity** | O(kn²) | O(n³) where n is features |
| **Scalability** | Works well for large datasets | Slow for large datasets |
| **Feature Scaling** | Required | Not required |

### When to Use Which?

- **Use Gradient Descent when**:
  - You have a very large dataset
  - You need to monitor convergence
  - Feature scaling is manageable

- **Use Normal Equation when**:
  - Dataset is small (n < 10,000)
  - You need an exact solution
  - You want to avoid hyperparameter tuning

---

## 5. Model Evaluation Metrics

Understanding how well your model performs is crucial. Here are the key evaluation metrics:

### 5.1 Coefficient of Determination (R² Score)

The **R² score** (also called the coefficient of determination) measures the proportion of variance in the dependent variable that is predictable from the independent variable.

$$R^2 = 1 - \frac{SS_{res}}{SS_{tot}}$$

Where:
- $SS_{res}$ (Residual Sum of Squares) = $\sum (y_i - \hat{y}_i)^2$
- $SS_{tot}$ (Total Sum of Squares) = $\sum (y_i - \bar{y})^2$
- $\bar{y}$ is the mean of actual values

**Interpretation of R²:**
- **R² = 1**: Perfect prediction (model explains 100% of variance)
- **R² = 0**: Model is as good as predicting the mean
- **R² < 0**: Model is worse than predicting the mean (possible with no intercept)

**Adjusted R²**: For simple linear regression, R² is sufficient, but when using multiple regression, adjusted R² is preferred as it penalizes adding unnecessary features.

### 5.2 Mean Squared Error (MSE)

$$MSE = \frac{1}{m} \sum_{i=1}^{m} (y_i - \hat{y}_i)^2$$

- Penalizes larger errors heavily
- Units are squared (not intuitive for interpretation)

### 5.3 Root Mean Squared Error (RMSE)

$$RMSE = \sqrt{MSE}$$

- Same units as the target variable
- More interpretable than MSE

### 5.4 Mean Absolute Error (MAE)

$$MAE = \frac{1}{m} \sum_{i=1}^{m} |y_i - \hat{y}_i|$$

- More robust to outliers
- Linear penalty for errors

---

## 6. Assumptions of Linear Regression

For linear regression to provide reliable and valid predictions, certain assumptions must be met:

### 6.1 Linearity

The relationship between the independent variable (x) and dependent variable (y) should be linear. This is checked by creating a scatter plot and observing if the data points roughly follow a straight line pattern.

### 6.2 Independence (No Autocorrelation)

The residuals (errors) should be independent of each other. This is particularly important in time-series data where consecutive observations might be correlated. The **Durbin-Watson test** can detect autocorrelation.

### 6.3 Homoscedasticity (Constant Variance)

The variance of residuals should be constant across all levels of the independent variable. If the variance increases or decreases with x, we have **heteroscedasticity**, which violates this assumption.

### 6.4 Normality of Residuals

The residuals (errors) should be normally distributed. This can be checked using:
- Q-Q plots (Quantile-Quantile plots)
- Shapiro-Wilk test
- Histogram of residuals

### 6.5 No Multicollinearity (for multiple regression)

Although this applies primarily to multiple regression, it's worth noting that predictor variables should not be highly correlated with each other.

### 6.6 No Endogeneity

There should be no correlation between the independent variables and the error term. This means all relevant factors affecting y should be included in the model.

---

## 7. Practical Examples with Code

### Example 1: Predicting House Prices Based on Square Footage

This example demonstrates simple linear regression using Python with scikit-learn.

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

# Dataset: Square footage and corresponding house prices
# X = Square Footage (in sq ft)
# y = Price (in lakhs INR)

X = np.array([500, 750, 1000, 1250, 1500, 1750, 2000, 2250, 2500, 2750, 3000]).reshape(-1, 1)
y = np.array([15, 22, 30, 38, 45, 52, 60, 68, 75, 82, 90])  # In lakhs

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Display results
print("=" * 50)
print("LINEAR REGRESSION MODEL RESULTS")
print("=" * 50)
print(f"Intercept (θ₀): {model.intercept_:.4f}")
print(f"Coefficient (θ₁): {model.coef_[0]:.4f}")
print(f"\nEquation: Price = {model.intercept_:.4f} + {model.coef_[0]:.4f} × Area")
print(f"\nR² Score: {r2_score(y_test, y_pred):.4f}")
print(f"MSE: {mean_squared_error(y_test, y_pred):.4f}")
print(f"RMSE: {np.sqrt(mean_squared_error(y_test, y_pred)):.4f}")
print(f"MAE: {mean_absolute_error(y_test, y_pred):.4f}")

# Visualization
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, model.predict(X), color='red', label='Regression Line')
plt.xlabel('Square Footage (sq ft)')
plt.ylabel('Price (Lakhs INR)')
plt.title('House Price Prediction using Linear Regression')
plt.legend()
plt.grid(True)
plt.show()
```

**Expected Output:**
```
Intercept (θ₀): 0.8182
Coefficient (θ₁): 0.0297

Equation: Price = 0.8182 + 0.0297 × Area

R² Score: 0.9998
```

### Example 2: Predicting Exam Scores Based on Study Hours

This example implements gradient descent from scratch.

```python
import numpy as np

def compute_cost(X, y, theta):
    """Compute the cost function (MSE)"""
    m = len(y)
    predictions = X.dot(theta)
    cost = (1 / (2 * m)) * np.sum((predictions - y) ** 2)
    return cost

def gradient_descent(X, y, theta, alpha, num_iterations):
    """Perform gradient descent to optimize theta"""
    m = len(y)
    cost_history = []
    
    for i in range(num_iterations):
        predictions = X.dot(theta)
        errors = predictions - y
        theta = theta - (alpha / m) * X.T.dot(errors)
        cost = compute_cost(X, y, theta)
        cost_history.append(cost)
        
    return theta, cost_history

# Dataset: Study hours and exam scores
# Adding column of ones for bias term
X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # Study hours
y = np.array([35, 42, 50, 58, 65, 72, 78, 85, 92, 98])  # Exam scores

# Add bias term (column of ones)
m = len(X)
X_with_bias = np.vstack([np.ones(m), X]).T

# Initialize parameters
theta = np.zeros(2)
alpha = 0.01  # Learning rate
num_iterations = 1000

# Run gradient descent
theta, cost_history = gradient_descent(X_with_bias, y, theta, alpha, num_iterations)

print("=" * 50)
print("GRADIENT DESCENT RESULTS")
print("=" * 50)
print(f"Intercept (θ₀): {theta[0]:.4f}")
print(f"Coefficient (θ₁): {theta[1]:.4f}")
print(f"\nEquation: Score = {theta[0]:.4f} + {theta[1]:.4f} × Study Hours")
print(f"\nFinal Cost (MSE/2): {cost_history[-1]:.4f}")

# Make a prediction for 5.5 hours of study
test_x = np.array([1, 5.5])
predicted_score = test_x.dot(theta)
print(f"\nPredicted score for 5.5 hours of study: {predicted_score:.2f}")
```

---

## 8. Model Evaluation Details

### Training vs Testing Performance

It is essential to evaluate your model on both training and testing data to detect **overfitting** or **underfitting**:

- **Training Error**: Error on the data used to train the model
- **Testing Error**: Error on unseen data

**Good Model**: Both training and testing errors are low and similar

### Underfitting (High Bias)

- Both training and testing errors are high
- Model is too simple to capture the pattern
- Solution: Add more features, use polynomial regression, decrease regularization

### Overfitting (High Variance)

- Training error is very low but testing error is high
- Model memorizes training data instead of learning general patterns
- Solution: Get more training data, reduce features, use regularization

### Cross-Validation

For more robust evaluation, use **k-fold cross-validation**:
1. Split data into k folds
2. Train on k-1 folds, test on 1 fold
3. Repeat for each fold
4. Average the performance metrics

This provides a more reliable estimate of model performance.

---

## 9. Key Takeaways

1. **Linear Regression with One Variable** establishes a linear relationship between a single feature (x) and a continuous target (y) using the equation: $h_\theta(x) = \theta_0 + \theta_1x$

2. **Cost Function (MSE)** measures prediction error: $J(\theta_0, \theta_1) = \frac{1}{2m} \sum_{i=1}^{m} (h_\theta(x^{(i)}) - y^{(i)})^2$

3. **Gradient Descent** iteratively optimizes parameters by taking steps proportional to the negative gradient of the cost function

4. **Normal Equation** provides a closed-form solution: $\theta = (X^T X)^{-1} X^T y$

5. **R² Score** indicates how well the model explains the variance in the target variable (ranges from 0 to 1)

6. **Key Assumptions** of Linear Regression include linearity, independence, homoscedasticity, and normality of residuals

7. **Model Evaluation** should include multiple metrics (R², MSE, RMSE, MAE) and use train-test splits or cross-validation

8. The **learning rate (α)** in gradient descent must be chosen carefully—too small leads to slow convergence, too large causes divergence

---

## 10. Multiple Choice Questions

### Level: Easy

**Question 1:** In simple linear regression, what does the slope (θ₁) represent?
- (a) The y-intercept of the regression line
- (b) The change in y for a one-unit change in x
- (c) The number of data points
- (d) The error term

**Answer:** (b) The change in y for a one-unit change in x

---

**Question 2:** Which of the following is the cost function used in linear regression?
- (a) Mean Absolute Error
- (b) Mean Squared Error
- (c) Accuracy
- (d) Precision

**Answer:** (b) Mean Squared Error

---

### Level: Medium

**Question 3:** What happens if the learning rate (α) in gradient descent is set too large?
- (a) The algorithm converges faster
- (b) The algorithm may overshoot the minimum and fail to converge
- (c) The algorithm always finds the global minimum
- (d) The algorithm becomes more accurate

**Answer:** (b) The algorithm may overshoot the minimum and fail to converge

---

**Question 4:** The normal equation for linear regression is: θ = (XᵀX)⁻¹Xᵀy. What is the computational complexity of computing (XᵀX)⁻¹?
- (a) O(n)
- (b) O(n²)
- (c) O(n³)
- (d) O(n⁴)

**Answer:** (c) O(n³)

---

**Question 5:** If R² = 0.85, what does this indicate?
- (a) The model explains 85% of the variance in the target variable
- (b) The model has 85% accuracy
- (c) The error is 85%
- (d) The model uses 85% of the data

**Answer:** (a) The model explains 85% of the variance in the target variable

---

**Question 6:** Which assumption states that the variance of residuals should be constant?
- (a) Linearity
- (b) Independence
- (c) Homoscedasticity
- (d) Normality

**Answer:** (c) Homoscedasticity

---

### Level: Hard

**Question 7:** In gradient descent, if the cost function J(θ) increases after an iteration instead of decreasing, what should be done?
- (a) Increase the learning rate
- (b) Decrease the learning rate
- (c) Change the feature scaling
- (d) Add more features

**Answer:** (b) Decrease the learning rate

---

**Question 8:** What does a negative R² value indicate?
- (a) The model is perfect
- (b) The model is worse than predicting the mean
- (c) There is no correlation
- (d) The model has high variance

**Answer:** (b) The model is worse than predicting the mean

---

**Question 9:** Which metric is most sensitive to outliers?
- (a) Mean Absolute Error (MAE)
- (b) Mean Squared Error (MSE)
- (c) Median Absolute Error
- (d) R² Score

**Answer:** (b) Mean Squared Error (MSE)

---

**Question 10:** For a dataset with 1 million samples, which approach would be more efficient?
- (a) Normal Equation
- (b) Gradient Descent
- (c) Both are equally efficient
- (d) Neither can be used

**Answer:** (b) Gradient Descent (Normal Equation has O(n³) complexity making it impractical for large datasets)

---

## 11. Flashcards

| Term | Definition |
|------|------------|
| **Simple Linear Regression** | A regression model with only one independent variable |
| **Hypothesis Function** | The prediction function: hθ(x) = θ₀ + θ₁x |
| **Cost Function** | Measures the error of the model; for linear regression: J(θ) = (1/2m)Σ(hθ(x⁽ⁱ⁾) - y⁽ⁱ⁾)² |
| **Gradient Descent** | An optimization algorithm that iteratively minimizes the cost function |
| **Learning Rate (α)** | The step size in gradient descent; controls how much parameters change per iteration |
| **Normal Equation** | A closed-form solution: θ = (XᵀX)⁻¹Xᵀy |
| **R² Score** | Coefficient of determination; measures explained variance (0 to 1) |
| **MSE** | Mean Squared Error; average of squared differences between predicted and actual values |
| **RMSE** | Root Mean Squared Error; square root of MSE, in same units as target |
| **MAE** | Mean Absolute Error; average of absolute differences; robust to outliers |
| **Homoscedasticity** | Assumption that error variance is constant across all levels of x |
| **Residuals** | Differences between actual values and predicted values |
| **Overfitting** | Model performs well on training data but poorly on test data |
| **Underfitting** | Model performs poorly on both training and test data |
| **Feature Scaling** | Normalizing feature values to similar ranges for faster gradient descent convergence |

---

## 12. Summary Table: Gradient Descent vs Normal Equation

| Feature | Gradient Descent | Normal Equation |
|---------|------------------|------------------|
| **Type** | Iterative | Analytical |
| **Learning Rate** | Required (hyperparameter) | Not needed |
| **Iterations** | Thousands | One computation |
| **Computational Cost** | O(k × n²) | O(n³) |
| **Large Datasets** | Efficient | Slow |
| **Feature Scaling** | Required | Not required |
| **Memory** | Low | High (matrix inversion) |

---

*This study material is prepared in accordance with the NEP 2024 UGCF curriculum for BSc (Hons) Computer Science, Delhi University. For further practice, students are encouraged to implement these algorithms from scratch and experiment with real-world datasets.*