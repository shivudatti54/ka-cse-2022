# Echelon Form, Rank, and Determinant

## A Comprehensive Study Material for Mathematics For Computing

---

## 1. Introduction

Linear algebra forms the backbone of modern computing, powering everything from search engine algorithms to machine learning models and computer graphics. This study material covers three interconnected fundamental concepts: **Echelon Form**, **Rank**, and **Determinant** of a matrix. These concepts are essential tools for any computer scientist, enabling efficient solutions to systems of linear equations, data transformation, and dimensional analysis.

### Real-World Relevance to Computer Science

| Application Area | How Echelon Form/Rank/Determinant are Used |
|------------------|-------------------------------------------|
| **Machine Learning** | Principal Component Analysis (PCA) uses rank to determine dimensionality reduction; determinants help in probability distributions |
| **Computer Graphics** | 3D transformations use matrices; determinant indicates whether transformations preserve orientation |
| **Search Engines** | PageRank algorithm uses linear algebraic methods |
| **Cryptography** | Matrix operations over finite fields; determinant for matrix invertibility |
| **Data Science** | Solving systems of linear equations in regression analysis |
| **Computer Vision** | Image transformations and camera calibration |

---

## 2. Echelon Form of a Matrix

### 2.1 Definition

A matrix is in **Row Echelon Form (REF)** if it satisfies:
1. All nonzero rows are above any rows of all zeros
2. Each leading entry (first nonzero element) of a row is strictly to the right of the leading entry of the row above it
3. All entries in a column below a leading entry are zero

### 2.2 Reduced Row Echelon Form (RREF)

A matrix is in **Reduced Row Echelon Form (RREF)** if it satisfies all REF conditions plus:
1. The leading entry in each nonzero row is 1 (called a **pivot**)
2. Each leading 1 is the only nonzero entry in its column

### 2.3 Key Terminology

- **Pivot**: The first nonzero entry in a nonzero row
- **Pivot Column**: Column containing a pivot
- **Pivot Row**: Row containing a pivot
- **Leading 1**: A pivot that equals 1

---

## 3. Determinant of a Matrix

### 3.1 Definition

The **determinant** is a scalar value derived from a square matrix that encodes properties of the linear transformation described by the matrix. For an n×n matrix A, the determinant is denoted as det(A) or |A|.

### 3.2 Determinant of 2×2 Matrix

For a 2×2 matrix:
```
A = | a  b |
    | c  d |
```
**det(A) = ad - bc**

### 3.3 Determinant of n×n Matrix (Cofactor Expansion)

For any n×n matrix, the determinant can be computed using **Laplace expansion** along any row or column:

```
det(A) = Σᵢ aᵢⱼCᵢⱼ
```

Where Cᵢⱼ is the **cofactor** given by:
```
Cᵢⱼ = (-1)^(i+j) × det(Mᵢⱼ)
```

Mᵢⱼ is the **minor** matrix obtained by deleting row i and column j.

### 3.4 Properties of Determinants

1. **det(AB) = det(A) × det(B)**
2. **det(Aᵀ) = det(A)**
3. **det(A⁻¹) = 1/det(A)** (when A is invertible)
4. **det(kA) = kⁿ × det(A)** for n×n matrix
5. If a row is all zeros, det(A) = 0
6. If two rows are identical, det(A) = 0
7. A matrix is **singular** (non-invertible) if and only if det(A) = 0

### 3.5 Elementary Row Operations and Determinants

| Operation | Effect on Determinant |
|-----------|----------------------|
| Rᵢ → kRᵢ (k ≠ 0) | Multiplies det by k |
| Rᵢ → Rᵢ + kRⱼ | No change |
| Rᵢ ↔ Rⱼ | Changes sign |

---

## 4. Rank of a Matrix

### 4.1 Definition

The **rank** of a matrix is the maximum number of linearly independent rows (or columns) in the matrix. It equals the number of nonzero rows in its row echelon form.

**Notation**: rank(A) or ρ(A)

### 4.2 Rank and Linear Independence

- A set of vectors is **linearly independent** if no vector can be expressed as a linear combination of the others
- The rank tells us the dimension of the vector space spanned by rows/columns
- For an m×n matrix: **rank(A) ≤ min(m, n)**

### 4.3 Determining Rank

The rank can be found by:
1. Converting to row echelon form
2. Counting nonzero rows
3. For square matrices: rank = n - (number of zero eigenvalues)

### 4.4 Full Rank

- **Full row rank**: rank(A) = number of rows (m)
- **Full column rank**: rank(A) = number of columns (n)
- **Full rank** (for square matrices): rank(A) = n

---

## 5. The Rank-Nullity Theorem

### 5.1 Definitions

