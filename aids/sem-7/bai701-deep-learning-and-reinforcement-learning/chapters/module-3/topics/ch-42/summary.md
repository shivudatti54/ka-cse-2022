# **Ch 4.2 Revision Notes**

## **Overview**

- This chapter focuses on **Training Supervised Deep Learning Networks**, specifically on techniques for improving the performance of deep neural networks in supervised learning settings.

## **Key Concepts**

- **Supervised Learning**:
  - Definition: Training model on labeled data to predict outputs
  - Types: Regression, Classification
- **Deep Learning**:
  - Definition: Neural networks with multiple hidden layers
  - Characteristics: Non-linear, parallel, and distributed representations
- **Convolutional Neural Networks (CNNs)**:
  - Definition: Neural networks with convolutional and pooling layers for image processing
  - Applications: Image classification, object detection, segmentation
- **Recurrent Neural Networks (RNNs)**:
  - Definition: Neural networks with feedback connections for sequential data
  - Applications: Natural Language Processing (NLP), speech recognition
- **Transfer Learning**:
  - Definition: Using pre-trained models as a starting point for new tasks
  - Benefits: Reduced training time, improved performance

## **Formulas and Definitions**

- **Activation Functions**:
  - ReLU (Rectified Linear Unit): f(x) = max(0, x)
  - Sigmoid: f(x) = 1 / (1 + e^(-x))
  - Tanh: f(x) = 2 / (1 + e^(-2x)) - 1
- **Batch Normalization**:
  - Definition: Normalizing inputs to each layer to reduce internal covariate shift
  - Formula: μ = E[x], σ = sqrt(Var[x])
- **Dropout**:
  - Definition: Randomly dropping out neurons during training to prevent overfitting
  - Formula: p = 1 - dropout_rate

## **Theorems and Important Results**

- **No Free Lunch Theorem**:
  - No algorithm can outperform all other algorithms in all situations
- **Overfitting**:
  - Occurs when model is too complex and fits training data too well
  - Can be mitigated using regularization, dropout, and early stopping
- **Underfitting**:
  - Occurs when model is too simple and fails to capture training data
  - Can be mitigated using regularization and increasing model capacity
