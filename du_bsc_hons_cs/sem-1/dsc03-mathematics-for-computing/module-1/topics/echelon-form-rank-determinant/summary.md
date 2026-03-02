# Echelon Form – Rank – Determinant  
*Mathematics for Computing (BSc Hons CS – DU, NEP 2024)*  

### Introduction
In linear algebra, the **echelon form** of a matrix provides a systematic way to determine two fundamental scalar quantities: the **rank** (dimension of the row/column space) and the **determinant** (a measure of volume scaling). Mastery of the relationships among these concepts is essential for solving systems of linear equations, analyzing transformations, and many computing applications such as graph theory, cryptography, and machine‑learning algorithms.

### Key Concepts  

- **Row Echelon Form (REF)**  
  - All non‑zero rows are above any zero rows.  
  - Leading entry (pivot) of each non‑zero row is to the right of the pivot in the row above.  
  - Achieved by elementary row operations (swap, scale, row‑addition).  

- **Reduced Row Echelon Form (RREF)**  
  - REF **plus** each pivot equals 1 and is the only non‑zero entry in its column.  
  - Uniquely defined for any matrix.  

- **Gaussian Elimination**  
  - Systematic method to transform a matrix to REF (or RREF) using forward elimination followed by back‑substitution.  

- **Rank of a Matrix**  
  - **Definition:** Number of non‑zero rows in its REF (or RREF).  
  - **Properties:**  
    - \( \text{rank}(A) \le \min\{m,n\}\) for an \(m\times n\) matrix.  
    - \( \text{rank}(A) = \text{rank}(A^T)\).  
    - For a square matrix \(A_{n\times n}\): full rank \( \Leftrightarrow\) \( \text{rank}(A)=n\).  

- **Determinant**  
  - **Definition:** Scalar \(\det(A)\) obtained by cofactor expansion (or by row‑reduction).  
  - **Effect of elementary row operations:**  
    - Swap two rows → multiplies determinant by \(-1\).  
    - Multiply a row by \(c\neq0\) → multiplies determinant by \(c\).  
    - Add a multiple of one row to another → determinant unchanged.  
  - **Key properties:**  
    - \(\det(AB)=\det(A)\det(B)\).  
    - \(\det(A)\neq0 \iff A\) is invertible \(\iff \text{rank}(A)=n\).  

- **Relationship between Rank and Determinant**  
  - **Square matrix:**  
    - \(\det(A)\neq0\) ⇔ full rank ⇔ matrix is invertible.  
    - \(\det(A)=0\) ⇔ rank < n ⇔ matrix is singular.  
  - **Rectangular matrix:**  
    - Determinant not defined, but rank determines solvability of linear systems (e.g., consistency when \(\text{rank}(A)=\text{rank}[A|b]\)).  

- **Rank–Nullity Theorem (optional, for completeness)**  
  - For \(A_{m\times n}\), \(\text{nullity}(A)=n-\text{rank}(A)\).  

### Quick Revision Checklist  
- Perform Gaussian elimination → obtain REF → count pivots → **rank**.  
- Use row operations to simplify determinant calculation (avoid cofactor expansion unless matrix is small).  
- Remember: **non‑zero determinant ⇔ full rank** for square matrices.  
- Keep track of scaling factors when row‑operations involve multiplication of a row.

### Conclusion
Understanding echelon forms, rank, and determinants equips you to analyse linear systems, assess matrix invertibility, and evaluate the behaviour of linear transformations—core skills for many computing tasks. Focus on mastering the elementary row operations and their impact on rank and determinant; these form the algorithmic backbone of most numerical methods taught in the Delhi University “Mathematics for Computing” syllabus.