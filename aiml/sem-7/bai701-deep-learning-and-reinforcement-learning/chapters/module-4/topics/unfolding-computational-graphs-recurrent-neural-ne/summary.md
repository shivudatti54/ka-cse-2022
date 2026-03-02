# **Unfolding Computational Graphs, Recurrent Neural Networks, and Beyond**

### Unfolding Computational Graphs

- **Definition:** Unfolding a computational graph involves recursively applying the same computation to a sequence of inputs.
- **Important Formula:**
  $f(x_t, h_{t-1}) = \sum_{i=1}^{N} w_{i} \cdot f_i(x_t, h_{t-1}) + b$
- **Key Points:**
  - Uses recurrent connections to maintain hidden state
  - Can be applied to any feedforward network

### Recurrent Neural Networks (RNNs)

- **Definition:** A RNN is a type of neural network that maintains a hidden state over time.
- **Types:**
  - Simple RNN: uses the same weight matrix for all time steps
  - Long Short-Term Memory (LSTM): uses memory cells to handle long-term dependencies
- **Important Formula:**
  $h_t = \sigma(W \cdot h_{t-1} + U \cdot x_t + b)$
- **Key Points:**
  - Uses feedback connections to maintain hidden state
  - Can learn long-term dependencies

### Bidirectional RNNs

- **Definition:** A bidirectional RNN processes input sequences in both forward and backward directions.
- **Types:**
  - Bidirectional Simple RNN
  - Bidirectional LSTM
- **Important Formula:**
  $h_t = \sigma(W_f \cdot h_{t-1} + W_o \cdot o_t + b_f)$
- **Key Points:**
  - Can capture both past and future dependencies
  - Often used for sequence classification tasks

### Deep Recurrent Networks

- **Definition:** A deep RNN is a type of RNN that uses multiple hidden layers to capture complex dependencies.
- **Types:**
  - Deep Simple RNN
  - Deep LSTM
- **Important Formula:**
  $h_t = \sigma(W \cdot h_{t-1} + U \cdot x_t + b)$
- **Key Points:**
  - Can capture long-term dependencies and hierarchies
  - Often used for sequence generation tasks

### Recursive Neural Networks

- **Definition:** A recursive neural network is a type of RNN that uses recursive functions to define the network architecture.
- **Types:**
  - Recursive Simple RNN
  - Recursive LSTM
- **Important Formula:**
  $h_t = f(h_{t-1}, x_t)$
- **Key Points:**
  - Can be more flexible than traditional RNNs
  - Often used for tasks that require recursive reasoning

### The Long Short-Term Memory (LSTM) Mechanism

- **Definition:** An LSTM is a type of RNN that uses memory cells to handle long-term dependencies.
- **Types:**
  - Basic LSTM
  - Gated LSTM
- **Important Formula:**
  $c_t = \sigma(W_c \cdot h_{t-1} + U_c \cdot x_t + b_c)$
- **Key Points:**
  - Can handle long-term dependencies and vanishing gradients
  - Often used for tasks that require long-term memory
