# Set Operations and Computer Representation - Summary

## Key Definitions and Concepts

- **Union (A ∪ B):** Set of elements in A or B or both
- **Intersection (A ∩ B):** Set of elements in both A and B
- **Difference (A − B):** Elements in A but not in B
- **Complement (Aᶜ):** Elements in universal set U but not in A
- **Bit Vector:** Binary string representing set membership where bit i = 1 if element uᵢ ∈ A, else 0

## Important Formulas and Theorems

- **De Morgan's Laws:** (A ∪ B)ᶜ = Aᶜ ∩ Bᶜ and (A ∩ B)ᶜ = Aᶜ ∪ Bᶜ
- **Distributive Laws:** A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C) and A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)
- **Bit Operations:** Union → OR (∨), Intersection → AND (∧), Complement → NOT (¬)
- **Set Difference:** A − B = A ∩ Bᶜ

## Key Points

- The universal set U must be explicitly defined for complement operations
- Bit vector representation requires a fixed ordering of universal set elements
- Empty set (∅) is the identity for union and the dominating element for intersection
- Universal set U is the identity for intersection and dominating element for union
- (Aᶜ)ᶜ = A (Double Complement Law)
- A − B = A ∩ Bᶜ = A − (A ∩ B)

## Common Mistakes to Avoid

- Confusing complement (Aᶜ) with difference (A − B)—they are equal only when B = Aᶜ
- Forgetting that bit vectors require a predefined ordering of universal set elements
- Applying complement without defining the universal set U
- Mixing up OR/AND operations for union/intersection in bit vector representation

## Revision Tips

1. Practice converting between set notation and bit vectors with at least 5 different examples
2. Memorize the truth tables for AND, OR, NOT to master bit vector operations
3. Draw Venn diagrams for three-set problems to visualize overlapping regions
4. Prove De Morgan's Laws step-by-step using element argument method
5. Solve previous year DU questions on set operations—similar patterns repeat every year