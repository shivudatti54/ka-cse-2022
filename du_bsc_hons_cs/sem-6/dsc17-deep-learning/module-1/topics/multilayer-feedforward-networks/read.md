# Multilayer Feedforward Networks

## A Comprehensive Study Material for BSc (Hons) Computer Science — Delhi University (NEP 2024 UGCF)

---

## 1. Introduction

**Multilayer Feedforward Networks** (also known as **Multilayer Perceptrons** or **MLPs**) form the foundational architecture of deep learning. These are artificial neural networks where information flows in a single direction — from the input layer through one or more hidden layers to the output layer — without any cycles or loops.

In the context of the Delhi University BSc (Hons) Computer Science syllabus (NEP 2024 UGCF), this topic falls under the **Deep Learning** module and carries significant weightage in both theory and practical examinations.

### Real-World Relevance

Multilayer Feedforward Networks power numerous real-world applications:

- **Medical Diagnosis**: Detecting diseases from X-rays, MRI scans, and patient data
- **Financial Forecasting**: Stock price prediction, credit scoring, fraud detection
- **Natural Language Processing**: Text classification, sentiment analysis
- **Computer Vision**: Image recognition, object detection (when combined with convolutions)
- **Recommendation Systems**: Product recommendations on e-commerce platforms
- **Autonomous Vehicles**: Decision-making systems for self-driving cars

---

## 2. Architecture of Multilayer Feedforward Networks

A typical MLP consists of three types of layers:

### 2.1 Input Layer
- Receives the raw features from the dataset
- Each neuron represents one feature
- No computation occurs here; just passes data to the first hidden layer
- Number of neurons = number of input features

### 2.2 Hidden Layer(s)
- One or more layers between input and output
- Perform the actual computation through weighted connections
- Each neuron applies an activation function to the weighted sum of inputs
- **Universal Approximation Theorem**: A single hidden layer with finite neurons can approximate any continuous function

### 2.3 Output Layer
- Produces the final prediction/classification
- Number of neurons depends on the task:
  - **Regression**: 1 neuron (continuous output)
  - **Classification (binary)**: 1 neuron (sigmoid output)
  - **Classification (multi-class)**: N neurons (softmax output)

### 2.4 Network Architecture Notation

```
Input Layer (n features) → Hidden Layer 1 (h1 neurons) → Hidden Layer 2 (h2 neurons) → Output Layer (m outputs)
```

Example: A network with 784 inputs (MNIST images), 2 hidden layers with 256 and 128 neurons, and 10 outputs (digits 0-9):

```
784 → 256 → 128 → 10
```

---

## 3. Mathematical Formulation

### 3.1 Forward Propagation

For a given layer *l*, the computation is:

**Weighted Sum (Pre-activation):**
$$z^{[l]} = W^{[l]} \cdot a^{[l-1]} + b^{[l]}$$

Where:
- $W^{[l]}$ = Weight matrix of layer *l* (shape: $n^{[l]} \times n^{[l-1]}$)
- $a^{[l-1]}$ = Activation from previous layer (shape: $n^{[l-1]} \times 1$)
- $b^{[l]}$ = Bias vector of layer *l* (shape: $n^{[l]} \times 1$)
- $z^{[l]}$ = Pre-activation vector

**Activation (Post-activation):**
$$a^{[l]} = g(z^{[l]})$$

Where $g(\cdot)$ is the activation function.

### 3.2 Loss Functions

**Mean Squared Error (MSE)** — For Regression:
$$L(y, \hat{y}) = \frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2$$

**Cross-Entropy Loss** — For Classification:
$$L(y, \hat{y}) = -\frac{1}{n}\sum_{i=1}^{n}[y_i \log(\hat{y}_i) + (1-y_i)\log(1-\hat{y}_i)]$$

**Categorical Cross-Entropy** — For Multi-class:
$$L(y, \hat{y}) = -\sum_{c=1}^{C} y_{c} \log(\hat{y}_{c})$$

### 3.3 Gradient Descent Update Rule

For weight $w$:
$$w_{new} = w_{old} - \eta \cdot \frac{\partial L}{\partial w}$$

For bias $b$:
$$b_{new} = b_{old} - \eta \cdot \frac{\partial L}{\partial b}$$

Where $\eta$ is the learning rate.

---

## 4. Activation Functions

Activation functions introduce non-linearity, enabling the network to learn complex patterns.

