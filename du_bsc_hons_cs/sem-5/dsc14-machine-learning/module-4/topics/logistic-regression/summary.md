# Logistic Regression - Summary

## Key Definitions and Concepts

- **Logistic Regression**: A classification algorithm that models the probability of belonging to a class using the sigmoid function; despite the name, it performs classification, not regression.

- **Sigmoid Function**: σ(z) = 1/(1 + e^(-z)), transforms any real number to a value between 0 and 1, representing probability.

- **Log-Odds (Logit)**: The natural logarithm of odds: logit(P) = ln(P/(1-P)), which is modeled as a linear function of features in logistic regression.

- **Decision Boundary**: The threshold (typically at probability 0.5) that separates classes; for logistic regression, this is linear: wx + b = 0.

- **One-vs-Rest (OvR)**: A multiclass strategy training K binary classifiers, one for each class against all others.

- **Softmax Regression**: Generalization of logistic regression for multiclass problems using the softmax function.

## Important Formulas and Theorems

- **Sigmoid**: σ(z) = 1 / (1 + e^(-z))
- **Hypothesis**: h(x) = σ(wx + b)
- **Log Loss (Cost)**: J(w,b) = -1/m * Σ[y*log(ŷ) + (1-y)*log(1-ŷ)]
- **Gradient Descent**: w := w - α * (1/m) * Σ(ŷ - y) * x
- **Odds Ratio**: e^(coefficient) - indicates change in odds per unit feature change

## Key Points

- Logistic regression outputs probabilities between 0 and 1, making it suitable for binary classification with probabilistic interpretations.

- The sigmoid function ensures bounded output and creates the characteristic S-shaped curve for probability estimation.

- Log loss is used instead of MSE because it creates a convex cost function, guaranteeing convergence to global optimum.

- The decision boundary is linear in the original feature space, limiting logistic regression to linearly separable problems.

- Coefficients can be exponentiated to obtain odds ratios for intuitive interpretation (e.g., 5% increase in odds per unit change).

- Multiclass problems require strategies like One-vs-Rest or Softmax; Softmax provides proper probability distributions over all classes.

- Logistic regression is highly interpretable, making it valuable in healthcare, finance, and other domains requiring explainable models.

## Common Mistakes to Avoid

- **Confusing with linear regression**: Remember logistic regression is for classification (discrete outputs), not regression (continuous outputs). The hypothesis uses sigmoid, not direct linear output.

- **Using wrong cost function**: Never use Mean Squared Error for logistic regression—it creates non-convex loss landscapes with local minima. Always use log loss.

- **Ignoring feature scaling**: Without feature scaling, gradient descent converges slowly or may not converge at all due to uneven feature ranges.

- **Setting threshold blindly**: While 0.5 is the default threshold, it may not be optimal for imbalanced datasets—always consider the context and potentially adjust.

- **Forgetting the intercept**: The bias term b is crucial even when features seem to have zero mean; it shifts the decision boundary.

## Revision Tips

1. **Practice deriving the gradient**: Work through the partial derivative of log loss with respect to weights—it reinforces understanding of how gradient descent updates occur.

2. **Draw decision boundaries**: Sketch simple 2D examples with positive and negative coefficients to visualize how the line wx + b = 0 separates classes.

3. **Interpret real coefficients**: Practice exponentiating coefficients and explaining what "e^0.7 = 2.01 means odds doubled" type interpretations.

4. **Compare with k-NN**: Understand why logistic regression is parametric (fixed number of parameters) while k-NN is non-parametric, and the implications for overfitting.

5. **Code from scratch**: Implement logistic regression with gradient descent in Python without libraries—this solidifies the mathematical concepts.