# Deep Learning - Summary

## Key Definitions and Concepts

- **Deep Learning**: Subset of machine learning using artificial neural networks with multiple hidden layers that automatically learn hierarchical representations from raw data
- **Neural Network**: Computing system inspired by biological neural networks, consisting of interconnected nodes (neurons) organized in layers
- **Convolutional Neural Network (CNN)**: Specialized architecture for processing grid-like data (images) using convolutional layers with learnable filters
- **Recurrent Neural Network (RNN)**: Architecture designed for sequential data processing, maintaining internal state to capture temporal dependencies
- **Backpropagation**: Learning algorithm that computes gradients of loss with respect to network parameters using chain rule
- **Activation Function**: Non-linear function applied to neuron outputs enabling networks to learn complex patterns (ReLU, sigmoid, tanh)
- **Overfitting**: Problem where model learns training data too well including noise, failing to generalize to new data

## Important Formulas and Theorems

- **Forward Propagation**: output = activation(Σ(weight × input) + bias)
- **Cross-Entropy Loss**: L = -Σ y_true × log(y_pred) for classification
- **Gradient Descent Update**: weight_new = weight_old - learning_rate × gradient
- **ReLU Activation**: f(x) = max(0, x)
- **Softmax**: f(x_i) = e^(x_i) / Σ e^(x_j) for multi-class probability distribution

## Key Points

- Deep learning automatically discovers features from raw data, eliminating manual feature engineering required in traditional ML
- The "depth" in deep learning refers to multiple hidden layers enabling hierarchical feature learning
- CNNs excel at image tasks through spatial feature detection via convolutional filters
- RNNs handle sequential data by maintaining memory of previous inputs
- ReLU activation is preferred in modern networks due to avoiding vanishing gradient problem
- Regularization (dropout, L2, batch normalization) prevents overfitting in parameter-rich deep networks
- Modern deep learning requires significant computational resources (GPUs) and large labeled datasets
- Transfer learning allows leveraging pre-trained models for new tasks with limited data

## Common Mistakes to Avoid

- Confusing deep learning with machine learning—deep learning is a subset with distinct characteristics
- Using sigmoid activation in hidden layers—it causes vanishing gradients preventing deep network training
- Neglecting data preprocessing—proper normalization significantly impacts training success
- Training without validation set—always monitor validation accuracy to detect overfitting

## Revision Tips

- Focus on understanding architectural differences between CNNs and RNNs and when to use each
- Memorize the backpropagation concept rather than exact mathematical derivations
- Remember ReLU advantages over older activation functions
- Practice drawing simple neural network architectures and labeling components
- Review how regularization techniques specifically address overfitting in deep networks