### 4.1 Sigmoid Function
$$\sigma(x) = \frac{1}{1 + e^{-x}}$$
- **Range**: (0, 1)
- **Use**: Output layer for binary classification
- **Drawback**: Vanishing gradient problem

### 4.2 Hyperbolic Tangent (tanh)
$$\tanh(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}}$$
- **Range**: (-1, 1)
- **Advantage**: Zero-centered
- **Drawback**: Still suffers from vanishing gradient

### 4.3 Rectified Linear Unit (ReLU)
$$f(x) = \max(0, x)$$
- **Range**: [0, ∞)
- **Advantages**: Computationally efficient, reduces vanishing gradient
- **Drawback**: Dying ReLU problem (neurons can get stuck at 0)

### 4.4 Leaky ReLU
$$f(x) = \begin{cases} x & \text{if } x > 0 \\ 0.01x & \text{otherwise} \end{cases}$$

### 4.5 Softmax Function
$$\text{Softmax}(x_i) = \frac{e^{x_i}}{\sum_{j=1}^{n} e^{x_j}}$$
- **Use**: Output layer for multi-class classification
- **Property**: Outputs sum to 1 (probability distribution)

---

## 5. The Backpropagation Algorithm

Backpropagation is the cornerstone of training neural networks. It efficiently computes gradients using the **chain rule**.

### 5.1 Algorithm Steps

**Step 1: Forward Pass**
- Compute all layer outputs from input to prediction
- Store intermediate values ($z^{[l]}$, $a^{[l]}$) for backprop

**Step 2: Compute Output Layer Error**
$$\delta^{[L]} = \frac{\partial L}{\partial a^{[L]}} \odot g'(z^{[L]})$$

Where $\odot$ denotes element-wise multiplication.

**Step 3: Backward Pass (Hidden Layers)**
For layer $l$ (going backwards):
$$\delta^{[l]} = (W^{[l+1]})^T \delta^{[l+1]} \odot g'(z^{[l]})$$

**Step 4: Compute Gradients**
$$\frac{\partial L}{\partial W^{[l]}} = \delta^{[l]} (a^{[l-1]})^T$$
$$\frac{\partial L}{\partial b^{[l]}} = \delta^{[l]}$$

**Step 5: Update Weights and Biases**
$$W^{[l]} = W^{[l]} - \eta \cdot \frac{\partial L}{\partial W^{[l]}}$$
$$b^{[l]} = b^{[l]} - \eta \cdot \frac{\partial L}{\partial b^{[l]}}$$

### 5.2 Why Backpropagation Works

The chain rule allows us to propagate error gradients backwards through the network. Each layer's gradient depends on the next layer's gradient, making computation efficient compared to numerical differentiation.

---

## 6. Training Algorithms

### 6.1 Batch Gradient Descent (BGD)
- Uses entire dataset for each gradient update
- Stable convergence but slow for large datasets

### 6.2 Stochastic Gradient Descent (SGD)
- Uses one sample per update
- Fast but noisy convergence

### 6.3 Mini-Batch Gradient Descent
- Uses batches of samples (typically 32, 64, 128)
- Balances speed and stability
- **Standard choice in deep learning**

### 6.4 Momentum
$$v_t = \gamma v_{t-1} + \eta \nabla_\theta J(\theta)$$
$$\theta = \theta - v_t$$

Where $\gamma$ is the momentum coefficient (typically 0.9).

### 6.5 Adam (Adaptive Moment Estimation)
Combines momentum and adaptive learning rates:
- Tracks first moment (mean): $m_t = \beta_1 m_{t-1} + (1-\beta_1) g_t$
- Tracks second moment (variance): $v_t = \beta_2 v_{t-1} + (1-\beta_2) g_t^2$
- Bias correction applied
- **Default choice for most deep learning tasks**

---

## 7. Hyperparameters

### 7.1 Learning Rate (η)
- Controls step size during gradient descent
- Too high: oscillations, divergence
- Too slow: slow convergence
- **Common values**: 0.001, 0.01, 0.1

### 7.2 Number of Hidden Layers
- 1-2 layers: Simple patterns
- Deep networks (3+): Complex patterns (requires deep learning techniques)

### 7.3 Neurons per Hidden Layer
- Rule of thumb: Between input and output size
- Can be tuned via validation

