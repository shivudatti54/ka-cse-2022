# Linear Recurrence Relations with Constant Coefficients

## Introduction

Recurrence relations are fundamental mathematical tools used to define sequences in terms of previous terms. They appear extensively in computer science, particularly in algorithm analysis (computing time complexity of recursive algorithms), combinatorics, number theory, and database theory. Understanding how to solve recurrence relations is essential for analyzing recursive algorithms, predicting system behavior, and modeling real-world phenomena.

A **recurrence relation** defines a sequence {a_n} where each term a_n is expressed as a function of one or more preceding terms. For example, the Fibonacci sequence is defined by a_n = a_{n-1} + a_{n-2} with initial conditions a_0 = 0, a_1 = 1. Linear recurrence relations with constant coefficients form a particularly important class because they have well-established solution methods and numerous practical applications.

In this topic, we will explore how to solve linear recurrence relations with constant coefficients, both homogeneous and non-homogeneous types. These techniques are crucial for the DU Computer Science curriculum and frequently appear in competitive examinations and practical applications.

## Key Concepts

### Definition of Linear Recurrence Relations

A **linear recurrence relation with constant coefficients** is a relation of the form:

**a_n = c_1 a_{n-1} + c_2 a_{n-2} + ... + c_k a_{n-k} + f(n)**

where:
- c_1, c_2, ..., c_k are constants (the constant coefficients)
- k is the order of the recurrence
- f(n) is a function of n (non-homogeneous part)

When f(n) = 0, the recurrence is called **homogeneous**; otherwise, it is **non-homogeneous**.

### Order and Degree

The **order** of a linear recurrence relation is the number of preceding terms required to determine the next term. In the general form above, the order is k. For example:
- Fibonacci: a_n = a_{n-1} + a_{n-2} has order 2
- a_n = 3a_{n-1} - 2a_{n-3} has order 3

### Characteristic Equation Method for Homogeneous Recurrences

For a homogeneous linear recurrence relation:
**a_n = c_1 a_{n-1} + c_2 a_{n-2} + ... + c_k a_{n-k}**

The solution approach involves:

1. **Form the characteristic equation**: Replace a_n with r^n, a_{n-1} with r^{n-1}, etc.:
   r^k = c_1 r^{k-1} + c_2 r^{k-2} + ... + c_k
   
   This simplifies to:
   r^k - c_1 r^{k-1} - c_2 r^{k-2} - ... - c_k = 0

2. **Solve the characteristic equation** to find roots r_1, r_2, ..., r_k

3. **Form the general solution**:
   - If all roots are distinct: a_n = α_1 r_1^n + α_2 r_2^n + ... + α_k r_k^n
   - If roots repeat: For a root r of multiplicity m, include terms (α_0 + α_1 n + α_2 n^2 + ... + α_{m-1} n^{m-1})r^n

4. **Use initial conditions** to find the constants α_1, α_2, ..., α_k

### Solving Non-Homogeneous Recurrence Relations

For non-homogeneous recurrences: **a_n = c_1 a_{n-1} + ... + c_k a_{n-k} + f(n)**

The solution has two parts:
**a_n = a_n^(h) + a_n^(p)**

where:
- a_n^(h) is the general solution to the homogeneous part
- a_n^(p) is a particular solution to the non-homogeneous recurrence

### Method of Undetermined Coefficients

For finding particular solutions when f(n) is a polynomial, exponential, or trigonometric function, we assume a form similar to f(n) and determine coefficients:

- If f(n) = P(n) (polynomial of degree d), try a particular solution as polynomial of same degree
- If f(n) = c^n (exponential), try a_n^(p) = A·c^n (if c is not a root of characteristic equation)
- If c is a root of multiplicity m, multiply by n^m

### Method of Variation of Parameters

An alternative method where we replace constants in the homogeneous solution with functions:
- If homogeneous solution is a_n^(h) = α_1 r_1^n + α_2 r_2^n
- Try particular solution: a_n^(p) = u_1(n)r_1^n + u_2(n)r_2^n

This method is more general but computationally complex.

## Examples

### Example 1: Solving a Homogeneous Recurrence

