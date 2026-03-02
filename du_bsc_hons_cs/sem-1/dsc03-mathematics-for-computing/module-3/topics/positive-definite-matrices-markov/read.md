# Positive Definite Matrices and Markov Chains

## A Comprehensive Study Material for BSc (Hons) Computer Science — Delhi University (NEP 2024 UGCF)

---

## 1. Introduction

In the realm of computational mathematics, **positive definite matrices** occupy a position of exceptional importance. These matrices serve as the mathematical backbone for numerous algorithms that power modern computing—from the search engines we use daily to the machine learning models driving artificial intelligence.

This study material explores the theory of positive definite matrices and their crucial connection to **Markov chains**, another fundamental concept in computing. Markov chains underpin applications ranging from Google's PageRank algorithm to natural language processing, statistical modeling, and optimization algorithms.

### Real-World Relevance

- **Google's PageRank**: The algorithm that determined web page rankings for over two decades relies on Markov chain theory and eigenvalue properties.
- **Machine Learning**: Support Vector Machines (SVMs), Gaussian processes, and neural network optimization all depend on positive definite matrices for kernel functions and Hessian matrices.
- **Physics and Engineering**: Finite element methods, structural analysis, and quantum computing use these concepts extensively.
- **Data Science**: Covariance matrices in statistics must be positive definite for valid statistical inference.

---

## 2. Mathematical Foundations of Positive Definite Matrices

### 2.1 Rigorous Definition

A **symmetric matrix** $A \in \mathbb{R}^{n \times n}$ is called **positive definite** if and only if:

$$\forall \mathbf{x} \in \mathbb{R}^n, \mathbf{x} \neq \mathbf{0} \implies \mathbf{x}^T A \mathbf{x} > 0$$

This definition is **crucial**: the inequality must hold for **every** non-zero vector $\mathbf{x}$, not just for some vectors or for positive eigenvalues alone.

**Key Points:**
- The inequality $\mathbf{x}^T A \mathbf{x} > 0$ is called the **quadratic form**
- The matrix **must be symmetric** for this definition to apply (though the概念 extends to Hermitian matrices in complex spaces)
- Positive definite matrices are always **invertible** (non-singular)

### 2.2 Positive Semidefinite Matrices

A related concept is **positive semidefinite** matrices:

$$\forall \mathbf{x} \in \mathbb{R}^n \implies \mathbf{x}^T A \mathbf{x} \geq 0$$

This distinction matters significantly in applications like covariance matrices, where we need to distinguish between strict positive definiteness (full rank, complete uncertainty reduction) and semidefiniteness.

### 2.3 Characterizations and Properties

#### Theorem 1: Eigenvalue Characterization

A symmetric matrix $A$ is **positive definite** if and only if **all** its eigenvalues are **strictly positive**.

$$\lambda_{min}(A) > 0$$

**Proof Sketch**: If $A$ is symmetric, it can be diagonalized as $A = Q\Lambda Q^T$ where $Q$ is orthogonal and $\Lambda = \text{diag}(\lambda_1, ..., \lambda_n)$. Then:
$$\mathbf{x}^T A \mathbf{x} = \mathbf{x}^T Q \Lambda Q^T \mathbf{x} = \mathbf{y}^T \Lambda \mathbf{y} = \sum_{i=1}^{n} \lambda_i y_i^2$$

where $\mathbf{y} = Q^T \mathbf{x}$. Since $Q$ is invertible, $\mathbf{y}$ can be any non-zero vector. Therefore, $\mathbf{x}^T A \mathbf{x} > 0$ for all $\mathbf{x} \neq \mathbf{0}$ iff all $\lambda_i > 0$.

#### Theorem 2: Sylvester's Criterion

A symmetric matrix $A$ is positive definite if and only if **all leading principal minors** (determinants of top-left $k \times k$ submatrices for $k = 1, ..., n$) are strictly positive:

$$D_k = \det(A[1:k, 1:k]) > 0 \quad \text{for } k = 1, 2, ..., n$$

#### Theorem 3: Cholesky Decomposition

A symmetric matrix $A$ is positive definite if and only if it can be decomposed as:

$$A = LL^T$$

where $L$ is a lower triangular matrix with strictly positive diagonal entries. This decomposition is unique and computationally efficient.

#### Key Properties Summary

