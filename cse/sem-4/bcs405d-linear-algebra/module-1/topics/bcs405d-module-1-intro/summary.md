# Introduction to Linear Algebra - Summary

## Key Definitions and Concepts

- **Matrix:** Rectangular array of elements with dimension m×n; represented as [aᵢⱼ] where i indicates row and j indicates column.
- **Vector:** Ordered n-tuple with magnitude and direction; can be represented as column or row matrix.
- **Linear Equation:** Equation of form a₁x₁ + a₂x₂ + ... + aₙxₙ = b where coefficients aᵢ are constants.
- **Determinant:** Scalar value det(A) computed from square matrix A that encodes properties of the linear transformation.
- **Rank:** Maximum number of linearly independent rows or columns in a matrix.
- **Vector Space:** Collection of vectors closed under addition and scalar multiplication satisfying eight axioms.

## Important Formulas and Theorems

- **2×2 Matrix Inverse:** A⁻¹ = (1/det(A)) × [[d,-b],[-c,a]] where A = [[a,b],[c,d]]
- **Determinant of 2×2:** det([[a,b],[c,d]]) = ad - bc
- **Dot Product:** a·b = Σaᵢbᵢ = ||a|| ||b|| cos(θ)
- **Vector Magnitude:** ||v|| = √(v₁² + v₂² + ... + vₙ²)
- **Matrix Multiplication:** (AB)ᵢⱼ = Σₖ aᵢₖbₖⱼ
- **Determinant Properties:** det(AB) = det(A)·det(B), det(A⁻¹) = 1/det(A), det(Aᵀ) = det(A)

## Key Points

- Matrix multiplication is associative (AB)C = A(BC) and distributive A(B+C) = AB + AC, but NOT commutative AB ≠ BA.
- Identity matrix Iₙ serves as multiplicative identity: AI = IA = A.
- System Ax = b has solution iff rank(A) = rank([A|b]); unique solution when rank = n.
- Gaussian elimination converts matrix to row echelon form; Gauss-Jordan reaches reduced row echelon form.
- A square matrix is invertible if and only if its determinant is non-zero.
- Elementary row operations preserve the rank and solution set of a linear system.
- Scalar multiplication of vectors scales magnitude; dot product results in scalar; cross product (3D) yields perpendicular vector.

## Common Mistakes to Avoid

- Confusing matrix addition with multiplication—addition is element-wise and requires identical dimensions.
- Forgetting that matrix multiplication requires column count of first matrix equals row count of second.
- Applying inverse method without verifying the matrix is invertible (determinant ≠ 0).
- Incorrectly computing determinants by expanding along wrong rows/columns without proper sign factors.
- Assuming AB = BA; always verify or compute both orders when required.

## Revision Tips

- Practice computing inverses of 2×2 matrices until automatic—this appears frequently in exam questions.
- Memorize the steps for Gaussian elimination: forward elimination then back substitution.
- Draw dimension diagrams when performing matrix operations to verify compatibility before computing.
- Solve at least 5 diverse problems on systems of linear equations covering unique, infinite, and no solution cases.
- Create a quick reference sheet for all determinant properties and review before examinations.
