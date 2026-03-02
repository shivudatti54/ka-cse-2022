# Confidence Limits: Estimating with Certainty

## Introduction

In statistical inference, we often use a sample to draw conclusions about a larger population. A single point estimate, like a sample mean (x̄), gives us a "best guess" for the population mean (μ). However, this single number doesn't convey any information about its own reliability or precision. How confident can we be that our estimate is close to the true population parameter? This is where **confidence limits** (or confidence intervals) come into play. They provide a range of values, constructed from sample data, that is likely to contain the true population parameter with a specified level of confidence.

## Core Concepts

### 1. What are Confidence Limits?

Confidence limits are the lower and upper boundaries of a **confidence interval (CI)**. Together, they define a range of values within which the true population parameter (e.g., mean, proportion) is estimated to lie, along with a specific level of confidence.

*   **Lower Confidence Limit (LCL):** The smallest value in the confidence interval.
*   **Upper Confidence Limit (UCL):** The largest value in the confidence interval.

The interval between the LCL and UCL is the confidence interval itself: **CI = (LCL, UCL)**.

### 2. Confidence Level

The **confidence level** (often denoted by `(1 - α) * 100%`) expresses the long-run frequency of such intervals containing the true parameter if we were to repeat the sampling process an infinite number of times.

*   A **95% confidence level** does *not* mean there is a 95% probability that the specific interval you calculated contains the true mean. Instead, it means that if you were to take 100 different random samples and compute a confidence interval for each sample, approximately 95 of those 100 intervals would contain the true population mean.
*   Common confidence levels are 90%, 95%, and 99%. A higher confidence level (e.g., 99%) requires a wider interval to be more sure of capturing the true parameter.

### 3. The Mathematical Foundation

The construction of a confidence interval for a population mean, when the population standard deviation (σ) is *known*, relies on the properties of the **sampling distribution of the mean** and the **Z-distribution**.

The general formula is:
**Confidence Interval = Point Estimate ± (Critical Value) × (Standard Error)**

For a population mean (μ), this becomes:
**CI for μ = x̄ ± (z_α/2) * (σ / √n)**

Where:
*   **x̄** is the sample mean (the point estimate).
*   **z_α/2** is the critical value from the standard normal (Z) distribution. For a 95% CI, α is 0.05, and z_α/2 is approximately 1.96.
*   **σ** is the known population standard deviation.
*   **n** is the sample size.
*   **σ / √n** is the standard error of the mean, which measures the variability of the sample mean.

The terms `x̄ - (z_α/2 * σ/√n)` and `x̄ + (z_α/2 * σ/√n)` are the **Lower and Upper Confidence Limits**, respectively.

### 4. Interpretation

Let's construct a 95% CI for a population mean. Suppose we have:
*   x̄ = 50
*   σ = 10
*   n = 100
*   z_α/2 for 95% confidence = 1.96

**Standard Error (SE)** = σ / √n = 10 / √100 = 10 / 10 = 1
**Margin of Error (E)** = z_α/2 * SE = 1.96 * 1 = 1.96

**Confidence Interval** = 50 ± 1.96 = **(48.04, 51.96)**

**Interpretation:** We are 95% confident that the true population mean (μ) lies between 48.04 and 51.96.

### 5. What Affects the Width of the Interval?

The width of the confidence interval (the distance between the LCL and UCL) is determined by three factors:
1.  **Confidence Level (1-α):** A higher confidence level (e.g., 99% vs. 95%) uses a larger critical value (e.g., 2.58 vs. 1.96), resulting in a wider interval.
2.  **Sample Size (n):** A larger sample size (n) reduces the standard error (σ/√n), which shrinks the margin of error and produces a narrower, more precise interval.
3.  **Population Variability (σ):** A more variable population (larger σ) leads to a larger standard error and a wider interval.

## Key Points & Summary

*   **Purpose:** Confidence limits provide a range of plausible values for an unknown population parameter (like the mean), accompanied by a degree of confidence.
*   **Interpretation:** A 95% CI means that 95% of similarly constructed intervals from repeated sampling will contain the true parameter. It is *not* a probability statement about a single interval.
*   **The Interval:** The confidence interval is defined as `Point Estimate ± Margin of Error`.
*   **The Margin of Error** is determined by the critical value (from Z or t-distribution) and the standard error.
*   **The "Cost" of Confidence:** Higher confidence requires a wider interval. The only way to gain higher confidence *and* a narrower interval is to increase the sample size.
*   **Next Steps:** In real-world computer science applications (like A/B testing or data analysis), the population standard deviation (σ) is rarely known. In such cases, we use the **t-distribution** and the sample standard deviation (s) to calculate the interval, leading to slightly wider intervals to account for the additional uncertainty. This is a crucial topic for Module 3, Part 2.