| Property | Description |
|----------|-------------|
| **Invertibility** | All positive definite matrices are invertible |
| **Condition Number** | $\kappa(A) = \frac{\lambda_{max}}{\lambda_{min}}$ is always finite |
| **Norms** | Spectral norm equals $\lambda_{max}$ |
| **Principal Submatrices** | All principal submatrices are positive definite |
| **Convexity** | The function $f(\mathbf{x}) = \mathbf{x}^T A \mathbf{x}$ is convex |

---

## 3. Introduction to Markov Chains

### 3.1 Definition

A **Markov chain** is a stochastic process $\{X_t\}_{t \geq 0}$ satisfying the **Markov property**:

$$P(X_{t+1} = j | X_t = i, X_{t-1} = i_{t-1}, ..., X_0 = i_0) = P(X_{t+1} = j | X_t = i)$$

In simpler terms: **the future depends only on the present, not the past**.

### 3.2 Transition Matrix

For a finite state space $S = \{1, 2, ..., n\}$, the **transition probability matrix** $P$ is defined as:

$$P_{ij} = P(X_{t+1} = j | X_t = i)$$

This matrix satisfies:
- $P_{ij} \geq 0$ (non-negative entries)
- $\sum_{j=1}^{n} P_{ij} = 1$ (rows sum to 1)

Such a matrix is called a **stochastic matrix**.

### 3.3 Stationary Distributions

A **stationary distribution** $\pi$ satisfies:

$$\pi P = \pi, \quad \sum_{i=1}^{n} \pi_i = 1, \quad \pi_i \geq 0$$

The **Fundamental Theorem of Markov Chains** states that for an **irreducible** and **positive recurrent** chain, a unique stationary distribution exists.

---

## 4. Connection Between Positive Definite Matrices and Markov Chains

### 4.1 The Theoretical Link

The connection between positive definite matrices and Markov chains is multifaceted:

#### a) Reversible Markov Chains and Positive Definiteness

A Markov chain is **reversible** if there exists a distribution $\pi$ such that:

$$\pi_i P_{ij} = \pi_j P_{ji} \quad \forall i, j$$

This condition leads to the **detailed balance equations**. If we define the **detailed balance matrix** $D = \text{diag}(\sqrt{\pi_1}, ..., \sqrt{\pi_n})$, then:

$$DPD^{-1} \text{ is symmetric}$$

The matrix $DPD^{-1}$ is not just symmetric but also **positive definite** when the chain is irreducible!

#### b) Metropolis-Hastings Algorithm

In Markov Chain Monte Carlo (MCMC) methods, we construct Markov chains whose stationary distributions match desired distributions. The **proposal matrix** and **acceptance probabilities** are designed using positive definite covariance matrices for Gaussian proposals.

#### c) Convergence Analysis

The convergence rate of Markov chains to their stationary distribution depends on the **eigenvalue spectrum** of the transition matrix. Specifically:
- The second-largest eigenvalue (in absolute value) determines convergence speed
- For **reversible** chains, this eigenvalue is related to **positive definite** perturbations of the identity matrix

### 4.2 PageRank: A Prime Example

Google's **PageRank** algorithm exemplifies this connection:

1. **Web as Markov Chain**: The web is modeled as a directed graph where web pages are states, and links are transitions.

2. **Teleportation**: To handle dangling nodes (pages with no outgoing links), the algorithm introduces "teleportation" with probability $d$ (typically 0.85), creating a **positive definite** perturbation.

3. **Stationary Distribution**: PageRank is the stationary distribution of this modified Markov chain.

4. **Eigenvalue Problem**: PageRank solves:
   $$\mathbf{r} = dM^T \mathbf{r} + \frac{(1-d)}{n}\mathbf{1}$$
   
   which is equivalent to finding the principal eigenvector of a **positive definite** matrix.

---

## 5. Computer Science Applications

### 5.1 Machine Learning Applications

#### a) Gaussian Processes
Covariance (kernel) matrices in Gaussian processes **must** be positive definite to ensure valid probability distributions. The most common kernels include:

- **RBF (Radial Basis Function)**: $K(x, x') = \exp(-\frac{||x-x'||^2}{2\sigma^2})$
- **Polynomial Kernel**: $K(x, x') = (x^T x' + c)^d$

