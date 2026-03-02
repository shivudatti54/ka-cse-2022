# 3D Geometric Transformations

## Introduction
3D Geometric Transformations are fundamental operations in computer graphics that manipulate objects in three-dimensional space. These transformations are essential for modeling, animation, rendering, and viewing 3D scenes. They form a core component of the Delhi University BSc (Hons) Computer Graphics syllabus under the NEP 2024 UGCF framework.

## Key Concepts

### 1. Basic 3D Transformations

- **Translation**: Moves a point from (x, y, z) to (x+dx, y+dy, z+dz) using translation vector T = [dx, dy, dz]
- **Rotation**: Rotates points around axes (X, Y, Z) by angle θ
  - Rotation about X-axis: clockwise/anticlockwise
  - Rotation about Y-axis: pitch
  - Rotation about Z-axis: roll
- **Scaling**: Changes object size using scale factors [Sx, Sy, Sz]
  - Uniform scaling: Sx = Sy = Sz
  - Non-uniform scaling: different values per axis

### 2. Homogeneous Coordinates

- Represent 3D points as 4D vectors [x, y, z, w]
- Enables matrix multiplication for composite transformations
- Standard form: (x/w, y/w, z/w) for w ≠ 0

### 3. Transformation Matrices (4×4)

- **Translation Matrix**: Uses identity matrix with translation values in last column
- **Rotation Matrices**: 
  - Rx(θ), Ry(θ), Rz(θ) — trigonometric matrices
- **Scaling Matrix**: Diagonal elements represent scale factors
- **Reflection**: Mirror image across planes (XY, YZ, XZ)
- **Shearing**: Skews shapes along axes

### 4. Composite Transformations

- Multiple transformations combined using matrix multiplication
- Order matters: T × R × S ≠ S × R × T
- Process: Apply transformations right to left
- Examples: Rotate-then-translate, scale-then-rotate

### 5. 3D Viewing Pipeline

- **Modeling Coordinates** → **World Coordinates** → **View Coordinates** → **Projection** → **Device Coordinates**
- **Viewing Transformations**: Define camera position and orientation
- **Projection Types**:
  - Orthographic: Parallel lines remain parallel
  - Perspective: Lines converge at vanishing point

### 6. Important Properties

- **Affine Transformations**: Preserve parallelism and ratios
- **Rigid Transformations**: Translation + Rotation (preserve shape/size)
- **Coordinate System**: Right-handed Cartesian system (standard in graphics)

## Conclusion
3D geometric transformations form the backbone of computer graphics rendering. Mastery of transformation matrices, homogeneous coordinates, and composite operations is essential for exam success and practical graphics programming. These concepts enable creation of complex 3D scenes, animations, and visual effects fundamental to modern computer graphics applications.