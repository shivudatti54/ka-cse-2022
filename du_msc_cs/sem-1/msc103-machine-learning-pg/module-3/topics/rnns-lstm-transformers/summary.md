# RNNs, LSTMs, and Transformers - Summary

## Key Definitions and Concepts
- **RNN**: Neural network with cyclic connections for sequential processing
- **LSTM**: RNN variant with input, forget, output gates to control information flow
- **Transformer**: Attention-based architecture without recurrence
- **BPTT**: Backpropagation Through Time for RNN training
- **Self-attention**: Mechanism computing relationships between all sequence positions

## Important Formulas and Theorems
- **LSTM Gates**:
  \( f_t = \sigma(W_f \cdot [h_{t-1}, x_t] + b_f) \)
- **Transformer Attention**:
  \( \text{Attention}(Q,K,V) = \text{softmax}(\frac{QK^T}{\sqrt{d_k}})V \)
- **Positional Encoding**:
  \( PE(pos,2i) = \sin(pos/10000^{2i/d}) \)
  \( PE(pos,2i+1) = \cos(pos/10000^{2i/d}) \)

## Key Points
- LSTMs solve vanishing gradients through gated memory cells
- Transformers enable parallel processing through self-attention
- Multi-head attention captures diverse relationship patterns
- Positional encodings replace recurrence for sequence order
- Layer normalization stabilizes transformer training
- Sparse attention reduces O(T²) complexity
- Hybrid models (e.g., ConvTransformer) combine multiple paradigms

## Common Mistakes to Avoid
- Using RNNs for very long sequences (>100 steps)
- Negging gradient clipping in RNN implementations
- Confusing cell state with hidden state in LSTMs
- Implementing attention without proper scaling (1/√d_k factor)

## Revision Tips
1. Create architecture comparison table (RNN vs LSTM vs Transformer)
2. Practice deriving gradients for 3-step RNN
3. Implement multi-head attention using NumPy
4. Study ablation studies from original Transformer paper
5. Explore HuggingFace implementations of BERT/GPT