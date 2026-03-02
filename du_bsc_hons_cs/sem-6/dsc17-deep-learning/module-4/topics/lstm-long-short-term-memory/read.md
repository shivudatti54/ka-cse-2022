# LSTM: Long Short-Term Memory Networks

## Introduction

Recurrent Neural Networks (RNNs) were designed to handle sequential data by maintaining memory of previous inputs through hidden states. However, standard RNNs suffer from a critical limitation known as the **vanishing gradient problem**. When training RNNs over long sequences, gradients propagated back through time tend to become extremely small, effectively preventing the network from learning long-range dependencies. This limitation made standard RNNs unsuitable for tasks requiring understanding of context spanning many time steps, such as machine translation, speech recognition, and time series forecasting.

Long Short-Term Memory (LSTM) networks, introduced by Hochreiter and Schmidhuber in 1997, revolutionized sequence modeling by introducing a sophisticated gating mechanism that allows the network to learn what information to store, forget, and retrieve. LSTMs maintain a **cell state** - a conveyor belt running through the entire network that carries relevant information across time steps with minimal modification. This architecture enables LSTMs to effectively learn dependencies across hundreds or even thousands of time steps, making them one of the most successful deep learning architectures for sequential data.

In the context of DU's Computer Science curriculum, understanding LSTM is essential for students pursuing careers in natural language processing, speech recognition, and time series analysis. Major tech companies like Google, Amazon, and Apple extensively use LSTMs in their AI products, from voice assistants to language translation services.

## Key Concepts

### The Vanishing Gradient Problem in RNNs

In standard RNNs, the hidden state at time t is computed as: h_t = tanh(W * h_{t-1} + U * x_t). During backpropagation through time (BPTT), the gradient contains terms multiplied repeatedly by weight matrices. When eigenvalues are less than 1, gradients exponentially decay; when greater than 1, they explode. This makes it impossible for the network to learn dependencies between distant time steps.

### LSTM Architecture

An LSTM cell consists of three main components:

1. **Cell State (C_t)**: The "memory" of the network, running from cell C_{t-1} to C_t with minimal linear interactions. Information can be added to or removed from the cell state through structures called gates.

2. **Gates**: Specialized neural network layers that control information flow:
   - **Forget Gate**: Decides what information to discard from the cell state
   - **Input Gate**: Decides what new information to store in the cell state
   - **Output Gate**: Decides what to output based on the cell state and current input

### The Forget Gate

The forget gate determines what information to discard from the previous cell state. It takes the previous hidden state h_{t-1} and current input x_t, passes them through a sigmoid layer, and outputs values between 0 and 1:

**f_t = σ(W_f · [h_{t-1}, x_t] + b_f)**

A value of 1 means "keep all information," while 0 means "discard completely."

### The Input Gate

The input gate decides what new information to add to the cell state. It has two parts:
- A sigmoid layer (i_t) decides which values we'll update
- A tanh layer creates a candidate vector of new values

**i_t = σ(W_i · [h_{t-1}, x_t] + b_i)**
**C̃_t = tanh(W_C · [h_{t-1}, x_t] + b_C)**

### Updating the Cell State

The old cell state C_{t-1} is updated to C_t by:
- Multiplying old state by forget gate (dropping information we decided to forget)
- Adding i_t * C̃_t (new candidate values scaled by how much we want to update each state value)

**C_t = f_t * C_{t-1} + i_t * C̃_t**

### The Output Gate

The output gate determines what the next hidden state should contain:
- A sigmoid layer decides what parts of the cell state to output
- The cell state is passed through tanh and multiplied by the sigmoid output

**o_t = σ(W_o · [h_{t-1}, x_t] + b_o)**
**h_t = o_t * tanh(C_t)**

### Variants of LSTM

Several variants of the standard LSTM exist:

1. **Peephole Connections**: Allow gates to "see" the cell state directly by adding peephole connections from C_{t-1} to the gate layers.

2. **Gated Recurrent Unit (GRU)**: Combines forget and input gates into a single "update gate" and merges cell state and hidden state. It has fewer parameters than LSTM but often performs similarly.

