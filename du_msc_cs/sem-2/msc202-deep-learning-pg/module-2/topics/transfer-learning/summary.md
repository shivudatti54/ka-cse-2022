# Transfer Learning - Summary

## Key Definitions and Concepts
- **Transfer Learning**: Leveraging knowledge from source domain/task to improve target domain/task learning
- **Domain**: D = {X, P(X)} where X is feature space and P(X) is marginal distribution
- **Task**: T = {Y, P(Y|X)} consisting of label space and conditional distribution
- **Negative Transfer**: When source knowledge hurts target performance

## Important Formulas and Theorems
- **H-score**: H(φ) = tr(cov⁻¹(Ȳ)cov(Ȳ)) (Feature transferability metric)
- **LEEP**: T(ỹ|y)P(y|x) (Log Expected Empirical Prediction)
- **MMD**: ‖E[φ(x_s)] - E[φ(x_t)]‖² (Domain discrepancy measure)
- **Catastrophic Forgetting**: L = L_new + λ‖θ - θ_old‖² (Elastic Weight Consolidation)

## Key Points
- Transfer learning is most effective when domains are related but not identical
- Early layers typically transfer better than later layers
- Optimal freezing strategy depends on dataset similarity
- Adversarial methods excel in domain adaptation scenarios
- Multimodal foundation models enable zero-shot transfer
- Transferability metrics prevent negative transfer
- Ethical audits are crucial for pre-trained model deployment

## Common Mistakes to Avoid
- Using ImageNet models for non-visual tasks without adaptation
- Overfitting small target datasets during fine-tuning
- Ignoring source domain data distribution shifts
- Applying transfer learning indiscriminately to all layers
- Neglecting computational costs of large foundation models

## Revision Tips
- Create comparative tables of model zoology (ResNet, BERT, CLIP)
- Practice implementing gradient checkpointing for large models
- Memorize key transfer learning survey papers (Torrey et al. 2010, Zhuang et al. 2020)
- Use PyTorch Lightning's transfer learning boilerplate code
- Study failure cases from medical AI deployment papers