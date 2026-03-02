# Neural Networks - Backpropagation - Summary

## Key Definitions and Concepts

- **Backpropagation**: An efficient algorithm that computes gradients of a loss function with respect to neural network weights by propagating error signals backward from output to input layer
- **Forward Pass**: Computation of network output by passing input through layers, applying weighted sums and activation functions
- **Backward Pass**: Propagation of gradients from output to input using chain rule, computing ∂L/∂W for each weight
- **Chain Rule**: Calculus principle (dy/dx = dy/du × du/dx) enabling gradient computation through multiple layers
- **Learning Rate (η)**: Hyperparameter controlling step size in weight updates; determines convergence speed and stability

## Important Formulas and Theorems

- **Weight Update Rule**: W_new = W_old - η × ∂L/∂W
- **Output Layer Error**: δᴸ = ∂L/∂aᴸ ⊙ σ'(zᴸ) (element-wise product)
- **Hidden Layer Error**: δˡ = (Wˡ⁺¹)ᵀδˣ⁺¹ ⊙ σ'(zˡ)
- **Sigmoid Derivative**: σ'(x) = σ(x)(1 - σ(x))
- **ReLU Derivative**: σ'(x) = 1 if x > 0, else 0
- **Tanh Derivative**: σ'(x) = 1 - tanh²(x)
- **MSE Loss**: L = (1/n)Σ(yᵢ - ŷᵢ)²

## Key Points

- Backpropagation makes training deep networks computationally feasible by reducing complexity from exponential to linear in number of weights
- The algorithm requires storing intermediate activations from forward pass for efficient gradient computation during backward pass
- Gradient descent uses computed gradients to iteratively minimize loss by updating weights in the opposite direction of the gradient
- Vanishing gradient problem occurs when derivatives are < 1, causing gradients to shrink exponentially through layers (especially with sigmoid/tanh)
- ReLU activation helps mitigate vanishing gradients due to constant derivative of 1 for positive inputs
- Learning rate is critical: too small yields slow convergence, too large causes oscillation or divergence
- Backpropagation computes gradients but doesn't guarantee global optimum; optimization depends on loss landscape and initialization

## Common Mistakes to Avoid

- Confusing forward pass (prediction) with backward pass (gradient computation)
- Forgetting to apply activation function derivatives when computing δ values
- Not using element-wise multiplication (⊙) when computing gradients through activation functions
- Mixing up the order of matrix multiplication in gradient propagation (Wᵀ vs W)
- Ignoring bias terms in gradient calculations
- Setting learning rate without validation, leading to either non-convergence or oscillation

## Revision Tips

1. **Practice with a simple 2-layer network**: Work through forward and backward passes manually with concrete numbers until the process is automatic
2. **Memorize activation derivatives**: Write them repeatedly until you can derive them instantly—they appear in every backpropagation calculation
3. **Understand the "why"**: Don't just memorize formulas; understand how chain rule connects layers and why gradients propagate backward
4. **Draw the computation graph**: Visualizing how gradients flow helps catch mistakes and understand dependencies
5. **Solve previous year DU questions**: Exam patterns are consistent; practicing actual problems reveals common question styles and expected depth of answers