# Test of Significance for Large Samples

## Table of Contents

- [Test of Significance for Large Samples](#test-of-significance-for-large-samples)
- [1. Introduction](#1-introduction)
- [2. Core Concepts](#2-core-concepts)
  - [The Null and Alternative Hypotheses](#the-null-and-alternative-hypotheses)
  - [Level of Significance (`α`)](#level-of-significance-)
  - [Test Statistic (`Z`)](#test-statistic-z)
  - [Steps in Testing a Hypothesis (Procedure)](#steps-in-testing-a-hypothesis-procedure)
- [3. Example: Test for Single Mean](#3-example-test-for-single-mean)
- [4. Key Points & Summary](#4-key-points--summary)

## 1. Introduction

In the realm of statistical inference, we often need to make decisions or draw conclusions about a population based on sample data. A **test of significance** is a formal procedure used to determine whether a claim (or hypothesis) about a population parameter (like mean or proportion) is supported by the evidence from the sample data. When the sample size is large (typically `n > 30`), the sampling distributions of many statistics (like the mean) tend to follow a normal distribution due to the **Central Limit Theorem**. This allows us to use the standard normal variate `Z` for testing hypotheses, making the procedure robust and relatively straightforward.

## 2. Core Concepts

### The Null and Alternative Hypotheses

Every test of significance begins with the formulation of two competing hypotheses:

- **Null Hypothesis (`H₀`)**: This is the hypothesis of no effect, no difference, or the status quo. It is the hypothesis we aim to test and either reject or fail to reject. (e.g., `H₀: μ = 70`).
- **Alternative Hypothesis (`H₁`)**: This contradicts the null hypothesis. It represents what we aim to establish or prove. It can be one-tailed (e.g., `H₁: μ > 70` or `H₁: μ < 70`) or two-tailed (e.g., `H₁: μ ≠ 70`).

### Level of Significance (`α`)

The level of significance, denoted by `α` (alpha), is the probability of rejecting the null hypothesis when it is actually true (Type I error). Common choices are 5% (`α = 0.05`), 1% (`α = 0.01`), etc. It defines the critical region in the tails of the distribution.

### Test Statistic (`Z`)

For large samples, the test statistic is the **Z-statistic**. Its formula depends on the parameter being tested.

**a) Test for Single Mean (`H₀: μ = μ₀`)**
Used when we want to test if the population mean is equal to a specific value `μ₀`.
`Z = (x̄ - μ₀) / (σ/√n)`
where:

- `x̄` is the sample mean,
- `μ₀` is the hypothesized population mean,
- `σ` is the population standard deviation (if unknown, the sample standard deviation `s` can be used for large samples),
- `n` is the sample size.

**b) Test for Difference of Means (`H₀: μ₁ = μ₂`)**
Used when we want to test if the means of two independent populations are equal.
`Z = (x̄₁ - x̄₂) / √( (σ₁²/n₁) + (σ₂²/n₂) )`
where `x̄₁` and `x̄₂` are the sample means, `σ₁` and `σ₂` are the population standard deviations, and `n₁` and `n₂` are the respective sample sizes.

**c) Test for Single Proportion (`H₀: p = p₀`)**
Used when we want to test if the population proportion is equal to a specific value `p₀`.
`Z = (p̂ - p₀) / √( (p₀ * q₀) / n )`
where:

- `p̂` is the sample proportion,
- `p₀` is the hypothesized population proportion,
- `q₀ = 1 - p₀`,
- `n` is the sample size.

### Steps in Testing a Hypothesis (Procedure)

1. **Formulate Hypotheses:** Clearly state `H₀` and `H₁`.
2. **Choose Significance Level (`α`):** Typically 0.05.
3. **Compute the Test Statistic (`Z`):** Use the appropriate formula.
4. **Determine the Critical Region:** Based on `α` and `H₁` (one-tailed or two-tailed), find the critical `Z-value` from the standard normal table (e.g., `Z_{α/2} = ±1.96` for `α=0.05` and a two-tailed test).
5. **Make a Decision:**

- If the calculated `|Z|` > critical `Z-value`, **reject `H₀`**.
- If the calculated `|Z|` <= critical `Z-value`, **do not reject `H₀`**.

## 3. Example: Test for Single Mean

**Problem:** A battery company claims its batteries last 100 hours on average. A random sample of 64 batteries showed a mean life of 98 hours with a standard deviation of 12 hours. Test the company's claim at a 5% level of significance.

**Solution:**

1. **Hypotheses:**

- `H₀: μ = 100 hours` (The company's claim is true)
- `H₁: μ ≠ 100 hours` (The company's claim is not true) → A two-tailed test.

2. **Given:**

- `n = 64` (Large sample)
- `x̄ = 98`
- `s = 12` (Using sample S.D. as population S.D. is unknown)
- `μ₀ = 100`
- `α = 0.05`

3. **Test Statistic:**
   `Z = (x̄ - μ₀) / (s/√n) = (98 - 100) / (12/√64) = (-2) / (12/8) = (-2) / 1.5 = -1.333`

4. **Critical Value:**
   For a two-tailed test with `α = 0.05`, the critical Z-values are `±1.96`.

5. **Decision:**
   The calculated `|Z| = 1.333` is less than the critical value `1.96`. Therefore, it does not fall in the critical region.

**Conclusion:** We fail to reject the null hypothesis (`H₀`). There is not sufficient evidence at the 5% level of significance to reject the company's claim that the batteries last 100 hours on average.

## 4. Key Points & Summary

- **Purpose:** Tests of significance are used to make objective decisions about hypotheses concerning population parameters.
- **Large Samples:** The procedure relies on the Central Limit Theorem, which ensures the sampling distribution is approximately normal for `n > 30`.
- **Test Statistic:** The **Z-test** is the appropriate test statistic for large sample tests concerning means and proportions.
- **Decision Making:** The conclusion is always made in the context of the chosen significance level `α`. Rejecting `H₀` suggests strong evidence against it, while failing to reject it means the data does not provide sufficient evidence to overturn the null hypothesis.
- **Error Types:**
- **Type I Error (α):** Rejecting a true `H₀`.
- **Type II Error (β):** Failing to reject a false `H₀`.
- This large sample theory forms the foundation for understanding more complex tests used with smaller samples (like the t-test).
