# Recurrence Relations

## Introduction

Recurrence relations are fundamental mathematical tools that define sequences recursively, where each term is expressed in terms of previous terms. Unlike explicit formulas that directly compute any term, recurrence relations establish relationships between consecutive terms, making them particularly powerful for modeling problems where the future state depends on previous states. This concept permeates computer science, appearing in algorithm analysis, data structures, combinatorial counting, and various computational processes.

In the context of the University of Delhi MCA program, recurrence relations form an essential component of discrete mathematics, with direct applications in analyzing recursive algorithms, computing time and space complexities, and solving counting problems. The ability to formulate and solve recurrence relations is a critical skill for any computer scientist, as recursive algorithms are ubiquitous in software development. From the classic Fibonacci sequence to the analysis of divide-and-conquer algorithms, recurrence relations provide the mathematical framework for understanding how systems evolve over time or how problems can be broken down into smaller subproblems.

This topic covers the formation of recurrence relations from problem statements, methods for solving them (including iteration, substitution, and characteristic root methods), and their practical applications in computer science. The examination pattern at DU emphasizes both theoretical understanding and problem-solving capabilities, making it essential to master these techniques thoroughly.

## Key Concepts

### Definition and Basic Terminology

A recurrence relation is an equation that defines a sequence {aₙ} where each term aₙ (for n ≥ n₀) is expressed as a function of one or more preceding terms. The smallest index n₀ for which the relation is defined is called the initial condition or boundary condition. Together, the recurrence relation and its initial conditions completely determine the sequence.

The **order** of a recurrence relation is the difference between the largest and smallest indices appearing in the relation. For example, aₙ = aₙ₋₁ + 2aₙ₋₂ is a second-order recurrence relation because the largest index is n and the smallest is n-2, giving an order of 2.

### Linear Recurrence Relations

A recurrence relation is **linear** if it can be expressed as a linear combination of previous terms, where each term is multiplied by a coefficient (which may depend on n) but never raised to a power or multiplied by other sequence terms. The general form is:

aₙ = c₁(n)aₙ₋₁ + c₂(n)aₙ₋₂ + ... + cₖ(n)aₙ₋ₖ + f(n)

Where c₁(n), c₂(n), ..., cₖ(n) are coefficient functions and f(n) is a function of n. When f(n) = 0, the relation is **homogeneous**; otherwise, it is **non-homogeneous** or **non-homogeneous**.

### Characteristic Equation Method

For linear homogeneous recurrence relations with constant coefficients, the characteristic equation provides a systematic solution approach. Consider the recurrence relation:

aₙ = c₁aₙ₋₁ + c₂aₙ₋₂ + ... + cₖaₙ₋ₖ

The characteristic equation is formed by assuming a solution of the form aₙ = rⁿ, giving:

rᵏ - c₁rᵏ⁻¹ - c₂rᵏ⁻² - ... - cₖ = 0

The roots of this polynomial determine the general solution. If r₁, r₂, ..., rₖ are distinct real roots, the general solution is:

aₙ = A₁r₁ⁿ + A₂r₂ⁿ + ... + Aₖrₖⁿ

If roots are repeated, say r₁ has multiplicity m, the corresponding terms become (A₁ + A₂n + A₃n² + ... + Aₘnᵐ⁻¹)r₁ⁿ.

### Solving Non-Homogeneous Recurrence Relations

For non-homogeneous recurrence relations, the general solution is the sum of the homogeneous solution and a particular solution:

aₙ = aₙ⁽ʰ⁾ + aₙ⁽ᵖ⁾

The homogeneous part aₙ⁽ʰ⁾ is solved using the characteristic equation method. The particular solution aₙ⁽ᵖ⁾ depends on the form of f(n) and is typically guessed based on the type of function (constant, polynomial, exponential, etc.).

### Methods for Solving Recurrence Relations

**Iteration Method (Forward Substitution):** This involves expanding the recurrence relation repeatedly until a pattern emerges. For example, starting with aₙ = 2aₙ₋₁ with a₀ = 1, we get a₁ = 2, a₂ = 4, a₃ = 8, leading to the pattern aₙ = 2ⁿ.

**Substitution Method (Backward Substitution):** We express aₙ in terms of aₙ₋₁, then in terms of aₙ₋₂, continuing until we reach the initial condition.

**Master Theorem:** While not a direct solving method, the Master Theorem provides asymptotic solutions for recurrence relations of the form T(n) = aT(n/b) + f(n), which frequently arise in divide-and-conquer algorithm analysis.

## Examples

### Example 1: Solving a Second-Order Homogeneous Recurrence Relation

**Problem:** Solve the recurrence relation aₙ = 5aₙ₋₁ - 6aₙ₋₂ with initial conditions a₀ = 1 and a₁ = 4.

**Solution:**

Step 1: Form the characteristic equation
r² - 5r + 6 = 0

Step 2: Solve the characteristic equation
(r - 2)(r - 3) = 0
r₁ = 2, r₂ = 3 (distinct real roots)

