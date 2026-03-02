# Kernel Methods & Support Vector Machines

## Introduction
Kernel methods revolutionized machine learning by enabling efficient non-linear classification through implicit feature space transformations. The fundamental insight - that many linear algorithms can be extended to non-linear cases using kernel functions - forms the theoretical foundation of Support Vector Machines (SVMs). These methods are particularly valuable in high-dimensional spaces and remain relevant in modern ML research, especially in domains with complex data structures like bioinformatics and natural language processing.

The importance of kernel methods stems from their ability to handle non-linearly separable data without explicitly computing coordinates in the feature space (kernel trick). SVMs, which maximize the margin between classes, demonstrate superior generalization performance compared to other classifiers. Current research explores adaptive kernel learning, deep kernel networks, and applications in quantum machine learning, maintaining SVMs' relevance in contemporary AI research.

## Key Concepts
1. **Kernel Trick**: Implicit mapping of data to high-dimensional space using kernel functions K(x,y) = φ(x)·φ(y)
2. **Mercer's Theorem**: Characterization of valid kernel functions as positive semi-definite matrices
3. **Hard-Margin SVM**: Optimization problem: min‖w‖² s.t. y_i(w·x_i + b) ≥ 1
4. **Soft-Margin SVM**: Introduces slack variables ξ_i to handle non-separable data
5. **Dual Formulation**: Lagrangian dual reveals kernel applicability: max Σα_i - ½ΣΣα_iα_jy_iy_jK(x_i,x_j)
6. **Reproducing Kernel Hilbert Space (RKHS)**: Theoretical framework for kernel methods
7. **Kernel Types**: 
   - RBF: K(x,y) = exp(-γ‖x-y‖²)
   - Polynomial: K(x,y) = (x·y + c)^d
   - Sigmoid: K(x,y) = tanh(κx·y + θ)

## Examples

**Example 1: XOR Problem with RBF Kernel**
Problem: Classify XOR data {(0,0)→0, (1,1)→0, (1,0)→1, (0,1)→1}

Solution:
1. Choose RBF kernel: K(x,y) = exp(-γ‖x-y‖²), γ=0.5
2. Compute kernel matrix:
   K = [[1, e^{-1}, e^{-0.5}, e^{-0.5}],
        [...symmetric...]]
3. Solve dual SVM problem to find support vectors
4. Decision function: f(x) = sign(Σα_iy_iK(x_i,x) + b)

**Example 2: Text Classification with String Kernel**
Problem: Classify documents using substring features

Solution:
1. Define spectrum kernel: K(s,t) = Σ_{u∈Σ^k} count_u(s)count_u(t)
2. Precompute all k-length substrings (k=3)
3. Compute kernel matrix for documents
4. Train SVM with custom kernel
5. Achieve 92% accuracy on Reuters dataset

## Exam Tips
1. Always write both primal and dual SVM formulations
2. Remember Mercer's condition for valid kernels
3. For non-separable data, discuss slack variables (ξ) and C parameter
4. Practice deriving the dual formulation from primal using Lagrange multipliers
5. Know kernel properties: closure under addition, multiplication, scaling
6. Be prepared to compute kernel matrices for simple datasets
7. Understand RKHS interpretation: ‖f‖² corresponds to regularization