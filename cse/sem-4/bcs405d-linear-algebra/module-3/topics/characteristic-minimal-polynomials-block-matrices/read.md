# Characteristic and Minimal Polynomials of Block Matrices

## Table of Contents

- [Characteristic and Minimal Polynomials of Block Matrices](#characteristic-and-minimal-polynomials-of-block-matrices)
- [1. Introduction](#1-introduction)
- [2. Characteristic Polynomial: Foundations and Properties](#2-characteristic-polynomial-foundations-and-properties)
  - [2.1 Definition and Basic Properties](#21-definition-and-basic-properties)
  - [2.2 Characteristic Polynomial of Block Diagonal Matrices](#22-characteristic-polynomial-of-block-diagonal-matrices)
  - [2.3 Characteristic Polynomial of Block Triangular Matrices](#23-characteristic-polynomial-of-block-triangular-matrices)
- [3. Minimal Polynomial: Theory and Applications](#3-minimal-polynomial-theory-and-applications)
  - [3.1 Definition and Characteristic Properties](#31-definition-and-characteristic-properties)
  - [3.2 Minimal Polynomial of Block Diagonal Matrices](#32-minimal-polynomial-of-block-diagonal-matrices)
  - [3.3 Minimal Polynomial of Block Triangular Matrices](#33-minimal-polynomial-of-block-triangular-matrices)
- [4. Advanced Block Matrix Operations](#4-advanced-block-matrix-operations)
  - [4.1 Kronecker Sum](#41-kronecker-sum)
  - [4.2 Kronecker Product](#42-kronecker-product)
- [5. Applications and Computational Considerations](#5-applications-and-computational-considerations)

## 1. Introduction

The characteristic polynomial and minimal polynomial constitute fundamental invariants in the spectral theory of matrices. These polynomial constructs provide deep insights into the structural properties of matrices, including eigenvalues, Jordan canonical forms, and diagonalizability criteria. The extension of these concepts to block matrices—matrices partitioned into smaller submatrices—reveals elegant relationships that significantly simplify computational complexity while offering profound theoretical understanding.

Block matrices arise extensively in applied mathematics, engineering disciplines, and computer science. Applications span systems theory, control engineering, numerical analysis, quantum mechanics, and graph theory. The ability to compute characteristic and minimal polynomials for block matrices efficiently has substantial practical implications for analyzing dynamical systems, solving systems of linear differential equations, and performing large-scale matrix computations.

This module establishes the theoretical foundation for understanding how the characteristic and minimal polynomials of block matrices relate to those of their constituent blocks. We examine special cases including block diagonal and block triangular matrices, providing rigorous proofs for key results. These foundations prepare students for advanced topics in matrix analysis and linear systems theory.

## 2. Characteristic Polynomial: Foundations and Properties

### 2.1 Definition and Basic Properties

**Definition 2.1**: Let $A \in M_n(F)$ be an $n \times n$ matrix over a field $F$. The characteristic polynomial of $A$ is defined as:

$$p_A(\lambda) = \det(A - \lambda I_n)$$

where $I_n$ denotes the $n \times n$ identity matrix and $\lambda$ is an indeterminate.

The characteristic polynomial is a monic polynomial of degree $n$. Its roots, called eigenvalues, determine the spectral properties of the matrix. The coefficients of the characteristic polynomial encode important matrix invariants:

- The constant term satisfies $p_A(0) = \det(A)$, providing the determinant.
- The coefficient of $\lambda^{n-1}$ equals $-\text{tr}(A)$, the negative of the trace.
- The coefficient of $\lambda^{n-2}$ relates to the sum of principal minors.

**Theorem 2.2** (Cayley-Hamilton Theorem): For any square matrix $A \in M_n(F)$, the characteristic polynomial satisfies $p_A(A) = 0$.

_Proof_: The Cayley-Hamilton theorem states that every square matrix satisfies its own characteristic equation. While the classical proof involves matrix algebra, an intuitive understanding recognizes that substituting $A$ for $\lambda$ in the determinant expansion yields the zero matrix. $\square$

### 2.2 Characteristic Polynomial of Block Diagonal Matrices

**Theorem 2.3**: Let $A = \text{diag}(A_1, A_2, \ldots, A_k)$ be a block diagonal matrix where $A_i \in M_{n_i}(F)$ for $i = 1, 2, \ldots, k$. Then:

$$p_A(\lambda) = \prod_{i=1}^{k} p_{A_i}(\lambda)$$

_Proof_: For the block diagonal matrix $A$, we have:

$$A - \lambda I = \text{diag}(A_1 - \lambda I_{n_1}, A_2 - \lambda I_{n_2}, \ldots, A_k - \lambda I_{n_k})$$

The determinant of a block diagonal matrix equals the product of the determinants of the diagonal blocks. Therefore:

$$\det(A - \lambda I) = \prod_{i=1}^{k} \det(A_i - \lambda I_{n_i}) = \prod_{i=1}^{k} p_{A_i}(\lambda)$$

This establishes the result. $\square$

**Corollary 2.4**: The eigenvalues of a block diagonal matrix are precisely the union (with multiplicities) of the eigenvalues of its diagonal blocks.

### 2.3 Characteristic Polynomial of Block Triangular Matrices

**Theorem 2.5**: Let $A = \begin{bmatrix} A_{11} & A_{12} \\ 0 & A_{22} \end{bmatrix}$ be a block upper triangular matrix with $A_{11} \in M_m(F)$ and $A_{22} \in M_n(F)$. Then:

$$p_A(\lambda) = p_{A_{11}}(\lambda) \cdot p_{A_{22}}(\lambda)$$

_Proof_: Consider the matrix $A - \lambda I$:

$$A - \lambda I = \begin{bmatrix} A_{11} - \lambda I_m & A_{12} \\ 0 & A_{22} - \lambda I_n \end{bmatrix}$$

For block triangular matrices, the determinant decomposes as:

$$\det(A - \lambda I) = \det(A_{11} - \lambda I_m) \cdot \det(A_{22} - \lambda I_n)$$

This follows from the Laplace expansion along the first $m$ rows (or columns), where only the diagonal blocks contribute to the determinant. The off-diagonal block $A_{12}$ does not affect the characteristic polynomial. $\square$

**Remark 2.6**: The same result holds for block lower triangular matrices. Furthermore, this property extends inductively to block triangular matrices of arbitrary size.

## 3. Minimal Polynomial: Theory and Applications

### 3.1 Definition and Characteristic Properties

**Definition 3.1**: The minimal polynomial $m_A(\lambda)$ of a matrix $A \in M_n(F)$ is the unique monic polynomial of least degree such that $m_A(A) = 0$.

The minimal polynomial satisfies several fundamental properties:

**Theorem 3.2**: Let $A \in M_n(F)$ and let $m_A(\lambda)$ be its minimal polynomial. Then:

1. $m_A(\lambda)$ divides every polynomial $p(\lambda)$ such that $p(A) = 0$.
2. $m_A(\lambda)$ and $p_A(\lambda)$ have the same irreducible factors over $F$.
3. The degree of $m_A(\lambda)$ equals the size of the largest Jordan block in the Jordan canonical form of $A$.

_Proof_: Property (1) follows from the division algorithm in the polynomial ring $F[\lambda]$. If $p(A) = 0$ and $\deg(m_A) \leq \deg(p)$, then $m_A$ divides $p$. Property (2) results from the Cayley-Hamilton theorem combined with the fact that the characteristic polynomial splits into irreducible factors corresponding to eigenvalues. Property (3) follows from the Jordan canonical form representation, where each Jordan block $J_k(\lambda_i)$ satisfies $(A - \lambda_i I)^k = 0$ on the corresponding subspace. $\square$

**Theorem 3.3**: A matrix $A$ is diagonalizable over $F$ if and only if its minimal polynomial has no repeated roots (i.e., is square-free).

_Proof_: If $A$ is diagonalizable, it has a basis of eigenvectors, and the minimal polynomial equals the product $(\lambda - \lambda_1)(\lambda - \lambda_2)\ldots(\lambda - \lambda_r)$ with distinct eigenvalues $\lambda_i$. Conversely, if the minimal polynomial has no repeated roots, each Jordan block must be of size 1, implying diagonalizability. $\square$

### 3.2 Minimal Polynomial of Block Diagonal Matrices

**Theorem 3.4**: For a block diagonal matrix $A = \text{diag}(A_1, A_2, \ldots, A_k)$, the minimal polynomial is:

$$m_A(\lambda) = \text{lcm}\{m_{A_1}(\lambda), m_{A_2}(\lambda), \ldots, m_{A_k}(\lambda)\}$$

_Proof_: Since $m_{A_i}(A_i) = 0$ for each $i$, let $m(\lambda) = \text{lcm}(m_{A_1}, \ldots, m_{A_k})$. For any $i$, $m_{A_i}$ divides $m$, hence $m(A_i) = 0$. For the block diagonal structure:

$$m(A) = \text{diag}(m(A_1), m(A_2), \ldots, m(A_k)) = \text{diag}(0, 0, \ldots, 0) = 0$$

Thus $m(A) = 0$. To show minimality, suppose $p(A) = 0$. Then $p(A_i) = 0$ for each diagonal block, implying $m_{A_i}$ divides $p$ for all $i$. Consequently, their least common multiple $m_A$ divides $p$. Therefore $m_A$ is the minimal polynomial. $\square$

### 3.3 Minimal Polynomial of Block Triangular Matrices

For block triangular matrices, determining the minimal polynomial requires more careful analysis. Consider $A = \begin{bmatrix} A_{11} & A_{12} \\ 0 & A_{22} \end{bmatrix}$.

**Theorem 3.5**: If $A_{11}$ and $A_{22}$ have no common eigenvalues (i.e., their spectra are disjoint), then:

$$m_A(\lambda) = m_{A_{11}}(\lambda) \cdot m_{A_{22}}(\lambda)$$

_Proof_: When the diagonal blocks have disjoint spectra, the minimal polynomial cannot have smaller degree than the product. Since both $m_{A_{11}}(A)$ and $m_{A_{22}}(A)$ vanish on their respective invariant subspaces, their product annihilates $A$. The disjoint eigenvalue condition ensures no cancellation of factors is possible, establishing the minimality. $\square$

**Remark 3.6**: When $A_{11}$ and $A_{22}$ share eigenvalues, the minimal polynomial may differ from the product. The off-diagonal block $A_{12}$ can introduce additional constraints, potentially increasing the degree of the minimal polynomial.

## 4. Advanced Block Matrix Operations

### 4.1 Kronecker Sum

**Definition 4.1**: The Kronecker sum (or tensor sum) of two matrices $A \in M_m(F)$ and $B \in M_n(F)$ is defined as:

$$A \oplus B = A \otimes I_n + I_m \otimes B$$

where $\otimes$ denotes the Kronecker product.

**Theorem 4.2**: The eigenvalues of the Kronecker sum $A \oplus B$ are given by $\lambda_i + \mu_j$ where $\lambda_i$ are eigenvalues of $A$ and $\mu_j$ are eigenvalues of $B$.

_Proof_: This follows from the spectral properties of the Kronecker product and the fact that if $Av = \lambda v$ and $Bw = \mu w$, then $(A \oplus B)(v \otimes w) = (\lambda + \mu)(v \otimes w)$. $\square$

**Corollary 4.3**: The characteristic polynomial of the Kronecker sum satisfies:

$$p_{A \oplus B}(\lambda) = \prod_{i,j} (\lambda - (\lambda_i + \mu_j))$$

### 4.2 Kronecker Product

**Definition 4.4**: The Kronecker product (tensor product) of $A \in M_{m \times n}$ and $B \in M_{p \times q}$ is the $mp \times nq$ matrix formed by taking all possible products of entries:

$$A \otimes B = \begin{bmatrix} a_{11}B & a_{12}B & \cdots & a_{1n}B \\ a_{21}B & a_{22}B & \cdots & a_{2n}B \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1}B & a_{m2}B & \cdots & a_{mn}B \end{bmatrix}$$

**Theorem 4.5**: For Kronecker products, the eigenvalues satisfy $\lambda_i \mu_j$ where $\lambda_i \in \sigma(A)$ and $\mu_j \in \sigma(B)$.

**Corollary 4.6**: The characteristic polynomial of $A \otimes B$ is:

$$p_{A \otimes B}(\lambda) = \prod_{i,j} (\lambda - \lambda_i \mu_j)$$

## 5. Applications and Computational Considerations

The theoretical results established in this module have significant practical applications. In control theory, block matrices arise in state-space representations where the characteristic polynomial determines system stability through the locations of poles. The eigenvalues of Kronecker sums appear in the analysis of coupled dynamical systems and in solving Sylvester equations.

Computationally, the factorization properties of characteristic polynomials for block matrices enable divide-and-conquer algorithms for large sparse matrices. The minimal polynomial plays a crucial role in Krylov subspace methods for solving linear systems and in computing matrix functions efficiently.

These concepts also provide the foundation for understanding more advanced topics including the Jordan canonical form, rational canonical forms, and the spectral theory of linear operators on finite-dimensional vector spaces.
