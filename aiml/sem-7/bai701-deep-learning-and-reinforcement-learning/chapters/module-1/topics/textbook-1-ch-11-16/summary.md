# **Textbook 1: Ch 1.1 – 1.6 Revision Notes**

## **Introduction to Deep Learning**

- **Definition:** Deep learning is a subfield of machine learning that uses neural networks with multiple layers to analyze data.
- **Motivation:** Deep learning techniques have achieved state-of-the-art performance in various fields, including computer vision, natural language processing, and speech recognition.

## **Supervised Learning**

- **Definition:** Supervised learning is a type of machine learning where the model learns from labeled data to make predictions on new, unseen data.
- **Types:**
  - **Linear Regression:** y = w^T x + b, where y is the target variable and x is the input feature.
  - **Logistic Regression:** P(y = 1 | x) = σ(w^T x + b), where P is the probability of the positive class and σ is the sigmoid function.

## **Unsupervised Learning**

- **Definition:** Unsupervised learning is a type of machine learning where the model learns from unlabeled data to discover patterns or structure.
- **Types:**
  - **K-Means Clustering:** partitions data into K clusters based on similarity.
  - **Principal Component Analysis (PCA):** reduces dimensionality by selecting the most informative features.

## **Deep Neural Networks**

- **Definition:** A deep neural network is a neural network with multiple layers, each consisting of artificial neurons and edges.
- **Types:**
  - **Feedforward Neural Network:** data flows only in one direction, from input to output.
  - **Convolutional Neural Network (CNN):** designed for image and video processing, uses convolutional and pooling layers.

## **Activation Functions**

- **Definition:** Activation functions introduce non-linearity to the model, allowing it to learn more complex relationships.
- **Types:**
  - **Sigmoid:** σ(x) = 1 / (1 + e^(-x))
  - **ReLU (Rectified Linear Unit):** ReLU(x) = max(0, x)
  - **Tanh (Hyperbolic Tangent):** tanh(x) = 2 / (1 + e^(-2x)) - 1
