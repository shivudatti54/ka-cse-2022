# The Well-Ordering Principle and Mathematical Induction - Summary

## Key Definitions and Concepts

- **Well-Ordering Principle (WOP):** Every non-empty subset of natural numbers ℕ has a least element. Used in proofs by contradiction to find smallest counterexamples.

- **Mathematical Induction (Weak):** Prove P(n₀) true, then prove P(k) → P(k+1) for arbitrary k ≥ n₀. Conclude P(n) true for all n ≥ n₀.

- **Strong Mathematical Induction:** Prove base cases P(n₀) through P(n₀+m), then assume P(i) true for all i from n₀ to k, and prove P(k+1).

## Important Formulas and Theorems

- **Induction Principle:** [P(n₀) ∧ ∀k≥n₀ (P(k) → P(k+1))] → ∀n≥n₀ P(n)

- **Strong Induction Principle:** [Base cases ∧ ∀k≥n₀ (P(n₀) ∧ P(n₀+1) ∧ ... ∧ P(k) → P(k+1))] → ∀n≥n₀ P(n)

- **WOP-Induction Equivalence:** Both principles are logically equivalent; each can prove the other.

## Key Points

- Both WOP and mathematical induction apply specifically to natural numbers, not all integer sets

- Weak induction requires exactly one base case; strong induction may require multiple base cases

- Strong induction is more general than weak induction—every weak induction proof is also a strong induction proof

- Common induction applications: sum formulas, divisibility proofs, inequalities, recursive algorithm correctness

- WOP is particularly useful when the inductive step requires going backward to find a contradiction

- The assumption in the inductive hypothesis is that P(k) is TRUE—we use this to prove P(k+1)

## Common Mistakes to Avoid

- Forgetting the base case—this makes the entire proof invalid
- Using the wrong base case (n = 1 when n = 0 is required or vice versa)
- Not clearly stating the induction hypothesis in exam answers
- Confusing weak induction (P(k) → P(k+1)) with strong induction (all previous cases → P(k+1))
- Assuming the inductive step proves the statement for all cases without establishing the base case

## Revision Tips

1. Practice at least 5-6 induction problems covering different patterns (sums, divisibility, inequalities)

2. Memorize the structure of both weak and strong induction proofs as flowcharts

3. When stuck on an induction problem, try writing out P(k) and P(k+1) explicitly to see the relationship

4. For divisibility proofs, express the term in terms of the inductive hypothesis plus a multiple of the divisor

5. Review the relationship between WOP and induction—they are proven equivalent in advanced treatments
