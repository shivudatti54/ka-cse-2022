# Linear Transformation
## Introduction

Linear transformation is a fundamental concept in mathematics and computer science, playing a crucial role in various fields such as computer graphics, machine learning, and data analysis. It is a way of transforming vectors from one vector space to another while preserving the operations of vector addition and scalar multiplication. In this topic, we will delve into the world of linear transformations, exploring their definitions, properties, and applications.

In essence, a linear transformation is a function between vector spaces that preserves the linear relationships between vectors. This means that the transformation maintains the operations of vector addition and scalar multiplication, allowing us to perform various tasks such as rotating, scaling, and projecting vectors. Linear transformations are used extensively in computer graphics to perform tasks such as rotating objects, projecting 3D objects onto 2D screens, and creating animations.

## Key Concepts

### Definition of Linear Transformation

A linear transformation T from a vector space V to a vector space W is a function T: V → W that satisfies the following two properties:

1. **Linearity**: T(u + v) = T(u) + T(v) for all u, v in V.
2. **Homogeneity**: T(cu) = cT(u) for all u in V and all scalars c.

### Types of Linear Transformations

There are several types of linear transformations, including:

1. **Isomorphism**: A bijective linear transformation between two vector spaces.
2. **Endomorphism**: A linear transformation from a vector space to itself.
3. **Automorphism**: A bijective linear transformation from a vector space to itself.

### Matrix Representation of Linear Transformations

Every linear transformation T: V → W can be represented by a matrix A, where A is an m x n matrix and m and n are the dimensions of W and V, respectively. The matrix A is called the **matrix representation** of T.

## Examples

### Example 1: Rotation Transformation

Suppose we want to rotate a vector v = (x, y) in a 2D plane by an angle θ. We can define a linear transformation T: ℝ² → ℝ² as follows:

T(x, y) = (x cos θ - y sin θ, x sin θ + y cos θ)

This transformation can be represented by the following matrix:

```
| cos θ  -sin θ |
| sin θ   cos θ |
```

### Example 2: Scaling Transformation

Suppose we want to scale a vector v = (x, y) in a 2D plane by a factor of k. We can define a linear transformation T: ℝ² → ℝ² as follows:

T(x, y) = (kx, ky)

This transformation can be represented by the following matrix:

```
| k  0 |
| 0  k |
```

### Example 3: Projection Transformation

Suppose we want to project a vector v = (x, y) in a 2D plane onto the x-axis. We can define a linear transformation T: ℝ² → ℝ² as follows:

T(x, y) = (x, 0)

This transformation can be represented by the following matrix:

```
| 1  0 |
| 0  0 |
```

## Exam Tips

1. Understand the definition of linear transformation and its properties.
2. Be able to identify the types of linear transformations (isomorphism, endomorphism, automorphism).
3. Know how to represent linear transformations using matrices.
4. Be able to perform linear transformations using matrix multiplication.
5. Understand the applications of linear transformations in computer graphics and other fields.
6. Practice solving problems involving linear transformations, such as finding the matrix representation of a transformation or applying a transformation to a vector.
7. Review the key concepts and formulas regularly to reinforce your understanding.