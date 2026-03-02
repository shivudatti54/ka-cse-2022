# Matrix Representation of Linear Transformations

## 1. Introduction and Core Concept

A linear transformation is a function $T: V \rightarrow W$ between two vector spaces that preserves the operations of vector addition and scalar multiplication. While we can describe these transformations abstractly, their true computational power is unlocked by representing them as matrices.

The **fundamental idea** is this: if we have a basis for the domain vector space $V$, any vector $\vec{v}$ in $V$ can be uniquely represented by its coordinates (a column vector) relative to that basis. The matrix representation of $T$ is a tool that takes the coordinate vector of $\vec{v}$ and returns the coordinate vector of $T(\vec{v})$ in the codomain space $W$, relative to a chosen basis for $W$.

This connection is profound because it allows us to replace abstract linear transformations with concrete matrix multiplication, enabling computation and analysis.

## 2. Constructing the Matrix Representation

### 2.1 The Standard Matrix

The most straightforward representation uses the **standard bases**. Let $T: \mathbb{R}^n \rightarrow \mathbb{R}^m$ be a linear transformation. Let $\mathcal{E} = \\{\vec{e}_1, \vec{e}_2, ..., \vec{e}_n\\}$ be the standard basis for $\mathbb{R}^n$ and $\mathcal{E}'$ be the standard basis for $\mathbb{R}^m$.

The **standard matrix** $[T]$ for $T$ is constructed as follows:
$$ [T] = \begin{bmatrix} | & | & & | \\ T(\vec{e}\_1) & T(\vec{e}\_2) & \cdots & T(\vec{e}\_n) \\ | & | & & | \end{bmatrix} $$
In other words, the $j$-th column of the matrix $[T]$ is the vector $T(\vec{e}_j)$, written as a column vector relative to the standard basis of $\mathbb{R}^m$.

**Example:**
Let $T: \mathbb{R}^2 \rightarrow \mathbb{R}^2$ be a linear transformation defined by $T\left(\begin{bmatrix} x \\ y \end{bmatrix}\right) = \begin{bmatrix} x + 3y \\ 2x + 5y \end{bmatrix}$.

1.  Apply $T$ to the standard basis vectors of $\mathbb{R}^2$:
    $T(\vec{e}_1) = T\left(\begin{bmatrix} 1 \\ 0 \end{bmatrix}\right) = \begin{bmatrix} 1 + 3(0) \\ 2(1) + 5(0) \end{bmatrix} = \begin{bmatrix} 1 \\ 2 \end{bmatrix}$
    $T(\vec{e}_2) = T\left(\begin{bmatrix} 0 \\ 1 \end{bmatrix}\right) = \begin{bmatrix} 0 + 3(1) \\ 2(0) + 5(1) \end{bmatrix} = \begin{bmatrix} 3 \\ 5 \end{bmatrix}$

2.  Form the standard matrix by placing these results as columns:
    $$ [T] = \begin{bmatrix} 1 & 3 \\ 2 & 5 \end{bmatrix} $$

We can now compute $T(\vec{v})$ for any vector $\vec{v} = \begin{bmatrix} a \\ b \end{bmatrix}$ by simple matrix multiplication:
$$ T(\vec{v}) = [T]\vec{v} = \begin{bmatrix} 1 & 3 \\ 2 & 5 \end{bmatrix} \begin{bmatrix} a \\ b \end{bmatrix} = \begin{bmatrix} a + 3b \\ 2a + 5b \end{bmatrix} $$

### 2.2 The Matrix Relative to Arbitrary Bases

The power of matrix representation extends far beyond the standard basis. Let:

- $T: V \rightarrow W$ be a linear transformation.
- $\mathcal{B} = \\{\vec{b}_1, \vec{b}_2, ..., \vec{b}_n\\}$ be a basis for the domain $V$.
- $\mathcal{C} = \\{\vec{c}_1, \vec{c}_2, ..., \vec{c}_m\\}$ be a basis for the codomain $W$.

The **matrix of $T$ relative to bases $\mathcal{B}$ and $\mathcal{C}$**, denoted $[T]_{\mathcal{C}}^{\mathcal{B}}$, is constructed as follows:

1.  Apply $T$ to each basis vector in $\mathcal{B}$: $T(\vec{b}_1), T(\vec{b}_2), ..., T(\vec{b}_n)$.
2.  Find the coordinate vector of each $T(\vec{b}_j)$ relative to the basis $\mathcal{C}$. This vector is denoted $[T(\vec{b}_j)]_{\mathcal{C}}$.
3.  Form the matrix by using these coordinate vectors as columns:
    $$ [T]_{\mathcal{C}}^{\mathcal{B}} = \begin{bmatrix} | & | & & | \\ [T(\vec{b}_1)]_{\mathcal{C}} & [T(\vec{b}_2)]_{\mathcal{C}} & \cdots & [T(\vec{b}_n)]_{\mathcal{C}} \\ | & | & & | \end{bmatrix} $$

