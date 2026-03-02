# Binomial

### Definitions and Notations

- **Binomial Distribution**: A discrete probability distribution of the number of successes in a sequence of `n` independent trials, where the probability of success at each trial is `p`.
- **Binomial Coefficient**: `nCr = n! / (r!(n-r)!)`, representing the number of ways to choose `r` successes from `n` trials.
- **Random Variable**: `X`, which represents the number of successes.

### Formulas and Theorems

- **Probability Mass Function (PMF)**: `P(X=k) = (nCk) \* p^k \* (1-p)^(n-k)`
- **Mean**: `μ = np`
- **Variance**: `σ^2 = np(1-p)`
- **Standard Deviation**: `σ = √(np(1-p))`
- **Chebyshev's Inequality**: `P(|X-μ| ≥ kσ) ≤ 1/k^2`

### Key Properties

- **Independence**: Trials are independent, meaning the outcome of one trial does not affect the outcome of another.
- **Memoryless**: The probability of success does not change over time.
- **Symmetry**: If `p = 0.5`, then `X` follows a symmetric binomial distribution.

### Important Results

- **Binomial Theorem**: `(a + b)^n = Σ (nCk) \* a^(n-k) \* b^k`, where `nCk` represents the binomial coefficient.
- **Binomial Test**: Used to test the null hypothesis that the probability of success is `p`, given a sample of `n` trials with `k` successes.

### Applications

- **Coin Tosses**: Modeling the probability of getting heads or tails in a sequence of coin tosses.
- **Medical Trials**: Estimating the effectiveness of a treatment or intervention.
- **Quality Control**: Monitoring the number of defects in a manufactured product.
