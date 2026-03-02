# Kernel Methods and SVM - Summary

## Key Definitions and Concepts

- **Kernel Function**: A symmetric, positive semi-definite function K(x, z) that computes inner products in transformed feature space without explicit transformation
- **Kernel Trick**: Replacing inner products ⟨φ(x), φ(z)⟩ with kernel K(x, z) to enable algorithms to work in high-dimensional spaces efficiently
- **Support Vectors**: Data points with αᵢ > 0 that lie on or within the margin; they alone determine the optimal hyperplane
- **Maximum Margin Classifier**: The hyperplane that maximizes the geometric margin between classes
- **Soft Margin SVM**: Allows some misclassification through slack variables ξᵢ, with C controlling the penalty

## Important Formulas and Theorems

- **Mercer's Theorem**: A symmetric function K is a valid kernel if and only if the Gram matrix is positive semi-definite for all finite datasets
- **RBF Kernel**: K(x, z) = exp(-γ||x - z||²)
- **Polynomial Kernel**: K(x, z) = (γx·z + r)ᵈ
- **SVM Primal**: Minimize (1/2)||w||² + CΣξᵢ subject to yᵢ(w·xᵢ + b) ≥ 1 - ξᵢ
- **SVM Dual**: Maximize Σαᵢ - (1/2)ΣΣαᵢαⱼyᵢyⱼK(xᵢ,xⱼ) subject to Σαᵢyᵢ = 0, αᵢ ≥ 0
- **Decision Function**: f(x) = sign(ΣαᵢyᵢK(x,xᵢ) + b)

## Key Points

1. Kernel methods enable linear algorithms to learn non-linear relationships by implicitly working in high-dimensional feature spaces
2. The RBF kernel maps to infinite dimensions and is the most versatile kernel for general classification problems
3. SVM finds the optimal separating hyperplane that maximizes the margin between classes
4. Only support vectors determine the decision boundary—all other training points can be removed without affecting predictions
5. The parameter C controls the bias-variance tradeoff: large C = complex boundary, small C = simpler boundary
6. For RBF kernel, γ controls locality: large γ = localized, wiggly boundaries; small γ = smooth boundaries
7. SVM training is a convex quadratic optimization problem guaranteeing global optimum
8. Kernelized SVM predictions depend on similarity (kernel value) to support vectors rather than raw distance

## Common Mistakes to Avoid

1. Forgetting that kernels must be positive semi-definite—claiming any function can be a kernel
2. Choosing C without cross-validation—directly using default or arbitrary values
3. Assuming larger γ always improves performance—very large γ causes severe overfitting
4. Ignoring feature scaling—SVM is sensitive to feature scales since it uses distances
5. Applying linear kernel to low-dimensional non-linear data without kernel transformation

## Revision Tips

1. Practice deriving the dual problem from the primal using Lagrangian multipliers
2. Implement simple SVM on 2D data to visualize how different kernels affect decision boundaries
3. Memorize the relationship: small γ → smooth boundary, large γ → complex boundary
4. Remember that support vectors are the critical points—any point with αᵢ = 0 is not a support vector
5. Review the KKT conditions as they are fundamental to understanding SVM optimality
6. Know the computational complexity: training is O(n²) to O(n³), prediction is O(n_sv)