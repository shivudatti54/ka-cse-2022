# Attention Mechanisms and Transformers

## Introduction
Attention mechanisms revolutionized deep learning by enabling models to dynamically focus on relevant parts of input sequences. Introduced in 2017 through the "Attention Is All You Need" paper, transformers eliminated the need for recurrent networks while achieving state-of-the-art performance in NLP tasks. This paradigm shift allows parallel processing of sequential data and better handling of long-range dependencies.

The core innovation lies in self-attention - a mechanism that computes contextual relationships between all positions in a sequence simultaneously. Transformers have become fundamental to modern AI systems, powering models like GPT-4, BERT, and T5. Their applications extend beyond text to vision (ViT), audio processing, and multimodal systems.

For DU MSc CS students, understanding transformers is crucial for research in cutting-edge NLP, computer vision, and generative AI. This architecture's mathematical foundations and scalability make it essential for tackling complex sequence modeling problems.

## Key Concepts
1. **Self-Attention Mechanism**:
   - Computes attention scores using query, key, value vectors
   - Formula: Attention(Q,K,V) = softmax(QKᵀ/√d_k)V
   - Scaled dot-product prevents gradient vanishing in high dimensions

2. **Multi-Head Attention**:
   - Parallel attention heads capture different semantic relationships
   - Enables model to focus on multiple positions simultaneously
   - Concatenated outputs passed through linear transformation

3. **Positional Encoding**:
   - Injects sequence order information using sine/cosine functions
   - PE(pos,2i) = sin(pos/10000^(2i/d_model))
   - Learned alternatives available but fixed encodings common

4. **Transformer Architecture**:
   - Encoder-decoder structure with residual connections
   - Layer normalization and feed-forward networks
   - Masked attention in decoder for autoregressive generation

5. **Cross-Attention**:
   - Links encoder and decoder in sequence-to-sequence tasks
   - Allows decoder to attend to encoder's hidden states

## Examples

**Example 1: Calculating Self-Attention**
Input: Sequence of 3 tokens with embedding dimension d=4
Embeddings: X = [[1,0,1,0], [0,2,0,2], [1,1,1,1]]
Weight matrices: W_Q, W_K, W_V (4x3 each)

Steps:
1. Compute Q = XW_Q, K = XW_K, V = XW_V
2. Calculate attention scores: QKᵀ = [[4,12,6], [12,36,18], [6,18,10]]
3. Scale and softmax: Divide by √3, apply row-wise softmax
4. Multiply with V to get final embeddings

**Example 2: Positional Encoding Visualization**
For d_model=4 and position=1:
PE(1) = [sin(1/1), cos(1/1), sin(1/10000^(2/4)), cos(1/10000^(2/4))]
≈ [0.8415, 0.5403, 0.00999983, 0.99995]

**Example 3: Building Transformer Block**
Implement encoder layer in PyTorch:
```python
class EncoderLayer(nn.Module):
    def __init__(self, d_model, num_heads):
        super().__init__()
        self.mha = MultiheadAttention(d_model, num_heads)
        self.ffn = PositionwiseFFN(d_model)
        self.norm1 = LayerNorm(d_model)
        self.norm2 = LayerNorm(d_model)
    
    def forward(self, x):
        attn_out = self.mha(x)
        x = self.norm1(x + attn_out)
        ffn_out = self.ffn(x)
        return self.norm2(x + ffn_out)
```

## Exam Tips
1. Derive attention gradients mathematically - focus on softmax derivatives
2. Compare computational complexity: O(n²d) vs O(n²) for RNNs
3. Understand rotary positional encoding (RoPE) variants
4. Explain why transformers need more data than RNNs
5. Draw complete architecture diagram with dimensions
6. Implement causal masking for decoder self-attention
7. Analyze attention patterns in different heads (syntax vs semantics)