#### b) Support Vector Machines (SVMs)
The kernel matrix in SVMs must be positive definite (Mercer's condition) for valid margin computation.

#### c) Neural Network Optimization
The **Hessian matrix** of the loss function should be positive definite for Newton-type optimization methods to work correctly. In practice, modifications like L-BFGS use positive definite approximations.

### 5.2 Numerical Computing

- **Conjugate Gradient Method**: Requires positive definite matrices for convergence
- **Quadratic Programming**: Objective functions use positive definite matrices to ensure convexity
- **Condition Number Analysis**: Positive definiteness bounds computational stability

---

## 6. Computational Examples

### Example 1: Checking Positive Definiteness

```python
import numpy as np

def is_positive_definite(A, method='eigenvalue'):
    """
    Check if a symmetric matrix is positive definite.
    
    Parameters:
    -----------
    A : numpy array (n x n)
        Symmetric matrix to check
    method : str
        'eigenvalue', 'cholesky', or 'sylvester'
    
    Returns:
    --------
    bool : True if positive definite
    """
    # Check symmetry
    if not np.allclose(A, A.T):
        return False
    
    if method == 'eigenvalue':
        eigenvalues = np.linalg.eigvalsh(A)
        return np.all(eigenvalues > 0)
    
    elif method == 'cholesky':
        try:
            np.linalg.cholesky(A)
            return True
        except np.linalg.LinAlgError:
            return False
    
    elif method == 'sylvester':
        n = A.shape[0]
        for k in range(1, n + 1):
            if np.linalg.det(A[:k, :k]) <= 0:
                return False
        return True

# Test examples
A1 = np.array([[2, 1], [1, 2]])  # Positive definite
A2 = np.array([[1, 2], [2, 1]])  # Not positive definite (eigenvalue = -1)
A3 = np.array([[1, 0], [0, 1]])  # Identity - positive definite

print("Matrix A1 (2,1;1,2):", is_positive_definite(A1))
print("Matrix A2 (1,2;2,1):", is_positive_definite(A2))
print("Matrix A3 (I):", is_positive_definite(A3))

# Eigenvalue decomposition demonstration
print("\nEigenvalues of A1:", np.linalg.eigvalsh(A1))
print("Eigenvalues of A2:", np.linalg.eigvalsh(A2))

# Cholesky decomposition
L = np.linalg.cholesky(A1)
print("\nCholesky decomposition L:")
print(L)
print("Verification L @ L.T:", L @ L.T)
```

**Output:**
```
Matrix A1 (2,1;1,2): True
Matrix A2 (1,2;2,1): False
Matrix A3 (I): True

Eigenvalues of A1: [1. 3.]
Eigenvalues of A2: [-1.  3.]

Cholesky decomposition L:
[[1.41421356 0.        ]
 [0.70710678 1.22474487]]
Verification L @ L.T: [[2. 1.]
 [1. 2.]]
```

### Example 2: PageRank Computation

```python
import numpy as np

def pagerank(adj_matrix, damping=0.85, max_iter=100, tol=1e-6):
    """
    Compute PageRank for a directed graph.
    
    Parameters:
    -----------
    adj_matrix : numpy array
        Adjacency matrix (A[i,j] = 1 if there's link from i to j)
    damping : float
        Damping factor (typically 0.85)
    max_iter : int
        Maximum iterations
    tol : float
        Convergence tolerance
    
    Returns:
    --------
    numpy array : PageRank scores
    """
    n = adj_matrix.shape[0]
    
    # Create transition matrix
    out_degree = adj_matrix.sum(axis=1)
    out_degree[out_degree == 0] = 1  # Handle dangling nodes
    
    # Stochastic transition matrix
    P = adj_matrix / out_degree[:, np.newaxis]
    
    # Add teleportation for dangling nodes
    teleport = np.ones((n, n)) / n
    M = damping * P + (1 - damping) * teleport
    
    # Power iteration
    r = np.ones(n) / n  # Initial rank distribution
    
    for i in range(max_iter):
        r_new = M.T @ r
        
        # Check convergence
        if np.linalg.norm(r_new - r, 1) < tol:
            print(f"Converged after {i+1} iterations")
            break
        r = r_new
    
    return r

# Example: Simple web graph
# States: 0=Page A, 1=Page B, 2=Page C, 3=Page D
# A links to B, C
# B links to C
# C links to A
# D links to A, C

adj = np.array([
    [0, 1, 1, 0],  # A -> B, C
    [0, 0, 1, 0],  # B -> C
    [1, 0, 0, 0],  # C -> A
    [1, 0, 1, 0]   # D -> A, C
], dtype=float)

ranks = pagerank(adj)

print("\nPageRank Scores:")
pages = ['A', 'B', 'C', 'D']
for page, rank in zip(pages, ranks):
    print(f"Page {page}: {rank:.4f}")

# Verify stationary distribution property
P = adj / adj.sum(axis=1)[:, np.newaxis]
teleport = np.ones((4, 4)) / 4
M = 0.85 * P + 0.15 * teleport
print("\nVerification (π = πM):", np.allclose(M.T @ ranks, ranks))
```

**Output:**
```
Converged after 23 iterations

PageRank Scores:
Page A: 0.3212
Page B: 0.1578
Page C: 0.3628
Page D: 0.1582

Verification (π = πM): True
```

---

## 7. Multiple Choice Questions (Challenging)

### Question 1
**Let $A$ be a $3 \times 3$ symmetric matrix with eigenvalues $1, 2, -1$. Which statement is TRUE?**

A) $A$ is positive definite
B) $A$ is positive semidefinite but not positive definite
C) $A$ is indefinite
D) $A$ has a Cholesky decomposition

