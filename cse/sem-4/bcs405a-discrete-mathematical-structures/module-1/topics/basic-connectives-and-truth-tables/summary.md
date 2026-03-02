# Basic Connectives and Truth Tables - Summary

## Key Definitions and Concepts

- **Proposition**: A declarative statement that is either definitely true (T) or definitely false (F), but not both.
- **Atomic Proposition**: A simple proposition represented by letters (p, q, r, etc.) without any connectives.
- **Compound Proposition**: Formed by combining atomic propositions using logical connectives.
- **Logical Connective**: An operator that combines propositions to form new propositions.

## Important Formulas and Theorems

**Truth Tables for Five Connectives:**

| p   | q   | ¬p  | p∧q | p∨q | p→q | p↔q |
| --- | --- | --- | --- | --- | --- | --- |
| T   | T   | F   | T   | T   | T   | T   |
| T   | F   | F   | F   | T   | F   | F   |
| F   | T   | T   | F   | T   | T   | F   |
| F   | F   | T   | F   | F   | T   | T   |

**Key Logical Equivalences:**

- **Implication Equivalence**: p → q ≡ ¬p ∨ q
- **De Morgan's Laws**: ¬(p ∧ q) ≡ ¬p ∨ ¬q; ¬(p ∨ q) ≡ ¬p ∧ ¬q
- **Biconditional**: p ↔ q ≡ (p → q) ∧ (q → p)

## Key Points

- Truth tables for n propositions require 2^n rows.
- Implication (p → q) is false only when p=T and q=F.
- A **tautology** is always true; a **contradiction** is always false; a **contingency** depends on component truth values.
- Operator precedence: ¬ > ∧ > ∨ > → > ↔
- Two propositions are logically equivalent if their truth tables are identical.
- The negation of "p AND q" is "NOT p OR NOT q" (De Morgan's Law).

## Common Mistakes to Avoid

1. Assuming implication requires causal relationship rather than treating it as a truth function.
2. Forgetting that disjunction (∨) is inclusive—it's true when both components are true.
3. Missing rows when constructing truth tables for multiple propositions.
4. Confusing logical equivalence (≡) with biconditional (↔).

## Revision Tips

1. Practice drawing truth tables for all connectives until they become automatic.
2. Memorize the standard logical equivalences—they simplify many problems.
3. Focus on understanding why implication behaves as it does (only false in one specific case).
4. Solve at least 5-10 truth table problems before the exam to build speed and accuracy.
