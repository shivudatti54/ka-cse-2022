# Logistic Regression

## Overview

Logistic regression is a classification algorithm despite its name. It models the probability that an instance belongs to a particular class using the sigmoid function, making it fundamental for binary and multiclass classification tasks with probabilistic interpretations.

## Key Points

- **Purpose**: Binary classification (spam/not spam, disease/healthy); outputs probability P(y=1|x) ∈ [0,1]
- **Sigmoid Function**: σ(z) = 1/(1+e^(-z)); squashes linear combination w^Tx to [0,1] range
- **Model**: P(y=1|x) = σ(w^Tx + b) = 1/(1+e^(-(w^Tx+b))); predict class 1 if P ≥ 0.5, class 0 otherwise
- **Loss Function**: Cross-entropy (log loss): L = -[y*log(ŷ) + (1-y)*log(1-ŷ)]; penalizes confident wrong predictions heavily
- **Optimization**: Gradient descent; no closed-form solution like linear regression; convex loss guarantees global minimum
- **Multiclass Extension**: One-vs-rest (OvR) or softmax regression for multiple classes

## Important Concepts

- Decision boundary: hyperplane where w^Tx + b = 0 separates classes; linear in feature space
- Outputs calibrated probabilities unlike SVM which gives decision only
- Regularization (L1/L2) prevents overfitting especially with many features
- Coefficients interpretation: positive weight means feature increases probability of class 1

## Notes

- Memorize sigmoid function σ(z) = 1/(1+e^(-z)) and its derivative σ(z)(1-σ(z))
- Understand it's classification not regression despite name; outputs probabilities
- Cross-entropy loss formula essential: L = -[y*log(ŷ) + (1-y)*log(1-ŷ)]
- Decision boundary is linear (straight line in 2D, hyperplane in higher dimensions)
- Compare with linear regression: different loss (cross-entropy vs MSE), different output (probability vs continuous)
