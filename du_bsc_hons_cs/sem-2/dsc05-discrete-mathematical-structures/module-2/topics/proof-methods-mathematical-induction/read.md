# Proof Methods: Mathematical Induction

## Introduction

Mathematical induction is one of the most fundamental and powerful proof techniques in discrete mathematics and computer science. It serves as the backbone for proving statements about natural numbers, algorithm correctness, program termination, and numerous properties of data structures. For Computer Science students at the University of Delhi, mastering mathematical induction is not merely an academic exercise—it is an essential skill that underlies the theoretical foundations of computing.

The principle of mathematical induction is deeply connected to the well-ordering principle, which states that every non-empty set of natural numbers has a least element. This intuitive concept allows us to establish the truth of infinitely many statements by proving only two key components: the base case and the inductive step. In the context of algorithm design and analysis, induction proves invaluable when demonstrating that recursive algorithms produce correct results, when establishing invariants in loops, and when analyzing divide-and-conquer recurrences.

This module explores both weak (simple) mathematical induction and strong (complete) mathematical induction, examining their theoretical foundations, procedural differences, and diverse applications in computer science. Understanding when to apply each variant and recognizing the subtle distinctions between them is crucial for solving complex proof problems encountered in university examinations and research.

## Key Concepts

### Principle of Mathematical Induction (Weak Induction)

The Principle of Mathematical Induction states that to prove a statement P(n) for all natural numbers n ≥ n₀, it suffices to establish two facts:

1. **Base Case**: P(n₀) is true, where n₀ is typically 0 or 1
2. **Inductive Step**: For every integer k ≥ n₀, if P(k) is true, then P(k+1) is also true

This creates a domino effect: once the base case is established and the inductive step is proven, the truth of P(n) cascades from n₀ to n₀+1, then to n₀+2, and so on indefinitely. The assumption that P(k) is true in the inductive step is called the **inductive hypothesis**.

The logical structure can be expressed as:
∀n ≥ n₀ [P(n₀) ∧ ∀k ≥ n₀ (P(k) → P(k+1))] → ∀n ≥ n₀ P(n)

### Strong Mathematical Induction

Strong (or complete) mathematical induction differs from weak induction in the inductive step. Instead of assuming P(k) implies P(k+1), we assume that P(n₀), P(n₀+1), ..., P(k) are all true to prove P(k+1). This is particularly useful when the truth of P(k+1) depends not only on P(k) but on earlier cases as well.

The strong induction principle requires:
1. **Base Case(s)**: P(n₀), P(n₀+1), ..., P(m) are true for a finite number of initial values
2. **Inductive Step**: For k ≥ m, if P(i) is true for all i where n₀ ≤ i ≤ k, then P(k+1) is true

### Relationship Between Weak and Strong Induction

A fundamental theorem states that weak and strong mathematical induction are equivalent. If a statement can be proven using strong induction, it can also be proven using weak induction (possibly with a different base case), and vice versa. However, strong induction often provides a more direct and elegant proof path when the statement's truth at (k+1) depends on multiple previous cases.

### Well-Ordering Principle

The Well-Ordering Principle states: Every non-empty subset of positive integers has a least element. This principle is logically equivalent to mathematical induction and is often used in contradiction proofs. For instance, if we assume there exists some natural number for which P(n) is false, we can consider the smallest such counterexample and derive a contradiction.

## Examples

### Example 1: Sum of First n Natural Numbers (Weak Induction)

**Prove**: For all n ∈ ℕ, 1 + 2 + 3 + ... + n = n(n+1)/2

**Proof by Weak Induction**:

*Base Case (n = 1)*:
Left side: 1
Right side: 1(1+1)/2 = 1(2)/2 = 1
Thus, P(1) is true.

*Inductive Step*:
Assume P(k) is true for some arbitrary k ≥ 1:
1 + 2 + ... + k = k(k+1)/2

We must prove P(k+1):
1 + 2 + ... + k + (k+1) = (k+1)(k+2)/2

Starting from the inductive hypothesis:
1 + 2 + ... + k + (k+1) = k(k+1)/2 + (k+1)
= (k+1)(k/2 + 1)
= (k+1)(k + 2)/2
= (k+1)((k+1)+1)/2

Thus, P(k+1) is true. By the principle of mathematical induction, the statement holds for all n ∈ ℕ.

### Example 2: Divisibility Proof (Strong Induction)

**Prove**: For all n ≥ 2, n is divisible by some prime number. (Fundamental Theorem of Arithmetic existence)

**Proof by Strong Induction**:

*Base Cases*:
- n = 2: 2 is prime, so 2 divides itself. True.
- n = 3: 3 is prime, so 3 divides itself. True.

*Inductive Step*:
Assume the statement is true for all integers i where 2 ≤ i ≤ k. We prove for k+1.

Consider k+1:
- If k+1 is prime, then k+1 divides itself, and we're done.
- If k+1 is composite, then k+1 = a × b where 2 ≤ a, b ≤ k

By the inductive hypothesis, a has a prime divisor p. Since p divides a and a divides (k+1), p divides (k+1). Thus, k+1 has a prime divisor.

Therefore, by strong induction, every integer n ≥ 2 has a prime divisor.

### Example 3: Algorithm Correctness - Recursive Sum

**Problem**: A recursive algorithm computes the sum of first n array elements. Prove by induction that the algorithm always returns the correct sum.

**Algorithm**:
```
function recursiveSum(arr, n):
    if n == 0:
        return 0
    else:
        return recursiveSum(arr, n-1) + arr[n-1]
```

**Proof**:

*Base Case*: When n = 0, the algorithm returns 0, which is the sum of zero elements. True.

*Inductive Step*: Assume the function correctly computes the sum of first k elements for some k ≥ 0. For n = k+1:
- recursiveSum(arr, k+1) = recursiveSum(arr, k) + arr[k]
- By inductive hypothesis, recursiveSum(arr, k) equals the sum of first k elements
- Adding arr[k] gives the sum of first (k+1) elements
- Hence, the algorithm is correct for n = k+1

By induction, the algorithm correctly computes the sum for all n ≥ 0.

## Exam Tips

1. **Identify the Statement Clearly**: Before attempting an induction proof, clearly identify P(n) and the domain (typically n ≥ 1 or n ≥ 0).

2. **Always State Base Case(s) Explicitly**: Examiners expect to see the base case proved separately, often as "Step 1: Base Case" or "For n = 1".

3. **State the Inductive Hypothesis Precisely**: Write "Assume P(k) is true for some arbitrary k ≥ 1" before proceeding to prove P(k+1).

4. **Choose Between Weak and Strong Induction**: Use weak induction when P(k+1) depends only on P(k). Use strong induction when it depends on multiple previous cases (like divisibility proofs or recurrence relations).

5. **Manipulate the Inductive Hypothesis Strategically**: Start with the left side of what you're trying to prove and work toward the right side, using the inductive hypothesis along the way.

6. **Strong Induction May Require Multiple Base Cases**: When using strong induction, ensure all base cases (usually P(1), P(2), ..., P(m)) are explicitly proven.

7. **Connect to CS Applications**: In exams, connect induction to algorithm correctness, recursive function verification, and data structure properties—this demonstrates deeper understanding.

8. **Watch for Off-by-One Errors**: Be careful with indices (arr[k] vs arr[k-1]) and the range of n in your proof.

9. **Practice Common Sum Formulas**: Be prepared to prove formulas for geometric series, sum of squares, cubes, etc.

10. **Use Strong Induction for Number Theory**: Problems involving divisors, prime numbers, or the Fundamental Theorem of Arithmetic typically require strong induction.