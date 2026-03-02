# Onto Functions

## Introduction

In the study of functions, understanding how elements from the domain map to elements in the codomain is fundamental. While one-to-one (injective) functions ensure that distinct inputs produce distinct outputs, surjective functions—or onto functions—ensure that every element in the codomain has at least one preimage in the domain. This property of "covering" the entire codomain makes onto functions essential in various mathematical and computational contexts.

The concept of onto functions appears frequently in discrete mathematics, database theory, and algorithm analysis. In database systems, surjective functions model scenarios where every possible output value can be generated from some input. In cryptography and hashing, understanding whether a function is onto helps analyze collision possibilities. For University of Delhi examinations, onto functions constitute a significant portion of questions in the Relations and Functions module, requiring both theoretical understanding and practical problem-solving skills.

This chapter explores the precise definition of onto functions, methods to verify surjectivity, the relationship between onto and other function properties, and computational techniques for counting onto functions between finite sets.

## Key Concepts

### Definition of Onto Functions

A function f: A → B is called ONTO (or SURJECTIVE) if for every element b in the codomain B, there exists at least one element a in the domain A such that f(a) = b.

Formally, f is onto if: ∀b ∈ B, ∃a ∈ A such that f(a) = b

The essential characteristic is that the range (or image) of f equals the codomain B. In other words, no element in the codomain is "left out" or unmapped.

### Visual Representation

Consider sets A = {1, 2, 3} and B = {a, b, c}. A function f: A → B is onto if every element of B appears as an output for some input from A. This can be visualized as arrows from each domain element to codomain elements, where all codomain elements must have at least one incoming arrow.

### Proving a Function is Onto

To prove a function f: A → B is onto, one must show that for an arbitrary element b ∈ B, there exists a specific a ∈ A such that f(a) = b. This typically involves:

1. Taking an arbitrary element y in the codomain B
2. Solving the equation f(x) = y for x in terms of y
3. Showing that this x belongs to the domain A
4. Concluding that every element in B has a preimage

### Onto vs One-to-One vs Bijective

It is crucial to distinguish between these function properties:

A function is ONE-TO-ONE (injective) if f(a₁) = f(a₂) implies a₁ = a₂ for all a₁, a₂ in the domain. Each output has at most one input.

A function is ONTO (surjective) if for every b in the codomain, there exists a in the domain with f(a) = b. Each output has at least one input.

A function is BIJECTIVE if it is both one-to-one and onto. A bijective function establishes a perfect "matching" between domain and codomain, with each element in each set having exactly one counterpart.

### Number of Onto Functions Between Finite Sets

For finite sets, we can count the number of onto functions using the inclusion-exclusion principle. If |A| = m and |B| = n where m ≥ n, the number of onto functions from A to B is:

Number of onto functions = n^m - C(n,1)(n-1)^m + C(n,2)(n-2)^m - C(n,3)(n-3)^m + ... + (-1)^n C(n,n-1)(1)^m

This formula subtracts functions that miss at least one codomain element, adds back those that miss at least two, and so on. The formula can be written as:

Number of onto functions = Σ(k=0 to n) (-1)^k C(n, k) (n - k)^m

Where C(n, k) denotes the binomial coefficient "n choose k".

For the special case where |A| = |B| = n, the number of onto (and therefore bijective) functions is simply n! (the number of permutations).

## Examples

### Example 1: Proving f: ℤ → ℤ defined by f(x) = 2x is NOT onto

SOLUTION:

We need to show that not every integer can be expressed as 2x for some integer x.

Take an arbitrary element y in the codomain ℤ. We need to find x ∈ ℤ such that f(x) = y, i.e., 2x = y.

If y = 1 (or any odd integer), then x = y/2 = 1/2, which is NOT an integer.

Since 1 ∈ ℤ (codomain) but there is no integer x such that 2x = 1, the function is NOT onto.

The range of f is the set of all even integers {..., -4, -2, 0, 2, 4, ...}, which is a proper subset of ℤ (codomain).

### Example 2: Proving g: ℝ → ℝ defined by g(x) = 3x + 7 is onto

SOLUTION:

Let y be an arbitrary element in the codomain ℝ. We need to find x ∈ ℝ such that g(x) = y.

Solving: 3x + 7 = y
3x = y - 7
x = (y - 7)/3

Since y ∈ ℝ, (y - 7)/3 ∈ ℝ. Therefore, x ∈ ℝ exists.

For any chosen y, we can compute x = (y - 7)/3, and g(x) = 3((y-7)/3) + 7 = y - 7 + 7 = y.

Thus, g is ONTO because every real number y has a preimage x = (y - 7)/3.

### Example 3: Counting onto functions from A = {1, 2, 3} to B = {a, b}

SOLUTION:

Here, |A| = m = 3, |B| = n = 2, and m ≥ n.

Using the inclusion-exclusion formula:
Number of onto functions = Σ(k=0 to 2) (-1)^k C(2, k) (2 - k)^3
= C(2, 0)(2)^3 - C(2, 1)(1)^3 + C(2, 2)(0)^3
= 1 × 8 - 2 × 1 + 1 × 0
= 8 - 2 + 0
= 6

Let us verify manually: With domain {1, 2, 3} and codomain {a, b}, an onto function must map all three elements to either {a, b} with both values used. The possibilities are:
- Exactly two inputs map to 'a', one to 'b': 3 ways (choose which input gets 'b')
- Exactly two inputs map to 'b', one to 'a': 3 ways (choose which input gets 'a')
Total = 6 onto functions. This matches our calculation.

### Example 4: Finding number of onto functions from a set of 5 elements to a set of 3 elements

SOLUTION:

Using the formula with m = 5, n = 3:
Number = Σ(k=0 to 3) (-1)^k C(3, k) (3 - k)^5
= C(3, 0)(3)^5 - C(3, 1)(2)^5 + C(3, 2)(1)^5 - C(3, 3)(0)^5
= 1 × 243 - 3 × 32 + 3 × 1 - 1 × 0
= 243 - 96 + 3
= 150

Therefore, there are 150 onto functions from a 5-element set to a 3-element set.

## Exam Tips

For the University of Delhi end-semester examinations, keep the following points in mind:

1. MEMORIZE THE DEFINITION: The formal definition f is onto if ∀b ∈ B, ∃a ∈ A such that f(a) = b appears frequently in definition-based questions.

2. PROOF TECHNIQUE: When proving a function is onto, always take an arbitrary element y from the codomain and explicitly find its preimage x. This two-step process (assume, then construct) is the standard approach.

3. COUNTEREXAMPLE FOR NON-ONTO: To show a function is not onto, it suffices to find ONE element in the codomain without a preimage—this is often the simplest approach.

4. CONNECT TO PIGEONHOLE PRINCIPLE: If |A| < |B| (domain smaller than codomain), the function cannot be onto—this is an immediate conclusion from the pigeonhole principle.

5. COUNTING FORMULA: Remember the inclusion-exclusion formula for counting onto functions. For n = 2, the formula simplifies to 2^m - 2, which is useful for quick calculations.

6. BIJECTIVE CHECK: A function is bijective if and only if it is both one-to-one and onto. Many exam questions ask you to determine whether a function is bijective by checking both properties.

7. INVERSE FUNCTIONS: Only onto functions have right inverses, and one-to-one functions have left inverses. This connection between surjectivity and invertibility is important for advanced questions.

8. CLEAR NOTATION: Distinguish clearly between range (image) and codomain. A function is onto precisely when range equals codomain.