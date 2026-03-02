# Vector Operations and Properties

## Introduction

In linear algebra, a vector is a fundamental object that represents a quantity possessing both magnitude and direction. Unlike a scalar, which has only magnitude, a vector is an ordered list of numbers (components) that define a point in a multidimensional space. Understanding how to manipulate these vectors through various operations is crucial for solving systems of equations, performing geometric transformations, and building the foundation for more advanced topics like machine learning and computer graphics. This section explores the core operations and their essential properties.

## Main Concepts

### 1. Vector Addition and Subtraction

Vectors of the same dimension can be added or subtracted by performing the operation on their corresponding components. Geometrically, vector addition follows the **parallelogram rule**: the sum $\vec{u} + \vec{v}$ is the vector from the tail of $\vec{u}$ to the head of $\vec{v}$ when they are placed tail-to-head. Subtraction, $\vec{u} - \vec{v}$, is equivalent to adding $\vec{u}$ and the negative of $\vec{v}$.

**Mathematical Formula:**
If $\vec{u} = \begin{bmatrix} u_1 \\ u_2 \\ \vdots \\ u_n \end{bmatrix}$ and $\vec{v} = \begin{bmatrix} v_1 \\ v_2 \\ \vdots \\ v_n \end{bmatrix}$, then:
$$
\vec{u} + \vec{v} = \begin{bmatrix} u_1 + v_1 \\ u_2 + v_2 \\ \vdots \\ u_n + v_n \end{bmatrix}, \quad
\vec{u} - \vec{v} = \begin{bmatrix} u_1 - v_1 \\ u_2 - v_2 \\ \vdots \\ u_n - v_n \end{bmatrix}
$$

### 2. Scalar Multiplication

Scalar multiplication involves multiplying each component of a vector by a real number (a scalar), $c$. This operation scales the vector's length. If $c > 0$, the direction is preserved; if $c < 0$, the direction is reversed.

**Mathematical Formula:**
$$
c \cdot \vec{v} = c \cdot \begin{bmatrix} v_1 \\ v_2 \\ \vdots \\ v_n \end{bmatrix} = \begin{bmatrix} c v_1 \\ c v_2 \\ \vdots \\ c v_n \end{bmatrix}
$$

### 3. Dot Product (Inner Product)

The dot product is an operation that takes two equal-dimension vectors and returns a single scalar value. It measures the magnitude of one vector in the direction of another and is fundamental in determining the angle between vectors.

**Mathematical Formula:**
$$
\vec{u} \cdot \vec{v} = u_1v_1 + u_2v_2 + \dots + u_nv_n = \sum_{i=1}^{n} u_i v_i
$$
The dot product can also be expressed geometrically as:
$$
\vec{u} \cdot \vec{v} = \|\vec{u}\| \|\vec{v}\| \cos\theta
$$
where $\theta$ is the angle between the two vectors and $\|\vec{u}\|$ is the magnitude (or norm) of $\vec{u}$, defined as $\sqrt{u_1^2 + u_2^2 + \dots + u_n^2}$.

### 4. Key Properties

These operations obey important algebraic properties that make calculations systematic.

*   **Commutativity of Addition:** $\vec{u} + \vec{v} = \vec{v} + \vec{u}$
*   **Associativity of Addition:** $(\vec{u} + \vec{v}) + \vec{w} = \vec{u} + (\vec{v} + \vec{w})$
*   **Distributivity:** $c(\vec{u} + \vec{v}) = c\vec{u} + c\vec{v}$ and $(c + d)\vec{u} = c\vec{u} + d\vec{u}$
*   **Commutativity of Dot Product:** $\vec{u} \cdot \vec{v} = \vec{v} \cdot \vec{u}$
*   **Orthogonality:** Two vectors are orthogonal (perpendicular) if and only if their dot product is zero: $\vec{u} \cdot \vec{v} = 0$.

## Worked Examples

### Example 1: Basic Operations

Given vectors $\vec{a} = \begin{bmatrix} 2 \\ -1 \\ 5 \end{bmatrix}$ and $\vec{b} = \begin{bmatrix} -3 \\ 4 \\ 1 \end{bmatrix}$, compute $2\vec{a} + \vec{b}$.

**Solution:**
First, perform the scalar multiplication:
$$
2\vec{a} = 2 \cdot \begin{bmatrix} 2 \\ -1 \\ 5 \end{bmatrix} = \begin{bmatrix} 4 \\ -2 \\ 10 \end{bmatrix}
$$
Then, add the result to $\vec{b}$:
$$
2\vec{a} + \vec{b} = \begin{bmatrix} 4 \\ -2 \\ 10 \end{bmatrix} + \begin{bmatrix} -3 \\ 4 \\ 1 \end{bmatrix} = \begin{bmatrix} 4 + (-3) \\ -2 + 4 \\ 10 + 1 \end{bmatrix} = \begin{bmatrix} 1 \\ 2 \\ 11 \end{bmatrix}
$$

### Example 2: Finding the Angle Between Vectors

Find the angle between $\vec{u} = \begin{bmatrix} 1 \\ 2 \\ -1 \end{bmatrix}$ and $\vec{v} = \begin{bmatrix} 2 \\ 1 \\ 0 \end{bmatrix}$.

**Solution:**
1.  Compute the dot product:
    $\vec{u} \cdot \vec{v} = (1)(2) + (2)(1) + (-1)(0) = 2 + 2 + 0 = 4$
2.  Compute the magnitudes:
    $\|\vec{u}\| = \sqrt{1^2 + 2^2 + (-1)^2} = \sqrt{1 + 4 + 1} = \sqrt{6}$
    $\|\vec{v}\| = \sqrt{2^2 + 1^2 + 0^2} = \sqrt{4 + 1 + 0} = \sqrt{5}$
3.  Use the geometric form of the dot product:
    $\vec{u} \cdot \vec{v} = \|\vec{u}\| \|\vec{v}\| \cos\theta$
    $4 = \sqrt{6} \cdot \sqrt{5} \cdot \cos\theta$
    $4 = \sqrt{30} \cdot \cos\theta$
    $\cos\theta = \frac{4}{\sqrt{30}}$
4.  Therefore, the angle is $\theta = \arccos\left(\frac{4}{\sqrt{30}}\right) \approx \arccos(0.730) \approx 43.1^\circ$.

## Key Takeaways

*   Vectors are added/subtracted **component-wise** and scaled through **scalar multiplication**.
*   The **dot product** yields a scalar and provides crucial geometric information about the relationship between two vectors, including the angle between them.
*   A dot product of zero indicates that two vectors are **orthogonal** (perpendicular).
*   These operations follow predictable **algebraic properties** (commutative, associative, distributive), which are essential for simplifying vector expressions.