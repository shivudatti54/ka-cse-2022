# **Model Multiplicity**

### Definition

- Model multiplicity refers to the situation where multiple models are equally good at explaining the data, i.e., they have the same likelihood or information criterion value.

### Key Points

- Model multiplicity occurs when there are multiple models with the same optimal value of a model selection criterion (e.g., AIC, BIC).
- There are two types of model multiplicity:
  - **Model multiplicity by model size**: This occurs when different models have the same optimal value, but the models have different sizes.
  - **Model multiplicity by model complexity**: This occurs when different models have the same optimal value, but the models have the same size and complexity.

### Theorems

- **The Consistency Theorem**: In a large sample, the estimated model that is chosen by the model selection criterion (e.g., AIC, BIC) is consistent and will converge to the true model.
- **The Efficiency Theorem**: The model with the minimum AIC or BIC value has the highest efficiency and is the most parsimonious model.

### Important Formulas

- Akaike information criterion (AIC): `AIC = 2k - 2ln(L)`, where `k` is the number of parameters and `L` is the log likelihood.
- Bayesian information criterion (BIC): `BIC = k * ln(n) + c`, where `n` is the sample size, `k` is the number of parameters, and `c` is a constant.

### Model Selection Criteria

- AIC: prefers models with lower values of `k` and higher values of `L`.
- BIC: prefers models with lower values of `k` and higher values of `L` compared to AIC.

### Model Evaluation

- **Cross-validation (CV)**: used to evaluate the performance of models on unseen data.
- **Information criteria**: can be used to compare the performance of models, but should be used with caution due to model multiplicity.
