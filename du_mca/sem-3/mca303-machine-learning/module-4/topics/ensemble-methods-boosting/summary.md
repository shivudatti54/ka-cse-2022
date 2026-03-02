# Ensemble Methods - Boosting - Summary

## Key Definitions and Concepts

- **Ensemble Learning**: Combining multiple base learners to create a single strong learner that outperforms individual models.
- **Weak Learner**: A base model that performs slightly better than random guessing (e.g., decision stump).
- **Strong Learner**: A high-accuracy model created by combining weak learners through boosting.
- **Boosting**: Sequential ensemble method where each learner focuses on correcting errors made by previous learners.
- **AdaBoost**: The original adaptive boosting algorithm that adjusts sample weights based on classification errors.
- **Gradient Boosting**: General boosting framework that minimizes differentiable loss functions via gradient descent.
- **XGBoost**: Extreme Gradient Boosting with regularization and efficient computation.
- **Learning Rate (η)**: Shrinkage parameter controlling each tree's contribution to prevent overfitting.

## Important Formulas and Theorems

- **AdaBoost Learner Weight**: α_t = (1/2) × ln((1 - ε_t) / ε_t)
- **AdaBoost Weight Update**: w_i ← w_i × exp(-α_t × y_i × h_t(x_i))
- **Final AdaBoost Classifier**: H(x) = sign(Σ α_t × h_t(x_t))
- **Gradient Boosting Update**: F_m(x) = F_{m-1}(x) + η × h_m(x)
- **Pseudo-residuals**: r_im = -[∂L(y_i, F(x_i)) / ∂F(x_i)]_{F=F_{m-1}}

## Key Points

- Boosting reduces bias (systematic error) while maintaining low variance through sequential error correction.
- AdaBoost minimizes exponential loss and can be interpreted as gradient descent in function space.
- The exponential weight update in AdaBoost increases focus on misclassified samples.
- Gradient Boosting generalizes AdaBoost to arbitrary loss functions (MSE, MAE, log loss).
- XGBoost adds L1/L2 regularization to prevent overfitting: Ω(f) = γT + (1/2)λ||w||².
- LightGBM uses histogram-based splitting and leaf-wise growth for faster training.
- Smaller learning rates require more trees but often yield better generalization.
- Early stopping prevents overfitting by monitoring validation error during training.
- Boosting is particularly effective for complex, non-linear relationships in data.
- Feature importance in boosting is computed based on split gain or coverage.

## Common Mistakes to Avoid

- Confusing boosting with bagging—bagging reduces variance while boosting reduces bias.
- Using too complex base learners (deep trees) which defeats the purpose of sequential correction.
- Setting learning rate too high, leading to overfitting on training data.
- Not using early stopping or cross-validation, resulting in overfitted models.
- Ignoring the computational cost of sequential training in boosting algorithms.

## Revision Tips

1. Practice tracing through one complete AdaBoost iteration by hand to understand weight updates.
2. Create a comparison table of AdaBoost vs. Gradient Boosting vs. XGBoost covering algorithm, loss function, regularization, and speed.
3. Remember the bias-variance tradeoff: Bagging → reduces variance; Boosting → reduces bias.
4. Review the mathematical derivation of learner weight α_t in AdaBoost and understand why it increases when error decreases.
5. Know practical applications: fraud detection (imbalanced), medical diagnosis, and recommendation systems where boosting excels.