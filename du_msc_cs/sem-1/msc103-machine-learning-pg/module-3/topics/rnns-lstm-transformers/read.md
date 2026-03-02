# RNNs, LSTMs, and Transformers

## Introduction
Recurrent Neural Networks (RNNs), Long Short-Term Memory (LSTM) networks, and Transformers form the cornerstone of modern sequence modeling in machine learning. These architectures address the critical challenge of processing sequential data while maintaining context awareness - a fundamental requirement for tasks like natural language processing, time series forecasting, and speech recognition.

RNNs emerged as the first neural architecture explicitly designed for sequential data, using hidden states to maintain temporal context. However, their limitations in handling long-range dependencies due to vanishing/exploding gradients led to the development of LSTMs with specialized memory cells and gating mechanisms. The recent Transformer architecture revolutionized the field through self-attention mechanisms, enabling parallel processing while capturing global dependencies more effectively.

These models underpin cutting-edge applications from Google's BERT to OpenAI's GPT series. Current research focuses on hybrid architectures, efficiency optimizations, and multimodal extensions. Understanding their mathematical foundations and implementation nuances is crucial for advancing in NLP research and industrial applications.

## Key Concepts

**1. RNN Fundamentals:**
- Hidden state propagation: \( h_t = \sigma(W_h h_{t-1} + W_x x_t + b) \)
- Backpropagation Through Time (BPTT)
- Vanishing gradient problem analysis using Jacobian matrices

**2. LSTM Architecture:**
- Cell state vs hidden state
- Gating mechanisms:
  - Forget gate: \( f_t = \sigma(W_f [h_{t-1}, x_t] + b_f) \)
  - Input gate: \( i_t = \sigma(W_i [h_{t-1}, x_t] + b_i) \)
  - Output gate: \( o_t = \sigma(W_o [h_{t-1}, x_t] + b_o) \)
- Peephole connections and variants

**3. Transformer Model:**
- Self-attention mechanism: 
  \( \text{Attention}(Q,K,V) = \text{softmax}(\frac{QK^T}{\sqrt{d_k}})V \)
- Multi-head attention and positional encoding
- Layer normalization and residual connections

**4. Advanced Topics:**
- Bidirectional RNNs for context fusion
- Transformer-XL for longer context handling
- Sparse attention patterns (e.g., Longformer, BigBird)

## Examples

**1. Character-Level Language Modeling with LSTM:**
```python
# Model Architecture
model = Sequential()
model.add(LSTM(256, input_shape=(SEQ_LENGTH, VOCAB_SIZE)))
model.add(Dense(VOCAB_SIZE, activation='softmax'))

# Training
model.compile(loss='categorical_crossentropy', optimizer='adam')
model.fit(generator, epochs=50, callbacks=[EarlyStopping(patience=3)])
```
*Analysis: The LSTM maintains character generation coherence through 256 hidden units, with dropout layers preventing overfitting.*

**2. Machine Translation with Transformer:**
```python
# Positional Encoding Implementation
def positional_encoding(position, d_model):
    angle_rates = 1 / np.power(10000, (2 * (np.arange(d_model)//2)) / d_model)
    angle_rads = np.arange(position)[:, np.newaxis] * angle_rates[np.newaxis, :]
    angle_rads[:, 0::2] = np.sin(angle_rads[:, 0::2])
    angle_rads[:, 1::2] = np.cos(angle_rads[:, 1::2])
    return angle_rads
```
*Application: This encoding allows the model to learn relative positions without recurrence, crucial for parallel processing.*

**3. Gradient Analysis in Vanilla RNN:**
Given loss \( L \), compute \( \frac{\partial L}{\partial W_h} \) over sequence length T:
\[
\frac{\partial L}{\partial W_h} = \sum_{k=1}^T \frac{\partial L}{\partial h_T} \left( \prod_{j=k+1}^T \frac{\partial h_j}{\partial h_{j-1}} \right) \frac{\partial h_k}{\partial W_h}
\]
*Interpretation: The product term causes exponential decay/growth of gradients, explaining vanishing/exploding gradients.*

## Exam Tips
1. Always compare computational complexity: RNNs O(T), Transformers O(T²)
2. Draw and label LSTM cell diagram with all gates and data flows
3. Derive gradient equations for RNNs to explain vanishing gradients
4. Implement self-attention from scratch using matrix operations
5. Explain transformer positional encoding using sine/cosine functions
6. Compare encoder-decoder architectures in Seq2Seq vs Transformer
7. Discuss recent improvements like Rotary Position Embeddings (RoPE)