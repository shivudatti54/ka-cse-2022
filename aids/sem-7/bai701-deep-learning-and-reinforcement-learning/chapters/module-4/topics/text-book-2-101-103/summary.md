### Revision Notes: 10.1-10.3 - Recurrent and Recursive Neural Networks

#### Overview

- Recurrent Neural Networks (RNNs) and Recursive Neural Networks (RNNs) are designed to handle sequential data.
- RNNs process input sequences one time step at a time, using previous information to inform current output.

#### Key Concepts

- **Recurrent Neural Networks (RNNs)**:
  - Define a feedback loop between time steps
  - Use gates (e.g., input gate, output gate, forget gate) to control information flow
  - Formula: `h_t = f(h_{t-1}, x_t, c_t)`
- **Recursive Neural Networks (RNNs)**:
  - Similar to RNNs, but with a recursive structure
  - Can be implemented using RNNs or other architectures (e.g., LSTMs)
- **Types of RNNs**:
  - Simple RNNs
  - Long Short-Term Memory (LSTM) networks
  - Gated Recurrent Unit (GRU) networks

#### Important Formulas and Definitions

- **Activation Functions**:
  - ReLU (Rectified Linear Unit)
  - Sigmoid
  - Tanh
- **Loss Functions**:
  - Mean Squared Error (MSE)
  - Cross-Entropy Loss
- **Optimization Algorithms**:
  - Stochastic Gradient Descent (SGD)
  - Adam
  - RMSProp

#### Theorems and Properties

- **Vanishing Gradient Problem**: a common issue in RNNs where gradients are lost over time
- **Exploding Gradient Problem**: a common issue in RNNs where gradients become unbounded
- **Equivalence theorem**: states that RNNs and LSTMs can be equivalent under certain conditions
