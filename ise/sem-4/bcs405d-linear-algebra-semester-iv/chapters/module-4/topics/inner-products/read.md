Of course. Here is a comprehensive educational note on Inner Products for  Engineering Students, Semester IV, Linear Algebra.

# **Module 4: Inner Product Spaces**

## **Topic: Inner Products**

### **Introduction**

Until now, we have studied vector spaces, subspaces, linear independence, basis, and dimension. These concepts helped us understand the structure of vector spaces. However, they lack a notion of "geometry"—concepts like length, distance, and angles between vectors. An **inner product** is a powerful mathematical tool that introduces this geometry into a vector space. It allows us to generalize the familiar dot product from $\mathbb{R}^n$ to more abstract vector spaces, such as spaces of functions, which are crucial in fields like signal processing, machine learning, and quantum mechanics.

---

### **Core Concepts**

#### **1. Definition of an Inner Product**

Let $V$ be a vector space over a field $\mathbb{F}$ (where $\mathbb{F}$ is typically the real numbers $\mathbb{R}$ or complex numbers $\mathbb{C}$). An **inner product** is a function that assigns to each pair of vectors $\mathbf{u}, \mathbf{v} \in V$ a scalar $\langle \mathbf{u}, \mathbf{v} \rangle \in \mathbb{F}$, satisfying the following axioms for all $\mathbf{u}, \mathbf{v}, \mathbf{w} \in V$ and all scalars $c \in \mathbb{F}$:

1.  **Conjugate Symmetry:** $\langle \mathbf{u}, \mathbf{v} \rangle = \overline{\langle \mathbf{v}, \mathbf{u} \rangle}$
    - (If $V$ is a real vector space, this simplifies to symmetry: $\langle \mathbf{u}, \mathbf{v} \rangle = \langle \mathbf{v}, \mathbf{u} \rangle$)

2.  **Linearity in the First Argument:**
    - $\langle c\mathbf{u}, \mathbf{v} \rangle = c\langle \mathbf{u}, \mathbf{v} \rangle$
    - $\langle \mathbf{u} + \mathbf{w}, \mathbf{v} \rangle = \langle \mathbf{u}, \mathbf{v} \rangle + \langle \mathbf{w}, \mathbf{v} \rangle$

3.  **Positive Definiteness:**
    - $\langle \mathbf{u}, \mathbf{u} \rangle \geq 0$
    - $\langle \mathbf{u}, \mathbf{u} \rangle = 0$ **if and only if** $\mathbf{u} = \mathbf{0}$

A vector space $V$ equipped with an inner product is called an **Inner Product Space**.

#### **2. The Standard Inner Product**

The most common example is the **dot product** in $\mathbb{R}^n$, which is a specific type of inner product.

For vectors $\mathbf{u} = (u_1, u_2, ..., u_n)$ and $\mathbf{v} = (v_1, v_2, ..., v_n)$ in $\mathbb{R}^n$, the standard inner product is defined as:
$$\langle \mathbf{u}, \mathbf{v} \rangle = \mathbf{u} \cdot \mathbf{v} = u_1v_1 + u_2v_2 + ... + u_nv_n$$

**Example:** Let $\mathbf{u} = (1, 2, -1)$ and $\mathbf{v} = (3, 0, 4)$ in $\mathbb{R}^3$.
$$\langle \mathbf{u}, \mathbf{v} \rangle = (1)(3) + (2)(0) + (-1)(4) = 3 + 0 - 4 = -1$$

#### **3. Inner Products on Other Spaces**

We can define inner products on various vector spaces. A key example is the space of continuous functions on the interval $[a, b]$, denoted by $C[a, b]$.

A common inner product for functions $f$ and $g$ in $C[a, b]$ is:
$$\langle f, g \rangle = \int_a^b f(t)g(t)  dt$$

This definition satisfies all the inner product axioms. It is fundamental in approximating functions using Fourier series and Legendre polynomials.

**Example:** In $C[0, 1]$, let $f(t) = t$ and $g(t) = t^2$. Their inner product is:
$$\langle f, g \rangle = \int_0^1 t \cdot t^2  dt = \int_0^1 t^3  dt = \left[ \frac{t^4}{4} \right]_0^1 = \frac{1}{4}$$

#### **4. Norm, Distance, and Angle**

Once an inner product is defined, we can derive geometric concepts:

- **Norm (Length) of a vector:** $||\mathbf{v}|| = \sqrt{\langle \mathbf{v}, \mathbf{v} \rangle}$
- **Distance between vectors:** $d(\mathbf{u}, \mathbf{v}) = ||\mathbf{u} - \mathbf{v}||$
- **Angle between vectors:** For real vector spaces, the angle $\theta$ between two non-zero vectors $\mathbf{u}$ and $\mathbf{v}$ is defined by:
  $$\cos \theta = \frac{\langle \mathbf{u}, \mathbf{v} \rangle}{||\mathbf{u}||  ||\mathbf{v}||}$$

This leads directly to the definition of orthogonality.

#### **5. Orthogonality**

Two vectors $\mathbf{u}$ and $\mathbf{v}$ in an inner product space are said to be **orthogonal** if their inner product is zero:
$$\langle \mathbf{u}, \mathbf{v} \rangle = 0$$

This generalizes the concept of perpendicular vectors.

**Example:** In $\mathbb{R}^2$ with the standard inner product, $\mathbf{u} = (1, 2)$ and $\mathbf{v} = (-4, 2)$ are orthogonal because:
$$\langle \mathbf{u}, \mathbf{v} \rangle = (1)(-4) + (2)(2) = -4 + 4 = 0$$

---

### **Key Points & Summary**

| Concept                          | Description                                                                                                            | Importance                                                                         |
| :------------------------------- | :--------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------- | ---------- | --- | ------------------------------------------------ | -------------------------------------------- |
| **Inner Product**                | A function $\langle \mathbf{u}, \mathbf{v} \rangle$ satisfying conjugate symmetry, linearity, and positive defineness. | Adds geometric structure (length, angle, distance) to abstract vector spaces.      |
| **Inner Product Space**          | A vector space $V$ equipped with an inner product.                                                                     | The setting for geometric analysis in linear algebra.                              |
| **Standard Inner Product**       | $\langle \mathbf{u}, \mathbf{v} \rangle = u_1v_1 + ... + u_nv_n$ in $\mathbb{R}^n$.                                    | The familiar dot product; a specific case of the general definition.               |
| **Norm**                         | $                                                                                                                      |                                                                                    | \mathbf{v} |     | = \sqrt{\langle \mathbf{v}, \mathbf{v} \rangle}$ | Defines the length or magnitude of a vector. |
| **Orthogonality**                | $\langle \mathbf{u}, \mathbf{v} \rangle = 0$                                                                           | Generalizes perpendicularity; essential for building orthogonal bases.             |
| **Function Space Inner Product** | $\langle f, g \rangle = \int_a^b f(t)g(t)  dt$                                                                         | Crucial for applications in engineering like signal processing and approximations. |

**In summary,** an inner product is the fundamental mechanism for introducing Euclidean geometry into vector spaces. It is the bridge between the algebraic structure of vector spaces and the geometric concepts of length, distance, angle, and orthogonality, forming the foundation for more advanced topics like orthonormal bases and the Gram-Schmidt process.
