# Introduction to Machine Learning & Deep Learning

## Artificial Intelligence - BSc (Hons) Computer Science (NEP 2024 UGCF)

---

## 1. Introduction and Real-World Relevance

**Machine Learning (ML)** and **Deep Learning (DL)** are subsets of Artificial Intelligence that have revolutionized how computers learn from data and make decisions. While AI encompasses the broader goal of creating intelligent machines, ML provides methods for computers to learn from experience, and DL uses neural networks with many layers to achieve exceptional performance on complex tasks.

### Real-World Applications

| Domain | Application |
|--------|-------------|
| **Healthcare** | Medical image diagnosis, drug discovery, patient outcome prediction |
| **Finance** | Fraud detection, stock market prediction, credit scoring |
| **E-commerce** | Recommendation systems, customer sentiment analysis |
| **Autonomous Vehicles** | Object detection, path planning, traffic sign recognition |
| **Natural Language Processing** | Chatbots, language translation, text summarization |
| **Computer Vision** | Face recognition, quality control in manufacturing |

According to the Delhi University NEP 2024 syllabus, this unit forms the foundation for understanding modern AI systems and prepares students for advanced topics in neural networks and intelligent systems.

---

## 2. What is Machine Learning?

### 2.1 Definition

Machine Learning is the study of algorithms that improve automatically through experience and by the use of data. It enables computers to find hidden insights without being explicitly programmed for specific tasks.

### 2.2 Types of Machine Learning

#### A. Supervised Learning
The algorithm learns from labeled training data (input-output pairs).

- **Classification**: Predicting discrete categories (e.g., spam/not spam)
- **Regression**: Predicting continuous values (e.g., house prices)

**Examples**: Linear Regression, Logistic Regression, Decision Trees, SVM, K-Nearest Neighbors

#### B. Unsupervised Learning
The algorithm learns from unlabeled data to find hidden patterns.

- **Clustering**: Grouping similar data points (e.g., customer segmentation)
- **Dimensionality Reduction**: Reducing features while preserving variance (e.g., PCA)

**Examples**: K-Means Clustering, Hierarchical Clustering, Principal Component Analysis (PCA)

#### C. Reinforcement Learning
An agent learns by interacting with an environment, receiving rewards or penalties.

**Example**: Game-playing AI (Chess, Go), robotics control

---

## 3. Deep Learning: Neural Networks Foundation

### 3.1 What is Deep Learning?

Deep Learning is a specialized subset of machine learning that uses artificial neural networks with multiple layers (hence "deep") to progressively extract higher-level features from raw input.

### 3.2 Biological Inspiration

The perceptron was inspired by the neuron in the human brain:

- **Dendrites**: Receive input signals
- **Cell Body**: Processes information
- **Axon**: Transmits output signal

### 3.3 The Perceptron (Single Layer Neural Network)

A perceptron is the simplest neural network unit:

```
Output = Activation(w₁x₁ + w₂x₂ + ... + wₙxₙ + b)
```

Where:
- `x₁, x₂, ..., xₙ` = Input features
- `w₁, w₂, ..., wₙ` = Weights
- `b` = Bias
- `Activation` = Activation function

### 3.4 Multi-Layer Perceptron (MLP)

An MLP consists of:
- **Input Layer**: Receives features
- **Hidden Layer(s)**: Process information (can be multiple)
- **Output Layer**: Produces final prediction

```
Input → Hidden Layer 1 → Hidden Layer 2 → ... → Output
```

---

## 4. Activation Functions

Activation functions introduce non-linearity, enabling neural networks to learn complex patterns.

### 4.1 Common Activation Functions

| Function | Formula | Use Case |
|----------|---------|----------|
| **Sigmoid** | σ(x) = 1/(1+e⁻ˣ) | Output layer (binary classification) |
| **Tanh** | tanh(x) = (eˣ-e⁻ˣ)/(eˣ+e⁻ˣ) | Hidden layers |
| **ReLU** | f(x) = max(0, x) | Hidden layers (most common) |
| **Leaky ReLU** | f(x) = x if x>0, 0.01x otherwise | Hidden layers (prevents dying ReLU) |
| **Softmax** | e^xᵢ/Σe^xⱼ | Output layer (multi-class) |

