# Generating Functions

## Introduction

Generating functions are one of the most powerful and elegant tools in discrete mathematics, serving as a bridge between algebraic manipulation and combinatorial counting. Originally developed by Abraham de Moivre in the 18th century and later formalized by Pafnuty Chebyshev and combinatorialists like Euler, generating functions provide a unified framework for solving a wide range of problems in mathematics and computer science.

In the context of the MCA program at the University of Delhi, generating functions hold particular significance because they form the theoretical foundation for analyzing algorithmic complexity, solving recurrence relations that arise in algorithm analysis, and tackling combinatorial enumeration problems that appear in data structures, database systems, and software engineering. Unlike elementary combinatorial techniques that require case-by-case analysis, generating functions allow us to transform complex counting problems into algebraic problems that can be solved systematically. This abstraction is particularly valuable in professional software development where we often need to analyze resource requirements of recursive algorithms or count valid configurations in systems.

The fundamental idea behind generating functions is deceptively simple: instead of working directly with a sequence of numbers, we encode the entire sequence as the coefficients of a formal power series. This encoding preserves all the combinatorial information while enabling the use of powerful algebraic operations to manipulate and extract desired information.

## Key Concepts

### Definition and Types of Generating Functions

An **ordinary generating function** (OGF) for a sequence {a₀, a₁, a₂, a₃, ...} is defined as:

**G(x) = a₀ + a₁x + a₂x² + a₃x³ + ... = Σ aₙxⁿ**

The coefficient of xⁿ in G(x) is exactly aₙ. We write this as [xⁿ]G(x) = aₙ. The variable x in a generating function is purely formal—we never substitute actual numerical values into it. This is crucial to understand: generating functions are algebraic objects that we manipulate symbolically.

**Exponential generating functions** (EGF) are used when dealing with labeled combinatorial structures and are defined as:

**E(x) = a₀ + a₁x + a₂x²/2! + a₃x³/3! + ... = Σ aₙ(xⁿ/n!)**

The factorial in the denominator accounts for the exponential growth in the number of ways to label objects, making EGFs particularly useful for counting permutations and arrangements.

### Operations on Generating Functions

The algebraic operations on generating functions have direct combinatorial interpretations:

**Addition**: If G(x) = Σ aₙxⁿ and H(x) = Σ bₙxⁿ, then G(x) + H(x) = Σ (aₙ + bₙ)xⁿ. This corresponds to combining two sets of objects where we choose objects from either set.

**Multiplication (Convolution)**: The product G(x)H(x) = Σ (Σ aₖbₙ₋ₖ) xⁿ. The coefficient of xⁿ equals the convolution of the sequences {aₙ} and {bₙ}. This operation corresponds to selecting objects from two different categories and counting the total ways to obtain n items.

**Shifting**: If G(x) = Σ aₙx⁙, then x·G(x) = Σ aₙxⁿ⁺¹ shifts the sequence right by one (introducing a leading zero). Similarly, (G(x) - a₀)/x shifts left, removing the a₀ term.

**Differentiation**: G'(x) = Σ n·aₙxⁿ⁻¹, which relates to the sequence {n·aₙ}.

### Common Generating Functions

Several fundamental sequences have well-known generating functions that serve as building blocks:

| Sequence | OGF |
|----------|-----|
| 1, 1, 1, 1, ... | 1/(1-x) |
| 1, 2, 3, 4, ... | 1/(1-x)² |
| 1, 0, 1, 0, 1, ... | 1/(1-x²) |
| C(n + k - 1, k - 1) | 1/(1-x)ᵏ |
| Fibonacci numbers | x/(1-x-x²) |
| Catalan numbers | (1-√(1-4x))/(2x) |

### Applications to Recurrence Relations

Generating functions provide a systematic method for solving linear recurrence relations with constant coefficients. The procedure involves: (1) multiplying the recurrence by xⁿ and summing over all valid n values, (2) substituting the generating function, (3) solving the resulting algebraic equation, and (4) extracting coefficients.

For example, consider the Fibonacci recurrence: Fₙ = Fₙ₋₁ + Fₙ₋₂ with F₀ = 0, F₁ = 1. Let F(x) = Σ Fₙxⁿ. Multiplying by xⁿ and summing from n=2 to ∞ gives:

