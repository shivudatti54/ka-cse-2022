# Essential Mathematics for Multivariate Data

## Introduction

Machine learning algorithms operate on multivariate data—datasets with multiple features observed across multiple instances. The mathematical foundations enabling these algorithms span three domains: **linear algebra** for data representation and transformation, **calculus** for optimization, and **probability theory** for reasoning under uncertainty. This study material develops the rigorous mathematical framework required for understanding multivariate statistical methods and advanced machine learning techniques.

## 1. Linear Algebra Foundations

### 1.1 Vector Spaces and Operators

A **vector space** V over ℝ is a collection of objects (vectors) closed under addition and scalar multiplication. For ML applications, we work primarily with ℝ^n—the space of n-dimensional real column vectors.

**Definition 1.1 (Vector):** A vector x ∈ ℝ^n is an ordered n-tuple x = (x₁, x₂, ..., xₙ)^T representing a point or direction in n-dimensional space.

**Definition 1.2 (Dot Product):** Given x, y ∈ ℝ^n, the dot product is defined as:
$$x \cdot y = \sum_{i=1}^{n} x_i y_i = x^T y$$

**Theorem 1.1 (Cauchy-Schwarz Inequality):** For any x, y ∈ ℝ^n:
$$|x^T y| \leq \|x\| \|y\|$$
**Proof:** Consider the quadratic polynomial p(t) = \|tx + y\|^2 = t^2\|x\|^2 + 2t(x^T y) + \|y\|^2 ≥ 0 for all t ∈ ℝ. The discriminant must be non-positive:
$$(x^T y)^2 - \|x\|^2 \|y\|^2 \leq 0$$
Rearranging yields the desired inequality. ∎

**Definition 1.3 (Norm):** The Euclidean norm is $\|x\| = \sqrt{x^T x}$. The Cauchy-Schwarz inequality immediately yields the triangle inequality: $\|x + y\| \leq \|x\| + \|y\|$.

### 1.2 Matrix Algebra

A **matrix** A ∈ ℝ^{m×n} is a rectangular array with m rows and n columns. In ML, we represent a dataset with n observations and p features as X ∈ ℝ^{n×p}.

**Definition 1.4 (Matrix Multiplication):** For A ∈ ℝ^{m×n} and B ∈ ℝ^{n×p}, the product C = AB ∈ ℝ^{m×p} is defined as:
$$c_{ij} = \sum_{k=1}^{n} a_{ik} b_{kj}$$
This represents applying the linear transformation B followed by A.

**Theorem 1.2 (Transpose Properties):** For matrices A, B of appropriate dimensions:

1. $(A^T)^T = A$
2. $(AB)^T = B^T A^T$
3. $(A + B)^T = A^T + B^T$

**Proof of (2):** Let C = AB. Then $c_{ij} = \sum_k a_{ik} b_{kj}$. The (i,j)-entry of $(AB)^T$ is $c_{ji} = \sum_k a_{jk} b_{ki}$. The (i,j)-entry of $B^T A^T$ is $\sum_k (B^T)_{ik} (A^T)_{kj} = \sum_k b_{ki} a_{jk} = \sum_k a_{jk} b_{ki}$. These are identical. ∎

### 1.3 Matrix Inverse and Determinant

**Definition 1.5 (Inverse):** A square matrix A ∈ ℝ^{n×n} is **invertible** (non-singular) if there exists A⁻¹ ∈ ℝ^{n×n} such that $AA^{-1} = A^{-1}A = I_n$, where I is the identity matrix.

**Theorem 1.3 (Determinant and Invertibility):** A square matrix A is invertible if and only if det(A) ≠ 0.

**Proof:** The determinant characterizes linear independence of columns. If det(A) ≠ 0, columns are linearly independent, implying full rank n, and the inverse exists. Conversely, if A is invertible, rank(A) = n, and det(A) ≠ 0 (determinant of a full-rank matrix is non-zero). ∎

**Definition 1.6 (Determinant - 2×2 case):** For A = [[a,b],[c,d]], det(A) = ad - bc.

For general n×n matrices, the determinant can be computed recursively via Laplace expansion or more efficiently via LU decomposition.

**Theorem 1.4 (Determinant Multiplication):** For square matrices A, B of same dimension:
$$\det(AB) = \det(A)\det(B)$$

