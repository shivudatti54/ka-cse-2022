# Exponential Distribution - Summary

## Key Definitions and Concepts

- **Exponential Distribution**: A continuous probability distribution modeling the time between independent events occurring at a constant average rate λ.

- **Probability Density Function**: f(x) = λe^(-λx) for x ≥ 0, where λ > 0 is the rate parameter.

- **Cumulative Distribution Function**: F(x) = 1 - e^(-λx) for x ≥ 0

- **Memoryless Property**: P(X > s + t | X > s) = P(X > t) = e^(-λt)—the probability of future waiting time is independent of past waiting.

- **Poisson-Exponential Relationship**: If events occur according to a Poisson process with rate λ, the inter-arrival time follows Exp(λ).

## Important Formulas and Theorems

| Parameter | Formula |
|-----------|---------|
| Mean (Expected Value) | E[X] = 1/λ |
| Variance | Var(X) = 1/λ² |
| Standard Deviation | σ = 1/λ |
| CDF | F(x) = 1 - e^(-λx) |
| Survival Function | P(X > x) = e^(-λx) |
| Memoryless Property | P(X > s + t \| X > s) = e^(-λt) |

## Key Points

- The Exponential Distribution is defined only for non-negative values (x ≥ 0).

- The rate parameter λ must be positive; higher λ means events occur more frequently (shorter average wait time).

- The mean equals the standard deviation—a unique property among common distributions.

- The memoryless property makes the exponential distribution suitable for modeling waiting times in systems without aging.

- It serves as the continuous analogue of the discrete Geometric Distribution.

- The hazard function (failure rate) is constant at λ, indicating that the risk of failure does not change with time.

## Common Mistakes to Avoid

1. **Confusing λ**: Remember λ is the rate (events per unit time), not the mean. If mean = 10, then λ = 0.1, not 10.

2. **Ignoring domain**: The exponential distribution is defined only for x ≥ 0. Always check your calculations.

3. **Memoryless misinterpretation**: The memoryless property applies to remaining wait time, not total wait time.

4. **Using wrong formula**: Distinguish between P(X ≤ x) = 1 - e^(-λx) and P(X > x) = e^(-λx).

## Revision Tips

1. **Practice probability calculations**: Work through several problems computing P(X < x), P(X > x), and conditional probabilities.

2. **Understand the memoryless property**: This is the defining characteristic of exponential distribution—explain it in your own words.

3. **Connect to Poisson**: Remember: Poisson counts events in a fixed interval; Exponential measures time between events.

4. **Memorize relationships**: Mean = 1/λ, Variance = 1/λ², Standard Deviation = Mean. These three should be instantly recallable.

5. **Solve applied problems**: Practice word problems from reliability engineering and queuing theory to reinforce concepts.