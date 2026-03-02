# Logic Equivalence and the Laws of Logic - Summary

## Key Definitions and Concepts

- **Logical Equivalence (≡)**: Two propositions have identical truth values under all interpretations; denoted p ≡ q
- **Tautology**: Proposition always true (e.g., p ∨ ¬p)
- **Contradiction**: Proposition always false (e.g., p ∧ ¬p)
- **Contingency**: Proposition neither always true nor always false

## Important Formulas and Theorems

| Law         | AND Form      | OR Form       |
| ----------- | ------------- | ------------- |
| Identity    | p ∧ T ≡ p     | p ∨ F ≡ p     |
| Domination  | p ∧ F ≡ F     | p ∨ T ≡ T     |
| Idempotent  | p ∧ p ≡ p     | p ∨ p ≡ p     |
| Commutative | p ∧ q ≡ q ∧ p | p ∨ q ≡ q ∨ p |
| Negation    | p ∧ ¬p ≡ F    | p ∨ ¬p ≡ T    |

**De Morgan's Laws**:

- ¬(p ∧ q) ≡ ¬p ∨ ¬q
- ¬(p ∨ q) ≡ ¬p ∧ ¬q

**Implication Equivalences**:

- p → q ≡ ¬p ∨ q
- p → q ≡ ¬q → ¬p (Contrapositive)
- p ↔ q ≡ (p → q) ∧ (q → p)

## Key Points

- Logical equivalence can be proved via truth tables (identical columns) or algebraic manipulation
- Always apply De Morgan's laws correctly: negate each component and change ∧ to ∨ (or vice versa)
- Convert implications to disjunctions early for easier simplification
- Absorption laws: p ∧ (p ∨ q) ≡ p and p ∨ (p ∧ q) ≡ p are powerful shortcuts
- The contrapositive of p → q is ¬q → ¬p (they are logically equivalent)
- Use truth tables when unsure—the method is always reliable

## Common Mistakes to Avoid

1. **Incorrect application of De Morgan's**: Forgetting to negate both components
2. **Confusing implication with equivalence**: p → q ≠ p ↔ q
3. **Wrong distribution**: p ∨ (q ∧ r) ≡ (p ∨ q) ∧ (p ∨ r), not (p ∨ q) ∧ r
4. **Assuming converse**: p → q is NOT equivalent to q → p

## Revision Tips

1. Create a quick reference card with all laws and review daily
2. Practice 5 truth table constructions to master the method
3. For simplification problems, work step-by-step and state each law used
4. Remember: implication is the hardest connective—always convert p → q to ¬p ∨ q first
