# Supervised Deep Learning Architectures: LetNet-5

=============================================

### Introduction

LetNet-5 is a convolutional neural network (CNN) designed for image classification tasks. It was proposed by Crespo et al. in 2012 and is considered a pioneering work in the field of deep learning.

### Key Points

- **Architecture:**
  - 5 layers: convolutional, max pooling, and fully connected
  - Convolutional layers with 96, 256, 384, 384, and 256 filters
  - Max pooling layers with 2x2 kernel size
- **Training:**
  - Random initialization of weights
  - Adam optimizer with learning rate 0.001
  - Cross-entropy loss function
- **Performance:**
  - Achieved 96.1% accuracy on CIFAR-10 dataset

### Important Formulas and Definitions

- **Convolutional Layer:**
  - Output = Σ(f(x - y + 2a) _ x^i _ y^j \* w)
  - f: activation function (e.g., ReLU)
- **Max Pooling Layer:**
  - Output = max(subset of input)
  - subset: kxk window centered at spatial coordinates
- **Activation Function:**
  - ReLU (Rectified Linear Unit): f(x) = max(0, x)
  - f(x) = max(0, x) if x > 0, 0 otherwise

### Theorems and Principles

- **Backpropagation:**
  - Derivative of loss function with respect to weights
  - Backpropagation algorithm: compute gradients of loss function with respect to weights
- **Convolutional Neural Networks:**
  - Composed of convolutional, pooling, and fully connected layers
  - Learn to extract features and represent images in a compact and hierarchical manner

### Revision Tips

- Understand the architecture of LetNet-5 and its components
- Be familiar with the training process and optimization algorithms
- Know the performance metrics and accuracy achieved by LetNet-5

This summary provides a concise overview of the key points, formulas, and theorems related to LetNet-5. It serves as a quick revision guide for students preparing for exams on supervised deep learning architectures.
