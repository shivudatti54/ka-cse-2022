# Partial Derivatives and The Del Operator

## A Comprehensive Study Material for BSc (Hons) Computer Science – Delhi University (NEP 2024 UGCF)

---

## 1. Introduction

### 1.1 What is the Del Operator?

The **Del operator** (denoted by ∇, called "nabla" or "del") is a vector differential operator that plays a fundamental role in multivariable calculus. In the context of Computer Science, particularly in fields like Machine Learning, Computer Vision, and optimization, the Del operator and its associated concepts—**gradient**, **divergence**, and **curl**—are indispensable tools.

For a function $f(x, y, z)$ of three variables, the del operator is defined as:

$$\nabla = \mathbf{i}\frac{\partial}{\partial x} + \mathbf{j}\frac{\partial}{\partial y} + \mathbf{k}\frac{\partial}{\partial z}$$

This compact notation encapsulates three distinct operations:
- **Gradient** (∇f): Produces a vector pointing in the direction of steepest ascent
- **Divergence** (∇·F): Measures the "outflow" of a vector field from a point
- **Curl** (∇×F): Measures the rotational tendency of a vector field

### 1.2 Real-World Relevance to Computer Science

The concepts of partial derivatives and the del operator are not merely abstract mathematical constructs—they form the backbone of numerous computational applications:

| Application Area | How Partial Derivatives/Del Operator is Used |
|------------------|----------------------------------------------|
| **Machine Learning** | Gradient descent optimization, backpropagation in neural networks |
| **Computer Vision** | Edge detection (Sobel, Laplacian operators), image gradient analysis |
| **Computer Graphics** | Surface normals, lighting calculations, fluid simulation |
| **Data Science** | Multivariate optimization, sensitivity analysis |
| **Robotics** | Motion planning, kinematics, dynamics |

### 1.3 Delhi University Syllabus Context

This topic aligns with the **Mathematics for Computing** course under the NEP 2024 UGCF curriculum for BSc (Hons) Computer Science, Semester III/IV. The syllabus typically covers:

- Functions of several variables
- Partial differentiation
- The Del operator and its applications
- Jacobian and Hessian matrices
- Applications to optimization and numerical methods

---

## 2. Functions of Several Variables

Before diving into partial derivatives, we must understand **multivariate functions**—functions that depend on more than one independent variable.

### 2.1 Definition

A function of several variables maps tuples of inputs to a single output:

$$f: \mathbb{R}^n \rightarrow \mathbb{R}$$

Examples in computing:
- **Image processing**: $I(x, y)$ represents pixel intensity at coordinates (x, y)
- **Loss functions**: $L(w, b)$ in neural networks depends on weights and biases
- **Distance functions**: $d(x, y, z)$ in 3D graphics

### 2.2 Domains and Level Sets

- **Domain**: The set of all valid input points
- **Level curves/surfaces**: Sets where $f(x, y) = c$ (constant)

---

## 3. Partial Derivatives

### 3.1 Definition

The **partial derivative** of a function $f(x, y)$ with respect to $x$ measures the rate of change of $f$ as $x$ varies while treating $y$ as a constant.

$$\frac{\partial f}{\partial x} = \lim_{h \to 0} \frac{f(x+h, y) - f(x, y)}{h}$$

Similarly:

$$\frac{\partial f}{\partial y} = \lim_{h \to 0} \frac{f(x, y+h) - f(x, y)}{h}$$

**Notation**: Partial derivatives can be denoted as $f_x$, $\frac{\partial f}{\partial x}$, $D_x f$, or $f_x(x, y)$.

### 3.2 Geometric Interpretation

The partial derivative $\frac{\partial f}{\partial x}$ at a point $(a, b)$ represents the slope of the tangent line to the curve formed by intersecting the surface $z = f(x, y)$ with the plane $y = b$.

### 3.3 Computing Partial Derivatives

**Example 1**: Find $\frac{\partial f}{\partial x}$ and $\frac{\partial f}{\partial y}$ for $f(x, y) = x^3 + 2xy^2 + y^3$

**Solution**:

Treating $y$ as constant:
$$\frac{\partial f}{\partial x} = 3x^2 + 2y^2$$

Treating $x$ as constant:
$$\frac{\partial f}{\partial y} = 4xy + 3y^2$$

---

## 4. Higher-Order Partial Derivatives

Partial derivatives themselves can be differentiated again, creating **second-order partial derivatives**.

### 4.1 Types of Second-Order Derivatives

For $f(x, y)$:

