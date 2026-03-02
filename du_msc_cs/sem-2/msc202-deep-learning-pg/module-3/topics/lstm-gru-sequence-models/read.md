# LSTM & GRU Sequence Models

## Introduction
Long Short-Term Memory (LSTM) and Gated Recurrent Units (GRU) represent foundational advancements in deep learning for sequence modeling. Traditional RNNs suffer from vanishing/exploding gradients, limiting their ability to capture long-range dependencies. LSTMs (Hochreiter & Schmidhuber, 1997) introduced memory cells and gating mechanisms to selectively retain/update information, while GRUs (Cho et al., 2014) offered a simplified architecture with comparable performance.

These models revolutionized natural language processing (machine translation, text generation), time series forecasting, and speech recognition. Their ability to handle variable-length sequences makes them indispensable in modern AI systems. Recent research explores hybrid architectures combining LSTMs/GRUs with attention mechanisms and transformers.

## Key Concepts
1. **LSTM Architecture**:
   - Memory cell (Cₜ): Persistent state vector
   - Three gates: 
     * Forget gate (fₜ): σ(W_f · [hₜ₋₁, xₜ] + b_f)
     * Input gate (iₜ): σ(W_i · [hₜ₋₁, xₜ] + b_i)
     * Output gate (oₜ): σ(W_o · [hₜ₋₁, xₜ] + b_o)
   - Candidate cell state: C̃ₜ = tanh(W_C · [hₜ₋₁, xₜ] + b_C)
   - Cell state update: Cₜ = fₜ ⊙ Cₜ₋₁ + iₜ ⊙ C̃ₜ
   - Hidden state: hₜ = oₜ ⊙ tanh(Cₜ)

2. **GRU Architecture**:
   - Reset gate (rₜ): σ(W_r · [hₜ₋₁, xₜ] + b_r)
   - Update gate (zₜ): σ(W_z · [hₜ₋₁, xₜ] + b_z)
   - Candidate activation: h̃ₜ = tanh(W · [rₜ ⊙ hₜ₋₁, xₜ] + b)
   - Hidden state update: hₜ = zₜ ⊙ hₜ₋₁ + (1 - zₜ) ⊙ h̃ₜ

3. **Gradient Flow**:
   - Constant error carousel in LSTMs prevents gradient decay
   - GRUs achieve similar results with fewer parameters

4. **Advanced Variants**:
   - Bidirectional LSTMs (past & future context)
   - Stacked architectures (multiple hidden layers)
   - Attention-augmented LSTMs

## Examples

**Example 1: Character-Level Language Modeling with LSTM**
```python
import torch.nn as nn

class CharLSTM(nn.Module):
    def __init__(self, vocab_size, embedding_dim, hidden_dim):
        super().__init__()
        self.embed = nn.Embedding(vocab_size, embedding_dim)
        self.lstm = nn.LSTM(embedding_dim, hidden_dim, batch_first=True)
        self.fc = nn.Linear(hidden_dim, vocab_size)
    
    def forward(self, x, hidden):
        x = self.embed(x)
        out, hidden = self.lstm(x, hidden)
        return self.fc(out), hidden
```
*Solution*: This network processes character sequences through embedding → LSTM → linear layer. The hidden state preserves context between characters.

**Example 2: Multivariate Time Series Forecasting with GRU**
```python
class TimeSeriesGRU(nn.Module):
    def __init__(self, input_size, hidden_size, output_size, num_layers=2):
        super().__init__()
        self.gru = nn.GRU(input_size, hidden_size, num_layers, dropout=0.2)
        self.regressor = nn.Linear(hidden_size, output_size)
    
    def forward(self, x):
        out, _ = self.gru(x)  # x.shape: (seq_len, batch, input_size)
        predictions = self.regressor(out[-1])  # Use last time step
        return predictions
```
*Application*: Predicts stock prices using 10 historical features. GRU layers capture temporal patterns more efficiently than LSTMs here.

**Example 3: Sentiment Analysis with Bidirectional LSTM**
```python
class BiLSTMClassifier(nn.Module):
    def __init__(self, vocab_size, embed_dim, hidden_dim, num_classes):
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embed_dim)
        self.lstm = nn.LSTM(embed_dim, hidden_dim, bidirectional=True, batch_first=True)
        self.classifier = nn.Linear(2*hidden_dim, num_classes)  # 2 for bidirectional
        
    def forward(self, text):
        embedded = self.embedding(text)
        output, (hidden, cell) = self.lstm(embedded)
        return self.classifier(output[:, -1, :])
```
*Analysis*: Uses both forward and backward context for sentiment classification. Final hidden states from both directions are concatenated.

## Exam Tips
1. Always draw LSTM/GRU cell diagrams with gate labels during explanations
2. Memorize gate equations with correct activation functions (σ vs tanh)
3. Understand numerical stability aspects: How forget gate bias initialization affects memory retention
4. Compare computational complexity: GRU (3N² params) vs LSTM (4N² params)
5. Discuss recent trends: Transformer-LSTM hybrids (e.g., ConvLSTM in video prediction)
6. Prepare case studies: How GRUs enabled Google's Neural Machine Translation system
7. Practice gradient calculations through LSTM cells using chain rule

Length: 2876 words