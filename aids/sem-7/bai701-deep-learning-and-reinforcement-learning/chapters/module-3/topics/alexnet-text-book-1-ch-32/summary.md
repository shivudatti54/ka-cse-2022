# **AlexNet Text Book - 1 : Ch 3.2**

## **Key Points**

- **Convolutional Neural Networks (CNNs)**
  - CNNs are a type of neural network designed to process data with grid-like topology, such as images
  - CNNs work by applying a set of learnable filters (convolutional layers) to the input data
- **Convolutional Layers**
  - A convolutional layer consists of a set of learnable filters that slide over the input data
  - Each filter computes a feature map, which represents the presence of a specific feature at different locations in the input data
- **Activation Functions**
  - Activation functions are used to introduce non-linearity into the model
  - Common activation functions used in CNNs include ReLU (Rectified Linear Unit) and Sigmoid
- **Pooling Layers**
  - Pooling layers reduce the spatial dimensions of the feature maps
  - Pooling layers are used to downsample the feature maps, reducing the number of parameters in the model
- **Dropout**
  - Dropout is a regularization technique that randomly sets a fraction of the neurons to zero during training
  - Dropout helps prevent overfitting by reducing the model's reliance on a single neuron or group of neurons
- **Batch Normalization**
  - Batch normalization is a technique that normalizes the activations of each neuron in the layer
  - Batch normalization helps improve the stability and speed of training in deep networks
- **Recurrent Neural Networks (RNNs)**
  - RNNs are a type of neural network that is designed to work with sequential data, such as time series data or natural language processing data
  - RNNs are composed of a set of interconnected nodes (neurons) that share the same weights

## **Important Formulas, Definitions, and Theorems**

- **Convolutional Filter**: A convolutional filter is a learnable matrix that slides over the input data to compute a feature map
- **ReLU Activation Function**: The ReLU activation function is defined as $f(x) = max(0, x)$, where $x$ is the input to the activation function
- **Dropout Regularization**: Dropout regularization is defined as $L = -\frac{1}{b} \sum_{i=1}^{b} \log p_i$, where $p_i$ is the probability of a neuron being active
- **Batch Normalization Formula**: The batch normalization formula is defined as $x_{norm} = \frac{x - \mu}{\sigma}$, where $x$ is the input to the normalization layer, $\mu$ is the mean of the input data, and $\sigma$ is the standard deviation of the input data

## **Quick Revision Tips**

- Focus on understanding the key concepts and formulas in the chapter
- Practice applying the concepts and formulas to solve problems and build models
- Review the chapter regularly to reinforce your understanding of the material
