# Vector Space And Subspaces

## A Comprehensive Study Material for BSc (Hons) Computer Science

### Delhi University NEP 2024 UGCF - Mathematics For Computing

---

## 1. Introduction

Welcome to this comprehensive study material on **Vector Spaces and Subspaces**, a fundamental topic in linear algebra that forms the mathematical backbone of modern computing. This unit aligns with the Delhi University NEP 2024 UGCF curriculum for BSc (Hons) Computer Science students.

### 1.1 Why This Topic Matters in Computing

Vector spaces are not just abstract mathematical constructs—they are the invisible framework behind many technologies you use daily:

- **Machine Learning & Data Science**: Neural networks operate in high-dimensional vector spaces. Image recognition, natural language processing, and recommendation systems all rely on vector representations.
- **Computer Graphics**: Every pixel, image, and 3D model is represented as vectors in coordinate spaces. Transformations, rotations, and scaling are all linear operations in vector spaces.
- **Search Engines**: Google PageRank uses eigenvector centrality—operating in vector space theory—to rank web pages.
- **Cryptography**: Lattice-based cryptography, crucial for post-quantum security, is built on vector space concepts.
- **Computer Vision**: Feature extraction and object recognition happen in vector spaces.
- **Data Compression**: Techniques like PCA (Principal Component Analysis) reduce dimensions in vector spaces.

As a computer science student, understanding vector spaces will empower you to grasp these technologies at their mathematical core.

---

## 2. Vector Spaces: Foundations

### 2.1 What is a Vector Space?

A **vector space** (also called a **linear space**) is a set of objects called **vectors**, equipped with two operations:

1. **Vector Addition**: Combining two vectors to produce a third
2. **Scalar Multiplication**: Multiplying a vector by a number (scalar) to produce another vector

These operations must satisfy ten specific axioms.

### 2.2 Formal Definition

A set **V** is a **vector space** over a field **F** (typically ℝ—real numbers or ℂ—complex numbers) if the following ten axioms hold for all vectors **u, v, w ∈ V** and all scalars **a, b ∈ F**:

| Axiom | Description |
|-------|-------------|
| **Closure under Addition** | If **u, v ∈ V**, then **u + v ∈ V** |
| **Closure under Scalar Multiplication** | If **v ∈ V** and **a ∈ F**, then **a·v ∈ V** |
| **Commutativity of Addition** | **u + v = v + u** |
| **Associativity of Addition** | **(u + v) + w = u + (v + w)** |
| **Additive Identity** | There exists **0 ∈ V** such that **v + 0 = v** |
| **Additive Inverse** | For each **v ∈ V**, there exists **-v ∈ V** such that **v + (-v) = 0** |
| **Associativity of Scalar Multiplication** | **a(bv) = (ab)v** |
| **Distributivity (Scalar over Vector)** | **a(u + v) = au + av** |
| **Distributivity (Vector over Scalar)** | **(a + b)v = av + bv** |
| **Multiplicative Identity** | **1·v = v** |

### 2.3 Key Observations

> **Important**: The field **F** is usually ℝ (real numbers) for most CS applications. When we say "vector space over ℝ," we mean real vector space.

> **The Zero Vector**: Every vector space must contain an additive identity (zero vector), denoted **0**. This is crucial for many proofs and applications.

---

## 3. Examples of Vector Spaces

Understanding vector spaces requires seeing them in various contexts. Here are the most important examples:

### 3.1 Standard Vector Spaces

**Example 1: ℝⁿ (n-dimensional Euclidean Space)**

The set of all n-tuples of real numbers is a vector space:

$$\mathbb{R}^n = \{(x_1, x_2, ..., x_n) : x_i \in \mathbb{R}\}$$

- **Vector Addition**: (x₁, x₂) + (y₁, y₂) = (x₁+y₁, x₂+y₂)
- **Scalar Multiplication**: a·(x₁, x₂) = (ax₁, ax₂)

For instance, ℝ² represents the 2D plane, and ℝ³ represents 3D space.

**Example 2: Space of Matrices**

The set of all m×n matrices, denoted **M(m,n)**, forms a vector space:

$$\begin{pmatrix} a & b \\ c & d \end{pmatrix} + \begin{pmatrix} e & f \\ g & h \end{pmatrix} = \begin{pmatrix} a+e & b+f \\ c+g & d+h \end{pmatrix}$$

