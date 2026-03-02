# Recurrence Relations and Master Theorem

## Introduction

Recurrence relations are fundamental mathematical tools used to describe the running time of recursive algorithms. When analyzing algorithms that divide a problem into smaller subproblems (such as Merge Sort, Binary Search, and Quick Sort), the running time is often expressed in terms of the time taken to solve smaller instances of the same problem plus the overhead of dividing and combining results. This creates a recursive definition of time complexity, known as a recurrence relation.

Understanding how to solve recurrence relations is essential for any computer science student, as it forms the backbone of algorithm analysis. The Master Theorem provides a powerful, general-purpose technique for solving a wide class of divide-and-conquer recurrences in a systematic manner. This theorem, attributed to computer science pioneers like Jon Bentley, has become one of the most frequently used tools in algorithm design and analysis. For students preparing for DU semester examinations, mastery of recurrence solving techniques and the Master Theorem is absolutely critical, as questions on this topic appear consistently in the End Semester Examination.

## Key Concepts

### Recurrence Relations: Definition and Types

A recurrence relation is an equation that defines a sequence recursively—each term is defined in terms of previous terms. In algorithm analysis, we typically express the running time T(n) of an algorithm in terms of T of smaller inputs.

**Basic structure of divide-and-conquer recurrences:**
- T(n) = aT(n/b) + f(n), where:
  - a ≥ 1 (number of subproblems)
  - b > 1 (factor by which problem size shrinks)
  - f(n) (cost of dividing and combining)

**Types of Recurrence Relations:**

1. **Homogeneous Linear Recurrences:** All terms are multiples of previous terms (e.g., T(n) = 2T(n-1))
2. **Inhomogeneous Linear Recurrences:** Include a non-recursive term (e.g., T(n) = 2T(n-1) + n)
3. **Divide-and-Conquer Recurrences:** The classic form T(n) = aT(n/b) + f(n)

### Methods for Solving Recurrences

**1. Substitution Method (Guess and Verify)**

This method involves guessing the form of the answer and then proving it correct by induction.

Steps:
- Make a guess about the solution form
- Assume the solution holds for smaller inputs
- Substitute into the recurrence
- Verify with mathematical induction

**2. Iteration Method (Unrolling)**

We expand the recurrence repeatedly until we can identify a pattern.

For T(n) = 2T(n/2) + n:
- T(n) = 2[2T(n/4) + n/2] + n = 4T(n/4) + 2n
- Continue expanding until we reach the base case

**3. Recursion Tree Method**

Each node represents the cost at a particular level of recursion. The total cost is the sum of costs at all levels.

### The Master Theorem

The Master Theorem provides a direct solution for recurrences of the form:

**T(n) = aT(n/b) + f(n)**

where a ≥ 1, b > 1, and f(n) is asymptotically positive.

Let ε > 0 be a constant. Then three cases exist:

**Case 1 (Polynomial Difference - f(n) is smaller):**
If f(n) = O(n^(log_b a - ε)), then:
T(n) = Θ(n^(log_b a))

**Case 2 (Balanced case):**
If f(n) = Θ(n^(log_b a) * log^k n) for some k ≥ 0, then:
T(n) = Θ(n^(log_b a) * log^(k+1) n)

**Case 3 (f(n) is larger):**
If f(n) = Ω(n^(log_b a + ε)) and if a·f(n/b) ≤ c·f(n) for some c < 1 and sufficiently large n, then:
T(n) = Θ(f(n))

### Understanding log_b a

The term n^(log_b a) represents the rate at which the problem size shrinks when divided among a subproblems. This is often called the "critical exponent" because it determines which term dominates.

- If a = 1, log_b a = 0, so n^(log_b a) = n^0 = 1
- If a = b, log_b a = 1, so n^(log_b a) = n
- If a = b^k, log_b a = k, so n^(log_b a) = n^k

### Master Theorem Limitations

