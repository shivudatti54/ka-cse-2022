# Markov's Inequality, Chebyshev's Inequality, and Central Limit Theorem

## Introduction

In the realm of probability theory for computing, understanding how to bound probabilities without knowing the complete distribution of a random variable is an invaluable skill. This module introduces three fundamental results: Markov's Inequality, Chebyshev's Inequality, and the Central Limit Theorem (CLT). These theorems provide powerful tools for analyzing algorithms, estimating errors, and making predictions in computer science applications ranging from network traffic modeling to machine learning.

Markov's Inequality gives us a crude but universal bound for non-negative random variables. Chebyshev's Inequality refines this by incorporating variance, providing tighter bounds. The Central Limit Theorem, arguably one of the most profound results in probability theory, explains why the normal distribution appears so frequently in nature and computing scenarios—it states that the sum (or average) of a large number of independent and identically distributed (i.i.d.) random variables, regardless of their original distribution, tends toward a normal distribution.

## Key Concepts

### Markov's Inequality

Markov's Inequality provides an upper bound on the probability that a non-negative random variable exceeds a certain value. It is named after the Russian mathematician Andrey Markov.

**Theorem:** Let X be a non-negative random variable (i.e., X ≥ 0) with finite expected value E(X) = μ. Then for any a > 0:

**P(X ≥ a) ≤ E(X)/a = μ/a**

**Proof Sketch:** For a non-negative random variable X, we can express the expected value as:

E(X) = ∫₀^∞ x f(x) dx ≥ ∫ₐ^∞ x f(x) dx ≥ ∫ₐ^∞ a f(x) dx = a · P(X ≥ a)

Rearranging gives us P(X ≥ a) ≤ E(X)/a.

**Key Properties:**
- Works for any non-negative distribution
- Often loose (not tight) but universally applicable
- Requires only the mean, not the full distribution
- Valid for any a > 0

### Chebyshev's Inequality

Chebyshev's Inequality improves upon Markov's by incorporating variance, giving better bounds for distributions concentrated around the mean.

**Theorem:** Let X be a random variable with finite mean μ and finite variance σ². Then for any k > 0:

**P(|X - μ| ≥ k) ≤ σ²/k²** or equivalently **P(|X - μ| ≥ kσ) ≤ 1/k²**

**Proof Sketch:** Consider the non-negative variable (X - μ)². Applying Markov's Inequality:

P((X - μ)² ≥ k²) ≤ E[(X - μ)²]/k² = σ²/k²

Since (X - μ)² ≥ k² iff |X - μ| ≥ k, we obtain the result.

**Interpretation:** At most 1/k² of the data lies more than k standard deviations away from the mean. For k = 2, at most 25% of data lies beyond 2σ; for k = 3, at most 11.1% lies beyond 3σ.

### Weak Law of Large Numbers

The Weak Law of Large Numbers (WLLN) is a direct application of Chebyshev's Inequality.

**Theorem:** Let X₁, X₂, ..., Xₙ be i.i.d. random variables with mean μ and variance σ². Define the sample mean X̄ₙ = (X₁ + ... + Xₙ)/n. Then for any ε > 0:

**lim_{n→∞} P(|X̄ₙ - μ| < ε) = 1**

In other words, the sample mean converges in probability to the true mean as sample size increases.

**Proof using Chebyshev:** Since E(X̄ₙ) = μ and Var(X̄ₙ) = σ²/n, applying Chebyshev:

P(|X̄ₙ - μ| ≥ ε) ≤ σ²/(nε²) → 0 as n → ∞

### Central Limit Theorem (CLT)

The Central Limit Theorem is perhaps the most important theorem in probability theory, explaining why the normal distribution appears so universally.

**Theorem (Classical CLT):** Let X₁, X₂, ..., Xₙ be i.i.d. random variables with mean μ and finite variance σ² > 0. Then as n → ∞, the standardized sum:

Zₙ = (X̄ₙ - μ) / (σ/√n) = (ΣᵢXᵢ - nμ) / (σ√n)

**converges in distribution to the standard normal distribution N(0,1).**

In simpler terms: **The distribution of sample means approaches a normal distribution with mean μ and standard error σ/√n, regardless of the original distribution.**

