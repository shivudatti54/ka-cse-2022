# Statistical Inference 1: Testing of Hypothesis

## Introduction

For  Computer Science students, data-driven decision-making is a core skill, whether you're A/B testing a website, training a machine learning model, or analyzing network performance metrics. Statistical inference allows us to draw conclusions about a population based on a sample. Hypothesis testing is a formal, step-by-step procedure within inference used to evaluate claims about a population parameter (like a mean or proportion). It is the statistical equivalent of a court trial, where we assume innocence until proven guilty beyond a reasonable doubt.

## Core Concepts of Hypothesis Testing

### 1. The Two Hypotheses

Every test involves two competing, mutually exclusive statements:

*   **Null Hypothesis (H₀):** This is the default or status quo assumption. It represents a statement of "no effect," "no difference," or "no change." (e.g., "The new algorithm does **not** improve average processing time.").
*   **Alternative Hypothesis (H₁ or Hₐ):** This is the claim we want to test *for*. It represents a statement of effect, difference, or change. (e.g., "The new algorithm **does** improve average processing time.").

The goal of the test is to determine whether the sample data provides sufficient evidence to **reject the null hypothesis (H₀)** in favor of the alternative (H₁).

### 2. Test Statistic

This is a standardized value calculated from the sample data. It measures how far the sample statistic (e.g., sample mean $\bar{x}$) is from the hypothesized population parameter (e.g., population mean $\mu_0$), relative to the standard error. The formula depends on the parameter and distribution (e.g., z-test, t-test).

### 3. Level of Significance (α)

This is the probability of making a **Type I Error**—rejecting the null hypothesis when it is actually true. It's the "reasonable doubt" threshold. In engineering and CS, a common choice is **α = 0.05 (5%)**. This means we are willing to accept a 5% chance of a false positive.

### 4. P-value

The p-value is the probability of obtaining a test statistic **at least as extreme** as the one observed, assuming the null hypothesis (H₀) is true.

*   A **small p-value** (typically ≤ α) indicates that the observed data is very unlikely under H₀. This provides strong evidence *against* H₀.
*   A **large p-value** (> α) indicates that the observed data is likely under H₀. We fail to find evidence against H₀.

**The decision rule is simple: If p-value ≤ α, reject H₀. If p-value > α, fail to reject H₀.**

### 5. Types of Tests: One-Tailed vs. Two-Tailed

The formulation of H₁ determines the "tail" of the distribution we examine.

*   **Two-Tailed Test:** Used when H₁ is simply "not equal to" (≠). We are testing for a difference in *either* direction.
    *   H₀: μ = μ₀
    *   H₁: μ ≠ μ₀
*   **One-Tailed Test:** Used when H₁ specifies a direction ("greater than" (>) or "less than" (<)). This is common in performance testing.
    *   H₀: μ ≤ μ₀
    *   H₁: μ > μ₀  *(Tests for an **increase**)*

---

## Example: Testing a New Compression Algorithm

A company claims its new lossless compression algorithm reduces the average file size by more than 20% from the original. The current standard achieves a 20% reduction on average (μ₀ = 20%). You test the algorithm on a sample of 50 files (`n=50`).

**Step 1: Formulate Hypotheses**
We want to test for an *improvement* (a "greater than" claim).
*   H₀: μ ≤ 20% (The new algorithm is no better than the standard)
*   H₁: μ > 20% (The new algorithm provides a greater than 20% reduction) *(This is our claim)*

**Step 2: Choose Significance Level**
We set α = 0.05.

**Step 3: Collect Data and Calculate Test Statistic**
From your sample, you calculate:
*   Sample mean reduction, $\bar{x}$ = 22%
*   Sample standard deviation, *s* = 8%

Since n > 30 but the population standard deviation is unknown, we use a **t-test**.
$$ t = \frac{\bar{x} - \mu_0}{s / \sqrt{n}} = \frac{22 - 20}{8 / \sqrt{50}} = \frac{2}{1.131} \approx 1.77 $$

**Step 4: Determine the P-value**
For a one-tailed t-test with 49 degrees of freedom, the p-value for t = 1.77 is approximately **0.042**.

**Step 5: Make a Decision**
Since p-value (0.042) ≤ α (0.05), we **reject the null hypothesis (H₀)**.

**Conclusion:** At the 5% significance level, there is sufficient statistical evidence to support the claim that the new compression algorithm provides an average reduction greater than 20%.

---

## Key Points & Summary

*   **Purpose:** Hypothesis testing is a structured process to make data-informed decisions about population parameters.
*   **Core Components:** The procedure revolves around two hypotheses (H₀ and H₁), a test statistic, a significance level (α), and a p-value.
*   **Decision Rule:** The p-value is the key to the decision. If `p-value ≤ α`, **reject H₀**. If `p-value > α`, **fail to reject H₀**. Failing to reject H₀ does *not* prove it is true; it just means evidence against it is weak.
*   **Errors:**
    *   **Type I Error (α):** Rejecting a true H₀ (False Positive).
    *   **Type II Error (β):** Failing to reject a false H₀ (False Negative).
*   **Relevance for CS:** This is fundamental for algorithm analysis (e.g., comparing runtimes), machine learning (e.g., evaluating model performance), data science, and network analysis. Mastering this concept is crucial for any engineer working with data.