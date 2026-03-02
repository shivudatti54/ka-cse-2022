# Generating Functions

## Introduction

Generating functions are one of the most powerful and elegant tools in discrete mathematics, serving as a bridge between algebraic manipulations and combinatorial counting. Introduced formally by Abraham de Moivre in the 18th century and later refined by Laplace, generating functions provide a systematic way to encode infinite sequences of numbers into a single function, enabling us to solve complex counting problems and recurrence relations with remarkable efficiency.

In the context of Computer Science, generating functions find extensive applications in algorithm analysis, particularly in analyzing the time complexity of recursive algorithms. They are indispensable in solving linear recurrence relations that frequently appear in the analysis of data structures, sorting algorithms, and divide-and-conquer strategies. Beyond algorithm analysis, generating functions play a crucial role in combinatorics, enabling us to count arrangements, selections, and partitions with unprecedented ease. For DU students preparing for competitive placements and higher studies, a thorough understanding of generating functions is essential, as this topic regularly appears in technical interviews and graduate-level examinations.

## Key Concepts

### Definition of Generating Function

A generating function is a formal power series that encodes an infinite sequence of numbers. For a sequence {a₀, a₁, a₂, a₃, ...}, the ordinary generating function (OGF) is defined as:

**G(x) = a₀ + a₁x + a₂x² + a₃x³ + ... = Σ aₙxⁿ** (where n ranges from 0 to ∞)

The variable x in a generating function is treated as a formal symbol—we rarely care about its numerical value. Instead, the coefficients of the powers of x carry the combinatorial information we seek. This "formal" treatment allows us to perform algebraic operations on generating functions without concerns about convergence.

### Ordinary Generating Function (OGF)

The ordinary generating function is used primarily for counting problems where order does not matter. Consider the sequence where aₙ = 1 for all n ≥ 0. Its generating function is:

G(x) = 1 + x + x² + x³ + ... = 1/(1-x), for |x| < 1

This fundamental generating function appears repeatedly in combinatorial problems. Another essential OGF is that of the Fibonacci sequence {F₀, F₁, F₂, ...}, given by G(x) = x/(1-x-x²).

### Exponential Generating Function (EGF)

For problems where order matters (arrangements of distinct objects), we use exponential generating functions. The EGF of a sequence {a₀, a₁, a₂, ...} is defined as:

**EGF(x) = a₀ + a₁x + a₂(x²/2!) + a₃(x³/3!) + ... = Σ aₙ(xⁿ/n!)**

The division by n! simplifies many operations, particularly when combining sequences through convolution. EGFs are essential when counting permutations and arrangements.

### Operations on Generating Functions

**Addition:** If G(x) = Σ aₙxⁿ and H(x) = Σ bₙxⁿ, then G(x) + H(x) = Σ (aₙ + bₙ)xⁿ

**Multiplication (Convolution):** The product G(x) · H(x) = Σ (Σ aₖbₙ₋ₖ) xⁿ, giving the convolution of the sequences. This corresponds to combining selections from two different sets.

**Shifting:** If G(x) = Σ aₙxⁿ, then x·G(x) shifts the sequence right (introducing a₀ = 0), while G(x)/x = Σ aₙ₊₁xⁿ shifts left (dropping a₀).

**Differentiation:** G'(x) = Σ naₙxⁿ⁻¹, shifting the sequence and multiplying by indices.

### Special Generating Functions

1. **Geometric Series:** 1/(1-x) = 1 + x + x² + x³ + ... (for |x| < 1)
2. **Binomial Series:** (1+x)ⁿ = Σ C(n,k)xᵏ
3. **Exponential:** eˣ = Σ xⁿ/n!
4. **Modified Geometric:** 1/(1-x)² = Σ (n+1)xⁿ (counting selections with repetitions where order matters)

## Examples

### Example 1: Counting Solutions to Equations

**Problem:** Find the number of ways to select 10 items from three types of items where at least 2 of the first type, at most 3 of the second type, and at least 1 of the third type must be selected.

**Solution:**

For each type, we construct the generating function:
- Type 1 (at least 2): x² + x³ + x⁴ + ... = x²/(1-x)
- Type 2 (at most 3): 1 + x + x² + x³ = (1-x⁴)/(1-x)
- Type 3 (at least 1): x + x² + x³ + ... = x/(1-x)

