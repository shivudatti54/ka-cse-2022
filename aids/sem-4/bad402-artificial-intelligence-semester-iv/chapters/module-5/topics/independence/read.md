# Linear Independence and Span

## Introduction to Key Concepts

In linear algebra, the concepts of **linear independence** and **span** are fundamental to understanding the structure of vector spaces. They help us describe how vectors relate to each other and how they can be combined to form larger sets or entire spaces.

## Linear Combinations

Before we can understand span and linear independence, we must first understand linear combinations.

**Definition:** A vector **v** is a **linear combination** of vectors **v₁, v₂, ..., vₖ** if there exist scalars c₁, c₂, ..., cₖ such that:

**v = c₁v₁ + c₂v₂ + ... + cₖvₖ**

**Example 1:** In ℝ², consider vectors **v₁ = (1, 0)** and **v₂ = (0, 1)**. The vector **v = (3, 4)** can be written as:
**v = 3*(1, 0) + 4*(0, 1) = (3, 4)**
So, **v** is a linear combination of **v₁** and **v₂**.

```
ASCII Diagram: Linear Combination in ℝ²
      
      ^
      |           v = (3,4)
      |           *
      |         / |
      |       /   |
      |     /     |
      |   /       |
      | /         |
4 * v₂|           | 3 * v₁
------+-----------+------>
      |           |
```

## Span of a Set of Vectors

**Definition:** The **span** of a set of vectors S = {v₁, v₂, ..., vₖ} is the set of all possible linear combinations of those vectors. We denote this as Span(S) or span{v₁, v₂, ..., vₖ}.

**Mathematically:** Span(S) = {c₁v₁ + c₂v₂ + ... + cₖvₖ | c₁, c₂, ..., cₖ are scalars}

**Example 2:** In ℝ², the span of the single vector **v = (1, 2)** is:
Span{v} = {c*(1, 2) | c is a scalar} = all vectors on the line y = 2x

```
ASCII Diagram: Span of a Single Vector
      
      ^
      |       / line y = 2x
      |     /
      |   /
      | /
      +---------->
      | 
```

**Example 3:** In ℝ², the span of **v₁ = (1, 0)** and **v₂ = (0, 1)** is the entire ℝ² plane, because any vector (a, b) can be written as a*(1, 0) + b*(0, 1).

**Example 4:** In ℝ³, the span of **v₁ = (1, 0, 0)** and **v₂ = (0, 1, 0)** is the xy-plane (all vectors of the form (x, y, 0)).

### Properties of Span

- The span of any set of vectors in a vector space V is a subspace of V
- Span(S) is the smallest subspace containing all vectors in S
- If S ⊆ T, then Span(S) ⊆ Span(T)

## Linear Independence

**Definition:** A set of vectors {v₁, v₂, ..., vₖ} is **linearly independent** if the only solution to the equation:
c₁v₁ + c₂v₂ + ... + cₖvₖ = 0
is the trivial solution c₁ = c₂ = ... = cₖ = 0.

If there exist scalars not all zero that satisfy this equation, the vectors are **linearly dependent**.

**Example 5:** Are **v₁ = (1, 2)** and **v₂ = (2, 4)** linearly independent?
Set up the equation: c₁(1, 2) + c₂(2, 4) = (0, 0)
This gives the system:
c₁ + 2c₂ = 0
2c₁ + 4c₂ = 0
We can see that c₁ = 2, c₂ = -1 is a solution (not all zeros), so the vectors are linearly dependent.

**Example 6:** Are **v₁ = (1, 0)** and **v₂ = (0, 1)** linearly independent?
Set up: c₁(1, 0) + c₂(0, 1) = (0, 0)
This gives c₁ = 0 and c₂ = 0 as the only solution, so they are linearly independent.

## Testing for Linear Independence

To test if vectors v₁, v₂, ..., vₖ are linearly independent:

1. Form the matrix A with these vectors as columns
2. Solve the homogeneous system Ax = 0
3. If the only solution is x = 0, the vectors are linearly independent
4. If there are nontrivial solutions, they are linearly dependent

**Example 7:** Test if **v₁ = (1, 2, 3), v₂ = (4, 5, 6), v₃ = (7, 8, 9)** are linearly independent.

Form the matrix:
```
[1  4  7]
[2  5  8]
[3  6  9]
```

Solve the system:
```
x + 4y + 7z = 0
2x + 5y + 8z = 0  
3x + 6y + 9z = 0
```

We can see that v₃ = v₁ + v₂ (since (7,8,9) = (1,2,3) + (4,5,6)), so these vectors are linearly dependent.

## Relationship Between Linear Independence and Span

The concepts of linear independence and span are closely related:

- A set of vectors is a **basis** for a vector space if it is both linearly independent and spans the space
- The number of linearly independent vectors in a set cannot exceed the dimension of the space
- If vectors are linearly dependent, at least one vector is in the span of the others

## Comparison of Key Properties

| Property | Linear Independence | Linear Dependence |
|----------|---------------------|-------------------|
| Definition | Only trivial solution to c₁v₁+...+cₖvₖ=0 | Non-trivial solution exists |
| Span | Vectors contribute new dimensions | At least one vector is redundant |
| Matrix Rank | Full column rank | Column rank deficient |
| Geometric Meaning | Vectors point in "different directions" | Vectors lie in the same plane/line |

## Special Cases and Important Theorems

**Theorem:** Any set containing the zero vector is linearly dependent.
*Proof:* 1·0 + 0·v₁ + ... + 0·vₖ = 0, which is a nontrivial combination.

**Theorem:** In ℝⁿ, any set of more than n vectors must be linearly dependent.

**Theorem:** If a set of vectors is linearly independent, then any subset is also linearly independent.

## Applications in Different Contexts

### In Systems of Equations
Linear independence determines whether solutions are unique. If the coefficient matrix has linearly independent columns, the homogeneous system has only the trivial solution.

### In Basis and Dimension
A basis must be linearly independent and span the space. The number of vectors in a basis is the dimension of the space.

### In Linear Transformations
The concepts help understand the kernel and range of transformations. The dimension of the kernel relates to linear dependencies among vectors.

## Examples with Different Vector Types

**Polynomial Example:** Are p₁(x) = 1, p₂(x) = x, p₃(x) = x² linearly independent?
Consider: c₁·1 + c₂·x + c₃·x² = 0 for all x
This implies c₁ = c₂ = c₃ = 0, so they are linearly independent.

**Function Example:** Are f(x) = sin²x, g(x) = cos²x, h(x) = 1 linearly independent?
Note that 1·sin²x + 1·cos²x - 1·1 = 0 for all x, so they are linearly dependent.

## Exam Tips

1. **For span questions:** Ask "Can I write an arbitrary vector as a linear combination of these vectors?"
2. **For linear independence:** Set up the equation c₁v₁ + ... + cₖvₖ = 0 and solve for the coefficients
3. **Use matrix methods:** Form a matrix with vectors as columns and find its rank
4. **Geometric interpretation:** In ℝ² or ℝ³, think about whether vectors lie on the same line/plane
5. **Remember special cases:** Any set containing 0 is dependent; in ℝⁿ, more than n vectors must be dependent
6. **Check your work:** Verify that your solution actually works by plugging it back in
7. **For proofs:** Often using contradiction works well for independence proofs