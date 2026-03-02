# Hermite and Bezier Curves: Comprehensive Study Material

## Subject: DSC Cg - Computer Graphics | BSc (Hons) Computer Science - Delhi University (NEP 2024 UGCF)

---

## 1. Introduction

### 1.1 What Are Parametric Curves?

In computer graphics, representing smooth, curved shapes is fundamental to modeling complex objects, animations, and surfaces. **Parametric curves** provide a powerful mathematical framework where a curve is defined by functions of an independent parameter (typically denoted as *t* or *u*), where *t* ranges from 0 to 1.

Instead of defining a curve as y = f(x) (which cannot represent vertical lines or loops), parametric curves use:

- **x = x(t)**
- **y = y(t)**
- **z = z(t)** (for 3D curves)

This flexibility makes parametric curves essential for computer-aided design (CAD), font glyphs, animation paths, and 3D modeling.

### 1.2 Real-World Relevance

Hermite and Bezier curves are ubiquitous in modern computing:

| Application Area | Examples |
|-----------------|----------|
| **Font Design** | TrueType, PostScript fonts use Bezier curves |
| **CAD Software** | AutoCAD, SolidWorks use these curves for surface modeling |
| **Animation** | Smooth motion paths for characters and objects |
| **Game Development** | Terrain rendering, character models, camera paths |
| **Road Design** | Highway and railway curve design |
| **Robotics** | Trajectory planning for robot arms |

---

## 2. Hermite Curves

### 2.1 Definition

A **Hermite curve** is a parametric polynomial curve defined by its **endpoints** and their **tangent vectors** (derivatives at endpoints). It is the simplest spline curve that provides direct control over positions and slopes.

Given:
- Point P₀ (position at t = 0)
- Point P₁ (position at t = 1)
- Tangent vector R₀ (derivative at t = 0)
- Tangent vector R₁ (derivative at t = 1)

The Hermite curve is a cubic polynomial:

```
P(t) = a₃t³ + a₂t² + a₁t + a₀
```

### 2.2 Hermite Basis Functions (Blending Functions)

The cubic Hermite curve can be expressed using **basis functions** (also called blending functions):

```
P(t) = P₀·H₀(t) + P₁·H₁(t) + R₀·H₂(t) + R₁·H₃(t)
```

Where the Hermite basis functions are:

| Basis Function | Formula | Purpose |
|---------------|---------|---------|
| **H₀(t)** | 2t³ - 3t² + 1 | Blends toward P₀ |
| **H₁(t)** | -2t³ + 3t² | Blends toward P₁ |
| **H₂(t)** | t³ - 2t² + t | Blends toward R₀ |
| **H₃(t)** | t³ - t² | Blends toward R₁ |

**Properties of Hermite Basis Functions:**
- H₀(0) = 1, H₀(1) = 0 (endpoint interpolation)
- H₁(0) = 0, H₁(1) = 1 (endpoint interpolation)
- H₂(0) = 0, H₂(1) = 0 (endpoint tangents)
- H₃(0) = 0, H₃(1) = 0 (endpoint tangents)
- Derivatives at endpoints match the tangent vectors

### 2.3 Vector/Matrix Form

In matrix form, the Hermite curve is:

```
P(t) = [t³ t² t 1] × M_H × [P₀ P₁ R₀ R₁]ᵀ
```

Where M_H (Hermite matrix) is:

```
        |  2  -2   1   1 |
M_H  =  | -3   3  -2  -1 |
        |  0   0   1   0 |
        |  1   0   0   0 |
```

### 2.4 Example 1: Hermite Curve Computation

**Problem:** Given P₀ = (0, 0), P₁ = (4, 4), R₀ = (1, 0), R₁ = (1, 4), find the point at t = 0.5.

**Solution:**

First, compute the basis function values at t = 0.5:
- H₀(0.5) = 2(0.125) - 3(0.25) + 1 = 0.25 - 0.75 + 1 = 0.5
- H₁(0.5) = -2(0.125) + 3(0.25) = -0.25 + 0.75 = 0.5
- H₂(0.5) = 0.125 - 2(0.25) + 0.5 = 0.125 - 0.5 + 0.5 = 0.125
- H₃(0.5) = 0.125 - 0.25 = -0.125

