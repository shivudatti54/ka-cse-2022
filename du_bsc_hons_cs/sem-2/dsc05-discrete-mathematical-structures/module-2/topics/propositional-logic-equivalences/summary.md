# Propositional Logic Equivalences - Summary

## Key Definitions and Concepts

- **Tautology:** A proposition always true regardless of component truth values (denoted T)
- **Contradiction:** A proposition always false regardless of component truth values (denoted F)
- **Contingency:** A proposition whose truth depends on its components' truth values
- **Logical Equivalence (P ≡ Q):** Two propositions with identical truth values under all interpretations; equivalently, P ↔ Q is a tautology

## Important Formulas and Theorems

**Identity Laws:** P ∧ T ≡ P, P ∨ F ≡ P

**Domination Laws:** P ∨ T ≡ T, P ∧ F ≡ F

**Idempotent Laws:** P ∧ P ≡ P, P ∨ P ≡ P

**Complement Laws:** P ∧ ¬P ≡ F, P ∨ ¬P ≡ T, ¬T ≡ F, ¬F ≡ T

**Double Negation:** ¬(¬P) ≡ P

**Commutative Laws:** P ∧ Q ≡ Q ∧ P, P ∨ Q ≡ Q ∨ P

**Associative Laws:** (P ∧ Q) ∧ R ≡ P ∧ (Q ∧ R), (P ∨ Q) ∨ R ≡ P ∨ (Q ∨ R)

**Distributive Laws:** P ∧ (Q ∨ R) ≡ (P ∧ Q) ∨ (P ∧ R), P ∨ (Q ∧ R) ≡ (P ∨ Q) ∧ (P ∨ R)

**De Morgan's Laws:** ¬(P ∧ Q) ≡ ¬P ∨ ¬Q, ¬(P ∨ Q) ≡ ¬P ∧ ¬Q

**Absorption Laws:** P ∧ (P ∨ Q) ≡ P, P ∨ (P ∧ Q) ≡ P

## Key Points

- Logical equivalence requires identical truth values in ALL rows of a combined truth table
- The biconditional P ↔ Q is true exactly when P and Q have the same truth value
- De Morgan's laws transform negation of conjunctions to disjunctions and vice versa, flipping connectives
- Algebraic proofs require citing the specific law at each transformation step
- 2^n rows are needed in a truth table for n propositional variables
- Logical equivalences enable circuit minimization and query optimization in practical applications

## Common Mistakes to Avoid

- Confusing the biconditional connective (↔) with the equivalence relation (≡)
- Forgetting to flip the connective when applying De Morgan's laws
- Incomplete truth tables missing some variable combinations
- Incorrectly applying distributive law—remember it works both ways
- Assuming P → Q ≡ Q → P (implication is not commutative)

## Revision Tips

- Practice constructing truth tables for 3-variable expressions until fluent
- Memorize all 10-12 fundamental equivalence laws with their names
- Work through at least 5 algebraic proof problems to master transformation techniques
- Verify algebraic simplifications with truth tables as a check