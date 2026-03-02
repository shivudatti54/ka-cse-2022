# Laplacian Operator
**Mathematics For Computing — BSc (Hons) CS (DU NEP 2024)**

---

## Introduction

The Laplacian Operator (∇²) is a fundamental second-order differential operator in vector calculus with significant applications in computer science, particularly in image processing, computer graphics, and machine learning. It measures the rate at which a function changes at a point relative to the average of its surrounding values.

---

## Definition & Formula

- **Mathematical Definition:** The Laplacian is the divergence of the gradient: **∇² = ∇ · ∇**
- **In 2D Cartesian Coordinates:**
  $$\nabla^2 f = \frac{\partial^2 f}{\partial x^2} + \frac{\partial^2 f}{\partial y^2}$$
- **In 3D Cartesian Coordinates:**
  $$\nabla^2 f = \frac{\partial^2 f}{\partial x^2} + \frac{\partial^2 f}{\partial y^2} + \frac{\partial^2 f}{\partial z^2}$$

---

## Key Properties

- **Linear Operator:** ∇²(af + bg) = a∇²f + b∇²g
- **Isotropic:** Results are independent of coordinate system orientation
- **Second-order derivative:** Captures curvature of functions
- **Harmonic Functions:** If ∇²f = 0, f is called harmonic

---

## Applications in Computing

### Image Processing
- **Edge Detection:** Laplacian highlights rapid intensity changes
- **Image Sharpening:** Enhances details by adding Laplacian to original image
- **Blob Detection:** Identifies regions of uniform intensity

### Graph Theory & Machine Learning
- **Graph Laplacian:** Used in spectral clustering and graph neural networks
- **Diffusion processes:** Models information flow on networks

### Computer Graphics
- Surface smoothing and mesh processing
- Solving partial differential equations for simulations

---

## Practical Example (2D)

For f(x,y) = x² + y²:
- ∂f/∂x = 2x → ∂²f/∂x² = 2
- ∂f/∂y = 2y → ∂²f/∂y² = 2
- **∇²f = 4**

---

## Conclusion

The Laplacian Operator is essential for computing students, bridging mathematics and practical applications. Its role in image processing and emerging AI applications makes it a valuable tool for modern computer scientists, forming a key component of the Delhi University syllabus.

---

*For exam revision: Focus on formula, properties, and image processing applications.*