Now compute P(0.5):
- x = 0×0.5 + 4×0.5 + 1×0.125 + 1×(-0.125) = 0 + 2 + 0.125 - 0.125 = **2**
- y = 0×0.5 + 4×0.5 + 0×0.125 + 4×(-0.125) = 0 + 2 + 0 - 0.5 = **1.5**

**Result:** P(0.5) = (2, 1.5)

---

## 3. Bezier Curves

### 3.1 Definition

A **Bezier curve** is a parametric curve defined by a set of **control points**. Unlike Hermite curves, Bezier curves provide intuitive geometric control—the curve doesn't necessarily pass through all control points (except endpoints), but is "pulled" toward them.

The standard Bezier curve uses **Bernstein polynomials** as its basis functions.

### 3.2 Bernstein Polynomials

For a Bezier curve of degree *n* with control points P₀, P₁, ..., Pₙ, the curve is:

```
P(t) = Σ Bᵢₙ(t) × Pᵢ    for i = 0 to n
```

Where Bᵢₙ(t) are the Bernstein polynomials:

```
Bᵢₙ(t) = C(n, i) × tⁱ × (1-t)^(n-i)
```

Where C(n, i) = n! / (i! × (n-i)!) is the binomial coefficient.

**Common Bezier Curves:**

| Degree | Bernstein Basis Functions |
|--------|---------------------------|
| **Linear (n=1)** | B₀₁ = 1-t, B₁₁ = t |
| **Quadratic (n=2)** | B₀₂ = (1-t)², B₁₂ = 2t(1-t), B₂₂ = t² |
| **Cubic (n=3)** | B₀₃ = (1-t)³, B₁₃ = 3t(1-t)², B₂₃ = 3t²(1-t), B₃₃ = t³ |

### 3.3 Cubic Bezier Curve

The most commonly used Bezier curve in computer graphics is the **cubic Bezier curve** (degree 3), defined by 4 control points P₀, P₁, P₂, P₃:

```
P(t) = (1-t)³P₀ + 3t(1-t)²P₁ + 3t²(1-t)P₂ + t³P₃
```

In matrix form:

```
        | -1   3  -3   1 |
M_B  =  |  3  -6   3   0 |
        | -3   3   0   0 |
        |  1   0   0   0 |
```

### 3.4 Properties of Bezier Curves

1. **Endpoint Interpolation:** The curve passes through P₀ (t=0) and P₃ (t=1)
2. **Convex Hull Property:** The curve lies entirely within the convex hull of control points
3. **Variation Diminishing:** The curve doesn't oscillate more than its control polygon
4. **Affine Invariance:** Transforming control points and evaluating curve produces same result as transforming curve
5. **Endpoint Tangents:** The tangent at t=0 is along P₀P₁, and at t=1 is along P₂P₃

---

## 4. De Casteljau's Algorithm

### 4.1 Introduction

**De Casteljau's algorithm** is a numerically stable method for evaluating Bezier curves. It uses **linear interpolation (lerp)** between control points recursively.

### 4.2 Algorithm Description

For a cubic Bezier curve with control points P₀, P₁, P₂, P₃:

**Step 1:** Compute first-level intermediate points:
```
Q₀ = lerp(P₀, P₁, t)
Q₁ = lerp(P₁, P₂, t)
Q₂ = lerp(P₂, P₃, t)
```

**Step 2:** Compute second-level intermediate points:
```
R₀ = lerp(Q₀, Q₁, t)
R₁ = lerp(Q₁, Q₂, t)
```

**Step 3:** Compute final point:
```
P(t) = lerp(R₀, R₁, t)
```

The lerp function is:
```
lerp(A, B, t) = (1-t)A + tB
```

### 4.3 Visual Representation

```
Original:     P₀─────P₁─────P₂─────P₃
                \     │     /
                 \    │    /
Level 1:       Q₀─────Q₁─────Q₂
                  \   │   /
                   \  │  /
Level 2:         R₀─────R₁
                    \
                     \
Final:             P(t)
```

### 4.4 Example 2: De Casteljau's Algorithm