Step 3: Write the general homogeneous solution
aₙ⁽ʰ⁾ = A₁(2)ⁿ + A₂(3)ⁿ

Step 4: Use initial conditions to find constants
For n = 0: a₀ = A₁ + A₂ = 1
For n = 1: a₁ = 2A₁ + 3A₂ = 4

Solving the system:
From first equation: A₁ = 1 - A₂
Substituting: 2(1 - A₂) + 3A₂ = 4
2 - 2A₂ + 3A₂ = 4
2 + A₂ = 4
A₂ = 2, therefore A₁ = -1

Step 5: Write the final solution
aₙ = -1(2)ⁿ + 2(3)ⁿ = 2(3)ⁿ - 2ⁿ

**Verification:** For n = 2: a₂ = 2(9) - 4 = 14, and from recurrence: a₂ = 5(4) - 6(1) = 14 ✓

### Example 2: Solving a Non-Homogeneous Recurrence Relation

**Problem:** Solve aₙ = 3aₙ₋₁ + 2ⁿ with a₀ = 1.

**Solution:**

Step 1: Solve the homogeneous part
aₙ⁽ʰ⁾ = 3aₙ₋₁ ⇒ characteristic: r - 3 = 0 ⇒ r = 3
aₙ⁽ʰ⁾ = A(3)ⁿ

Step 2: Find a particular solution
Since f(n) = 2ⁿ is exponential and 2 is not a root of the homogeneous characteristic equation, we guess aₙ⁽ᵖ⁾ = B(2)ⁿ.

Substituting into the recurrence:
B(2)ⁿ = 3B(2)ⁿ⁻¹ + 2ⁿ
B(2)ⁿ = 3B(2)ⁿ/2 + 2ⁿ
B = 3B/2 + 1
B - 3B/2 = 1
-B/2 = 1
B = -2

So aₙ⁽ᵖ⁾ = -2(2)ⁿ

Step 3: Write general solution
aₙ = A(3)ⁿ - 2(2)ⁿ

Step 4: Use initial condition
For n = 0: a₀ = A - 2 = 1 ⇒ A = 3

Step 5: Final solution
aₙ = 3(3)ⁿ - 2(2)ⁿ

**Verification:** For n = 1: a₁ = 3(3) - 2(2) = 9 - 4 = 5, and from recurrence: a₁ = 3(1) + 2 = 5 ✓

### Example 3: Forming and Solving a Recurrence from Word Problem

**Problem:** A computer virus spreads such that each infected computer infects 2 new computers each day, and 3 computers are newly added to the network daily. If initially 5 computers are infected, find the number of infected computers after n days.

**Solution:**

Step 1: Form the recurrence relation
Each day: existing infected computers multiply by 3 (1 infects 2 new), plus 3 new additions
aₙ = 3aₙ₋₁ + 3, with a₀ = 5

Step 2: Solve the recurrence
Homogeneous part: aₙ⁽ʰ⁾ = 3aₙ₋₁ ⇒ r - 3 = 0 ⇒ r = 3 ⇒ aₙ⁽ʰ⁾ = A(3)ⁿ

Particular solution: Since f(n) = 3 (constant), guess aₙ⁽ᵖ⁾ = B (constant)
B = 3B + 3
B - 3B = 3
-2B = 3
B = -3/2

General solution: aₙ = A(3)ⁿ - 3/2

Step 3: Apply initial condition
a₀ = A - 3/2 = 5 ⇒ A = 5 + 3/2 = 13/2

Step 4: Final answer
aₙ = (13/2)(3)ⁿ - 3/2 = (13·3ⁿ - 3)/2

After n days: aₙ = (13·3ⁿ - 3)/2 computers

## Exam Tips

1. **Identify the order correctly:** Always determine the order of the recurrence relation first—this tells you how many initial conditions you need and the degree of the characteristic polynomial.

2. **Check for homogeneity:** Determine whether the recurrence is homogeneous (f(n) = 0) or non-homogeneous before choosing your solving approach.

3. **Characteristic equation for constant coefficients:** For linear recurrences with constant coefficients, the characteristic equation method is most efficient. Remember to handle distinct roots, repeated roots, and complex roots appropriately.

4. **Particular solution guess table:** For non-homogeneous recurrences, memorize the standard guess forms: constant for constant f(n), polynomial of degree d for polynomial f(n), and exponential form for exponential f(n). If the guess overlaps with the homogeneous solution, multiply by n.

5. **Verify your solution:** Always substitute back into the original recurrence and check initial conditions—this catches algebraic mistakes and ensures your solution is correct.

6. **Iteration for simple cases:** For first-order recurrences like aₙ = caₙ₋₁ + d, iteration often yields quick results: aₙ = cⁿa₀ + d(cⁿ - 1)/(c - 1) for c ≠ 1.

7. **Algorithm analysis applications:** Understand how recurrence relations arise in algorithm analysis, particularly for recursive algorithms. Be familiar with the form T(n) = aT(n/b) + f(n) and basic cases of the Master Theorem.