This matrix acts on coordinate vectors:
$$ [T(\vec{v})]_{\mathcal{C}} = [T]_{\mathcal{C}}^{\mathcal{B}} [\vec{v}]\_{\mathcal{B}} $$
The coordinate vector of the output ($T(\vec{v})$ in $W$) is equal to the matrix multiplied by the coordinate vector of the input ($\vec{v}$ in $V$).

**Example:**
Let $T: \mathcal{P}_2 \rightarrow \mathcal{P}_1$ be defined by $T(p(x)) = p'(x)$ (the derivative transformation). Let $\mathcal{B} = \\{1, x, x^2\\}$ be a basis for $\mathcal{P}_2$ and $\mathcal{C} = \\{2, 2x\\}$ be a basis for $\mathcal{P}_1$.

1.  Apply $T$ to each vector in $\mathcal{B}$:
    $T(1) = 0$
    $T(x) = 1$
    $T(x^2) = 2x$

2.  Find the coordinate vector of each result relative to $\mathcal{C}$.
    - To write $0$ in terms of $\mathcal{C}=\\{2, 2x\\}$: $0 = 0(2) + 0(2x)$ $\rightarrow$ $[0]_{\mathcal{C}} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$
    - To write $1$ in terms of $\mathcal{C}$: $1 = \frac{1}{2}(2) + 0(2x)$ $\rightarrow$ $[1]_{\mathcal{C}} = \begin{bmatrix} 1/2 \\ 0 \end{bmatrix}$
    - To write $2x$ in terms of $\mathcal{C}$: $2x = 0(2) + 1(2x)$ $\rightarrow$ $[2x]_{\mathcal{C}} = \begin{bmatrix} 0 \\ 1 \end{bmatrix}$

3.  Form the matrix:
    $$ [T]_{\mathcal{C}}^{\mathcal{B}} = \begin{bmatrix} [T(1)]_{\mathcal{C}} & [T(x)]_{\mathcal{C}} & [T(x^2)]_{\mathcal{C}} \end{bmatrix} = \begin{bmatrix} 0 & 1/2 & 0 \\ 0 & 0 & 1 \end{bmatrix} $$

Now, to find the derivative of $p(x) = 3 + 5x - x^2$:

1.  Find its coordinate vector relative to $\mathcal{B}$: $[p(x)]_{\mathcal{B}} = \begin{bmatrix} 3 \\ 5 \\ -1 \end{bmatrix}$
2.  Multiply by the matrix:
    $$ [T(p(x))]_{\mathcal{C}} = [T]_{\mathcal{C}}^{\mathcal{B}} [p(x)]\_{\mathcal{B}} = \begin{bmatrix} 0 & 1/2 & 0 \\ 0 & 0 & 1 \end{bmatrix} \begin{bmatrix} 3 \\ 5 \\ -1 \end{bmatrix} = \begin{bmatrix} (0)(3) + (1/2)(5) + (0)(-1) \\ (0)(3) + (0)(5) + (1)(-1) \end{bmatrix} = \begin{bmatrix} 5/2 \\ -1 \end{bmatrix} $$
3.  Interpret the result: The coordinate vector $\begin{bmatrix} 5/2 \\ -1 \end{bmatrix}$ means $T(p(x)) = p'(x) = \frac{5}{2}(2) + (-1)(2x) = 5 - 2x$, which is indeed the derivative of $3 + 5x - x^2$.

## 3. Properties and Connections

### 3.1 Composition and Matrix Multiplication

One of the most elegant results in linear algebra is the connection between composition of transformations and matrix multiplication.

Let $T: U \rightarrow V$ and $S: V \rightarrow W$ be linear transformations. Let $\mathcal{B}, \mathcal{C}, \mathcal{D}$ be bases for $U, V, W$ respectively. The composition $(S \circ T): U \rightarrow W$ is also a linear transformation.

The matrix representation of the composition is the product of the individual matrix representations:
$$ [S \circ T]_{\mathcal{D}}^{\mathcal{B}} = [S]_{\mathcal{D}}^{\mathcal{C}} [T]\_{\mathcal{C}}^{\mathcal{B}} $$

The order of multiplication is crucial and matches the order of function composition (from right to left).

### 3.2 Invertibility and the Matrix Inverse

A linear transformation $T: V \rightarrow W$ is invertible if and only if it is both one-to-one (injective) and onto (surjective). If it is invertible, its inverse $T^{-1}: W \rightarrow V$ is also a linear transformation.

