# **Inner Product Spaces Linear Algebra Revision Notes**

### Definitions and Formulas

- **Inner Product**: A function [u, v] that assigns a scalar value to each pair of vectors u and v in an inner product space.
- **Inner Product Space**: A vector space V equipped with an inner product.
- **Length (or Norm)**: The square root of the inner product of a vector with itself: ||u|| = √[u, u].
- **Orthogonality**: Two vectors u and v are orthogonal if their inner product is zero: [u, v] = 0.
- **Orthogonal Set**: A set of vectors {u1, u2, ..., un} such that any two distinct vectors are orthogonal.
- **Orthogonal Basis**: A basis consisting of an orthogonal set of vectors.
- **Projection**: A linear transformation P that projects a vector u onto a subspace W.

### Key Concepts

- **Gram-Schmidt Process**: An algorithm for constructing an orthogonal basis from a given set of linearly independent vectors.
- **QR-Factorization**: A factorization of a matrix A into a product A = QR, where Q is an orthogonal matrix and R is an upper triangular matrix.
- **Least Squares**: A method for finding the best approximate solution to a system of linear equations.

### Important Theorems

- **Parseval's Identity**: For any orthogonal basis {u1, u2, ..., un}, ||u||^2 = [u1, u2, ..., un] u1 + [u1, u2, ..., un] u2 + ... + [u1, u2, ..., un] un.
- **Orthogonality Theorem**: If ||u|| = 0, then u = 0.

### Important Formulas

- **Length Formula**: ||u|| = √[u, u] = √(u1^2 + u2^2 + ... + un^2)
- **Inner Product Formula**: [u, v] = u1v1 + u2v2 + ... + unvn
- **Gram-Schmidt Formula**: v1 = u1, v2 = u2 - [u2, v1]v1, ..., vn = u_n - [u_n, v1]v1 - ... - [u_n, vn-1]vn-1

### Quick Revision Tips

- Remember that an orthogonal basis is a basis consisting of an orthogonal set of vectors.
- The Gram-Schmidt process is used to construct an orthogonal basis from a given set of linearly independent vectors.
- QR-factorization is a factorization of a matrix A into a product A = QR, where Q is an orthogonal matrix and R is an upper triangular matrix.
- Least squares is a method for finding the best approximate solution to a system of linear equations.
