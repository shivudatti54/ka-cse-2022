# Second Order Linear Homogeneous Recurrence Relation with Constant Coefficients

## Table of Contents

- [Second Order Linear Homogeneous Recurrence Relation with Constant Coefficients](#second-order-linear-homogeneous-recurrence-relation-with-constant-coefficients)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Definition and Standard Form](#definition-and-standard-form)
  - [Characteristic Equation](#characteristic-equation)
  - [Three Cases for Characteristic Roots](#three-cases-for-characteristic-roots)
  - [Method of Solving](#method-of-solving)
- [Examples](#examples)
  - [Example 1: Distinct Real Roots](#example-1-distinct-real-roots)
  - [Example 2: Repeated Real Roots](#example-2-repeated-real-roots)
  - [Example 3: Complex Roots](#example-3-complex-roots)
- [Exam Tips](#exam-tips)

## Introduction

Recurrence relations are fundamental mathematical tools used to describe sequences where each term is defined in terms of previous terms. In computer science, they play a crucial role in analyzing algorithms, particularly in determining time and space complexity. The second order linear homogeneous recurrence relation with constant coefficients represents one of the most important classes of recurrence relations, serving as the foundation for solving more complex recurrence relations encountered in algorithm analysis, combinatorics, and various engineering applications.

A recurrence relation of order 2 has the general form: aₙ = c₁aₙ₋₁ + c₂aₙ₋₂, where c₁ and c₂ are constants, and c₂ ≠ 0. When the relation equals zero (homogeneous), it becomes aₙ - c₁aₙ₋₁ - c₂aₙ₋₂ = 0. These relations appear frequently in real-world scenarios such as population growth models, financial calculations (compound interest), Fibonacci sequences, and analyzing recursive algorithm running times.

Understanding how to solve these recurrence relations is essential for any computer science student, as they provide the mathematical foundation for analyzing divide-and-conquer algorithms, recursive data structures, and many other computational problems.

## Key Concepts

### Definition and Standard Form

A second order linear homogeneous recurrence relation with constant coefficients is defined as:

**aₙ = c₁aₙ₋₁ + c₂aₙ₋₂** for n ≥ 2

where:

- aₙ represents the nth term of the sequence
- c₁ and c₂ are constants (coefficients)
- c₂ ≠ 0 (to maintain second order)
- Initial conditions a₀ and a₁ (or a₁ and a₂) must be given to uniquely determine the sequence

The relation is called "linear" because each term appears to the first power and there are no products of terms. It is "homogeneous" because all terms involve aₙ or its previous values (no constant term or function of n). It has "constant coefficients" because c₁ and c₂ are constants, not functions of n.

### Characteristic Equation

The key to solving second order linear homogeneous recurrence relations lies in the characteristic equation. To find this equation, we assume a solution of the form aₙ = rⁿ, where r is a constant to be determined.

Substituting aₙ = rⁿ into the recurrence relation:
rⁿ = c₁rⁿ⁻¹ + c₂rⁿ⁻²

Dividing both sides by rⁿ⁻² (assuming r ≠ 0):
r² = c₁r + c₂

Rearranging to standard form:
r² - c₁r - c₂ = 0

This quadratic equation is called the **characteristic equation** of the recurrence relation. The roots of this equation determine the form of the general solution.

### Three Cases for Characteristic Roots

The solution depends on the nature of the roots of the characteristic equation:

**Case 1: Distinct Real Roots (r₁ ≠ r₂)**
When the characteristic equation has two distinct real roots r₁ and r₂, the general solution is:
aₙ = A(r₁)ⁿ + B(r₂)ⁿ

where A and B are constants determined by the initial conditions.

**Case 2: Repeated Real Roots (r₁ = r₂ = r)**
When the characteristic equation has a repeated real root r (discriminant = 0), the general solution is:
aₙ = (A + Bn)rⁿ

The presence of the n factor accounts for the multiplicity of the root.

**Case 3: Complex Roots (r = α ± iβ)**
When the discriminant is negative, the roots are complex conjugates. Using Euler's formula, the solution can be written in trigonometric form:
aₙ = rⁿ(A cos(nθ) + B sin(nθ))

where r = √(α² + β²) and θ = arctan(β/α)

### Method of Solving

The systematic approach to solve second order linear homogeneous recurrence relations involves:

1. Write the recurrence relation in standard form: aₙ - c₁aₙ₋₁ - c₂aₙ₋₂ = 0
2. Form the characteristic equation: r² - c₁r - c₂ = 0
3. Find the roots of the characteristic equation
4. Based on the nature of roots, write the general solution form
5. Use the given initial conditions to find the constants A and B
6. Write the particular solution by substituting the values of A and B

## Examples

### Example 1: Distinct Real Roots

**Problem:** Solve the recurrence relation aₙ = 3aₙ₋₁ - 2aₙ₋₂ with initial conditions a₀ = 2, a₁ = 3.

**Solution:**

**Step 1:** Write in standard form
aₙ - 3aₙ₋₁ + 2aₙ₋₂ = 0

**Step 2:** Form characteristic equation
r² - 3r + 2 = 0

**Step 3:** Find roots
(r - 1)(r - 2) = 0
r₁ = 1, r₂ = 2 (distinct real roots)

**Step 4:** Write general solution
aₙ = A(1)ⁿ + B(2)ⁿ = A + B(2)ⁿ

**Step 5:** Use initial conditions
For n = 0: a₀ = A + B = 2
For n = 1: a₁ = A + 2B = 3

Solving: A + B = 2, A + 2B = 3
Subtracting: B = 1, therefore A = 1

**Step 6:** Particular solution
aₙ = 1 + 2ⁿ

Verification: a₂ = 1 + 4 = 5, and from recurrence: a₂ = 3(3) - 2(2) = 9 - 4 = 5 ✓

### Example 2: Repeated Real Roots

**Problem:** Solve the recurrence relation aₙ = 4aₙ₋₁ - 4aₙ₋₂ with initial conditions a₀ = 1, a₁ = 4.

**Solution:**

**Step 1:** Standard form
aₙ - 4aₙ₋₁ + 4aₙ₋₂ = 0

**Step 2:** Characteristic equation
r² - 4r + 4 = 0

**Step 3:** Find roots
(r - 2)² = 0
r₁ = r₂ = 2 (repeated root)

**Step 4:** General solution (for repeated root)
aₙ = (A + Bn)2ⁿ

**Step 5:** Apply initial conditions
For n = 0: a₀ = (A + 0) = 1 ⇒ A = 1
For n = 1: a₁ = (A + B)2 = 4 ⇒ 2(A + B) = 4 ⇒ A + B = 2 ⇒ 1 + B = 2 ⇒ B = 1

**Step 6:** Particular solution
aₙ = (1 + n)2ⁿ

Verification: a₂ = (1 + 2)4 = 12, and from recurrence: a₂ = 4(4) - 4(1) = 16 - 4 = 12 ✓

### Example 3: Complex Roots

**Problem:** Solve the recurrence relation aₙ = 2aₙ₋₁ - 2aₙ₋₂ with initial conditions a₀ = 2, a₁ = 2.

**Solution:**

**Step 1:** Standard form
aₙ - 2aₙ₋₁ + 2aₙ₋₂ = 0

**Step 2:** Characteristic equation
r² - 2r + 2 = 0

**Step 3:** Find roots
Using quadratic formula: r = [2 ± √(4 - 8)]/2 = [2 ± √(-4)]/2 = 1 ± i
So r = 1 ± i (complex conjugates)

**Step 4:** Convert to polar form
r = √(1² + 1²) = √2
θ = arctan(1/1) = π/4

**Step 5:** General solution for complex roots
aₙ = (√2)ⁿ(A cos(nπ/4) + B sin(nπ/4))

**Step 6:** Apply initial conditions
For n = 0: a₀ = A = 2 ⇒ A = 2
For n = 1: a₁ = √2(2 cos(π/4) + B sin(π/4)) = √2(2(√2/2) + B(√2/2)) = √2(√2 + B√2/2) = 2 + B
Given a₁ = 2, so 2 + B = 2 ⇒ B = 0

**Step 7:** Particular solution
aₙ = 2(√2)ⁿ cos(nπ/4)

## Exam Tips

1. **Always write the characteristic equation correctly**: Remember to bring all terms to one side. For aₙ = c₁aₙ₋₁ + c₂aₙ₋₂, the characteristic equation is r² - c₁r - c₂ = 0.

2. **Identify the case first**: Before solving, determine whether you have distinct real roots, repeated roots, or complex roots. This determines the solution form.

3. **Use the correct solution form for repeated roots**: Don't forget the 'n' factor. The solution is (A + Bn)rⁿ, not just A(r₁)ⁿ + B(r₂)ⁿ.

4. **Practice converting complex roots to trigonometric form**: Remember to use r = √(α² + β²) and θ = arctan(β/α).

5. **Always verify with initial conditions**: The constants A and B must be determined using the given initial conditions.

6. **For homogeneous relations, there is no particular term**: Remember that homogeneous means the right-hand side equals zero, so there's no f(n) term to handle.

7. **Check your solution**: Substitute back a few terms to verify the solution satisfies both the recurrence relation and initial conditions.

8. **Remember the Fibonacci special case**: When solving Fibonacci (aₙ = aₙ₋₁ + aₙ₋₂), the characteristic equation is r² - r - 1 = 0 with roots (1 ± √5)/2.