This is crucial in machine learning where matrices represent datasets and transformations.

**Example 3: Space of Polynomials**

The set of all polynomials of degree ≤ n is a vector space. For degree ≤ 2:

$$P_2 = \{a + bx + cx^2 : a, b, c \in \mathbb{R}\}$$

### 3.2 Function Spaces (Advanced CS Relevance)

The set of all functions from ℝ to ℝ forms an **infinite-dimensional** vector space. This is foundational in:

- Signal processing
- Neural network theory
- Functional programming concepts

---

## 4. Subspaces

### 4.1 Definition

A **subspace** of a vector space **V** is a subset **W** that is itself a vector space under the same operations as **V**.

### 4.2 The Subspace Test

To verify if a subset **W** is a subspace of **V**, you only need to check **three conditions**:

> **W is a subspace of V if and only if:**
> 1. **W is non-empty** (contains the zero vector: **0 ∈ W**)
> 2. **Closed under addition**: If **u, v ∈ W**, then **u + v ∈ W**
> 3. **Closed under scalar multiplication**: If **v ∈ W** and **a ∈ ℝ**, then **a·v ∈ W**

### 4.3 Examples of Subspaces

**Example 1: Lines Through the Origin**

In ℝ², any line passing through the origin (0,0) is a subspace:

$$W = \{(x, y) : y = mx\} = \{(t, mt) : t \in \mathbb{R}\}$$

- Contains (0,0): yes, when t=0
- Closed under addition: (t₁, mt₁) + (t₂, mt₂) = (t₁+t₂, m(t₁+t₂)) ∈ W
- Closed under scalar multiplication: a(t, mt) = (at, mat) ∈ W

**Example 2: The xy-plane in ℝ³**

$$W = \{(x, y, 0) : x, y \in \mathbb{R}\}$$

This is a 2D plane (subspace) inside 3D space.

**Example 3: Space of Symmetric Matrices**

The set of all symmetric matrices is a subspace of M(n,n).

### 4.4 Trivial Subspaces

Every vector space has two **trivial subspaces**:

1. **{0}** — the set containing only the zero vector
2. **V** — the vector space itself

These are called **improper subspaces**. All other subspaces are **proper subspaces**.

---

## 5. Linear Combinations and Span

### 5.1 Linear Combination

Given vectors **v₁, v₂, ..., vₖ** in a vector space **V**, a **linear combination** is:

$$a_1v_1 + a_2v_2 + ... + a_kv_k$$

where **a₁, a₂, ..., aₖ** are scalars.

### 5.2 Span

The **span** of a set of vectors **S = {v₁, v₂, ..., vₖ}** is the set of ALL linear combinations:

$$span(S) = \{a_1v_1 + a_2v_2 + ... + a_kv_k : a_i \in \mathbb{R}\}$$

> **Interpretation**: The span represents all vectors that can be "reached" or "generated" by the given set of vectors.

### 5.3 Geometric Interpretation

- In ℝ², the span of a single non-zero vector is a **line** through the origin.
- In ℝ², the span of two non-collinear vectors is the **entire plane** ℝ².
- In ℝ³, the span of one vector is a line, two non-parallel vectors form a plane, and three non-coplanar vectors fill ℝ³.

---

## 6. Linear Independence

This is one of the most critical concepts in linear algebra—often tested in exams but previously under-explained.

### 6.1 Definition

A set of vectors **{v₁, v₂, ..., vₖ}** is **linearly dependent** if there exist scalars **a₁, a₂, ..., aₖ**, **not all zero**, such that:

$$a_1v_1 + a_2v_2 + ... + a_kv_k = 0$$

Conversely, the set is **linearly independent** if:

$$a_1v_1 + a_2v_2 + ... + a_kv_k = 0 \implies a_1 = a_2 = ... = a_k = 0$$

### 6.2 Understanding the Definition

**Linearly Independent**: No vector in the set can be written as a combination of the others. Each vector adds "new direction" or "new information."

**Linearly Dependent**: At least one vector is redundant—it can be expressed as a combination of the others.

### 6.3 Examples

**Example 1: Independent Vectors in ℝ³**

$$v_1 = (1, 0, 0), v_2 = (0, 1, 0), v_3 = (0, 0, 1)$$

These are linearly independent because:

$$a(1,0,0) + b(0,1,0) + c(0,0,1) = (0,0,0)$$

