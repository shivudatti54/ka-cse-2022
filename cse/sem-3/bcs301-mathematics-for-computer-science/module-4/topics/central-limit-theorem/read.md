## Table of Contents

- [Central Limit Theorem & Confidence Limits for Unknown Mean](#central-limit-theorem--confidence-limits-for-unknown-mean)
  - [1. Introduction](#1-introduction)
  - [2. Core Concepts](#2-core-concepts)
  - [3. Example](#3-example)
  - [4. Key Points & Summary](#4-key-points--summary)

## Central Limit Theorem & Confidence Limits for Unknown Mean

### 1. Introduction

In the previous module, you learned about point estimation. But how confident can we be in a single sample mean? Statistical inference provides the tools to quantify this uncertainty. Two of the most powerful concepts in this domain are the **Central Limit Theorem (CLT)** and **Confidence Intervals**. Together, they allow computer scientists and data engineers to make reliable inferences about a population (e.g., all users, all transactions) based on a single, relatively small sample (e.g., a sampled dataset).

### 2. Core Concepts

#### The Central Limit Theorem (CLT)

The CLT is the statistical foundation that enables us to use the normal distribution for inference, even when the underlying population distribution is not normal.

**Definition:** If you take sufficiently large random samples from _any_ population with a mean µ and finite variance σ², the distribution of the sample means (`x̄`) will be approximately normally distributed.

This holds true _regardless of the shape of the original population's distribution_ (be it skewed, exponential, uniform, etc.).

**Key Conditions and Implications:**

- **Sample Size (n):** The sample must be "sufficiently large." A common rule of thumb is `n ≥ 30`. For highly skewed distributions, a larger `n` might be needed.
- **Mean of Sample Means:** The mean of the sampling distribution of `x̄` will be equal to the population mean, µ.
- **Standard Error (SE):** The standard deviation of the sampling distribution of `x̄` is called the **standard error**. It is calculated as:
  `SE = σ / √n`
  where `σ` is the population standard deviation. This formula shows that as sample size `n` increases, the variation (error) in our sample means decreases.

**Why is this crucial for Computer Science?**
When analyzing metrics like app load times, API response latencies, or user engagement scores—which are often not normally distributed—the CLT guarantees that if we repeatedly sample this data, the _mean_ of those samples will form a normal distribution. This allows us to apply all the powerful techniques based on the normal curve.

#### Confidence Intervals for an Unknown Mean (µ)

A point estimate (like a single sample mean, `x̄`) gives us one number for the population mean, µ. A confidence interval provides a range of values that is likely to _contain_ the true population mean µ with a specified level of confidence.

**The 95% Confidence Interval Formula (when σ is known):**
This is the most common case derived directly from the CLT. The formula for a confidence interval is:
`CI = x̄ ± Z_(α/2) * (σ / √n)`

Where:

- `x̄` (x-bar) is the sample mean.
- `Z_(α/2)` is the **Z-critical value** from the standard normal distribution. For a 95% confidence level, α (alpha) is 0.05. Therefore, α/2 = 0.025. The Z-value for which P(Z < z) = 0.975 is `1.96`.
- `σ / √n` is the standard error (SE).

**Interpretation:** It is incorrect to say "there is a 95% probability that the population mean lies within this interval." The correct interpretation is: "If we were to take many random samples and construct a confidence interval from each sample, we would expect about 95% of those intervals to contain the true population mean µ."

**What if σ is unknown? (The More Common Case)**
In reality, we almost never know the population standard deviation σ. In this case, we use the **t-distribution** instead of the Z-distribution.

- We estimate σ using the **sample standard deviation (`s`)**.
- We use the **t-critical value (`t_(α/2, n-1)`)** from the t-distribution with `n-1` degrees of freedom. The t-distribution is similar to the normal distribution but has heavier tails, accounting for the extra uncertainty introduced by estimating σ.

The formula becomes:
`CI = x̄ ± t_(α/2, n-1) * (s / √n)`

As the sample size `n` increases, the t-distribution converges to the standard normal distribution.

### 3. Example

Let's say you are a data engineer analyzing the response time of a new database query. You don't know the true population mean (µ) or standard deviation (σ).

- You take a random sample of `n = 40` queries.
- Your sample has a mean response time `x̄ = 152 ms`.
- Your sample has a standard deviation `s = 28 ms`.

You want to construct a 95% confidence interval for the true mean response time.

1. Since `n=40` (≥30), the CLT applies, and the sampling distribution is approximately normal.
2. Since σ is unknown, we use the t-distribution.
3. Degrees of Freedom (df) = n - 1 = 39.
4. The t-critical value for 95% confidence and 39 df is approximately `t = 2.023` (you would look this up in a t-table or use a software function).
5. Calculate the Standard Error: `SE = s / √n = 28 / √40 ≈ 4.42`
6. Calculate the Margin of Error (MOE): `MOE = t * SE = 2.023 * 4.42 ≈ 8.95`
7. Construct the Interval: `CI = 152 ± 8.95`

Therefore, the 95% confidence interval is **(143.05 ms, 160.95 ms)**. We are 95% confident that the true mean response time for all queries lies between 143.05 and 160.95 milliseconds.

### 4. Key Points & Summary

- **Central Limit Theorem (CLT):** The superhero of statistics. It states that the sampling distribution of the mean approaches normality as sample size increases, regardless of the population's shape. This allows for inference.
- **Standard Error (SE):** `σ/√n` or `s/√n`. It measures the variability of sample means around the true population mean. Larger `n` leads to a smaller SE and a more precise estimate.
- **Confidence Interval:** A range of values, constructed from sample data, that is likely to contain an unknown population parameter. It provides an estimate _with a margin of error_.
- **Choosing the Right Distribution:**
- Use the **Z-distribution** if the population standard deviation **σ is known**.
- Use the **t-distribution** if **σ is unknown** and you must estimate it with the sample standard deviation `s`. This is the far more common scenario in real-world computer science applications.
- **Width of the Interval:** The width of the confidence interval is affected by sample size (`n`) and variability (`s` or `σ`). To get a more precise (narrower) interval, you can either reduce variability or, more practically, increase your sample size.
