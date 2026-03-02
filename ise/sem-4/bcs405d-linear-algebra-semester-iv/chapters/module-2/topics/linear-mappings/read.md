Of course. Here is a comprehensive educational note on Linear Mappings for  Engineering Students, Semester IV, Linear Algebra.

### Module 2: Linear Transformations

#### Topic: Linear Mappings

---

### 1. Introduction

In engineering, we often need to convert data or models from one form to another. A **linear mapping** (or linear transformation) is a fundamental function that performs this conversion while preserving the essential structures of vector addition and scalar multiplication. Think of it as a function that takes a vector from one vector space and "maps" it to a vector in another (or the same) space in a predictable, straight-line fashion. They are the cornerstone for understanding concepts in computer graphics (rotations, scaling), signal processing (Fourier transform), and solving systems of differential equations.

---

### 2. Core Concepts

#### Definition of a Linear Mapping

Let $V$ and $W$ be real vector spaces. A function $T: V \rightarrow W$ is called a **linear mapping** (or linear transformation) if for all vectors $\mathbf{u}, \mathbf{v} \in V$ and all scalars $c \in \mathbb{R}$, the following two properties hold:

1.  **Additivity (Preservation of Addition):**
    $T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v})$

2.  **Homogeneity (Preservation of Scalar Multiplication):**
    $T(c\mathbf{u}) = cT(\mathbf{u})$

These two properties can be combined into a single condition:
$T(c_1\mathbf{u} + c_2\mathbf{v}) = c_1T(\mathbf{u}) + c_2T(\mathbf{v})$ for any scalars $c_1, c_2$.

#### The Matrix of a Linear Transformation

For mappings between the familiar coordinate spaces $\mathbb{R}^n$ and $\mathbb{R}^m$, every linear transformation can be represented by a matrix. This provides a concrete computational tool.

Let $T: \mathbb{R}^n \rightarrow \mathbb{R}^m$ be a linear transformation. Let $\{\mathbf{e}_1, \mathbf{e}_2, ..., \mathbf{e}_n\}$ be the standard basis for $\mathbb{R}^n$. The **standard matrix** $A$ of $T$ is an $m \times n$ matrix defined by:
$$A = \begin{bmatrix} T(\mathbf{e}_1) & T(\mathbf{e}_2) & \cdots & T(\mathbf{e}_n) \end{bmatrix}$$
In other words, the columns of $A$ are the images of the standard basis vectors under the transformation $T$.

Once you have the matrix $A$, evaluating $T(\mathbf{x})$ for any vector $\mathbf{x} \in \mathbb{R}^n$ becomes simple matrix multiplication:
$$T(\mathbf{x}) = A\mathbf{x}$$

#### Kernel and Image (Null Space and Column Space)

Two crucial subspaces are associated with every linear mapping $T: V \rightarrow W$:

- **Kernel (or Null Space):** The set of all vectors in $V$ that map to the zero vector in $W$.
  $$\text{Ker}(T) = \{\mathbf{v} \in V \ | \ T(\mathbf{v}) = \mathbf{0}\}$$
  - **Significance:** If $\text{Ker}(T) = \{\mathbf{0}\}$, the transformation is **one-to-one** (injective). Non-zero vectors in the kernel are "collapsed" to zero.

- **Image (or Range):** The set of all vectors in $W$ that are the image of some vector in $V$.
  $$\text{Im}(T) = \{T(\mathbf{v}) \in W \ | \ \mathbf{v} \in V\}$$
  - **Significance:** For $T: \mathbb{R}^n \rightarrow \mathbb{R}^m$ with standard matrix $A$, $\text{Im}(T)$ is precisely the **column space** of $A$.

---

### 3. Examples

**Example 1: A Transformation from $\mathbb{R}^2$ to $\mathbb{R}^2$**
Consider the transformation $T: \mathbb{R}^2 \rightarrow \mathbb{R}^2$ defined by $T(x, y) = (x + y, 2x)$.

- **Check Linearity:**
  Let $\mathbf{u} = (u_1, u_2)$, $\mathbf{v} = (v_1, v_2)$, and scalar $c$.
  1.  $T(\mathbf{u}+\mathbf{v}) = T(u_1+v_1, u_2+v_2) = ((u_1+v_1)+(u_2+v_2), 2(u_1+v_1)) = (u_1+u_2+v_1+v_2, 2u_1+2v_1)$
  2.  $T(\mathbf{u}) + T(\mathbf{v}) = (u_1+u_2, 2u_1) + (v_1+v_2, 2v_1) = (u_1+u_2+v_1+v_2, 2u_1+2v_1)$
      They are equal. A similar check works for scalar multiplication. Therefore, $T$ is linear.

- **Find its Standard Matrix:**
  Apply $T$ to the standard basis vectors of $\mathbb{R}^2$: $\mathbf{e}_1 = (1, 0)$ and $\mathbf{e}_2 = (0, 1)$.
  $T(\mathbf{e}_1) = T(1, 0) = (1+0, 2*1) = (1, 2)$
  $T(\mathbf{e}_2) = T(0, 1) = (0+1, 2*0) = (1, 0)$
  The standard matrix $A$ is formed by writing these images as columns:
  $$A = \begin{bmatrix} 1 & 1 \\ 2 & 0 \end{bmatrix}$$
  Now, to find $T(3, -1)$, we compute $A\mathbf{x}$:
  $$T(3, -1) = \begin{bmatrix} 1 & 1 \\ 2 & 0 \end{bmatrix} \begin{bmatrix} 3 \\ -1 \end{bmatrix} = \begin{bmatrix} (1)(3) + (1)(-1) \\ (2)(3) + (0)(-1) \end{bmatrix} = \begin{bmatrix} 2 \\ 6 \end{bmatrix}$$

**Example 2: The Zero and Identity Transformations**

- **Zero Transformation:** $T(\mathbf{v}) = \mathbf{0}$ for all $\mathbf{v} \in V$. Its kernel is all of $V$, and its image is $\{\mathbf{0}\}$.
- **Identity Transformation:** $T(\mathbf{v}) = \mathbf{v}$ for all $\mathbf{v} \in V$. Its kernel is $\{\mathbf{0}\}$, and its image is all of $V$.

---

### 4. Key Points & Summary

- **Definition:** A linear mapping $T: V \rightarrow W$ preserves vector addition and scalar multiplication.
- **Matrix Representation:** For $T: \mathbb{R}^n \rightarrow \mathbb{R}^m$, the standard matrix $A$ is built from the images of the standard basis vectors. The action of $T$ is then just matrix multiplication: $T(\mathbf{x}) = A\mathbf{x}$.
- **Kernel (Null Space):** The set of all vectors that map to $\mathbf{0}$. If only $\{\mathbf{0}\}$ is in the kernel, $T$ is **injective (one-to-one)**.
- **Image (Range):** The set of all possible outputs. For matrix $A$, this is its column space.
- **Applications:** Linear mappings are not abstract concepts. They are used everywhere in engineering:
  - **Robotics:** Transformations for arm movement and rotation.
  - **Computer Graphics:** Scaling, rotating, and translating images.
  - **Circuit Analysis:** Relating voltages and currents.
  - **Data Science:** Principal Component Analysis (PCA) for dimensionality reduction.
