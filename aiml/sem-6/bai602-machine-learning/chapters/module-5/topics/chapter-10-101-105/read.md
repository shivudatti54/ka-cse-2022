# **Chapter-10: Artificial Neural Networks**

### 10.1 Introduction to Artificial Neural Networks

---

Artificial Neural Networks (ANNs) are computational models inspired by the structure and function of biological neurons. ANNs are composed of interconnected nodes or "neurons" that process and transmit information.

**Key Concepts:**

- **Artificial Neural Networks (ANNs)**: ANNs are computational models that mimic the structure and function of biological neurons.
- **Neural Network Architecture**: The arrangement of nodes, edges, and layers in an ANN.
- **Training**: The process of adjusting the weights and biases of the ANN to optimize its performance.

### 10.2 Biological Neurons

---

Biological neurons are the basic building blocks of the human brain. They process and transmit information through electrical and chemical signals.

**Key Concepts:**

- **Biological Neurons**: The basic building blocks of the human brain.
- **Synapses**: The gaps between biological neurons where chemical signals are transmitted.
- **Axons**: The long, thin extensions of biological neurons that transmit signals to other neurons or to muscles or glands.

### 10.3 Artificial Neurons

---

Artificial neurons are the basic building blocks of ANNs. They process and transmit information through electrical and digital signals.

**Key Concepts:**

- **Artificial Neurons**: The basic building blocks of ANNs.
- **Activation Functions**: Mathematical functions that introduce non-linearity into the artificial neuron.
- **Weights and Biases**: Parameters that adjust the strength and direction of the signal transmitted by the artificial neuron.

### 10.4 Perceptron

---

The Perceptron is a type of artificial neuron that can recognize and classify patterns.

**Key Concepts:**

- **Perceptron**: A type of artificial neuron that can recognize and classify patterns.
- **Linear Perceptron**: A Perceptron that uses a linear activation function.
- **Non-Linear Perceptron**: A Perceptron that uses a non-linear activation function.

### 10.5 Learning in Artificial Neural Networks

---

Learning in ANNs occurs through the adjustment of the weights and biases of the network to optimize its performance.

**Key Concepts:**

- **Supervised Learning**: A type of learning where the network is trained on labeled data.
- **Unsupervised Learning**: A type of learning where the network is trained on unlabeled data.
- **Backpropagation**: An algorithm used to adjust the weights and biases of the network during training.

**Example:**

Suppose we have a Perceptron that is trained to recognize handwritten digits. The Perceptron is presented with a set of labeled data, where each label corresponds to the correct digit. The Perceptron adjusts its weights and biases to minimize the error between its predictions and the actual labels. Through this process, the Perceptron learns to recognize the patterns in the data and make accurate predictions.

**Code Example:**

```python
import numpy as np

# Define the Perceptron class
class Perceptron:
    def __init__(self, learning_rate, num_inputs, num_outputs):
        self.learning_rate = learning_rate
        self.num_inputs = num_inputs
        self.num_outputs = num_outputs
        self.weights = np.random.rand(num_inputs, num_outputs)
        self.bias = np.random.rand(num_outputs)

    def predict(self, inputs):
        # Calculate the output of the Perceptron
        outputs = np.dot(inputs, self.weights) + self.bias
        return np.argmax(outputs)

    def train(self, inputs, labels):
        # Calculate the error
        errors = np.argmax(labels) - np.argmax(outputs)

        # Adjust the weights and biases
        self.weights += self.learning_rate * np.dot(inputs.T, errors)
        self.bias += self.learning_rate * np.sum(errors)

# Train the Perceptron
perceptron = Perceptron(learning_rate=0.1, num_inputs=784, num_outputs=10)
inputs = np.random.rand(100, 784)
labels = np.random.randint(0, 10, 100)
perceptron.train(inputs, labels)
```

**Conclusion:**

In this chapter, we have introduced the concept of Artificial Neural Networks and explored the key concepts in detail. We have also seen an example of how a Perceptron can be used to recognize handwritten digits. Understanding these concepts is essential for building and training ANNs, which are a fundamental component of modern machine learning.
