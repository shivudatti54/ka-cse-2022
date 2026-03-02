# Modelling in Machine Learning

## Overview

A model in machine learning is a mathematical function that maps input features to output predictions (y = f(x)). Models encapsulate patterns discovered from training data and serve as the core artifact enabling prediction, classification, or decision-making on new inputs.

## Key Points

- **Parametric Models**: Fixed functional form with fixed number of parameters; fast training, less data needed; examples: Linear Regression, Logistic Regression, Naive Bayes; risk of underfitting
- **Non-Parametric Models**: No fixed form assumption, parameters grow with data; flexible, captures complex patterns; examples: KNN, Decision Trees, SVM; risk of overfitting
- **Model Representation**: Hypothesis function h(x) = w^T x + b where w is weight vector, x is input features, b is bias; parameter vector theta encodes learned knowledge
- **Bias-Variance Tradeoff**: Total Error = Bias² + Variance + Irreducible Noise; low complexity → high bias, high complexity → high variance, optimal → balanced
- **Loss Functions**: MSE for regression (penalizes large errors), Cross-Entropy for classification (measures probability divergence)
- **Gradient Descent**: theta = theta - alpha \* gradient(Loss); learning rate alpha controls step size; variants include batch, stochastic, mini-batch

## Important Concepts

- Parametric vs Non-Parametric: fixed vs growing parameters, low vs high flexibility, fast vs slow training, underfitting vs overfitting risk
- Model complexity determines flexibility in fitting data; finding sweet spot minimizes total error
- Decision boundaries: linear models create hyperplanes, non-linear models create curved/piecewise boundaries
- Model selection criteria: AIC/BIC (balance fit with complexity), Cross-Validation (direct generalization estimate)
- Optimization convergence occurs when loss function change between iterations is below threshold

## Notes

- Always define model as mathematical function mapping inputs to outputs
- Memorize parametric vs non-parametric comparison table - frequent 5-8 mark question
- Know two loss functions: MSE (regression) and Cross-Entropy (classification)
- Write gradient descent update rule: theta = theta - alpha \* gradient
- Explain bias-variance tradeoff with U-shaped total error curve diagram
- Link AIC/BIC to overfitting prevention through complexity penalization
