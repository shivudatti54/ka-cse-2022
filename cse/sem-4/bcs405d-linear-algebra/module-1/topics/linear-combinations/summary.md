# Linear Combinations - Summary

## Key Definitions and Concepts

- **Linear Combination**: An expression c₁v₁ + c₂v₂ + ... + cₙvₙ where c₁, c₂, ..., cₙ are scalars and v₁, v₂, ..., vₙ are vectors
- **Span**: The set of all possible linear combinations of a set of vectors, denoted span{v₁, v₂, ..., vₙ}
- **Trivial Combination**: When all coefficients equal zero, producing the zero vector
- **Linear Dependence**: When vectors can be combined with non-zero coefficients to produce the zero vector
- **Linear Independence**: When the only combination producing zero is the trivial one

## Important Formulas and Theorems

- **Linear Combination Equation**: c₁v₁ + c₂v₂ + ... + cₙvₙ = b
- **Matrix Form**: Ac = b, where A = [v₁ v₂ ... vₙ], c = [c₁ c₂ ... cₙ]ᵀ
- **Span Definition**: span{v₁, ..., vₙ} = {c₁v₁ + ... + cₙvₙ : cᵢ ∈ ℝ}
- **Existence Condition**: b is in span{v₁, ..., vₙ} if and only if rank(A) = rank([A|b])
- **Dependence Theorem**: Vectors are linearly dependent if and only if one can be expressed as a combination of others

## Key Points

- Linear combinations generalize the idea of adding scaled vectors together
- The span tells us the complete "coverage" of a set of vectors—everything reachable through combinations
- In ℝ², two non-collinear vectors span the entire plane; in ℝ³, three non-coplanar vectors span the entire space
- Row reduction on augmented matrices [A|b] systematically determines if solutions exist
- Multiple solutions are possible when a vector can be expressed as a linear combination in different ways
- The zero vector is always in the span of any set of vectors
- Adding more vectors to a set can never decrease the span—it either maintains or expands it

## Common Mistakes to Avoid

- Confusing "span" with a specific combination—span is the collection of ALL combinations
- Forgetting that coefficients can be negative, zero, or positive
- Assuming linear dependence automatically means one vector is a multiple of another (only true for 2 vectors)
- Neglecting to check consistency conditions when determining if b is in the span

## Revision Tips

- Practice converting vector equations to augmented matrices and solving via row reduction
- Always verify your coefficient solutions by substituting back into the original equation
- Draw geometric interpretations in ℝ² and ℝ³ to build intuition
- Memorize the rank condition for linear combination existence—it frequently appears in exams
- Work through at least 5-10 problems covering different scenarios (2D, 3D, different numbers of vectors)