implies a = b = c = 0.

**Example 2: Dependent Vectors**

$$v_1 = (1, 2, 3), v_2 = (2, 4, 6)$$

These are dependent because v₂ = 2·v₁, so:

$$2v_1 - v_2 = 0$$

### 6.4 Practical Insight

> **In CS applications**: Linearly independent vectors represent **unique features** or **non-redundant information**. When features are linearly dependent, we have redundant data—crucial insight for:
>
> - **Dimensionality reduction** (removing redundant features)
> - **Principal Component Analysis (PCA)**
> - **Feature engineering** in machine learning

---

## 7. Basis and Dimension

### 7.1 Definition of Basis

A **basis** for a vector space **V** is a set of vectors **B** that satisfies:

1. **B is linearly independent**
2. **B spans V** (span(B) = V)

### 7.2 Examples of Bases

**Standard Basis for ℝ³:**

$$e_1 = (1, 0, 0), e_2 = (0, 1, 0), e_3 = (0, 0, 1)$$

Every vector (x, y, z) can be written as: x·e₁ + y·e₂ + z·e₃

**Standard Basis for Matrix Space:**

The 2×2 identity matrices form a basis for M(2,2):

$$E_{11} = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}, E_{12} = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}, E_{21} = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}, E_{22} = \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}$$

### 7.3 Dimension

The **dimension** of a vector space **V** (denoted dim(V)) is the number of vectors in any basis for **V**.

> **Key Theorem**: All bases of a vector space have the same number of elements.

| Vector Space | Dimension |
|--------------|------------|
| ℝⁿ | n |
| M(m,n) | m × n |
| Pₙ (polynomials degree ≤ n) | n + 1 |
| {0} | 0 |

### 7.4 Dimension and Subspaces (Important Theorem)

For a subspace **W** of a finite-dimensional vector space **V**:

$$\dim(W) \leq \dim(V)$$

And if **dim(W) = dim(V)**, then **W = V**.

---

## 8. Practical Computing Applications

### 8.1 Machine Learning: Feature Spaces

In machine learning, your dataset forms a vector space:

```python
import numpy as np

# Consider a dataset with 4 features (4-dimensional vector space)
# Each data point is a vector in ℝ⁴
data_point = np.array([25, 175, 72, 8.5])  # age, height, weight, score

# A dataset of 100 samples lives in ℝ⁴
# Each feature forms a subspace
# Understanding linear independence helps identify redundant features
```

### 8.2 Computer Graphics: Coordinate Systems

3D graphics use basis vectors for transformations:

```python
import numpy as np

# Standard basis for 3D graphics
i = np.array([1, 0, 0])  # x-axis
j = np.array([0, 1, 0])  # y-axis
k = np.array([0, 0, 1])  # z-axis

# A point in 3D space
point = 3*i + 2*j + 1*k  # (3, 2, 1)

# Rotation matrices perform linear transformations
# These are operations within the vector space ℝ³
```

### 8.3 Data Science: Dimensionality Reduction

PCA uses basis and dimension concepts:

```python
# PCA finds the "best" basis (principal components)
# that captures maximum variance with fewer dimensions

from sklearn.decomposition import PCA
import numpy as np

# Data with 100 features (100-dimensional space)
data = np.random.rand(1000, 100)

# Reduce to 10-dimensional subspace
pca = PCA(n_components=10)
reduced_data = pca.fit_transform(data)

# The 10 principal components form a basis for the reduced space
print(f"Explained variance ratio: {pca.explained_variance_ratio_}")
```

### 8.4 Quantum Computing

Quantum states exist in complex vector spaces (Hilbert spaces):

- Qubits are vectors in ℂ²
- Quantum gates are linear transformations (matrices)
- Quantum entanglement involves subspace concepts

### 8.5 Search Engines: PageRank

Google's PageRank uses eigenvectors—a concept from vector space theory:

- Web pages form nodes in a directed graph
- The PageRank vector is the principal eigenvector of the link matrix
- This lives in a high-dimensional vector space

---

## 9. Comprehensive Examples with Code

### Example 1: Verifying Vector Space Properties in Python