3. **Bidirectional LSTM**: Processes sequences in both forward and backward directions, useful when the entire sequence is available (e.g., speech recognition, NLP tasks).

## Examples

### Example 1: LSTM Forward Pass Calculation

Consider a simplified LSTM with the following initialized weights (for educational clarity):

Assume single units for input and hidden state:
- Sigmoid activation: σ(x) = 1/(1 + e^(-x))
- tanh activation: tanh(x)

Given:
- Previous hidden state: h_{t-1} = 0.5
- Previous cell state: C_{t-1} = 0.8
- Current input: x_t = 0.3

Let weight matrices (simplified as scalars for demonstration):
- All weight matrices W = 0.2
- All bias terms b = 0

Step 1: Forget Gate
f_t = σ(W_f × h_{t-1} + U_f × x_t + b_f)
f_t = σ(0.2 × 0.5 + 0.2 × 0.3 + 0) = σ(0.16) ≈ 0.540

Step 2: Input Gate
i_t = σ(0.2 × 0.5 + 0.2 × 0.3) = σ(0.16) ≈ 0.540
C̃_t = tanh(0.2 × 0.5 + 0.2 × 0.3) = tanh(0.16) ≈ 0.159

Step 3: Cell State Update
C_t = f_t × C_{t-1} + i_t × C̃_t
C_t = 0.540 × 0.8 + 0.540 × 0.159 ≈ 0.432 + 0.086 = 0.518

Step 4: Output Gate
o_t = σ(0.2 × 0.5 + 0.2 × 0.3) = σ(0.16) ≈ 0.540
h_t = o_t × tanh(C_t) = 0.540 × tanh(0.518) ≈ 0.540 × 0.475 = 0.257

The final outputs are: h_t = 0.257, C_t = 0.518

### Example 2: Understanding Gate Behavior

Suppose we're building an LSTM to predict the next word in a sentence. Consider the sentence: "The clouds will rain tomorrow."

When processing "tomorrow," the network needs to remember "clouds" from the beginning:
- The forget gate should retain information about "clouds" (high value near 1)
- The input gate should add information about "rain" from the current context
- The output gate should output information relevant to predicting "tomorrow" as the next word

This demonstrates how LSTMs selectively remember relevant information over long sequences.

### Example 3: LSTM for Time Series Forecasting

For stock price prediction, an LSTM might:
1. At time t, receive today's price and previous hidden state
2. Forget gate decides if yesterday's minor fluctuations should be forgotten
3. Input gate adds any significant new patterns detected
4. Output gate produces prediction for tomorrow's price

If a sudden market crash occurs, the input gate will capture this significant event, and the cell state will preserve this information to influence future predictions, unlike standard RNNs which would let this crucial information vanish.

## Exam Tips

1. **Understand the Problem LSTM Solves**: Be clear about why LSTM was invented - to solve the vanishing gradient problem in standard RNNs that prevented learning long-term dependencies.

2. **Memorize the Three Gates**: Remember that LSTM has three gates (forget, input, output) with specific purposes. The forget gate decides what to discard, input gate decides what to add, output gate decides what to output.

3. **Know the Cell State Role**: The cell state is the key innovation - it's the "highway" for information flow that remains relatively unchanged across time steps.

4. **Sigmoid Always for Gates**: Remember that gate activations always use sigmoid (output 0-1) to represent how much information passes, while state updates use tanh (-1 to 1).

5. **Understand BPTT in LSTMs**: Unlike standard RNNs, LSTMs maintain gradients through the cell state, making backpropagation more effective for long sequences.

6. **Difference Between LSTM and GRU**: Know that GRU combines forget and input gates, merges cell state and hidden state, making it simpler but often equally effective.

7. **Bidirectional LSTM Applications**: For tasks like named entity recognition where context from both directions matters, bidirectional LSTMs are essential.

8. **Real-World Applications**: Be prepared to explain applications like machine translation, speech recognition, video analysis, and time series prediction.

9. **Gradient Flow Visualization**: Practice drawing and explaining how gradients flow through the cell state without vanishing.

10. **Comparison with RNN**: Always be ready to compare LSTM with standard RNN - LSTM has gating mechanism, maintains cell state, solves vanishing gradient, but has more parameters.