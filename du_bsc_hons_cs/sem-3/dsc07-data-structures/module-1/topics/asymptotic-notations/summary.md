# Asymptotic Notations - Summary

## Key Definitions and Concepts

- **Big O Notation O(g(n))**: Upper bound; worst-case scenario. f(n) = O(g(n)) if ∃ c > 0, n₀ > 0 such that 0 ≤ f(n) ≤ c × g(n) for all n ≥ n₀.

- **Big Omega Notation Ω(g(n))**: Lower bound; best-case scenario. f(n) = Ω(g(n)) if ∃ c > 0, n₀ > 0 such that 0 ≤ c × g(n) ≤ f(n) for all n ≥ n₀.

- **Theta Notation Θ(g(n))**: Tight bound; both upper and lower bounds are the same. f(n) = Θ(g(n)) if ∃ c₁, c₂, n₀ > 0 such that c₁ × g(n) ≤ f(n) ≤ c₂ × g(n) for all n ≥ n₀.

- **Little o Notation o(g(n))**: Upper bound but not tight; f grows strictly slower than g.

- **Little Omega Notation ω(g(n))**: Lower bound but not tight; f grows strictly faster than g.

## Important Formulas and Theorems

- **Growth Rate Hierarchy**: O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(n³) < O(2ⁿ)

- **Transitivity**: If f = O(g) and g = O(h), then f = O(h)

- **Symmetry**: f = Θ(g) if and only if g = Θ(f)

- **Transpose Symmetry**: f = O(g) if and only if g = Ω(f)

- **Polynomial Rule**: For polynomial anᵏ + ... + a₀, complexity is Θ(nᵏ)

- **Logarithm Rule**: All logarithmic bases are equivalent: log₂n = Θ(log₁₀n) = Θ(ln n)

## Key Points

- Asymptotic notations ignore hardware dependencies and focus on algorithm behavior as input size grows.

- Big O is most commonly used for worst-case analysis in practice.

- A function can have multiple Big O bounds, but we seek the tightest (smallest) one.

- Constants and lower-order terms are dropped in asymptotic analysis.

- Θ notation provides the most precise classification when upper and lower bounds match.

- Little o and ω indicate strict inequalities (not tight bounds).

- Understanding growth rates helps in choosing appropriate algorithms for different problem sizes.

## Common Mistakes to Avoid

1. **Confusing Big O with Ω**: Remember O means "at most" (upper bound), Ω means "at least" (lower bound).

2. **Including constants incorrectly**: O(2n) should be written as O(n); we drop constants.

3. **Wrong inequality direction**: For Big O, f(n) ≤ c × g(n); for Ω, f(n) ≥ c × g(n). Getting this reversed is a common error.

4. **Using equals sign casually**: It's technically correct to write f(n) = O(g(n)) in mathematics, but understand it means f(n) ∈ O(g(n)).

5. **Ignoring n₀**: The definition only applies for n ≥ n₀; values below n₀ are irrelevant.

## Revision Tips

1. **Practice with code**: Take actual code snippets and determine their complexity by counting operations.

2. **Prove relationships**: Work through mathematical proofs for f = O(g), f = Ω(g), and f = Θ(g) using the definitions.

3. **Memorize the hierarchy**: The complexity hierarchy should be ingrained - know it like multiplication tables.

4. **Solve previous years**: DU exam questions frequently ask for complexity analysis of given algorithms.

5. **Draw comparison graphs**: Visualizing function growth helps understand why exponential grows so much faster than polynomial.