# Singular Value Decomposition (SVD)

## Introduction

Singular Value Decomposition (SVD) is one of the most powerful and versatile concepts in linear algebra, particularly significant in the context of the university's Linear Algebra course (BCS405D). It provides a way to decompose any rectangular matrix into three fundamental components that reveal its intrinsic properties. Unlike eigenvalue decomposition which only works for square symmetric matrices, SVD can be applied to any m×n matrix, making it universally applicable across various domains.

The significance of SVD extends far beyond theoretical mathematics. In computer science and engineering, SVD forms the backbone of numerous practical applications including image compression, recommendation systems (like Netflix movie suggestions), principal component analysis (PCA) for data science, solving ill-conditioned linear systems, and noise reduction in signals. Understanding SVD is essential for any CSE student as it connects linear algebra to real-world computational problems that engineers face regularly.

This topic builds upon concepts from previous modules including matrix operations, determinants, rank of matrices, and eigenvalues/eigenvectors. The decomposition A = UΣV^T where U and V are orthogonal matrices and Σ is a diagonal matrix, provides deep insights into the structure of any linear transformation.

## Key Concepts

### Definition of SVD

For any m×n matrix A of rank r, the Singular Value Decomposition is defined as:

**A = UΣV^T**

Where:

- U is an m×m orthogonal matrix (columns are left singular vectors)
- Σ is an m×n diagonal matrix with non-negative real entries (singular values)
- V is an n×n orthogonal matrix (columns are right singular vectors)

The diagonal entries of Σ are called **singular values** and are typically arranged in descending order: σ₁ ≥ σ₂ ≥ ... ≥ σᵣ > 0.

### Relationship Between SVD and Eigenvalues

The singular values of A are the square roots of the eigenvalues of both A^T A and AA^T. Specifically:

- σᵢ = √λᵢ(A^T A) = √λᵢ(AA^T)

The left singular vectors (columns of U) are eigenvectors of AA^T.
The right singular vectors (columns of V) are eigenvectors of A^T A.

### Properties of SVD

1. **Uniqueness**: If all singular values are distinct and non-zero, the SVD is unique (up to signs of singular vectors).

2. **Orthogonality**: U and V are orthogonal matrices, meaning U^T U = I and V^T V = I.

3. **Rank**: The number of non-zero singular values equals the rank of matrix A.

4. **Energy Preservation**: The sum of squares of singular values equals the sum of squares of all entries in A.

5. **Compact SVD**: For an m×n matrix of rank r, we can write A = UᵣΣᵣVᵣ^T where Uᵣ is m×r, Σᵣ is r×r diagonal, and Vᵣ is n×r.

### Geometric Interpretation

SVD represents any linear transformation as a sequence of three geometric operations:

1. A rotation/reflection (V^T) - coordinate transformation
2. A scaling (Σ) - stretching/compressing along axes
3. Another rotation/reflection (U) - final coordinate transformation

### Low-Rank Approximation (Eckart-Young Theorem)

For any matrix A and integer k < rank(A), the best k-rank approximation to A in Frobenius norm is given by:
Aₖ = UₖΣₖVₖ^T
where only the top k singular values are retained.

## Examples

### Example 1: Compute SVD of a 2×2 Matrix

Find the SVD of A = [[3, 1], [1, 3]]

**Step 1: Compute A^T A**
A^T A = [[3, 1], [1, 3]]^T × [[3, 1], [1, 3]]
= [[10, 6], [6, 10]]

**Step 2: Find eigenvalues and eigenvectors of A^T A**
|A^T A - λI| = 0
|[[10-λ, 6], [6, 10-λ]]| = (10-λ)² - 36 = 0
λ² - 20λ + 64 = 0
λ₁ = 16, λ₂ = 4

Singular values: σ₁ = √16 = 4, σ₂ = √4 = 2

**Step 3: Find eigenvectors of A^T A**
For λ₁ = 16: (A^T A - 16I)v = 0
[[-6, 6], [6, -6]]v = 0
v₁ = [1/√2, 1/√2]^T

For λ₂ = 4: (A^T A - 4I)v = 0
[[6, 6], [6, 6]]v = 0
v₂ = [1/√2, -1/√2]^T

V = [[1/√2, 1/√2], [1/√2, -1/√2]]

**Step 4: Compute U**
u₁ = (1/σ₁)Av₁ = (1/4)[[3, 1], [1, 3]][1/√2, 1/√2]^T = [1/√2, 1/√2]^T
u₂ = (1/σ₂)Av₂ = (1/2)[[3, 1], [1, 3]][1/√2, -1/√2]^T = [1/√2, -1/√2]^T

U = [[1/√2, 1/√2], [1/√2, -1/√2]]

**Step 5: Write SVD**
A = UΣV^T = [[1/√2, 1/√2], [1/√2, -1/√2]] × [[4, 0], [0, 2]] × [[1/√2, 1/√2], [1/√2, -1/√2]]^T

### Example 2: Rank and SVD

For matrix A = [[1, 1], [1, 1]], find its SVD and verify rank.

**Solution:**
A^T A = [[2, 2], [2, 2]]
Eigenvalues: λ₁ = 4, λ₂ = 0
Singular values: σ₁ = 2, σ₂ = 0

Since one singular value is zero, rank(A) = 1.

V = [[1/√2, 1/√2], [1/√2, -1/√2]]
Σ = [[2, 0], [0, 0]]
U = [[1], [1]] (first column), second column can be any orthogonal vector

A = [[1/√2], [1/√2]] × [2] × [[1/√2, 1/√2]]

This shows rank-1 decomposition.

### Example 3: Image Compression Application

Given a 4×4 image matrix with singular values [10, 5, 1, 0.1], if we keep only the first two singular values (k=2), calculate the compression ratio and approximate error.

**Solution:**
Original: 16 elements stored
Compressed: U (4×2) + Σ (2) + V^T (2×4) = 8 + 2 + 8 = 18... but in practice, we store only non-zero values.

For k=2 approximation:
Storage = 4×2 + 2 + 2×4 = 8 + 2 + 8 = 18 values
But effective information: 2 singular values capture most energy

Energy retained = (10² + 5²)/(10² + 5² + 1² + 0.01²) = (100 + 25)/(100 + 25 + 1 + 0.0001) ≈ 125/126 ≈ 99.2%

This demonstrates why SVD achieves excellent compression with minimal quality loss.

## Exam Tips

1. **Remember the SVD formula**: A = UΣV^T is fundamental - know that U and V are orthogonal matrices.

2. **Singular values are always non-negative**: Unlike eigenvalues which can be negative, singular values σᵢ ≥ 0.

3. **Relationship with eigenvalues**: σᵢ = √λᵢ(A^T A) - this is frequently tested in university exams.

4. **Rank from SVD**: Number of non-zero singular values equals rank of matrix - a key property for solving problems.

5. **Compact SVD**: For rank-r matrix, you only need r singular values - remember this for computational problems.

6. **Orthogonal matrices**: U^T U = I and V^T V = I - always verify this property in solutions.

7. **Geometric meaning**: SVD transforms any matrix into rotation-scaling-rotation - understanding this helps visualize linear transformations.

8. **Low-rank approximation**: For minimum error approximation, use largest k singular values (Eckart-Young theorem).
