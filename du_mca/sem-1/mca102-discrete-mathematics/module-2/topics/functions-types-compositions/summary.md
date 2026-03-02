# Functions: Types and Compositions - Summary

## Key Definitions and Concepts
- **Domain/Codomain**: Input/output sets of a function
- **Injective**: Distinct inputs → distinct outputs
- **Surjective**: Codomain fully covered
- **Bijective**: Perfect input-output pairing
- **Composition**: Function chaining (g∘f)(x) = g(f(x))
- **Inverse**: Reverse mapping for bijections

## Important Formulas and Theorems
- **Inverse Uniqueness**: If f⁻¹ exists, it's unique
- **Composition Associativity**: h∘(g∘f) = (h∘g)∘f
- **Schröder-Bernstein Theorem**: If |A| ≤ |B| and |B| ≤ |A|, then |A| = |B|
- **Cardinality Relations**: For finite sets:
  - Injective ⇒ |A| ≤ |B|
  - Surjective ⇒ |A| ≥ |B|
  - Bijective ⇒ |A| = |B|

## Key Points
- Bijections enable reversible computations
- Composition is fundamental in middleware architectures
- Hash functions must be non-injective to handle collisions
- Database keys require injective mappings
- Inverse functions crucial in cryptography
- Characteristic functions implement set membership tests
- Function properties determine algorithm invertibility

## Common Mistakes to Avoid
- Assuming all functions have inverses (only bijections do)
- Confusing codomain with range/image
- Claiming injectivity without formal proof
- Neglecting composition domain compatibility
- Misapplying infinite set cardinality rules to finite cases

## Revision Tips
1. Practice constructing truth tables for function properties
2. Diagram functions with arrow representations
3. Solve previous years' DU questions on function composition
4. Implement function types in Python (e.g., using decorators)
5. Relate RSA encryption to bijective function concepts
6. Use Venn diagrams for set-function relationships