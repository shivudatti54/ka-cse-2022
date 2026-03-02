# Recurrence Relations

## Introduction

Recurrence relations are fundamental mathematical tools used to define sequences where each term is expressed as a function of its preceding terms. In computer science, recurrence relations play a critical role in analyzing the time and space complexity of recursive algorithms. When you study divide-and-conquer algorithms like binary search, merge sort, or quick sort, the running time is naturally expressed as a recurrence relation. Understanding how to solve these relations is essential for any computer scientist, particularly for students at the University of Delhi where algorithm analysis forms a core component of the curriculum.

The study of recurrence relations extends beyond algorithm analysis into various domains including combinatorial counting, number theory, and formal language theory. In this chapter, we will explore the fundamental concepts of recurrence relations, learn different methods to solve them, and understand their practical applications in computer science. The ability to solve recurrence relations is a skill that will serve you throughout your career, whether you're analyzing algorithms, designing data structures, or pursuing advanced studies in theoretical computer science.

## Key Concepts

### Definition and Basic Terminology

A recurrence relation is an equation that defines a sequence recursively, expressing the nth term as a function of one or more preceding terms. Formally, a recurrence relation for a sequence {aₙ} is an equation of the form:

aₙ = f(aₙ₋₁, aₙ₋₂, ..., aₙ₋ₖ)

where k is the order of the recurrence relation and f is some function. To completely define a sequence, we also need k initial conditions (base cases): a₀, a₁, ..., aₖ₋₁.

For example, the Fibonacci sequence is defined by the recurrence relation:
Fₙ = Fₙ₋₁ + Fₙ₋₂, with initial conditions F₀ = 0, F₁ = 1

This is a second-order linear homogeneous recurrence relation with constant coefficients.

### Types of Recurrence Relations

**Linear vs Non-linear**: A linear recurrence relation has each term expressed as a linear combination of previous terms. The general form is:

aₙ = c₁aₙ₋₁ + c₂aₙ₋₂ + ... + cₖaₙ₋ₖ + f(n)

where c₁, c₂, ..., cₖ are constants. If f(n) = 0, it is homogeneous; otherwise, it is non-homogeneous. Non-linear recurrences involve products, powers, or other non-linear functions of previous terms, such as aₙ = aₙ₋₁² + 1.

**Order**: The order of a recurrence relation is the number of preceding terms needed to compute the next term. In aₙ = aₙ₋₁ + 2aₙ₋₂, the order is 2.

**Constant Coefficients**: When the coefficients multiplying previous terms are constants, we have a recurrence with constant coefficients. The Fibonacci recurrence has constant coefficients, while aₙ = naₙ₋₁ does not.

### Solving Linear Recurrence Relations with Constant Coefficients

**Homogeneous Case**: For a homogeneous linear recurrence with constant coefficients:

aₙ = c₁aₙ₋₁ + c₂aₙ₋₂ + ... + cₖaₙ₋ₖ

We solve it using the characteristic equation approach:

rᵏ - c₁rᵏ⁻¹ - c₂rᵏ⁻² - ... - cₖ = 0

If the characteristic equation has k distinct roots r₁, r₂, ..., rₖ, the general solution is:
aₙ = A₁r₁ⁿ + A₂r₂ⁿ + ... + Aₖrᵏⁿ

If there are repeated roots, say r₁ with multiplicity m, the solution includes terms of the form (A₁ + A₂n + A₃n² + ... + Aₘnᵐ⁻¹)r₁ⁿ.

**Non-homogeneous Case**: For non-homogeneous recurrences:
aₙ = c₁aₙ₋₁ + c₂aₙ₋₂ + ... + cₖaₙ₋ₖ + f(n)

The general solution is aₙ = aₙ^(h) + aₙ^(p), where aₙ^(h) is the homogeneous solution and aₙ^(p) is a particular solution. The form of the particular solution depends on f(n). Common cases include:

- If f(n) is a polynomial of degree d, try a polynomial of degree d
- If f(n) = c·bⁿ, try a solution of the form A·bⁿ (if b is not a root of the characteristic equation)
- If f(n) = c·bⁿ and b is a root of multiplicity m, try nᵐ·A·bⁿ

### Methods for Solving Recurrences

**Iteration Method (Forward Substitution)**: Expand the recurrence repeatedly until you identify a pattern.

Example: aₙ = 2aₙ₋₁ + 1, with a₀ = 1
a₁ = 2a₀ + 1 = 2(1) + 1 = 3
a₂ = 2a₁ + 1 = 2(3) + 1 = 7
a₃ = 2a₂ + 1 = 2(7) + 1 = 15

Pattern emerges: aₙ = 2ⁿ⁺¹ - 1 (proved by induction)

