# Text Book 1: Ch 1 & 2 Summary

### Machine Learning II

#### Introduction

- Well-Posed Learning Problems:
  - Problem definition
  - Clear evaluation criterion
  - Finite training data
  - No constraints on the learning system

#### Designing a Learning System

- Model selection
- Model training
- Model evaluation
- Model selection criteria (e.g., bias-variance tradeoff, cross-validation)

#### Key Concepts

- **Dictionary Learning**:
  - Definition: learning a dictionary that represents the data
  - Example: sparse coding, denoising
- **Regularization**:
  - Definition: adding a penalty term to the loss function to prevent overfitting
  - Examples: L1, L2, dropout

#### Important Formulas and Definitions

- **Bias-variance tradeoff**:
  - Definition: the tradeoff between model complexity and fit
  - Formula: $Variance = \sigma^2 = \frac{1}{n} \sum_{i=1}^n (y_i - \hat{y_i})^2$
- **Cross-validation**:
  - Definition: evaluating model performance on unseen data
  - Formula: $CV = \frac{1}{n} \sum_{i=1}^n \frac{1}{k} \sum_{j=1}^k L(y_i, \hat{y_i}^{(j)})$
- **Overfitting**:
  - Definition: when a model is too complex and fits the training data too well
  - Example: L1, L2 regularization

#### Important Theorems

- **No Free Lunch Theorem**:
  - Definition: there is no universally optimal model
  - Implication: model selection criteria are necessary
