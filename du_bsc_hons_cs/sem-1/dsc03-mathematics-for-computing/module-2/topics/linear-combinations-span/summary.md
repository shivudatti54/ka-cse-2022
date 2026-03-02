# Linear Combinations and Span - Summary

## Key Definitions and Concepts

- **Linear Combination**: A vector **v** = c₁**v₁** + c₂**v₂** + ... + cₖ**vₖ** where c₁, c₂, ..., cₖ are scalars

- **Span**: span{**v₁**, **v₂**, ..., **vₖ**} = {c₁**v₁** + c₂**v₂** + ... + cₖ**vₖ** : cᵢ ∈ ℝ} — the set of all possible linear combinations

- **Linearly Dependent**: ∃ scalars, not all zero, such that c₁**v₁** + ... + cₖ**vₖ** = **0**

- **Linearly Independent**: Only solution to c₁**v₁** + ... + cₖ**vₖ** = **0** is c₁ = c₂ = ... = cₖ = 0

- **Basis**: A set that spans the space AND is linearly independent

## Important Formulas and Theorems

- **Span equation**: **v** ∈ span{S} ⟺ ∃ scalars c₁,...,cₖ such that **v** = Σcᵢ**vᵢ**

- **Key theorem**: In ℝⁿ, any set of more than n vectors is linearly dependent

- **Key theorem**: n linearly independent vectors in ℝⁿ form a basis and span ℝⁿ

- **Standard basis**: ℝⁿ has basis {e₁, e₂, ..., eₙ} where eᵢ has 1 in position i, 0 elsewhere

## Key Points

- Span of one non-zero vector in ℝⁿ = line through origin
- Span of two linearly independent vectors in ℝ³ = plane through origin
- The zero vector is always in any span (trivial combination)
- Adding a dependent vector to a set does not increase its span
- Linear combinations correspond to matrix-vector multiplication: A**c**
- The standard basis vectors (1,0,...,0), (0,1,0,...,0), ..., (0,...,0,1) span ℝⁿ

## Common Mistakes to Avoid

- Assuming any two vectors span ℝ³ (they span only a plane, not the full 3D space)
- Forgetting that linear dependence requires at least one non-zero coefficient
- Confusing span with the set itself (span includes ALL linear combinations)
- Not checking if coefficients exist before claiming a vector is in the span

## Revision Tips

- Practice converting between span descriptions and parametric equations
- Always verify linear combinations by substitution
- For geometric problems in ℝ³, sketch or visualize the planes/lines
- Memorize the relationship: n independent vectors in ℝⁿ = basis = spans ℝⁿ
- Use row reduction on augmented matrices for efficient computation