- **Nullity(A)**: Dimension of the null space (kernel) of A
- **Null Space (N(A) or Ker(A))**: Set of all vectors x such that Ax = 0

### 5.2 Rank-Nullity Theorem

For an m×n matrix A:
```
rank(A) + nullity(A) = n
```

**Interpretation**: The dimension of the domain (n) equals the sum of the rank (dimension of the image) and nullity (dimension of the kernel).

### 5.3 Implications

- If rank(A) = n (full column rank), then nullity(A) = 0, meaning the only solution to Ax = 0 is x = 0 (columns are linearly independent)
- If rank(A) = m (full row rank), then the system Ax = b has at least one solution for every b

---

## 6. Gaussian Elimination and Gauss-Jordan Elimination

### 6.1 Gaussian Elimination (REF)

A systematic method to convert a matrix to row echelon form:

1. Start from leftmost nonzero column
2. Use row operations to create zeros below pivot
3. Move to next row and column
4. Repeat

### 6.2 Gauss-Jordan Elimination (RREF)

Extends Gaussian elimination to produce reduced row echelon form:

1. Follow Gaussian elimination
2. Create zeros above each pivot
3. Scale each pivot to 1

### 6.3 Solving Systems of Linear Equations

For a system Ax = b:
1. Form augmented matrix [A|b]
2. Apply Gauss-Jordan elimination
3. Read solution from RREF

---

## 7. Worked Examples

### Example 1: Finding Echelon Form and Rank

**Problem**: Find the row echelon form and rank of:
```
A = | 1  2 -1 |
    | 2  4  1 |
    | 1  2  3 |
```

**Solution**:

**Step 1**: Start with the augmented structure
```
| 1  2 -1 |
| 2  4  1 |
| 1  2  3 |
```

**Step 2**: R₂ → R₂ - 2R₁
```
| 1  2 -1 |
| 0  0  3 |
| 1  2  3 |
```

**Step 3**: R₃ → R₃ - R₁
```
| 1  2 -1 |
| 0  0  3 |
| 0  0  4 |
```

**Step 4**: Swap R₂ and R₃ (to get pivot in column 3)
```
| 1  2 -1 |
| 0  0  4 |
| 0  0  3 |
```

**Step 5**: R₃ → R₃ - (3/4)R₂
```
| 1  2 -1 |
| 0  0  4 |
| 0  0  0 |
```

**Row Echelon Form**: The matrix has 2 nonzero rows

**Rank(A) = 2**

### Example 2: Determinant Using Cofactor Expansion

**Problem**: Find det(A) where:
```
A = | 3  2  1 |
    | 2  5  3 |
    | 1  2  4 |
```

**Solution** (expanding along first row):

```
det(A) = 3 × det(|5 3| |2 4|) - 2 × det(|2 3| |1 4|) + 1 × det(|2 5| |1 2|)

       = 3 × (5×4 - 3×2) - 2 × (2×4 - 3×1) + 1 × (2×2 - 5×1)
       
       = 3 × (20 - 6) - 2 × (8 - 3) + 1 × (4 - 5)
       
       = 3 × 14 - 2 × 5 + 1 × (-1)
       
       = 42 - 10 - 1
       
       = 31
```

**det(A) = 31** (nonzero, so A is invertible)

### Example 3: Rank-Nullity Theorem Application

**Problem**: For matrix A (3×5) with rank 2, find nullity.

**Solution**:
```
rank(A) + nullity(A) = n (number of columns)
2 + nullity(A) = 5
nullity(A) = 3
```

This means the solution space to Ax = 0 has dimension 3.

---

## 8. Python Code Examples for Computing

### 8.1 Using NumPy

```python
import numpy as np

# Define a matrix
A = np.array([[1, 2, -1],
              [2, 4, 1],
              [1, 2, 3]])

# Find determinant
det_A = np.linalg.det(A)
print(f"Determinant: {det_A:.2f}")

# Find rank
rank_A = np.linalg.matrix_rank(A)
print(f"Rank: {rank_A}")

# Find RREF using sympy
from sympy import Matrix
A_sym = Matrix(A)
rref, pivots = A_sym.rref()
print(f"RREF:\n{rref}")
print(f"Pivot columns: {pivots}")
```

**Output:**
```
Determinant: 0.00
Rank: 2
RREF:
Matrix([[1, 2, 0], [0, 0, 1], [0, 0, 0]])
Pivot columns: (0, 2)
```

### 8.2 Solving Systems of Equations

```python
import numpy as np

# System: 2x + y = 5
#          x - y = 1

A = np.array([[2, 1],
              [1, -1]])
b = np.array([5, 1])

# Check determinant first
det_A = np.linalg.det(A)
print(f"Determinant: {det_A}")

if det_A != 0:
    # Solve using inverse
    x = np.linalg.inv(A) @ b
    print(f"Solution: x = {x[0]}, y = {x[1]}")
    
    # Or use numpy's solve
    x = np.linalg.solve(A, b)
    print(f"Solution (solve): x = {x[0]}, y = {x[1]}")
else:
    print("System has no unique solution (singular matrix)")
```

