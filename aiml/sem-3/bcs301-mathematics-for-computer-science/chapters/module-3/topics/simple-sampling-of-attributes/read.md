Of course. Here is a comprehensive educational note on "Simple Sampling of Attributes" for  engineering students.

# Module 3: Statistical Inference 1
## Topic: Simple Sampling of Attributes

### Introduction

In computer science, we often need to make decisions or draw conclusions about large populations based on limited data. For instance, a quality control engineer might want to know the percentage of defective chips in a production batch without testing every single one. This process of making inferences about a population using a sample is called **Statistical Inference**. **Simple Sampling of Attributes** is a fundamental technique within this domain, used specifically when the data we collect is categorical or binary (e.g., pass/fail, yes/no, defective/non-defective). This module provides the foundation for understanding how to estimate population proportions and test hypotheses about them.

### Core Concepts

#### 1. Population Proportion (`p`)

The population proportion is the parameter we are interested in. It represents the probability that a randomly selected item from the entire population possesses a specific attribute (e.g., is defective). It is denoted by `p`. Since we usually cannot measure the entire population, `p` is unknown.

#### 2. Sample Proportion (`p̂`)

This is the statistic we calculate from our sample to *estimate* the unknown population proportion `p`. It is denoted by `p̂` (p-hat).
If we take a random sample of size `n` and find that `x` number of items possess the attribute, then:
`p̂ = x / n`

#### 3. Sampling Distribution of `p̂`

The sample proportion `p̂` is a random variable; its value will change from sample to sample. The distribution of all possible values of `p̂` is called its **sampling distribution**.

For large sample sizes (a common rule of thumb is `np > 5` and `n(1-p) > 5`), the sampling distribution of `p̂` can be approximated by a **Normal Distribution** thanks to the Central Limit Theorem.

*   **Mean of the sampling distribution:** The mean of all possible `p̂` values is equal to the population proportion `p`.
    `μ_p̂ = p`
*   **Standard Error of `p̂`:** This measures the variability of the sample proportion around the population proportion. It is given by:
    `σ_p̂ = sqrt( p(1-p) / n )`

Since `p` is unknown, we often use `p̂` to estimate it in the standard error formula for practical calculations: `Est. σ_p̂ = sqrt( p̂(1-p̂) / n )`.

#### 4. Setting Up a Test of Hypothesis

We often want to test a claim about the population proportion (e.g., "The defect rate is 5%"). This is done using hypothesis testing.

*   **Null Hypothesis (`H₀`):** This is the hypothesis of no change or status quo. E.g., `H₀: p = p₀` (where `p₀ = 0.05`).
*   **Alternative Hypothesis (`H₁`):** This is what we want to prove. It could be two-tailed (`H₁: p ≠ p₀`), one-tailed left (`H₁: p < p₀`), or one-tailed right (`H₁: p > p₀`).
*   **Test Statistic (`Z`):** We use the `Z-statistic` to determine how far our sample proportion `p̂` is from the hypothesized proportion `p₀`, measured in terms of standard errors.
    `Z = (p̂ - p₀) / sqrt( p₀(1-p₀) / n )`

We then compare this calculated `Z` value to the critical value from the Standard Normal Distribution (Z-table) at a chosen **level of significance (α)**, typically 0.05.

### Example: Quality Control

A manufacturer claims that only 2% of its chips are defective (`p₀ = 0.02`). A quality engineer tests a random sample of 500 chips (`n = 500`) and finds 15 defective chips (`x = 15`). Test the manufacturer's claim at a 5% level of significance (`α = 0.05`).

**Step 1: Set up hypotheses.**
`H₀: p = 0.02` (The claim is true)
`H₁: p > 0.02` (We are testing if the defect rate is *higher* than claimed)

**Step 2: Calculate the sample proportion.**
`p̂ = x / n = 15 / 500 = 0.03`

**Step 3: Calculate the test statistic (Z).**
`Z = (p̂ - p₀) / sqrt( p₀(1-p₀)/n ) = (0.03 - 0.02) / sqrt( (0.02 * 0.98) / 500 )`
`Z = 0.01 / sqrt(0.0196 / 500) = 0.01 / sqrt(0.0000392) ≈ 0.01 / 0.00626 ≈ 1.597`

**Step 4: Make a decision.**
For a right-tailed test at `α = 0.05`, the critical value `Z_α` from the Z-table is **1.645**.

Since our calculated `Z` (1.597) is **less than** the critical value (1.645), it falls in the "Do Not Reject H₀" region.

**Step 5: Conclusion.**
There is **not sufficient evidence** at the 0.05 significance level to reject the manufacturer's claim that the defect rate is 2%.

### Key Points & Summary

*   **Purpose:** Simple sampling of attributes is used to make inferences (estimation and hypothesis testing) about a population proportion (`p`) based on a sample proportion (`p̂`).
*   **Data Type:** It is used for categorical, binary data (attributes).
*   **Foundation:** The core concept is the **Sampling Distribution of p̂**, which becomes approximately normal for large samples.
*   **Mean and Spread:** The mean of the sampling distribution is `p`, and its standard error is `sqrt(p(1-p)/n)`.
*   **Hypothesis Testing:** The test of hypothesis for a proportion uses a **Z-test statistic** to compare the sample evidence (`p̂`) against the null hypothesis (`H₀: p = p₀`).
*   **Assumptions:** The sample must be random and the sample size `n` must be sufficiently large so that `np₀` and `n(1-p₀)` are both greater than 5 for the hypothesis test to be valid.