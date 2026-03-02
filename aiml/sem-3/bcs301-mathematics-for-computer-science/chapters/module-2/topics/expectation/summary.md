# Expectation - Summary

## Key Definitions and Concepts

- **Expected Value (E[X])**: The long-run average value of a random variable. For discrete X: E[X] = Σ x·P(X=x). For continuous X: E[X] = ∫ x·f(x)dx.

- **Variance (Var(X))**: Measures dispersion around the mean: Var(X) = E[(X - E[X])²] = E[X²] - (E[X])²

- **Standard Deviation**: σ = √Var(X)

- **Covariance**: Joint variability of two variables: Cov(X,Y) = E[XY] - E[X]E[Y]

- **Law of Total Expectation**: E[E[X|Y]] = E[X]

## Important Formulas and Theorems

- Linearity: E[aX + bY] = aE[X] + bE[Y]
- Constant: E[c] = c
- Product (independence): E[XY] = E[X]E[Y] when X and Y are independent
- Function of random variable: E[g(X)] = Σ g(x)·P(X=x) for discrete case

## Key Points

- Expectation represents the theoretical mean of a probability distribution

- Linearity of expectation is the most powerful property and does NOT require independence

- Variance can be computed efficiently using E[X²] - (E[X])²

- Zero covariance implies uncorrelated, NOT necessarily independent

- For joint distributions, compute marginal expectations by summing over all values of the other variable

- The tower property E[E[X|Y]] = E[X] is crucial for conditional expectation problems

- An expectation may not exist if the corresponding sum/integral diverges

## Common Mistakes to Avoid

- Confusing E[X] with the most likely value (mode) — they are different concepts

- Forgetting that Var(X) = E[X²] - (E[X])² requires computing E[X²], not just E[X]

- Assuming zero covariance implies independence (correlation does not imply causation)

- Not checking whether expectation exists before attempting to compute it

## Revision Tips

- Practice computing E[X] for common distributions: Uniform, Binomial, Poisson, Exponential

- Memorize that E[X²] = Var(X) + (E[X])² — this rearangement is frequently useful

- Work through joint distribution problems to master double summation in expectation

- Remember that linearity applies to sums of any number of random variables