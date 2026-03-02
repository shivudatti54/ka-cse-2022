# Hermite-Bezier Curves

## Introduction

Hermite and Bezier curves are fundamental parametric curve representations in computer graphics, widely used for smooth curve design, animation path planning, and font glyph definition. These curves form an essential part of the Computer Graphics syllabus (DSE-CG) for BSc (Hons) Computer Science at Delhi University (NEP 2024 UGCF).

---

## Hermite Curves

- **Definition**: A parametric cubic curve defined by **two endpoints** (P₀, P₁) and **two tangent vectors** (T₀, T₁) at those endpoints
- **Equation**: P(t) = (2t³ - 3t² + 1)P₀ + (t³ - 2t² + t)T₀ + (-2t³ + 3t²)P₁ + (t³ - t²)T₁, where t ∈ [0,1]
- **Basis Functions** (Blending Functions):
  - H₀(t) = 2t³ - 3t² + 1
  - H₁(t) = t³ - 2t² + t
  - H₂(t) = -2t³ + 3t²
  - H₃(t) = t³ - t²
- **Properties**: Interpolation (passes through control points), local control via tangent modification

---

## Bezier Curves

- **Definition**: A parametric curve defined by **n+1 control points** using Bernstein polynomials
- **Cubic Bezier (n=3)**: P(t) = (1-t)³P₀ + 3(1-t)²tP₁ + 3(1-t)t²P₂ + t³P₃
- **Bernstein Basis**: B₀ⁿ(t) = (1-t)ⁿ, B₁ⁿ(t) = n(1-t)ⁿ⁻¹t, ..., Bₙⁿ(t) = tⁿ
- **Properties**:
  - **Convex Hull Property**: Curve lies within the convex hull of control points
  - **Interpolation**: Only endpoints (P₀, Pₙ) are interpolated
  - **Global Control**: Moving any control point affects entire curve
  - **Affine Invariance**: Transforming control points transforms the curve equivalently

---

## Relationship: Hermite to Bezier Conversion

- **Bezier to Hermite**: Use endpoints and calculate tangents from control points
  - T₀ = 3(P₁ - P₀), T₁ = 3(P₃ - P₂)
- **Hermite to Bezier**: Compute intermediate control points from tangents
  - P₁ = P₀ + T₀/3, P₂ = P₁ - T₁/3
- Bezier curves are more intuitive and widely adopted in graphics APIs (PostScript, SVG, Canvas)

---

## Continuity Conditions

- **C⁰ (Positional)**: Curve segments meet at common point
- **C¹ (Tangential)**: Tangents are equal in magnitude and direction
- **C² (Curvature)**: Second derivatives match at junction points

---

## Applications

- Font design and TrueType outlines
- Vector graphics and CAD systems
- Path animation and motion planning
- Surface patch definitions (Bezier patches)

---

## Conclusion

Hermite and Bezier curves form the foundation of modern curve modeling in computer graphics. While Hermite offers direct control via tangents, Bezier's convex hull property and intuitive control points make it industry-standard. Understanding their mathematical foundations and interconversion is crucial for the DSE-CG paper, as these concepts frequently appear in university examinations under the parametric curves unit.