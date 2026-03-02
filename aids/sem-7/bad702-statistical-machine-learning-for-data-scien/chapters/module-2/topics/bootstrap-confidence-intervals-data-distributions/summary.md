# **Bootstrap, Confidence Intervals, Data Distributions**

### Bootstrap Method

- Bootstrap sampling: resampling with replacement from original dataset
- Purpose: estimate variability and uncertainty in estimates
- Formula: `CI = (x̄ - SE, x̄ + SE)` where `x̄` is sample mean and `SE` is standard error
- Theorem: Bootstrap distribution is asymptotically normal

### Confidence Intervals

- Confidence interval: range of values within which a population parameter is likely to lie
- Formula: `CI = (x̄ - Zα/2 \* (σ/n), x̄ + Zα/2 \* (σ/n))` where `x̄` is sample mean, `σ` is population standard deviation, `n` is sample size, and `Zα/2` is critical value from standard normal distribution
- Types:
  - Interval estimation
  - Hypothesis testing

### Data Distributions

- **Normal Distribution**
  - Formula: `f(x) = (1/√(2πσ^2)) \* e^(-((x-μ)^2)/(2σ^2))`
  - Definition: bell-shaped curve with mean `μ` and standard deviation `σ`
  - Theorem: Central Limit Theorem (CLT)
- **Long-Tailed Distribution**
  - Formula: `f(x) = (1/2πσ^2) \* e^(-x/σ)` where `σ` is scale parameter
  - Definition: skewed distribution with heavy tails
  - Examples: Exponential, Gamma, Pareto distributions
- **Student's-t Distribution**
  - Formula: `f(x) = (1/√(2πσ^2)) \* (x/σ)^{(n-1)/2} \* e^(-x^2/(2σ^2(n-1)))`
  - Definition: skewed distribution with degrees of freedom `n-1`
  - Theorem: Studentized range distribution

### Specialized Distributions

- **Binomial Distribution**
  - Formula: `P(X=k) = (nCk) \* p^k \* (1-p)^(n-k)` where `n` is number of trials, `k` is number of successes, and `p` is probability of success
  - Definition: discrete distribution of number of successes in fixed number of trials
- **Chi-Square Distribution**
  - Formula: `f(x) = (1/2^(n/2)) \* (x^(n/2-1)) \* e^(-x/2)` where `n` is number of degrees of freedom
  - Definition: skewed distribution of sum of squares
- **F Distribution**
  - Formula: `f(x) = (1/((n1-1) \* (n2-1) \* Γ(n1/2) \* Γ(n2/2))) \* x^(n1/2-1) \* (1/x)^{(n2-1)/2}` where `n1` and `n2` are degrees of freedom
  - Definition: ratio of chi-square distributions
- **Poisson Distribution**
  - Formula: `P(X=k) = (e^(-λ) \* (λ^k))/k!` where `λ` is mean and `k` is number of occurrences
  - Definition: discrete distribution of number of occurrences in fixed interval of time or space

### Related Distributions

- **Gamma Distribution**
  - Formula: `f(x) = (1/Γ(α) \* x^(α-1)) \* e^(-x/β)` where `α` is shape parameter and `β` is scale parameter
  - Definition: continuous distribution of sum of exponential random variables
- **Weibull Distribution**
  - Formula: `f(x) = (1/β) \* (x/β)^((α-1)/α) \* e^(-(x/β)^α)` where `α` is shape parameter and `β` is scale parameter
  - Definition: continuous distribution of time to failure