### 7.4 Batch Size
- Smaller: More noisy updates, better generalization
- Larger: Stable updates, requires more memory

### 7.5 Epochs
- Number of complete passes through training data
- Use early stopping to prevent overfitting

### 7.6 Regularization Techniques
- **L2 Regularization (Weight Decay)**: Adds $\frac{\lambda}{2}||w||^2$ to loss
- **Dropout**: Randomly sets neurons to zero during training
- **Batch Normalization**: Normalizes layer inputs

---

## 8. Practical Implementation Example

### Example 1: MLP for XOR Problem

The XOR problem is a classic non-linearly separable pattern that requires a hidden layer.

```python
import numpy as np

# XOR dataset
X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])

y = np.array([[0],
              [1],
              [1],
              [0]])

# Neural Network Architecture
class MLP:
    def __init__(self, input_size, hidden_size, output_size):
        # Xavier initialization
        self.W1 = np.random.randn(input_size, hidden_size) * np.sqrt(2.0 / input_size)
        self.b1 = np.zeros((1, hidden_size))
        self.W2 = np.random.randn(hidden_size, output_size) * np.sqrt(2.0 / hidden_size)
        self.b2 = np.zeros((1, output_size))
    
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-np.clip(x, -500, 500)))
    
    def sigmoid_derivative(self, x):
        return x * (1 - x)
    
    def forward(self, X):
        self.z1 = np.dot(X, self.W1) + self.b1
        self.a1 = self.sigmoid(self.z1)
        self.z2 = np.dot(self.a1, self.W2) + self.b2
        self.a2 = self.sigmoid(self.z2)
        return self.a2
    
    def backward(self, X, y, learning_rate):
        m = X.shape[0]
        
        # Output layer error
        delta2 = (self.a2 - y) * self.sigmoid_derivative(self.a2)
        
        # Gradients for W2 and b2
        dW2 = np.dot(self.a1.T, delta2) / m
        db2 = np.sum(delta2, axis=0, keepdims=True) / m
        
        # Hidden layer error
        delta1 = np.dot(delta2, self.W2.T) * self.sigmoid_derivative(self.a1)
        
        # Gradients for W1 and b1
        dW1 = np.dot(X.T, delta1) / m
        db1 = np.sum(delta1, axis=0, keepdims=True) / m
        
        # Update weights
        self.W2 -= learning_rate * dW2
        self.b2 -= learning_rate * db2
        self.W1 -= learning_rate * dW1
        self.b1 -= learning_rate * db1
    
    def train(self, X, y, epochs, learning_rate):
        for epoch in range(epochs):
            output = self.forward(X)
            self.backward(X, y, learning_rate)
            if (epoch + 1) % 1000 == 0:
                loss = np.mean((y - output) ** 2)
                print(f"Epoch {epoch + 1}, Loss: {loss:.4f}")

# Train the network
mlp = MLP(input_size=2, hidden_size=4, output_size=1)
mlp.train(X, y, epochs=10000, learning_rate=0.5)

# Test
print("\nPredictions:")
print(mlp.forward(X).round(2))
```

### Example 2: MLP for Digit Classification (MNIST-like)

