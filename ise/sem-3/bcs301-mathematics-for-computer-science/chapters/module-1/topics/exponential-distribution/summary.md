# Exponential Distribution - Summary

## Key Definitions and Concepts

- **Exponential Distribution**: A continuous probability distribution modeling the time between events in a Poisson process. X ~ Exp(λ) with λ > 0 as the rate parameter.

- **PDF**: f(x) = λe^(-λx) for x ≥ 0, and f(x) = 0 for x < 0

- **CDF**: F(x) = P(X ≤ x) = 1 - e^(-λx) for x ≥ 0

- **Complement**: P(X > x) = e^(-λx)

## Important Formulas and Theorems

- **Mean**: E[X] = 1/λ

- **Variance**: Var(X) = 1/λ²

- **Standard Deviation**: σ = 1/λ (equals the mean)

- **Memoryless Property**: P(X > s + t | X > s) = P(X > t) for all s, t ≥ 0

- **Hazard Function**: h(x) = λ (constant)

- **Relationship with Poisson**: Inter-arrival times in Poisson(λ) process follow Exp(λ)

## Key Points

- The exponential distribution models waiting times between random events occurring independently at a constant average rate

- It is the ONLY continuous distribution with the memoryless property—future probability is independent of past elapsed time

- The rate parameter λ represents the average number of events per unit time; mean waiting time = 1/λ

- Mean equals standard deviation, making dispersion easy to characterize

- The hazard (failure) rate is constant, implying no aging or wear effects—suitable for random failures

- Closely connected to Poisson distribution: if events follow Poisson process, inter-arrival times are exponential

- Used extensively in queuing theory, reliability engineering, and survival analysis

## Common Mistakes to Remember

- Confusing the rate parameter λ with the scale parameter (sometimes θ = 1/λ is used)

- Forgetting to check that x ≥ 0 in the exponential distribution—probability is zero for negative values

- Mixing units: ensure λ and x use the same time unit

- Using variance formula incorrectly—remember Var = 1/λ², not λ²

- Applying memoryless property to problems involving specific distributions without checking assumptions

## Revision Tips

- Practice computing probabilities using both F(x) and e^(-λx) forms until comfortable

- Memorize the memoryless property formula—it appears frequently in exam questions

- Work through at least 3-4 word problems covering different application areas

- Remember the mean-variance relationship: knowing mean immediately gives variance

- Review the Poisson-exponential connection as it frequently appears in applied problems