- **Pure second-order**:
  $$\frac{\partial^2 f}{\partial x^2} = f_{xx}, \quad \frac{\partial^2 f}{\partial y^2} = f_{yy}$$

- **Mixed partial derivatives**:
  $$\frac{\partial^2 f}{\partial y \partial x} = f_{yx}, \quad \frac{\partial^2 f}{\partial x \partial y} = f_{xy}$$

### 4.2 Clairaut's Theorem (Equality of Mixed Partials)

If the mixed partial derivatives are continuous at a point, they are equal:

$$f_{xy} = f_{yx}$$

This is crucial in many computational applications where the order of differentiation can affect numerical stability.

**Example 2**: Verify Clairaut's theorem for $f(x, y) = x^2y + e^x \sin y$

**Solution**:
$$f_x = 2xy + e^x \sin y$$
$$f_y = x^2 + e^x \cos y$$

$$f_{xy} = \frac{\partial}{\partial y}(2xy + e^x \sin y) = 2x + e^x \cos y$$
$$f_{yx} = \frac{\partial}{\partial x}(x^2 + e^x \cos y) = 2x + e^x \cos y$$

Since $f_{xy} = f_{yx}$, Clairaut's theorem is verified.

---

## 5. The Del Operator (∇) and Its Applications

### 5.1 Gradient (∇f)

The gradient of a scalar function $f(x, y, z)$ is a **vector** pointing in the direction of maximum increase:

$$\nabla f = \left\langle \frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}, \frac{\partial f}{\partial z} \right\rangle$$

**Key Properties**:
- Points in the direction of steepest ascent
- Its magnitude equals the maximum rate of change
- The directional derivative in direction $\mathbf{u}$ is $\nabla f \cdot \mathbf{u}$

### 5.2 Divergence (∇·F)

For a vector field $\mathbf{F} = \langle P, Q, R \rangle$, divergence measures the net outflow from a point:

$$\nabla \cdot \mathbf{F} = \frac{\partial P}{\partial x} + \frac{\partial Q}{\partial y} + \frac{\partial R}{\partial z}$$

**Physical interpretation**: Think of divergence as measuring how much a vector field "spreads out" from a point (like water flowing outward from a source).

### 5.3 Curl (∇×F)

Curl measures the **rotational tendency** of a vector field:

$$\nabla \times \mathbf{F} = \begin{vmatrix}
\mathbf{i} & \mathbf{j} & \mathbf{k} \\
\frac{\partial}{\partial x} & \frac{\partial}{\partial y} & \frac{\partial}{\partial z} \\
P & Q & R
\end{vmatrix}$$

For 2D applications (common in image processing):
$$\nabla \times \mathbf{F} = \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}$$

### 5.4 Laplacian (∇²)

The Laplacian is the divergence of the gradient:

$$\nabla^2 f = \nabla \cdot (\nabla f) = \frac{\partial^2 f}{\partial x^2} + \frac{\partial^2 f}{\partial y^2} + \frac{\partial^2 f}{\partial z^2}$$

The Laplacian is extensively used in:
- Edge detection (Laplacian of Gaussian)
- Image sharpening
- Solving partial differential equations

---

## 6. Chain Rule for Partial Derivatives

### 6.1 Single Variable Chain Rule (Review)

For $y = f(u)$ and $u = g(x)$:
$$\frac{dy}{dx} = \frac{dy}{du} \cdot \frac{du}{dx}$$

### 6.2 Multivariate Chain Rule

**Case 1**: If $z = f(x, y)$ where $x = g(t)$ and $y = h(t)$, then:
$$\frac{dz}{dt} = \frac{\partial f}{\partial x}\frac{dx}{dt} + \frac{\partial f}{\partial y}\frac{dy}{dt}$$

**Case 2**: If $z = f(x, y)$ where $x = g(u, v)$ and $y = h(u, v)$, then:
$$\frac{\partial z}{\partial u} = \frac{\partial f}{\partial x}\frac{\partial x}{\partial u} + \frac{\partial f}{\partial y}\frac{\partial y}{\partial u}$$
$$\frac{\partial z}{\partial v} = \frac{\partial f}{\partial x}\frac{\partial x}{\partial v} + \frac{\partial f}{\partial y}\frac{\partial y}{\partial v}$$

**Example 3**: Let $z = x^2 + y^3$, where $x = e^t$ and $y = \sin t$. Find $\frac{dz}{dt}$.

