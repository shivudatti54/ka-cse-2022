Of course. Here is a comprehensive educational note on the "Comparison of Large Samples" for  Engineering students.

# Module 3: Statistical Inference 1 - Comparison of Large Samples

## Introduction

In engineering and computer science, we often need to compare two different datasets or populations. For instance, you might want to know if a new algorithm is significantly faster than an old one, or if user engagement is higher on a new website design compared to the old one. Statistical inference provides the tools to make these comparisons objectively. When our sample sizes are large (typically n > 30), we can leverage the powerful **Central Limit Theorem** to make robust comparisons about the population means. This section focuses on the **Z-test for the difference of two means**, the primary method for comparing large, independent samples.

## Core Concepts

### 1. The Central Limit Theorem (CLT) for Two Samples

The CLT states that the sampling distribution of the sample mean approaches a normal distribution as the sample size increases, regardless of the shape of the population distribution. For two independent samples, this implies:
*   The difference between the two sample means, $\bar{X}_1 - \bar{X}_2$, will also be approximately normally distributed.
*   The mean of this sampling distribution of differences is the true difference in population means, $\mu_1 - \mu_2$.
*   The standard deviation of this distribution is the **standard error of the difference between two means**.

### 2. Hypothesis Setup

We are typically testing one of two hypotheses:
*   **Two-Tailed Test:** Checks for *any* difference between the two population means.
    *   $H_0: \mu_1 = \mu_2$ (There is no difference)
    *   $H_1: \mu_1 \neq \mu_2$ (There is a difference)
*   **One-Tailed Test:** Checks if one mean is specifically larger or smaller (e.g., is the new algorithm *faster*?).
    *   $H_0: \mu_1 \leq \mu_2$
    *   $H_1: \mu_1 > \mu_2$

### 3. The Test Statistic: The Z-Score

The test statistic for comparing the means of two large samples is the Z-score, calculated as:

**$$z = \frac{(\bar{X}_1 - \bar{X}_2) - (\mu_1 - \mu_2)}{SE(\bar{X}_1 - \bar{X}_2)}$$**

Under the null hypothesis ($H_0$), we assume $\mu_1 - \mu_2 = 0$, so the formula simplifies to:

**$$z = \frac{(\bar{X}_1 - \bar{X}_2) - 0}{\sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}}}$$**

Where:
*   $\bar{X}_1$, $\bar{X}_2$ are the sample means.
*   $\sigma_1$, $\sigma_2$ are the population standard deviations.
*   $n_1$, $n_2$ are the sample sizes.

**In practice, since population standard deviations ($\sigma_1, \sigma_2$) are often unknown, we use the sample standard deviations ($s_1, s_2$) as very good approximations when n is large.**

**$$z = \frac{(\bar{X}_1 - \bar{X}_2)}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}}$$**

### 4. Decision Rule

1.  Calculate the Z-statistic using the formula above.
2.  Choose a significance level ($\alpha$), commonly 0.05 for a 95% confidence level.
3.  Find the critical Z-value from the standard normal table (e.g., $Z_{\alpha/2} = \pm1.96$ for a two-tailed test with $\alpha=0.05$).
4.  **Decision:**
    *   If the calculated |z| > critical Z-value, **reject the null hypothesis ($H_0$)**. There is a statistically significant difference.
    *   If the calculated |z| ≤ critical Z-value, **fail to reject the null hypothesis ($H_0$)**. There is no significant evidence of a difference.

## Example: Algorithm Comparison

A computer scientist wants to know if a new sorting algorithm (Algorithm B) is faster than the standard one (Algorithm A). They run each algorithm on *large, independent* sets of data.

*   **Sample A (Standard):** $n_A = 50$, mean execution time $\bar{X}_A = 102$ ms, sample standard deviation $s_A = 15$ ms.
*   **Sample B (New):** $n_B = 60$, mean execution time $\bar{X}_B = 96$ ms, sample standard deviation $s_B = 12$ ms.

Test the hypothesis at the 0.05 significance level that the new algorithm is faster.

**Step 1: Set up hypotheses.**
*   $H_0: \mu_B \geq \mu_A$ (The new algorithm is not faster)
*   $H_1: \mu_B < \mu_A$ (The new algorithm **is** faster)  [Note: We are expecting a lower time, so $\mu_B < \mu_A$]

**Step 2: Calculate the Z-statistic.**
$$z = \frac{(\bar{X}_B - \bar{X}_A)}{\sqrt{\frac{s_B^2}{n_B} + \frac{s_A^2}{n_A}}} = \frac{(96 - 102)}{\sqrt{\frac{12^2}{60} + \frac{15^2}{50}}} = \frac{-6}{\sqrt{\frac{144}{60} + \frac{225}{50}}} = \frac{-6}{\sqrt{2.4 + 4.5}} = \frac{-6}{\sqrt{6.9}} = \frac{-6}{2.627} \approx -2.28$$

**Step 3: Find the critical value.**
For a **left-tailed test** at $\alpha=0.05$, the critical Z-value is $-1.645$.

**Step 4: Make a decision.**
The calculated z-score (-2.28) is *less than* the critical value (-1.645). It falls in the rejection region.
--> **Reject $H_0$.**

**Conclusion:** There is sufficient evidence at the 0.05 significance level to conclude that the new algorithm (B) has a lower average execution time than the standard algorithm (A).

## Key Points / Summary

*   **Purpose:** The Two-Sample Z-test is used to determine if there is a significant difference between the means of two independent large samples (n > 30).
*   **Foundation:** Relies on the Central Limit Theorem, which ensures the sampling distribution is approximately normal.
*   **Test Statistic:** Uses the Z-score, which measures how many standard errors the difference between sample means is from the hypothesized difference (usually 0).
*   **Assumptions:**
    1.  Samples are independent and randomly selected.
    2.  Sample sizes are sufficiently large (n₁, n₂ > 30 is a common rule of thumb).
    3.  Population standard deviations can be approximated by sample standard deviations.
*   **Output:** The result allows us to either reject or fail to reject the null hypothesis, providing a statistical basis for comparing two groups, a common task in data analysis, algorithm design, and machine learning model evaluation.