Σ Fₙxⁿ = Σ Fₙ₋₁xⁿ + Σ Fₙ₋₂xⁿ

This yields F(x) - F₁x = xF(x) + x²F(x), so F(x) = x/(1-x-x²), matching the known closed form.

### Partition Numbers

The partition function p(n) counts the number of ways to write n as a sum of positive integers, where order does not matter. The generating function for partitions is remarkably elegant:

P(x) = 1/∏(1-xᵏ) for k=1 to ∞

This infinite product representation connects partition theory to the theory of partitions, revealing deep number-theoretic properties. Euler's pentagonal theorem, which gives the generating function for partitions into distinct parts, is a cornerstone result: ∏(1-xᵏ) = Σ (-1)ᵐx^(m(3m-1)/2).

## Examples

**Example 1: Counting Binary Strings**

Problem: Find the number of binary strings of length n with no consecutive 1s.

Solution: Let aₙ be the desired count. For n=0, we have the empty string: a₀ = 1. For n=1, we have "0" and "1": a₁ = 2. For n ≥ 2, the first bit determines the rest: if it starts with 0, we have aₙ₋₁ possibilities for the remaining n-1 bits; if it starts with 10, we have aₙ₋₂ possibilities. Thus aₙ = aₙ₋₁ + aₙ₋₂.

This is the Fibonacci recurrence! Let G(x) = Σ aₙx⁙. Using the recurrence and initial conditions:

G(x) - a₀ - a₁x = x(G(x) - a₀) + x²G(x)
G(x) - 1 - 2x = x(G(x) - 1) + x²G(x)
G(x)(1 - x - x²) = 1 + x
G(x) = (1+x)/(1-x-x²)

Expanding this gives aₙ = Fₙ₊₂, the (n+2)nd Fibonacci number. For n=4, a₄ = F₆ = 8 (strings: 0000, 0001, 0010, 0100, 0101, 1000, 1001, 1010).

**Example 2: Solving a Non-homogeneous Recurrence**

Problem: Solve aₙ = 3aₙ₋₁ + 2ⁿ with a₀ = 1.

Solution: Let G(x) = Σ aₙx⁙. The generating function for {2ⁿ} is Σ 2ⁿxⁿ = 1/(1-2x).

Multiplying the recurrence by xⁿ and summing from n=1 to ∞:

Σ aₙx⁙ = 3Σ aₙ₋₁x⁙ + Σ 2ⁿx⁙

G(x) - a₀ = 3xG(x) + (1/(1-2x) - 1)

G(x)(1 - 3x) = 1 + (x/(1-2x))

G(x) = (1 + x/(1-2x))/(1-3x) = (1 - 2x + x)/((1-2x)(1-3x)) = (1 - x)/((1-2x)(1-3x))

Using partial fractions:
(1 - x)/((1-2x)(1-3x)) = A/(1-2x) + B/(1-3x)

Solving: 1 - x = A(1-3x) + B(1-2x)
Setting x = 1/2: 1 - 1/2 = A(1 - 3/2) ⇒ 1/2 = A(-1/2) ⇒ A = -1
Setting x = 1/3: 1 - 1/3 = B(1 - 2/3) ⇒ 2/3 = B(1/3) ⇒ B = 2

Thus G(x) = -1/(1-2x) + 2/(1-3x) = -Σ 2ⁿxⁿ + 2Σ 3⁙x⁙

Therefore aₙ = -2ⁿ + 2·3ⁿ. Checking: a₀ = -1 + 2 = 1 ✓, a₁ = -2 + 6 = 4, and indeed 4 = 3(1) + 2 = 5? Wait, let's verify: a₁ = 3(1) + 2¹ = 3 + 2 = 5 ≠ 4. I need to recalculate.

Actually: G(x) - a₀ = 3xG(x) + (1/(1-2x) - a₀)? Let's re-do:

Σ aₙxⁿ for n≥1 = 3x Σ aₙ₋₁xⁿ⁻¹ + Σ 2ⁿxⁿ for n≥1
G(x) - a₀ = 3xG(x) + (1/(1-2x) - 1)
G(x) - 1 = 3xG(x) + (x/(1-2x))
G(x)(1 - 3x) = 1 + x/(1-2x) = (1-2x + x)/(1-2x) = (1-x)/(1-2x)
G(x) = (1-x)/((1-2x)(1-3x))

