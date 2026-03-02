# Propositional and Predicate Logic - Summary

## Key Definitions and Concepts
- **Proposition**: Statement with definite truth value
- **Tautology**: Always true (e.g., p ∨ ¬p)
- **Contingency**: Depends on variable values
- **Predicate**: Function returning truth value (P(x))
- **Bound Variable**: Quantified variable in predicate logic

## Important Formulas and Theorems
- De Morgan's Laws:
  - ¬(p ∧ q) ≡ ¬p ∨ ¬q
  - ¬(p ∨ q) ≡ ¬p ∧ ¬q
- Implication Equivalence: p → q ≡ ¬p ∨ q
- Quantifier Negation:
  - ¬∀xP(x) ≡ ∃x¬P(x)
  - ¬∃xP(x) ≡ ∀x¬P(x)
- Distributive Laws:
  - p ∨ (q ∧ r) ≡ (p ∨ q) ∧ (p ∨ r)
  - p ∧ (q ∨ r) ≡ (p ∧ q) ∨ (p ∧ r)

## Key Points
- Truth tables exhaustively verify logical expressions
- Order of quantifiers affects meaning (∀x∃y ≠ ∃y∀x)
- Implication p→q is false only when p=T and q=F
- NAND and NOR are functionally complete sets
- Predicate logic extends propositional logic with variables and quantifiers
- Vacuous truth: ∀x(P(x)→Q(x)) is true if P(x) is always false
- Formal proofs require stated rules of inference

## Common Mistakes to Avoid
- Confusing ↔ (biconditional) with ≡ (logical equivalence)
- Misapplying quantifier scope (e.g., ∀xP(x) ∧ Q(x) vs ∀x(P(x) ∧ Q(x)))
- Forgetting implicit domain restrictions in predicates
- Incorrect truth table row counts (must have 2ⁿ rows)
- Assuming commutative property for implication (p→q ≠ q→p)

## Revision Tips
1. Practice with DU previous years' questions on logical equivalence proofs
2. Create flashcards for key laws (De Morgan, Absorption, Distribution)
3. Use Venn diagrams to visualize predicate logic statements
4. Solve at least 5 problems on nested quantifiers
5. Time yourself constructing 4-variable truth tables (16 rows)