### 4.2 Why Non-linearity?

Without non-linear activation functions, stacking multiple layers would be equivalent to a single linear transformation, limiting the network's ability to learn complex relationships.

---

## 5. Deep Learning Architectures

### 5.1 Convolutional Neural Networks (CNNs)

Designed for processing grid-like data (images).

**Key Layers**:
- **Convolutional Layer**: Extracts features using filters
- **Pooling Layer**: Reduces spatial dimensions
- **Fully Connected Layer**: Classification

**Applications**: Image classification, object detection, face recognition

### 5.2 Recurrent Neural Networks (RNNs)

Designed for sequential data processing.

**Key Feature**: Hidden state carries information from previous time steps

**Problem**: Vanishing gradients (long sequences)

### 5.3 Long Short-Term Memory (LSTM)

An advanced RNN that can learn long-term dependencies through gating mechanisms:
- **Input Gate**: Controls what information to store
- **Forget Gate**: Controls what information to discard
- **Output Gate**: Controls what information to output

**Applications**: Time series forecasting, NLP, speech recognition

### 5.4 Generative Adversarial Networks (GANs)

Two networks compete:
- **Generator**: Creates fake samples
- **Discriminator**: Distinguishes real from fake

**Applications**: Image generation, data augmentation, art creation

---

## 6. Common Machine Learning Algorithms

### 6.1 Linear Regression

Predicts continuous values using a linear relationship:

```
y = wx + b
```

**Cost Function**: Mean Squared Error (MSE)

### 6.2 Logistic Regression

Binary classification using sigmoid function:

```
P(y=1|x) = 1/(1 + e^-(wx + b))
```

### 6.3 Decision Trees

Tree-like model making decisions based on feature values.

- **Gini Impurity**: Measures impurity
- **Information Gain**: Entropy reduction

### 6.4 Support Vector Machines (SVM)

Finds optimal hyperplane maximizing margin between classes.

- **Kernel Trick**: Transforms data to higher dimensions

### 6.5 K-Nearest Neighbors (KNN)

Classifies based on majority class of k nearest neighbors.

### 6.6 K-Means Clustering

Unsupervised algorithm partitioning data into k clusters.

**Steps**:
1. Initialize k centroids
2. Assign points to nearest centroid
3. Update centroids
4. Repeat until convergence

---

## 7. Evaluation Metrics

### 7.1 Classification Metrics

| Metric | Formula | When to Use |
|--------|---------|-------------|
| **Accuracy** | (TP + TN)/(TP + TN + FP + FN) | Balanced classes |
| **Precision** | TP/(TP + FP) | Minimize false positives |
| **Recall** | TP/(TP + FN) | Minimize false negatives |
| **F1-Score** | 2×(Precision×Recall)/(Precision+Recall) | Imbalanced classes |
| **AUC-ROC** | Area under ROC curve | Model discrimination ability |

### 7.2 Confusion Matrix

```
                  Predicted
                Positive  Negative
Actual  Positive    TP       FN
       Negative    FP       TN
```

### 7.3 Regression Metrics

- **Mean Absolute Error (MAE)**
- **Mean Squared Error (MSE)**
- **Root Mean Squared Error (RMSE)**
- **R² Score**

---

## 8. Overfitting and Underfitting

### 8.1 Underfitting

The model is too simple to capture patterns in data.

**Symptoms**: High training error, high test error

**Solutions**:
- Increase model complexity
- Add more features
- Train longer

### 8.2 Overfitting

The model memorizes training data but fails on new data.

**Symptoms**: Low training error, high test error

**Solutions**:
- Regularization (L1/L2)
- Dropout (neural networks)
- Early stopping
- Cross-validation
- Data augmentation

### 8.3 Bias-Variance Tradeoff

```
Total Error = Bias² + Variance + Irreducible Error
```

- **High Bias**: Underfitting (too simple)
- **High Variance**: Overfitting (too complex)

---

## 9. Tools and Frameworks

### 9.1 TensorFlow

Open-source by Google, production-ready.

```python
import tensorflow as tf
model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])
```

