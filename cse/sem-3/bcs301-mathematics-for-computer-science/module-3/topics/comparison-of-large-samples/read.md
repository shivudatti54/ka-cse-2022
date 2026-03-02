# Comparison of Large Samples

## Table of Contents

- [Comparison of Large Samples](#comparison-of-large-samples)
- [Introduction](#introduction)
- [Core Concepts](#core-concepts)
  - [1. The Foundation: Sampling Distributions](#1-the-foundation-sampling-distributions)
  - [2. The Hypotheses: Null and Alternative](#2-the-hypotheses-null-and-alternative)
  - [3. The Tool: Z-Test for Two Large Samples](#3-the-tool-z-test-for-two-large-samples)
  - [4. The Decision: Critical Value and p-value](#4-the-decision-critical-value-and-p-value)
- [Example Scenario (Hypothetical)](#example-scenario-hypothetical)
- [Key Points & Summary](#key-points--summary)

## Introduction

In engineering and computer science, we often need to compare two different sets of data. For instance, does a new caching algorithm reduce average server response time compared to the old one? Is the mean battery life of smartphones from Brand A significantly different from those of Brand B? **Statistical inference for large samples** provides a rigorous, mathematical framework to answer these questions, moving beyond simple visual comparisons of means. It allows us to determine if observed differences are due to a real underlying effect or merely random chance.

## Core Concepts

### 1. The Foundation: Sampling Distributions

When we deal with large samples (typically, n > 30), the **Central Limit Theorem (CLT)** becomes our most powerful tool. The CLT states that the sampling distribution of the sample mean ( $\bar{x}$ ) will be approximately normally distributed, regardless of the original population's distribution, given a sufficiently large sample size.

This is crucial because the normal distribution has well-known properties, allowing us to calculate probabilities and make inferences.

### 2. The Hypotheses: Null and Alternative

Every comparison test starts by formulating two competing hypotheses:

- **Null Hypothesis ($H_0$)**: This is the default assumption, usually stating that there is _no difference_ or _no effect_. For comparing two means, it is often $\mu_1 = \mu_2$.
- **Alternative Hypothesis ($H_1$ or $H_a$)**: This is what we want to prove. It can be two-tailed ( $\mu_1 \neq \mu_2$ ) or one-tailed ( $\mu_1 > \mu_2$ or $\mu_1 < \mu_2$ ).

The goal of the test is to determine whether we have enough evidence to **reject the null hypothesis** ($H_0$) in favor of the alternative ($H_1$).

### 3. The Tool: Z-Test for Two Large Samples

The **Z-test** is the appropriate statistical test for comparing the means of two independent large samples. The test statistic is calculated as follows:

$$ Z = \frac{(\bar{X}\_1 - \bar{X}\_2) - (\mu_1 - \mu_2)}{S.E.(\bar{X}\_1 - \bar{X}\_2)} $$

Under the null hypothesis, we assume $(\mu_1 - \mu_2) = 0$. The **Standard Error (S.E.)** for the difference between two independent means is given by:

$$ S.E. = \sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}} $$

If the population standard deviations ($\sigma_1$ and $\sigma_2$) are unknown—which is almost always the case—we use the sample standard deviations ($s_1$ and $s_2$) as reliable estimators because of the large sample size.

Thus, the formula becomes:

$$ Z = \frac{\bar{X}\_1 - \bar{X}\_2}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}} $$

This calculated Z-value tells us how many standard errors the difference between our sample means ($\bar{X}_1 - \bar{X}_2$) is from the hypothesized difference of zero.

### 4. The Decision: Critical Value and p-value

We compare the calculated Z-value to a critical value from the **Standard Normal Distribution (Z-table)** based on our chosen **significance level ($\alpha$)**. A common choice in engineering is $\alpha = 0.05$ (5%), corresponding to a critical value of approximately ±1.96 for a two-tailed test.

- **Critical Value Approach:** If |Calculated Z| > Critical Z, we reject $H_0$.
- **p-value Approach:** The p-value is the probability of obtaining a test result at least as extreme as the one observed, assuming $H_0$ is true. If p-value < $\alpha$, we reject $H_0$.

---

## Example Scenario (Hypothetical)

**Problem:** A computer scientist has developed a new compression algorithm. Two large groups of 40 files each are selected. Group A is compressed with the standard algorithm, and Group B with the new one. The average compression time for Group A ($\bar{X}_A$) is 22.5 ms with a standard deviation ($s_A$) of 4 ms. For Group B ($\bar{X}_B$), it is 20.8 ms with a standard deviation ($s_B$) of 3.5 ms. Can we conclude that the new algorithm is faster at the 0.05 significance level? ($H_a: \mu_B < \mu_A$)

**Solution:**

1. **Hypotheses:**

- $H_0: \mu_A = \mu_B$ (The new algorithm is not faster)
- $H_1: \mu_B < \mu_A$ (The new algorithm is faster) - _This is a one-tailed test._

2. **Calculate Z-statistic:**
   $$ Z = \frac{\bar{X}\_B - \bar{X}\_A}{\sqrt{\frac{s_B^2}{n_B} + \frac{s_A^2}{n_A}}} = \frac{20.8 - 22.5}{\sqrt{\frac{(3.5)^2}{40} + \frac{(4)^2}{40}}} = \frac{-1.7}{\sqrt{\frac{12.25}{40} + \frac{16}{40}}} = \frac{-1.7}{\sqrt{0.30625 + 0.4}} $$
 $$ Z = \frac{-1.7}{\sqrt{0.70625}} = \frac{-1.7}{0.840} \approx -2.024 $$

3. **Make a Decision:**
   For a one-tailed test at $\alpha=0.05$, the critical Z-value is -1.645.
   Our calculated Z ($-2.024$) is _less than_ $-1.645$. It falls in the rejection region.
   _Alternatively, the p-value for Z = -2.024 is ~0.0214, which is less than 0.05._

4. **Conclusion:** We reject the null hypothesis. There is sufficient statistical evidence at the 5% significance level to conclude that the new compression algorithm is faster than the standard one.

---

## Key Points & Summary

- **Purpose:** To determine if the difference between the means of two large, independent samples is statistically significant.
- **Foundation:** Relies on the **Central Limit Theorem**, which ensures the sampling distribution of the mean is normal.
- **Test Used:** **Two-Sample Z-Test**.
- **Test Statistic:**
  $Z = \frac{\bar{X}_1 - \bar{X}_2}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}}$
- **Decision Rule:** Reject the null hypothesis ($H_0$) if the |Calculated Z| > Critical Z-value **or** if the p-value < $\alpha$.
- **Assumptions:** Samples are independent, randomly selected, and large (n > 30 for each). For smaller samples, a different test (t-test) is used.
- **Application:** Extensively used in A/B testing, algorithm performance analysis, quality control, and any scenario requiring comparison of two population means.
