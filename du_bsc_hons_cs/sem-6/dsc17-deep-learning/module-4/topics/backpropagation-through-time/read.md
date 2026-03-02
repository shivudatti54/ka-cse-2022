# Backpropagation Through Time (BPTT)

## Introduction

Backpropagation Through Time (BPTT) is the fundamental algorithm used to train Recurrent Neural Networks (RNNs), enabling them to learn from sequential data. Unlike feedforward neural networks where information flows in one direction, RNNs have cyclic connections that allow them to maintain memory of previous inputs. This recurrent nature presents a unique challenge: how do we compute gradients through time to update network parameters? BPTT solves this problem by "unrolling" the RNN through time, transforming the recurrent computation into an equivalent feedforward structure, and then applying the standard backpropagation algorithm.

The importance of BPTT in modern deep learning cannot be overstated. It forms the backbone of language models, time-series prediction, speech recognition, and many other applications where understanding sequential dependencies is crucial. In the University of Delhi's BSc (H) Computer Science program, understanding BPTT is essential for grasping how modern sequence models work, including the more advanced variants like LSTMs and GRUs that were developed to address BPTT's limitations.

## Key Concepts

### The Unrolling Process

The core idea behind BPTT is temporal unrolling. Consider an RNN with a single hidden state that recurs at each time step. To apply backpropagation, we conceptually "unroll" the network across all time steps, creating a feedforward network where each time step becomes a separate layer. For an RNN with hidden state $h_t$ at time $t$, updated as $h_t = \tanh(W_{xh}x_t + W_{hh}h_{t-1} + b_h)$, the unrolled network contains one copy of the network for each time step, with all copies sharing the same weight matrices $W_{xh}$, $W_{hh}$, and bias $b_h$.

This unrolling transforms the sequential problem into a deep feedforward network where the depth equals the sequence length. The shared weights mean that gradients computed at each time step must be accumulated and summed to update the parameters once.

### Forward Pass in Unrolled Network

During the forward pass through the unrolled RNN, information flows from the initial hidden state $h_0$ through each time step sequentially. At each time step $t$, the hidden state $h_t$ is computed using the current input $x_t$ and the previous hidden state $h_{t-1}$. The output at each time step (if applicable) is computed from the hidden state. The total loss is typically the sum of losses at each time step: $L = \sum_{t=1}^{T} L_t$, where $L_t$ is the loss at time step $t$.

### Computing Gradients Through Time

The backward pass in BPTT propagates the error gradient backwards through the unrolled network. Starting from the final time step, we compute $\frac{\partial L}{\partial h_t}$ and then use the chain rule to compute gradients with respect to weights at each time step. The key gradient computations involve:

For the weight $W_{hh}$ (hidden-to-hidden):
$$\frac{\partial L}{\partial W_{hh}} = \sum_{t=1}^{T} \frac{\partial L}{\partial h_t} \frac{\partial h_t}{\partial W_{hh}}$$

The challenge arises because $\frac{\partial h_t}{\partial h_{t-1}}$ involves the Jacobian matrix, and when we backpropagate through many time steps, we multiply these Jacobians repeatedly. This leads to the vanishing or exploding gradient problem.

### Vanishing and Exploding Gradients

When backpropagating through many time steps, the repeated multiplication of Jacobian matrices causes gradient magnitudes to either shrink exponentially (vanishing gradients) or grow exponentially (exploding gradients). Vanishing gradients prevent the network from learning long-term dependencies, as early time steps receive negligible gradient updates. Exploding gradients cause numerical instability and gradient descent divergence.

Mathematically, if the largest eigenvalue of the Jacobian $\frac{\partial h_t}{\partial h_{t-1}}$ is greater than 1, gradients explode; if less than 1, they vanish. This is why standard RNNs struggle with long sequences, and why LSTM and GRU architectures were developed with gating mechanisms to control gradient flow.

### Truncated BPTT

For very long sequences, full BPTT becomes computationally expensive and memory-intensive. Truncated BPTT (TBPTT) addresses this by limiting backpropagation to a fixed number of time steps (e.g., $k$ steps). The forward pass still processes the entire sequence, but the backward pass only computes gradients for the last $k$ time steps. This provides a practical compromise between computational efficiency and the ability to learn long-term dependencies.

### BPTT Algorithm Steps

The complete BPTT algorithm proceeds as follows:

1. **Forward Pass**: Process the entire input sequence through time, computing hidden states and outputs at each time step. Store all intermediate values for use in backward pass.

2. **Compute Output Loss**: Calculate the loss at each time step and sum them to get total loss $L$.

