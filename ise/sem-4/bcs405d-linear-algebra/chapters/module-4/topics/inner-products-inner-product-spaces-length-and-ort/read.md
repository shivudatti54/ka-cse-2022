# Inner Products, Inner Product Spaces, Length and Orthogonality

=====================================================

## Definition and Notation

---

An inner product on a vector space `V` over a field `F` is a function `∀u,v∈V` `〈u,v〉: V×V→F` that satisfies the following properties:

- Positive definiteness: `〈u,u〉 ≥ 0` for all `u ∈ V`, with equality if and only if `u = 0`.
- Linearity in the first argument: `〈au+bv,w〉 = a〈u,w〉 + b〈v,w〉` for all `a,b ∈ F` and `u,v,w ∈ V`.
- Conjugate symmetry: `〈u,v〉 = \overline{〈v,u〉}` for all `u,v ∈ V`.

The inner product is denoted by `〈⋅,⋅〉`.

## Length and Orthogonality

---

- The length or norm of a vector `u ∈ V` is defined as `||u|| = √〈u,u〉`.
- Two vectors `u,v ∈ V` are said to be orthogonal if `〈u,v〉 = 0`.
- An orthonormal basis of a vector space `V` is a basis consisting of vectors that are both orthogonal and have length 1.

## Orthogonal Sets and Bases

---

- An orthogonal set of vectors `u1,u2,...,un` is a set such that `〈ui,uj〉 = 0` for all `i ≠ j`.
- An orthogonal basis of a vector space `V` is an orthonormal basis.
- The Gram-Schmidt process is a method for constructing an orthogonal basis from a given basis.

## Projections

---

- The projection of a vector `u ∈ V` onto a vector `v ∈ V` is defined as `proj_v(u) = \frac{{〈u,v〉}}{{||v||^2}}v`.
- The projection of `V` onto a subspace `W` is a subspace of `V` consisting of all vectors that can be written as the sum of a vector in `W` and a vector orthogonal to `W`.

## QR-Factorization

---

- The QR-factorization of a matrix `A ∈ M_m(F)` is a factorization of the form `A = QR`, where `Q ∈ GL_m(F)` and `R ∈ M_m(F)`.
- The matrix `Q` is called an orthogonal matrix, and the matrix `R` is called an upper triangular matrix.

## Least Squares

---

- The least squares problem is to find the vector `x ∈ V` that minimizes the distance between `x` and a given vector `b ∈ V`, subject to the constraint `Ax = b`.
- The solution to the least squares problem is given by `x = (A^T A)^-1 A^T b`, where `A^T` is the transpose of `A`.

## Gram-Schmidt Process

---

The Gram-Schmidt process is a method for constructing an orthogonal basis from a given basis.

### Algorithm

1.  Let `v1` be the first vector in the basis.
2.  For `i = 2` to `n`, let `wi` be the `i`-th vector in the basis.
3.  Let `vi` be the `i`-th component of the orthogonal basis.
4.  `vi = wi - \frac{{〈wi,v1〉}}{{||v1||^2}}v1`
5.  Repeat steps 2-4 until all vectors have been processed.

### Example

Suppose we have the following basis: `{v1 = [1,0]^T`, `v2 = [0,1]^T`, `v3 = [1,1]^T`}

Using the Gram-Schmidt process, we obtain the following orthogonal basis: `{u1 = [1,0]^T`, `u2 = [-1/√2,1/√2]^T`, `u3 = [1/√2,-1/√2]^T`}

### Code

Here is an example implementation of the Gram-Schmidt process in Python:

```python
import numpy as np

def gram_schmidt(v1, v2, ..., vn):
    u1 = v1
    for vi in v2:
        wi = vi
        for uj in u1:
            wi = wi - np.dot(wi, uj) * uj
        uj = wi / np.linalg.norm(wi)
        u1 = np.append(u1, uj)
    return u1

# Example usage
v1 = np.array([1,0])
v2 = np.array([0,1])
v3 = np.array([1,1])

u1 = gram_schmidt(v1, v2, v3)
print(u1)
```

This code takes as input a set of vectors `v1,v2,...,vn` and returns an orthogonal basis `u1,u2,...,un`.