The Master Theorem cannot handle:
1. Cases where f(n) is not polynomially bounded (e.g., f(n) = n^(log_b a) / log n)
2. Non-polynomial differences between f(n) and n^(log_b a)
3. The case where a is not a constant (though in practice a is typically constant)
4. Recurrences that are not of the form T(n) = aT(n/b) + f(n)

## Examples

### Example 1: Binary Search

Binary Search has the recurrence: T(n) = T(n/2) + O(1)

Here: a = 1, b = 2, f(n) = 1 = Θ(1)

Compute n^(log_b a) = n^(log_2 1) = n^0 = 1

Compare f(n) with n^(log_b a): f(n) = Θ(1) = Θ(n^0 * log^0 n)

This matches **Case 2** with k = 0.

Therefore: T(n) = Θ(n^(log_b a) * log^(k+1) n) = Θ(1 * log^1 n) = **Θ(log n)**

### Example 2: Merge Sort

Merge Sort has the recurrence: T(n) = 2T(n/2) + Θ(n)

Here: a = 2, b = 2, f(n) = n

Compute n^(log_b a) = n^(log_2 2) = n^1 = n

Compare: f(n) = n vs n^(log_b a) = n

We have f(n) = Θ(n^(log_b a) * log^0 n), so k = 0

This matches **Case 2** with k = 0.

Therefore: T(n) = Θ(n^(log_b a) * log^(k+1) n) = Θ(n * log n)

Thus, Merge Sort runs in **Θ(n log n)** time.

### Example 3: Strassen's Matrix Multiplication

Strassen's algorithm has the recurrence: T(n) = 7T(n/2) + Θ(n^2)

Here: a = 7, b = 2, f(n) = n^2

Compute n^(log_b a) = n^(log_2 7) ≈ n^2.807

Compare: f(n) = n^2 = O(n^(log_2 7 - ε)) where ε ≈ 0.807

This matches **Case 1** (f(n) is polynomially smaller).

Therefore: T(n) = Θ(n^(log_2 7)) ≈ **Θ(n^2.807)**

This is faster than the naive Θ(n³) matrix multiplication.

### Example 4: Using Substitution Method

Solve T(n) = 2T(n/2) + n by substitution.

**Guess:** T(n) = O(n log n)

**Inductive Hypothesis:** Assume T(m) ≤ c·m log m for all m < n

**Proof:**
T(n) = 2T(n/2) + n
≤ 2·c·(n/2)·log(n/2) + n
= c·n·[log n - log 2] + n
= c·n·log n - c·n + n
= c·n·log n - (c-1)·n

For this to be ≤ c·n·log n, we need -(c-1) ≤ 0, which is true for c ≥ 1.

Base case: T(1) = O(1), which holds for appropriate c.

**Therefore: T(n) = O(n log n)**

## Exam Tips

1. **Always identify a, b, and f(n) first** - This is the crucial first step for applying Master Theorem correctly in any exam question.

2. **Calculate log_b a carefully** - Students often make errors here. Remember: log_b a means "the exponent to which b must be raised to get a."

3. **Master Theorem Case 2 requires careful attention** - The f(n) = Θ(n^(log_b a) * log^k n) form appears frequently in exams, especially with k = 0 (balanced case like Merge Sort).

4. **Know the three cases by heart** - Case 1: f(n) smaller → answer is n^(log_b a); Case 2: equal → answer involves an extra log factor; Case 3: f(n) larger → answer is f(n).

5. **Practice identifying when Master Theorem cannot be applied** - Questions often ask "which case applies" or "can Master Theorem be applied here?"

6. **Don't forget the regularity condition in Case 3** - The condition a·f(n/b) ≤ c·f(n) for some c < 1 is necessary and is often tested in exams.

7. **Substitution method is often tested for verification** - Be prepared to prove your Master Theorem answer using induction.

8. **Recursion trees help visualize the problem** - Drawing even a 2-level recursion tree can help verify your Master Theorem answer during exams.