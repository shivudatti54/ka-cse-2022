# Attention Mechanisms and Transformers - Summary

## Key Definitions and Concepts
- **Self-Attention**: Content-based addressing mechanism relating all sequence positions
- **Query/Key/Value**: Learned projections for attention computation
- **Positional Encoding**: Function preserving sequence order information
- **Transformer**: Stacked self-attention and feed-forward layers with residuals

## Important Formulas and Theorems
- Scaled Dot-Product Attention: 
  $$\text{Attention}(Q,K,V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$
- Multi-Head Attention:
  $$\text{MultiHead}(Q,K,V) = \text{Concat}(head_1,...,head_h)W^O$$
- Positional Encoding:
  $$PE_{(pos,2i)} = \sin(pos/10000^{2i/d_{model}})$$
  $$PE_{(pos,2i+1)} = \cos(pos/10000^{2i/d_{model}})$$

## Key Points
- Transformers enable parallel sequence processing unlike RNNs
- Attention complexity grows quadratically with sequence length
- Residual connections mitigate vanishing gradients in deep stacks
- Layer normalization stabilizes training dynamics
- Masked self-attention prevents information leakage in decoders
- Modern variants use sparse attention to reduce computation
- Cross-attention bridges encoder-decoder information flow

## Common Mistakes to Avoid
- Forgetting to scale attention scores before softmax
- Misapplying attention masks in encoder-decoder architectures
- Negging positional encodings when input sequences are position-sensitive
- Confusing multi-head attention with multiple attention layers

## Revision Tips
1. Practice deriving gradient equations for attention mechanism
2. Implement transformer from scratch using NumPy
3. Visualize attention patterns using heatmaps for sample sentences
4. Study ablation studies from original transformer paper
5. Explore efficient attention implementations (FlashAttention, Linformer)