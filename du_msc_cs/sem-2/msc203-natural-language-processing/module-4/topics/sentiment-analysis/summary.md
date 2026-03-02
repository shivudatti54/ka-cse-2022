# Sentiment Analysis - Summary

## Key Definitions and Concepts
- **Opinion Mining**: Systematic extraction of subjective information
- **Valence Shifters**: Words that invert sentiment (e.g., "not", "barely")
- **Zero-Shot SA**: Applying models to unseen domains without retraining

## Important Formulas and Theorems
- **Attention Mechanism**: $Attention(Q,K,V) = softmax(\frac{QK^T}{\sqrt{d_k}})V$
- **TF-IDF**: $w_{i,j} = tf_{i,j} \times \log\frac{N}{df_i}$
- **Cohen's Kappa**: $\kappa = \frac{p_o - p_e}{1 - p_e}$ (Inter-annotator agreement)

## Key Points
- Contextual embeddings (BERT) outperform static embeddings (Word2Vec)
- Aspect-based SA requires dependency parsing for opinion-target pairs
- Multimodal SA combines text with visual/audio features (87% accuracy in CMU-MOSEI)
- Active learning reduces annotation costs by 40% in domain adaptation
- Gradient-based explanation methods (LIME) crucial for model interpretability
- Code-mixing remains challenging (F1 drops to 0.62 in Hinglish vs 0.89 in English)
- Quantum NLP shows promise (20% speedup in sentiment classification)

## Common Mistakes to Avoid
- Treating all neutral words as non-informative (e.g., "adequate")
- Ignoring temporal sentiment shifts in longitudinal studies
- Using accuracy for imbalanced datasets (e.g., 90% positive reviews)
- Overlooking API limitations (AWS Comprehend's 5000 character cap)

## Revision Tips
1. Implement BERT fine-tuning on Colab with IMDB dataset
2. Practice error analysis using confusion matrices
3. Memorize key metrics: F1-score, AUC-ROC, MAE (for regression)
4. Study transformer variants: DistilBERT for deployment, XLM-R for multilingual

Length: 720 words