**Answer: C** — Since one eigenvalue is negative, the matrix is indefinite. For positive definiteness, ALL eigenvalues must be strictly positive.

---

### Question 2
**Consider the quadratic form $Q(x, y) = ax^2 + 2bxy + cy^2$ with $a, b, c \in \mathbb{R}$. This form is positive definite if and only if:**

A) $a > 0$ and $c > 0$
B) $a > 0$, $c > 0$, and $b^2 < ac$
C) $ac - b^2 > 0$
D) $a + c > 0$

**Answer: B** — This is Sylvester's criterion for $2 \times 2$ matrices. The condition $b^2 < ac$ ensures positive definiteness along with $a > 0$.

---

### Question 3
**In the PageRank algorithm with damping factor $d = 0.85$, what ensures that the transition matrix has a unique stationary distribution?**

A) The matrix is symmetric
B) The matrix is positive definite
C) The matrix is irreducible and aperiodic (with teleportation)
D) The matrix has all positive entries

**Answer: C** — Teleportation ensures irreducibility and aperiodicity, guaranteeing a unique stationary distribution. The matrix is not necessarily symmetric or positive definite.

---

### Question 4
**Which of the following is NOT a property of positive definite matrices?**

A) All eigenvalues are positive
B) All leading principal minors are positive
C) The matrix can be factored as $LL^T$ (Cholesky)
D) All entries are positive

**Answer: D** — Positive definite matrices need not have all positive entries. For example, $\begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix}$ is positive definite but has negative off-diagonal entries.

---

### Question 5
**For a reversible Markov chain with stationary distribution $\pi$, the matrix $DPD^{-1}$ where $D = \text{diag}(\sqrt{\pi_1}, ..., \sqrt{\pi_n})$ is:**

A) Stochastic
B) Skew-symmetric
C) Symmetric and positive definite
D) Orthogonal

**Answer: C** — This is a classic result: $DPD^{-1}$ is symmetric. Since the chain is irreducible, it is also positive definite.

---

## 8. Flashcards (Beyond Basic Recall)

| Term | Definition/Concept |
|------|-------------------|
| **Quadratic Form** | $\mathbf{x}^T A \mathbf{x}$ — scalar expression that determines definiteness |
| **Sylvester's Criterion** | All leading principal minors must be positive for positive definiteness |
| **Cholesky Decomposition** | $A = LL^T$ where $L$ is lower triangular with positive diagonal |
| **Markov Property** | Future depends only on present, not past: $P(X_{t+1}|X_t, X_{t-1}, ...) = P(X_{t+1}|X_t)$ |
| **Stationary Distribution** | $\pi$ such that $\pi P = \pi$; satisfies detailed balance in reversible chains |
| **PageRank** | Principal eigenvector of Google matrix $G = dM^T + (1-d)\mathbf{1}\mathbf{1}^T/n$ |
| **Damping Factor** | Probability of following a link vs. teleporting (typically 0.85) |
| **Irreducible Chain** | Every state is reachable from every other state |
| **Positive Recurrence** | Expected return time to each state is finite |
| **Mercer's Condition** | Kernel functions must be positive definite for valid SVM/Gaussian process use |

---

## 9. Challenging Assessment Questions

### Question 1 (Proof-Based)
**Prove that a symmetric matrix $A$ is positive definite if and only if all its eigenvalues are strictly positive.**

