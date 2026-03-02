# Sequence Modeling with Recurrent Neural Networks (RNN)

## Introduction

Sequence modeling represents one of the most fundamental challenges in modern machine learning, where the goal is to predict or generate sequences of data points that are interdependent. Unlike traditional feedforward neural networks that assume input-output independence, sequence models must capture temporal dependencies where the current output depends not only on the current input but also on previous inputs in the sequence. This capability is essential for numerous real-world applications including natural language processing (NLP), speech recognition, time series forecasting, music generation, and video analysis.

Recurrent Neural Networks (RNNs) were introduced specifically to handle sequential data by introducing the concept of hidden state that maintains information about previous time steps. The key innovation of RNNs is the presence of recurrent connections that allow information to persist across time steps, creating a form of internal memory. This architectural choice makes RNNs uniquely suited for tasks where context from earlier in the sequence is crucial for understanding or predicting subsequent elements.

In the context of the University of Delhi's Computer Science curriculum, understanding RNNs is essential for students aiming to work in AI/ML domains. The University of Delhi, through its NEP 2024 curriculum, emphasizes practical and theoretical knowledge of deep learning architectures. This topic forms the foundation for understanding more advanced sequence models like Long Short-Term Memory (LSTM) and Gated Recurrent Units (GRU), which are extensively used in industry applications such as chatbots, language translation systems, and voice assistants.

## Key Concepts

### Architecture of Basic RNN

The fundamental RNN architecture consists of three main components: an input layer (x_t), a hidden layer (h_t), and an output layer (y_t). At each time step t, the RNN receives an input vector x_t and the previous hidden state h_(t-1). The current hidden state h_t is computed using an activation function (typically tanh or ReLU) applied to the weighted sum of the previous hidden state and current input:

**h_t = tanh(W_{xh} · x_t + W_{hh} · h_(t-1) + b_h)**

The output y_t is then computed from the hidden state:

**y_t = W_{hy} · h_t + b_y**

Where W_{xh}, W_{hh}, and W_{hy} are weight matrices, and b_h, b_y are bias vectors. The same weight matrices are shared across all time steps, which is a key characteristic of RNNs that makes them parameter-efficient and allows them to handle variable-length sequences.

### Forward Propagation in RNN

The forward pass through an RNN unfolds the network through time. For a sequence of length T, the process proceeds sequentially:

At time step 1: The initial hidden state h_0 is typically initialized to zeros or learned. The first hidden state h_1 is computed using x_1 and h_0.
At time step 2: Using x_2 and h_1, we compute h_2.
This process continues for all T time steps. The final output can be taken from the last time step (for many-to-one tasks like sentiment classification) or from every time step (for many-to-many tasks like part-of-speech tagging).

### Backpropagation Through Time (BPTT)

Training RNNs requires a variant of backpropagation called Backpropagation Through Time (BPTT). The process involves:
1. Unrolling the RNN through all time steps
2. Computing the loss at each time step (for sequence tasks) or at the final step
3. Propagating gradients backward through each time step
4. Accumulating gradients and updating weights using gradient descent

The gradient at time step t depends on all previous time steps, which is why BPTT can be computationally expensive for long sequences.

### Vanishing and Exploding Gradient Problem

One of the most significant challenges in training basic RNNs is the vanishing and exploding gradient problem. When backpropagating through many time steps, the gradients can either become extremely small (vanishing) or extremely large (exploding).

For a basic RNN with weight matrix W and activation function, the gradient involves repeated multiplication of W. If the largest eigenvalue of W is less than 1, gradients shrink exponentially (vanishing gradient), making it impossible to learn long-term dependencies. If eigenvalues exceed 1, gradients grow exponentially (exploding gradient), causing training instability.

Mathematically, the gradient contribution from time step t-k to the weight update at time step involves terms like (W^T)^k. When k is large and spectral radius of W < 1, this term approaches zero; when > 1, it grows without bound.

### Long Short-Term Memory (LSTM)

LSTMs were introduced by Hochreiter and Schmidhuber in 1997 to address the vanishing gradient problem. LSTMs introduce a cell state (c_t) that acts as a information highway, allowing long-term dependencies to be learned more effectively.

The key components of an LSTM are:

**Forget Gate (f_t):** Determines what information to discard from the cell state
**f_t = σ(W_f · [h_(t-1), x_t] + b_f)**

**Input Gate (i_t):** Determines what new information to store in the cell state
**i_t = σ(W_i · [h_(t-1), x_t] + b_i)**

**Candidate Value (C̃_t):** Creates new candidate values to add to the cell state
**C̃_t = tanh(W_C · [h_(t-1), x_t] + b_C)**

**Cell State Update:**
**c_t = f_t * c_(t-1) + i_t * C̃_t**

**Output Gate (o_t):** Determines what to output
**o_t = σ(W_o · [h_(t-1), x_t] + b_o)**

**Hidden State:**
**h_t = o_t * tanh(c_t)**

The sigmoid function σ outputs values between 0 and 1, representing how much of each component passes through.

### Gated Recurrent Unit (GRU)

GRUs, introduced in 2014, are a simplified variant of LSTMs that combine the forget and input gates into a single update gate and merge the cell state and hidden state. GRUs have two gates:

**Update Gate (z_t):** Controls how much past information to carry forward
**z_t = σ(W_z · [h_(t-1), x_t])**

**Reset Gate (r_t):** Controls how much past information to forget
**r_t = σ(W_r · [h_(t-1), x_t])**

**Candidate Hidden State:**
**h̃_t = tanh(W · [r_t * h_(t-1), x_t])**