### 9.2 PyTorch

Open-source by Facebook, research-friendly.

```python
import torch
import torch.nn as nn
class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = nn.Linear(784, 10)
    def forward(self, x):
        return torch.relu(self.fc(x))
```

### 9.3 Keras

High-level API, now integrated with TensorFlow.

### 9.4 Scikit-learn

Traditional ML algorithms.

```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
```

---

## 10. Mathematical Foundations

### 10.1 Linear Algebra

- **Vectors**: Ordered list of numbers
- **Matrices**: 2D array of numbers
- **Dot Product**: u·v = Σuᵢvᵢ
- **Matrix Multiplication**: (A×B)ᵢⱼ = ΣAᵢₖBₖⱼ

### 10.2 Calculus

- **Derivative**: Rate of change
- **Chain Rule**: d/dx[f(g(x))] = f'(g(x))·g'(x)
- **Gradient**: Vector of partial derivatives
- **Optimization**: Finding minimum/maximum

### 10.3 Probability and Statistics

- **Mean, Median, Mode**
- **Standard Deviation, Variance**
- **Probability Distributions**: Normal, Binomial, Poisson
- **Bayes' Theorem**: P(A|B) = P(B|A)·P(A)/P(B)

---

## 11. Practical Examples

### Example 1: Linear Regression with Scikit-learn

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Generate sample data
np.random.seed(42)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Create and train model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Coefficient: {model.coef_[0][0]:.2f}")
print(f"Intercept: {model.intercept_[0]:.2f}")
print(f"MSE: {mse:.4f}")
print(f"R² Score: {r2:.4f}")

# Plot
plt.scatter(X_test, y_test, color='blue', label='Actual')
plt.plot(X_test, y_pred, color='red', label='Predicted')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Linear Regression')
plt.legend()
plt.show()
```

**Output**:
```
Coefficient: 2.98
Intercept: 4.12
MSE: 0.6534
R² Score: 0.93
```

### Example 2: Neural Network with TensorFlow/Keras

```python
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np

# Load Fashion MNIST dataset
(X_train, y_train), (X_test, y_test) = keras.datasets.fashion_mnist.load_data()

# Normalize data
X_train = X_train.astype('float32') / 255.0
X_test = X_test.astype('float32') / 255.0

# Build model
model = keras.Sequential([
    layers.Flatten(input_shape=(28, 28)),
    layers.Dense(256, activation='relu'),
    layers.Dropout(0.3),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.3),
    layers.Dense(10, activation='softmax')
])

# Compile model
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Train model
history = model.fit(
    X_train, y_train,
    epochs=10,
    batch_size=64,
    validation_split=0.1,
    verbose=1
)

# Evaluate
test_loss, test_accuracy = model.evaluate(X_test, y_test)
print(f"\nTest Accuracy: {test_accuracy:.4f}")

