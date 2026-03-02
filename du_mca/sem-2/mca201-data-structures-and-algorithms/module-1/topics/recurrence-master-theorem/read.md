# Recurrence Relations and Master Theorem

## Introduction

Recurrence relations are fundamental mathematical tools used to analyze the time and space complexity of recursive algorithms. When an algorithm calls itself with smaller inputs, its running time can be expressed as a function of the running time on smaller problem sizes, plus the overhead of the recursive calls. This chapter explores how to formulate and solve such recurrence relations, with particular emphasis on the Master Theorem—a powerful tool that provides asymptotic bounds for recurrences of the form T(n) = aT(n/b) + f(n).

In the context of the University of Delhi MCA program, mastering recurrence relations and the Master Theorem is essential for analyzing divide-and-conquer algorithms, which form the backbone of many efficient computational solutions. Whether analyzing merge sort, binary search, or Strassen's matrix multiplication, the ability to determine time complexity through recurrence solving is a critical skill expected in both internal assessments and end-semester examinations.

## Key Concepts

### 1. Recurrence Relation Basics

A recurrence relation defines a sequence recursively—each term is defined in terms of previous terms. In algorithm analysis, we use recurrences to express the running time T(n) of an algorithm in terms of its running time on smaller inputs.

**Standard Form:** T(n) = T(n-1) + O(1) represents algorithms that reduce problem size by 1 each step (like linear search).

**Divide-and-Conquer Form:** T(n) = aT(n/b) + f(n), where:
- 'a' is the number of recursive subproblems
- 'n/b' is the size of each subproblem
- f(n) is the cost of dividing the problem and combining results

### 2. Methods for Solving Recurences

**Substitution Method:** Guess the form of the solution and verify by induction. This method is flexible but requires an inspired guess.

**Recursion Tree Method:** Expand the recurrence into a tree structure, where each node represents the cost at a particular level of recursion. Summing all levels gives the total cost.

**Master Theorem:** Provides direct asymptotic solutions for recurrences of the form T(n) = aT(n/b) + f(n), where a ≥ 1, b > 1, and f(n) is asymptotically positive.

### 3. Master Theorem Statement

Let a ≥ 1 and b > 1 be constants, and let f(n) be a function. Then the recurrence T(n) = aT(n/b) + f(n) has the following asymptotic bounds:

**Case 1 (Polynomial Difference):** If f(n) = O(n^log_b(a-ε)) for some constant ε > 0, then T(n) = Θ(n^log_b(a)).

**Case 2 (Balanced):** If f(n) = Θ(n^log_b(a) * log^k(n)) for some constant k ≥ 0, then T(n) = Θ(n^log_b(a) * log^(k+1)(n)).

**Case 3 (Polynomial Difference Above):** If f(n) = Ω(n^log_b(a+ε)) for some constant ε > 0, and if a f(n/b) ≤ c f(n) for some constant c < 1 and sufficiently large n, then T(n) = Θ(f(n)).

### 4. Common Recurrence Patterns

| Algorithm | Recurrence | Solution |
|-----------|------------|----------|
| Binary Search | T(n) = T(n/2) + O(1) | O(log n) |
| Merge Sort | T(n) = 2T(n/2) + O(n) | O(n log n) |
| Quick Sort (average) | T(n) = 2T(n/2) + O(n) | O(n log n) |
| Strassen's Matrix | T(n) = 7T(n/2) + O(n^2) | O(n^log_2(7)) ≈ O(n^2.81) |

## Examples

### Example 1: Binary Search Analysis

**Problem:** Solve the recurrence T(n) = T(n/2) + 1, with T(1) = O(1).

**Solution:**
- Here, a = 1, b = 2, f(n) = 1
- n^log_b(a) = n^log_2(1) = n^0 = 1
- f(n) = Θ(1) = Θ(n^log_b(a))

This is Case 2 of the Master Theorem with k = 0.
- T(n) = Θ(n^log_b(a) * log^(k+1)(n)) = Θ(1 * log(n)) = Θ(log n)

**Verification by Substitution:**
T(n) = T(n/2) + 1
= T(n/4) + 1 + 1 = T(n/4) + 2
= T(n/8) + 3 = ... = T(n/2^k) + k

When n/2^k = 1, we have k = log_2(n)
Thus, T(n) = T(1) + log_2(n) = Θ(log n)

### Example 2: Merge Sort Analysis

**Problem:** Solve T(n) = 2T(n/2) + n, with T(1) = O(1).

**Solution:**
- a = 2, b = 2, f(n) = n
- n^log_b(a) = n^log_2(2) = n^1 = n
- f(n) = Θ(n) matches n^log_b(a)

This is Case 2 of Master Theorem with k = 0.
- T(n) = Θ(n^log_b(a) * log^(k+1)(n)) = Θ(n * log n)

**Recursion Tree Verification:**
Level 0: n
Level 1: 2 × (n/2) = n
Level 2: 4 × (n/4) = n
...
Level log(n): n × 1 = n

Total = n × (log n + 1) = Θ(n log n)

### Example 3: Applying Master Theorem

**Problem:** Determine the asymptotic complexity of T(n) = 3T(n/4) + n^2.

**Solution:**
- a = 3, b = 4
- n^log_b(a) = n^log_4(3) = n^(0.792...)
- f(n) = n^2

Compare f(n) with n^log_b(a):
- n^2 vs n^0.792
- f(n) = Ω(n^log_b(a+ε)) where ε ≈ 1.208

This is Case 3. Check regularity condition:
- a f(n/b) = 3 × (n/4)^2 = 3n^2/16 = (3/16) f(n)
- c = 3/16 < 1, condition satisfied

Therefore, T(n) = Θ(f(n)) = Θ(n^2)

## Exam Tips

1. **Identify a, b, and f(n) correctly:** The first step in applying Master Theorem is correctly identifying the number of subproblems (a), the factor by which problem size reduces (b), and the combining cost (f(n)).

2. **Compare exponents carefully:** Calculate n^log_b(a) and compare with f(n). The comparison is polynomial, not just asymptotic—look for polynomial differences (n^ε for some ε > 0).

3. **Remember Case 2 has three sub-cases:** k < 0, k = 0, and k > 0 all yield different results. The extra log factor depends on whether k = 0 or k > 0.

4. **Check regularity condition for Case 3:** Always verify that a f(n/b) ≤ c f(n) for some c < 1 before applying Case 3.

5. **Use substitution for non-standard forms:** Master Theorem only applies to T(n) = aT(n/b) + f(n). For other forms, use substitution or recursion tree methods.

6. **Practice with common recurrences:** Be familiar with standard patterns—merge sort (n log n), binary search (log n), Strassen's (n^2.81).

7. **Don't forget the base case:** While Master Theorem gives asymptotic complexity, remember that the recurrence needs a base case for complete specification.