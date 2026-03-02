# Generating Functions - Summary

## Key Definitions and Concepts

- **Generating Function:** A formal power series G(x) = Σ aₙxⁿ that encodes an infinite sequence {a₀, a₁, a₂, ...} of numbers or combinatorial quantities.

- **Ordinary Generating Function (OGF):** G(x) = Σ aₙxⁿ, used for counting problems where order does not matter (combinations/selections).

- **Exponential Generating Function (EGF):** G(x) = Σ aₙ(xⁿ/n!), used when order matters (arrangements/permutations of distinct objects).

- **Convolution:** The coefficient of xⁿ in the product of two generating functions, representing combinations from two independent choices.

## Important Formulas and Theorems

- Geometric Series: 1/(1-x) = Σ xⁿ for |x| < 1
- Binomial Theorem: (1+x)ⁿ = Σ C(n,k)xᵏ
- Exponential: eˣ = Σ xⁿ/n!
- (1-x)⁻ᵏ = Σ C(n+k-1, k-1)xⁿ (stars and bars)
- Euler's Theorem: Partitions into distinct parts = partitions into odd parts

## Key Points

- Generating functions transform recurrence relations into algebraic equations, simplifying solution procedures.

- For "at least k" constraints, use generating function xᵏ/(1-x); for "at most k" constraints, use (1-xᵏ⁺¹)/(1-x).

- Multiplication of generating functions corresponds to convolution—the fundamental operation for combining independent choices.

- EGFs divide by n! to automatically account for permutations, making them ideal for labeled/distinct objects.

- The coefficient [xⁿ]G(x) extracts the nth term of the encoded sequence from the generating function.

- Partial fraction decomposition is essential for extracting coefficients from rational generating functions.

- Standard generating functions (1/(1-x), eˣ, (1+x)ⁿ) serve as building blocks for more complex problems.

## Common Mistakes to Avoid

1. Confusing when to use OGF versus EGF—using OGF for permutation problems yields incorrect counts.

2. Forgetting to account for initial conditions when solving recurrence relations via generating functions.

3. Incorrectly handling the "at least one" constraint by not starting the series from the appropriate power of x.

4. Neglecting to simplify generating functions before extracting coefficients, leading to unnecessary complexity.

5. Treating x as a numerical value instead of a formal symbol; generating functions are formal power series.

## Revision Tips

1. Practice converting 5-6 combinatorial problems into generating functions before the exam.

2. Memorize standard generating functions: 1/(1-x), eˣ, (1+x)ⁿ as they appear frequently.

3. When solving recurrence relations, always verify the solution by checking initial terms.

4. Understand the combinatorial interpretation of multiplication: G(x)·H(x) means "choose from G, then choose from H."

5. For integer partition problems, remember that OGF with factors (1+xᵏ) gives distinct parts, while 1/(1-xᵏ) gives unlimited repetitions.