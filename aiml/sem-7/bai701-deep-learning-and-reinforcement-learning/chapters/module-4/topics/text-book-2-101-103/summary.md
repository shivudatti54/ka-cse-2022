# **Text Book – 2: 10.1-10.3 Revision Notes**

### Introduction to Recurrent Neural Networks (RNNs)

- **Definition:** A type of neural network that uses feedback connections to maintain internal state and generate outputs based on input sequences.
- **Key Features:**
  - Feedback connections
  - Internal state (hidden states)
  - Gradient descent optimization

### Types of RNNs

- **Simple RNN (SRNN):** Uses a single internal state to process input sequences.
- **Long Short-Term Memory (LSTM) Networks:** A type of RNN that uses memory cells to selectively retain information over long periods.
- **Gated Recurrent Units (GRUs):** A type of RNN that uses gates to control the flow of information between the input gate, output gate, and memory cell.

### Mathematical Formulas

- **SRNN:**
  - Input: `x_t`
  - Hidden state: `h_t`
  - Output: `y_t`
  - Update rule: `h_t = sigmoid(w \* (h_{t-1} + b) + u \* x_t)`
- **LSTM Network:**
  - Input: `x_t`
  - Memory cell: `C_t`
  - Hidden state: `h_t`
  - Output: `y_t`
  - Update rules:
    - `I_t = sigmoid(w_i \* (h_{t-1} + b_i) + u_i \* x_t)`
    - `F_t = sigmoid(w_f \* (h_{t-1} + b_f) + u_f \* x_t)`
    - `C_t = sigmoid(w_c \* (h_{t-1} + b_c) + u_c \* x_t)`
    - `h_t = sigmoid(w_h \* (h_{t-1} + b_h) + u_h \* x_t)`
- **GRU Network:**
  - Input: `x_t`
  - Hidden state: `h_t`
  - Output: `y_t`
  - Update rules:
    - `z_t = sigmoid(w_z \* (h_{t-1} + b_z) + u_z \* x_t)`
    - `r_t = sigmoid(w_r \* (h_{t-1} + b_r) + u_r \* x_t)`
    - `u_t = sigmoid(w_u \* (h_{t-1} + b_u) + u_u \* x_t)`
    - `h_t = r_t \* tanh(w_h \* (h_{t-1} + b_h) + u_h \* x_t)`

### Important Theorems

- **The Chain Rule:** Used to compute the gradients of the loss function with respect to the model parameters.
- **The Backpropagation Algorithm:** Used to compute the gradients of the loss function with respect to the model parameters.

### References

- Hochreiter, S., & Schmidhuber, J. (1997). Long short-term memory. Neural Computing, 9(8), 1735-1780.