**In ML Applications:** The normal equation for linear regression is $w = (X^T X)^{-1} X^T y$, requiring $(X^T X)$ to be invertible. This holds when X has full column rank (linearly independent features).

## 2. Eigenvalue Decomposition

### 2.1 Definitions and Properties

**Definition 2.1 (Eigenvalue/Eigenvector):** For A ∈ ℝ^{n×n}, λ ∈ ℝ is an eigenvalue with eigenvector v ≠ 0 if:
$$Av = \lambda v$$

Equivalently, $(A - \lambda I)v = 0$. Non-trivial solutions exist when:
$$\det(A - \lambda I) = 0$$
This characteristic polynomial yields n eigenvalues (possibly complex).

**Theorem 2.1 (Eigenvalue Properties):**

1. Trace(A) = Σ λᵢ (sum of eigenvalues)
2. det(A) = Π λᵢ (product of eigenvalues)
3. A is invertible iff all λᵢ ≠ 0

**Proof of (1):** The characteristic polynomial is $p(\lambda) = \det(A - \lambda I) = (-1)^n \lambda^n + \text{tr}(A)\lambda^{n-1} + \ldots$. The coefficient of $\lambda^{n-1}$ is tr(A), which also equals Σ λᵢ by Vieta's formulas. ∎

**Worked Example:** Let A = [[4,1],[2,3]]. Compute eigenvalues:
$$\det\begin{pmatrix} 4-\lambda & 1 \\ 2 & 3-\lambda \end{pmatrix} = (4-\lambda)(3-\lambda) - 2 = \lambda^2 - 7\lambda + 10 = 0$$
Solving: λ₁ = 5, λ₂ = 2.

For λ₁ = 5: (A - 5I)v = 0 gives [[-1,1],[2,-2]]v = 0 ⇒ v₁ = [1,1]^T.
For λ₂ = 2: (A - 2I)v = 0 gives [[2,1],[2,1]]v = 0 ⇒ v₂ = [1,-2]^T.

### 2.2 Symmetric Matrices and Spectral Theorem

**Theorem 2.2 (Spectral Theorem):** If A ∈ ℝ^{n×n} is symmetric (A = A^T), then there exists an orthogonal matrix Q (Q^T Q = I) such that:
$$A = Q \Lambda Q^T$$
where Λ = diag(λ₁, ..., λₙ) contains real eigenvalues.

**Corollary:** For symmetric A, eigenvectors corresponding to distinct eigenvalues are orthogonal. Repeated eigenvalues yield eigenspaces whose basis vectors can be orthonormalized.

### 2.3 Positive Definiteness

**Definition 2.2 (Positive Definite):** A symmetric matrix A ∈ ℝ^{n×n} is **positive definite** if for all x ≠ 0:
$$x^T A x > 0$$

**Theorem 2.3 (Eigenvalue Characterization):** A symmetric matrix is positive definite if and only if all eigenvalues are strictly positive.

**Proof:** Let A = QΛQ^T with orthogonal Q. For any x ≠ 0, let y = Q^T x (also non-zero). Then:
$$x^T A x = x^T Q \Lambda Q^T x = y^T \Lambda y = \sum_{i=1}^n \lambda_i y_i^2$$
Since y_i² ≥ 0 and not all zero, the sum is positive iff all λᵢ > 0. ∎

**Definition 2.3 (Positive Semi-Definite):** $x^T A x \geq 0$ for all x, equivalent to eigenvalues ≥ 0.

**In ML:** Covariance matrices Σ are always positive semi-definite. The Hessian matrix of the loss function being positive definite ensures a local minimum in optimization.

## 3. Singular Value Decomposition

**Theorem 3.1 (SVD):** Any matrix A ∈ ℝ^{m×n} can be decomposed as:
$$A = U \Sigma V^T$$
where U ∈ ℝ^{m×m} and V ∈ ℝ^{n×n} are orthogonal, and Σ ∈ ℝ^{m×n} is diagonal with singular values σ₁ ≥ σ₂ ≥ ... ≥ 0.

The columns of U are eigenvectors of AA^T; columns of V are eigenvectors of A^T A. Singular values satisfy σᵢ² = eigenvalueᵢ of A^T A.

**Theorem 3.2 (Matrix Rank via SVD):** rank(A) = number of non-zero singular values.