---

## 9. Applications to Computer Science

### 9.1 Machine Learning and Data Science

- **Linear Regression**: Solving normal equations (XᵀX)β = Xᵀy requires matrix rank analysis
- **PCA**: Rank determines the number of principal components
- **Singular Value Decomposition (SVD)**: Uses rank for dimensionality reduction

### 9.2 Computer Graphics

- **Transformations**: 3D rotations, scaling, and translations use 4×4 matrices
- **Determinant Sign**: Positive determinant = orientation preserved; negative = reflection

### 9.3 Network Analysis

- **PageRank**: Uses eigenvectors of the Google matrix
- **Social Network Analysis**: Adjacency matrix rank indicates connectivity

### 9.4 Cryptography

- **Hill Cipher**: Uses matrix inversion (requires nonzero determinant)
- **Error-Correcting Codes**: Rank is used in decoding algorithms

### 9.5 Database Systems

- **Relational Algebra**: Rank concepts apply to table dependencies
- **SQL Optimization**: Understanding data dependencies

---

## 10. Assessment Questions

### Multiple Choice Questions

1. **The determinant of a 3×3 identity matrix is:**
   - (a) 0
   - (b) 1
   - (c) 3
   - (d) -1

2. **If rank(A) = 3 for a 4×5 matrix, then nullity(A) =:**
   - (a) 1
   - (b) 2
   - (c) 3
   - (d) 5

3. **Which of the following is true for a singular matrix?**
   - (a) Determinant > 0
   - (b) Determinant = 0
   - (c) Inverse exists
   - (d) Rank > dimension

4. **In RREF, each pivot must be:**
   - (a) Any nonzero number
   - (b) 1
   - (c) The largest in its row
   - (d) Negative

5. **If A is a 3×3 matrix with det(A) = -2, then det(2A) =:**
   - (a) -4
   - (b) -16
   - (c) 4
   - (d) 16

### Short Answer Questions

1. **Define row echelon form and reduced row echelon form with two distinguishing features.**

2. **State and explain the Rank-Nullity Theorem for an m×n matrix.**

3. **Prove that if A is invertible, then det(A⁻¹) = 1/det(A).**

4. **Find the rank and nullity of matrix B = [[1,2,3],[2,4,6],[3,6,9]] and explain your answer.**

5. **Explain why a matrix with determinant zero cannot have an inverse.**

### Flashcard-Style Questions

| Term | Definition/Key Point |
|------|---------------------|
| **Pivot** | First nonzero entry in a nonzero row of a matrix in echelon form |
| **Singular Matrix** | A square matrix with determinant = 0; not invertible |
| **Full Rank** | When rank(A) = min(m, n) for an m×n matrix |
| **Null Space** | Set of all vectors x such that Ax = 0 |
| **Elementary Matrix** | Matrix obtained by a single elementary row operation on identity matrix |

---

## 11. Key Takeaways

✅ **Echelon Form**: A matrix in row echelon form has zeros below each pivot; RREF has pivots equal to 1 with zeros above and below.

✅ **Determinant**: A scalar value that is zero for singular matrices; computed via cofactor expansion for n×n matrices; key properties: det(AB) = det(A)det(B), det(A⁻¹) = 1/det(A).

✅ **Rank**: Maximum number of linearly independent rows/columns; equals number of nonzero rows in echelon form; determines solvability of linear systems.

✅ **Rank-Nullity Theorem**: rank(A) + nullity(A) = n for an m×n matrix; fundamental relationship between dimensions of image and kernel.

✅ **Applications in CS**: Machine learning (PCA, regression), computer graphics (transformations), cryptography (matrix-based ciphers), and network analysis.

✅ **Practical Computation**: Use Gaussian elimination for REF; Gauss-Jordan for RREF; Python/NumPy for computational verification.

---

## 12. References and Delhi University Syllabus Context

This content aligns with the **Mathematics For Computing** paper of the **BSc (Hons) Computer Science** program under **NEP 2024 UGCF** at Delhi University. The topics covered correspond to:

- Unit on Matrices and Linear Algebra
- Systems of Linear Equations
- Rank, Determinants, and Inverses
- Applications to computing problems

**Recommended Texts:**
1. "Linear Algebra and Its Applications" - David C. Lay
2. "Mathematics for Computer Science" - Eric Lehman, F. Thomson Leighton
3. "Higher Engineering Mathematics" - B.S. Grewal

---

*Study Material prepared for BSc (Hons) Computer Science, Delhi University*