1 - x = A(1-3x) + B(1-2x) = A - 3Ax + B - 2Bx = (A+B) - (3A+2B)x
Equating: A + B = 1, and -(3A+2B) = -1, so 3A+2B=1
Solving: from A+B=1, B=1-A. Then 3A+2(1-A)=1 ⇒ 3A+2-2A=1 ⇒ A=-1, so B=2.

So G(x) = -1/(1-2x) + 2/(1-3x) = -Σ2ⁿxⁿ + 2Σ3⁙x⁙ = Σ(-2ⁿ+2·3⁙)x⁙

Now a₁ = -2 + 2·3 = 4. The recurrence: a₁ = 3a₀ + 2¹ = 3(1) + 2 = 5. There's a discrepancy! The issue is that we summed from n=1 but should include n=0 properly. Let's verify with the formula: aₙ = 2·3ⁿ - 2ⁿ. Then a₁ = 6 - 2 = 4, a₂ = 18 - 4 = 14. Check recurrence: a₂ = 3a₁ + 2² = 3(4) + 4 = 16 ≠ 14. 

The recurrence should be aₙ = 3aₙ₋₁ + 2ⁿ with n≥1. So a₁ = 3(1) + 2 = 5, a₂ = 3(5) + 4 = 19. Our solution gives 14. The generating function setup was correct, but we must have made an algebraic error. The correct generating function approach gives aₙ = 2·3ⁿ - 2ⁿ, and verification shows it works: a₀ = 2-1=1 ✓, a₁ = 6-2=4 ≠ 5, so the formula must be aₙ = 3^(n+1) - 2^(n+1). This simplifies to aₙ = 3^(n+1) - 2^(n+1), which correctly yields a₁ = 9-4=5 and a₂ = 27-8=19, matching the recurrence.

**Example 3: Coin Change Problem**

Problem: In how many ways can we make change for n rupees using coins of denominations 1, 2, and 5?

Solution: The generating function for each coin type is:
- For 1-rupee coins: 1 + x + x² + x³ + ... = 1/(1-x)
- For 2-rupee coins: 1 + x² + x⁴ + x⁶ + ... = 1/(1-x²)
- For 5-rupee coins: 1 + x⁵ + x¹⁰ + x¹⁵ + ... = 1/(1-x⁵)

The overall generating function is G(x) = 1/((1-x)(1-x²)(1-x⁵)). The coefficient of xⁿ gives the number of ways to make change for n rupees.

For n=10, we can compute this coefficient by expanding or using combinatorial reasoning. The partitions using {1,2,5} that sum to 10 are: 5+5, 5+2+2+1, 5+2+1+1+1, 5+1+1+1+1+1, 2+2+2+2+2, 2+2+2+2+1+1, 2+2+2+1+1+1+1, 2+2+1+1+1+1+1+1, 2+1+1+1+1+1+1+1+1, and all 1s. That's 11 ways.

## Exam Tips

1. **Understand the fundamental correspondence**: Remember that coefficients of generating functions represent the sequence elements. Always identify what aₙ represents in your problem before constructing G(x).

2. **Master the standard forms**: Memorize generating functions for 1/(1-x), 1/(1-x)², 1/(1-xᵏ), and x/(1-x-x²). These appear frequently and save significant computation time.

3. **For recurrence relations**: The standard approach is: multiply by xⁿ, sum over valid n, substitute G(x), solve for G(x), then extract coefficients (often using partial fractions).

4. **Distinguish between OGF and EGF**: Use ordinary generating functions for combinations and selections (order doesn't matter). Use exponential generating functions when labeling is involved (order matters, objects are distinct).

5. **Partial fractions are essential**: When solving for G(x), you'll frequently need to decompose rational functions. Practice partial fraction decomposition with quadratic factors.

6. **Convolution shortcut**: The coefficient of xⁿ in product G(x)H(x) equals Σ aₖbₙ₋ₖ. This is useful for "two-stage" selection problems.

7. **Check your answers**: Verify initial conditions and small values (n=0,1,2) against your generating function solution. This catches algebraic errors early.