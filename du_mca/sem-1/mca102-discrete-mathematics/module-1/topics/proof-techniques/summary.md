# Proof Techniques - Summary

## Key Definitions and Concepts

- **Direct Proof:** Proves P → Q by assuming P is true and logically deducing Q through valid implications.
- **Proof by Contradiction:** Assumes ¬P and derives a contradiction (Q ∧ ¬Q), concluding P must be true.
- **Proof by Contrapositive:** Proves ¬Q → ¬P (logically equivalent to P → Q) instead of the original statement.
- **Mathematical Induction:** Proves P(n) for all n ≥ 1 by establishing base case P(1) and inductive step (P(k) → P(k+1)).
- **Strong Induction:** Proves P(k+1) using assumption that P(1), P(2), ..., P(k) are all true.
- **Proof by Cases:** Divides the domain into exhaustive, mutually exclusive cases and proves statement for each.
- **Counterexample:** A specific instance that disproves a universal statement.

## Important Formulas and Theorems

- Principle of Mathematical Induction: [P(1) ∧ ∀k(P(k) → P(k+1))] → ∀n P(n)
- Strong Induction: [P(1) ∧ ∀k(P(1) ∧ P(2) ∧ ... ∧ P(k) → P(k+1))] → ∀n P(n)
- Logical Equivalence: P → Q ≡ ¬Q → ¬P (contrapositive)

## Key Points

- Direct proofs are preferred when the logical flow from hypothesis to conclusion is clear and straightforward.
- Proof by contradiction is especially powerful for proving negative statements, irrationality, and non-existence results.
- The contrapositive is logically equivalent to the original statement—prove either; the choice depends on which is easier.
- Mathematical induction requires two essential components: base case (usually n=1) and inductive step.
- Strong induction is necessary when P(k+1) depends on more than just P(k)—common in recursively defined structures.
- For proof by cases, ensure cases are exhaustive (cover all possibilities) and mutually exclusive (no overlap).
- Universal statements require proofs across all cases; a single counterexample disproves them.

## Common Mistakes to Avoid

1. **Forgetting the base case in induction:** The inductive step is meaningless without establishing the foundation—without P(1), the domino effect has no starting point.

2. **Assuming what needs to be proved:** Circular reasoning occurs when the proof assumes the conclusion directly or indirectly. Always start from known facts or given assumptions.

3. **Incorrect use of negation:** Many students struggle with negating compound statements. Remember: ¬(P ∧ Q) ≡ ¬P ∨ ¬Q, and ¬(P ∨ Q) ≡ ¬P ∧ ¬Q.

4. **Confusing contradiction with contrapositive:** These are different techniques. Contradiction introduces a new element (a contradiction), while contrapositive restructures the logical statement.

## Revision Tips

1. **Practice with classic proofs:** Master the standard proofs (even + even = even, √2 irrational, infinite primes, sum of first n integers) until the techniques become automatic.

2. **Work backwards from the conclusion:** When constructing a proof, sometimes it's helpful to start from what you want to prove and determine what would imply it, then work toward those conditions.

3. **Keep a proof technique checklist:** For each statement, ask: Is it universal? Existential? Does it involve negation? Does it concern natural numbers (indduction)? Does it have distinct cases?

4. **Time yourself on problems:** In exams, practice completing standard proof problems within 10-15 minutes to build speed and clarity.