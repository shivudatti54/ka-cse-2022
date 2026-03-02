# BERT & GPT Language Models - Summary

## Key Definitions and Concepts
- **Self-Attention**: Mechanism to weigh relationships between tokens
- **MLM**: BERT's pretraining task masking random tokens
- **Causal Masking**: GPT's restriction to prevent future token visibility

## Important Formulas and Theorems
- Scaled Dot-Product Attention: $\text{Attention}(Q,K,V) = \text{softmax}(\frac{QK^T}{\sqrt{d_k}})V$
- Positional Encoding: $PE_{(pos,2i)} = \sin(pos/10000^{2i/d_{model}})$
- Perplexity: $PP(W) = \sqrt[N]{\prod_{i=1}^N \frac{1}{P(w_i|w_{<i})}}$

## Key Points
- BERT excels in understanding tasks (Q&A, NER), GPT in generation
- Transformer layers enable parallel computation during training
- Pretraining requires massive computational resources (TPU/GPU clusters)
- Fine-tuning adapts models to specific domains with limited data
- Ethical concerns include environmental impact and bias propagation

## Common Mistakes to Avoid
- Confusing encoder-decoder architecture with decoder-only (GPT)
- Misapplying MLM pretraining to autoregressive tasks
- Overlooking gradient checkpointing in memory management
- Neglecting tokenization differences (WordPiece vs BPE)

## Revision Tips
1. Create comparison tables: BERT vs GPT vs Traditional RNNs
2. Practice attention matrix visualization for sample sentences
3. Implement a mini-transformer from scratch using PyTorch
4. Review recent papers on model compression (e.g., DistilBERT)

Length: 650 words