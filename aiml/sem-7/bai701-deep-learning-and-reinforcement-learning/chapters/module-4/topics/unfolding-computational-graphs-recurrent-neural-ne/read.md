# Unfolding Computational Graphs, Recurrent Neural Networks, Bidirectional RNNs, Deep Recurrent Networks, Recursive Neural Networks, The Long Short-Term

=====================================================

## Introduction

---

Recurrent Neural Networks (RNNs) are a fundamental component of deep learning and reinforcement learning. They are designed to process sequential data efficiently, handling the complexities of temporal relationships. In this study material, we will delve into the concepts of unfolding computational graphs, Recurrent Neural Networks, Bidirectional RNNs, Deep Recurrent Networks, Recursive Neural Networks, and The Long Short-Term.

## Unfolding Computational Graphs

---

Unfolding computational graphs is a technique used to analyze and understand the dynamic behavior of RNNs. It involves breaking down the complex temporal relationships into a series of static computations, allowing for better insights into the model's behavior.

### Key Concepts:

- **Temporal Unfolding**: The process of unfolding the temporal dimension of an RNN into a series of static computations.
- **Static Computation**: A single computation that occurs at a specific time step, without considering the previous or future time steps.
- **Dynamic Computation**: A computation that depends on previous or future time steps.

### Example:

Suppose we have an RNN with two time steps: `t = 1` and `t = 2`. The computation at `t = 1` depends on the previous time step `t-1`, and the computation at `t = 2` depends on both the previous and current time steps.

| Time Step | Hidden State                   | Output                         |
| --------- | ------------------------------ | ------------------------------ |
| 1         | `h1`                           | `o1`                           |
| 2         | `h2` = `h1` + `W1 * o1` + `b1` | `o2` = `h2` + `W2 * o1` + `b2` |

By unfolding the computational graph, we can represent the dynamic behavior of the RNN as a series of static computations:

| Time Step | Hidden State                   | Output                        |
| --------- | ------------------------------ | ----------------------------- |
| 1         | `h1` = `I` + `W1 * o1` + `b1`  | -                             |
| 1         | `h1`                           | -                             |
| 2         | `h2` = `h1` + `W1 * o1` + `b1` | `o1` = `I` + `W1 * o1` + `b1` |
| 2         | `h2`                           | `o1`                          |
| 2         | `h2`                           | -                             |

## Recurrent Neural Networks

---

RNNs are designed to process sequential data by maintaining a hidden state that captures the temporal relationships between consecutive time steps.

### Key Concepts:

- **Recurrent Connection**: A connection between the hidden state at a previous time step and the current time step.
- **Hidden State**: The internal state of the RNN that captures the temporal relationships between consecutive time steps.
- **Output**: The output of the RNN at a specific time step.

### Example:

Suppose we have an RNN with two time steps: `t = 1` and `t = 2`. The hidden state at `t = 1` is `h1`, and the output at `t = 1` is `o1`.

| Time Step | Hidden State                   | Output                         |
| --------- | ------------------------------ | ------------------------------ |
| 1         | `h1`                           | `o1`                           |
| 2         | `h2` = `h1` + `W1 * o1` + `b1` | `o2` = `h2` + `W2 * o1` + `b2` |

## Bidirectional RNNs

---

Bidirectional RNNs are designed to process sequential data by maintaining two separate hidden states: one for the forward direction and one for the backward direction.

### Key Concepts:

- **Bidirectional Connection**: A connection between the forward and backward hidden states.
- **Forward Hidden State**: The hidden state that captures the temporal relationships in the forward direction.
- **Backward Hidden State**: The hidden state that captures the temporal relationships in the backward direction.
- **Output**: The output of the RNN at a specific time step.

### Example:

Suppose we have a Bidirectional RNN with two time steps: `t = 1` and `t = 2`. The forward hidden state at `t = 1` is `h1_f`, and the backward hidden state at `t = 1` is `h1_b`.

| Time Step | Forward Hidden State                   | Backward Hidden State                  | Output                               |
| --------- | -------------------------------------- | -------------------------------------- | ------------------------------------ |
| 1         | `h1_f`                                 | `h1_b`                                 | `o1`                                 |
| 2         | `h2_f` = `h1_f` + `W1_f * o1` + `b1_f` | `h2_b` = `h1_b` + `W1_b * o1` + `b1_b` | `o2` = `h2_f` + `W2_f * o1` + `b2_f` |

## Deep Recurrent Networks

---

Deep Recurrent Networks are designed to process sequential data by stacking multiple RNNs on top of each other.

### Key Concepts:

- **Stacking**: The process of stacking multiple RNNs on top of each other.
- **Hidden State**: The internal state of the RNN that captures the temporal relationships between consecutive time steps.
- **Output**: The output of the RNN at a specific time step.

### Example:

Suppose we have a Deep Recurrent Network with three RNNs: RNN1, RNN2, and RNN3. The hidden state of RNN1 is `h1`, and the output of RNN2 is `o2`.

| Time Step | Hidden State                   | Output                         |
| --------- | ------------------------------ | ------------------------------ |
| 1         | `h1`                           | `o2`                           |
| 2         | `h2` = `h1` + `W1 * o2` + `b1` | -                              |
| 3         | `h3` = `h2` + `W2 * o2` + `b2` | `o3` = `h3` + `W3 * o2` + `b3` |

## Recursive Neural Networks

---

Recursive Neural Networks are designed to process sequential data by recursively applying a set of transformations to the input data.

### Key Concepts:

- **Recursion**: The process of recursively applying a set of transformations to the input data.
- **Transformations**: A set of operations that are applied to the input data to produce the output.
- **Output**: The output of the RNN at a specific time step.

### Example:

Suppose we have a Recursive Neural Network with two transformations: `T1` and `T2`. The input data is `x`, and the output is `o`.

| Time Step | Input | Transformations | Output |
| --------- | ----- | --------------- | ------ |
| 1         | `x`   | `T1`            | `o1`   |
| 2         | `o1`  | `T2`            | `o2`   |

## The Long Short-Term

---

The Long Short-Term (LSTM) is a type of RNN that uses memory cells to capture long-term dependencies in sequential data.

### Key Concepts:

- **Memory Cell**: A cell that stores the output of the previous time step.
- **Input Gate**: The gate that controls the input to the memory cell.
- **Output Gate**: The gate that controls the output from the memory cell.
- **Forget Gate**: The gate that controls the forgetfulness of the memory cell.

### Example:

Suppose we have an LSTM with three time steps: `t = 1`, `t = 2`, and `t = 3`. The memory cell at `t = 1` is `m1`, and the output at `t = 1` is `o1`.

| Time Step | Input | Memory Cell                    | Output Gate | Forget Gate | Input Gate                     | Output |
| --------- | ----- | ------------------------------ | ----------- | ----------- | ------------------------------ | ------ |
| 1         | `x`   | `m1`                           | `o1`        | `f1`        | `i1`                           | `o1`   |
| 2         | `x`   | `m2` = `m1` + `W1 * o1` + `b1` | `f2`        | `i2`        | `o2` = `m2` + `W2 * o1` + `b2` |
| 3         | `x`   | `m3` = `m2` + `W1 * o2` + `b1` | `f3`        | `i3`        | `o3` = `m3` + `W2 * o2` + `b2` |

By using the LSTM, we can capture long-term dependencies in sequential data while avoiding the vanishing gradient problem.
