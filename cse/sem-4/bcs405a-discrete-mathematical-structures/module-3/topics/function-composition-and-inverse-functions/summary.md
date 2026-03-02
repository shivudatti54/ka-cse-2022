# Function Composition and Inverse Functions - Summary

## Key Definitions and Concepts

- **Function:** A relation f: A → B where each element in domain A maps to exactly one element in codomain B.
- **Injective (One-to-One):** f(a₁) = f(a₂) ⇒ a₁ = a₂; distinct inputs yield distinct outputs.
- **Surjective (Onto):** For every b ∈ B, there exists a ∈ A such that f(a) = b; range equals codomain.
- **Bijective:** Both injective and surjective; required for inverse to exist.
- **Function Composition (g ∘ f):** Defined as (g ∘ f)(a) = g(f(a)); applies f first, then g.
- **Inverse Function f⁻¹:** A function such that f⁻¹(f(a)) = a and f(f⁻¹(b)) = b; exists only for bijective functions.

## Important Formulas and Theorems

- **(g ∘ f)⁻¹ = f⁻¹ ∘ g⁻¹** - Inverse of composition reverses the order
- **Associativity:** h ∘ (g ∘ f) = (h ∘ g) ∘ f
- **Identity:** I ∘ f = f ∘ I = f
- **Injective composition:** If f and g are injective, then g ∘ f is injective
- **Surjective composition:** If f and g are surjective, then g ∘ f is surjective

## Key Points

- Function composition is NOT commutative: f ∘ g ≠ g ∘ f in general
- Only bijective functions have true inverses
- To find inverse: solve y = f(x) for x, then swap variables
- Permutations are bijective functions from a set to itself
- The identity function serves as the neutral element for composition
- Domain and codomain must be specified when defining functions
- Range is a subset of codomain; range = codomain for surjective functions

## Common Mistakes to Avoid

1. Assuming all functions have inverses (only bijective functions do)
2. Confusing domain with codomain or codomain with range
3. Believing composition is commutative (it isn't!)
4. Forgetting to verify injectivity before claiming an inverse exists
5. Incorrectly applying the inverse composition formula (reversing order is crucial)

## Revision Tips

1. Practice proving injectivity and surjectivity with algebraic functions
2. Memorize the inverse composition formula and verify with examples
3. Draw mapping diagrams for functions on finite sets
4. Always verify inverses by checking both f(f⁻¹(x)) = x and f⁻¹(f(x)) = x
5. Review previous university exam questions on this topic for pattern recognition
