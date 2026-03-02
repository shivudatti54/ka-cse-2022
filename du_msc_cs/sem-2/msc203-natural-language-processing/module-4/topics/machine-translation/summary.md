# Machine Translation - Summary

## Key Definitions and Concepts
- **BLEU**: Computes n-gram overlap between candidate and reference translations
- **Attention Mechanism**: Neural network layer that learns source-target alignments
- **Subword Tokenization**: Splitting rare words into meaningful subunits (e.g., "unhappiness" → "un", "happiness")

## Important Formulas and Theorems
- **BLEU Score**: BP × exp(∑ wₙ log pₙ) where BP = min(1, e^(1 - r/c))
- **Bahdanau Attention**: αₜ = softmax(vₐ tanh(Wₐ[hₛ; hₜ]))
- **Transformer Self-Attention**: Attention(Q,K,V) = softmax(QKᵀ/√dₖ)V

## Key Points
- Neural MT dominates modern systems but requires large parallel corpora
- Transformer models enable parallel processing through self-attention
- Multilingual models share parameters across languages for better low-resource performance
- Handling named entities requires specialized dictionary lookup modules
- Back-translation is effective for semi-supervised MT
- Gender bias remains a critical issue in pronoun translation
- Hybrid architectures combine neural and rule-based approaches for domain-specific systems

## Common Mistakes to Avoid
- Confusing alignment models (IBM Models 1-5) with translation models
- Neglecting beam search hyperparameters in NMT implementation
- Overlooking subword regularization techniques like BPE dropout
- Misapplying BLEU to languages with rich morphology without proper tokenization

## Revision Tips
- Practice drawing transformer architecture with multi-head attention blocks
- Create comparison tables of SMT vs NMT with 5+ characteristics each
- Memorize BLEU calculation steps through worked examples
- Study Hindi-English specific challenges using ACL anthology papers
- Implement basic seq2seq model with attention on Colab

Length: 400-800 words