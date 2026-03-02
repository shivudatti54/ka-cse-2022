# Vector Spaces and Subspaces

## 1. Introduction to Vector Spaces

A vector space is one of the most fundamental concepts in linear algebra. It provides a structured framework for studying vectors and their properties in a generalized way, moving beyond the intuitive 2D and 3D vectors to more abstract mathematical objects.

**Definition:** A **vector space** over a field **F** (typically the real numbers ℝ or complex numbers ℂ) is a non-empty set **V** equipped with two operations:

1. **Vector Addition:** For any **u, v ∈ V**, the sum **u + v ∈ V**
2. **Scalar Multiplication:** For any **a ∈ F** and **v ∈ V**, the product **a·v ∈ V**

These operations must satisfy ten specific axioms that ensure the algebraic structure behaves consistently.

## 2. The Ten Axioms of a Vector Space

For a set V to be a vector space over a field F, the following axioms must hold for all u, v, w ∈ V and all scalars a, b ∈ F:

### Additive Axioms:

1. **Closure under Addition:** u + v ∈ V
2. **Commutativity:** u + v = v + u
3. **Associativity:** (u + v) + w = u + (v + w)
4. **Additive Identity:** ∃ 0 ∈ V such that v + 0 = v
5. **Additive Inverse:** For each v ∈ V, ∃ -v ∈ V such that v + (-v) = 0

### Multiplicative Axioms:

6. **Closure under Scalar Multiplication:** a·v ∈ V
7. **Distributivity of Scalar over Vector Addition:** a·(u + v) = a·u + a·v
8. **Distributivity of Scalar Addition over Scalar Multiplication:** (a + b)·v = a·v + b·v
9. **Compatibility of Scalar Multiplication:** a·(b·v) = (ab)·v
10. **Multiplicative Identity:** 1·v = v (where 1 is the multiplicative identity in F)

## 3. Examples of Vector Spaces

### Example 1: ℝⁿ (n-dimensional Euclidean Space)

The most familiar vector space consists of all ordered n-tuples of real numbers:

- V = ℝⁿ = {(x₁, x₂, ..., xₙ) | xᵢ ∈ ℝ}
- Addition: (x₁, x₂, ..., xₙ) + (y₁, y₂, ..., yₙ) = (x₁+y₁, x₂+y₂, ..., xₙ+yₙ)
- Scalar multiplication: a·(x₁, x₂, ..., xₙ) = (ax₁, ax₂, ..., axₙ)

### Example 2: Matrix Spaces Mₘₓₙ

The set of all m×n matrices with real entries forms a vector space:

- Addition: Standard matrix addition
- Scalar multiplication: Multiply each entry by the scalar

```
Matrix Addition:      Scalar Multiplication:
[1 2]   [5 6]   [6 8]        3·[1 2]   [3 6]
[3 4] + [7 8] = [10 12]        [3 4] = [9 12]
```

### Example 3: Function Spaces

The set of all real-valued functions defined on an interval [a,b] forms a vector space:

- Addition: (f + g)(x) = f(x) + g(x)
- Scalar multiplication: (a·f)(x) = a·f(x)

### Example 4: Polynomial Spaces Pₙ

The set of all polynomials of degree ≤ n with real coefficients forms a vector space:

- p(x) = aₙxⁿ + aₙ₋₁xⁿ⁻¹ + ... + a₁x + a₀
- Addition: Add coefficients of like terms
- Scalar multiplication: Multiply each coefficient by the scalar

## 4. Subspaces

**Definition:** A **subspace** of a vector space V is a subset W ⊆ V that is itself a vector space under the same operations of addition and scalar multiplication as V.

**Subspace Test Theorem:** A subset W of a vector space V is a subspace if and only if:

1. W is non-empty (contains the zero vector)
2. W is closed under vector addition: If u, v ∈ W, then u + v ∈ W
3. W is closed under scalar multiplication: If u ∈ W and a ∈ F, then a·u ∈ W

