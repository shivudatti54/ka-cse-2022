# Sequence Modeling with RNN - Summary

## Key Definitions and Concepts

- **Sequence Modeling**: The task of predicting or generating sequences where the order of elements matters and current outputs depend on previous inputs.
- **Recurrent Neural Network (RNN)**: A neural network with recurrent connections that maintains hidden state to capture temporal dependencies in sequential data.
- **Hidden State (h_t)**: The internal memory of an RNN at time t that encodes information from previous time steps.
- **Backpropagation Through Time (BPTT)**: Training algorithm for RNNs that unrolls the network through time and propagates gradients backward.
- **Vanishing/Exploding Gradient**: Problem where gradients become extremely small or large when backpropagating through many time steps, preventing learning of long-term dependencies.
- **LSTM (Long Short-Term Memory)**: RNN variant with gating mechanisms (forget, input, output gates) and cell state to preserve long-term information.
- **GRU (Gated Recurrent Unit)**: Simplified LSTM variant with update and reset gates, fewer parameters but comparable performance.

## Important Formulas and Theorems

**Basic RNN Forward Pass:**
- h_t = tanh(W_xh · x_t + W_hh · h_(t-1) + b_h)
- y_t = W_hy · h_t + b_y

**LSTM Gates:**
- f_t = σ(W_f · [h_(t-1), x_t] + b_f) (Forget Gate)
- i_t = σ(W_i · [h_(t-1), x_t] + b_i) (Input Gate)
- o_t = σ(W_o · [h_(t-1), x_t] + b_o) (Output Gate)
- c_t = f_t × c_(t-1) + i_t × C̃_t (Cell State Update)
- h_t = o_t × tanh(c_t) (Hidden State)

**GRU Equations:**
- z_t = σ(W_z · [h_(t-1), x_t]) (Update Gate)
- r_t = σ(W_r · [h_(t-1), x_t]) (Reset Gate)
- h_t = (1 - z_t) × h_(t-1) + z_t × tanh(W · [r_t × h_(t-1), x_t])

## Key Points

- RNNs use weight sharing across time steps, enabling parameter efficiency and handling variable-length sequences.
- The four RNN architectures are: one-to-one, one-to-many, many-to-one, and many-to-many.
- LSTMs solve vanishing gradients through cell state—a "gradient superhighway" that allows information to flow unchanged.
- GRUs have fewer gates (2 vs 3) and parameters than LSTMs, often training faster with comparable performance.
- Bidirectional RNNs process sequences in both directions, useful when context from entire sequence is available.
- Common activations in RNNs: tanh (hidden states, outputs -1 to 1), sigmoid (gates, outputs 0 to 1).
- Applications include machine translation, sentiment analysis, speech recognition, time series forecasting, and video captioning.

## Common Mistakes to Avoid

- Confusing the cell state (c_t) with hidden state (h_t) in LSTMs—they serve different purposes.
- Forgetting that weight matrices are shared across all time steps in RNNs.
- Assuming RNNs can only process fixed-length sequences—they handle variable length through unrolling.
- Mixing up gate functions: sigmoid (0-1 range for gating) vs tanh (-1 to 1 range for transformations).
- Neglecting to initialize hidden states appropriately, especially for bidirectional RNNs.

## Revision Tips

1. Practice deriving forward pass equations for all RNN types (basic RNN, LSTM, GRU) with example inputs.
2. Create a comparison table of basic RNN vs LSTM vs GRU, focusing on gates, parameters, and complexity.
3. Draw the unrolled RNN diagram for a 3-4 timestep sequence to visualize forward and backward pass.
4. Review past DU exam questions on RNNs to understand the question patterns and emphasis areas.
5. Implement small RNNs in NumPy/PyTorch to gain hands-on understanding of the computations.