# Predictions
predictions = model.predict(X_test)
print(f"First prediction: {np.argmax(predictions[0])}")
```

---

## 12. Multiple Choice Questions

### Level 1: Basic

1. **What is the primary difference between AI, ML, and DL?**
   - (A) They are all the same
   - (B) ML is a subset of AI; DL is a subset of ML
   - (C) AI is a subset of ML
   - (D) None of the above

2. **Which type of machine learning uses labeled data?**
   - (A) Supervised Learning
   - (B) Unsupervised Learning
   - (C) Reinforcement Learning
   - (D) None

3. **What does ReLU stand for?**
   - (A) Rectified Linear Unit
   - (B) Random Linear Unit
   - (C) Recursive Linear Unit
   - (D) Regularized Linear Unit

### Level 2: Intermediate

4. **In a CNN, which layer extracts features from images?**
   - (A) Pooling Layer
   - (B) Convolutional Layer
   - (C) Fully Connected Layer
   - (D) Dropout Layer

5. **What problem does Dropout address?**
   - (A) Underfitting
   - (B) Overfitting
   - (C) Vanishing Gradient
   - (D) None

6. **Which metric is best for imbalanced datasets?**
   - (A) Accuracy
   - (B) Precision
   - (C) F1-Score
   - (D) MSE

7. **What is the purpose of the softmax function?**
   - (A) Feature extraction
   - (B) Dimensionality reduction
   - (C) Multi-class probability distribution
   - (D) Regularization

### Level 3: Advanced

8. **LSTM networks were developed to solve which problem in RNNs?**
   - (A) Overfitting
   - (B) Vanishing/Exploding gradients
   - (C) Computational complexity
   - (D) All of the above

9. **In a confusion matrix, precision is calculated as:**
   - (A) TP/(TP + FN)
   - (B) TP/(TP + FP)
   - (C) (TP + TN)/(Total)
   - (D) FP/(FP + TN)

10. **Which framework is primarily used for research?**
    - (A) TensorFlow
    - (B) PyTorch
    - (C) Scikit-learn
    - (D) All equally

**Answer Key**: 1-B, 2-A, 3-A, 4-B, 5-B, 6-C, 7-C, 8-B, 9-B, 10-B

---

## 13. Flashcards

| # | Term | Definition |
|---|------|------------|
| 1 | Machine Learning | Algorithms that improve automatically through experience |
| 2 | Deep Learning | Neural networks with multiple layers learning hierarchical features |
| 3 | Perceptron | Basic unit of neural network (inspired by biological neuron) |
| 4 | Activation Function | Non-linear function applied to neuron output (ReLU, Sigmoid, Tanh) |
| 5 | CNN | Convolutional Neural Network - best for image processing |
| 6 | RNN | Recurrent Neural Network - processes sequential data |
| 7 | Overfitting | Model memorizes training data, fails on test data |
| 8 | Underfitting | Model too simple to capture data patterns |
| 9 | Gradient Descent | Optimization algorithm to minimize loss function |
| 10 | Backpropagation | Algorithm to train neural networks by computing gradients |
| 11 | Dropout | Regularization technique - randomly drops neurons during training |
| 12 | Epoch | One complete pass through the training dataset |
| 13 | Batch Size | Number of samples processed before updating weights |
| 14 | Learning Rate | Step size in gradient descent optimization |
| 15 | Transfer Learning | Using pre-trained models for new tasks |

---

## 14. Key Takeaways

1. **Machine Learning** enables computers to learn from data without explicit programming, while **Deep Learning** uses neural networks with multiple layers for complex pattern recognition.

2. **Three types of ML**: Supervised (labeled data), Unsupervised (unlabeled data), Reinforcement (reward-based learning).

3. **Neural Networks** consist of input, hidden, and output layers with weights, biases, and activation functions that introduce non-linearity.

4. **Deep Learning Architectures**: CNNs for images, RNNs/LSTMs for sequences, GANs for generation.

5. **Evaluation Metrics**: Accuracy for balanced data; Precision, Recall, F1-Score for imbalanced data; MSE/R² for regression.

6. **Overfitting** is prevented through regularization, dropout, cross-validation, and early stopping.

7. **Popular Frameworks**: TensorFlow (production), PyTorch (research), Scikit-learn (traditional ML).

8. **Mathematical Foundations**: Linear algebra (matrices/vectors), Calculus (derivatives/gradients), Probability (distributions/Bayes theorem).

9. **Real-World Impact**: ML/DL are used in healthcare, finance, autonomous vehicles, NLP, and computer vision.

10. **Practical Skills**: Students should be able to implement basic ML algorithms and neural networks using Python libraries.

---

## 15. Delhi University Syllabus Context (NEP 2024 UGCF)

This study material covers the following modules from the BSc (Hons) Computer Science syllabus:

- **Unit I**: Introduction to AI, ML, and DL - definitions and relationships
- **Unit II**: Neural Networks - perceptron, MLP, activation functions, backpropagation
- **Unit III**: Deep Learning Architectures - CNN, RNN, LSTM, GANs
- **Unit IV**: Machine Learning Algorithms - supervised and unsupervised methods
- **Unit V**: Evaluation and Optimization - metrics, overfitting/underfitting, regularization

**Suggested Practical Work**: Implementation of linear regression, logistic regression, and basic neural networks using Python libraries.

---

*Study Material prepared for BSc (Hons) Computer Science, Delhi University, NEP 2024 UGCF*