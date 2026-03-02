# LSTM & GRU Sequence Models - Summary

## Key Definitions and Concepts
- **LSTM**: Gated RNN variant with input, forget, output gates and cell state
- **GRU**: Simplified gated unit with reset and update gates
- **Vanishing Gradient**: Problem addressed by constant error carousel in LSTMs
- **Bidirectional RNN**: Processes sequence in both directions

## Important Formulas and Theorems
- LSTM Forget Gate: fₜ = σ(W_f · [hₜ₋₁, xₜ] + b_f)
- GRU Update Gate: zₜ = σ(W_z · [hₜ₋₁, xₜ] + b_z)
- Cell State Update: Cₜ = fₜ ⊙ Cₜ₋₁ + iₜ ⊙ C̃ₜ
- GRU Candidate Activation: h̃ₜ = tanh(W·[rₜ⊙hₜ₋₁, xₜ] + b)

## Key Points
- LSTMs maintain separate cell state and hidden state
- GRUs merge cell and hidden states for parameter efficiency
- Both architectures enable learning long-term dependencies (>1000 steps)
- Bidirectional variants capture past and future context
- Modern implementations use cuDNN-optimized kernels for speed
- Attention mechanisms often augment LSTMs/GRUs in state-of-the-art systems
- Initialization of forget gate bias critical for stable training

## Common Mistakes to Avoid
- Confusing input/output gate roles in LSTMs
- Using tanh instead of sigmoid for gate activations
- Neglecting gradient clipping in very deep recurrent nets
- Overlooking sequence padding in variable-length inputs

## Revision Tips
1. Create comparative tables: LSTM vs GRU vs vanilla RNN
2. Practice deriving gradients through LSTM cells
3. Study seminal papers: Hochreiter & Schmidhuber (1997), Cho et al. (2014)
4. Experiment with torch.nn.LSTMCell and GRUCell implementations

Length: 672 words