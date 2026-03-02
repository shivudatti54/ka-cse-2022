# Inner Products

## Table of Contents

- [Inner Products](#inner-products)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Definition of Inner Product](#definition-of-inner-product)
  - [Inner Product Space](#inner-product-space)
  - [Norm Induced by Inner Product](#norm-induced-by-inner-product)
  - [Cauchy-Schwarz Inequality](#cauchy-schwarz-inequality)
  - [Angle Between Vectors](#angle-between-vectors)
  - [Orthogonality](#orthogonality)
  - [Gram-Schmidt Orthogonalization Process](#gram-schmidt-orthogonalization-process)
  - [Orthogonal Complements](#orthogonal-complements)
  - [Best Approximation Theorem](#best-approximation-theorem)
- [Examples](#examples)
  - [Example 1: Standard Inner Product on ℝ³](#example-1-standard-inner-product-on-)
  - [Example 2: Gram-Schmidt Orthogonalization](#example-2-gram-schmidt-orthogonalization)
  - [Example 3: Inner Product on Function Space](#example-3-inner-product-on-function-space)
- [Exam Tips](#exam-tips)

## Introduction

Inner products are fundamental constructs in linear algebra that generalize the concept of the dot product in Euclidean space. An inner product introduces geometric notions such as length, angle, and orthogonality into abstract vector spaces, making it a powerful tool for solving problems in physics, engineering, computer science, and mathematics. In the context of the university's Linear Algebra course (BCS405D), understanding inner products is essential for grasping advanced topics like orthogonal projections, least squares approximations, and spectral theory.

The concept of an inner product transforms a mere vector space into an inner product space, which retains all the algebraic properties of vector spaces while gaining rich geometric structure. This module builds upon the foundational concepts of vector spaces and linear transformations, introducing the machinery necessary for solving real-world problems involving distances and angles in higher-dimensional spaces. The study of inner products has profound applications in quantum mechanics (where states are vectors and measurements involve inner products), signal processing (Fourier series), machine learning (kernel methods), and numerical analysis.

## Key Concepts

### Definition of Inner Product

An inner product on a vector space V over a field F (typically ℝ or ℂ) is a binary operation that maps two vectors to a scalar, denoted as ⟨u, v⟩, satisfying the following axioms for all vectors u, v, w ∈ V and all scalars α ∈ F:

1. **Conjugate Symmetry (for complex spaces)**: ⟨u, v⟩ = ⟨v, u⟩_ (where _ denotes complex conjugation; for real spaces, this reduces to symmetry: ⟨u, v⟩ = ⟨v, u⟩)
2. ** linearity in the first argument**: ⟨αu + v, w⟩ = α⟨u, w⟩ + ⟨v, w⟩
3. **Positive-definiteness**: ⟨v, v⟩ ≥ 0, and ⟨v, v⟩ = 0 if and only if v = 0

For real vector spaces, these axioms simplify since conjugation has no effect. The most common example is the **Euclidean inner product** on ℝⁿ: ⟨(x₁, x₂, ..., xₙ), (y₁, y₂, ..., yₙ)⟩ = Σᵢ xᵢyᵢ.

### Inner Product Space

An inner product space is a vector space equipped with an inner product. The pair (V, ⟨·, ·⟩) defines this space, and when the field is ℝ, we call it a Euclidean space; when the field is ℂ, it's called a unitary space. The dimension can be finite or infinite, with function spaces providing important infinite-dimensional examples.

### Norm Induced by Inner Product

Every inner product induces a norm (length) on the vector space through the formula: ||v|| = √⟨v, v⟩. This satisfies all norm properties: positivity, absolute homogeneity, and the triangle inequality. The norm provides a notion of distance through d(u, v) = ||u - v||.

### Cauchy-Schwarz Inequality

For any vectors u, v in an inner product space, the Cauchy-Schwarz inequality states: |⟨u, v⟩| ≤ ||u|| ||v||. Equality holds if and only if u and v are linearly dependent (one is a scalar multiple of the other). This fundamental inequality has far-reaching consequences in analysis and probability theory.

### Angle Between Vectors

The Cauchy-Schwarz inequality ensures that -1 ≤ ⟨u, v⟩/(||u|| ||v||) ≤ 1, allowing us to define the angle θ between nonzero vectors u and v as: cos θ = ⟨u, v⟩/(||u|| ||v||), where 0 ≤ θ ≤ π.

### Orthogonality

Two vectors u and v are orthogonal (perpendicular) if ⟨u, v⟩ = 0. A set of vectors is orthogonal if every pair of distinct vectors is orthogonal. If additionally each vector has unit norm (||vᵢ|| = 1), the set is orthonormal. In an orthonormal set, ⟨vᵢ, vⱼ⟩ = δᵢⱼ (Kronecker delta).

### Gram-Schmidt Orthogonalization Process

The Gram-Schmidt process transforms any linearly independent set {x₁, x₂, ..., xₙ} into an orthogonal set {v₁, v₂, ..., vₙ} that spans the same subspace. The formulas are:

- v₁ = x₁
- v₂ = x₂ - projᵥ₁(x₂) = x₂ - ⟨x₂, v₁⟩/⟨v₁, v₁⟩v₁
- v₃ = x₃ - projᵥ₁(x₃) - projᵥ₂(x₃) = x₃ - ⟨x₃, v₁⟩/⟨v₁, v₁⟩v₁ - ⟨x₃, v₂⟩/⟨v₂, v₂⟩v₂

Normalizing each vᵢ gives an orthonormal basis.

### Orthogonal Complements

For a subspace W of an inner product space V, the orthogonal complement W⊥ consists of all vectors in V orthogonal to every vector in W: W⊥ = {v ∈ V : ⟨v, w⟩ = 0 for all w ∈ W}. Key properties include: V = W ⊕ W⊥ (direct sum) and (W⊥)⊥ = W.

### Best Approximation Theorem

Given a subspace W and vector v ∈ V, the orthogonal projection of v onto W (denoted projᵂ(v)) minimizes the distance between v and any vector in W. That is, ||v - projᵂ(v)|| ≤ ||v - w|| for all w ∈ W.

## Examples

### Example 1: Standard Inner Product on ℝ³

Let u = (1, 2, 3) and v = (4, 5, 6). Compute ⟨u, v⟩, ||u||, ||v||, and the angle between them.

**Solution:**
⟨u, v⟩ = 1×4 + 2×5 + 3×6 = 4 + 10 + 18 = 32

||u|| = √(1² + 2² + 3²) = √(1 + 4 + 9) = √14 ≈ 3.742

||v|| = √(4² + 5² + 6²) = √(16 + 25 + 36) = √77 ≈ 8.775

cos θ = 32/(√14 × √77) = 32/√1078 ≈ 32/32.83 ≈ 0.9747

θ = arccos(0.9747) ≈ 0.225 radians ≈ 12.9°

### Example 2: Gram-Schmidt Orthogonalization

Apply Gram-Schmidt to transform the linearly independent set {x₁, x₂} = {(1, 1, 0), (1, 0, 1)} into an orthogonal set in ℝ³.

**Solution:**

Step 1: v₁ = x₁ = (1, 1, 0)

Step 2: Compute projection of x₂ onto v₁:
projᵥ₁(x₂) = ⟨x₂, v₁⟩/⟨v₁, v₁⟩ × v₁
⟨x₂, v₁⟩ = 1×1 + 0×1 + 1×0 = 1
⟨v₁, v₁⟩ = 1² + 1² + 0² = 2
proj = (1/2) × (1, 1, 0) = (0.5, 0.5, 0)

Step 3: v₂ = x₂ - projᵥ₁(x₂) = (1, 0, 1) - (0.5, 0.5, 0) = (0.5, -0.5, 1)

Verification: ⟨v₁, v₂⟩ = 1×0.5 + 1×(-0.5) + 0×1 = 0.5 - 0.5 + 0 = 0 ✓

The orthogonal set is {(1, 1, 0), (0.5, -0.5, 1)}.

### Example 3: Inner Product on Function Space

Consider the vector space C[0,1] of continuous real-valued functions on [0,1]. Define an inner product as ⟨f, g⟩ = ∫₀¹ f(x)g(x)dx. Verify that this satisfies inner product axioms and compute ⟨x², sin(x)⟩.

**Solution:**

Axiom verification:

- Symmetry: ⟨f, g⟩ = ∫ fg = ∫ gf = ⟨g, f⟩ ✓
- Linearity: ⟨αf + g, h⟩ = ∫(αf + g)h = α∫fh + ∫gh = α⟨f, h⟩ + ⟨g, h⟩ ✓
- Positive-definiteness: ⟨f, f⟩ = ∫ f² ≥ 0, and ∫ f² = 0 implies f ≡ 0 ✓

Now compute ⟨x², sin(x)⟩:
⟨x², sin(x)⟩ = ∫₀¹ x² sin(x) dx

Using integration by parts twice:
= [-x² cos(x)]₀¹ + ∫₀¹ 2x cos(x) dx
= [-1² × cos(1)] + [2x sin(x)]₀¹ - ∫₀¹ 2 sin(x) dx
= -cos(1) + 2sin(1) + 2cos(x)|₀¹
= -cos(1) + 2sin(1) + 2(cos(1) - 1)
= cos(1) + 2sin(1) - 2 ≈ 0.5403 + 1.6829 - 2 ≈ 0.2232

## Exam Tips

1. **Remember all inner product axioms**: For real spaces, focus on symmetry, linearity, and positive-definiteness. For complex spaces, don't forget conjugate symmetry.

2. **Cauchy-Schwarz inequality applications**: This is frequently tested. Remember the inequality form |⟨u, v⟩| ≤ ||u|| ||v|| and know when equality holds.

3. **Gram-Schmidt process steps**: Practice the projection formula projᵥ(u) = ⟨u, v⟩/⟨v, v⟩ × v thoroughly; this appears in most examination questions.

4. **Orthogonal vs Orthonormal**: Orthogonal vectors have dot product zero; orthonormal vectors additionally have unit length.

5. **Computing angles**: Use cos θ = ⟨u, v⟩/(||u|| ||v||) only after verifying neither vector is zero.

6. **Best approximation theorem**: The orthogonal projection onto a subspace gives the closest point—remember this for least squares problems.

7. **Properties of orthogonal complements**: Always remember that V = W ⊕ W⊥ and (W⊥)⊥ = W for finite-dimensional spaces.
