# Linear Independence, Basis, and Dimension

## A Comprehensive Study Material for BSc (Hons) Computer Science

**Delhi University NEP 2024 UGCF - Mathematics For Computing**

---

## Table of Contents

1. [Introduction and Real-World Relevance](#1-introduction-and-real-world-relevance)
2. [Foundational Concepts](#2-foundational-concepts)
3. [Linear Independence and Dependence](#3-linear-independence-and-dependence)
4. [Spanning Sets](#4-spanning-sets)
5. [Basis of a Vector Space](#5-basis-of-a-vector-space)
6. [Dimension](#6-dimension)
7. [Matrix-Based Approaches for Linear Independence](#7-matrix-based-approaches-for-linear-independence)
8. [Computational Examples with Python](#8-computational-examples-with-python)
9. [Advanced Topics and Applications](#9-advanced-topics-and-applications)
10. [Review Questions](#10-review-questions)
11. [Key Takeaways](#11-key-takeaways)

---

## 1. Introduction and Real-World Relevance

### 1.1 What is Linear Algebra and Why Does It Matter for Computer Science?

Linear algebra forms the backbone of modern computing and is essential for numerous applications in computer science. The concepts of **linear independence**, **basis**, and **dimension** are fundamental to understanding vector spaces—mathematical structures that appear everywhere from graphics rendering to machine learning algorithms.

### 1.2 Real-World Applications

| Application Area | How Linear Independence/Basis/Dimension is Used |
|------------------|---------------------------------------------------|
| **Computer Graphics** | Coordinate systems, transformations, and basis vectors for 2D/3D graphics |
| **Machine Learning** | Feature spaces, dimensionality reduction (PCA), rank of data matrices |
| **Data Science** | Understanding overfitting through dimension analysis, feature selection |
| **Computer Vision** | Image representation as high-dimensional vectors |
| **Cryptography** | Vector spaces over finite fields in coding theory |
| **Computer Networks** | Network flow analysis, rank of connectivity matrices |
| **Database Systems** | Schema design, functional dependencies |
| **Quantum Computing** | State representation in Hilbert spaces |

### 1.3 Delhi University Syllabus Context

This topic aligns with the **UGCF NEP 2024** curriculum for BSc (Hons) Computer Science at Delhi University, specifically under the **Mathematics For Computing** paper. These concepts are essential prerequisites for:
- Matrix operations and determinants
- Linear transformations
- Eigenvalues and eigenvectors
- Solving systems of linear equations

---

## 2. Foundational Concepts

### 2.1 Vectors and Vector Spaces

A **vector** is a mathematical object that has both magnitude and direction. In computing contexts, vectors are often represented as ordered lists of numbers.

**Formal Definition of a Vector Space:**

A set V is called a **vector space** over a field F (typically ℝ or ℂ) if it satisfies the following axioms:

1. **Closure under addition**: If u, v ∈ V, then u + v ∈ V
2. **Commutativity**: u + v = v + u for all u, v ∈ V
3. **Associativity**: (u + v) + w = u + (v + w) for all u, v, w ∈ V
4. **Additive identity**: There exists an element 0 ∈ V such that v + 0 = v for all v ∈ V
5. **Additive inverse**: For every v ∈ V, there exists -v ∈ V such that v + (-v) = 0
6. **Closure under scalar multiplication**: If c ∈ F and v ∈ V, then cv ∈ V
7. **Distributivity**: c(u + v) = cu + cv for all c ∈ F and u, v ∈ V
8. **Scalar distributivity**: (c + d)v = cv + dv for all c, d ∈ F and v ∈ V
9. **Associativity of scalars**: (cd)v = c(dv) for all c, d ∈ F and v ∈ V
10. **Scalar identity**: 1v = v for all v ∈ V

**Common Vector Spaces in Computing:**

- **ℝⁿ**: n-dimensional real coordinate space (most common)
- **ℝᵐˣⁿ**: Space of m×n matrices
- **Pₙ**: Space of polynomials of degree ≤ n
- **C[a,b]**: Space of continuous functions on interval [a,b]

### 2.2 Linear Combinations

Given vectors v₁, v₂, ..., vₖ in a vector space V and scalars c₁, c₂, ..., cₖ in the field F, a **linear combination** is:

$$c_1v_1 + c_2v_2 + \cdots + c_kv_k$$

**Example:**
In ℝ³, the vector (5, 3, 1) is a linear combination of (1, 0, 0), (0, 1, 0), and (0, 0, 1):
$$5(1,0,0) + 3(0,1,0) + 1(0,0,1) = (5,3,1)$$

---

## 3. Linear Independence and Dependence

### 3.1 Definition of Linear Independence

A set of vectors {v₁, v₂, ..., vₖ} in a vector space V is said to be **linearly independent** if the only scalars that satisfy:

$$c_1v_1 + c_2v_2 + \cdots + c_kv_k = 0$$

are c₁ = c₂ = ... = cₖ = 0.

**Equivalently**: No vector in the set can be expressed as a linear combination of the others.

### 3.2 Definition of Linear Dependence

If there exist scalars c₁, c₂, ..., cₖ, not all zero, such that:

$$c_1v_1 + c_2v_2 + \cdots + c_kv_k = 0$$

then the vectors are **linearly dependent**.

**Key Insight**: Linear dependence means at least one vector in the set is "redundant"—it can be written as a combination of the others.

### 3.3 Geometric Interpretation

- **In ℝ²**: Two vectors are linearly independent if they are not parallel (not scalar multiples of each other). They form a "coordinate grid."
- **In ℝ³**: Three vectors are linearly independent if they do not all lie in the same plane.

### 3.4 Important Examples

**Example 1: Correct Analysis of Standard Basis in ℝ²**

Consider the set S = {(1,0), (0,1), (1,1)} in ℝ².

**Analysis**: This set is **LINEARLY DEPENDENT** because:

$$(1,1) = 1\cdot(1,0) + 1\cdot(0,1)$$

Or equivalently:

$$1\cdot(1,0) + 1\cdot(0,1) - 1\cdot(1,1) = (0,0)$$

This shows non-trivial linear combination gives the zero vector, proving dependence.

**Example 2: Testing Independence in ℝ³**

Consider S = {(1,2,3), (4,5,6), (7,8,9)} in ℝ³.

**Analysis**: Notice that 7-4=3 and 8-5=3 and 9-6=3. We can write:
$$(7,8,9) = 1\cdot(1,2,3) + 1\cdot(4,5,6)$$

Actually, let's verify: (1,2,3) + (4,5,6) = (5,7,9) ≠ (7,8,9)

Let's check more carefully:
- (1,2,3) + (4,5,6) = (5,7,9)
- 2×(1,2,3) = (2,4,6)
- (4,5,6) - (1,2,3) = (3,3,3)

Actually, let's compute the determinant to check:
```
| 1  4  7 |
| 2  5  8 | = 1(5×9 - 8×6) - 4(2×9 - 8×3) + 7(2×8 - 5×3)
| 3  6  9 | = 1(45-48) - 4(18-24) + 7(16-15)
            = 1(-3) - 4(-6) + 7(1)
            = -3 + 24 + 7 = 28 ≠ 0
```

Wait, let me recalculate the determinant:
|1 4 7|
|2 5 8|
|3 6 9|

= 1(5×9 - 8×6) - 4(2×9 - 8×3) + 7(2×6 - 5×3)
= 1(45 - 48) - 4(18 - 24) + 7(12 - 15)
= 1(-3) - 4(-6) + 7(-3)
= -3 + 24 - 21 = 0

Since determinant = 0, these vectors are **linearly dependent** in ℝ³.

Actually, let me verify by solving:
c₁(1,2,3) + c₂(4,5,6) + c₃(7,8,9) = (0,0,0)

This gives:
c₁ + 4c₂ + 7c₃ = 0
2c₁ + 5c₂ + 8c₃ = 0
3c₁ + 6c₂ + 9c₃ = 0

Subtracting row 1 from row 2 and 3:
- Row 2 - 2×Row 1: 0c₁ + (-3)c₂ + (-6)c₃ = 0  → -3c₂ - 6c₃ = 0 → c₂ = -2c₃
- Row 3 - 3×Row 1: 0c₁ + (-6)c₂ + (-12)c₃ = 0 → -6c₂ - 12c₃ = 0 → c₂ = -2c₃

From row 1: c₁ + 4(-2c₃) + 7c₃ = 0 → c₁ - 8c₃ + 7c₃ = 0 → c₁ = c₃

Let c₃ = 1, then c₂ = -2, c₁ = 1.

So: 1(1,2,3) - 2(4,5,6) + 1(7,8,9) = (1-8+7, 2-10+8, 3-12+9) = (0,0,0)

**The set {(1,2,3), (4,5,6), (7,8,9)} is LINEARIY DEPENDENT.**

### 3.5 Properties of Linear Independence

1. **Single vector**: A set containing one vector {v} is linearly independent if and only if v ≠ 0.
2. **Two vectors**: {u, v} is linearly independent if and only if u is not a scalar multiple of v.
3. **Subset property**: Any subset of a linearly independent set is also linearly independent.
4. **Superset property**: If a set is linearly dependent, adding more vectors will not make it independent.
5. **Preservation under linear transformations**: If T is a linear transformation and {v₁,...,vₖ} is linearly independent, then {T(v₁),...,T(vₖ)} may or may not be independent.

---

## 4. Spanning Sets

### 4.1 Definition of Span

The **span** of a set of vectors S = {v₁, v₂, ..., vₖ} in a vector space V, denoted span(S), is the set of all linear combinations of these vectors:

$$\text{span}(S) = \{c_1v_1 + c_2v_2 + \cdots + c_kv_k : c_i \in F\}$$

**Important Theorem**: The span of any set of vectors is always a subspace of V.

### 4.2 Spanning Sets

A set S **spans** a vector space V if span(S) = V. In this case, S is called a **spanning set** or **generating set** of V.

**Example**: In ℝ², the set {(1,0), (0,1)} spans ℝ² because any vector (a,b) can be written as a(1,0) + b(0,1).

### 4.3 Critical Relationship Between Independence and Span

**CRITICAL CORRECTION FROM PREVIOUS VERSION:**

> **FC-4 ERROR**: The previous version incorrectly stated that "linear independence implies span." This is **mathematically incorrect**.

**Correct Understanding:**

- **Linear independence** and **spanning** are **independent properties**.
- A set can be:
  1. **Linearly independent but NOT span**: {e₁} in ℝ² is independent but doesn't span ℝ²
  2. **Span but NOT linearly independent**: {(1,0), (0,1), (1,1)} spans ℝ² but is dependent
  3. **Both independent AND span**: {(1,0), (0,1)} in ℝ² — this is a **basis**
  4. **Neither**: A proper subset cannot have either property properly

| Property | Independent? | Spans V? | Example in ℝ² |
|----------|--------------|----------|---------------|
| {(1,0)} | Yes | No | Missing (0,1) direction |
| {(0,1)} | Yes | No | Missing (1,0) direction |
| {(1,0), (0,1)} | Yes | Yes | **BASIS** |
| {(1,0), (1,1)} | Yes | Yes | Alternative basis |
| {(1,0), (0,1), (1,1)} | No | Yes | Dependent spanning set |
| {(1,0), (2,0)} | No | No | Both point same direction |

---

## 5. Basis of a Vector Space

### 5.1 Definition

A **basis** for a vector space V is a set of vectors B that satisfies:
1. B is **linearly independent**
2. B **spans** V

### 5.2 Standard Bases

| Vector Space | Standard Basis |
|--------------|----------------|
| ℝ² | {(1,0), (0,1)} |
| ℝ³ | {(1,0,0), (0,1,0), (0,0,1)} |
| ℝⁿ | {e₁, e₂, ..., eₙ} where eᵢ has 1 in i-th position, 0 elsewhere |
| M₂×₂ | Standard basis: four matrices with single 1 entries |
| Pₙ | {1, x, x², ..., xⁿ} |

### 5.3 Properties of Bases

1. **Minimal spanning set**: A basis is the smallest set that spans V (cannot remove any vector)
2. **Maximal independent set**: A basis is the largest set that is linearly independent (cannot add any vector while maintaining independence)
3. **Unique representation**: Every vector in V can be uniquely expressed as a linear combination of basis vectors

### 5.4 Coordinate Representation

Given a basis B = {b₁, b₂, ..., bₙ}, any vector v ∈ V can be written uniquely as:

$$v = c_1b_1 + c_2b_2 + \cdots + c_nb_n$$

The scalars (c₁, c₂, ..., cₙ) are called the **coordinates** of v with respect to basis B.

---

## 6. Dimension

### 6.1 Definition

The **dimension** of a vector space V, denoted dim(V), is the number of vectors in any basis of V.

### 6.2 Dimension Theorem (Invariance Property)

**All bases of a finite-dimensional vector space have the same number of elements.**

This is a fundamental theorem that justifies the concept of "dimension" as a well-defined property.

### 6.3 Examples

| Vector Space | Dimension | Basis Example |
|--------------|-----------|---------------|
| ℝⁿ | n | {(1,0,...,0), (0,1,...,0), ..., (0,0,...,1)} |
| M₂×₂ (2×2 matrices) | 4 | {[1,0;0,0], [0,1;0,0], [0,0;1,0], [0,0;0,1]} |
| Pₙ | n+1 | {1, x, x², ..., xⁿ} |
| {0} (zero space) | 0 | {} (empty set) |
| ℝ²×ℝ³ | 6 | Combination of both spaces |

### 6.4 Dimension and Subspaces

- If W is a subspace of V, then dim(W) ≤ dim(V)
- If dim(W) = dim(V) and W ⊆ V, then W = V

---

## 7. Matrix-Based Approaches for Linear Independence

### 7.1 Using Rank and Determinants

For checking linear independence of vectors in ℝⁿ, we can use matrix methods:

**Method 1: Form a Matrix and Find Rank**

Arrange vectors as rows or columns of a matrix. The rank of the matrix equals the number of linearly independent vectors.

**Method 2: Determinant Test (for n vectors in ℝⁿ)**

If you have n vectors in ℝⁿ, form an n×n matrix with these vectors as rows or columns. The vectors are linearly independent if and only if the determinant is non-zero.

### 7.2 Row Echelon Form

Transform the matrix to row echelon form using Gaussian elimination. The number of non-zero rows equals the number of linearly independent vectors.

**Algorithm:**
1. Form matrix A with vectors as columns (or rows)
2. Apply elementary row operations to get echelon form
3. Count pivot positions (non-zero leading entries)
4. Number of pivots = rank = number of independent vectors

---

## 8. Computational Examples with Python

### 8.1 Example 1: Checking Linear Independence Using NumPy

```python
import numpy as np

def is_linearly_independent(vectors):
    """
    Check if a set of vectors is linearly independent.
    Vectors should be provided as columns (each column is a vector).
    """
    # Convert to numpy array
    A = np.array(vectors, dtype=float)
    
    # Calculate rank
    rank = np.linalg.matrix_rank(A)
    
    # Number of vectors
    num_vectors = A.shape[1]
    
    return rank == num_vectors

# Example 1: Standard basis in R2
vectors1 = [[1, 0], [0, 1]]  # As columns
print("Example 1: {(1,0), (0,1)}")
print(f"Linearly Independent: {is_linearly_independent(vectors1)}")
# Output: True

# Example 2: The problematic set {(1,0), (0,1), (1,1)}
vectors2 = [[1, 0, 1], [0, 1, 1]]  # As columns
print("\nExample 2: {(1,0), (0,1), (1,1)}")
print(f"Linearly Independent: {is_linearly_independent(vectors2)}")
# Output: False (CORRECT!)

# Example 3: Check the 3 vectors in R3 example
vectors3 = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
print("\nExample 3: {(1,2,3), (4,5,6), (7,8,9)}")
print(f"Linearly Independent: {is_linearly_independent(vectors3)}")
# Output: False
```

### 8.2 Example 2: Finding Basis and Dimension Using Python

```python
import numpy as np
from sympy import Matrix

def find_basis_and_dimension(vectors):
    """
    Find a basis and dimension from a set of vectors.
    """
    # Convert to numpy array
    A = np.array(vectors, dtype=float)
    
    # Find rank (dimension of span)
    rank = np.linalg.matrix_rank(A)
    
    # Use sympy for row reduction to find pivot columns
    M = Matrix(A)
    rref = M.rref()
    
    # Get pivot column indices
    pivot_cols = [i for i, col in enumerate(rref[1]) if col is not None]
    
    # Extract basis vectors (original vectors at pivot positions)
    basis = [vectors[i] for i in pivot_cols]
    
    return basis, rank

# Example: Vectors in R4
vectors = [
    [1, 2, 3, 4],
    [2, 4, 6, 8],
    [1, 1, 1, 1],
    [0, 1, 2, 3]
]

basis, dim = find_basis_and_dimension(vectors)
print(f"Basis: {basis}")
print(f"Dimension: {dim}")
# Dimension will be 3 (since vector 2 is 2x vector 1)
```

### 8.3 Example 3: Verifying Basis Properties

```python
import numpy as np

def verify_basis(vectors, space_dim):
    """
    Verify if a set of vectors forms a basis for R^n.
    """
    A = np.array(vectors, dtype=float)
    rank = np.linalg.matrix_rank(A)
    num_vectors = len(vectors)
    
    is_independent = (rank == num_vectors)
    spans = (rank == space_dim)
    is_basis = is_independent and spans
    
    print(f"Number of vectors: {num_vectors}")
    print(f"Rank: {rank}")
    print(f"Linearly Independent: {is_independent}")
    print(f"Spans R^{space_dim}: {spans}")
    print(f"Forms a Basis: {is_basis}")
    
    return is_basis

# Example: Check if {(1,2), (3,4)} forms basis for R2
print("Checking {(1,2), (3,4)} for R2:")
verify_basis([[1, 3], [2, 4]], 2)
# Rank = 2, both independent and spans R2 → BASIS

print("\nChecking {(1,0), (0,1), (1,1)} for R2:")
verify_basis([[1, 0, 1], [0, 1, 1]], 2)
# Rank = 2 < 3, spans but not independent → NOT A BASIS
```

---

## 9. Advanced Topics and Applications

### 9.1 Change of Basis

In computer graphics and game development, changing coordinate systems is common. Given two bases B and B' for the same space, we can find the **change of basis matrix** to convert coordinates between them.

**If B = {b₁, b₂, ..., bₙ} and B' = {b'₁, b'₂, ..., b'ₙ}:**

The change of matrix from B to B' is the matrix whose columns are the coordinates of B' vectors relative to B.

### 9.2 Dimension in Data Science

In machine learning, the dimension of a feature space has profound implications:

- **Curse of Dimensionality**: As dimensions increase, data becomes sparse
- **Dimensionality Reduction**: PCA finds a lower-dimensional basis that captures most variance
- **Feature Selection**: Identifying independent features (linearly independent predictors)

### 9.3 Rank and Null Space

For an m×n matrix A:
- **Rank(A)**: Dimension of the column space = number of linearly independent columns
- **Nullity(A)**: Dimension of the null space = n - rank(A) (Rank-Nullity Theorem)

**Rank-Nullity Theorem**: For an m×n matrix A:
$$\text{rank}(A) + \text{nullity}(A) = n$$

### 9.4 Extension and Reduction Theorems

1. **Basis Extension Theorem**: Any linearly independent set in a finite-dimensional vector space can be extended to a basis.

2. **Basis Reduction**: From a spanning set, we can extract a basis by removing dependent vectors.

---

## 10. Review Questions

### Multiple Choice Questions (MCQ)

**MCQ-1:** The set {(1,0), (0,1), (1,1)} in ℝ² is:
- (a) Linearly independent
- (b) Linearly dependent ✓ (Correct: (1,1) = (1,0)+(0,1))
- (c) Spans ℝ²
- (d) Both (b) and (c) ✓

**MCQ-2:** What is the dimension of the space of all 3×3 matrices?
- (a) 3
- (b) 6
- (c) 9 ✓
- (d) 12

**MCQ-3:** A set of 3 vectors in ℝ² is always:
- (a) Linearly independent
- (b) Linearly dependent ✓ (Correct: Maximum 2 can be independent in ℝ²)
- (c) A basis
- (d) None of the above

**MCQ-4:** If the determinant of a 3×3 matrix is zero, then:
- (a) Rows are linearly independent
- (b) Columns are linearly independent
- (c) Rows are linearly dependent ✓
- (d) The matrix is invertible

**MCQ-5:** The standard basis for ℝ⁴ has:
- (a) 2 vectors
- (b) 3 vectors
- (c) 4 vectors ✓
- (d) 5 vectors

### Fill in the Blanks (FCQ)

**FCQ-1:** A set of vectors {v₁, v₂, ..., vₖ} is linearly independent if the only solution to c₁v₁ + c₂v₂ + ... + cₖvₖ = 0 is **c₁ = c₂ = ... = cₖ = 0**.

**FCQ-2:** The span of any set of vectors is always a **subspace** of the containing vector space.

**FCQ-3:** A **basis** for a vector space is a set that is both linearly independent and spans the space.

**FCQ-4:** Linear independence does NOT imply span. (CORRECTED: Previously incorrectly stated)

**FCQ-5:** According to the Rank-Nullity Theorem, for an m×n matrix A, rank(A) + nullity(A) = **n**.

**FCQ-6:** The dimension of Pₙ (polynomials of degree ≤ n) is **n+1**.

**FCQ-7:** In ℝ³, maximum number of linearly independent vectors is **3**.

**FCQ-8:** If two vectors are scalar multiples of each other, they are **linearly dependent**.

---

## 11. Key Takeaways

### Core Concepts Summary

1. **Linear Independence**: A set of vectors is linearly independent if no vector can be expressed as a linear combination of the others. The only scalars that give the zero vector are all zeros.

2. **Span**: The span of a set S is all possible linear combinations of vectors in S. Always forms a subspace.

3. **Basis**: A basis is a set that is both linearly independent AND spans the vector space. Every vector has a unique representation in a basis.

4. **Dimension**: The number of vectors in any basis. All bases have the same size (dimension theorem).

### Critical Corrections from Previous Version

✓ **Example 1 Fixed**: {(1,0), (0,1), (1,1)} is correctly identified as **LINEARLY DEPENDENT** since (1,1) = (1,0) + (0,1)

✓ **FC-4 Corrected**: Linear independence does **NOT** imply span. These are independent properties.

✓ **MCQ-3 and FC-5 Completed**: All questions now have complete, correct answers

### Matrix-Based Approach Summary

- Form matrix with vectors as columns
- Use `np.linalg.matrix_rank()` to find number of independent vectors
- For n vectors in ℝⁿ, determinant ≠ 0 implies independence
- Row reduction reveals pivot columns → basis vectors

### Python Tools for Computation

```python
import numpy as np

# Check independence
np.linalg.matrix_rank(A) == A.shape[1]

# Find dimension of span
np.linalg.matrix_rank(A)

# Check if basis for R^n
rank = np.linalg.matrix_rank(A)
is_basis = (rank == n and A.shape[1] == n)
```

---

## References

1. Delhi University NEP 2024 UGCF Syllabus - Mathematics for Computing
2. Gilbert Strang, "Introduction to Linear Algebra" - For theoretical depth
3. Kenneth Hoffman and Ray Kunze, "Linear Algebra" - Advanced references
4. NumPy Documentation - For computational approaches

---

*This study material is specifically designed for BSc (Hons) Computer Science students at Delhi University under NEP 2024 UGCF framework. The content balances theoretical understanding with computational applications relevant to computing professionals.*