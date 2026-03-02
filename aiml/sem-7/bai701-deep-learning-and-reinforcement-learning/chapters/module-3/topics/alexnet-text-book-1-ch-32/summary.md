# **AlexNet Text Book - 1 : Ch 3.2**

## **Key Points**

- **Convolutional Neural Networks (CNNs)**:
  - Design for image processing tasks
  - Utilize convolutions and pooling layers
- **AlexNet Architecture**:
  - 5 convolutional and 3 fully connected layers
  - Max pooling layers
  - ReLU activation function
- **Activation Functions**:
  - ReLU (Rectified Linear Unit): f(x) = max(0, x)
  - Sigmoid: f(x) = 1 / (1 + e^(-x))
  - Tanh: f(x) = 2 / (1 + e^(-2x)) - 1
- **Backpropagation**:
  - Algorithm for computing gradients
  - Used for training neural networks

## **Important Formulas**

- **Convolutional Layer**:
  - Output: ∑[a(i) \* f(k(i)) \* h(i-j)]
  - where a(i) is filter, f(k(i)) is feature map, h(i) is input, and j is convolutional stride
- **ReLU Activation Function**:
  - f(x) = max(0, x)
- **Gradient Descent**:
  - Update rule: θ = θ - α \* ∇L/∇θ
  - where α is learning rate, θ is weight, and ∇L/∇θ is gradient of loss function

## **Theorems**

- **Chain Rule**:
  - ∂(f ∘ g)/∂x = ∂f/∂y \* ∂g/∂x
- **Backpropagation**:
  - ∂L/∂w = ∂L/∂y \* ∂y/∂w
