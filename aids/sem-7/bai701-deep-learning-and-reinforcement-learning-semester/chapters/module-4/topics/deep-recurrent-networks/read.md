# Recurrent Neural Networks (RNNs)

## 1. Introduction to Sequence Modeling

Traditional neural networks, like Multi-Layer Perceptrons (MLPs) and Convolutional Neural Networks (CNNs), are designed to work with fixed-size input vectors. They assume all inputs are independent of each other. However, many real-world problems involve **sequential data** where the order and context of previous inputs are crucial for understanding the current one.

**Examples of Sequential Data:**
*   **Time Series:** Stock prices, weather data, sensor readings.
*   **Natural Language:** Sentences, paragraphs, speech signals.
*   **Genomic Sequences:** DNA and protein sequences.
*   **Video Frames:** A sequence of images.

A Recurrent Neural Network (RNN) is a class of artificial neural networks designed specifically to recognize patterns in sequences of data. Their key feature is an internal "memory" that captures information about what has been computed so far in the sequence.

## 2. The Core Concept of RNNs: Persistence of State

The fundamental idea behind an RNN is its **recurrent connection**. At each time step `t`, the network not only receives a new input `x_t` but also its own hidden state from the previous time step `h_{t-1}`. This hidden state acts as a "memory" of all the previous elements in the sequence.

```
Time Step t:   Input (x_t)  +  Previous Hidden State (h_{t-1})  ->  New Hidden State (h_t) & Output (y_t)
```

This creates a loop within the network, allowing information to persist from one step to the next.

## 3. Unfolding the RNN Through Time

To understand how an RNN processes an entire sequence, we "unroll" or "unfold" it through time. This means we create a copy of the network for each time step, showing the flow of information.

**ASCII Diagram of an Unfolded RNN:**

```
      h₀
       │
       ▼
x₁ ──► RNN ──► y₁
       │
       ▼ h₁
       │
       ▼
x₂ ──► RNN ──► y₂
       │
       ▼ h₂
       │
       ▼
x₃ ──► RNN ──► y₃
       │
       ▼ h₃
```

*   `x_t`: Input at time step `t` (e.g., a word in a sentence, a stock price on a day).
*   `h_t`: Hidden state at time step `t`. This is the "memory" of the network.
*   `y_t`: Output at time step `t`.
*   The arrow from `h_t` to the next RNN cell represents the recurrent connection, passing the memory forward.

This unfolded view reveals that an RNN is essentially a very deep neural network where the same parameters (weights) are shared across all time steps.

## 4. Mathematical Formulation

The computations at a single time step `t` are defined by the following equations:

**Hidden State Update:**
`h_t = activation_function(W_{xh} * x_t + W_{hh} * h_{t-1} + b_h)`

**Output Calculation:**
`y_t = W_{hy} * h_t + b_y`

Where:
*   `W_{xh}`: Weight matrix connecting the input to the hidden layer.
*   `W_{hh}`: Weight matrix connecting the previous hidden state to the current hidden state (the recurrent weights).
*   `W_{hy}`: Weight matrix connecting the hidden state to the output.
*   `b_h`, `b_y`: Bias vectors.
*   `activation_function`: Typically a `tanh` or `ReLU` function.

**The key point is that the matrices `W_{xh}`, `W_{hh}`, and `W_{hy}` are shared across all time steps.** This parameter sharing makes the model efficient and allows it to generalize to sequences of different lengths.

## 5. Types of RNN Architectures

Depending on the task, the input and output sequences can have different structures.

| Architecture | Input Sequence | Output Sequence | Example Use Case |
| :--- | :--- | :--- | :--- |
| **One-to-One** | Single | Single | Standard image classification (not sequential) |
| **One-to-Many** | Single | Sequence | Image captioning (image -> sequence of words) |
| **Many-to-One** | Sequence | Single | Sentiment analysis (sentence -> sentiment score) |
| **Many-to-Many (Synced)** | Sequence | Sequence (same length) | Video frame classification (e.g., per-frame tagging) |
| **Many-to-Many (Delayed)** | Sequence | Sequence (different length) | Machine Translation (e.g., Encoder-Decoder architecture) |

## 6. The Problem of Long-Term Dependencies: Vanishing and Exploding Gradients

While RNNs are theoretically capable of connecting past information to the present task, they struggle to learn long-range dependencies in practice. This is due to the **vanishing/exploding gradient problem**.

During training, we use Backpropagation Through Time (BPTT). The gradient is calculated at the final output and propagated back through every time step. For long sequences, this gradient is a product of many terms (the chain rule).

*   **Vanishing Gradient:** If the gradients are small (|W_{hh}| < 1), repeated multiplication causes the gradient to shrink exponentially, becoming vanishingly small. The early layers in the sequence (time steps) don't get updated effectively, so the network "forgets" what it saw long ago.
*   **Exploding Gradient:** If the gradients are large (|W_{hh}| > 1), repeated multiplication causes the gradient to grow exponentially, becoming huge and causing the model to diverge (NaN values).

