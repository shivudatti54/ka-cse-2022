# Polynomial and Logistic Regression

## 1. Introduction to Regression

Regression is a fundamental supervised learning technique used to predict a continuous outcome variable (dependent variable) based on one or more predictor variables (independent variables). It establishes a relationship between these variables by fitting a best-fit line or curve to the observed data points.

### 1.1 Linear Regression: A Quick Recap

Linear Regression models the relationship between a dependent variable `y` and one or more independent variables `X` using a linear approach. The model for simple linear regression is:

`y = β₀ + β₁x + ε`

Where:

- `y` is the dependent variable.
- `x` is the independent variable.
- `β₀` is the y-intercept.
- `β₁` is the slope of the line.
- `ε` is the error term.

The parameters `β₀` and `β₁` are estimated using methods like Ordinary Least Squares (OLS), which minimizes the sum of squared differences between the observed and predicted values.

## 2. Polynomial Regression

### 2.1 The Limitation of Linearity

Real-world data is often more complex and rarely follows a perfect straight line. For example, the growth of a plant over time, the spread of a virus, or the depreciation of a car's value are rarely linear processes. Using a simple straight line to model such relationships leads to **underfitting**, where the model is too simple to capture the underlying patterns in the data.

### 2.2 Concept of Polynomial Regression

Polynomial Regression is a form of regression analysis that models the relationship between the independent variable `x` and the dependent variable `y` as an `n-th` degree polynomial. It extends the linear model by adding extra predictors, obtained by raising each of the original predictors to a power.

The model equation for a single feature `x` with degree `d` is:
`y = β₀ + β₁x + β₂x² + ... + β_dx^d + ε`

This allows the model to fit a wide range of curvilinear relationships.

**Example:**
Imagine data points that follow a parabolic path. A linear model would fail, but a 2nd-degree polynomial (quadratic) model would fit perfectly.

```
    y
    ^
    |    *
    |  *   *
    |*       *
    |
    *---------*------> x
```

### 2.3 Implementation and Interpretation

In practice, we create new features: `x²`, `x³`, etc. We then perform multiple linear regression on these new features. Scikit-learn provides a convenient `PolynomialFeatures` transformer for this purpose.

**Important Consideration: Feature Scaling**
When using polynomial terms, the values of `x²`, `x³`, etc., can become very large, leading to numerical instability. It is crucial to apply feature scaling (e.g., StandardScaler) before fitting a polynomial regression model.

### 2.4 The Danger of Overfitting

While polynomial regression can model complex relationships, it is highly susceptible to **overfitting**, especially with high degrees. A model with a very high degree will fit the training data almost perfectly but will fail to generalize to new, unseen data.

```
    y
    ^
    |    *      *
    |  *   *  *   *
    |*             *
    |
    *----------------> x
    High-degree polynomial (overfitting)
    ---- 2nd-degree polynomial (good fit)
    .... Linear regression (underfitting)
```

**How to Choose the Right Degree?**
The optimal degree is a hyperparameter. It is chosen using techniques like:

- **Cross-Validation:** Evaluate model performance on a validation set for different degrees.
- **Visualization:** Plot the fitted curve against the data to assess fit.
- **Regularization:** Use techniques like Ridge or Lasso regression to penalize large coefficients associated with high-degree terms.

## 3. Logistic Regression

### 3.1 From Regression to Classification

While regression predicts continuous values, classification predicts discrete class labels. Logistic Regression is a **classification algorithm**, despite its name. It is used to estimate the probability that an instance belongs to a particular class.

### 3.2 The Logistic Function (Sigmoid)

The core of logistic regression is the **sigmoid function** (or logistic function). It maps any real-valued number into a value between 0 and 1.

**Sigmoid Function:**
`σ(z) = 1 / (1 + e^{-z})`

Where `z` is the linear combination of inputs and weights: `z = β₀ + β₁x₁ + β₂x₂ + ... + β_nx_n`.

The shape of the sigmoid function is an "S-shaped" curve:

