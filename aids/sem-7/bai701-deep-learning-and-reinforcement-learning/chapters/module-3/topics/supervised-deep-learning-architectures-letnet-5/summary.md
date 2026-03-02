# **Supervised Deep Learning Architectures: LetNet-5**

## **Overview**

LetNet-5 is a supervised deep learning architecture proposed by Farahmand et al. in 2012. It is a variant of the traditional LeNet-5 convolutional neural network (CNN) designed for handwritten digit recognition.

## **Key Points**

- **Architecture:**
  - 5 convolutional layers with 6, 16, 32, 64, and 128 neurons respectively
  - 3 fully connected layers with 128, 64, and 10 neurons respectively
  - ReLU activation function
  - Output layer has 10 neurons for handwritten digit recognition
- **Training:**
  - Backpropagation with stochastic gradient descent (SGD) optimization
  - Weight decay and dropout regularizations
  - Learning rate scheduling
- **Theorems and Formulas:**
  - **Backpropagation**: $\frac{\partial L}{\partial W} = -\frac{\partial L}{\partial y} \cdot x^T$
  - **Stochastic Gradient Descent**: $W_{t+1} = W_t - \alpha \cdot \frac{\partial L}{\partial W_t}$
- **Importance:**
  - Introduced dropout regularization to prevent overfitting
  - Improved recognition accuracy on MNIST dataset

## **Revision Notes**

- Understand the architecture and training process of LetNet-5
- Familiarize yourself with backpropagation, SGD, and regularization techniques
- Recall the importance of dropout regularization in preventing overfitting