```python
import numpy as np
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

class MLPClassifier:
    def __init__(self, layer_sizes, learning_rate=0.1):
        self.layer_sizes = layer_sizes
        self.learning_rate = learning_rate
        self.weights = []
        self.biases = []
        
        # Initialize weights with Xavier initialization
        np.random.seed(42)
        for i in range(len(layer_sizes) - 1):
            w = np.random.randn(layer_sizes[i], layer_sizes[i+1]) * \
                np.sqrt(2.0 / layer_sizes[i])
            b = np.zeros((1, layer_sizes[i+1]))
            self.weights.append(w)
            self.biases.append(b)
    
    def relu(self, x):
        return np.maximum(0, x)
    
    def relu_derivative(self, x):
        return (x > 0).astype(float)
    
    def softmax(self, x):
        exp_x = np.exp(x - np.max(x, axis=1, keepdims=True))
        return exp_x / np.sum(exp_x, axis=1, keepdims=True)
    
    def forward(self, X):
        self.activations = [X]
        self.z_values = []
        
        current = X
        for i in range(len(self.weights) - 1):
            z = np.dot(current, self.weights[i]) + self.biases[i]
            self.z_values.append(z)
            current = self.relu(z)
            self.activations.append(current)
        
        # Output layer with softmax
        z_out = np.dot(current, self.weights[-1]) + self.biases[-1]
        self.z_values.append(z_out)
        output = self.softmax(z_out)
        self.activations.append(output)
        
        return output
    
    def backward(self, X, y):
        m = X.shape[0]
        num_layers = len(self.weights)
        
        # One-hot encoding
        y_onehot = np.zeros((m, self.layer_sizes[-1]))
        y_onehot[np.arange(m), y] = 1
        
        # Output layer error
        delta = self.activations[-1] - y_onehot
        
        # Backpropagate
        for i in range(num_layers - 1, -1, -1):
            dW = np.dot(self.activations[i].T, delta) / m
            db = np.sum(delta, axis=0, keepdims=True) / m
            
            if i > 0:
                delta = np.dot(delta, self.weights[i].T) * \
                       self.relu_derivative(self.z_values[i-1])
            
            self.weights[i] -= self.learning_rate * dW
            self.biases[i] -= self.learning_rate * db
    
    def train(self, X, y, epochs, batch_size=32):
        n_samples = X.shape[0]
        for epoch in range(epochs):
            # Mini-batch training
            indices = np.random.permutation(n_samples)
            X_shuffled = X[indices]
            y_shuffled = y[indices]
            
            for i in range(0, n_samples, batch_size):
                X_batch = X_shuffled[i:i+batch_size]
                y_batch = y_shuffled[i:i+batch_size]
                self.forward(X_batch)
                self.backward(X_batch, y_batch)
            
            if (epoch + 1) % 10 == 0:
                predictions = np.argmax(self.forward(X), axis=1)
                accuracy = np.mean(predictions == y)
                print(f"Epoch {epoch + 1}, Accuracy: {accuracy:.4f}")
    
    def predict(self, X):
        return np.argmax(self.forward(X), axis=1)

# Load dataset
digits = load_digits()
X, y = digits.data, digits.target

# Preprocessing
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
mlp = MLPClassifier(layer_sizes=[64, 128, 64, 10], learning_rate=0.1)
mlp.train(X_train, y_train, epochs=100, batch_size=32)

# Evaluate
predictions = mlp.predict(X_test)
accuracy = np.mean(predictions == y_test)
print(f"\nTest Accuracy: {accuracy:.4f}")
```

---

## 9. Challenges and Solutions

### 9.1 Overfitting
- **Problem**: Network memorizes training data
- **Solutions**: Dropout, regularization, early stopping, data augmentation

### 9.2 Underfitting
- **Problem**: Network fails to learn training data
- **Solutions**: Increase model capacity, more training, better features

### 9.3 Vanishing Gradient
- **Problem**: Gradients become too small in early layers
- **Solutions**: Use ReLU, residual connections, batch normalization

### 9.4 Exploding Gradient
- **Problem**: Gradients become too large
- **Solutions**: Gradient clipping, proper initialization, lower learning rate

---

## 10. Delhi University Examination Focus Areas

Based on the NEP 2024 UGCF syllabus, students should focus on:

1. **Architecture understanding**: Drawing and explaining MLP diagrams
2. **Mathematical derivations**: Forward propagation formulas, gradient updates
3. **Backpropagation**: Step-by-step computation
4. **Activation functions**: Properties, comparisons, when to use
5. **Hyperparameter tuning**: Impact of learning rate, batch size, epochs
6. **Practical questions**: Given a network architecture, compute outputs

---

## 11. Multiple Choice Questions (Advanced/Application-Based)

### Question 1
In a Multilayer Feedforward Network with 3 input neurons, 4 hidden neurons, and 2 output neurons, what is the total number of learnable parameters (weights + biases)?

- A) 12
- B) 14
- C) 26
- D) 30

**Answer: C) 26**
- Input→Hidden weights: 3 × 4 = 12
- Hidden biases: 4
- Hidden→Output weights: 4 × 2 = 8
- Output biases: 2
- **Total: 12 + 4 + 8 + 2 = 26**

### Question 2
Which activation function is most suitable for the output layer of a multi-class classification neural network?

- A) Sigmoid
- B) ReLU
- C) Tanh
- D) Softmax

**Answer: D) Softmax**

### Question 3
The vanishing gradient problem is most severe when using which activation function?

- A) ReLU
- B) Leaky ReLU
- C) Sigmoid
- D) Softmax

**Answer: C) Sigmoid**

