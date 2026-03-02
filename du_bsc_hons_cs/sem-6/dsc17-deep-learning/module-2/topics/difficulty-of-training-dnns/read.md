# Difficulty of Training Deep Neural Networks

## Introduction

Training Deep Neural Networks (DNNs) presents significant challenges that distinguish them from traditional machine learning algorithms. While shallow networks with fewer layers can often be trained using gradient-based optimization relatively easily, adding more layers introduces fundamental difficulties that can make training unstable or even impossible. These challenges have historically limited the depth of neural networks, which is why early neural networks remained shallow despite theoretical evidence that deeper networks should be more powerful.

The difficulties in training DNNs arise from multiple interconnected factors: gradients can become extremely small (vanishing) or extremely large (exploding) as they propagate through many layers; the optimization landscape becomes highly non-convex with countless local minima and saddle points; and the distribution of inputs to each layer shifts as network parameters change during training, a phenomenon known as internal covariate shift. Understanding these challenges is essential for any deep learning practitioner, as it explains why sophisticated architectural choices and training techniques are necessary to build effective deep models.

This topic is particularly important for the DU Computer Science curriculum because it provides the theoretical foundation for understanding why modern deep learning works. Students must grasp these difficulties not only to debug training issues but also to appreciate the elegant solutions—batch normalization, residual connections, proper initialization—that make deep learning practical.

## Key Concepts

### Vanishing and Exploding Gradients

The most fundamental challenge in training deep networks is the vanishing and exploding gradient problem. When backpropagating errors through many layers, the gradient signal can diminish exponentially (vanishing) or grow exponentially (exploding). Consider a simple network where each layer applies a weight matrix W and an activation function. The gradient at the earliest layers involves repeated multiplication of weight matrices:

∂E/∂W₁ = (∂E/∂aₙ)(∂aₙ/∂aₙ₋₁)...(∂a₂/∂a₁)(∂a₁/∂W₁)

If the spectral radius (largest absolute eigenvalue) of the weight matrices is less than 1, gradients shrink exponentially with depth. If greater than 1, they grow exponentially. This makes it impossible to tune early layers effectively—their weights barely change regardless of the error at the output.

### Internal Covariate Shift

When the parameters of a layer change during training, the distribution of its inputs (which come from previous layers) also changes. This phenomenon, termed internal covariate shift by Ioffe and Szegedy (2015), forces each layer to continuously adapt to new input distributions. This is problematic because neural networks assume input distributions to be stationary (as in traditional machine learning). When input distributions shift, layers must learn to compensate, slowing training significantly and requiring lower learning rates.

### Non-Convex Optimization Landscape

The loss landscape of deep neural networks is extraordinarily complex. Unlike convex problems with a single global minimum, deep networks have countless local minima, saddle points, and flat regions. While some research suggests that local minima in high dimensions may be close to global minima in terms of loss, the presence of saddle points—where gradients vanish in all directions but some directions curve upward while others curve downward—can trap optimization algorithms. The prevalence of saddle points increases dramatically in higher dimensions, making them a significant challenge for deep networks.

### Activation Function Considerations

The choice of activation function profoundly impacts trainability. The sigmoid and tanh activations, while historically popular, contribute to vanishing gradients because their derivatives are always less than 1 (and near 0 for large inputs). When a neuron saturates (output close to 0 or 1 for sigmoid), the gradient through that neuron becomes nearly zero, effectively "killing" learning in that pathway. The ReLU activation function addresses this by having a constant derivative of 1 for positive inputs, but it introduces its own problem: the "dying ReLU" issue where neurons permanently output zero if their weighted sum is ever negative.

### Weight Initialization

Proper weight initialization is crucial for training stability. If weights are too small, signals vanish as they propagate forward. If too large, signals explode. The Xavier initialization (for sigmoid/tanh) and He initialization (for ReLU) provide theoretically grounded starting points by setting variance based on layer dimensions. Even with proper initialization, very deep networks can still experience gradient issues, necessitating additional techniques.

### Plateaus and Slow Convergence

Deep networks often encounter flat regions where gradients are small but non-zero, leading to extremely slow progress. These plateaus can occur due to the network learning coarse features first before refining them, or simply because the optimization landscape contains vast flat regions. Adaptive learning rate methods like Adam help navigate these regions more effectively than vanilla SGD.

## Examples

### Example 1: Demonstrating Vanishing Gradients

Consider a 10-layer network with sigmoid activations, all weights initialized from a standard normal distribution. Suppose we're trying to classify a simple pattern. Calculate the effective learning signal reaching layer 1:

For sigmoid: σ'(x) = σ(x)(1 - σ(x)), maximum value = 0.25
With weight variance = 1: average gradient multiplier ≈ (0.25 × 1)¹⁰ ≈ 9.5 × 10⁻⁷

The gradient reaching layer 1 is approximately one-millionth of the gradient at layer 10. This explains why early layers train extremely slowly—almost any meaningful signal is lost. To fix this, we can use ReLU activations (derivative = 1 for positive inputs) or residual connections that provide direct paths for gradient flow.

### Example 2: Internal Covariate Shift in Practice

Suppose a network layer receives inputs with mean = 0, std = 1 during initialization. After some training, the previous layer's weights might shift outputs to mean = 5, std = 3. This layer's neurons, designed for inputs in [-1, 1], now operate in the saturated region of their activation function, producing very small gradients. Batch normalization addresses this by normalizing layer inputs to have zero mean and unit variance, then learning scale and shift parameters to restore representation capacity.

### Example 3: Batch Normalization Computation

Given a mini-batch with values B = {x₁, x₂, ..., xₘ}, batch normalization transforms them as follows:

1. Compute batch mean: μB = (1/m)Σxᵢ
2. Compute batch variance: σ²B = (1/m)Σ(xᵢ - μB)²
3. Normalize: x̂ᵢ = (xᵢ - μB) / √(σ²B + ε)
4. Scale and shift: yᵢ = γx̂ᵢ + β

The parameters γ (scale) and β (shift) are learnable, allowing the network to recover any representation power lost through normalization. During inference, running statistics (moving averages from training) replace batch statistics.

## Exam Tips

1. **Remember the core cause**: Vanishing gradients occur because derivatives of sigmoid/tanh are < 1, and repeated multiplication amplifies this effect exponentially with depth.

2. **Know solutions to each problem**: Vanishing gradients → ReLU, residual connections; Internal covariate shift → Batch normalization; Plateaus → Adam/adaptive methods; Dying ReLU → Leaky ReLU, ELU.

3. **Explain why residual connections work**: They create "shortcut paths" allowing gradients to flow directly to earlier layers, making the effective network depth less relevant for gradient propagation.

4. **Understand batch normalization at inference**: It uses running statistics (moving averages computed during training), not batch statistics, making predictions deterministic.

5. **Differentiate initialization schemes**: Xavier uses √(1/n) or √(2/(n_in + n_out)) for variance; He initialization uses √(2/n_in) specifically for ReLU networks.

6. **Internal covariate shift impacts**: It causes each layer to constantly adapt to changing input distributions, requiring lower learning rates and leading to slower convergence.

7. **Saddle points vs. local minima**: In high dimensions, saddle points are more prevalent than local minima; gradient-based methods can escape saddle points but may get stuck in flat regions.