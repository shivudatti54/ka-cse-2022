# Artificial Neural Networks: Introduction to Biological and Artificial Neurons, Perceptron, and Learning

=====================================================

## 10.9-10.11: Introduction to Artificial Neural Networks

### Biological Neurons

Biological neurons, also known as nerve cells, are the basic building blocks of the nervous system in animals. They are specialized cells that process and transmit information through electrical and chemical signals.

**Key Characteristics of Biological Neurons:**

- Receive input signals from other neurons or sensory receptors
- Process the input signals through electrical and chemical signals
- Transmit the processed signals to other neurons or muscles
- Have a controlled release of neurotransmitters to transmit signals

**Example:** The human brain contains approximately 86 billion neurons, each with an average of 7,000 synapses (connections to other neurons).

### Artificial Neurons

Artificial neurons, also known as perceptrons, are mathematical models of biological neurons. They are used to simulate the behavior of biological neurons and are the core components of artificial neural networks.

**Key Characteristics of Artificial Neurons:**

- Receive input signals from other neurons or sensors
- Process the input signals through weighted sums and activation functions
- Transmit the processed signals to other neurons or actuators
- Can be trained using machine learning algorithms to improve performance

**Example:** An artificial neuron can be modeled using the following equation:

```
output = activation_function(sum weighted inputs)
```

Where `weighted inputs` are the inputs multiplied by their corresponding weights, and `activation function` is a mathematical function that maps the weighted sum to an output value.

### Perceptron

The perceptron is a type of artificial neuron that is capable of learning and adapting to new data. It is a simple neural network that consists of a single artificial neuron with a linear activation function.

**Key Characteristics of the Perceptron:**

- Can learn and adapt to new data using a training algorithm
- Uses a linear activation function to process input signals
- Can only learn linearly separable data

**Example:** The perceptron can be trained using the following equations:

```
weight1 = learning_rate * error * input1
weight2 = learning_rate * error * input2
output = input1 * weight1 + input2 * weight2
```

Where `learning_rate` is the rate at which the weights are updated, `error` is the difference between the predicted output and the actual output, and `input1` and `input2` are the inputs to the perceptron.

### Learning

Learning is the process of adjusting the weights and biases of artificial neurons to improve their performance on a given task. There are several types of learning algorithms, including:

- **Supervised learning:** The algorithm is trained on labeled data, where the correct output is provided for each input.
- **Unsupervised learning:** The algorithm is trained on unlabeled data, and the goal is to discover patterns or structure in the data.
- **Reinforcement learning:** The algorithm is trained using trial and error, where the goal is to maximize a reward signal.

**Example:** A simple supervised learning algorithm can be implemented using the following steps:

1. Collect labeled data (e.g. images of dogs and cats)
2. Split the data into training and testing sets
3. Train the perceptron using the training data
4. Evaluate the performance of the perceptron on the testing data
