# 2D Geometric Transformations

## Introduction
2D Geometric Transformations are fundamental operations in computer graphics that manipulate the position, size, orientation, and shape of 2D objects. These transformations are essential for rendering scenes, animation, and image processing. According to the Delhi University NEP 2024 UGCF syllabus for DSE-CG (Computer Graphics), this unit carries significant weightage.

---

## Key Concepts

### 1. Basic 2D Transformations

- **Translation**: Shifts a point from (x, y) to (x', y') by adding displacement values
  - Formula: x' = x + tx, y' = y + ty
  - Represented as: [x' y' 1] = [x y 1] × T(tx, ty)

- **Rotation**: Rotates a point around the origin by angle θ
  - Formula: x' = x cosθ - y sinθ, y' = x sinθ + y cosθ
  - Counter-clockwise rotation is positive
  - Matrix: R(θ) = [[cosθ, -sinθ, 0], [sinθ, cosθ, 0], [0, 0, 1]]

- **Scaling**: Changes the size of an object
  - Formula: x' = x × sx, y' = y × sy
  - Uniform scaling: sx = sy; Differential scaling: sx ≠ sy
  - Matrix: S(sx, sy) = [[sx, 0, 0], [0, sy, 0], [0, 0, 1]]

### 2. Homogeneous Coordinates

- Adds a third coordinate (w = 1) to represent 2D points as 3-element vectors
- Enables matrix multiplication for all transformations
- Point representation: (x, y, 1) or (xw, yw, w)
- Essential for composite transformations

### 3. Composite Transformations

- **Sequence of transformations combined into a single matrix**
- **Transformation multiplication is non-commutative** (order matters)
- Common composites:
  - Rotation about any point (translate → rotate → translate back)
  - Scaling about any point
  - Reflection through arbitrary lines

### 4. Other Transformations

- **Reflection**: Mirror image across axis/line
  - X-axis: (x, -y), Y-axis: (-x, y), Origin: (-x, -y)
- **Shear**: Distorts shape by shifting parallel lines
  - X-shear: x' = x + shy, y' = y
  - Y-shear: x' = x, y' = shx × x + y

---

## Important Formulas Summary

| Transformation | Matrix Form |
|----------------|-------------|
| Translation | T(tx, ty) = [[1, 0, tx], [0, 1, ty], [0, 0, 1]] |
| Rotation | R(θ) = [[cosθ, -sinθ, 0], [sinθ, cosθ, 0], [0, 0, 1]] |
| Scaling | S(sx, sy) = [[sx, 0, 0], [0, sy, 0], [0, 0, 1]] |

---

## Conclusion
2D Geometric Transformations form the backbone of computer graphics. Mastery of matrix representations and composite transformations is crucial for exam success. Remember: transformation order significantly affects the final result—always apply transformations from right to left in matrix multiplication. Practice deriving transformation matrices for rotation about arbitrary points, as this is a frequently asked question in Delhi University examinations.