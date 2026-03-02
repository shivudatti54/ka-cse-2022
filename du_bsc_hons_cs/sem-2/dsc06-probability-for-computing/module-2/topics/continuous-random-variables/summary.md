# Continuous Random Variables - Summary

## Key Definitions and Concepts

- **Continuous Random Variable**: A random variable that can take any value within an interval (real numbers), with probabilities assigned to intervals rather than individual values.

- **Probability Density Function (PDF)**: A non-negative function f(x) where P(a ≤ X ≤ b) = ∫[a to b] f(x) dx. Must satisfy: f(x) ≥ 0 and ∫[-∞ to ∞] f(x) dx = 1.

- **Cumulative Distribution Function (CDF)**: F(x) = P(X ≤ x) = ∫[-∞ to x] f(t) dt. Relationship: f(x) = d/dx F(x).

- **Key Property**: For continuous variables, P(X = c) = 0 for any specific value c.

## Important Formulas and Theorems

| Distribution | PDF | Mean | Variance |
|--------------|-----|------|----------|
| Uniform U(a,b) | 1/(b-a) for a≤x≤b | (a+b)/2 | (b-a)²/12 |
| Exponential Exp(λ) | λe^(-λx) for x≥0 | 1/λ | 1/λ² |
| Normal N(μ,σ²) | (1/(σ√2π))e^(-(x-μ)²/(2σ²)) | μ | σ² |

**Z-score transformation**: Z = (X - μ)/σ transforms N(μ,σ²) to N(0,1)

## Key Points

1. Continuous random variables assign zero probability to exact values; all probability lies in intervals.

2. The PDF f(x) at a point does not represent probability—it must be integrated over a range.

3. A PDF can exceed 1 at certain points; only the integral over the entire domain equals 1.

4. Exponential distribution has the unique memoryless property: P(X > s+t | X > s) = P(X > t).

5. Normal distribution is symmetric and bell-shaped; the empirical rule covers 68-95-99.7% within 1-2-3 standard deviations.

6. Standard normal transformation is essential for using z-tables to compute normal probabilities.

7. The CDF is always non-decreasing, ranges from 0 to 1, and is right-continuous.

## Common Mistakes to Avoid

- **Treating PDF like PMF**: Remember f(x) is not P(X = x)—it's a density that must be integrated.

- **Ignoring domain of definition**: PDFs are often zero outside certain intervals; always check the support of the distribution.

- **Forgetting to standardize**: When solving normal distribution problems, always convert to standard normal before using tables.

- **Confusing mean and variance**: For exponential, mean = 1/λ but variance = 1/λ²—these are different.

## Revision Tips

1. Practice converting between PDF and CDF by both differentiation and integration.

2. Memorize the formulas for mean and variance of the three key distributions (uniform, exponential, normal).

3. Solve at least 5 problems each on exponential and normal distributions focusing on probability calculations.

4. Understand why P(X = c) = 0 for continuous variables—this is a fundamental concept that distinguishes them from discrete variables.

5. Review the memoryless property and be able to state and prove it for exponential distributions.