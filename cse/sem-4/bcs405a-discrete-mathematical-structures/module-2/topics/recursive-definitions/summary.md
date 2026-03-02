# Recursive Definitions - Summary

## Key Definitions and Concepts

- **Recursive Definition**: A definition that defines an object in terms of simpler instances of itself, consisting of a base case and a recursive step.

- **Base Case**: The initial, explicitly defined elements of a recursively defined set or the starting value of a recursively defined function.

- **Recursive Step**: The rule that defines how to construct new elements from existing ones or how to compute new function values from previously computed values.

- **Structural Induction**: A proof technique used to prove properties about recursively defined structures, consisting of base case proof and inductive step proof.

- **Well-Ordering Principle**: Every non-empty subset of natural numbers has a least element; equivalent to mathematical induction.

## Important Formulas and Theorems

- **Factorial**: n! = 1 if n = 0; n! = n × (n-1)! if n ≥ 1

- **Fibonacci**: F(0) = 0, F(1) = 1; F(n) = F(n-1) + F(n-2) for n ≥ 2

- **Sum of First n Numbers**: S(0) = 0; S(n) = S(n-1) + n for n ≥ 1

- **Towers of Hanoi**: H(1) = 1; H(n) = 2H(n-1) + 1 for n ≥ 2, giving H(n) = 2^n - 1

- **Binary Strings**: b(0) = 1; b(n) = 2 × b(n-1) for n ≥ 1, giving b(n) = 2^n

## Key Points

- Every recursive definition requires both a basis (base case) and a recursive step to be complete.

- Recursive definitions can define infinite sets using a finite number of rules.

- The closure property ensures the recursive definition generates exactly the intended set.

- Structural induction mirrors mathematical induction but is tailored for recursively defined structures.

- Recursive definitions are foundational to algorithm design, data structures, and formal language theory.

- Well-ordering principle provides an alternative foundation for proof by induction.

- Understanding recursion is essential for analyzing recursive algorithms and their complexity.

## Common Mistakes to Avoid

- Forgetting the base case in a recursive definition, which leads to undefined or circular definitions.

- Failing to ensure the recursive step moves toward the base case, causing infinite recursion.

- Confusing the recursive definition with its closed-form solution (e.g., thinking H(n) = 2^n - 1 is the definition rather than a derived formula).

- In proofs by structural induction, not properly stating the inductive hypothesis.

- Omitting the proof that the recursive definition produces all intended elements (closure).

## Revision Tips

- Practice writing recursive definitions for common sets and functions until they become automatic.

- Work through multiple examples of computing values from recursive definitions by hand.

- Solve several structural induction proofs to master the technique.

- Connect recursive definitions to their equivalent iterative or closed-form representations.

- Review how recursive definitions appear in data structures and algorithm contexts.
