# Functions - One-to-One - Summary

## Key Definitions and Concepts

- **Function**: A relation f: A → B where each element in domain A maps to exactly one element in codomain B.
- **One-to-One (Injective) Function**: f is one-to-one if f(a₁) = f(a₂) implies a₁ = a₂ (distinct inputs give distinct outputs).
- **Onto (Surjective) Function**: Every element in codomain has at least one preimage.
- **Bijective Function**: Both one-to-one AND onto; has an inverse.
- **Composition**: (g∘f)(x) = g(f(x)); if f and g are one-to-one, then g∘f is one-to-one.

## Important Formulas and Theorems

- **One-to-one test**: f(a₁) = f(a₂) ⇒ a₁ = a₂
- **Contrapositive test**: a₁ ≠ a₂ ⇒ f(a₁) ≠ f(a₂)
- **Horizontal line test**: A function is one-to-one iff no horizontal line intersects its graph more than once.
- **Inverse existence**: f⁻¹ exists iff f is bijective.
- **Composition rule**: (f ∘ g)⁻¹ = g⁻¹ ∘ f⁻¹ (when f and g are bijective).

## Key Points

- Domain ⊆ Codomain; Range ⊆ Codomain; Range = {f(x) : x ∈ Domain}
- f(x) = x² is NOT one-to-one over ℤ (f(2) = f(-2) = 4)
- f(x) = 3x + 5 IS one-to-one over ℝ
- f(x) = x³ IS one-to-one over ℝ
- One-to-one functions are essential for creating encryption keys in cryptography
- Only bijective functions have true inverses
- Restricting domain can make a non-injective function injective

## Common Mistakes to Avoid

1. Confusing domain with codomain—know that Range ⊆ Codomain always.
2. Thinking one-to-one functions are the same as onto functions—they are different properties.
3. Believing every function has an inverse—only bijective functions do.
4. Forgetting that f(x) = x² is not one-to-one over ℤ; students often incorrectly assume it's injective.

## Revision Tips

1. Practice proving injectivity by assuming f(a₁) = f(a₂) and solving for a₁ = a₂.
2. Memorize the horizontal line test for quick visual verification.
3. Review composition properties—theorem about preserving injectivity is exam-friendly.
4. Create a table comparing one-to-one, onto, and bijective with at least two examples each.