**In ML:** SVD enables dimensionality reduction (truncate to top k singular values), noise reduction, and computing pseudoinverse: A⁺ = V Σ⁺ U^T where Σ⁺ replaces non-zero σᵢ with 1/σᵢ.

## 4. Multivariate Calculus

### 4.1 Gradient and Jacobian

**Definition 4.1 (Gradient):** For f: ℝ^n → ℝ, the gradient ∇f(x) ∈ ℝ^n is:
$$\nabla f(x) = \begin{pmatrix} \frac{\partial f}{\partial x_1} \\ \frac{\partial f}{\partial x_2} \\ \vdots \\ \frac{\partial f}{\partial x_n} \end{pmatrix}$$

**Theorem 4.1 (Gradient Descent):** For minimizing f, iterate:
$$x^{(t+1)} = x^{(t)} - \alpha \nabla f(x^{(t)})$$
where α > 0 is the learning rate. For convex f, small α ensures convergence to global minimum.

**Definition 4.2 (Jacobian):** For F: ℝ^n → ℝ^m, the Jacobian J ∈ ℝ^{m×n} is:
$$J_{ij} = \frac{\partial F_i}{\partial x_j}$$

### 4.2 Hessian Matrix

**Definition 4.3 (Hessian):** For f: ℝ^n → ℝ, the Hessian H ∈ ℝ^{n×n}$ is:
$$H_{ij} = \frac{\partial^2 f}{\partial x_i \partial x_j}$$

**Theorem 4.2 (Second-Order Optimality):** At a critical point x* (∇f(x*) = 0):

- If H(x*) is positive definite, x* is a local minimum
- If H(x*) is negative definite, x* is a local maximum
- If H has mixed eigenvalues, x\* is a saddle point

**Worked Example:** For f(x) = x₁² + x₂² - x₁x₂, compute:
$$\nabla f = \begin{pmatrix} 2x_1 - x_2 \\ 2x_2 - x_1 \end{pmatrix} = 0 \Rightarrow x_1 = x_2 = 0$$
H = [[2, -1], [-1, 2]]. Eigenvalues: 1, 3 (both positive). Thus x\* = (0,0) is a local minimum.

## 5. Probability Theory for Multivariate Data

### 5.1 Covariance Matrix

**Definition 5.1 (Covariance):** For random vectors X, Y ∈ ℝ^n:
$$\text{Cov}(X, Y) = \mathbb{E}[(X - \mu_X)(Y - \mu_Y)^T]$$

**Definition 5.2 (Covariance Matrix):** For X ∈ ℝ^p with mean μ ∈ ℝ^p:
$$\Sigma = \text{Cov}(X) = \mathbb{E}[(X - \mu)(X - \mu)^T] \in \mathbb{R}^{p \times p}$$

**Theorem 5.1 (Properties of Covariance):**

1. Σ is symmetric: Σ = Σ^T
2. Σ is positive semi-definite: $a^T \Sigma a = \text{Var}(a^T X) \geq 0$

**Proof of (2):** For any a ∈ ℝ^p, $a^T \Sigma a = \mathbb{E}[(a^T(X - \mu))^2] \geq 0$ since squares are non-negative. ∎

### 5.2 Multivariate Gaussian Distribution

**Definition 5.3 (Multivariate Normal):** X ~ N(μ, Σ) if its density is:
$$f(x) = \frac{1}{(2\pi)^{p/2} |\Sigma|^{1/2}} \exp\left(-\frac{1}{2}(x-\mu)^T \Sigma^{-1} (x-\mu)\right)$$

**Theorem 5.2 (Marginal Distributions):** If X ~ N(μ, Σ) is partitioned as X = (X₁, X₂), then X₁ ~ N(μ₁, Σ₁₁) where Σ₁₁ is the appropriate submatrix.

**In ML:** Linear discriminant analysis (LDA) uses the multivariate Gaussian assumption for classification. Mahalanobis distance $(x-\mu)^T \Sigma^{-1} (x-\mu)$ measures distance accounting for correlation structure.

---

## Summary

This material established the mathematical foundations for multivariate data analysis: vector/matrix operations with rigorous proofs, eigenvalue decomposition and the spectral theorem, positive definiteness criteria, singular value decomposition, multivariate calculus (gradients, Jacobians, Hessians), and probability theory including covariance matrices and the multivariate Gaussian distribution. These tools enable understanding of PCA, linear regression, discriminant analysis, and gradient-based optimization in machine learning.
