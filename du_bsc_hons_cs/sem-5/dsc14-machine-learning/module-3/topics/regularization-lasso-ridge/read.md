# Regularization: Lasso and Ridge
## Introduction

Regularization is a fundamental concept in machine learning that helps prevent overfitting by adding a penalty term to the loss function. This penalty term discourages the model from overfitting to the training data, resulting in better generalization performance on unseen data. In this topic, we will explore two popular regularization techniques: Lasso and Ridge.

Lasso (Least Absolute Shrinkage and Selection Operator) and Ridge (also known as L2 regularization) are two widely used regularization techniques in linear regression. Both techniques add a penalty term to the loss function, but they differ in the type of penalty used. Lasso uses an L1 penalty, which adds a term proportional to the absolute value of the coefficients, while Ridge uses an L2 penalty, which adds a term proportional to the square of the coefficients.

## Key Concepts

### Lasso Regularization

Lasso regularization adds an L1 penalty term to the loss function, which is proportional to the absolute value of the coefficients. The Lasso loss function can be written as:

L = (y - Xw)^2 + α|w|

where y is the target variable, X is the feature matrix, w is the weight vector, and α is the regularization parameter.

The L1 penalty term has the effect of setting some coefficients to zero, effectively performing feature selection. This is because the L1 penalty is not differentiable at zero, so the optimizer will set some coefficients to zero to minimize the penalty term.

### Ridge Regularization

Ridge regularization adds an L2 penalty term to the loss function, which is proportional to the square of the coefficients. The Ridge loss function can be written as:

L = (y - Xw)^2 + αw^2

where y is the target variable, X is the feature matrix, w is the weight vector, and α is the regularization parameter.

The L2 penalty term has the effect of shrinking the coefficients towards zero, but not setting them exactly to zero. This is because the L2 penalty is differentiable everywhere, so the optimizer will reduce the magnitude of the coefficients to minimize the penalty term.

### Comparison of Lasso and Ridge

Lasso and Ridge regularization have different effects on the model:

* Lasso performs feature selection by setting some coefficients to zero, while Ridge shrinks the coefficients towards zero.
* Lasso is more robust to outliers, while Ridge is more sensitive to outliers.
* Lasso can result in sparse models, while Ridge results in dense models.

## Examples

### Example 1: Lasso Regularization

Suppose we have a dataset with two features, X1 and X2, and a target variable y. We want to train a linear regression model with Lasso regularization.

| X1 | X2 | y |
| --- | --- | --- |
| 1  | 2  | 3 |
| 2  | 3  | 4 |
| 3  | 4  | 5 |

We can write the Lasso loss function as:

L = (y - Xw)^2 + α|w|

where w = [w1, w2] is the weight vector.

To minimize the loss function, we can use gradient descent. The gradient of the loss function with respect to w is:

∂L/∂w = -2X^T(y - Xw) + αsign(w)

where sign(w) is the sign function, which returns 1 if w is positive and -1 if w is negative.

### Example 2: Ridge Regularization

Suppose we have the same dataset as before, but we want to train a linear regression model with Ridge regularization.

We can write the Ridge loss function as:

L = (y - Xw)^2 + αw^2

where w = [w1, w2] is the weight vector.

To minimize the loss function, we can use gradient descent. The gradient of the loss function with respect to w is:

∂L/∂w = -2X^T(y - Xw) + 2αw

### Example 3: Comparison of Lasso and Ridge

Suppose we have a dataset with 10 features and a target variable. We want to compare the performance of Lasso and Ridge regularization.

We can train two linear regression models, one with Lasso regularization and one with Ridge regularization. We can then compare the coefficients of the two models.

The Lasso model may set some coefficients to zero, while the Ridge model will shrink the coefficients towards zero.

## Exam Tips

1. Understand the difference between Lasso and Ridge regularization.
2. Know how to write the loss function for Lasso and Ridge regularization.
3. Understand how to minimize the loss function using gradient descent.
4. Be able to compare the effects of Lasso and Ridge regularization on the model.
5. Know how to choose the regularization parameter α.
6. Understand how to interpret the coefficients of a Lasso or Ridge model.
7. Be able to implement Lasso and Ridge regularization in Python using scikit-learn.