```python
import numpy as np

# Define vector space ℝ² operations
def vector_add(v1, v2):
    return np.add(v1, v2)

def scalar_mult(scalar, vector):
    return np.multiply(scalar, vector)

def zero_vector(dim):
    return np.zeros(dim)

# Test the vector space axioms
v1 = np.array([1, 2])
v2 = np.array([3, 4])
v3 = np.array([5, 6])
a, b = 3, 2

# Closure under addition
result = vector_add(v1, v2)
print(f"Closure under addition: {result}")  # [4 6]

# Closure under scalar multiplication
result = scalar_mult(a, v1)
print(f"Scalar multiplication: {result}")  # [3 6]

# Commutativity
print(f"Commutative: {np.array_equal(v1 + v2, v2 + v1)}")  # True

# Associativity
print(f"Associative: {np.array_equal((v1 + v2) + v3, v1 + (v2 + v3))}")  # True

# Additive identity
zero = zero_vector(2)
print(f"Additive identity: {np.array_equal(v1 + zero, v1)}")  # True

# Additive inverse
print(f"Additive inverse: {np.array_equal(v1 + (-v1), zero)}")  # True
```

### Example 2: Linear Independence and Span in NumPy

```python
import numpy as np

def check_linear_independent(vectors):
    """Check if vectors are linearly independent"""
    matrix = np.column_stack(vectors)
    rank = np.linalg.matrix_rank(matrix)
    return rank == len(vectors)

# Example 1: Independent vectors in ℝ³
v1 = np.array([1, 0, 0])
v2 = np.array([0, 1, 0])
v3 = np.array([0, 0, 1])

print(f"Independent (3D standard basis): {check_linear_independent([v1, v2, v3])}")
# Output: True

# Example 2: Dependent vectors
w1 = np.array([1, 2, 3])
w2 = np.array([2, 4, 6])  # w2 = 2 * w1

print(f"Dependent vectors: {check_linear_independent([w1, w2])}")
# Output: False

# Example 3: Span verification
def is_in_span(vectors, target):
    """Check if target is in the span of vectors"""
    A = np.column_stack(vectors)
    try:
        coeffs = np.linalg.lstsq(A, target, rcond=None)[0]
        reconstruction = A @ coeffs
        return np.allclose(target, reconstruction), coeffs
    except:
        return False, None

# Check if (3, 3, 3) is in span of v1, v2, v3
result, coeffs = is_in_span([v1, v2, v3], np.array([3, 3, 3]))
print(f"In span: {result}, coefficients: {coeffs}")
# Output: True, coefficients: [3. 3. 3.]
```

---

## 10. Delhi University Examination Focus Areas

Based on the NEP 2024 UGCF syllabus, prepare for:

1. **Definition Problems**: Verify if a given set is a vector space/subspace
2. **Subspace Tests**: Apply the three conditions to prove subspace status
3. **Linear Independence**: Determine if given vectors are linearly independent
4. **Span Problems**: Find span and determine if a vector belongs to span
5. **Basis Problems**: Find basis for given subspaces
6. **Dimension Calculations**: Compute dimensions of various spaces

---

## Key Takeaways

### Core Concepts

1. **Vector Space**: A set with vector addition and scalar multiplication satisfying 10 axioms
2. **Subspace**: A subset that is itself a vector space (contains zero, closed under addition and scalar multiplication)
3. **Linear Combination**: Sum of scalar multiples of vectors
4. **Span**: Set of all possible linear combinations—a subspace itself
5. **Linear Independence**: Vectors are independent if only the trivial combination produces zero
6. **Basis**: A linearly independent set that spans the entire space
7. **Dimension**: Number of vectors in any basis (unique for a given space)

### CS Applications Summary

- **Machine Learning**: Feature spaces, dimensionality reduction
- **Computer Graphics**: 3D transformations, coordinate systems
- **Data Science**: PCA, feature engineering
- **Search Engines**: PageRank algorithm
- **Quantum Computing**: State spaces and quantum gates

### Remember

> - Every vector space contains the **zero vector**
> - **Linearly independent** means "no redundancy"
> - **Basis** provides a "coordinate system" for the space
> - **Dimension** tells you "how many numbers" you need to describe any vector
> - All bases of a vector space have the **same number of elements**

---

*This study material is designed for BSc (Hons) Computer Science, Delhi University NEP 2024 UGCF Curriculum. For further reading, consult "Linear Algebra and Its Applications" by David C. Lay or "Mathematics for Computer Science" by Lehman, Leighton, and Meyer.*