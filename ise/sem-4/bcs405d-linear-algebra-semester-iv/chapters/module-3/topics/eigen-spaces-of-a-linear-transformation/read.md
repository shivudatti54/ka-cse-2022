Of course. Here is a comprehensive educational guide on "Eigenspaces of a Linear Transformation" designed for  engineering students.

---

### **Module 3: Eigenspaces of a Linear Transformation**

#### **1. Introduction**

In the previous topics, you learned about eigenvalues and eigenvectors. An eigenspace is a natural and powerful extension of these concepts. It's not just a single eigenvector but the entire _set_ of vectors associated with a particular eigenvalue. This concept is fundamental in applications like stability analysis, vibration modes, and diagonalizing matrices.

#### **2. Definition: What is an Eigenspace?**

Let `T: V → V` be a linear transformation on a vector space `V`, and let `λ` be an eigenvalue of `T`.

The **eigenspace** corresponding to the eigenvalue `λ`, denoted by `E_λ`, is defined as the set of all eigenvectors associated with `λ`, plus the zero vector.

**Mathematically, it is defined as:**
`E_λ = { v in V : T(v) = λv }`

This can also be written as the solution space (or null space) of the transformation `(T - λI)`, where `I` is the identity transformation:
`E_λ = { v in V : (T - λI)(v) = 0 } = Null(T - λI)`

> **Why include the zero vector?** The zero vector satisfies the equation `T(0) = λ0 = 0`, but by definition, an eigenvector cannot be zero. We include it to ensure the eigenspace is a valid _subspace_ of `V` (closed under addition and scalar multiplication).

#### **3. For a Square Matrix `A`**

If our linear transformation is defined by an `n x n` matrix `A`, the eigenspace `E_λ` for an eigenvalue `λ` is:
`E_λ = { x in R^n : (A - λI)x = 0 }`

This means the eigenspace `E_λ` is the **null space of the matrix `(A - λI)`**.

**How to find it?**

1.  For a given eigenvalue `λ`, form the matrix `(A - λI)`.
2.  Solve the homogeneous system of linear equations: `(A - λI)x = 0`.
3.  The solution set, expressed in parametric vector form, is the eigenspace `E_λ`. The basis for this null space is a basis for the eigenspace.

#### **4. Example**

Find the eigenspaces for the matrix `A = [[5, 4], [2, 3]]`.

**Step 1: Find the eigenvalues.**
The characteristic equation is `det(A - λI) = 0`.
`det([[5-λ, 4], [2, 3-λ]]) = (5-λ)(3-λ) - 8 = λ² - 8λ + 7 = 0`
Solving, we get `λ₁ = 7` and `λ₂ = 1`.

**Step 2: Find the eigenspace for `λ₁ = 7`.**
Form `(A - 7I) = [[5-7, 4], [2, 3-7]] = [[-2, 4], [2, -4]]`.
Now solve `(A - 7I)x = 0`:
`[[-2, 4], [2, -4]] * [[x1], [x2]] = [[0], [0]]`
This leads to the single equation: `-2x1 + 4x2 = 0` => `x1 = 2x2`.
Let `x2 = t` (a free parameter), then `x1 = 2t`.
The solution in parametric vector form is: `x = t * [[2], [1]]`.
Therefore, the eigenspace `E_7` is the set of all scalar multiples of the vector `[2, 1]^T`.
`E_7 = Span{ [[2], [1]] }`
A basis for `E_7` is `{ [[2], [1]] }`.

**Step 3: Find the eigenspace for `λ₂ = 1`.**
Form `(A - 1*I) = [[4, 4], [2, 2]]`.
Solve `(A - I)x = 0`:
`[[4, 4], [2, 2]] * [[x1], [x2]] = [[0], [0]]`
This leads to `4x1 + 4x2 = 0` => `x1 = -x2`.
Let `x2 = t`, then `x1 = -t`.
The solution is: `x = t * [[-1], [1]]`.
Therefore, the eigenspace `E_1` is:
`E_1 = Span{ [[-1], [1]] }`
A basis for `E_1` is `{ [[-1], [1]] }`.

#### **5. Geometric Interpretation & Dimension**

- Each eigenspace is a **line** through the origin in `R^2` (in the example above).
- The **geometric multiplicity** of an eigenvalue `λ` is defined as the _dimension_ of its eigenspace, `dim(E_λ)`.
  - In our example, `dim(E_7) = 1` and `dim(E_1) = 1`.
- The geometric multiplicity is always _less than or equal to_ the algebraic multiplicity (the multiplicity of `λ` as a root of the characteristic equation).

#### **6. Key Points & Summary**

- An **eigenspace** `E_λ` is the set of all eigenvectors for a given eigenvalue `λ`, plus the zero vector.
- It is a **subspace** of the original vector space `V`.
- For a matrix `A`, `E_λ = Null(A - λI)`.
- The **basis** of an eigenspace is found by solving `(A - λI)x = 0` and writing the solution in parametric form. The vectors that span the solution space form the basis.
- The **dimension** of the eigenspace is called the **geometric multiplicity** of `λ`.
- Understanding eigenspaces is crucial for determining if a matrix is **diagonalizable**. A matrix is diagonalizable if the sum of the dimensions of all its eigenspaces (geometric multiplicities) equals `n` (the size of the matrix).
