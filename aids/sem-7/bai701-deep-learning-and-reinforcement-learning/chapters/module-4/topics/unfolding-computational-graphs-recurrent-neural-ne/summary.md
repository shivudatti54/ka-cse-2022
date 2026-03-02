# Unfolding Computational Graphs, Recurrent Neural Network, Bidirectional RNNs, Deep Recurrent Networks, Recursive Neural Networks, The Long Short-Term

=====================================

## Introduction

---

Recurrent Neural Networks (RNNs) are a type of neural network designed to handle sequential data. They can learn patterns in data that have temporal relationships.

## Unfolding Computational Graphs

---

- Unfolding is a technique used to simplify the computation of RNNs by transforming them into a flat, feedforward neural network.
- The unfolded graph is a 2D representation of the original RNN's computational graph.
- Formula: `RNN = [RNN'] * W`

## Recurrent Neural Networks (RNNs)

---

- A type of neural network designed to handle sequential data.
- Each neuron in the network maintains an internal state that is updated based on the input and previous state.
- Formula: `h_t = f(x_t, h_{t-1})`

## Bidirectional RNNs (BRNNs)

---

- A type of RNN that uses two separate RNNs, one that processes the input sequence from left to right and another from right to left.
- The output of the two RNNs is then combined to produce the final output.
- Formula: `h_t = f(x_t, h_{t-1}) + f(x_t, h_{t-1}^R)`

## Deep Recurrent Networks

---

- A type of RNN that uses multiple layers to process sequential data.
- Each layer is connected to the previous layer through a set of weights.
- Formula: `h_t = f(W * h_{t-1} + b)`

## Recursive Neural Networks (RNNs)

---

- A type of neural network that uses recursion to process sequential data.
- Each layer is connected to the previous layer through a set of weights.
- Formula: `h_t = f(W * h_{t-1} + b)`

## The Long Short-Term Memory (LSTM)

---

- A type of RNN that uses a memory cell to learn long-term dependencies in sequential data.
- The memory cell is updated based on the input and previous state.
- Formula: `c_t = f(W_c * h_{t-1} + U_c * c_{t-1} + b_c)`

## Theorems:

- The chain rule for RNNs states that the output of the network is a linear combination of the input and previous state.
- The convolutional neural network (CNN) has a similar structure to RNNs, but it is used to process spatial data instead of temporal data.
