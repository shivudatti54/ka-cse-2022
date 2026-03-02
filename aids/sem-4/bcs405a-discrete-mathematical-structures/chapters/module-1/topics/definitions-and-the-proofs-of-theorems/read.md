# **Definitions and the Proofs of Theorems**

## **Introduction**

In the realm of discrete mathematical structures, definitions and the proofs of theorems serve as the building blocks for constructing and proving theorems. A definition is a statement that provides a clear and concise explanation of a mathematical concept, while a proof is a logical argument that establishes the truth of a theorem.

## **Definitions**

- **Definition of a Theorem**: A theorem is a statement that has been rigorously proved to be true for all possible values of its variables.
- **Definition of a Proof**: A proof is a logical argument that establishes the truth of a theorem by using axioms, definitions, and previously proved theorems.
- **Definition of an Axiom**: An axiom is a statement that is accepted as true without proof, serving as the foundation for a mathematical theory.

## **Key Concepts**

- **Induction**: A method of proof that involves using mathematical induction to establish the truth of a statement.
  - **Strong Induction**: A type of induction that assumes the statement is true for all values up to some arbitrary point, and then proves it is true for the next value.
  - **Weak Induction**: A type of induction that assumes the statement is true for some values, and then proves it is true for the next value.
- **Proof by Contradiction**: A method of proof that involves assuming the opposite of what is to be proven, and then showing that this assumption leads to a logical contradiction.
- **Direct Proof**: A method of proof that involves using a series of logical steps to establish the truth of a statement.

## **Examples**

### Example 1: Proving a Theorem using Induction

Suppose we want to prove the following theorem:

"The sum of the first `n` positive integers is equal to `n(n + 1)/2`."

**Proof by Induction**

- **Base Case**: We assume `n = 1`, and show that the statement is true.
  - `1(1 + 1)/2 = 1`
  - The statement is true for `n = 1`.
- **Inductive Step**: We assume the statement is true for some arbitrary value `k`, and then prove it is true for `k + 1`.
  - `k(k + 1)/2 + (k + 1)`
  - Simplifying, we get `(k^2 + k) + (k + 1)`
  - Combining like terms, we get `(k^2 + 2k + 1)`
  - Factoring, we get `(k + 1)^2`
  - The statement is true for `k + 1`.
- **Conclusion**: By mathematical induction, the statement is true for all values of `n`.

### Example 2: Proving a Theorem using Proof by Contradiction

Suppose we want to prove the following theorem:

"The square of an even number is always divisible by 4."

**Proof by Contradiction**

- **Assume the opposite**: Assume that there exists an even number `x` such that `x^2` is not divisible by 4.
- **Reach a contradiction**: If `x` is even, then `x = 2k` for some integer `k`.
  - `x^2 = (2k)^2 = 4k^2`
  - Since `4k^2` is divisible by 4, we have reached a contradiction.
- **Conclusion**: By proof by contradiction, the statement is true for all even numbers.

### Example 3: Proving a Theorem using Direct Proof

Suppose we want to prove the following theorem:

"The sum of the interior angles of a triangle is always 180 degrees."

**Direct Proof**

- **Step 1**: Let `ABC` be a triangle with interior angles `A`, `B`, and `C`.
- **Step 2**: We can use the fact that the sum of the interior angles of a triangle is equal to 180 degrees.
- **Step 3**: We can use the fact that the sum of the interior angles of a triangle is equal to 180 degrees.
- **Conclusion**: By direct proof, the statement is true for all triangles.