If $A = [T]_{\mathcal{C}}^{\mathcal{B}}$ is the matrix representation of an invertible linear transformation $T$, then the matrix representation of its inverse is the matrix inverse of $A$:
$$ [T^{-1}]_{\mathcal{B}}^{\mathcal{C}} = ([T]_{\mathcal{C}}^{\mathcal{B}})^{-1} = A^{-1} $$

This provides a deep connection between the abstract notion of an invertible function and the concrete algebraic property of a square matrix having an inverse.

## 4. Common Transformations and Their Matrices

The matrix representation makes it easy to identify and work with common geometric transformations.

| Transformation | Description                                         | Standard Matrix (in $\mathbb{R}^2$)                                                 | Diagram                                   |
| :------------- | :-------------------------------------------------- | :---------------------------------------------------------------------------------- | :---------------------------------------- |
| **Identity**   | Maps every vector to itself.                        | $\begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$                                      | `(x,y) -> (x,y)`                          |
| **Scaling**    | Stretches or shrinks vectors.                       | $\begin{bmatrix} s_x & 0 \\ 0 & s_y \end{bmatrix}$                                  | `(x,y) -> (s_x*x, s_y*y)`                 |
| **Rotation**   | Rotates vectors by angle $\theta$ counterclockwise. | $\begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}$ | `(x,y) -> (xcosθ - ysinθ, xsinθ + ycosθ)` |
| **Shear**      | Slants the shape.                                   | $\begin{bmatrix} 1 & k \\ 0 & 1 \end{bmatrix}$ (Horizontal)                         | `(x,y) -> (x + k*y, y)`                   |
| **Reflection** | Mirrors vectors across a line.                      | Across x-axis: $\begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}$                      | `(x,y) -> (x, -y)`                        |
| **Projection** | Drops vectors onto a line/plane.                    | Onto x-axis: $\begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}$                         | `(x,y) -> (x, 0)`                         |

**ASCII Diagram of Rotation:**

```
Initial Vector (1,0)
     |
     |   After 90° rotation
     |   becomes (0,1)
     |     /
     |    /
     |   /
-----+-------/-----> x-axis
    /|
   / |
  /  |
y-axis
```

## 5. Change of Basis and Similarity

A single linear transformation $T: V \rightarrow V$ (an operator) can have many different matrix representations, depending on the chosen basis. This leads to the concept of **similar matrices**.

Two $n \times n$ matrices $A$ and $B$ are **similar** if there exists an invertible matrix $P$ such that:
$$ B = P^{-1} A P $$

The matrix $P$ here is the **change-of-basis matrix**. If $A = [T]_{\mathcal{B}}$ is the matrix of $T$ relative to basis $\mathcal{B}$, and $B = [T]_{\mathcal{C}}$ is the matrix of $T$ relative to basis $\mathcal{C}$, then $B = P^{-1} A P$, where $P = [I]_{\mathcal{B}}^{\mathcal{C}}$ is the matrix that converts $\mathcal{C}$-coordinates into $\mathcal{B}$-coordinates.

Similar matrices represent the same linear transformation under different bases. They share many properties, such as determinant, trace, rank, and eigenvalues.

## 6. Exam Tips and Summary

**Key Takeaways:**

1.  The matrix of a linear transformation is built by applying $T$ to the basis vectors of the domain and using the results as columns.
2.  Matrix multiplication corresponds to composition of linear transformations.
3.  An invertible transformation corresponds to an invertible matrix.
4.  Similar matrices represent the same linear operator in different bases.

**Common Exam Mistakes to Avoid:**

- **Incorrect Order:** Remember that for composition, the matrix for the second transformation applied _($T$)_ is on the right, and the matrix for the first transformation applied _($S$)_ is on the left: $[S] [T]$.
- **Basis Confusion:** Always note the bases involved. The standard matrix is just a special case. Clearly label your matrices, e.g., $[T]_{\mathcal{C}}^{\mathcal{B}}$.
- **Coordinate Vectors:** Do not confuse the vector $\vec{v}$ itself with its coordinate vector $[\vec{v}]_{\mathcal{B}}$. The matrix acts on coordinate vectors, not necessarily on the vectors in their standard form.

**Problem-Solving Strategy:**

1.  **Identify:** What is the transformation? What are the domain and codomain? What bases are given or should be used (often standard bases if not specified)?
2.  **Construct:** Apply $T$ to each basis vector of the domain. Find the coordinate vector of each result relative to the codomain's basis. Use these coordinate vectors as columns to form the matrix.
3.  **Use:** To find $T(\vec{v})$, find $[\vec{v}]_{\mathcal{B}}$ and compute $[T]_{\mathcal{C}}^{\mathcal{B}} [\vec{v}]_{\mathcal{B}} = [T(\vec{v})]_{\mathcal{C}}$. Then, reconstruct the vector in $W$ from this coordinate vector.
4.  **Connect:** For composition, multiply the matrices. For invertibility, check if the matrix is invertible.
