# **Statistical Machine Learning for Data Science: Chapter 3 Revision Notes**

## **Key Concepts**

- **A/B Testing**: Comparing the performance of two different versions of a product, system, or process to determine which one performs better.
  - Formula: \(p_1 - p_2 > \alpha\) or \(p_1 - p_2 < -\alpha\)
- **Hypothesis Testing**: Testing a hypothesis about a population based on a sample.
  - Formula: \(H_0: \mu = \mu_0\), \(H_1: \mu \neq \mu_0\)
  - Definition: **Null Hypothesis (H0)**: A statement of no effect or no difference.
  - Definition: **Alternative Hypothesis (H1)**: A statement of an effect or difference.
  - Theorem: **Central Limit Theorem (CLT)**: The distribution of sample means approaches a normal distribution as sample size increases.
- **Resampling**: A method of generating multiple samples from a population and re-running analysis on each sample to estimate the variability of the results.
  - Formula: **Bootstrapping**: \(P = \frac{1}{B}\sum\_{i=1}^{B}\mathbf{I}(\text{event})\), where B is the number of bootstrap samples.
- **Statistical Significance**: The probability of obtaining a result at least as extreme as the observed result, assuming that the null hypothesis is true.

## **Important Formulas and Definitions**

- **Standard Error (SE)**: A measure of the variability of a sample mean. \(SE = \frac{\sigma}{\sqrt{n}}\)
- **Margin of Error (ME)**: A measure of the maximum amount by which the sample mean is expected to differ from the population mean. \(ME = SE \times z\_{\alpha/2}\)
- **Confidence Intervals**: A range of values within which the true population parameter is expected to lie. \(CI = \bar{x} \pm ME\)

## **Important Theorems**

- **Central Limit Theorem (CLT)**: The distribution of sample means approaches a normal distribution as sample size increases.
- **Independence Theorem**: The distribution of the sum of independent random variables is the sum of their individual distributions.

## **Quick Revision Tips**

- Understand the difference between a null hypothesis and an alternative hypothesis.
- Recognize the importance of sample size and variability when conducting statistical tests.
- Be familiar with the formulas and concepts of A/B testing, hypothesis testing, and resampling.
