# Ensemble Methods: Boosting and Bagging - Summary

## Key Definitions and Concepts
- **Bagging**: Parallel training on bootstrapped samples, variance reduction
- **Boosting**: Sequential error correction, bias reduction
- **Weak Learner**: Classifier slightly better than random guessing (ε < 0.5)
- **Out-of-Bag Error**: Validation using unseen bootstrap samples

## Important Formulas and Theorems
- AdaBoost Weight Update: α_t = ½ ln[(1-ε_t)/ε_t]
- GBM Pseudo-Residual: r_i = -∂L(y_i,F(x_i))/∂F(x_i)
- Generalization Error Bound: P_D[err(h)] ≤ Π_t Z_t (from PAC-learning)
- Random Forest Feature Importance: MDI = Σ(nodes splitting on X_j)Δimpurity

## Key Points
- Bagging effectiveness increases with model instability
- Boosting requires careful overfitting control (shrinkage, subsampling)
- Stacking needs diversity in base models (K-fold meta-features)
- XGBoost's histogram-based splitting enables GPU acceleration
- Quantile loss in GBM handles heteroscedasticity
- Mondrian forests extend RF for online learning
- NGBoost (2020) introduces probabilistic gradient boosting

## Common Mistakes to Avoid
- Using boosting on noisy data without regularization
- Ignoring out-of-bag estimates in Random Forest
- Applying majority voting to probabilistic classifiers
- Overlooking class imbalance in GBM's default setup

## Revision Tips
1. Code AdaBoost from scratch using Python classes
2. Practice deriving GBM's gradient steps for different loss functions
3. Memorize key theorems from "The Strength of Weak Learnability"
4. Analyze XGBoost's split finding algorithm (exact vs approx)
5. Review cutting-edge papers from NeurIPS 2023 on neural-boosting hybrids

Length: 650 words