**Mathematical Expression:**
lim_{n→∞} P(Zₙ ≤ z) = Φ(z) where Φ is the standard normal CDF

**Key Implications:**
1. For sufficiently large n (typically n ≥ 30), X̄ₙ ≈ N(μ, σ²/n)
2. The approximation improves as n increases
3. Works for virtually any distribution with finite variance

## Examples

### Example 1: Applying Markov's Inequality

**Problem:** The average memory usage of a server process is 2 GB. Using Markov's Inequality, find an upper bound on the probability that the process uses at least 8 GB of memory.

**Solution:**

Given: E(X) = 2 GB, a = 8 GB

Using Markov's Inequality: P(X ≥ 8) ≤ E(X)/8 = 2/8 = 0.25

**Interpretation:** At most 25% of the time can the memory usage be 8 GB or higher, regardless of the actual distribution. This is a conservative (loose) bound—the actual probability might be much lower.

### Example 2: Chebyshev's Inequality for Quality Control

**Problem:** A packet router processes packets with mean throughput μ = 1000 packets/second and standard deviation σ = 50 packets/second. Using Chebyshev's Inequality, bound the probability that throughput deviates by more than 150 packets/second from the mean.

**Solution:**

Given: μ = 1000, σ = 50, k = 150/50 = 3 standard deviations

Using Chebyshev: P(|X - μ| ≥ 150) ≤ σ²/k² = 50²/150² = 2500/22500 ≈ 0.111

Or using the alternative form: P(|X - μ| ≥ 3σ) ≤ 1/3² = 1/9 ≈ 0.111

**Interpretation:** At most 11.1% of observations fall beyond 3 standard deviations from the mean. In practice, for many distributions, this percentage is much smaller.

### Example 3: Central Limit Theorem Application

**Problem:** A cloud server handles independent tasks. Each task's execution time (in milliseconds) is uniformly distributed on [50, 150] with mean μ = 100 and variance σ² = (150-50)²/12 = 10000/12 ≈ 833.33.

For n = 64 tasks, find the probability that the average execution time exceeds 105 milliseconds.

**Solution:**

Step 1: Identify parameters
- Original distribution: Uniform[50, 150]
- For Uniform[a,b]: μ = (a+b)/2 = 100, σ² = (b-a)²/12 = 833.33
- n = 64
- Standard error: σ/√n = √833.33/8 ≈ 28.87/8 ≈ 3.61

Step 2: Apply CLT
X̄₆₄ ~ approximately N(μ, σ²/n) = N(100, 3.61²) = N(100, 13.03)

Step 3: Standardize
P(X̄ > 105) = P(Z > (105 - 100)/3.61) = P(Z > 1.39)

Step 4: Use standard normal table
P(Z > 1.39) ≈ 0.0823

**Interpretation:** Approximately 8.23% of the time, the average execution time for 64 tasks will exceed 105 ms. This approximation is valid because n = 64 ≥ 30 satisfies the CLT requirements.

## Exam Tips

1. **Memorize the formulas exactly:** Markov: P(X ≥ a) ≤ E(X)/a; Chebyshev: P(|X - μ| ≥ kσ) ≤ 1/k²; CLT: X̄ₙ ~ N(μ, σ²/n) for large n.

2. **Check conditions before applying:** Markov requires X ≥ 0; Chebyshev requires finite mean and variance; CLT requires i.i.d. variables with finite variance.

3. **Understand the direction of inequalities:** Markov and Chebyshev give upper bounds only, not exact probabilities.

4. **CLT approximation rule of thumb:** Use CLT when n ≥ 30; the approximation improves with larger n.

5. **Standardization is essential:** For CLT problems, always standardize using Z = (X̄ - μ)/(σ/√n) before using the standard normal table.

6. **Variance of sample mean:** Remember Var(X̄ₙ) = σ²/n—this is crucial for CLT and WLLN problems.

7. **Chebyshev vs. Empirical Rule:** For normal distributions, Chebyshev bounds are conservative (e.g., empirical rule says ~5% beyond 2σ, Chebyshev says ≤25%).

8. **WLLN is a consequence of Chebyshev:** Understand this connection as it frequently appears in proofs.