**Solve: a_n = 3a_{n-1} - 2a_{n-2}, with a_0 = 2, a_1 = 3**

**Step 1: Form characteristic equation**
r^2 - 3r + 2 = 0

**Step 2: Solve characteristic equation**
(r - 1)(r - 2) = 0
r_1 = 1, r_2 = 2

**Step 3: General solution**
a_n = α_1(1)^n + α_2(2)^n = α_1 + α_2(2)^n

**Step 4: Use initial conditions**
For n = 0: a_0 = α_1 + α_2 = 2
For n = 1: a_1 = α_1 + 2α_2 = 3

Solving:
α_1 + α_2 = 2
α_1 + 2α_2 = 3
Subtracting: α_2 = 1, then α_1 = 1

**Solution: a_n = 1 + 2^n**

### Example 2: Repeated Roots

**Solve: a_n = 4a_{n-1} - 4a_{n-2}, with a_0 = 1, a_1 = 3**

**Step 1: Characteristic equation**
r^2 - 4r + 4 = 0
(r - 2)^2 = 0

Root r = 2 with multiplicity m = 2

**Step 2: General solution**
Since we have a repeated root:
a_n = (α_1 + α_2 n) · 2^n

**Step 3: Apply initial conditions**
For n = 0: a_0 = (α_1 + 0)·1 = α_1 = 1
For n = 1: a_1 = (α_1 + α_2)·2 = 3
Substituting α_1 = 1: (1 + α_2)·2 = 3 → 1 + α_2 = 3/2 → α_2 = 1/2

**Solution: a_n = (1 + n/2) · 2^n**

### Example 3: Non-Homogeneous Recurrence

**Solve: a_n = 3a_{n-1} + 2^n, with a_0 = 1**

**Step 1: Solve homogeneous part**
a_n = 3a_{n-1}
Characteristic: r - 3 = 0 → r = 3
Homogeneous solution: a_n^(h) = α·3^n

**Step 2: Find particular solution**
Since f(n) = 2^n (exponential), and 2 is not a root of r - 3 = 0:
Try a_n^(p) = A·2^n

Substitute into recurrence:
A·2^n = 3·A·2^{n-1} + 2^n
A·2^n = (3A/2)·2^n + 2^n
A = 3A/2 + 1
2A = 3A + 2
-A = 2 → A = -2

So a_n^(p) = -2·2^n

**Step 3: General solution**
a_n = α·3^n - 2·2^n

**Step 4: Use initial condition**
a_0 = α - 2 = 1 → α = 3

**Solution: a_n = 3·3^n - 2·2^n = 3^{n+1} - 2^{n+1}**

## Exam Tips

1. **Identify the order correctly**: The order equals the maximum subscript difference. For a_n = 5a_{n-1} + 3a_{n-3}, the order is 3.

2. **Always form the characteristic equation first**: For homogeneous recurrences, this is your primary tool. Practice writing r^n for each term.

3. **Check for repeated roots**: If the characteristic equation has repeated roots, multiply the corresponding terms by increasing powers of n.

4. **Particular solution form selection**: Choose the correct trial solution based on f(n). If f(n) is a polynomial of degree d, try a polynomial of degree d. If f(n) involves a term that is a solution to the homogeneous part, multiply by n.

5. **Verify your solution**: Always substitute your solution back into the original recurrence to verify correctness. This catches calculation errors.

6. **Initial conditions are essential**: You cannot find a unique solution without initial conditions. The number of initial conditions needed equals the order of the recurrence.

7. **Practice common patterns**: Familiarize yourself with solving Fibonacci-like recurrences, geometric progressions defined recursively, and polynomial-gro

8. **Time complexity applications**: Understand how to convert recursive algorithm analysis (like merge sort: T(n) = 2T(n/2) + n) into closed-form solutions.

9. **Avoid common errors**: Do not forget to multiply by n^m when the trial solution overlaps with homogeneous solutions. Always solve the homogeneous part first.

10. **State-space diagrams**: For recurrence relations modeling real systems, remember that different initial conditions can produce different solution "paths" in the state space.