# Mathematical Induction - Summary

## Key Definitions and Concepts

- **Mathematical Induction**: A proof technique for establishing the truth of statements about all natural numbers n ≥ n₀
- **Weak (Simple) Induction**: Requires proving P(n₀) is true and P(k) → P(k+1) for all k ≥ n₀
- **Strong (Complete) Induction**: Requires proving base cases P(n₀) through P(m), and (P(n₀) ∧ P(n₀+1) ∧ ... ∧ P(k)) → P(k+1)
- **Inductive Hypothesis**: The assumption that P(k) is true (or all P(i) for i ≤ k in strong induction) used to prove P(k+1)
- **Well-Ordering Principle**: Every non-empty set of positive integers has a least element; equivalent to induction

## Important Formulas and Theorems

- **Sum of first n numbers**: Σi=1^n i = n(n+1)/2
- **Geometric Series**: Σi=0^n r^i = (r^(n+1) - 1)/(r - 1), for r ≠ 1
- **Sum of squares**: Σi=1^n i² = n(n+1)(2n+1)/6
- **Induction Equivalence**: Weak and strong induction are logically equivalent

## Key Points

- Mathematical induction proves statements for infinitely many values by establishing a "domino effect"
- The base case must be proven explicitly—never assume it's "obvious"
- In weak induction, only P(k) is assumed to prove P(k+1); in strong induction, all P(i) for i ≤ k are assumed
- Strong induction is essential for proofs involving factorization, prime numbers, and recursive definitions
- Algorithm correctness proofs use induction to verify base case and recursive case
- The inductive step must be proven for all k ≥ n₀, not just a specific value

## Common Mistakes to Avoid

- Forgetting to prove the base case or treating it as "obviously true"
- Using the inductive hypothesis incorrectly (e.g., trying to prove P(k) from P(k+1))
- Switching between weak and strong induction mid-proof without justification
- Off-by-one errors in indices when working with sequences or arrays
- Assuming the inductive hypothesis is true for the exact value needed without properly establishing the chain

## Revision Tips

- Memorize the standard structure: Base Case → Inductive Hypothesis → Inductive Step → Conclusion
- Practice proving common sum formulas until the process becomes automatic
- For exam problems, first identify whether weak or strong induction is appropriate
- Always explicitly state what you're assuming (the inductive hypothesis) and what you're proving
- Review algorithm correctness proofs and recurrence relation analyses as they commonly appear in exams