### Question 4
What happens when the learning rate is set too high during training?

- A) The model converges slowly
- B) The model may oscillate or diverge
- C) The model overfits
- D) The model underfits

**Answer: B) The model may oscillate or diverge**

### Question 5
In backpropagation, the chain rule is used to compute:

- A) Forward pass activations
- B) Gradient of loss with respect to weights
- C) Network architecture
- D) Batch size

**Answer: B) Gradient of loss with respect to weights**

### Question 6
Which optimization algorithm combines the benefits of momentum and adaptive learning rates?

- A) SGD
- B) Momentum
- C) Adam
- D) Adagrad

**Answer: C) Adam**

### Question 7
A neural network with zero hidden layers can solve the XOR problem. (True/False)

- A) True
- B) False

**Answer: B) False — XOR is not linearly separable and requires at least one hidden layer**

### Question 8
What is the purpose of dropout in neural networks?

- A) Increase training speed
- B) Reduce overfitting
- C) Initialize weights
- D) Compute gradients

**Answer: B) Reduce overfitting**

### Question 9
If a neural network has 1000 training examples and batch size of 100, how many iterations constitute one epoch?

- A) 10
- B) 100
- C) 1000
- D) 10000

**Answer: A) 10**

### Question 10
The Universal Approximation Theorem states that:

- A) Deep networks are always better than shallow networks
- B) A single hidden layer can approximate any continuous function
- C) Neural networks cannot learn XOR
- D) Backpropagation always converges

**Answer: B) A single hidden layer can approximate any continuous function**

---

## 12. Flashcards for Quick Revision

| Term | Definition |
|------|------------|
| **Multilayer Feedforward Network** | A neural network where information flows in one direction (input → hidden → output) without cycles |
| **Hidden Layer** | Intermediate layer between input and output that performs computation |
| **Forward Propagation** | Process of computing output by passing input through layers |
| **Backpropagation** | Algorithm to compute gradients by propagating error backwards through the network |
| **Activation Function** | Non-linear function applied to weighted sum to introduce non-linearity |
| **Sigmoid** | σ(x) = 1/(1+e^(-x)); Range: (0,1) |
| **ReLU** | max(0,x); Most commonly used hidden layer activation |
| **Softmax** | Exponential normalization; Used for multi-class output |
| **Learning Rate** | Hyperparameter controlling step size in gradient descent |
| **Epoch** | One complete pass through the entire training dataset |
| **Batch Size** | Number of samples processed before parameter update |
| **Momentum** | Technique to accelerate SGD by adding a fraction of previous update |
| **Adam** | Adaptive moment estimation optimizer |
| **Dropout** | Regularization technique: randomly set neurons to zero during training |
| **Xavier Initialization** | Weight initialization method: W ~ N(0, √(2/n_in)) |
| **Vanishing Gradient** | Problem where gradients become too small for early layers to learn |
| **Exploding Gradient** | Problem where gradients become too large causing instability |
| **Loss Function** | Measures difference between predicted and actual values |
| **Universal Approximation** | Theorem: Single hidden layer can approximate any continuous function |
| **Overfitting** | Model memorizes training data; poor generalization |

---

## 13. Key Takeaways

1. **Architecture**: MLPs consist of input, hidden, and output layers with fully connected neurons between adjacent layers.

2. **Forward Propagation**: Information flows from input to output through weighted connections and activation functions.

3. **Activation Functions**: ReLU is preferred for hidden layers; Sigmoid/Softmax for output layers depending on the task.

4. **Backpropagation**: The core algorithm that computes gradients using the chain rule, enabling efficient training.

5. **Training**: Mini-batch gradient descent with Adam optimizer is the standard approach.

6. **Hyperparameters**: Learning rate, batch size, number of layers, and neurons significantly impact performance.

7. **Regularization**: Dropout, L2 regularization, and early stopping help prevent overfitting.

8. **Universal Approximation**: Even a single hidden layer can theoretically solve any complex problem, though deep networks often learn more efficiently.

9. **Implementation**: Libraries like NumPy enable from-scratch implementation; frameworks like TensorFlow/PyTorch simplify production use.

10. **Exam Preparation**: Focus on understanding mathematical formulations, being able to draw network diagrams, and solving numerical problems on backpropagation and gradient updates.

---

*Study Material prepared for BSc (Hons) Computer Science, Delhi University (NEP 2024 UGCF)*