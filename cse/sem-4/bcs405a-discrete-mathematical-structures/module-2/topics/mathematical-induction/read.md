# Mathematical Induction

## Table of Contents

- [Mathematical Induction](#mathematical-induction)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Principle of Mathematical Induction (First/Weak Form)](#principle-of-mathematical-induction-firstweak-form)
  - [Strong (Second) Mathematical Induction](#strong-second-mathematical-induction)
  - [Extended Principle of Mathematical Induction](#extended-principle-of-mathematical-induction)
  - [Important Theorems](#important-theorems)
- [Examples](#examples)
  - [Example 1: Sum of First n Natural Numbers](#example-1-sum-of-first-n-natural-numbers)
  - [Example 2: Divisibility Proof](#example-2-divisibility-proof)
  - [Example 3: Strong Induction - Fibonacci Numbers](#example-3-strong-induction---fibonacci-numbers)
  - [Example 4: Inequality Proof](#example-4-inequality-proof)
- [Exam Tips](#exam-tips)

## Introduction

Mathematical induction is one of the most fundamental and powerful proof techniques in discrete mathematics and computer science. It serves as the cornerstone for proving statements about natural numbers, which are ubiquitous in algorithm analysis, recursive algorithms, and theoretical computer science. The principle of mathematical induction allows us to establish the truth of an infinite sequence of statements by verifying only two conditions: a base case and an inductive step. This elegant technique transforms what might appear to be an infinite task into a finite, manageable proof.

The significance of mathematical induction in the context of the university's Discrete Mathematical Structures cannot be overstated. It forms the theoretical foundation for understanding recursive algorithms, proving correctness of programs, analyzing time complexity, and establishing properties of data structures. Every computer scientist must master this technique as it appears repeatedly in courses like Data Structures, Design and Analysis of Algorithms, Theory of Computation, and Cryptography. Beyond academics, induction is a critical thinking skill that helps in solving complex problems systematically.

## Key Concepts

### Principle of Mathematical Induction (First/Weak Form)

The Principle of Mathematical Induction states that for any predicate P(n) defined on natural numbers, if we can prove:

1. **Base Case**: P(1) is true (or P(0) if starting from 0)
2. **Inductive Step**: For any arbitrary natural number k ≥ 1, if P(k) is true, then P(k+1) is true

Then we can conclude that P(n) is true for all natural numbers n ≥ 1.

The intuition behind this principle is analogous to an infinite row of dominoes falling. If we push the first domino (base case) and ensure that whenever one domino falls, it knocks down the next one (inductive step), then all dominoes will fall. This chain reaction establishes the truth for the entire infinite sequence.

**Mathematical Formulation:**
Let P(n) be a statement about natural number n. If:

- P(1) is true (base case)
- ∀k ∈ ℕ: P(k) → P(k+1) is true (indductive step)

Then ∀n ∈ ℕ: P(n) is true.

### Strong (Second) Mathematical Induction

The Strong or Complete Principle of Mathematical Induction provides a more powerful tool when the relationship between statements is not just with the immediate predecessor but with all previous cases. In strong induction:

1. **Base Case**: P(1), P(2), ..., P(b) are true (where b is a positive integer, often b = 1)
2. **Inductive Step**: If P(1), P(2), ..., P(k) are all true, then P(k+1) is true

This principle is particularly useful when P(k+1) depends not just on P(k) but on any or all of P(1), P(2), ..., P(k).

**When to use Strong Induction:**

- When proving properties of recursively defined structures
- When the inductive step requires using multiple previous cases
- For proving statements about factors, divisors, and prime numbers
- In algorithm analysis where complexity depends on subproblems

### Extended Principle of Mathematical Induction

The extended form allows us to start from any integer m (not necessarily 1 or 0). If P(m) is true and P(k) → P(k+1) holds for all k ≥ m, then P(n) is true for all n ≥ m.

### Important Theorems

**Well-Ordering Principle:** Every non-empty set of natural numbers has a least element. This is logically equivalent to mathematical induction.

**Theorem Relationship:** The following are logically equivalent:

- Principle of Mathematical Induction
- Strong Mathematical Induction
- Well-Ordering Principle

## Examples

### Example 1: Sum of First n Natural Numbers

**Problem:** Prove that 1 + 2 + 3 + ... + n = n(n+1)/2 for all n ∈ ℕ

**Solution:**

**Step 1: Base Case (n = 1)**
Let P(n): 1 + 2 + 3 + ... + n = n(n+1)/2

For n = 1: LHS = 1, RHS = 1(2)/2 = 1
Therefore, P(1) is true.

**Step 2: Inductive Hypothesis**
Assume P(k) is true for some arbitrary k ≥ 1
That is: 1 + 2 + 3 + ... + k = k(k+1)/2

**Step 3: Inductive Step**
We need to prove P(k+1): 1 + 2 + 3 + ... + k + (k+1) = (k+1)(k+2)/2

Starting from the left-hand side:
1 + 2 + 3 + ... + k + (k+1)
= [k(k+1)/2] + (k+1) [Using inductive hypothesis]
= (k+1)(k/2 + 1)
= (k+1)(k + 2)/2
= (k+1)(k+2)/2

This is exactly the right-hand side of P(k+1). Hence, P(k+1) is true.

**Conclusion:** By the Principle of Mathematical Induction, P(n) is true for all n ∈ ℕ.

---

### Example 2: Divisibility Proof

**Problem:** Prove that 3^(2n) - 1 is divisible by 8 for all n ∈ ℕ

**Solution:**

**Step 1: Base Case (n = 1)**
For n = 1: 3^(2) - 1 = 9 - 1 = 8
8 is divisible by 8. So P(1) is true.

**Step 2: Inductive Hypothesis**
Assume P(k) is true for some arbitrary k ≥ 1
That is: 3^(2k) - 1 is divisible by 8
So, 3^(2k) - 1 = 8m for some integer m

**Step 3: Inductive Step**
We need to prove P(k+1): 3^(2(k+1)) - 1 is divisible by 8

3^(2(k+1)) - 1 = 3^(2k+2) - 1
= 3^2 · 3^(2k) - 1
= 9 · 3^(2k) - 1
= (8 + 1) · 3^(2k) - 1 [Writing 9 as 8 + 1]
= 8 · 3^(2k) + 3^(2k) - 1
= 8 · 3^(2k) + (3^(2k) - 1)
= 8 · 3^(2k) + 8m [Using inductive hypothesis]
= 8(3^(2k) + m)

Since 3^(2k) + m is an integer, 3^(2(k+1)) - 1 is divisible by 8.

**Conclusion:** By mathematical induction, 3^(2n) - 1 is divisible by 8 for all n ∈ ℕ.

---

### Example 3: Strong Induction - Fibonacci Numbers

**Problem:** Prove that for the Fibonacci sequence defined as F(1) = 1, F(2) = 1, F(n) = F(n-1) + F(n-2) for n ≥ 3, we have F(n) < 2^n for all n ∈ ℕ

**Solution:**

**Step 1: Base Cases**
For n = 1: F(1) = 1 < 2^1 = 2 → True
For n = 2: F(2) = 1 < 2^2 = 4 → True

**Step 2: Inductive Hypothesis**
Assume F(i) < 2^i is true for all i where 1 ≤ i ≤ k (for some k ≥ 2)

**Step 3: Inductive Step**
We need to prove F(k+1) < 2^(k+1)

Using the definition: F(k+1) = F(k) + F(k-1)

By inductive hypothesis:
F(k) < 2^k
F(k-1) < 2^(k-1)

Therefore:
F(k+1) = F(k) + F(k-1)
< 2^k + 2^(k-1)
< 2^k + 2^k [Since 2^(k-1) < 2^k]
= 2 · 2^k
= 2^(k+1)

Hence F(k+1) < 2^(k+1)

**Conclusion:** By strong mathematical induction, F(n) < 2^n for all n ∈ ℕ.

---

### Example 4: Inequality Proof

**Problem:** Prove that 2^n > n^2 for all n ≥ 5

**Solution:**

**Step 1: Base Case (n = 5)**
For n = 5: 2^5 = 32, 5^2 = 25
32 > 25, so P(5) is true.

**Step 2: Inductive Hypothesis**
Assume P(k) is true for some k ≥ 5
That is: 2^k > k^2

**Step 3: Inductive Step**
We need to prove P(k+1): 2^(k+1) > (k+1)^2

2^(k+1) = 2 · 2^k

> 2 · k^2 [Using inductive hypothesis]

We need to show: 2k^2 > (k+1)^2 for k ≥ 5

2k^2 - (k+1)^2 = 2k^2 - (k^2 + 2k + 1)
= k^2 - 2k - 1
= (k - 1)^2 - 2

For k ≥ 5: (k - 1)^2 - 2 ≥ 4^2 - 2 = 14 > 0

Therefore: 2k^2 > (k+1)^2

Thus: 2^(k+1) > 2k^2 > (k+1)^2

Hence P(k+1) is true.

**Conclusion:** By extended mathematical induction, 2^n > n^2 for all n ≥ 5.

## Exam Tips

1. **Identify the Base Case Correctly:** Determine whether the proof starts from n=0, n=1, or any other value. Many students lose marks by incorrectly starting the induction.

2. **Write Clear Inductive Hypothesis:** Explicitly state "Assume P(k) is true for some arbitrary k ≥ [base value]" before proceeding to prove P(k+1).

3. **Maintain Balance in Inductive Step:** When manipulating expressions, ensure you transform the left-hand side to match the right-hand side or vice versa consistently.

4. **Know When to Use Strong Induction:** If your inductive step requires using more than just P(k) to prove P(k+1), switch to strong induction. Common indicators include recursive definitions and statements about divisibility or factors.

5. **Practice Common Induction Patterns:** Sum formulas, divisibility proofs, and inequality proofs are the most common types in university exams. Master these standard patterns.

6. **Check Small Values:** Before writing your formal proof, verify the statement for initial values (n=1,2,3...) to understand the pattern and catch errors.

7. **For Divisibility Proofs:** Express the term for (k+1) in terms of the k-th term plus additional terms. This often involves adding and subtracting the same quantity strategically.

8. **State Conclusion Clearly:** End your proof with "Therefore, by the Principle of Mathematical Induction, P(n) is true for all n ∈ ℕ" to demonstrate understanding.

9. **Watch Out for Off-by-One Errors:** In extended induction problems, clearly state the starting point and ensure all inequalities and equalities are adjusted accordingly.

10. **Time Management:** In exam questions, if you're stuck on a complex inductive step, check if you can use strong induction or if there's an alternative approach that simplifies the proof.