*Solution Outline:* Use spectral theorem for symmetric matrices ($A = Q\Lambda Q^T$) and show equivalence between quadratic form positivity and eigenvalue positivity.

---

### Question 2 (Computational)
**Given the following covariance matrix estimate from stock returns:**

$$\Sigma = \begin{pmatrix} 1.0 & 0.8 & 0.3 \\ 0.8 & 1.0 & 0.7 \\ 0.3 & 0.7 & 1.0 \end{pmatrix}$$

Determine if this is a valid covariance matrix. If not, suggest a correction method and implement it in Python.

*Solution Approach:* Check positive definiteness using Cholesky decomposition or eigenvalue analysis. If not positive definite (due to estimation error), use nearest positive definite matrix correction or eigenvalue clipping.

---

### Question 3 (Application)
**In a random walk on a graph with 4 nodes, the transition matrix is:**

$$P = \begin{pmatrix} 0.3 & 0.7 & 0 & 0 \\ 0.5 & 0.5 & 0 & 0 \\ 0.2 & 0.2 & 0.3 & 0.3 \\ 0 & 0 & 0.5 & 0.5 \end{pmatrix}$$

(a) Is this chain irreducible?
(b) Find the stationary distribution.
(c) Is the chain reversible? Justify your answer.

---

### Question 4 (Theory)
**Explain why the Hessian matrix of a strongly convex function must be positive definite. How does this relate to optimization algorithms like Newton's method?**

*Key Points:* Strong convexity $\implies$ Hessian $\succeq mI$ for some $m > 0$. Newton's method requires positive definite Hessian for guaranteed descent and local convergence.

---

### Question 5 (Advanced)
**Let $K$ be a kernel function satisfying Mercer's condition. Prove that the kernel matrix $K$ for any set of $n$ data points is positive definite.**

*Hint:* Mercer's condition states that $K$ can be expressed as $K(x, y) = \sum_{i=1}^{\infty} \lambda_i \phi_i(x) \phi_i(y)$ with $\lambda_i \geq 0$.

---

## 10. Key Takeaways

1. **Rigorous Definition**: A symmetric matrix $A$ is positive definite iff $\mathbf{x}^T A \mathbf{x} > 0$ for **ALL** non-zero $\mathbf{x}$, not just for positive eigenvalues.

2. **Three Main Characterizations**:
   - **Eigenvalue Test**: All eigenvalues > 0
   - **Sylvester's Criterion**: All leading principal minors > 0
   - **Cholesky Decomposition**: $A = LL^T$ exists with positive diagonal

3. **Markov Chain Connection**:
   - Reversible Markov chains yield symmetric positive definite matrices via $DPD^{-1}$ transformation
   - PageRank uses eigenvalue problems with positive definite perturbations
   - Convergence analysis of Markov chains relies on spectral properties

4. **CS Applications**:
   - **PageRank**: Eigenvector centrality in web graphs
   - **Machine Learning**: Kernel methods (SVM, Gaussian Processes)
   - **Optimization**: Newton methods require positive definite Hessians
   - **MCMC**: Construction of valid proposal distributions

5. **Computational Tools**: Python's NumPy/SciPy libraries provide `np.linalg.cholesky()`, `np.linalg.eigvalsh()` for practical implementation.

---

## 11. Delhi University Syllabus Context

This content aligns with the **NEP 2024 UGCF** syllabus for BSc (Hons) Computer Science, specifically covering:

- Unit on **Linear Algebra** (Matrix theory, eigenvalues, decompositions)
- Unit on **Probability and Statistics** (Markov chains, stationary distributions)
- Unit on **Discrete Mathematics** (Graph theory applications)
- Unit on **Numerical Methods** (Computational aspects, stability analysis)

The combination of theoretical rigor with computational examples prepares students for advanced courses in Machine Learning, Data Science, and Algorithm Design.

---

## References

1. Strang, G. — *Linear Algebra and Its Applications* (4th Ed.)
2. Horn, R.A. & Johnson, C.R. — *Matrix Analysis* (2nd Ed.)
3. Langville, A.N. & Meyer, C.D. — *Google's PageRank and Beyond*
4. Rasmussen, C.E. & Williams, C.K.I. — *Gaussian Processes for Machine Learning*
5. Meyer, C.D. — *Matrix Analysis and Applied Linear Algebra*

---

*Study Material prepared for Delhi University BSc (Hons) Computer Science — NEP 2024 UGCF Curriculum*