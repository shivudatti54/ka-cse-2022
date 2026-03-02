# Inner Product Spaces - Teaching Methodology Summary

## Key Definitions
- **Inner Product**: A function $\langle \cdot, \cdot \rangle: V \times V \to \mathbb{F}$ satisfying conjugate symmetry, linearity in first argument, and positive definiteness.
- **Norm**: $\|v\| = \sqrt{\langle v, v \rangle}$ induced by the inner product.
- **Orthogonal Vectors**: Vectors $u, v$ where $\langle u, v \rangle = 0$.
- **Orthonormal Set**: Vectors that are mutually orthogonal and have unit norm.

## Important Formulas
- **Cauchy-Schwarz**: $|\langle u, v \rangle| \leq \|u\| \|v\|$
- **Gram-Schmidt**: $v_k = u_k - \sum_{i=1}^{k-1} \frac{\langle u_k, v_i \rangle}{\|v_i\|^2} v_i$
- **Projection**: $\text{proj}_W(v) = \sum_{i=1}^{m} \langle v, w_i \rangle w_i$ for orthonormal basis $\{w_i\}$
- **Normal Equations**: $A^T A \mathbf{x} = A^T \mathbf{b}$
- **QR Factorization**: $A = QR$ where $Q^T Q = I$ and $R$ is upper triangular

## Key Points
- Inner products generalize the dot product to abstract vector spaces.
- Orthogonal bases simplify computations significantly.
- Gram-Schmidt converts any linearly independent set to an orthogonal set.
- QR factorization uses orthonormal bases for numerical stability.
- Orthogonal projection onto a subspace gives the closest point in that subspace.
- Least squares minimizes squared error, solving $Ax \approx b$ when no exact solution exists.
- The column space of $A$ and null space of $A^T$ are orthogonal complements in $\mathbb{R}^n$.

## Common Mistakes
- Forgetting to normalize vectors when constructing orthonormal bases from orthogonal ones.
- Applying Gram-Schmidt to linearly dependent vectors, which leads to division by zero.
- Confusing orthogonal (perpendicular) with orthonormal (perpendicular and unit length).
- Inverting $A^T A$ in least squares without checking its invertibility.
- Using the wrong inner product when working in function spaces.
- Forgetting that the projection formula $P = A(A^T A)^{-1} A^T$ assumes $A$ has full column rank.