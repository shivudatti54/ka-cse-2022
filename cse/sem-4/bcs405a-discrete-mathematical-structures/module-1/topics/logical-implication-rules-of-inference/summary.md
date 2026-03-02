# Logical Implication and Rules of Inference - Summary

## Key Definitions and Concepts

- **Logical Implication (p → q)**: A compound proposition false only when p is true and q is false; equivalent to ¬p ∨ q

- **Valid Argument**: An argument where true premises guarantee a true conclusion

- **Tautology**: Always true proposition; **Contradiction**: Always false proposition; **Contingency**: Neither

- **Contrapositive**: ¬q → ¬p (logically equivalent to original implication)

## Important Rules of Inference

| Rule                   | Premises     | Conclusion |
| ---------------------- | ------------ | ---------- |
| Modus Ponens           | p → q, p     | q          |
| Modus Tollens          | p → q, ¬q    | ¬p         |
| Hypothetical Syllogism | p → q, q → r | p → r      |
| Disjunctive Syllogism  | p ∨ q, ¬p    | q          |
| Addition               | p            | p ∨ q      |
| Simplification         | p ∧ q        | p          |
| Conjunction            | p, q         | p ∧ q      |

## Key Points

- Implication p → q is not logically equivalent to its converse (q → p) or inverse (¬p → ¬q)

- The contrapositive (¬q → ¬p) is always logically equivalent to the original implication

- Modus tollens can be viewed as applying modus ponens to the contrapositive

- A fallacy occurs when the conclusion does not necessarily follow from the premises

- Resolution (p ∨ q, ¬p ∨ r ⊢ q ∨ r) is fundamental to automated reasoning

## Common Mistakes to Avoid

1. Confusing modus ponens with affirming the consequent (invalid)

2. Treating converse and inverse as equivalent to the original implication

3. Forgetting that implication is true when antecedent is false (vacuous truth)

4. Applying rules incorrectly by mismatching premise patterns

## Revision Tips

1. Practice constructing truth tables for all compound propositions

2. Memorize all eight rules of inference with their premise-conclusion patterns

3. Solve at least 5 formal proof problems to understand step-by-step reasoning

4. Remember: whenever you have p → q and need to prove q, you need p (modus ponens)
