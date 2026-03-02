# **Revision Notes: Introduction, Convolution Neural Network, Evolution of Convolution Neural Network, Architecture of CNN, Convolution Operation**

### Introduction

- **Definition:** Deep learning is a subset of machine learning that uses neural networks with multiple layers to learn complex patterns in data.
- **Key Concepts:**
  - Supervised learning
  - Unsupervised learning
  - Reinforcement learning
- **Important Theorems:**
  - Central Limit Theorem
  - No Free Lunch Theorem

### Convolution Neural Network (CNN)

- **Definition:** A type of neural network designed to process data with grid-like topology, such as images.
- **Key Components:**
  - Convolutional layers
  - Activation functions
  - Pooling layers
- **Convolution Operation:**
  - Definition: Cross-correlation between a kernel and input feature map
  - Formula: `y[i, j] = sum(kernels[k][i + k][j + k] * inputs[i + k][j + k])`
- **Types of Convolution:**
  - 2D convolution
  - 3D convolution
- **Importance:**
  - Image recognition
  - Object detection
  - Image classification

### Evolution of Convolution Neural Network

- **Early Works:**
  - Yann LeCun's convolutional neural network (CNN)
  - Alex Net
- **Key Innovations:**
  - ReLU activation function
  - Data augmentation
  - Batch normalization
- **Modern CNN Architectures:**
  - Residual learning
  - Dense connectivity

### Architecture of CNN

- **Component Layers:**
  - Convolutional layers
  - Activation functions
  - Pooling layers
  - Flattening layer
- **Architecture Patterns:**
  - Dense layers
  - Convolutional layers
- **Common Architectures:**
  - LeNet
  - Alex Net
  - VGG Net

### Convolution Operation

- **Definition:** Cross-correlation between a kernel and input feature map
- **Mathematical Representation:**
  - `y[i, j] = sum(kernels[k][i + k][j + k] * inputs[i + k][j + k])`
- **Properties:**
  - Translation-invariance
  - Shift-invariance
