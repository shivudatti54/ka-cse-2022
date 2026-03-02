Of course. Here is a comprehensive educational module on the Comparison of Large Samples for  Engineering students.

# Module 3: Statistical Inference 1 - Comparison of Large Samples

## Introduction

In engineering and computer science, we often need to compare two different groups or processes. For instance, does a new algorithm run faster than the old one? Is the average throughput of Server A different from Server B? Does a change in code improve the average user engagement time?

When the sample sizes are large (typically n > 30), we can leverage the power of the **Central Limit Theorem** to make statistically sound comparisons about their population means. This process, known as **Hypothesis Testing for Large Samples**, allows us to move beyond mere observation and make data-driven decisions and inferences.

## Core Concepts

### 1. The Hypothesis Framework

Every comparison starts with two opposing statistical hypotheses:

*   **Null Hypothesis (H₀):** This is the default assumption, usually representing "no effect" or "no difference." For comparing two means, it states that the means of the two populations are equal.
    *   *Form:* H₀: μ₁ = μ₂ or equivalently, H₀: μ₁ - μ₂ = 0

*   **Alternative Hypothesis (H₁ or Ha):** This is what we want to prove. It can be one of three types:
    *   **Two-tailed test:** H₁: μ₁ ≠ μ₂ (We believe there is a difference, but don't know the direction)
    *   **Left-tailed test:** H₁: μ₁ < μ₂
    *   **Right-tailed test:** H₁: μ₁ > μ₂

### 2. The Test Statistic (Z-statistic)

For large independent samples (n₁ & n₂ > 30) drawn from two populations, the difference between the sample means (x̄₁ - x̄₂) follows a normal distribution. The standardized test statistic used is the **Z-score**:

**$$Z = \frac{( \bar{x}_1 - \bar{x}_2 ) - ( \mu_1 - \mu_2 )}{S.E.}$$**

Under the null hypothesis (H₀: μ₁ - μ₂ = 0), this simplifies to:

**$$Z = \frac{ \bar{x}_1 - \bar{x}_2 }{ \sqrt{ \frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2} } }$$**

Where:
*   x̄₁ and x̄₂ are the sample means.
*   σ₁² and σ₂² are the **population variances**.
*   n₁ and n₂ are the sample sizes.

In practice, since the population variances (σ²) are often unknown, we use the **sample variances (s₁² and s₂²)** as very good approximations for them when samples are large.

**$$Z_{calculated} = \frac{ \bar{x}_1 - \bar{x}_2 }{ \sqrt{ \frac{s_1^2}{n_1} + \frac{s_2^2}{n_2} } }$$**

### 3. Decision Making: The Critical Value Approach

1.  **Compute the Z-statistic:** Calculate the value using the formula above.
2.  **Choose a Significance Level (α):** This is the probability of rejecting H₀ when it is actually true (Type I error). Common choices are α = 0.05 (95% confidence) or α = 0.01 (99% confidence).
3.  **Find the Critical Value (Z\_critical):** This value marks the boundary of the rejection region in the standard normal distribution. It depends on α and the type of test (one-tailed or two-tailed).
    *   For a two-tailed test at α=0.05, Z_critical = ±1.96.
    *   For a right-tailed test at α=0.05, Z_critical = +1.645.
    *   For a left-tailed test at α=0.05, Z_critical = -1.645.
4.  **Make a Decision:**
    *   If |Z_calculated| > |Z_critical|, **reject the null hypothesis (H₀)**. The difference is statistically significant.
    *   If |Z_calculated| <= |Z_critical|, **do not reject the null hypothesis (H₀)**. There is not enough evidence to support a significant difference.

---

## Example: Comparing Algorithm Efficiency

A computer scientist has two algorithms, A and B. She runs each algorithm on 50 different large datasets and records the average execution time.

*   **Algorithm A (n₁=50):** Mean time x̄₁ = 22.5 sec, Variance s₁² = 15.2
*   **Algorithm B (n₂=50):** Mean time x̄₂ = 20.8 sec, Variance s₂² = 12.7

Test the hypothesis that the two algorithms have the same mean execution time at the 0.05 level of significance.

**Step 1: Set up Hypotheses**
*   H₀: μ₁ = μ₂ (The mean execution times are the same)
*   H₁: μ₁ ≠ μ₂ (The mean execution times are different) -> **Two-tailed test**

**Step 2: Calculate the Z-statistic**
$$Z = \frac{22.5 - 20.8}{\sqrt{ \frac{15.2}{50} + \frac{12.7}{50} }} = \frac{1.7}{\sqrt{0.304 + 0.254}} = \frac{1.7}{\sqrt{0.558}} = \frac{1.7}{0.747} \approx 2.28$$

**Step 3: Determine the Critical Value**
For a two-tailed test with α = 0.05, Z_critical = ±1.96.

**Step 4: Make a Decision**
|Z_calculated| = 2.28 > |Z_critical| = 1.96.

Therefore, we **reject the null hypothesis (H₀)**. There is sufficient evidence at the 5% significance level to conclude that there is a statistically significant difference in the mean execution time between Algorithm A and Algorithm B.

---

## Key Points & Summary

*   **Purpose:** To compare the means of two independent large samples (n₁, n₂ > 30) to infer if their population means are significantly different.
*   **Foundation:** Relies on the Central Limit Theorem, which ensures the sampling distribution of the difference in means is approximately normal.
*   **Test Statistic:** Uses the **Z-test**. The formula requires the sample means, sample variances (as proxies for population variances), and sample sizes.
*   **Hypothesis:** Defined by H₀ (no difference) and H₁ (difference exists, is greater, or is lesser).
*   **Decision Rule:** Based on comparing the calculated Z-value to a critical Z-value from the standard normal table, determined by the chosen significance level (α).
*   **Result:** Allows engineers to move from "these two numbers look different" to "we have statistical evidence that these two populations are different." This is crucial for A/B testing, performance analysis, and quality control.