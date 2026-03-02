# Loss Functions

## What are Loss Functions?
A loss function (also called cost function or objective function) measures how well a neural network's predictions match the true labels. Training minimizes this loss to improve model accuracy. The choice of loss function depends on the task type.

## Key Concepts

### Loss vs Cost
- **Loss**: Error for a single training example
- **Cost**: Average loss over the entire training set
```
Cost = (1/m) * Σ Loss(y_i, ŷ_i)
```

### Desirable Properties
1. **Differentiable**: Enables gradient-based optimization
2. **Convex** (ideally): Single global minimum
3. **Bounded below**: Has a minimum value (often 0)
4. **Appropriate scale**: Gradients should be informative

## Regression Loss Functions

### Mean Squared Error (MSE)
```
MSE = (1/n) * Σ(y_i - ŷ_i)²
```
- **Properties**: Penalizes large errors heavily (quadratic)
- **Gradient**: 2(ŷ - y), smooth everywhere
- **Use Case**: Standard regression tasks
- **Sensitivity**: Very sensitive to outliers

### Mean Absolute Error (MAE)
```
MAE = (1/n) * Σ|y_i - ŷ_i|
```
- **Properties**: Linear penalty, robust to outliers
- **Gradient**: sign(ŷ - y), discontinuous at 0
- **Use Case**: Regression with outliers
- **Trade-off**: Less sensitive but harder to optimize

### Huber Loss
```
Huber = { 0.5*(y-ŷ)²           if |y-ŷ| ≤ δ
        { δ*|y-ŷ| - 0.5*δ²     otherwise
```
- **Properties**: MSE for small errors, MAE for large errors
- **Use Case**: Best of both worlds for regression

## Classification Loss Functions

### Binary Cross-Entropy (Log Loss)
```
BCE = -[y*log(ŷ) + (1-y)*log(1-ŷ)]
```
- **Range**: [0, ∞), 0 is perfect
- **Properties**: Penalizes confident wrong predictions heavily
- **Use Case**: Binary classification
- **Activation**: Use with sigmoid output

### Categorical Cross-Entropy
```
CCE = -Σ(y_i * log(ŷ_i))
```
- **Properties**: Generalizes BCE to multi-class
- **Use Case**: Multi-class classification (one-hot labels)
- **Activation**: Use with softmax output

### Sparse Categorical Cross-Entropy
- Same as CCE but labels are integers, not one-hot
- More memory efficient for many classes

## Loss Function Comparison

| Loss | Task | Formula | Outlier Sensitivity |
|------|------|---------|---------------------|
| MSE | Regression | (y-ŷ)² | High |
| MAE | Regression | |y-ŷ| | Low |
| Huber | Regression | Hybrid | Medium |
| BCE | Binary Class | -[y log(ŷ) + ...] | N/A |
| CCE | Multi-class | -Σ y_i log(ŷ_i) | N/A |

## Why Cross-Entropy for Classification?

### Information Theory Connection
- Cross-entropy measures "surprise" between distributions
- Low when predicted distribution matches true distribution
- Related to KL divergence: CE(p,q) = H(p) + KL(p||q)

### Gradient Properties
For softmax + cross-entropy:
```
∂L/∂z_i = ŷ_i - y_i
```
- Clean gradient: prediction minus target
- No vanishing gradients from softmax saturation

### Why Not MSE for Classification?
- MSE with sigmoid creates flat gradients when confident and wrong
- Cross-entropy maintains strong gradients for wrong predictions

## Advanced Loss Functions

### Focal Loss (Object Detection)
```
FL = -α(1-ŷ)^γ * log(ŷ)
```
- Focuses on hard examples
- Used in RetinaNet for class imbalance

### Contrastive Loss (Similarity Learning)
```
L = y*d² + (1-y)*max(0, margin-d)²
```
- Pulls similar pairs together, pushes dissimilar apart

### Triplet Loss
```
L = max(0, d(a,p) - d(a,n) + margin)
```
- Anchor-positive closer than anchor-negative

## Summary

- Loss functions measure prediction-target mismatch
- MSE for regression, cross-entropy for classification
- Cross-entropy has better gradient properties for classification
- Choice depends on task, data characteristics, and problem specifics
- Advanced losses address class imbalance, similarity learning