**Hidden State Update:**
**h_t = (1 - z_t) * h_(t-1) + z_t * h̃_t**

GRUs often perform comparably to LSTMs while being computationally more efficient.

## Examples

### Example 1: Forward Pass Computation in Basic RNN

Consider a simple RNN with the following configuration:
- Input dimension: 3
- Hidden dimension: 2  
- Sequence length: 2
- Weights: W_xh = [[1, 0], [0, 1], [1, 1]], W_hh = [[0.5, 0.1], [0.1, 0.5]], W_hy = [[1, 0], [0, 1]]
- Bias: b_h = [0, 0], b_y = [0, 0]
- Activation: tanh, Output activation: identity
- Input sequence: x_1 = [1, 0, 1], x_2 = [0, 1, 0]
- Initial hidden state: h_0 = [0, 0]

**Step 1: Compute h_1**
h_1_raw = W_xh · x_1 + W_hh · h_0 + b_h
= [[1, 0], [0, 1], [1, 1]] · [1, 0, 1] + [[0.5, 0.1], [0.1, 0.5]] · [0, 0]
= [1×1 + 0×0 + 1×1, 0×1 + 1×0 + 1×1] + [0, 0]
= [2, 1]

h_1 = tanh([2, 1]) = [tanh(2), tanh(1)] ≈ [0.964, 0.762]

**Step 2: Compute h_2**
h_2_raw = W_xh · x_2 + W_hh · h_1 + b_h
= [[1, 0], [0, 1], [1, 1]] · [0, 1, 0] + [[0.5, 0.1], [0.1, 0.5]] · [0.964, 0.762]
= [0×1 + 0×1 + 1×0, 0×1 + 1×1 + 1×0] + [0.5×0.964 + 0.1×0.762, 0.1×0.964 + 0.5×0.762]
= [0, 1] + [0.554, 0.482]
= [0.554, 1.482]

h_2 = tanh([0.554, 1.482]) ≈ [0.504, 0.905]

**Step 3: Compute outputs**
y_1 = W_hy · h_1 + b_y = [[1, 0], [0, 1]] · [0.964, 0.762] = [0.964, 0.762]
y_2 = W_hy · h_2 + b_y = [[1, 0], [0, 1]] · [0.504, 0.905] = [0.504, 0.905]

### Example 2: LSTM Gate Calculations

Consider an LSTM with single-unit gates for simplicity:
- All weight matrices are 1×1 with value 1
- All biases are 0
- Input: x_t = 1, Previous hidden state: h_(t-1) = 0.5, Previous cell state: c_(t-1) = 0.3

**Forget Gate:**
f_t = σ(W_f · [h_(t-1), x_t] + b_f) = σ(1×0.5 + 1×1 + 0) = σ(1.5) ≈ 0.818

**Input Gate:**
i_t = σ(W_i · [h_(t-1), x_t] + b_i) = σ(1×0.5 + 1×1 + 0) = σ(1.5) ≈ 0.818

**Candidate Cell State:**
C̃_t = tanh(W_C · [h_(t-1), x_t] + b_C) = tanh(0.5 + 1) = tanh(1.5) ≈ 0.905

**Cell State Update:**
c_t = f_t × c_(t-1) + i_t × C̃_t
= 0.818 × 0.3 + 0.818 × 0.905
= 0.245 + 0.740 = 0.985

**Output Gate:**
o_t = σ(W_o · [h_(t-1), x_t] + b_o) = σ(1.5) ≈ 0.818

**Hidden State:**
h_t = o_t × tanh(c_t) = 0.818 × tanh(0.985) = 0.818 × 0.831 ≈ 0.680

### Example 3: Sentiment Classification Using RNN

For a movie review "This movie is excellent" being classified as positive:
- Tokenize: ["This", "movie", "is", "excellent"]
- Embed each word into a 100-dimensional vector
- Process sequentially through RNN
- Final hidden state h_4 captures information from all words
- Pass h_4 through a softmax layer for binary classification

If the final hidden vector h_4 = [0.8, -0.3] after training, the output layer would compute:
scores = W_hy · h_4 = [positive_score, negative_score]
Apply softmax to get probabilities. The class with higher probability is the prediction.

## Exam Tips

1. **Understand the difference between RNN variants**: Know when to use basic RNN, LSTM, and GRU. Basic RNNs are suitable for short-term dependencies; LSTMs for long-term dependencies with complex patterns; GRUs when computational efficiency is important.

2. **Memorize the equations**: For exams, be prepared to write out the forward propagation equations for basic RNN, LSTM gates, and GRU gates. Understanding the dimensions of weight matrices is crucial.

3. **Gradient problem explanation**: Be able to explain why vanishing/exploding gradients occur in basic RNNs and how LSTM/GRU gates address this issue. The key insight is the cell state (in LSTM) or the update mechanism (in GRU) that provides a direct path for gradient flow.

4. **Different RNN architectures**: Know the four types: one-to-one (image classification), one-to-many (image captioning), many-to-one (sentiment analysis), and many-to-many (machine translation, POS tagging).

5. **BPTT conceptual understanding**: You don't need to compute full BPTT by hand for long sequences, but understand its concept—unrolling through time and propagating gradients backward.

6. **Weight sharing advantage**: Emphasize that RNNs use the same weights at every time step, which enables handling variable-length sequences and reduces the number of parameters.

7. **Comparison with CNN**: RNNs are designed for sequential data with variable length, while CNNs are for grid-like data (images). This distinction frequently appears in exam questions.