The combined generating function is:
G(x) = [x²/(1-x)] · [(1-x⁴)/(1-x)] · [x/(1-x)]
     = x³(1-x⁴)/(1-x)³

We need the coefficient of x¹⁰ in G(x). The term x³ from numerator contributes x³, and we need x⁷ from (1-x⁴)/(1-x)³.

From (1-x⁴)/(1-x)³ = (1-x³-x²+x⁴)/(1-x)³, we find coefficient of x⁷:

Coefficient from 1/(1-x)³ is C(7+3-1, 3-1) = C(9,2) = 36
Coefficient from -x⁴/(1-x)³ is -C(7-4+3-1, 2) = -C(5,2) = -10

Total coefficient = 36 - 10 = 26

**Answer:** There are 26 ways to select the items.

### Example 2: Solving Recurrence Relations

**Problem:** Solve the recurrence relation aₙ = 3aₙ₋₁ + 2 with initial condition a₀ = 1.

**Solution:**

Let G(x) = Σ aₙxⁿ be the generating function.

Multiply the recurrence by xⁿ and sum from n=1 to ∞:
Σ aₙxⁿ = 3Σ aₙ₋₁xⁿ + 2Σ xⁿ

This gives: G(x) - a₀ = 3xG(x) + 2x/(1-x)

Substituting a₀ = 1:
G(x) - 1 = 3xG(x) + 2x/(1-x)

Rearranging: G(x)(1 - 3x) = 1 + 2x/(1-x) = (1-x+2x)/(1-x) = (1+x)/(1-x)

Therefore: G(x) = (1+x)/[(1-x)(1-3x)]

Using partial fractions:
(1+x)/[(1-x)(1-3x)] = A/(1-x) + B/(1-3x)

Solving: 1+x = A(1-3x) + B(1-x)
         = A - 3Ax + B - Bx = (A+B) + (-3A-B)x

Equating coefficients: A + B = 1 and -3A - B = 1
Solving: A = -1, B = 2

Thus: G(x) = -1/(1-x) + 2/(1-3x)
         = -Σ xⁿ + 2Σ 3ⁿxⁿ
         = Σ (2·3ⁿ - 1)xⁿ

Therefore: **aₙ = 2·3ⁿ - 1**

### Example 3: Partitions of Integers

**Problem:** Find the generating function for the number of partitions of an integer n into distinct parts.

**Solution:**

For partitions into distinct parts, we can use either odd parts or even parts, but not both. Using distinct parts (exactly one of each part), the generating function is:

G(x) = (1+x)(1+x²)(1+x³)(1+x⁴)... = Π(1+xᵏ) for k from 1 to ∞

This can be alternatively expressed using partitions into odd parts:
H(x) = 1/(1-x) · 1/(1-x³) · 1/(1-x⁵) ... = Π 1/(1-x²ᵏ⁻¹)

These two generating functions are equal, demonstrating Euler's famous theorem: the number of partitions of n into distinct parts equals the number of partitions of n into odd parts.

For example, n = 5: Distinct partitions are 5, 4+1, 3+2 (3 ways); odd partitions are 5, 3+1+1, 1+1+1+1+1 (3 ways).

## Exam Tips

1. **Identify the Type:** Quickly determine whether you need OGF or EGF. Use OGF when order doesn't matter (combinations), use EGF when order matters (permutations).

2. **Construct Generating Functions Systematically:** For "at least k" constraints, use xᵏ + xᵏ⁺¹ + ... = xᵏ/(1-x). For "at most k" constraints, use 1 + x + ... + xᵏ = (1-xᵏ⁺¹)/(1-x).

3. **Recurrence Relations:** Always start by forming G(x) - a₀ equation, multiply the recurrence by xⁿ and sum appropriately, then solve for G(x).

4. **Partial Fractions are Essential:** For solving recurrence relations, master partial fraction decomposition to convert rational generating functions into simple geometric series.

5. **Convolution Interpretation:** When multiplying generating functions, understand that the coefficient of xⁿ in the product represents the sum of products of terms that sum to n—this is convolution.

6. **Check Initial Terms:** After finding a generating function, expand the first few terms to verify they match the original sequence.

7. **Applications to Know:** Be prepared to apply generating functions to: coin change problems, distribution of identical objects, recurrence relation solving, and partition problems.

8. **EGF vs OGF Remember:** The n! in the denominator of EGFs "automatically" accounts for arrangements, making them perfect for problems involving labeled objects.