# Difficulty of Training Deep Neural Networks - Summary

## Key Definitions and Concepts

- **Vanishing Gradients**: Problem where gradients become exponentially small as they propagate backward through many layers, preventing early layers from learning.

- **Exploding Gradients**: Problem where gradients become exponentially large during backpropagation, causing unstable training and numerical overflow.

- **Internal Covariate Shift**: The change in input distribution to a network layer as preceding layers adapt during training, forcing continuous relearning.

- **Saddle Points**: Critical points where gradients vanish but the function is neither a maximum nor minimum—a major challenge in high-dimensional optimization.

- **Batch Normalization**: Technique that normalizes layer inputs to zero mean and unit variance, then learns scale and shift parameters to restore representation capacity.

## Important Formulas and Theorems

- **Xavier Initialization**: Weight variance = 2/(n_in + n_out) for tanh, or 1/n_in for sigmoid
- **He Initialization**: Weight variance = 2/n_in (specifically for ReLU)
- **Batch Norm Transform**: yᵢ = γ((xᵢ - μB)/√(σ²B + ε)) + β
- **Gradient multiplier through L layers**: Product of weight variances and activation derivatives

## Key Points

- Vanishing gradients occur because sigmoid/tanh derivatives are always ≤ 0.25, and repeated multiplication amplifies this exponentially through depth.

- Residual connections (skip connections) create alternative gradient paths that bypass layers, enabling training of much deeper networks.

- Batch normalization reduces internal covariate shift by normalizing inputs, allowing higher learning rates and faster convergence.

- ReLU activations have constant derivative of 1 for positive inputs, mitigating vanishing gradients but introducing the "dying ReLU" problem.

- Proper weight initialization (Xavier/He) sets weight variance based on network architecture to prevent signal explosion or vanishing in forward pass.

- Adaptive optimizers (Adam, RMSprop) help navigate flat regions and plateaus that are common in deep network loss landscapes.

- The dying ReLU problem can be addressed using Leaky ReLU, ELU, or SELU activations that allow small gradients for negative inputs.

## Common Mistakes to Avoid

- Using sigmoid activation in deep networks without understanding its gradient properties
- Applying batch statistics (from training) at inference time instead of running statistics
- Assuming local minima are the primary optimization challenge—in high dimensions, saddle points are more problematic
- Using Xavier initialization for ReLU networks (should use He initialization instead)
- Setting learning rate too high when training deep networks without normalization techniques

## Revision Tips

1. Draw the gradient flow diagram for a 5-layer network and calculate approximate gradient attenuation with sigmoid derivatives.

2. Implement batch normalization from scratch, including the distinction between training and inference modes.

3. Compare training dynamics (convergence speed, final accuracy) with and without batch normalization on a simple deep network.

4. Memorize why He initialization uses √(2/n_in) while Xavier uses √(1/n_in)—the factor of 2 accounts for ReLU zeroing half the inputs.

5. Practice identifying which training difficulty (vanishing gradients, internal covariate shift, plateaus) explains observed symptoms like loss not decreasing or gradients being near zero.