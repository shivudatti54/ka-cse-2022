# Onto Functions - Summary

## Key Definitions and Concepts

- **Function**: A mapping f: A → B where each element in domain A is assigned exactly one element in codomain B.
- **Onto (Surjective) Function**: f: A → B is onto if ∀b ∈ B, ∃a ∈ A such that f(a) = b. Every element in the codomain has at least one preimage.
- **Range (Image)**: The set of all outputs {f(a) : a ∈ A}. For onto functions, Range(f) = B.
- **Bijective Function**: A function that is both one-to-one (injective) and onto (surjective).

## Important Formulas and Theorems

- **Number of onto functions** from n-element set to m-element set (n ≥ m):
  - Using Stirling numbers: m! × S(n, m)
  - Using inclusion-exclusion: mⁿ - C(m,1)(m-1)ⁿ + C(m,2)(m-2)ⁿ - ... + (-1)^(m-1)C(m,m-1)(1)ⁿ

- **Composition theorem**: If f: A → B is onto and g: B → C is onto, then g ∘ f: A → C is onto.

- **Pigeonhole principle**: If |A| < |B|, no onto function f: A → B exists.

## Key Points

1. An onto function ensures complete coverage of the codomain—no element is "left out."

2. To prove f is onto: Show that for any output, there exists an input that produces it.

3. To prove f is NOT onto: Find ONE element in the codomain with no preimage.

4. A function can be: one-to-one only, onto only, both (bijective), or neither.

5. For finite sets with |A| = n and |B| = m, onto functions exist only if n ≥ m.

6. The identity function f(x) = x is both one-to-one and onto (bijective).

7. The constant function f(x) = c is onto only if the codomain has exactly one element.

## Common Mistakes to Avoid

- Confusing codomain with range: The codomain is the target set; the range is actual outputs.
- Forgetting that onto requires EVERY element in codomain to be covered.
- Assuming composition being onto implies the first function is onto.
- Not considering the domain and codomain when determining onto property.

## Revision Tips

1. Practice identifying onto functions with various examples (finite and infinite sets).

2. Work through counting problems for onto functions between small finite sets.

3. Remember: "Onto" = "covers everything" = Range = Codomain.

4. Review the difference between injective, surjective, and bijective with contrasting examples.

5. Solve previous university exam questions on this topic to understand the question patterns.
