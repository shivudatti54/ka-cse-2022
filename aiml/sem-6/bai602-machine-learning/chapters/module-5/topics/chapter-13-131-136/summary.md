# **Chapter 13 Revision Notes**

## **Introduction**

- Artificial Neural Networks (ANNs) are a key component of Machine Learning.
- Inspired by the structure and function of biological neurons.
- ANNs are composed of interconnected nodes (neurons) that process and transmit information.

## **13.1: Biological Neurons**

- Biological neurons are the building blocks of the nervous system.
- They receive input, process information, and transmit output through electrical and chemical signals.
- Key components:
  - Dendrites (receive input)
  - Cell body (processes information)
  - Axon (transmits output)

## **13.2: Artificial Neurons (Artificial Perceptron)**

- Artificial neurons are modeled after biological neurons.
- They receive input, process information, and transmit output using mathematical equations.
- Key components:
  - Weights and biases
  - Activation functions (e.g. sigmoid, ReLU)

## **13.3: Perceptron Learning Rule**

- Perceptron learning rule is an algorithm for training artificial neurons.
- It updates the weights and biases of the neuron based on the error between the predicted and actual output.
- Key equation:
  - Δw = α \* (y - y') \* x
  - where Δw is the update to the weight, α is the learning rate, y is the predicted output, y' is the actual output, and x is the input.

## **13.4: Multi-Layer Perceptron (MLP)**

- MLPs are a type of ANNs that consist of multiple layers of artificial neurons.
- Each layer processes the input and transforms it into a higher-level representation.
- Key components:
  - Input layer
  - Hidden layers
  - Output layer

## **13.5: Backpropagation**

- Backpropagation is an algorithm for training MLPs.
- It uses the error gradient to update the weights and biases of the neurons.
- Key equation:
  - ∂E/∂w = -2 \* z \* (y - y')
  - where E is the error, w is the weight, z is the activation, y is the predicted output, and y' is the actual output.

## **13.6: Types of Learning**

- Supervised learning: training on labeled data
- Unsupervised learning: training on unlabeled data
- Reinforcement learning: training through trial and error

## **Important Formulas and Definitions**

- Activation function: a mathematical function that maps the input to an output value.
- Learning rate: a hyperparameter that controls the rate of weight updates.
- Error gradient: the partial derivative of the error with respect to the weights.
