# LSTM: Long Short-Term Memory - Summary

## Key Definitions and Concepts

- **LSTM (Long Short-Term Memory)**: A specialized RNN architecture introduced by Hochreiter and Schmidhuber (1997) that uses gating mechanisms to learn long-range dependencies in sequential data.

- **Vanishing Gradient Problem**: The phenomenon in standard RNNs where gradients exponentially decay during backpropagation through time, preventing learning of long-term dependencies.

- **Cell State (C_t)**: The "memory" of an LSTM that runs through the entire network, carrying relevant information across time steps with minimal modification.

- **Forget Gate**: Determines what information to discard from the previous cell state (output: 0-1).

- **Input Gate**: Decides what new information to store in the cell state.

- **Output Gate**: Determines what the next hidden state should contain based on cell state and current input.

## Important Formulas and Theorems

- **Forget Gate**: f_t = σ(W_f · [h_{t-1}, x_t] + b_f)
- **Input Gate**: i_t = σ(W_i · [h_{t-1}, x_t] + b_i)
- **Candidate Cell State**: C̃_t = tanh(W_C · [h_{t-1}, x_t] + b_C)
- **Cell State Update**: C_t = f_t × C_{t-1} + i_t × C̃_t
- **Output Gate**: o_t = σ(W_o · [h_{t-1}, x_t] + b_o)
- **Hidden State**: h_t = o_t × tanh(C_t)

## Key Points

- LSTMs solve the vanishing gradient problem through constant error carousel in the cell state
- The gating mechanism (sigmoid + multiplication) allows selective information retention
- Sigmoid outputs (0-1) represent information flow magnitude; tanh (-1 to 1) represents content values
- Cell state acts as a information highway with minimal linear transformation
- Bidirectional LSTMs process sequences in both directions for complete context
- GRU is a simplified variant with fewer parameters but comparable performance

## Common Mistakes to Avoid

- Confusing the roles of different gates (forget vs input vs output)
- Assuming LSTM completely eliminates vanishing gradients (it only mitigates them)
- Forgetting that gates use sigmoid while state updates use tanh
- Not understanding that [h_{t-1}, x_t] denotes concatenation, not addition

## Revision Tips

1. Practice drawing the LSTM architecture diagram from memory, labeling all gates and connections
2. Work through at least one complete forward pass calculation by hand
3. Compare LSTM with standard RNN to solidify understanding of the problem it solves
4. Review the mathematical equations until you can write them without looking
5. Think of real-world examples where long-term dependency matters (translation, prediction)