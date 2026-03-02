# **Chapter -13: Artificial Neural Networks**

## **13.1: Introduction to Artificial Neural Networks**

### Definition

An Artificial Neural Network (ANN) is a computational model inspired by the structure and function of biological neurons. ANNs are composed of interconnected nodes or "neurons" that process and transmit information.

### Key Characteristics

- **Distributed representation**: ANNs represent data as a distributed representation of features, where each node represents a feature.
- **Parallel processing**: ANNs process information in parallel, making them efficient for large datasets.
- **Non-linearity**: ANNs can learn non-linear relationships between inputs and outputs.

### Applications

- **Image recognition**: ANNs are used in image recognition applications, such as self-driving cars and facial recognition.
- **Natural Language Processing**: ANNs are used in natural language processing applications, such as language translation and sentiment analysis.

### Example

Consider a simple ANN that takes in two inputs, x1 and x2, and produces an output y. The ANN consists of two nodes, each with a weighted connection to the inputs and a bias term.

| Node | Input | Weight | Bias | Output |
| ---- | ----- | ------ | ---- | ------ |
| 1    | x1    | w1     | b1   | z1     |
| 2    | x2    | w2     | b2   | z2     |

The output of each node is calculated using the following formula:

z = w \* x + b

where z is the output, w is the weight, x is the input, and b is the bias.

### Learning Algorithm

The learning algorithm for ANNs is based on the backpropagation algorithm, which adjusts the weights and biases to minimize the error between the predicted output and the actual output.

### Example Code

```python
import numpy as np

# Define the inputs and weights
x1 = np.array([1, 2])
x2 = np.array([3, 4])
w1 = np.array([0.5, 0.3])
w2 = np.array([0.2, 0.1])
b1 = np.array([0.1, 0.2])
b2 = np.array([0.3, 0.4])

# Calculate the output
z1 = w1 * x1 + b1
z2 = w2 * x2 + b2

# Calculate the error
error = np.mean((z1 - x1) ** 2 + (z2 - x2) ** 2)

# Backpropagation
delta1 = 0.1 * (z1 - x1)
delta2 = 0.1 * (z2 - x2)

# Update the weights and biases
w1 -= 0.01 * delta1 * x1
w2 -= 0.01 * delta2 * x2
b1 -= 0.01 * delta1
b2 -= 0.01 * delta2

print("Error:", error)
print("Weights:", w1, w2)
print("Biases:", b1, b2)
```

## **13.2: Biological Neurons**

### Structure

A biological neuron consists of:

- **Dendrites**: Receive signals from other neurons.
- **Cell Body**: Contains the nucleus and other organelles.
- **Axon**: Transmits signals to other neurons or to muscles or glands.
- **Synapses**: The gaps between neurons where chemical signals are transmitted.

### Function

Biological neurons process and transmit information through the following steps:

1.  **Signal reception**: Dendrites receive signals from other neurons.
2.  **Signal integration**: The cell body integrates the signals from the dendrites.
3.  **Signal transmission**: The axon transmits the signal to other neurons or to muscles or glands.
4.  **Signal termination**: The signal is terminated at the synapses.

### Key Concepts

- **Threshold**: The minimum amount of signal required to trigger an action potential.
- **Action potential**: A sudden change in the membrane potential that allows the signal to be transmitted.
- **Neurotransmitters**: Chemical signals that transmit information between neurons.

### Example

Consider a biological neuron that receives signals from two other neurons, A and B. The neuron has a threshold of 0.5 and an action potential threshold of 0.8.

| Dendrite | Signal | Strength |
| -------- | ------ | -------- |
| A        | 0.6    | 0.8      |
| B        | 0.4    | 0.7      |

The cell body integrates the signals from the dendrites and calculates the total signal strength.

Signal strength = 0.6 + 0.4 = 1.0

Since the signal strength is greater than the threshold, an action potential is triggered.

### Learning Algorithm

The learning algorithm for biological neurons is based on the Hebbian rule, which states that "neurons that fire together, wire together."

### Example Code

```python
import numpy as np

# Define the inputs and weights
x1 = np.array([0.6, 0.4])
w1 = np.array([0.8, 0.7])
b1 = np.array([0.0, 0.0])

# Calculate the output
output = np.dot(x1, w1) + b1

# Check if the output exceeds the threshold
if output > 0.5:
    print("Action potential triggered")
else:
    print("No action potential triggered")

# Update the weights and biases
w1 += 0.01 * x1
b1 += 0.01
```