**Master Theorem**: A fundamental result for divide-and-conquer recurrences of the form T(n) = aT(n/b) + f(n), where a ≥ 1, b > 1:

- If f(n) = O(n^logₐᵇ - ε), then T(n) = Θ(n^logₐᵇ)
- If f(n) = Θ(n^logₐᵇ), then T(n) = Θ(n^logₐᵇ log n)
- If f(n) = Ω(n^logₐᵇ + ε), then T(n) = Θ(f(n))

This theorem directly gives us the time complexity of algorithms like merge sort (T(n) = 2T(n/2) + Θ(n), resulting in Θ(n log n)).

## Examples

### Example 1: Solving a Homogeneous Recurrence

Solve: aₙ = 5aₙ₋₁ - 6aₙ₋₂, with a₀ = 1, a₁ = 4

**Solution**:

Step 1: Write the characteristic equation
r² - 5r + 6 = 0

Step 2: Factor the characteristic equation
(r - 2)(r - 3) = 0
r₁ = 2, r₂ = 3

Step 3: Write the general solution
aₙ = A₁(2)ⁿ + A₂(3)ⁿ

Step 4: Use initial conditions to find constants
For n = 0: a₀ = A₁ + A₂ = 1
For n = 1: a₁ = 2A₁ + 3A₂ = 4

Solving:
A₁ + A₂ = 1 → A₁ = 1 - A₂
2(1 - A₂) + 3A₂ = 4
2 - 2A₂ + 3A₂ = 4
2 + A₂ = 4
A₂ = 2, A₁ = -1

Step 5: Final answer
aₙ = -1(2)ⁿ + 2(3)ⁿ = 2·3ⁿ - 2ⁿ

### Example 2: Solving a Non-homogeneous Recurrence

Solve: aₙ = 3aₙ₋₁ + 2ⁿ, with a₀ = 1

**Solution**:

Step 1: Solve the homogeneous part
aₙ^(h) = 3aₙ₋₁ → characteristic r - 3 = 0 → r = 3
aₙ^(h) = A·3ⁿ

Step 2: Find a particular solution
Since f(n) = 2ⁿ, and 2 is not a root of the characteristic equation, try aₙ^(p) = B·2ⁿ

Substituting: B·2ⁿ = 3B·2ⁿ⁻¹ + 2ⁿ
B·2ⁿ = (3B/2)·2ⁿ + 2ⁿ
B = 3B/2 + 1
2B = 3B + 2
-B = 2
B = -2

So aₙ^(p) = -2·2ⁿ

Step 3: General solution
aₙ = A·3ⁿ - 2·2ⁿ

Step 4: Use initial condition a₀ = 1
1 = A - 2(1) = A - 2
A = 3

Step 5: Final answer
aₙ = 3·3ⁿ - 2·2ⁿ = 3ⁿ⁺¹ - 2ⁿ⁺¹

### Example 3: Application - Binary Search Time Complexity

The time complexity of binary search is given by:
T(n) = T(n/2) + Θ(1), with T(1) = Θ(1)

Using Master Theorem:
a = 1, b = 2, f(n) = Θ(1) = n⁰
logₐᵇ = log₂(1) = 0

Since f(n) = Θ(n⁰) = Θ(n^logₐᵇ), we have:
T(n) = Θ(n^logₐᵇ log n) = Θ(log n)

## Exam Tips

1. **Identify the type correctly**: Always determine whether the recurrence is linear/non-linear, homogeneous/non-homogeneous, and with/without constant coefficients before choosing your solution method.

2. **Master the characteristic equation method**: This is the most important technique for solving linear recurrences with constant coefficients. Practice forming and solving characteristic equations until it becomes automatic.

3. **Remember the Master Theorem**: For algorithm analysis questions, the Master Theorem is often the fastest way to find time complexity. Memorize its three cases precisely.

4. **Check your particular solution form**: When solving non-homogeneous recurrences, ensure your guess for the particular solution doesn't overlap with the homogeneous solution. Use the "multiplication by nᵏ" rule when there's overlap.

5. **Verify with base cases**: Always substitute your solution back into the recurrence and check initial conditions to verify correctness.

6. **Iteration for simple recurrences**: For first-order recurrences like aₙ = caₙ₋₁ + d, the iteration method often gives quick results. Look for geometric or arithmetic patterns.

7. **Practice with algorithm examples**: Connect recurrence solving with algorithm analysis. Know the recurrences for binary search, merge sort, and quick search to quickly identify patterns.

8. **Don't forget constant coefficients**: The Master Theorem and characteristic equation method only apply to recurrences with constant coefficients. For variable coefficients, other methods are needed.