```
Probability (y)
  1.0 |    *********
      |   *         *
      |  *           *
  0.5 | *             *
      | *             *
      |*               *
  0.0 |****------------****--> z (linear predictor)
      -∞               +∞
```

As `z` approaches `+∞`, `σ(z)` approaches 1. As `z` approaches `-∞`, `σ(z)` approaches 0.

### 3.3 Making Predictions

The output of the sigmoid function is interpreted as a probability. For binary classification:

- If the estimated probability `ŷ = σ(z)` is greater than or equal to 0.5, the model predicts class 1.
- If the estimated probability `ŷ = σ(z)` is less than 0.5, the model predicts class 0.

The decision boundary, where `z = 0`, is a linear hyperplane. This makes logistic regression a **linear classifier**.

### 3.4 Model Training and Cost Function

The parameters (coefficients `β`) cannot be fit using OLS. Instead, they are estimated using **Maximum Likelihood Estimation (MLE)**. The goal of MLE is to find the parameters that maximize the likelihood that the observed data would be produced by the model.

This is equivalent to minimizing a cost function called **Log Loss** (or Cross-Entropy loss).

**Log Loss for one instance:**
`Cost(ŷ, y) = -[y log(ŷ) + (1 - y) log(1 - ŷ)]`

This function penalizes confident wrong predictions much more than wrong predictions where the model was unsure.

### 3.5 Multinomial Logistic Regression

Logistic Regression can be extended to multi-class classification (e.g., classifying images into cats, dogs, or birds). This is done using the **Softmax Regression** classifier.

- The Softmax function generalizes the sigmoid function to multiple classes.
- It calculates the probability for each class `j` and the predicted class is the one with the highest probability.

## 4. Comparison Table: Polynomial vs. Logistic Regression

| Feature                  | Polynomial Regression                             | Logistic Regression                                                       |
| :----------------------- | :------------------------------------------------ | :------------------------------------------------------------------------ |
| **Type**                 | Regression                                        | Classification                                                            |
| **Output**               | Continuous value (e.g., price, temperature)       | Discrete class label or probability (e.g., spam/not spam)                 |
| **Core Function**        | Polynomial equation (e.g., `y = β₀ + β₁x + β₂x²`) | Sigmoid function (`σ(z) = 1/(1+e^{-z})`)                                  |
| **Decision Boundary**    | Not applicable (predicts a value)                 | Linear (can be made non-linear with kernel tricks or polynomial features) |
| **Cost Function**        | Mean Squared Error (MSE)                          | Log Loss (Cross-Entropy)                                                  |
| **Parameter Estimation** | Ordinary Least Squares (OLS)                      | Maximum Likelihood Estimation (MLE)                                       |
| **Key Challenge**        | Overfitting with high degrees                     | Feature scaling, multicollinearity                                        |

## 5. Exam Tips

1.  **Understand the "Why":** Don't just memorize formulas. Understand _why_ we need polynomial regression (non-linear data) and _why_ logistic regression uses a sigmoid function (to output probabilities).
2.  **Visualize the Curves:** Be able to sketch what a 2nd-degree (quadratic) or 3rd-degree (cubic) polynomial fit might look like on a scatter plot. Similarly, sketch the sigmoid function and interpret its axes.
3.  **Overfitting is Key:** For polynomial regression, the most common exam question revolves around the trade-off between bias and variance. Be prepared to explain overfitting and how to prevent it (e.g., cross-validation, regularization).
4.  **Interpret the Coefficients:** In linear regression, `β₁` is the change in `y` for a one-unit change in `x`. In logistic regression, `β₁` is the change in the _log-odds_ of the outcome for a one-unit change in `x`. You may need to transform this into an **odds ratio** (`e^{β₁}`).
5.  **Know the Cost Functions:** Be able to name and briefly describe the cost functions: MSE for regression and Log Loss for logistic regression. Understand why MSE isn't suitable for logistic regression (it's not convex, leading to local minima).
6.  **Terminology:** Use the correct terms: "sigmoid function," "log odds," "decision boundary," "maximum likelihood," "polynomial features," and "regularization."