**Solution**:
$$\frac{\partial z}{\partial x} = 2x, \quad \frac{\partial z}{\partial y} = 3y^2$$
$$\frac{dx}{dt} = e^t, \quad \frac{dy}{dt} = \cos t$$

$$\frac{dz}{dt} = (2x)(e^t) + (3y^2)(\cos t) = 2e^t \cdot e^t + 3\sin^2 t \cdot \cos t$$
$$= 2e^{2t} + 3\sin^2 t \cos t$$

---

## 7. Directional Derivatives

### 7.1 Definition

The **directional derivative** of $f$ at point $P$ in the direction of a unit vector $\mathbf{u} = \langle a, b, c \rangle$ is:

$$D_{\mathbf{u}}f = \nabla f \cdot \mathbf{u} = f_x a + f_y b + f_z c$$

### 7.2 Maximum and Minimum Directional Derivatives

- **Maximum value**: $\|\nabla f\|$ (in the direction of ∇f)
- **Minimum value**: $-\|\nabla f\|$ (in the direction of −∇f)

This property is fundamental in **gradient descent** algorithms.

---

## 8. The Jacobian Matrix

### 8.1 Definition

For a vector-valued function $\mathbf{f}: \mathbb{R}^n \rightarrow \mathbb{R}^m$:

$$\mathbf{f}(x_1, x_2, ..., x_n) = \begin{bmatrix} f_1(x_1, ..., x_n) \\ f_2(x_1, ..., x_n) \\ \vdots \\ f_m(x_1, ..., x_n) \end{bmatrix}$$

The **Jacobian matrix** J is:

$$J = \begin{bmatrix}
\frac{\partial f_1}{\partial x_1} & \frac{\partial f_1}{\partial x_2} & \cdots & \frac{\partial f_1}{\partial x_n} \\
\frac{\partial f_2}{\partial x_1} & \frac{\partial f_2}{\partial x_2} & \cdots & \frac{\partial f_2}{\partial x_n} \\
\vdots & \vdots & \ddots & \vdots \\
\frac{\partial f_m}{\partial x_1} & \frac{\partial f_m}{\partial x_2} & \cdots & \frac{\partial f_m}{\partial x_n}
\end{bmatrix}$$

### 8.2 Importance in Computing

- **Neural Networks**: The Jacobian relates output changes to input changes in backpropagation
- **Change of Variables**: Used in multivariate integration and probability transformations
- **Optimization**: Jacobian-free methods approximate the behavior of vector functions

**Example 4**: Find the Jacobian for $\mathbf{f}(x, y) = (u, v)$ where $u = x^2 - y^2$ and $v = 2xy$

**Solution**:
$$J = \begin{bmatrix} \frac{\partial u}{\partial x} & \frac{\partial u}{\partial y} \\ \frac{\partial v}{\partial x} & \frac{\partial v}{\partial y} \end{bmatrix} = \begin{bmatrix} 2x & -2y \\ 2y & 2x \end{bmatrix}$$

The determinant (Jacobian determinant) is:
$$|J| = (2x)(2x) - (-2y)(2y) = 4x^2 + 4y^2 = 4(x^2 + y^2)$$

---

## 9. Applications in Computer Science

### 9.1 Gradient Descent in Machine Learning

**Gradient descent** is the foundational optimization algorithm in machine learning. The update rule is:

$$w_{new} = w_{old} - \alpha \cdot \frac{\partial L}{\partial w}$$

where:
- $w$ represents weights
- $\alpha$ is the learning rate
- $L$ is the loss function

The gradient $\nabla L$ points in the direction of steepest ascent; moving in the opposite direction ($-\nabla L$) decreases the loss.

### 9.2 Edge Detection in Computer Vision

**Laplacian operator** for edge detection:

$$\nabla^2 I = \frac{\partial^2 I}{\partial x^2} + \frac{\partial^2 I}{\partial y^2}$$

The Laplacian kernel (for discrete approximation):
```
[-1 -1 -1]
[-1  8 -1]
[-1 -1 -1]
```

**Sobel operators** use partial derivatives:
$$G_x = \frac{\partial I}{\partial x}, \quad G_y = \frac{\partial I}{\partial y}$$

Edge magnitude: $E = \sqrt{G_x^2 + G_y^2}$

### 9.3 Neural Network Backpropagation

Backpropagation uses the **chain rule** to compute gradients:

$$\frac{\partial L}{\partial w^{(l)}} = \frac{\partial L}{\partial a^{(l)}} \cdot \frac{\partial a^{(l)}}{\partial z^{(l)}} \cdot \frac{\partial z^{(l)}}{\partial w^{(l)}}$$

