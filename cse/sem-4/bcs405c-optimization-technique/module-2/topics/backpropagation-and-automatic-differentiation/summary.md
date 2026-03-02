# Backpropagation - Summary

## Key Concepts

- Forward pass: input → output
- Backward pass: compute gradients using chain rule
- ∂E/∂w = ∂E/∂a × ∂a/∂z × ∂z/∂w

## Automatic Differentiation

- Forward mode: input → output
- Reverse mode: output → input (preferred for neural networks)

## Exam Tips

1. Remember: Forward then Backward passes
2. Chain rule is the foundation
3. Loss propagates backwards through layers
4. Exact derivatives (not numerical approximation)
