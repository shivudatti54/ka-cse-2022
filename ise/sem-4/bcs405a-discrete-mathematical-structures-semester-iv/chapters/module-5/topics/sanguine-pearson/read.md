Of course. Here is comprehensive educational content on "Sanguine-Pearson" for  Engineering students, structured as requested.

---

# Module 5: Introduction to Group Theory - Sanguine-Pearson Test

## 1. Introduction

In the study of Discrete Mathematical Structures, Group Theory provides the algebraic foundation for understanding symmetry, coding theory, cryptography, and many computational concepts. When applying group theory or any mathematical construct to real-world data (e.g., in machine learning or network analysis), we often deal with statistical distributions. It is crucial to verify our underlying assumptions about this data. The **Sanguine-Pearson Test** (more commonly and correctly known as the **Shapiro-Wilk Test**) is a fundamental statistical procedure used to test the null hypothesis that a sample of data came from a normally distributed population. This test is vital for engineers, as many advanced algorithms and statistical methods (like many parametric tests) assume normality in the data.

> **Note on the Name:** The term "Sanguine-Pearson" appears to be a misnomer or a typographical error. The standard and powerful test for normality is the **Shapiro-Wilk test**, developed by Samuel Shapiro and Martin Wilk. "Sanguine" might be a malapropism for "Shapiro," and "Pearson" might be confused with Karl Pearson, who developed the Chi-Square test (a different test for goodness-of-fit). We will proceed with the correct terminology: the **Shapiro-Wilk test**.

## 2. Core Concepts

The Shapiro-Wilk test is a **goodness-of-fit test**. Its core objective is to quantify how likely it is that a given sample of data was drawn from a normal distribution.

### Null and Alternative Hypotheses

- **Null Hypothesis (H₀):** The sample data comes from a normally distributed population.
- **Alternative Hypothesis (H₁):** The sample data does _not_ come from a normally distributed population.

### The Test Statistic (W)

The power of the Shapiro-Wilk test comes from its test statistic, denoted as **W**. The calculation of W is based on the idea of a **normal probability plot**.

1.  **Order the Sample:** The `n` sample observations are first sorted in ascending order: `x₁ ≤ x₂ ≤ ... ≤ xₙ`.
2.  **Calculate the Mean:** The sample mean, `x̄`, is computed.
3.  **Coefficients and Covariance:** The test uses pre-tabulated coefficients (`aᵢ`) which are based on the expected values of the ordered statistics from a normal distribution and their covariances.
4.  **The Formula:** The test statistic W is calculated as:
    $$
    W = \frac{\left( \sum_{i=1}^{n} a_i x_i \right)^2}{\sum_{i=1}^{n} (x_i - \bar{x})^2}
    $$
    Here, the numerator is the square of a weighted linear combination of the ordered sample, and the denominator is the standard sample variance (up to a constant factor).

### Interpreting the W Statistic

- The value of `W` always lies between `0` and `1`.
- **W = 1:** Indicates a perfect match to a normal distribution.
- **W ≈ 1:** The sample is very likely to be normally distributed.
- **W << 1:** (i.e., W is significantly less than 1) provides evidence that the sample is _not_ normally distributed.

To make a formal decision, the calculated `W` statistic is compared to a critical value from a Shapiro-Wilk table (for a given significance level `α`, commonly 0.05) based on the sample size `n`. If `W` is less than the critical value, we **reject the null hypothesis (H₀)**.

## 3. Example

Let's consider a practical scenario an engineer might face.

**Scenario:** You are analyzing the processing times (in milliseconds) of a new algorithm. You run 15 tests and collect the following sample:
`[12.1, 13.4, 12.8, 14.0, 12.5, 13.7, 12.2, 13.8, 14.5, 12.9, 13.2, 13.1, 12.7, 13.5, 12.3]`

Before using a parametric test to compare this to another algorithm, you must check for normality.

1.  **State the Hypotheses:**
    - H₀: The processing time data is normally distributed.
    - H₁: The processing time data is not normally distributed.

2.  **Choose Significance Level:** α = 0.05

3.  **Compute the Test Statistic:**
    - Sort the data: `[12.1, 12.2, 12.3, 12.5, 12.7, 12.8, 12.9, 13.1, 13.2, 13.4, 13.5, 13.7, 13.8, 14.0, 14.5]`
    - Calculate the mean `x̄`.
    - Using statistical software (e.g., Python `scipy.stats.shapiro`, R `shapiro.test()`, or a calculator), compute `W`. For this sample, let's assume the result is `W = 0.961`.

4.  **Make a Decision:**
    - For n=15 and α=0.05, the critical value from the Shapiro-Wilk table is approximately 0.881.
    - Since our calculated `W (0.961)` is **greater than** the critical value `(0.881)`, we **fail to reject H₀**.

5.  **Conclusion:** There is not sufficient evidence to conclude that the data is non-normal. You may proceed with the assumption that the data is approximately normally distributed for your further analysis.

## 4. Key Points & Summary

| Key Point                        | Description                                                                                                                                                                                        |
| :------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Purpose**                      | To test if a sample data set comes from a normally distributed population.                                                                                                                         |
| **Test Type**                    | Goodness-of-fit test.                                                                                                                                                                              |
| **Hypotheses**                   | **H₀:** Data is normal. **H₁:** Data is not normal.                                                                                                                                                |
| **Test Statistic**               | **W**, a value between 0 and 1. Values close to 1 suggest normality.                                                                                                                               |
| **Decision Rule**                | Reject H₀ if **p-value < α** or if **W < critical value**.                                                                                                                                         |
| **Why it Matters for Engineers** | Validates the normality assumption required for many statistical models, machine learning algorithms, control charts, and process capability analysis (Cp, Cpk).                                   |
| **Software**                     | The calculation is complex; always use statistical software (`scipy.stats.shapiro`, R, MATLAB, etc.) to perform this test.                                                                         |
| **Limitation**                   | The test can be sensitive to sample size. With very large samples, it may reject H₀ for trivial deviations from normality. With very small samples, it may lack the power to detect non-normality. |

**Summary:** The Shapiro-Wilk test is an essential tool in an engineer's statistical toolkit. It provides an objective method to check the critical assumption of normality before applying more advanced parametric statistical techniques. Understanding this test allows you to ensure the validity and reliability of your data-driven conclusions and models. Always remember to use computational tools to perform the actual calculations.
