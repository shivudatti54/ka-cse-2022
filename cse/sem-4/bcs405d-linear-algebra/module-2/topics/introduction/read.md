# Introduction to Linear Transformations

## Introduction

Linear transformations form one of the most fundamental concepts in linear algebra, serving as the bridge between abstract vector spaces and the concrete world of matrices. A linear transformation is a mapping between two vector spaces that preserves the operations of vector addition and scalar multiplication. These transformations appear extensively in physics, engineering, computer graphics, data science, and numerous other disciplines where linear relationships need to be analyzed or geometric operations need to be performed.

The study of linear transformations generalizes the concept of functions that students encounter in calculus, but with two crucial differences: the domain and codomain are vector spaces rather than subsets of real numbers, and the transformation must satisfy two specific properties that ensure linearity. Understanding this concept requires a solid foundation in vector spaces, including familiarity with vector addition and scalar multiplication operations.

Historically, linear transformations emerged from the need to solve systems of linear equations and to study geometric transformations in Euclidean spaces. Today, they provide the theoretical framework for matrix operations, eigenvalues and eigenvectors, and numerous applications in applied mathematics. The elegance of linear transformations lies in their ability to represent complex operations through relatively simple algebraic conditions, making them computationally tractable and theoretically rich.

## Key Concepts

### Definition of Linear Transformation

Let V and W be two vector spaces over the same field F (typically the real numbers ℝ or complex numbers ℂ). A function T: V → W is called a linear transformation if for all vectors u, v ∈ V and all scalars c ∈ F, the following two properties hold:

1. **Additivity (Superposition Principle)**: T(u + v) = T(u) + T(v)
2. **Homogeneity (Scalar Multiplication)**: T(cu) = cT(u)

These two properties can be combined into a single condition: T(cu + dv) = cT(u) + dT(v) for all u, v ∈ V and all scalars c, d ∈ F. This combined property is often the most convenient for verification purposes.

The vector space V is called the **domain** of T, while W is the **codomain**. The set of all possible outputs, denoted as {T(v) : v ∈ V}, is called the **range** or **image** of T.

### The Zero Transformation

The simplest linear transformation is the zero transformation, denoted T: V → W where T(v) = 0 for all v ∈ V. This transformation maps every vector in the domain to the zero vector in the codomain. It trivially satisfies both linearity conditions: T(u + v) = 0 = 0 + 0 = T(u) + T(v) and T(cv) = 0 = c0 = cT(v).

### The Identity Transformation

The identity transformation, denoted I: V → V, maps every vector to itself: I(v) = v for all v ∈ V. This transformation satisfies linearity trivially, as I(u + v) = u + v = I(u) + I(v) and I(cv) = cv = cI(v).

### Characteristic Properties

Several important properties follow directly from the definition. Let T: V → W be a linear transformation:

1. **Preservation of the Zero Vector**: T(0_V) = 0_W, where 0_V and 0_W are the zero vectors in V and W respectively. This follows from homogeneity with c = 0.

2. **Preservation of Negatives**: T(-v) = -T(v) for all v ∈ V. This follows from homogeneity with c = -1.

3. **Preservation of Linear Combinations**: For any scalars c₁, c₂, ..., cₙ and vectors v₁, v₂, ..., vₙ, we have T(c₁v₁ + c₂v₂ + ... + cₙvₙ) = c₁T(v₁) + c₂T(v₂) + ... + cₙT(vₙ).

4. **Image of Span**: The image of a span of vectors equals the span of their images: T(span{v₁, v₂, ..., vₙ}) = span{T(v₁), T(v₂), ..., T(vₙ)}.

### Linear Transformations and Bases

A crucial theorem states that a linear transformation is completely determined by its action on a basis of the domain. If B = {v₁, v₂, ..., vₙ} is a basis for V, then for any vector v = a₁v₁ + a₂v₂ + ... + aₙvₙ, we have T(v) = a₁T(v₁) + a₂T(v₂) + ... + aₙT(vₙ). This means knowing the images of basis vectors uniquely determines the entire transformation.

## Examples

### Example 1: Scaling Transformation in ℝ²