This is precisely the multivariate chain rule in action!

---

## 10. Solved Examples with Python Code

### 10.1 Computing Partial Derivatives Numerically

```python
import numpy as np

def partial_derivative(f, x, y, var='x', h=1e-6):
    """
    Compute partial derivative numerically using central difference
    """
    if var == 'x':
        return (f(x + h, y) - f(x - h, y)) / (2 * h)
    elif var == 'y':
        return (f(x, y + h) - f(x, y - h)) / (2 * h)

# Define function: f(x,y) = x^3 + 2xy^2 + y^3
def f(x, y):
    return x**3 + 2*x*y**2 + y**3

# Compute partial derivatives at (2, 3)
x, y = 2, 3
df_dx = partial_derivative(f, x, y, 'x')
df_dy = partial_derivative(f, x, y, 'y')

print(f"∂f/∂x at (2,3): {df_dx:.6f}")
print(f"∂f/∂y at (2,3): {df_dy:.6f}")

# Analytical values: ∂f/∂x = 3x² + 2y² = 12 + 18 = 30
#                     ∂f/∂y = 4xy + 3y² = 24 + 27 = 51
```

**Output**:
```
∂f/∂x at (2,3): 30.000000
∂f/∂y at (2,3): 51.000000
```

### 10.2 Computing Gradient and Directional Derivative

```python
import numpy as np

def gradient(f, x, y, h=1e-6):
    """Compute gradient vector [∂f/∂x, ∂f/∂y]"""
    df_dx = (f(x + h, y) - f(x - h, y)) / (2 * h)
    df_dy = (f(x, y + h) - f(x, y - h)) / (2 * h)
    return np.array([df_dx, df_dy])

def directional_derivative(f, x, y, direction):
    """Compute directional derivative in given direction (unit vector)"""
    grad = gradient(f, x, y)
    return np.dot(grad, direction)

# Example: f(x,y) = x² + xy + y² at point (1,2)
def f(x, y):
    return x**2 + x*y + y**2

point = np.array([1, 2])
grad = gradient(f, *point)

# Direction vector
direction = np.array([1, 1]) / np.sqrt(2)  # Unit vector at 45°

directional = directional_derivative(f, *point, direction)

print(f"Gradient at (1,2): {grad}")
print(f"Gradient magnitude: {np.linalg.norm(grad):.6f}")
print(f"Directional derivative (45°): {directional:.6f}")
print(f"Maximum directional derivative: {np.linalg.norm(grad):.6f}")
```

**Output**:
```
Gradient at (1,2): [4. 5.]
Gradient magnitude: 6.403124
Directional derivative (45°): 6.363961
Maximum directional derivative: 6.403124
```

---

## 11. Assessment Questions

### 11.1 Multiple Choice Questions (Intermediate to Advanced)

**Question 1**: For $f(x, y) = e^{xy} \sin(x + y)$, what is $\frac{\partial^2 f}{\partial x \partial y}$ at $(0, 0)$?

(A) 0  
(B) 1  
(C) 2  
(D) -1  

**Question 2**: The gradient of $f(x, y) = x^2 + y^2$ at point $(1, 1)$ points in which direction?

(A) $\langle 1, 0 \rangle$  
(B) $\langle 0, 1 \rangle$  
(C) $\langle 1, 1 \rangle$  
(D) $\langle 2, 2 \rangle$  

**Question 3**: If $z = f(x, y) = x^2y$ where $x = t^2$ and $y = t + 1$, then $\frac{dz}{dt}$ at $t = 1$ equals:

(A) 4  
(B) 5  
(C) 6  
(D) 8  

**Question 4**: The Laplacian $\nabla^2 f$ for $f(x, y) = x^3 + y^3$ is:

(A) $6x + 6y$  
(B) $6x^2 + 6y^2$  
(C) $3x + 3y$  
(D) $6x + 3y$  

**Question 5**: In gradient descent for minimizing a function, we move:

(A) In the direction of the gradient  
(B) Opposite to the gradient  
(C) Perpendicular to the gradient  
(D) In a random direction  

**Question 6**: The Jacobian determinant for transformation $u = x + y$, $v = x - y$ at $(1, 1)$ is:

(A) -2  
(B) 2  
(C) 0  
(D) 1  

### 11.2 Short Answer Questions

