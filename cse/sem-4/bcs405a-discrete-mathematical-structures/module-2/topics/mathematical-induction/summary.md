# Mathematical Induction - Summary

## Key Definitions and Concepts

- **Mathematical Induction:** A proof technique for establishing truth of statements about natural numbers through a chain reaction from base case to all cases
- **Principle of Mathematical Induction (First Form):** If P(1) is true and P(k) → P(k+1) for all k ≥ 1, then P(n) is true for all n ∈ ℕ
- **Strong (Second) Mathematical Induction:** If P(1), P(2), ..., P(b) are true and P(1)∧P(2)∧...∧P(k) → P(k+1), then P(n) is true for all n ∈ ℕ
- **Extended PMI:** Allows starting induction from any integer m rather than 1

## Important Formulas and Theorems

- **Sum of first n natural numbers:** 1 + 2 + ... + n = n(n+1)/2
- **Sum of squares:** 1² + 2² + ... + n² = n(n+1)(2n+1)/6
- **Geometric sum:** 1 + r + r² + ... + r^n = (r^(n+1) - 1)/(r - 1), for r ≠ 1
- **Well-Ordering Principle:** Every non-empty set of natural numbers has a least element (logically equivalent to induction)

## Key Points

- Mathematical induction has two essential components: Base Case and Inductive Step
- The inductive hypothesis assumes P(k) is true and uses it to prove P(k+1)
- Weak induction uses only P(k) to prove P(k+1); strong induction can use P(1), P(2), ..., P(k)
- Strong induction is essential for recursively defined structures and problems involving divisibility by multiple cases
- Extended induction allows proving statements for n ≥ m where m ≠ 1
- The principle is logically equivalent to the Well-Ordering Principle and Strong Induction

## Common Mistakes to Avoid

- Forgetting to prove the base case (base case is mandatory)
- Using the inductive hypothesis incorrectly or not using it at all in the inductive step
- Starting induction from the wrong value (n=0 vs n=1 matters)
- Not clearly distinguishing between what is given and what needs to be proven in the inductive step
- Trying to use weak induction when strong induction is required (and vice versa)

## Revision Tips

1. Memorize the standard structure: Base Case → Inductive Hypothesis → Inductive Step → Conclusion
2. Practice at least 3-4 problems from each category: sum formulas, divisibility, and inequalities
3. Understand when strong induction is needed: recursive definitions, multiple previous cases, prime factorization
4. For divisibility proofs, practice the technique of expressing n+1 case in terms of n case plus additional terms
5. In exams, always explicitly state which form of induction you are using
