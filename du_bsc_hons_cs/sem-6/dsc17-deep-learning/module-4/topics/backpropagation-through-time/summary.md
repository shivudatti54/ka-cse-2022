# Backpropagation Through Time (BPTT) - Summary

## Key Definitions and Concepts

- **BPTT (Backpropagation Through Time)**: Training algorithm for RNNs that unrolls the network through time and applies standard backpropagation to the resulting feedforward network.

- **Temporal Unrolling**: Converting an RNN with cyclic connections into an equivalent deep feedforward network by creating copies of the network for each time step.

- **Weight Sharing**: The same weight matrices are used at every time step in the unrolled network, requiring gradient accumulation across all time steps.

- **Truncated BPTT**: A variant that limits backpropagation to a fixed number of time steps for computational efficiency.

## Important Formulas and Theorems

- **Hidden state update**: $h_t = \tanh(W_{xh}x_t + W_{hh}h_{t-1} + b_h)$

- **Total loss**: $L = \sum_{t=1}^{T} L_t$ (sum of losses at each time step)

- **Weight gradient accumulation**: $\frac{\partial L}{\partial W} = \sum_{t=1}^{T} \frac{\partial L_t}{\partial W}$

- **Gradient flow through time**: $\frac{\partial h_t}{\partial h_{t-1}}$ (Jacobian) multiplied repeatedly causes vanishing/exploding gradients

## Key Points

- BPTT unrolls RNNs through time to apply standard backpropagation algorithms.

- Weights are shared across time steps, so gradients must be accumulated (summed) before updates.

- The vanishing gradient problem occurs when $|λ_{max}| < 1$ (Jacobian eigenvalues), preventing learning of long-term dependencies.

- Exploding gradients occur when $|λ_{max}| > 1$, causing numerical instability in training.

- Truncated BPTT limits backward pass to k steps, trading some gradient quality for computational efficiency.

- Full BPTT has $O(T)$ forward pass but $O(T^2)$ backward pass complexity due to gradient propagation through all previous steps.

- LSTMs and GRUs were designed to address BPTT's limitations through gating mechanisms that control gradient flow.

## Common Mistakes to Avoid

- **Averaging instead of summing**: Remember to sum gradients across time steps, not average them.

- **Forgetting weight sharing**: The same weights apply at every time step — this is fundamental to BPTT.

- **Ignoring the Jacobian**: The chain rule through hidden states involves Jacobian matrices, causing the vanishing/exploding gradient problems.

- **Confusing forward and backward complexity**: Forward pass is $O(T)$, but backward pass is $O(T^2)$ for full BPTT.

## Revision Tips

1. Practice deriving gradients by hand for a simple 2-3 time step RNN to build intuition.

2. Draw the unrolled network diagram for different sequence lengths to visualize the architecture.

3. Compare BPTT with standard backprop — understanding the similarities reinforces core concepts.

4. Review how LSTM/GRU gating solves gradient problems — this connects BPTT to modern architectures.

5. Memorize the time complexity trade-offs between full and truncated BPTT.