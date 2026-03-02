# Deep Learning Overview - Summary

## Key Definitions and Concepts

- **Deep Learning**: Subset of machine learning using artificial neural networks with multiple layers to automatically learn hierarchical representations from data
- **Perceptron**: Single neuron model that computes weighted sum of inputs plus bias, passed through activation function
- **Neural Network**: Interconnected layers of neurons where each layer transforms data until output is produced
- **Forward Propagation**: Process of passing input through network layers to generate predictions
- **Backpropagation**: Gradient-based optimization algorithm computing loss gradients through chain rule
- **Activation Function**: Non-linear function applied to neuron output enabling complex pattern learning
- **Loss Function**: Measures difference between predicted and actual values; guides optimization

## Important Formulas and Theorems

- **Perceptron Output**: f(Σwᵢxᵢ + b) where f is activation
- **Sigmoid**: σ(x) = 1/(1 + e^(-x)), range (0,1)
- **Tanh**: (e^x - e^(-x))/(e^x + e^(-x)), range (-1,1)
- **ReLU**: max(0,x)
- **Cross-Entropy Loss**: -Σy·log(ŷ) for multi-class
- **Weight Update**: w_new = w_old - η × ∂L/∂w
- **Chain Rule**: ∂L/∂w = (∂L/∂a) × (∂a/∂net) × (∂net/∂w)

## Key Points

1. Deep learning excels with large datasets, automatically learning features vs. hand-crafted features in traditional ML
2. Multiple hidden layers enable learning of hierarchical abstractions from raw data
3. ReLU is the default choice for hidden layers due to efficiency and gradient flow
4. CNNs use convolution and pooling for spatial data (images); RNNs for sequential data
5. LSTM networks solve vanishing gradient problem in RNNs through gating mechanisms
6. Dropout randomly deactivates neurons (typically 20-50%) to prevent overfitting
7. Batch normalization normalizes layer inputs, stabilizes training, enables higher learning rates
8. Adam optimizer combines momentum with adaptive learning rates; typically best default choice
9. Vanishing gradient: use ReLU, residual connections; Exploding gradient: use gradient clipping
10. Transformer architecture revolutionized NLP through self-attention mechanism

## Common Mistakes to Avoid

1. **Using sigmoid in hidden layers**: Causes vanishing gradients; use ReLU instead
2. **Forgetting to zero gradients**: Must call optimizer.zero_grad() before backward pass in PyTorch
3. **Setting learning rate too high**: Causes training instability; too low causes slow convergence
4. **Not using validation set**: Cannot detect overfitting without validation monitoring
5. **Ignoring data preprocessing**: Neural networks require normalized/scaled input data for stable training
6. **Using wrong activation for output**: Classification needs softmax (multi-class) or sigmoid (binary), not ReLU

## Revision Tips

1. Practice drawing and explaining neural network architectures for different problem types
2. Implement backpropagation manually for a 2-3 layer network to understand the math
3. Memorize activation function properties: output range, monotonicity, computational cost
4. For each architecture (CNN, RNN, LSTM), note: what it processes, key components, when to use
5. Review PyTorch/TensorFlow syntax for model definition, training loops, and common operations
6. Solve previous year DU exam questions on neural networks and backpropagation