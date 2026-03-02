# Discrete Random Variables - Summary

## Key Definitions and Concepts

- **Discrete Random Variable**: A variable that takes only countable, distinct values (finite or countably infinite), as opposed to continuous values.

- **Probability Mass Function (PMF)**: pX(x) = P(X = x), giving probability for each discrete value. Must satisfy pX(x) ≥ 0 and ΣpX(x) = 1.

- **Cumulative Distribution Function (CDF)**: FX(x) = P(X ≤ x), a step function for discrete variables that jumps at each possible value.

- **Expected Value (Mean)**: E[X] = Σ x·pX(x), representing the long-run average.

- **Variance**: Var(X) = E[(X - μ)²] = E[X²] - (E[X])², measuring spread around the mean.

- **Standard Deviation**: σ = √Var(X), in original units.

## Important Formulas and Theorems

| Distribution | PMF | E[X] | Var(X) |
|--------------|-----|------|--------|
| Bernoulli(p) | p^k (1-p)^(1-k) | p | p(1-p) |
| Binomial(n,p) | C(n,k)p^k(1-p)^(n-k) | np | np(1-p) |
| Poisson(λ) | e^(-λ)λ^k/k! | λ | λ |
| Geometric(p) | (1-p)^(k-1)p | 1/p | (1-p)/p² |

**Key Properties**:
- E[aX + b] = aE[X] + b
- Var(aX + b) = a²Var(X)
- E[X + Y] = E[X] + E[Y]

## Key Points

- Discrete random variables model countable events in computing: packet losses, queue lengths, bug counts, search results.

- The Poisson distribution approximates Binomial when n is large, p is small, and np = λ is constant.

- The CDF for discrete variables is right-continuous and non-decreasing, with jumps equal to PMF values.

- Variance is always non-negative; standard deviation provides interpretable measure of spread.

- Geometric distribution is memoryless: P(X > m+n | X > m) = P(X > n).

## Common Mistakes to Avoid

1. **Forgetting normalization**: Always verify Σp(x) = 1 before calculating probabilities.

2. **Confusing discrete and continuous**: Discrete variables use PMF and summations; continuous use PDF and integrals.

3. **CDF boundary errors**: P(X < a) vs P(X ≤ a) are different for discrete—remember to check inclusive/exclusive.

4. **Incorrect variance formula**: Using Var(X) = E[X]² - E[X²] instead of the correct E[X²] - (E[X])².

## Revision Tips

1. Practice identifying which distribution applies to given scenarios—this is the most important skill.

2. Work through at least 3-4 problems from each distribution type before the exam.

3. Create a table summarizing all four distributions with their parameters, formulas, means, and variances.

4. Memorize the relationship: Binomial → Poisson (large n, small p) → Normal (large λ).

5. Use the "indicator variable" technique: Represent complex problems as sum of simpler Bernoulli variables to use linearity of expectation.