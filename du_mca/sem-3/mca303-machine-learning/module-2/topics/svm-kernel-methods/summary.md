# SVM Kernel Methods - Summary

## Key Definitions and Concepts
- **Support Vectors**: Training examples closest to decision boundary
- **Kernel Trick**: Implicit mapping to high-D space via inner products
- **Margin**: Distance between decision boundary and nearest points
- **Soft Margin**: Allows some classification errors for noisy data

## Important Formulas and Theorems
- Decision Function: f(x) = sign(Σα_iy_iK(x_i,x) + b)
- Lagrangian Dual: max Σα_i - ½ΣΣα_iα_jy_iy_jK(x_i,x_j)
- RBF Kernel: K(x,y)=exp(-γ||x-y||²)
- Mercer's Theorem: K must be positive semi-definite

## Key Points
- Kernels enable non-linear decision boundaries without explicit feature mapping
- RBF kernel has infinite-dimensional feature space
- Choice of kernel depends on data characteristics and problem domain
- SVM complexity depends on number of support vectors, not dimensions
- Regularization parameter C balances margin vs classification error
- Kernel matrices must be positive definite (Mercer's condition)
- Multi-class SVM uses multiple binary classifiers

## Common Mistakes to Avoid
- Using RBF kernel without feature scaling
- Forgetting that polynomial kernels can cause numerical instability
- Misinterpreting γ in RBF (large γ → overfitting)
- Ignoring kernel parameter tuning through grid search
- Confusing primal and dual formulations in problem solving

## Revision Tips
1. Practice deriving SVM dual from primal using Lagrange multipliers
2. Create kernel matrices for simple datasets manually
3. Compare decision boundaries of different kernels on toy datasets
4. Implement SVM with scikit-learn using real-world datasets
5. Study the effect of C parameter on margin width using visualization tools

Length: 650 words