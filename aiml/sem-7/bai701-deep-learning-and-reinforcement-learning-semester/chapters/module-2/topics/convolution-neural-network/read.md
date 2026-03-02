# Neural Network Basics

## What is a Neural Network?
A neural network is a computational model inspired by biological neurons, consisting of interconnected nodes (neurons) organized in layers. Each neuron receives inputs, applies weights and a bias, then passes the result through an activation function.

## Key Concepts

### The Artificial Neuron (Perceptron)
A single neuron computes:
```
output = activation(sum(weights * inputs) + bias)
       = activation(w1*x1 + w2*x2 + ... + wn*xn + b)
```

**Components:**
- **Inputs (x)**: Features from data or previous layer
- **Weights (w)**: Learnable parameters controlling input importance
- **Bias (b)**: Allows shifting the activation threshold
- **Activation**: Non-linear function enabling complex mappings

### Network Architecture

#### Layer Types
| Layer | Description |
|-------|-------------|
| Input Layer | Receives raw features (no computation) |
| Hidden Layers | Intermediate processing layers |
| Output Layer | Produces final predictions |

#### Fully Connected (Dense) Layers
- Every neuron connects to all neurons in the previous layer
- Parameters: (input_size * output_size) weights + output_size biases
- Example: 100 inputs to 50 outputs = 5,050 parameters

### Forward Propagation
The process of computing output from input:

```
For each layer l:
    z[l] = W[l] * a[l-1] + b[l]    # Linear transformation
    a[l] = activation(z[l])        # Non-linear activation
```

Where:
- `a[0]` = input X
- `a[L]` = final output (predictions)

## Mathematical Representation

### Single Layer Computation
```
Input:  X ∈ R^(n x m)       # n features, m samples
Weight: W ∈ R^(h x n)       # h neurons in layer
Bias:   b ∈ R^(h x 1)       # one bias per neuron
Output: A = σ(W·X + b)      # σ is activation function
```

### Matrix Dimensions Through Network
```
Input:     (784, batch_size)  # 28x28 image flattened
Layer 1:   (128, batch_size)  # 128 neurons
Layer 2:   (64, batch_size)   # 64 neurons
Output:    (10, batch_size)   # 10 classes
```

## Network Design Choices

### Width vs Depth
- **Width**: Number of neurons per layer
- **Depth**: Number of layers
- Deeper networks can represent hierarchical features
- Wider networks may need fewer layers for same capacity

### Common Architectures
| Type | Structure | Use Case |
|------|-----------|----------|
| MLP | Input → Hidden(s) → Output | Tabular data, regression |
| CNN | Conv → Pool → FC | Images, spatial data |
| RNN | Recurrent connections | Sequences, time series |

## Capacity and Expressiveness

### Parameter Count
Total parameters in a network:
```
params = Σ(layer_i_neurons * layer_i-1_neurons + layer_i_neurons)
       = Σ(weights + biases)
```

### Example: Simple MLP
- Input: 784 (28x28 image)
- Hidden: 256 neurons
- Output: 10 classes
- Parameters: (784×256 + 256) + (256×10 + 10) = 203,530

## Summary

- Neural networks consist of layers of connected neurons
- Each neuron computes weighted sum plus bias, then applies activation
- Forward propagation flows from input to output layer
- Network capacity determined by width, depth, and connectivity
- Dense/fully-connected layers connect every neuron to all previous neurons