**Problem:** Evaluate cubic Bezier curve at t = 0.5 with control points:
- P₀ = (0, 0)
- P₁ = (2, 4)
- P₂ = (6, 4)
- P₃ = (8, 0)

**Solution using De Casteljau's Algorithm:**

**Step 1 - First level:**
- Q₀ = lerp(P₀, P₁, 0.5) = ((0+2)/2, (0+4)/2) = (1, 2)
- Q₁ = lerp(P₁, P₂, 0.5) = ((2+6)/2, (4+4)/2) = (4, 4)
- Q₂ = lerp(P₂, P₃, 0.5) = ((6+8)/2, (4+0)/2) = (7, 2)

**Step 2 - Second level:**
- R₀ = lerp(Q₀, Q₁, 0.5) = ((1+4)/2, (2+4)/2) = (2.5, 3)
- R₁ = lerp(Q₁, Q₂, 0.5) = ((4+7)/2, (4+2)/2) = (5.5, 3)

**Step 3 - Final point:**
- P(0.5) = lerp(R₀, R₁, 0.5) = ((2.5+5.5)/2, (3+3)/2) = (4, 3)

**Result:** P(0.5) = (4, 3)

### 4.5 Implementation in Python

```python
import matplotlib.pyplot as plt

def lerp(p1, p2, t):
    """Linear interpolation between two points."""
    return ((1 - t) * p1[0] + t * p2[0], 
            (1 - t) * p1[1] + t * p2[1])

def de_casteljau(points, t):
    """
    Evaluate Bezier curve using De Casteljau's algorithm.
    points: list of control points as (x, y) tuples
    t: parameter value between 0 and 1
    """
    n = len(points)
    # Create working copy of points
    temp = [list(p) for p in points]
    
    # Recursive interpolation
    for i in range(1, n):
        for j in range(n - i):
            temp[j] = lerp(temp[j], temp[j + 1], t)
    
    return tuple(temp[0])

def plot_bezier_curve(points, num_points=100):
    """Plot Bezier curve with control points."""
    # Extract x, y coordinates
    px = [p[0] for p in points]
    py = [p[1] for p in points]
    
    # Generate curve points
    curve_x = []
    curve_y = []
    for i in range(num_points + 1):
        t = i / num_points
        point = de_casteljau(points, t)
        curve_x.append(point[0])
        curve_y.append(point[1])
    
    # Plot
    plt.figure(figsize=(10, 6))
    plt.plot(px, py, 'b--o', label='Control Polygon')
    plt.plot(curve_x, curve_y, 'r-', linewidth=2, label='Bezier Curve')
    plt.scatter(px, py, c='blue', s=100, zorder=5)
    plt.legend()
    plt.grid(True)
    plt.axis('equal')
    plt.title('Cubic Bezier Curve (De Casteljau Algorithm)')
    plt.show()

# Example usage
control_points = [(0, 0), (2, 4), (6, 4), (8, 0)]
plot_bezier_curve(control_points)
```

---

## 5. Connection Between Hermite and Bezier

### 5.1 Mathematical Relationship

Bezier curves can be viewed as a user-friendly variant of Hermite curves. The key difference lies in how tangents are specified:

| Aspect | Hermite | Bezier |
|--------|---------|--------|
| **Input** | Endpoints + Tangent vectors | Control points |
| **Tangent Control** | Explicit tangent values | Implicit via control points |
| **Ease of Use** | More mathematical | More intuitive |

### 5.2 Conversion: Bezier to Hermite

Given Bezier control points P₀, P₁, P₂, P₃, the equivalent Hermite parameters are:

- P₀ (Hermite) = P₀ (Bezier)
- P₁ (Hermite) = P₃ (Bezier)
- R₀ (Hermite) = 3(P₁ - P₀)  *(3 times the vector from P₀ to first control point)*
- R₁ (Hermite) = 3(P₃ - P₂)  *(3 times the vector from second-to-last control point to endpoint)*

The factor of 3 comes from the derivative of the cubic Bernstein polynomials at endpoints.

### 5.3 Why Bezier Is Preferred

1. **Intuitive Control:** Moving control points "pulls" the curve naturally
2. **Standard in Industry:** Adobe, TrueType, PostScript use Bezier
3. **Convex Hull Property:** Easier to predict curve behavior
4. **No Tangent Specification:** Users specify points, not slopes

