# Propositional Logic - Summary

## Key Definitions and Concepts

- **Proposition:** A declarative statement that is either definitely true (T) or definitely false (F), but not both.
- **Atomic Proposition:** A simple proposition not containing other propositions (p, q, r).
- **Compound Proposition:** Formed by combining atomic propositions using logical connectives.
- **Logical Connectives:** ¬ (negation), ∧ (conjunction), ∨ (disjunction), → (implication), ↔ (biconditional).
- **Tautology:** Always true proposition regardless of truth values.
- **Contradiction:** Always false proposition regardless of truth values.
- **Contingency:** Neither tautology nor contradiction; truth depends on component values.
- **Logical Equivalence (≡):** Two propositions have identical truth values for all assignments.
- **Argument Validity:** An argument is valid if truth of premises guarantees truth of conclusion.

## Important Formulas and Theorems

- Implication equivalence: p → q ≡ ¬p ∨ q
- Biconditional equivalence: p ↔ q ≡ (p → q) ∧ (q → p)
- De Morgan's Laws: ¬(p ∧ q) ≡ ¬p ∨ ¬q, ¬(p ∨ q) ≡ ¬p ∧ ¬q
- Double Negation: ¬(¬p) ≡ p
- Distributive: p ∧ (q ∨ r) ≡ (p ∧ q) ∨ (p ∧ r), p ∨ (q ∧ r) ≡ (p ∨ q) ∧ (p ∨ r)
- Implication truth condition: p → q is FALSE only when p=TRUE and q=FALSE

## Key Points

- Truth table for n propositions has 2ⁿ rows
- All connectives except negation are binary; negation is unary
- Valid arguments: Modus Ponens (p → q, p ∴ q), Modus Tollens (p → q, ¬q ∴ ¬p)
- Invalid forms: Affirming consequent, denying antecedent
- CNF: Conjunction of disjunctions of literals (AND of ORs)
- DNF: Disjunction of conjunctions of literals (OR of ANDs)

## Common Mistakes to Avoid

1. Treating questions or commands as propositions—they lack definite truth values
2. Confusing p → q with q → p—implication is not commutative
3. Forgetting that p → q is true when p is false (vacuously true)
4. Applying De Morgan's laws incorrectly—negation must be distributed to each component
5. Confusing CNF with DNF—CNF has ∧ outside ∨ inside; DNF has ∨ outside ∧ inside

## Revision Tips

1. Practice constructing truth tables for all connectives until automatic
2. Memorize the key logical equivalences—they simplify complex problems
3. Remember: 2ⁿ rows for n propositions—don't try to list unnecessary combinations
4. For argument validity, check rows where ALL premises are TRUE; if conclusion can be FALSE, argument is invalid
5. Focus on implication truth condition—most exam errors occur here
6. Solve at least 5-10 problems from previous years to understand exam patterns
