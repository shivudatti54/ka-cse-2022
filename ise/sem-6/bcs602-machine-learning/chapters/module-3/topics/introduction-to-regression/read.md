# Linear Regression

## What is Linear Regression?
Linear Regression is a supervised learning algorithm that models the relationship between a dependent variable (target) and one or more independent variables (features) by fitting a linear equation to the observed data.

## Key Concepts

### Simple Linear Regression
Models the relationship between one feature (x) and target (y):

**y = wx + b**

Where:
- **y**: Predicted value (target)
- **x**: Input feature
- **w**: Weight (slope) - how much y changes per unit change in x
- **b**: Bias (intercept) - value of y when x = 0

### Multiple Linear Regression
Extends to multiple features:

**y = w1x1 + w2x2 + ... + wnxn + b**

Or in vector form: **y = w^T x + b**

### Assumptions of Linear Regression
1. **Linearity**: Relationship between X and y is linear
2. **Independence**: Observations are independent
3. **Homoscedasticity**: Constant variance of residuals
4. **Normality**: Residuals are normally distributed
5. **No Multicollinearity**: Features are not highly correlated

## How It Works

### Cost Function (Mean Squared Error)
The model minimizes the average squared difference between predictions and actual values:

**MSE = (1/n) * SUM[(y_actual - y_predicted)^2]**

### Gradient Descent
Iteratively updates weights to minimize MSE:

```
w = w - learning_rate * d(MSE)/dw
b = b - learning_rate * d(MSE)/db
```

### Normal Equation (Closed-form Solution)
Direct solution without iteration:

**w = (X^T X)^(-1) X^T y**

## Complexity Analysis
| Method | Time Complexity | Space Complexity |
|--------|-----------------|------------------|
| Gradient Descent | O(n * d * iterations) | O(d) |
| Normal Equation | O(n * d^2 + d^3) | O(d^2) |
| Prediction | O(d) | O(1) |

Where n = samples, d = features

## Regularization

### Ridge Regression (L2)
Adds penalty for large weights:
**Cost = MSE + lambda * SUM(w^2)**
- Reduces variance, prevents overfitting
- Shrinks coefficients toward zero but never exactly zero

### Lasso Regression (L1)
Adds penalty based on absolute values:
**Cost = MSE + lambda * SUM(|w|)**
- Can set coefficients exactly to zero (feature selection)
- Produces sparse models

### Elastic Net
Combines L1 and L2:
**Cost = MSE + lambda1 * SUM(|w|) + lambda2 * SUM(w^2)**

## Evaluation Metrics
- **MSE**: Mean Squared Error
- **RMSE**: Root Mean Squared Error (same units as target)
- **MAE**: Mean Absolute Error (more robust to outliers)
- **R^2**: Coefficient of determination (variance explained)

## Real-World Applications
- House price prediction
- Sales forecasting
- Stock price trends
- Medical dosage prediction
- Energy consumption estimation

## Summary
- Linear regression fits a line/hyperplane to minimize squared errors
- Simple model with strong interpretability
- Assumptions must be checked for valid inference
- Regularization (Ridge, Lasso) prevents overfitting
- Foundation for understanding more complex models