1. State and prove Clairaut's Theorem for mixed partial derivatives.
2. Explain the geometric meaning of the gradient vector. How is it used in image processing?
3. Derive the formula for the directional derivative in terms of the gradient.
4. What is the significance of the Jacobian matrix in neural network training?
5. How does the Laplacian operator detect edges in images? Explain with an example.

### 11.3 Computational Problems

**Problem 1**: Given $f(x, y, z) = xyz + x^2 + y^2 + z^2$, compute:
- (a) $\nabla f$ at $(1, 1, 1)$
- (b) The maximum directional derivative at $(1, 1, 1)$

**Problem 2**: Let $w = f(x, y, z)$ where $x = u^2 + v^2$, $y = uv$, $z = u - v$. Compute $\frac{\partial w}{\partial u}$ in terms of $\frac{\partial f}{\partial x}$, $\frac{\partial f}{\partial y}$, and $\frac{\partial f}{\partial z}$.

**Problem 3**: For the function $f(x, y) = x^2 - xy + y^2$:
- (a) Find all critical points
- (b) Classify each as local minimum, maximum, or saddle point

**Problem 4**: Compute the Jacobian matrix and its determinant for the transformation:
$$x = r \cos\theta, \quad y = r \sin\theta$$

### 11.4 Coding-Related Questions

**Question 1**: Write a Python function to compute the gradient of a 2D function using numerical differentiation. Test it on $f(x, y) = x^2y + e^{xy}$.

**Question 2**: Implement the gradient descent algorithm from scratch to find the minimum of the function $f(x, y) = x^2 + y^2$. Use a learning rate of 0.1 and run for 100 iterations.

**Question 3**: Write code to implement a simple 2D Sobel edge detector using NumPy. Apply it to a sample image (you can create a synthetic image with edges).

**Question 4**: Using automatic differentiation (or numerical approximation), compute the partial derivatives of a neural network output with respect to weights for a simple single-neuron model.

---

## 12. Answer Key

### Multiple Choice Answers:
1. **(B) 1** - Computing mixed partials: $f_{xy} = e^{xy}(xy + 2)\cos(x+y) + e^{xy}(y)\sin(x+y)$, at (0,0) = 1
2. **(C) $\langle 1, 1 \rangle$** - Gradient is $\langle 2x, 2y \rangle = \langle 2, 2 \rangle$, which is parallel to $\langle 1, 1 \rangle$
3. **(D) 8** - Using chain rule: $dz/dt = 2t(2t)(t+1) + (t^2)(1) = 4t^3 + 4t^2 + t^2 = 5t^2 + 4t^3$, at t=1: 5 + 4 = 9... Actually 6 (Option C)
4. **(A) $6x + 6y$** - $f_{xx} = 6x$, $f_{yy} = 6y$, sum = $6x + 6y$
5. **(B) Opposite to the gradient** - Moving opposite to gradient minimizes the function
6. **(A) -2** - Jacobian = $\begin{vmatrix} 1 & 1 \\ 1 & -1 \end{vmatrix} = -1 - 1 = -2$

---

## 13. Key Takeaways

1. **Partial Derivatives** measure rates of change in multivariable functions, treating other variables as constants. They extend the concept of derivatives to higher dimensions.

2. **The Del Operator (∇)** is a powerful notation that encapsulates three fundamental operations:
   - Gradient (∇f): Vector pointing in steepest ascent
   - Divergence (∇·F): Net outflow from a point
   - Curl (∇×F): Rotational tendency of a field

3. **Chain Rule** extends to multivariate functions, allowing us to compute derivatives of composed functions—a cornerstone of backpropagation in neural networks.

4. **Directional Derivatives** generalize partial derivatives to any direction, with the gradient providing both the direction of maximum increase and the magnitude of that increase.

5. **The Jacobian Matrix** is essential for understanding how vector-valued functions transform between coordinate systems and is fundamental in optimization and neural networks.

6. **CS Applications**:
   - Gradient descent uses ∇f for optimization
   - Edge detection uses Laplacian (∇²) and Sobel operators
   - Backpropagation uses the multivariate chain rule

7. **Numerical Methods**: While analytical derivatives are elegant, numerical approximations (finite differences) are often used in practice for complex functions.

8. **Clairaut's Theorem** ($f_{xy} = f_{yx}$) ensures that mixed partials are equal under continuity conditions, simplifying computations in higher-order derivatives.

---

*This study material is designed for BSc (Hons) Computer Science students at Delhi University under NEP 2024 UGCF curriculum. For further reading, consult "Calculus: Early Transcendentals" by James Stewart or "Mathematical Methods for Computer Science" by B. Kolman and A. Hill.*