# POS Tagging and Named Entity Recognition (NER) - Summary

## Key Definitions and Concepts
- POS Tagging: Assigning grammatical categories to words
- NER: Identifying named entities and classifying them
- HMM: Probabilistic model with hidden states (tags) and observations (words)
- BIO Scheme: Begin, Inside, Outside entity tagging format

## Important Formulas and Theorems
- Viterbi Path Probability: δₜ(j) = maxₐ[δₜ₋₁(a) * P(qⱼ|qₐ) * P(wₜ|qⱼ)]
- F1 Score: 2 * (Precision * Recall) / (Precision + Recall)
- CRF Objective: P(y|x) = (1/Z(x)) exp(Σλₖfₖ(y,x))

## Key Points
- Context window size critically impacts tagging accuracy
- Handling unknown words requires subword modeling
- Transformer models outperform traditional methods but require more data
- Domain adaptation is crucial for real-world applications
- NER systems struggle with nested entities (e.g., "New York Times")
- Multilingual BERT enables zero-shot cross-lingual transfer
- Active learning reduces annotation costs for NER

## Common Mistakes to Avoid
- Confusing token-level vs span-level evaluation
- Ignoring case sensitivity in NER
- Mishandling sentence boundaries in document-level tagging
- Overlooking class imbalance in entity categories

## Revision Tips
1. Practice Viterbi calculations on paper for small examples
2. Memorize CoNLL-2003 evaluation criteria
3. Compare architectures using ACL Anthology papers
4. Implement a basic CRF using sklearn-crfsuite
5. Explore HuggingFace's transformers library for NER fine-tuning