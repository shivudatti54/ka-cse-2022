# **Textbook 1: Ch 1.1 – 1.6**

## **1.1 Introduction to Deep Learning**

### Definition

Deep learning is a subfield of machine learning that involves the use of artificial neural networks with multiple layers to analyze data. These networks are inspired by the structure and function of the human brain, with each layer representing a complex processing step.

### History

The concept of deep learning dates back to the 1940s, when Warren McCulloch and Walter Pitts proposed the first artificial neural network. However, it wasn't until the 1980s that the idea of multilayer perceptrons (MLPs) gained popularity. In the 1990s and 2000s, the development of large datasets and computational power enabled researchers to explore the potential of deep learning.

### Key Concepts

- **Artificial neural networks**: networks of interconnected nodes (neurons) that process inputs and produce outputs
- **Multilayer perceptrons (MLPs)**: a type of neural network with multiple layers of nodes
- **Backpropagation**: an algorithm used to train neural networks

### Example

Suppose we want to build a neural network that can recognize handwritten digits. We train the network on a dataset of images of digits, and it learns to recognize patterns in the images. The network consists of multiple layers, each representing a complex processing step.

## **1.2 Neural Networks and Activation Functions**

### Definition

A neural network is a mathematical model that consists of interconnected nodes (neurons) that process inputs and produce outputs.

### Activation Functions

Activation functions are used to introduce non-linearity into the neural network, allowing it to learn complex patterns in the data. Common activation functions include:

- **Sigmoid**: maps input to a value between 0 and 1
- **ReLU (Rectified Linear Unit)**: maps input to 0 if input is negative, and to the input itself if input is non-negative
- **Tanh (Hyperbolic Tangent)**: maps input to a value between -1 and 1

### Example

Suppose we have a neural network with one input node, one hidden layer with 10 nodes, and one output node. We want to use the sigmoid activation function. The output of the input node is 0.5, and the output of the hidden layer is 10. The sigmoid activation function maps the input to a value between 0 and 1, so the output of the output node is 0.5.

## **1.3 Regression and Classification**

### Regression

Regression is a type of neural network that predicts a continuous output variable. For example, predicting house prices based on features such as number of bedrooms and square footage.

### Classification

Classification is a type of neural network that predicts a categorical output variable. For example, classifying images as either "cat" or "dog".

### Example

Suppose we want to build a regression neural network that predicts house prices based on features such as number of bedrooms and square footage. We train the network on a dataset of house prices and features, and it learns to predict prices. The network consists of multiple layers, each representing a complex processing step.

## **1.4 Convolutional Neural Networks (CNNs)**

### Definition

CNNs are a type of neural network that are specifically designed for image and video processing.

### Key Concepts

- **Convolutional layers**: layers that apply filters to small regions of the input image
- **Pooling layers**: layers that downsample the input image
- **Fully connected layers**: layers that connect all nodes in the network

### Example

Suppose we want to build a CNN that can recognize handwritten digits. We train the network on a dataset of images of digits, and it learns to recognize patterns in the images. The network consists of multiple layers, each representing a complex processing step.

## **1.5 Recurrent Neural Networks (RNNs)**

### Definition

RNNs are a type of neural network that are specifically designed for sequential data, such as time series or natural language processing.

### Key Concepts

- **Recurrent connections**: connections that loop back on themselves, allowing the network to use previous information
- **Vanishing gradients**: a problem that occurs when gradients are backpropagated through the network, causing the values to decrease over time

### Example

Suppose we want to build an RNN that can recognize spoken words. We train the network on a dataset of audio recordings of words, and it learns to recognize patterns in the audio. The network consists of multiple layers, each representing a complex processing step.

## **1.6 Types of Neural Networks**

### Definition

Neural networks can be classified into different types based on their architecture and functionality.

### Key Concepts

- **Feedforward networks**: networks where the data flows only in one direction
- **Recurrent networks**: networks where the data flows in a loop
- **Convolutional networks**: networks that are specifically designed for image and video processing

### Example

Suppose we want to build a feedforward neural network that can recognize handwritten digits. We train the network on a dataset of images of digits, and it learns to recognize patterns in the images. The network consists of multiple layers, each representing a complex processing step.
