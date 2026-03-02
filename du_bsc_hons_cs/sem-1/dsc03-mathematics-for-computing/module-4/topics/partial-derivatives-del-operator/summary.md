# Partial Derivatives & Del Operator – Quick Revision

## Introduction
- In **Mathematics for Computing (Delhi University, NEP 2024 UGCF)**, partial derivatives and the Del (∇) operator are essential tools for multivariable calculus, optimisation, and vector‑field analysis – core components of Unit‑2 of the syllabus.

## 1. Partial Derivatives
- **Definition**: For f(x₁,…,xₙ), the partial derivative ∂f/∂xᵢ treats all other variables as constants.  
- **Notation**: ∂f/∂x, fₓ, f_{x_i}.  
- **Higher‑order**: Second‑order partials, mixed partials (Clairaut’s theorem if continuous).  
- **Techniques**  
  - Power, product, quotient, chain rule for partials.  
  - **Total derivative**: df = ∑ (∂f/∂xᵢ)dxᵢ (Jacobians for change of variables).  
- **Directional derivative**: D_u f = ∇f·u, where u is a unit vector; the gradient ∇f gives the direction of steepest ascent.  
- **Hessian**: matrix H = [∂²f/∂xᵢ∂xⱼ] – captures curvature, used in convexity tests and Newton‑type optimisation.

## 2. The Del Operator (∇)
- **Symbol**: ∇ = (∂/∂x, ∂/∂y, ∂/∂z) in ℝ³ (or (∂/∂x, ∂/∂y) in ℝ²).  
- **Applied to scalar field** → **Gradient**: ∇f is a vector pointing uphill.  
- **Applied to vector field**:  
  - **Divergence** ∇·F: scalar measuring net source/sink.  
  - **Curl** ∇×F: vector describing rotation.  
- **Laplacian** ∇²f = ∂²f/∂x² + ∂²f/∂y² + ∂²f/∂z²: appears in Laplace/Poisson equations (image smoothing, heat flow).  
- **Vector identities** (required by syllabus): ∇×(∇f)=0, ∇·(∇×F)=0, ∇(af+bg)=a∇f+b∇g, product rules.

## 3. Key Properties (Delhi University Syllabus)
- **Linearity**: ∇(af+bg)=a∇f+b∇g.  
- **Product rule**: ∇·(FG)= (∇·F)G + F·∇G.  
- **Jacobian matrix**: J = [∂f_i/∂x_j]; its determinant is crucial for change‑of‑variables in multiple integrals.  
- **Second‑order & Hessian**: used for classification of critical points (max/min/saddle).

## 4. Computing Applications
- **Optimisation**: Gradient descent uses ∇f to move toward minima; back‑propagation in neural networks is a chain of partial derivatives.  
- **Computer Graphics / Vision**: gradient & Laplacian for edge detection (Sobel), shading, diffusion filters.  
- **Machine Learning**: Hessian informs second‑order optimisation (e.g., Newton‑CG); Jacobian appears in auto‑differentiation.  
- **Physics‑based simulation**: divergence & curl model fluid flow, electromagnetism, and heat diffusion.

## Conclusion
- Mastering partial derivatives, gradient, divergence, curl, and the Del operator enables you to analyse multivariable functions, design gradient‑based algorithms, and solve problems in graphics, AI, and data science—objectives aligned with the Delhi University B.Sc. (H) Computer Science syllabus (Unit‑2).