3. **Backward Pass**: Initialize gradient accumulators to zero. For $t$ from $T$ down to 1:
   - Compute gradient of loss with respect to hidden state: $\frac{\partial L_t}{\partial h_t}$
   - Backpropagate through the output layer if present
   - Compute gradients with respect to $W_{xh}$, $W_{hh}$, and $b_h$ using chain rule
   - Propagate gradient to previous time step: $\frac{\partial L}{\partial h_{t-1}} = \frac{\partial L}{\partial h_t} \cdot \frac{\partial h_t}{\partial h_{t-1}}$

4. **Gradient Accumulation**: Sum gradients across all time steps for each weight matrix (since weights are shared).

5. **Weight Update**: Apply gradient descent using accumulated gradients.

## Examples

### Example 1: Simple RNN Forward and Backward Pass

Consider a simple RNN with single hidden unit (scalar values) processing a 3-time-step sequence. Let weights be $W_{xh} = 0.5$, $W_{hh} = 0.3$, $b_h = 0.1$, and output weight $W_{hy} = 1.0$. Initial hidden state $h_0 = 0$. Input sequence: $x = [1, 0.5, 0.25]$. Target output at final step: $y_{target} = 1$.

**Forward Pass:**
- $h_1 = \tanh(0.5 \times 1 + 0.3 \times 0 + 0.1) = \tanh(0.6) \approx 0.537$
- $h_2 = \tanh(0.5 \times 0.5 + 0.3 \times 0.537 + 0.1) = \tanh(0.461) \approx 0.441$
- $h_3 = \tanh(0.5 \times 0.25 + 0.3 \times 0.441 + 0.1) = \tanh(0.357) \approx 0.344$
- Output $y = W_{hy} \times h_3 = 0.344$
- Loss $L = 0.5 \times (1 - 0.344)^2 = 0.5 \times 0.430 = 0.215$

**Backward Pass (simplified):**
- $\frac{\partial L}{\partial y} = -(1 - 0.344) = 0.656$
- $\frac{\partial L}{\partial h_3} = \frac{\partial L}{\partial y} \times W_{hy} \times (1 - h_3^2) = 0.656 \times 1 \times (1 - 0.118) = 0.579$
- $\frac{\partial L}{\partial h_2}$ (through $h_3$): $0.579 \times 0.3 \times (1 - 0.441^2) = 0.579 \times 0.3 \times 0.805 = 0.140$
- Continue backpropagation to compute weight gradients

### Example 2: Gradient Flow Analysis

For a simple RNN without nonlinearity ($h_t = W_{hh}h_{t-1} + x_tW_{xh}$), demonstrate vanishing gradients:

Let $W_{hh} = 0.5$, sequence length $T = 10$. The gradient backpropagated to time step 0 is:
$$\frac{\partial h_T}{\partial h_0} = (W_{hh})^{T-1} = (0.5)^9 = 0.002$$

This shows gradients shrink exponentially — after just 10 time steps, the gradient has become less than 0.2% of its original value, making it impossible to learn dependencies spanning more than a few time steps.

### Example 3: Truncated BPTT Practical Implementation

Suppose we have a sequence of length 100 and use TBPTT with truncation length $k=20$:

1. Process first 20 inputs, compute hidden states
2. Compute loss at step 20
3. Backpropagate gradients only 20 steps back
4. Reset hidden state (or keep it), process next 20 inputs
5. Repeat 5 times for full sequence

This reduces computational complexity from $O(T^2)$ to $O(T \times k)$ in terms of backward pass operations.

## Exam Tips

1. **Understand the unrolling concept**: Know that BPTT converts recurrent computation into a feedforward structure through time, and that weights are shared across all time steps.

2. **Gradient computation formula**: Memorize the key gradient formula for BPTT — gradients at each time step accumulate and are summed to get weight updates.

3. **Vanishing/exploding gradients**: Be prepared to explain why this occurs (repeated Jacobian multiplication) and its consequences (inability to learn long-term dependencies).

4. **Relationship with standard backpropagation**: BPTT is essentially standard backpropagation applied to an unrolled network — understand this fundamental connection.

5. **Truncated BPTT**: Know when and why it's used — for computational efficiency with long sequences.

6. **Shared weights**: Remember that since the same weights are used at every time step, gradients from all time steps must be summed (not averaged) before updating.

7. **Difference from standard backprop**: Unlike standard backprop in feedforward networks, BPTT must handle the temporal aspect and the dependence of each step on previous steps through the hidden state.