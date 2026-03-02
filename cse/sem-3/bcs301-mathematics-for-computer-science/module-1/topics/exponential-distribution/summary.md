# Exponential Distribution - Summary

## Key Definitions

- **Exponential Distribution**: A continuous probability distribution modeling the time between independent events occurring at constant average rate λ

- **Rate Parameter (λ)**: The average number of events per unit time; λ > 0

- **Memoryless Property**: P(X > s + t | X > s) = P(X > t) - the probability of additional waiting time is independent of past waiting

## Important Formulas

- **PDF**: f(x) = λe^(-λx) for x ≥ 0
- **CDF**: F(x) = 1 - e^(-λx) for x ≥ 0
- **Mean**: E[X] = 1/λ
- **Variance**: Var(X) = 1/λ²
- **Standard Deviation**: σ = 1/λ
- **P(X > x)**: e^(-λx)
- **P(s < X < t)**: e^(-λs) - e^(-λt)

## Key Points

1. The exponential distribution is continuous, defined only for x ≥ 0

2. The mean (1/λ) represents the average time between events; larger λ means smaller mean inter-arrival time

3. The memoryless property is unique to exponential distribution among continuous distributions

4. Exponential and Poisson are duals: Poisson counts events in fixed time; Exponential measures time between events

5. If N(t) ~ Poisson(λt), then inter-arrival times follow Exponential(λ)

6. In queuing theory (M/M/1), utilization ρ = λ/μ must be < 1 for stability

7. The exponential distribution is closely related to the geometric distribution (its discrete counterpart) through the memoryless property

8. In reliability engineering, λ often represents failure rate; higher λ means less reliable systems

## Common Mistakes

1. **Confusing λ with its reciprocal**: Remember mean = 1/λ, not λ itself

2. **Forgetting the domain**: Exponential distribution is defined only for x ≥ 0; for x < 0, f(x) = 0

3. **Ignoring unit conversion**: Failing to convert between seconds/minutes/hours when λ is given in different units than the time asked

4. **Not applying memoryless property**: Trying to calculate P(X > t | X > s) by computing from time zero instead of using the memoryless property

5. **Using wrong formula for intervals**: For P(s < X < t), some students incorrectly use e^(-λ(t-s)) instead of e^(-λs) - e^(-λt)