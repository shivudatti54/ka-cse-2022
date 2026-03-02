# Reasoning Patterns in Propositional Logic - Summary

## Key Definitions and Concepts

- **Argument:** A set of premises P₁, P₂, ..., Pₙ and a conclusion Q, denoted P₁, P₂, ..., Pₙ ⊢ Q
- **Valid Argument:** An argument where truth of all premises guarantees truth of conclusion
- **Sound Argument:** A valid argument with actually true premises
- **Rule of Inference:** A basic valid argument form used as a step in formal proofs
- **Formal Proof:** A sequence of statements where each follows from previous ones by rules of inference

## Important Formulas and Theorems

**Rules of Inference:**

- Modus Ponens: P → Q, P ⊢ Q
- Modus Tollens: P → Q, ¬Q ⊢ ¬P
- Hypothetical Syllogism: P → Q, Q → R ⊢ P → R
- Disjunctive Syllogism: P ∨ Q, ¬P ⊢ Q
- Addition: P ⊢ P ∨ Q
- Simplification: P ∧ Q ⊢ P
- Conjunction: P, Q ⊢ P ∧ Q
- Resolution: P ∨ Q, ¬P ∨ R ⊢ Q ∨ R

## Key Points

- Validity depends on logical form, not content or actual truth values
- Modus Ponens and Modus Tollens are the most frequently used rules
- A formal proof requires citing the specific rule for each step
- Proof by contradiction assumes ¬P and derives contradiction to prove P
- Proof by contraposition proves ¬Q → ¬P to establish P → Q
- All rules of inference preserve truth (are truth-preserving)
- Resolution is fundamental in automated theorem proving and Prolog

## Common Mistakes to

- Confusing validity with soundness
- Applying Modus Ponens to the converse: P → Q, Q ⊢ P (fallacy of affirming consequent)
- Applying Modus Tollens to the inverse: P → Q, ¬P ⊢ ¬Q (fallacy of denying antecedent)
- Skipping steps in formal proofs without justification
- Using invalid rules in proofs

## Revision Tips

1. Practice deriving conclusions from 2-3 premises using multiple rules
2. Create a table of all eight rules with examples for quick recall
3. Solve at least 5 formal proof exercises before the exam
4. Understand why the fallacies (affirming consequent, denying antecedent) are invalid
5. Remember: A valid argument with false premises can have a false conclusion