Consider the transformation T: ℝ² → ℝ² defined by T(x, y) = (3x, 3y). This transformation scales every vector by a factor of 3. To verify linearity:

- Additivity: T((x₁, y₁) + (x₂, y₂)) = T(x₁ + x₂, y₁ + y₂) = (3(x₁ + x₂), 3(y₁ + y₂)) = (3x₁ + 3x₂, 3y₁ + 3y₂) = (3x₁, 3y₁) + (3x₂, 3y₂) = T(x₁, y₁) + T(x₂, y₂).

- Homogeneity: T(c(x, y)) = T(cx, cy) = (3cx, 3cy) = c(3x, 3y) = cT(x, y).

Thus, T is a linear transformation. Geometrically, this represents a uniform expansion away from the origin by a factor of 3.

### Example 2: Projection onto the x-axis

Define T: ℝ² → ℝ² by T(x, y) = (x, 0). This transformation projects any point onto the x-axis by discarding the y-coordinate. Verification:

- Additivity: T((x₁, y₁) + (x₂, y₂)) = T(x₁ + x₂, y₁ + y₂) = (x₁ + x₂, 0) = (x₁, 0) + (x₂, 0) = T(x₁, y₁) + T(x₂, y₂).

- Homogeneity: T(c(x, y)) = T(cx, cy) = (cx, 0) = c(x, 0) = cT(x, y).

This is a linear transformation. Note that T maps many different input vectors to the same output (for example, (1, 2) and (1, 5) both map to (1, 0)), making it a non-injective transformation.

### Example 3: Differentiation as a Linear Transformation

Consider the vector space Pₙ of polynomials of degree at most n, and define D: Pₙ → Pₙ by D(p(x)) = p'(x), the derivative of the polynomial. We verify linearity using properties of differentiation:

For polynomials p(x) and q(x) and scalar c:
- D(p + q) = (p + q)' = p' + q' = D(p) + D(q)
- D(cp) = (cp)' = cp' = cD(p)

Thus, differentiation is a linear transformation. In this case, the domain and codomain are infinite-dimensional spaces of polynomials.

### Example 4: A Non-Linear Transformation

It is instructive to see transformations that are NOT linear. Consider S: ℝ² → ℝ² defined by S(x, y) = (x + 1, y). This adds 1 to the x-coordinate. To check linearity:

Let u = (x₁, y₁), v = (x₂, y₂). Then S(u + v) = S(x₁ + x₂, y₁ + y₂) = (x₁ + x₂ + 1, y₁ + y₂). Meanwhile, S(u) + S(v) = (x₁ + 1, y₁) + (x₂ + 1, y₂) = (x₁ + x₂ + 2, y₁ + y₂). Since S(u + v) ≠ S(u) + S(v), the additivity property fails, and S is not linear. Geometrically, this transformation translates the plane by 1 unit in the x-direction—a rigid motion that does not preserve the origin and is therefore not linear.

## Exam Tips

1. **Memorize the Definition Precise**: The two properties—additivity and homogeneity—must be memorized exactly. Many exam errors occur from forgetting one of these conditions or stating them incorrectly.

2. **Verify Using Combined Form**: When checking if a transformation is linear, use T(cu + dv) = cT(u) + dT(v) as your primary verification method. This single check is equivalent to verifying both properties.

3. **Always Check T(0) = 0**: A quick necessary (but not sufficient) test for linearity is to verify that the transformation maps the zero vector to zero. If T(0) ≠ 0, the transformation cannot be linear.

4. **Understand Geometric Interpretations**: For transformations in ℝ², be able to visualize the effect: scaling, rotation, projection, reflection, and shear. Each has a characteristic geometric behavior.

5. **Connect to Matrices**: Remember that every linear transformation from ℝⁿ to ℝᵐ can be represented by an m×n matrix. This connection is fundamental and frequently tested.

6. **Use Basis Arguments**: When asked to find or characterize linear transformations, remember they are completely determined by their action on a basis of the domain.

7. **Distinguish Linear from Affine**: Transformations of the form T(x) = Ax + b (where b ≠ 0) are affine, not linear. Recognize this common mistake pattern.