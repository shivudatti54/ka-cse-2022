# Challenges of Machine Learning - Summary

## Key Definitions and Concepts

- **Overfitting**: When a model learns noise in training data, failing to generalize to unseen data
- **Underfitting**: When a model is too simple to capture underlying patterns in data
- **Bias-Variance Tradeoff**: The inverse relationship between model complexity and generalization error
- **Model Drift**: Degradation of model performance due to changes in data distributions over time
- **Class Imbalance**: Uneven distribution of classes in training data
- **Adversarial Attacks**: Malicious inputs designed to fool ML models

## Important Formulas and Theorems

- **Bias-Variance Decomposition**: Total Error = Bias² + Variance + Irreducible Error
- **F1-Score**: Harmonic mean of precision and recall = 2 × (Precision × Recall) / (Precision + Recall)
- **SMOTE**: Synthetic Minority Over-sampling Technique creates synthetic samples by interpolating between minority class examples

## Key Points

- Data quality issues (missing values, noise, outliers) consume 60-80% of ML project time
- The bias-variance tradeoff explains why model complexity must be carefully balanced
- Class imbalance requires specialized techniques; accuracy is misleading for imbalanced data
- Model interpretability is crucial for high-stakes applications in healthcare and finance
- Production ML requires continuous monitoring for concept drift and data drift
- Ethical challenges include data bias, privacy erosion, and environmental impact

## Common Mistakes to Avoid

- Using accuracy as the sole evaluation metric for imbalanced datasets
- Ignoring data preprocessing and jumping directly to model training
- Assuming trained models will perform consistently over time without monitoring
- Overlooking the interpretability requirements when deploying in regulated industries
- Treating ML as a one-time development process rather than an iterative lifecycle

## Revision Tips

1. Practice drawing and explaining the bias-variance curve from memory
2. Memorize at least 2 techniques for each major challenge category
3. Review real-world ML failure case studies (Amazon hiring tool, COMPAS, facial recognition biases)
4. Understand why cross-validation provides more reliable estimates than single train-test splits
5. Be prepared to explain how you would handle a scenario where a production model performance degrades over time