## **13.3: Artificial Neurons**

### Definition

An artificial neuron is a computational model that mimics the behavior of biological neurons. It consists of:

- **Input**: The input signals from other neurons.
- **Weight**: The strength of the connection between the input and the output.
- **Bias**: The offset term that adjusts the output.
- **Output**: The result of the computation.

### Key Characteristics

- **Non-linearity**: Artificial neurons can learn non-linear relationships between inputs and outputs.
- **Parallel processing**: Artificial neurons can process information in parallel, making them efficient for large datasets.

### Example

Consider an artificial neuron that takes in two inputs, x1 and x2, and has a weight and bias term.

| Input | Weight | Bias |
| ----- | ------ | ---- |
| x1    | w1     | b1   |
| x2    | w2     | b2   |

The output of the neuron is calculated using the following formula:

output = w1 \* x1 + b1
output = w2 \* x2 + b2

### Learning Algorithm

The learning algorithm for artificial neurons is based on the backpropagation algorithm, which adjusts the weights and biases to minimize the error between the predicted output and the actual output.

### Example Code

```python
import numpy as np

# Define the inputs and weights
x1 = np.array([1, 2])
x2 = np.array([3, 4])
w1 = np.array([0.5, 0.3])
w2 = np.array([0.2, 0.1])
b1 = np.array([0.1, 0.2])
b2 = np.array([0.3, 0.4])

# Calculate the output
output1 = w1 * x1 + b1
output2 = w2 * x2 + b2

# Calculate the error
error = np.mean((output1 - x1) ** 2 + (output2 - x2) ** 2)

# Backpropagation
delta1 = 0.1 * (output1 - x1)
delta2 = 0.1 * (output2 - x2)

# Update the weights and biases
w1 -= 0.01 * delta1 * x1
w2 -= 0.01 * delta2 * x2
b1 -= 0.01 * delta1
b2 -= 0.01 * delta2

print("Error:", error)
print("Weights:", w1, w2)
print("Biases:", b1, b2)
```

## **13.4: Perceptron**

### Definition

A Perceptron is a type of artificial neuron that can learn linearly separable patterns. It consists of:

- **Input**: The input signals from other neurons.
- **Weight**: The strength of the connection between the input and the output.
- **Bias**: The offset term that adjusts the output.
- **Output**: The result of the computation.

### Key Characteristics

- **Linear separability**: Perceptrons can learn linearly separable patterns, meaning that the output can be separated into two or more classes using a linear decision boundary.
- **No non-linearity**: Perceptrons do not have non-linear activation functions, which means that they can only learn linearly separable patterns.

### Example

Consider a Perceptron that takes in two inputs, x1 and x2, and has a weight and bias term.

| Input | Weight | Bias |
| ----- | ------ | ---- |
| x1    | w1     | b1   |
| x2    | w2     | b2   |

The output of the Perceptron is calculated using the following formula:

output = w1 \* x1 + b1
output = w2 \* x2 + b2

### Learning Algorithm

The learning algorithm for Perceptrons is based on the perceptron learning rule, which adjusts the weights and biases to minimize the number of errors.

### Example Code

```python
import numpy as np

# Define the inputs and weights
x1 = np.array([1, 2])
x2 = np.array([3, 4])
w1 = np.array([0.5, 0.3])
w2 = np.array([0.2, 0.1])
b1 = np.array([0.1, 0.2])
b2 = np.array([0.3, 0.4])

# Calculate the output
output1 = w1 * x1 + b1
output2 = w2 * x2 + b2

# Calculate the error
error = np.mean((output1 - x1) ** 2 + (output2 - x2) ** 2)

# Perceptron learning rule
if output1 > x1 and output2 > x2:
    w1 += 0.01 * x1
    w2 += 0.01 * x2
    b1 += 0.01
    b2 += 0.01
elif output1 < x1 and output2 < x2:
    w1 -= 0.01 * x1
    w2 -= 0.01 * x2
    b1 -= 0.01
    b2 -= 0.01

print("Error:", error)
print("Weights:", w1, w2)
print("Biases:", b1, b2)
```

## **13.5: Multilayer Perceptron (MLP)**

### Definition

A Multilayer Perceptron (MLP) is a type of artificial neuron that can learn complex patterns. It consists of:

- **Input**: The input signals from other neurons.
- **Hidden layers**: One or more hidden layers that process the input signals.
- **Output layer**: The output layer that produces the final output.

### Key Characteristics

- **Non-linearity**: MLPs can learn non-linear relationships between inputs and outputs.
- **Parallel processing**: MLPs can process information in parallel, making them efficient for large datasets.

### Example

Consider an MLP that takes in two inputs, x1 and x2, and has two hidden layers and an output layer.

| Input | Weight | Bias |
| ----- | ------ | ---- |
| x1    | w1     | b1   |
| x2    | w2     | b2   |

The output of the MLP is calculated using the following formula:

h1 = w1 \* x1 + b1
h2 = w2 \* x2 + b2

The output of the hidden layer is calculated using the following formula:

h3 = sigmoid(h1)
h4 = sigmoid(h2)

The output of the output layer is calculated using the following formula:

output = w3 \* h3 + b3
output = w4 \* h4 + b4

### Learning Algorithm

The learning algorithm for MLPs is based on the backpropagation algorithm, which adjusts the weights and biases to minimize the error between the predicted output and the actual output.

### Example Code

```python
import numpy as np
from sklearn.neural_network import MLPClassifier

# Define the inputs and weights
x1 = np.array([1, 2])
x2 = np.array([3, 4])
w1 = np.array([0.5, 0.3])
w2 = np.array([0.2, 0.1])
b1 = np.array([0.1, 0.2])
b2 = np.array([0.3, 0.4])

# Calculate the output
h1 = w1 * x1 + b1
h2 = w2 * x2 + b2

# Calculate the output
output = np.dot([h1, h2], [[0.5, 0.3], [0.2, 0.1]])

# Calculate the error
error = np.mean((output - [5, 6]) ** 2)

# MLP learning algorithm
mlp = MLPClassifier(hidden_layer_sizes=(10,))
mlp.fit([x1, x2], [5, 6])

print("Error:", error)
print("Weights:", mlp.coefs_[0])
print("Biases:", mlp.intercepts_[0])
```

## **13.6: Applications of Artificial Neural Networks**

### Definition

Artificial neural networks have a wide range of applications in various fields, including:

- **Image recognition**: ANNs are used in image recognition applications, such as self-driving cars and facial recognition.
- **Natural Language Processing**: ANNs are used in natural language processing applications, such as language translation and sentiment analysis.
- **Speech recognition**: ANNs are used in speech recognition applications, such as voice assistants and speech-to-text systems.
- **Time series prediction**: ANNs are used in time series prediction applications, such as stock market prediction and weather forecasting.

### Key Characteristics

- **Flexibility**: ANNs can learn non-linear relationships between inputs and outputs.
- **Parallel processing**: ANNs can process information in parallel, making them efficient for large datasets.

### Example

Consider an ANN that takes in a time series dataset and predicts the next value in the sequence. The ANN is trained using the backpropagation algorithm and consists of two hidden layers and an output layer.

| Input     | Weight | Bias |
| --------- | ------ | ---- |
| Time step | w1     | b1   |
| Time step | w2     | b2   |

The output of the ANN is calculated using the following formula:

output = w1 \* time step + b1
output = w2 \* time step + b2

### Learning Algorithm

The learning algorithm for ANNs is based on the backpropagation algorithm, which adjusts the weights and biases to minimize the error between the predicted output and the actual output.

### Example Code

```python
import numpy as np
from sklearn.neural_network import MLPRegressor

# Define the inputs and weights
time_step = np.array([1, 2, 3, 4, 5])
w1 = np.array([0.5, 0.3])
w2 = np.array([0.2, 0.1])
b1 = np.array([0.1, 0.2])
b2 = np.array([0.3, 0.4])

# Calculate the output
output = np.dot([time_step, time_step], [[w1, w2], [b1, b2]])

# Calculate the error
error = np.mean((output - [6, 7]) ** 2)

# ANN learning algorithm
ann = MLPRegressor(hidden_layer_sizes=(10,))
ann.fit([time_step], [6, 7])

print("Error:", error)
print("Weights:", ann.coefs_[0])
print("Biases:", ann.intercepts_[0])
```

In conclusion, artificial neural networks are a powerful tool for modeling complex relationships between inputs and outputs. They have a wide range of applications in various fields, including image recognition, natural language processing, speech recognition, and time series prediction.
