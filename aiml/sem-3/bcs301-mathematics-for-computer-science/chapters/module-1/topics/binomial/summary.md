# Binomial

### Definition and Notation

- A binomial distribution is a discrete probability distribution of the number of successes in a sequence of `n` independent trials, each with a probability `p` of success.
- Random variable `X` represents the number of successes.
- Notation: `X ~ Bin(n, p)`

### Parameters

- `n`: number of trials
- `p`: probability of success on each trial
- `q = 1 - p`: probability of failure on each trial

### Formulas

- Probability mass function (PMF): `P(X = k) = (n choose k) * p^k * q^(n-k)`, where `k = 0, 1, ..., n`
- Expected value: `E(X) = np`
- Variance: `Var(X) = npq`

### Key Theorems

- **Binomial Theorem**: `(a + b)^n = ∑(n choose k) * a^k * b^(n-k)`
- **Binomial Probabilities**: `P(X = k) = P(X = n-k)`
- **Independence**: `P(X = k1, X = k2) = P(X = k1) * P(X = k2)`, if trials are independent

### Important Formulas

- `P(X ≤ k) = ∑[i=0 to k] (n choose i) * p^i * q^(n-i)`
- `Z = (X - np) / sqrt(npq)`, standardized random variable

### Revision Tips

- Understand the concept of independent trials and the relationship between `p` and `q`.
- Learn the formulas for PMF, expected value, and variance.
- Familiarize yourself with the binomial theorem and its applications.
- Practice calculating probabilities and using the formulas to solve problems.