---

## 6. C1 and G1 Geometric Continuity

### 6.1 Parametric Continuity (C¹)

Two curve segments join with **C¹ continuity** (parametric continuity) when:
- They meet at a common point: P₁(1) = P₂(0)
- Their tangent vectors are equal (direction and magnitude): P₁'(1) = P₂'(0)

### 6.2 Geometric Continuity (G¹)

Two curve segments join with **G¹ continuity** when:
- They meet at a common point: P₁(1) = P₂(0)
- Their tangent directions are parallel (magnitudes may differ): P₁'(1) = k × P₂'(0) for some k > 0

### 6.3 Practical Implications

- **C⁰ continuity:** Curves touch (no visible seam)
- **C¹/G¹ continuity:** Smooth join, no sharp corners
- **C² continuity:** Curvature continuous (used in high-quality surfaces)

For Bezier curves, ensuring G¹ continuity at a junction requires:
```
(P₁ - P₀) = k × (P₃ - P₂)  [for cubic segments]
```

---

## 7. Delhi University Syllabus Context

This topic aligns with the **DSC Cg - Computer Graphics** paper under the NEP 2024 UGCF curriculum for BSc (Hons) Computer Science. The key learning objectives include:

1. Understanding parametric curve representations
2. Implementing curve generation algorithms
3. Applying curves in graphics applications
4. Analyzing curve properties for design purposes

**Expected Skills:**
- Derive basis functions for Hermite curves
- Apply De Casteljau's algorithm for Bezier evaluation
- Convert between Hermite and Bezier representations
- Ensure geometric continuity in curve design

---

## 8. Key Takeaways

1. **Hermite Curves** are defined by endpoints and tangent vectors, using cubic polynomials with four basis functions that provide direct control over slope at endpoints.

2. **Bezier Curves** use control points to define curves intuitively, with Bernstein polynomials serving as basis functions. The curve is pulled toward control points but only passes through the endpoints.

3. **De Casteljau's Algorithm** provides a numerically stable method to evaluate Bezier curves through repeated linear interpolation, revealing the geometric construction of the curve.

4. **Cubic Bezier** (degree 3) is the most widely used form in computer graphics, balancing computational efficiency with sufficient flexibility for most design needs.

5. **Geometric Continuity (G¹)** ensures smooth curve joins where tangent directions align, even if magnitudes differ—essential for creating smooth, professional-looking curves.

6. **Industry Standard:** Bezier curves form the foundation of modern font design (TrueType, PostScript), CAD systems, and vector graphics software.

7. **Affine Invariance** means you can transform control points and evaluate the curve, or evaluate the curve and then transform it—both produce identical results, simplifying implementation.

---

## 9. Practice Questions

### Short Answer Questions
1. What is the difference between Hermite and Bezier curve representations?
2. List four properties of Bezier curves.
3. What is the purpose of Bernstein polynomials in Bezier curves?
4. Explain the Convex Hull Property of Bezier curves.
5. Define G¹ geometric continuity.

### Long Answer Questions
1. Derive the Hermite basis functions and explain their properties.
2. Describe De Casteljau's algorithm in detail. Evaluate a cubic Bezier curve at t = 0.25 using this algorithm.
3. Convert the Bezier control points P₀=(0,0), P₁=(3,6), P₂=(9,6), P₃=(12,0) to equivalent Hermite form.
4. Write a Python program to generate and plot a cubic Bezier curve using both the Bernstein polynomial formula and De Casteljau's algorithm.
5. Explain how you would ensure C¹ continuity when joining two cubic Bezier curve segments.

### Computational Questions
1. Given Hermite endpoints P₀=(1,2), P₁=(5,6) and tangent vectors R₀=(1,0), R₁=(2,4), find the point and tangent at t=0.5.
2. For control points (0,0), (2,8), (6,8), (8,0), compute the Bezier curve point at t=0.33 using De Casteljau's algorithm.

---

*Study Material prepared for DSC Cg - Computer Graphics, BSc (Hons) Computer Science, Delhi University (NEP 2024 UGCF)*