This problem makes it very difficult for a simple RNN to learn to associate information that is many steps apart.

## 7. Long Short-Term Memory (LSTM) Networks

To solve the vanishing gradient problem, Sepp Hochreiter and Jürgen Schmidhuber introduced the Long Short-Term Memory (LSTM) network in 1997. LSTMs are a special kind of RNN explicitly designed to remember information for long periods.

The key innovation of the LSTM is its **memory cell** and gating mechanism. The cell state `c_t` acts as a "conveyor belt" that runs through the entire sequence chain, with only minor linear interactions, making it easy for information to flow unchanged.

### LSTM Gates

LSTMs have three gates that regulate the flow of information into, within, and out of the cell:

1.  **Forget Gate (`f_t`):** Decides what information to *throw away* from the cell state. It looks at `h_{t-1}` and `x_t`, and outputs a number between 0 (completely forget) and 1 (completely keep) for each number in the cell state `c_{t-1}`.
    `f_t = σ(W_f * [h_{t-1}, x_t] + b_f)`

2.  **Input Gate (`i_t`):** Decides what *new information* to store in the cell state. First, a `tanh` layer creates a vector of new candidate values, `\tilde{C}_t`. Then, the input gate decides which values to update.
    `i_t = σ(W_i * [h_{t-1}, x_t] + b_i)`
    `\tilde{C}_t = tanh(W_C * [h_{t-1}, x_t] + b_C)`

3.  **Output Gate (`o_t`):** Decides what *to output* based on the current cell state. The output is a filtered version of the cell state.
    `o_t = σ(W_o * [h_{t-1}, x_t] + b_o)`

### Updating the Cell State and Hidden State

The old cell state `c_{t-1}` is updated to the new cell state `c_t`:
`c_t = f_t * c_{t-1} + i_t * \tilde{C}_t`

The new hidden state `h_t` (which is also the output for this time step) is then:
`h_t = o_t * tanh(c_t)`

**ASCII Diagram of an LSTM Cell at a single time step:**

```
 (Previous Hidden State)
        h_{t-1}
          │
 (Previous Cell State)   ┌─────┐
        c_{t-1} ────────►│  f  │───┐
          │              └─────┘   │
          │                         │
 (Current Input)        ┌─────┐     │  ┌───┐
        x_t  ──────────►│  i  │────┼─►│ * │─────┐
          │             └─────┘    │  └───┘     │
          │             ┌─────┐    │            │
          └────────────►│  o  │    │            ▼
                        └─────┘    │        ┌────────┐
                                   ▼        │ Cell   │
                                ┌───┐       │ State  │
                                │ * │◄──────│ Update │◄─────┐
                                └───┘       └────────┘      │
                                  │             │           │
                                  │             ▼ c_t       │
                                  │             │           │
                                  │             ▼tanh       │
                                  │             │           │
                                  └───────────►│ * │◄──────┘
                                               └───┘
                                                 │
                                                 ▼
                                                h_t, y_t
```
*Note: This is a simplified conceptual diagram. The `[h_{t-1}, x_t]` concatenation is implied as input to each gate.*

## 8. Gated Recurrent Unit (GRU)

The Gated Recurrent Unit (GRU) is a simpler variant of the LSTM introduced in 2014. It combines the forget and input gates into a single "update gate." It also merges the cell state and hidden state. This results in a model that is often faster to train and has fewer parameters, while still performing comparably to an LSTM on many tasks.

## 9. Applications of RNNs and LSTMs

*   **Machine Translation:** Many-to-many Encoder-Decoder models (e.g., Google Translate).
*   **Speech Recognition:** Converting audio signals to text.
*   **Text Generation:** Generating new text character-by-character or word-by-word.
*   **Sentiment Analysis:** Classifying the sentiment of a sentence or document.
*   **Time Series Prediction:** Forecasting stock prices or weather.

## Exam Tips

1.  **Understand the "Why":** Be prepared to explain why we need RNNs. Contrast them with Feedforward networks for sequential data.
2.  **Draw the Diagram:** Practice drawing the unfolded RNN and the internal structure of an LSTM cell. Label all components (x_t, h_t, gates, cell state).
3.  **Know the Equations:** For exams, you might need to write down the core update equations for a vanilla RNN and know the purpose of each gate in an LSTM (Forget, Input, Output).
4.  **Vanishing Gradients:** Explain the problem of vanishing gradients in simple RNNs and how LSTMs solve it using the gating mechanism and cell state.
5.  **Application Matching:** Be able to match the correct RNN architecture (One-to-Many, Many-to-One, etc.) to a given problem description.
6.  **LSTM vs. GRU:** Know the key difference: GRUs have fewer parameters and combine the cell state and hidden state, making them computationally more efficient.