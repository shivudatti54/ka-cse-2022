# Test of Significance for Means of Two Small Samples

## Table of Contents

- [Test of Significance for Means of Two Small Samples](#test-of-significance-for-means-of-two-small-samples)
- [1. Introduction](#1-introduction)
- [2. Core Concepts](#2-core-concepts)
  - [Student's t-Distribution](#students-t-distribution)
  - [Assumptions for the Test](#assumptions-for-the-test)
  - [The Hypothesis](#the-hypothesis)
  - [The Test Statistic](#the-test-statistic)
- [3. Example: Comparing Algorithm Efficiency](#3-example-comparing-algorithm-efficiency)
- [4. Key Points & Summary](#4-key-points--summary)

## 1. Introduction

In statistical inference, we often need to compare the means of two different groups or processes. For instance, a computer scientist might want to compare the average execution time of two different algorithms, or the average throughput of two network protocols. When the sample sizes are large (`n > 30`), we can use the **Z-test** based on the normal distribution. However, in practical engineering and computer science experiments, data is often scarce and expensive to collect, leading to **small sample sizes** (`n < 30`). For these cases, we use the **t-test**, which is more reliable for small samples as it accounts for the extra uncertainty in estimating the population variance.

## 2. Core Concepts

### Student's t-Distribution

The t-distribution is a probability distribution similar to the normal distribution but with heavier tails. This makes it more prone to producing values that fall far from its mean, which is a crucial property when dealing with the uncertainty of small samples. The shape of the t-distribution depends on its **degrees of freedom (df)**. For a two-sample test, the degrees of freedom are typically `df = n1 + n2 - 2`.

### Assumptions for the Test

Before applying the t-test for two small samples, certain assumptions must be met:

1. **Samples are drawn from Normal Populations:** The data for both groups should be approximately normally distributed.
2. **Samples are Independent:** The two samples must be independent of each other (e.g., response times from two separate, unrelated algorithms).
3. **Population Variances are Equal:** This is a key assumption for the standard test (`σ1² = σ2²`). We assume the variability within both populations is the same, even if their means are different.

### The Hypothesis

We test the **null hypothesis (H₀)** that there is no significant difference between the means of the two populations against an **alternative hypothesis (H₁)**.

- **H₀:** μ₁ = μ₂ (The means are equal)
- **H₁:** μ₁ ≠ μ₂ (Two-tailed test: means are not equal)
- H₁ can also be μ₁ > μ₂ or μ₁ < μ₂ for a one-tailed test.

### The Test Statistic

The test statistic for comparing two small sample means, under the assumption of equal variances, is calculated as:

**t =** `(x̄₁ - x̄₂) / (S_p * √(1/n₁ + 1/n₂))`

Where:

- `x̄₁` and `x̄₂` are the sample means.
- `n₁` and `n₂` are the sample sizes.
- `S_p` is the **pooled standard deviation**, a weighted average of the two sample standard deviations. It is calculated as:

**S_p² =** `((n₁ - 1)S₁² + (n₂ - 1)S₂²) / (n₁ + n₂ - 2)`

Here, `S₁²` and `S₂²` are the sample variances.

We then compare the calculated `t` value with the critical `t` value from the t-distribution table at `(n₁+n₂-2)` degrees of freedom and a chosen **level of significance (α)**, commonly 5% (0.05).

## 3. Example: Comparing Algorithm Efficiency

A developer has designed a new sorting algorithm (Algorithm B) and wants to compare its average run-time against the standard algorithm (Algorithm A). They run each algorithm on 10 different random datasets and record the run-time (in ms).

**Data:**

- **Algorithm A (n₁=10):** Mean (`x̄₁`) = 22.5 ms, Variance (`S₁²`) = 15.2
- **Algorithm B (n₂=10):** Mean (`x̄₂`) = 19.5 ms, Variance (`S₂²`) = 12.8

**Step 1: State the Hypothesis**

- H₀: μ_A = μ_B (The new algorithm is not faster)
- H₁: μ_A > μ_B (One-tailed test: The standard algorithm A is slower)

**Step 2: Calculate Pooled Variance (S_p²)**
`S_p² = ((10 - 1)*15.2 + (10 - 1)*12.8) / (10 + 10 - 2)`
`S_p² = (9*15.2 + 9*12.8) / 18 = (136.8 + 115.2) / 18 = 252 / 18 = 14.0`
`S_p = √14.0 ≈ 3.74`

**Step 3: Calculate the t-statistic**
`t = (22.5 - 19.5) / (3.74 * √(1/10 + 1/10))`
`t = 3.0 / (3.74 * √0.2) = 3.0 / (3.74 * 0.447) ≈ 3.0 / 1.67 ≈ 1.80`

**Step 4: Determine the Critical Value**
For a one-tailed test at α=0.05 and degrees of freedom `df = 10+10-2=18`, the critical value from the t-table is `t_critical ≈ 1.734`.

**Step 5: Make a Decision**
Since the calculated `t (1.80)` is **greater than** the critical value `(1.734)`, we **reject the null hypothesis (H₀)**.

**Conclusion:** There is sufficient evidence at the 5% significance level to conclude that the new Algorithm B has a faster average run-time than the standard Algorithm A.

## 4. Key Points & Summary

- **Purpose:** The t-test for two small samples is used to determine if there is a statistically significant difference between the means of two independent groups when sample sizes are small (`n < 30`).
- **Assumptions are Key:** The test relies on the assumptions of normality, independence, and equal population variances. Violating these can lead to incorrect conclusions.
- **Test Statistic:** It uses a pooled estimate of the variance to account for the uncertainty inherent in small samples, resulting in a test statistic that follows a t-distribution.
- **Decision Rule:** Compare the calculated `t`-value against the critical `t`-value from the table. If `|t_calculated| > t_critical`, reject H₀.
- **Engineering Application:** This test is invaluable in computer science for A/B testing, performance benchmarking, algorithm analysis, and any scenario where you need to compare two systems or methods with limited data.

**Remember:** Statistical significance does not always imply practical significance. Always consider the context and the magnitude of the difference observed.
