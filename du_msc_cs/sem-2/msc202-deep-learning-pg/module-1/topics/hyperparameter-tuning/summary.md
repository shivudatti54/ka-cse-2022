# Hyperparameter Tuning - Summary

## Key Definitions and Concepts
- **Hyperparameter**: Configurable parameter not learned during training (e.g., learning rate)
- **Exploitation-Exploration Tradeoff**: Balancing local search vs global exploration
- **Multi-Fidelity Optimization**: Using partial training (epochs, subsets) to evaluate candidates
- **Hypergradient**: Gradient of validation loss w.r.t hyperparameters

## Important Formulas and Theorems
- **Expected Improvement (EI)**: EI(x) = 𝔼[max(f(x) - f(x⁺), 0)]
- **Hyperband Resource Allocation**: n_i = n_0 * η^i (η=elimination rate)
- **Differentiable NAS**: ∇_αL_val(w*(α), α) using chain rule through architecture parameters α
- **Learning Rate Warmup**: η_t = min(η_max, η_min + t/T * (η_max - η_min))

## Key Points
- Random search outperforms grid search in high dimensions (≥5 hyperparameters)
- Bayesian optimization uses surrogate models to guide search
- Nested cross-validation prevents overfitting in hyperparameter selection
- Neural architecture search can automate network design but is computationally expensive
- Learning rate is the most sensitive hyperparameter in most architectures
- Always decouple hyperparameter search data from final test evaluation
- Emerging trend: Zero-Cost Proxies for architecture evaluation (e.g., NASWOT)

## Common Mistakes to Avoid
- Using test set for hyperparameter tuning (data leakage)
- Insufficient budget for Bayesian optimization (needs ≥30 iterations)
- Ignoring hardware constraints (e.g., batch size vs GPU memory)
- Early stopping without proper validation checks

## Revision Tips
- Create comparison tables: Grid vs Random vs Bayesian vs Evolutionary
- Practice implementing Hyperband with Keras Tuner
- Study the original Random Search paper (Bergstra & Bengio 2012)
- Use MNIST/CIFAR-10 for hands-on tuning experiments
- Review gradient-based hyperparameter optimization mathematics

Length: 650 words