# **AlexNet Text Book - 1 : Ch 3.2**

## **Convolutional Neural Networks (CNNs)**

### Overview of CNNs

Convolutional Neural Networks (CNNs) are a type of deep learning network designed to process data with grid-like topology, such as images. They are a fundamental component of many computer vision applications, including image classification, object detection, and image segmentation.

### Key Components of CNNs

- **Layers:**
  - Convolutional Layers: Apply filters to the input data to detect local patterns.
  - Activation Layers: Apply non-linear activation functions to the output of the convolutional layers.
  - Pooling Layers: Downsample the feature maps to reduce spatial dimensions.
  - Fully Connected Layers: Convert the feature maps to a one-dimensional representation.
- **Convolutional Layers:**
  - **Filters:** Small, learnable matrices that slide over the input data to detect local patterns.
  - **Stride:** The number of pixels that the filter moves over the input data at each step.
  - **Padding:** The number of pixels that are added to the input data to maintain spatial dimensions.
- **Activation Functions:**
  - **ReLU (Rectified Linear Unit):**
    - F(x) = max(0, x)
    - Useful for hidden layers to introduce non-linearity.
  - **Sigmoid:**
    - F(x) = 1 / (1 + exp(-x))
    - Useful for output layers to produce output between 0 and 1.
- **Pooling Layers:**
  - **Max Pooling:**
    - F(x) = max(x)
    - Reduces spatial dimensions by taking the maximum value in each region.

### Example: AlexNet Architecture

The AlexNet architecture, proposed in the paper "One Million Minutes of Peaceful Skies: A Large-Scale Image Classification Benchmark" by Alex Krizhevsky et al. (2012), is a classic example of a CNN.

- **Convolutional Layers:**
  - 5 layers with 96 filters each, using 11x11 filters with stride 4 and padding 2
  - ReLU activation function
- **Max Pooling Layers:**
  - 3 layers with 3x3 filters, using stride 2
- **Fully Connected Layers:**
  - 2 layers with 4096 and 4096 units, using ReLU activation function
  - Output layer with 1000 units, using Softmax activation function

### Key Takeaways

- CNNs are designed to process data with grid-like topology, such as images.
- Key components of CNNs include convolutional layers, activation layers, pooling layers, and fully connected layers.
- Understanding the architecture of CNNs, such as AlexNet, is essential for building and training effective deep learning models.
