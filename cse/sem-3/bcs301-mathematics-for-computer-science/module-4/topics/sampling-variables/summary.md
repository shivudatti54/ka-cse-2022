# Sampling Variables Revision Notes

## Overview of Sampling Variables

#### Definitions:

- **Population**: The complete set from which samples are drawn.
- **Sample**: A subset or sample drawn from a population.
- **Sampling Variable (Random Variable)**: A variable whose values represent measurements on the sampled items.

### Types of Random Variables in Sampling

1. **Binary Random Variables**:
   - Represent binary outcomes, e.g., success/failure.
   - Formula: \( p \) and \( q = 1-p \)

2. **Discrete Uniform Random Variable**:
   - Values are equally likely within a discrete set (e.g., roll of a die).
   - Formula: \( P(X=k) = \frac{1}{n} \), where \( n \) is the number of outcomes.

3. **Continuous Random Variable**:
   - Takes on any value in an interval.
   - Examples include heights, weights.
   - Probability Distribution Function (PDF):
     - Formula: \( f(x) \)
   - Cumulative Distribution Function (CDF):
     - Formula: \( F(x) = P(X \leq x) = \int\_{-\infty}^{x} f(t) dt \)

4. **Normal Random Variable**:
   - Bell-shaped curve distribution.
   - Empirical Rule (68-95-99.7 rule):
     - Approximately 68% of the data lies within one standard deviation (\( \sigma \)) of the mean (\( \mu \)).
     - Approximately 95% within two standard deviations.
     - Approximately 99.7% within three standard deviations.

### Important Theorems and Concepts

- **Law of Large Numbers**: As sample size increases, the sample mean approaches the population mean (expected value).

- **Central Limit Theorem**:
  - For a sufficiently large sample size, regardless of the underlying distribution of the population, the sampling distribution of the mean will be approximately normally distributed.

## Key Formulas for Statistical Inference

### Expected Value and Variance

- **Expected Value (Mean)**: \( E(X) = \mu \)
- **Variance**: \( Var(X) = \sigma^2 \)

### Standard Deviation:

- \( \sigma = \sqrt{Var(X)} \)

### Confidence Intervals for Population Mean

- For a large sample size, assuming the population is normally distributed or with a sufficiently large sample size:
  - Point estimate: \( \bar{x} \)
  - Standard error of the mean (SEM): \( SE\_{\bar{x}} = \frac{\sigma}{\sqrt{n}} \)

  - Confidence Interval:
    - Formula: \( \bar{x} \pm z^\* \cdot SE\_{\bar{x}} \)

- For smaller samples or unknown population standard deviation:
  - Use the t-distribution instead of the Z-distribution.

### Hypothesis Testing for Population Mean

- Null hypothesis (\( H_0 \)) vs. Alternative hypothesis (\( H_a \)).
- Test statistic (Z-test or t-test depending on sample size and distribution assumptions).
- Compare test statistic to critical value from standard normal (for Z-tests) or t-distribution.

### Sample Size Calculation for Estimating Mean

- Formula: \( n = \left(\frac{z\_{\alpha/2} \cdot \sigma}{E}\right)^2 \)

Where:

- \( z\_{\alpha/2} \): The critical value from the standard normal distribution.
- \( \sigma \): Population standard deviation (or estimated population standard deviation in case of unknown).
- \( E \): Precision or margin of error.

---

This summary provides a concise overview and key points for sampling variables, their types, formulas, and important statistical concepts. It’s tailored to aid quick revision before exams in the context of Statistical Inference 2 within Mathematics for Computer Science.