### Examples of Subspaces:

**Example 1:** The zero subspace {0} is always a subspace of any vector space V.

**Example 2:** In ℝ³, the xy-plane is a subspace:
W = {(x, y, 0) | x, y ∈ ℝ}

**Example 3:** The set of all solutions to a homogeneous system of linear equations forms a subspace.

**Example 4:** In the space of all polynomials P, the set of all polynomials of degree ≤ 2 forms a subspace.

## 5. Important Subspace Concepts

### Null Space (Kernel)

For an m×n matrix A, the null space is defined as:
N(A) = {x ∈ ℝⁿ | Ax = 0}

This is always a subspace of ℝⁿ.

### Column Space (Range)

For an m×n matrix A, the column space is defined as:
C(A) = {Ax | x ∈ ℝⁿ}

This is always a subspace of ℝᵐ.

### Span

The span of a set of vectors {v₁, v₂, ..., vₖ} in a vector space V is the set of all linear combinations of these vectors:
span{v₁, v₂, ..., vₖ} = {a₁v₁ + a₂v₂ + ... + aₖvₖ | aᵢ ∈ F}

The span of any set of vectors is always a subspace of V.

## 6. Comparison of Vector Space Properties

| Property                           | Vector Space         | Subspace          |
| ---------------------------------- | -------------------- | ----------------- |
| Contains zero vector               | Always               | Always            |
| Closed under addition              | Always               | Must be verified  |
| Closed under scalar multiplication | Always               | Must be verified  |
| Inherits operations                | N/A (defines them)   | From parent space |
| Number of elements                 | Infinite (typically) | Could be finite   |

## 7. Visualizing Vector Spaces and Subspaces

While we can't visualize high-dimensional spaces directly, we can use lower-dimensional analogs:

```
3D Space (ℝ³) Visualization:

         z-axis
          |
          |   ˙ (1,2,3)
          |  /
          | /
          |/_____ y-axis
         /
        /
      x-axis

Subspaces in ℝ³:
- {0}: A single point at origin
- Lines through origin: 1D subspaces
- Planes through origin: 2D subspaces
- ℝ³ itself: 3D subspace
```

## 8. Special Types of Subspaces

### Proper Subspace

A subspace W of V is called a proper subspace if W ≠ V (W is strictly contained in V).

### Trivial Subspace

The zero subspace {0} is called the trivial subspace.

### Intersection of Subspaces

If W₁ and W₂ are subspaces of V, then their intersection W₁ ∩ W₂ is also a subspace of V.

### Sum of Subspaces

If W₁ and W₂ are subspaces of V, then their sum W₁ + W₂ = {w₁ + w₂ | w₁ ∈ W₁, w₂ ∈ W₂} is also a subspace of V.

## 9. Applications of Vector Spaces

Vector spaces form the foundation for:

- Solving systems of linear equations
- Understanding linear transformations
- Quantum mechanics (Hilbert spaces)
- Computer graphics (transformation of objects)
- Data analysis (vector space models)
- Signal processing (Fourier analysis)

## 10. Exam Tips

1. **When proving a set is a vector space:** Always verify all 10 axioms, though you can sometimes use known results (e.g., if it's a subset of a known vector space, you only need to check the 3 subspace conditions).

2. **When proving a subset is a subspace:** Use the subspace test - check that it contains the zero vector, and is closed under addition and scalar multiplication.

3. **Common mistakes to avoid:**
   - Forgetting to check that the set is non-empty (usually by verifying 0 is in the set)
   - Assuming closure properties without verification
   - Confusing the zero vector with the scalar 0

4. **For span questions:** Remember that the span of any set of vectors is always a subspace.

5. **For matrix-related subspaces:** For N(A), check that Ax = 0; for C(A), express vectors as linear combinations of columns.

6. **Visualization aid:** For ℝ² and ℝ³ problems, draw diagrams to understand relationships between subspaces.
