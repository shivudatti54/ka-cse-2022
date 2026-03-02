# Syntax and Semantics of First-Order Logic - Summary

## Key Definitions and Concepts

- **First-Order Logic (FOL)**: Extends propositional logic with quantifiers (∀, ∃), predicates, and variables to reason about objects and their properties.

- **Terms**: Expressions denoting objects - constants, variables, or function applications. Defined recursively: constants and variables are terms; if f is an n-ary function and t₁...tₙ are terms, then f(t₁...tₙ) is a term.

- **Atomic Formulas**: Predicates applied to terms, e.g., P(x, y), or equality expressions like x = y.

- **Well-Formed Formulas (WFFs)**: Formulas with correct syntax - built from atoms using connectives and quantifiers following recursive rules.

- **Bound vs Free Variables**: Variables within quantifier scope are bound; others are free. Formula truth requires assignments for free variables.

## Important Formulas and Theorems

- **¬∀x φ ≡ ∃x ¬φ** (Negation of universal)
- **¬∃x φ ≡ ∀x ¬φ** (Negation of existential)
- **∀x φ → φ[t/x]** (Universal instantiation)
- **φ[t/x] → ∃x φ** (Existential generalization)
- **∀x (φ → ψ) ≡ (∃x φ) → ψ** (if x not free in ψ)
- **∀x (φ ∧ ψ) ≡ (∀x φ) ∧ (∀x ψ)**
- **∃x (φ ∨ ψ) ≡ (∃x φ) ∨ (∃x ψ)**

## Key Points

- The alphabet consists of logical connectives, quantifiers, variables, constant symbols, function symbols, predicate symbols, parentheses, and equality.

- An interpretation assigns meaning: domain (non-empty set), constant → domain elements, functions → Dⁿ→D, predicates → subsets of Dⁿ.

- ∀x φ is true iff φ holds for all domain elements; ∃x φ is true iff φ holds for at least one domain element.

- Quantifier order matters: ∀x∃y R(x,y) ≠ ∃y∀x R(x,y) in general.

- Valid formulas are true under all interpretations; satisfiable under at least one; unsatisfiable under none.

- Scope of a quantifier is the subformula immediately following it.

## Common Mistakes to Avoid

- Confusing bound and free variables - remember variables can be both bound and free in different parts of the same formula.

- Swapping quantifier order assuming they are commutative - ∀x∃y is generally NOT equivalent to ∃y∀x.

- Forgetting that domain must be non-empty in interpretations.

- Incorrectly applying truth values for connectives, especially implications (only false when antecedent true and consequent false).

## Revision Tips

1. Practice constructing WFFs from English statements and vice versa.

2. Work through multiple interpretation examples to solidify understanding of truth evaluation.

3. Memorize the quantifier negation laws - they're essential for proof simplification.

4. Create truth tables for simple formulas with different interpretations to see when they hold or fail.
