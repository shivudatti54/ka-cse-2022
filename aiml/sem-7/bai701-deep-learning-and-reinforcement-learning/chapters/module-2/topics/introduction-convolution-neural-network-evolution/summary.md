# **Revision Notes: Introduction, Convolution Neural Network, Evolution, Architecture of CNN, Convolution Operation**

### Introduction

- Deep learning is a subfield of machine learning that uses neural networks to analyze data
- Convolutional Neural Networks (CNNs) are a type of deep learning model used for image and signal processing
- Key advantages of CNNs include:
  - Ability to automatically detect features in images
  - Robustness to small transformations (e.g. rotation, scaling)

### Convolution Neural Network

- Definition: A neural network that uses convolutional and pooling layers to extract features from data
- Key components:
  - Convolutional layers
  - Activation functions (e.g. ReLU, Sigmoid)
  - Pooling layers
  - Fully connected layers

### Evolution of Convolution Neural Network

- Early CNNs (1980s-1990s):
  - Proposed by Yann LeCun et al. (1998)
  - Used for image classification and feature extraction
- Modern CNNs (2000s-present):
  - Use more complex architectures (e.g. ResNet, Inception)
  - Incorporate techniques like batch normalization and dropout

### Architecture of CNN

- Basic architecture:
  - Convolutional layer -> Activation function -> Pooling layer -> Flatten layer -> Fully connected layer
- Common architectures:
  - LeNet-5
  - AlexNet
  - VGGNet

### Convolution Operation

- Definition: A mathematical operation that combines two functions (e.g. `f(x)` and `g(x)`) into a new function (e.g. `h(x) = f(x) * g(x)`)

## **Important Formulas and Theorems**

- Convolution theorem:
  - `∇_{x,y} (f(x) * g(x)) = ∇_{x,y} f(x) * ∑_{k} g(x_k) + f(x) * ∇_{x,y} g(x)`
- Backpropagation formula:
  - `∂L/∂w = ∇L/∂z * ∂z/∂w`
- Convolutional layer formula:
  - `y = sum_{i,j} w_{i,j} * f(i, j) * h(i, j)`

Note: This is a concise summary, and there are many more details and nuances to each topic.
