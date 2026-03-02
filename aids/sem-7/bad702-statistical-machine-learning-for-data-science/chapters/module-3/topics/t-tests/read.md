# Module 3: Statistical Hypothesis Testing with t-tests

**Subject:** Statistical Machine Learning for Data Science

## 1. Introduction

In data science and machine learning, we constantly make inferences from data. How do we know if a new algorithm is genuinely better than an existing one? Or if the average user engagement time after a website redesign has *truly* increased? We use statistical hypothesis tests to move beyond mere intuition and provide quantifiable evidence. The **t-test** is a fundamental inferential statistic used to determine if there is a significant difference between the means of two groups, which is especially crucial when comparing models or analyzing experimental results (A/B testing). It is the workhorse of comparative analysis.

## 2. Core Concepts

### The Need for the t-test
Why not just use the well-known **z-test**? The z-test requires knowing the population standard deviation (σ), a luxury we rarely have with sample data. The t-test, developed by William Sealy Gosset under the pseudonym "Student," elegantly solves this by using the **sample standard deviation (s)**. It is specifically designed for small sample sizes (typically n < 30) and situations where σ is unknown.

### The t-Distribution
The t-test uses the **t-distribution** as its theoretical foundation. Similar to the normal distribution, it is symmetrical and bell-shaped but has heavier tails. This means it is more prone to producing values that fall far from its mean, accounting for the extra uncertainty introduced by estimating σ from the sample. The shape of the t-distribution depends on the **degrees of freedom (df)**, which is typically related to the sample size (e.g., for a one-sample test, df = n - 1). As the sample size increases (df → ∞), the t-distribution converges to the standard normal distribution.

### Types of t-tests
There are three primary types of t-tests:

1.  **One-Sample t-test:** Compares the mean of a single sample to a known population mean or a hypothetical mean (μ₀).
    *   **Formula:** $t = \frac{\bar{x} - \mu_0}{s / \sqrt{n}}$
    *   **Example:** Is the average CPU utilization of our new cloud server configuration (sample mean) significantly different from the industry standard of 70% (μ₀)?

2.  **Independent Two-Sample t-test:** Compares the means of two independent, unrelated groups. Also called Student's t-test. A key assumption is **homogeneity of variance** (the variances of the two groups are approximately equal). A variant (Welch's t-test) is used when this assumption is violated.
    *   **Formula (pooled variance):** $t = \frac{\bar{x}_1 - \bar{x}_2}{s_p \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}}$ where $s_p^2$ is the pooled variance.
    *   **Example:** Is the mean accuracy of a new machine learning model (Group 1) significantly higher than the mean accuracy of the current model (Group 2) when tested on different datasets?

3.  **Paired Sample t-test:** Compares the means of two related groups. This could be the same group tested twice (e.g., pre-test vs. post-test) or matched pairs.
    *   **Formula:** $t = \frac{\bar{d}}{s_d / \sqrt{n}}$ where $\bar{d}$ is the mean of the differences between pairs.
    *   **Example:** Is there a significant difference in the battery life of a smartphone *before* and *after* a new OS update? Each phone is its own control.

### The Hypothesis Testing Procedure
The general workflow for any t-test is:
1.  **Formulate Hypotheses:**
    *   **Null Hypothesis (H₀):** States that there is no effect or no difference (e.g., μ₁ = μ₂).
    *   **Alternative Hypothesis (H₁):** States that there is an effect or a difference (e.g., μ₁ ≠ μ₂ for two-tailed; μ₁ > μ₂ for one-tailed).
2.  **Choose Significance Level (α):** Typically set at 0.05 (5%). This is the probability of rejecting H₀ when it is actually true (Type I error).
3.  **Calculate the t-statistic:** Use the appropriate formula from above.
4.  **Determine the p-value:** Using the calculated t-value and the degrees of freedom, find the probability of observing the data if the null hypothesis were true.
5.  **Make a Decision:**
    *   If **p-value ≤ α**: Reject the null hypothesis. The result is **statistically significant**.
    *   If **p-value > α**: Fail to reject the null hypothesis. There is not enough evidence for a significant difference.

## 3. Key Points & Summary

*   **Purpose:** The t-test determines if the difference between the means of one or two groups is statistically significant, accounting for sample variability.
*   **Key Assumptions:** Data should be approximately normally distributed (especially important for small n), and for the independent t-test, variances should be roughly equal (check with Levene's test). Data should also be continuous.
*   **Degrees of Freedom:** A parameter that describes the amount of information available to estimate the test statistic. It determines the shape of the t-distribution.
*   **Output:** The key output is the **t-statistic** (a ratio of the signal to noise) and the **p-value** (the probability that the observed result occurred by chance).
*   **Application in ML/DSA:** Crucial for evaluating model performance (e.g., comparing accuracy, F1-score, MSE between models), conducting A/B tests on user interfaces, and analyzing experimental results in a data-driven way.

**In essence, the t-test provides a rigorous statistical framework to answer the critical question: "Is this observed difference real, or could it just be random noise?"**