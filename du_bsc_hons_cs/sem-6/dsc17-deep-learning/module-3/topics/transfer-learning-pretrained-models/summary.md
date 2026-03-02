# Transfer Learning and Pretrained Models - Summary

## Key Definitions and Concepts

- **Transfer Learning**: A machine learning method where a model developed for one task is reused as the starting point for a model on a different but related task
- **Pretrained Model**: A model trained on a large dataset (e.g., ImageNet with 14 million images) that captures general features
- **Fine-tuning**: Unfreezing some/all pretrained layers and continuing training on the target dataset
- **Feature Extraction**: Using pretrained model weights as fixed feature extractors with a new classification head
- **Catastrophic Forgetting**: The phenomenon where learning new information causes the model to forget previously learned representations

## Important Formulas and Techniques

- **Learning Rate for Fine-tuning**: Typically 10x smaller than training from scratch (1e-4 to 1e-5)
- **Gradual Unfreezing Strategy**: Train classification head first → unfreeze last N layers → progressively unfreeze earlier layers
- **Differential Learning Rates**: Lower LR for early layers (general features), higher LR for late layers (task-specific)

## Key Points

- Transfer learning reduces data requirements and training time significantly
- Early layers of CNNs learn general features (edges, textures) that transfer across domains
- Feature extraction recommended when target dataset < 1,000 samples per class
- Fine-tuning recommended when target dataset > 10,000 samples
- Popular computer vision pretrained models: VGG, ResNet, Inception, EfficientNet, ViT
- Popular NLP pretrained models: BERT, GPT, RoBERTa, DistilBERT
- Data augmentation is essential when fine-tuning on small datasets
- Domain adaptation addresses distribution shift between source and target domains

## Common Mistakes to Avoid

1. **Using too high learning rate** during fine-tuning → destroys pretrained features
2. **Not freezing any layers** on small datasets → overfitting and catastrophic forgetting
3. **Ignoring input shape requirements** of pretrained models (e.g., 224×224 for VGG/ResNet)
4. **Forgetting to preprocess images** using the same preprocessing as original training (ImageNet normalization)

## Revision Tips

1. Practice implementing transfer learning in both TensorFlow and PyTorch before exams
2. Memorize the recommended learning rates and dataset size thresholds
3. Understand the internal workings of at least one pretrained model (ResNet skip connections are exam-friendly)
4. Review case studies of transfer learning in medical imaging and NLP applications
5. Be prepared to draw and explain model architecture diagrams showing frozen vs. trainable layers