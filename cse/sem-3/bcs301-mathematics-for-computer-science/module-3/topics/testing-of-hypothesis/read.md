# Statistical Inference: Hypothesis Testing

## Table of Contents

- [Statistical Inference: Hypothesis Testing](#statistical-inference-hypothesis-testing)
- [Introduction](#introduction)
- [Core Concepts of Hypothesis Testing](#core-concepts-of-hypothesis-testing)
  - [1. The Hypotheses](#1-the-hypotheses)
  - [2. Test Statistic](#2-test-statistic)
  - [3. Significance Level ($\alpha$)](#3-significance-level-alpha)
  - [4. p-value](#4-p-value)
  - [5. Decision and Conclusion](#5-decision-and-conclusion)
- [Example: One-Sample t-test](#example-one-sample-t-test)
- [Key Points & Summary](#key-points--summary)

## Introduction

In **Statistical Inference**, we use data from a sample to draw conclusions about a larger population. **Hypothesis Testing** is a core procedure in this domain. It is a formal, statistical method used to validate or reject an assumption (a _hypothesis_) about a population parameter (like a mean or proportion) based on sample data. This is crucial in fields like A/B testing for software, machine learning model evaluation, network performance analysis, and data-driven decision making.

## Core Concepts of Hypothesis Testing

### 1. The Hypotheses

Every hypothesis test involves two opposing statements:

- **Null Hypothesis ($H_0$):** This is the hypothesis of "no effect," "no difference," or the status quo. It is a statement of equality ($=$, $\leq$, $\geq$). For example, $H_0: \mu = 100$ (the true mean CPU usage is 100 ms).
- **Alternative Hypothesis ($H_1$ or $H_a$):** This is what the researcher wants to prove. It is a statement of inequality ($\neq$, $<$, $>$). It contradicts the null hypothesis. For example, $H_1: \mu > 100$ (the true mean CPU usage is greater than 100 ms).

The goal of the test is to determine whether there is sufficient evidence from the sample data to **reject the null hypothesis** $H_0$ in favor of the alternative hypothesis $H_1$.

### 2. Test Statistic

A test statistic is a standardized value calculated from the sample data. It measures how far the sample statistic is from the null hypothesis value, in terms of standard errors. The formula depends on the parameter being tested (e.g., z-statistic for large sample means, t-statistic for small sample means).

### 3. Significance Level ($\alpha$)

The significance level, denoted by $\alpha$ (alpha), is the probability of making a **Type I Error**. A Type I error occurs when we reject the null hypothesis when it is actually true. It is the threshold for how much risk we are willing to take of being wrong in this way. Common choices are $\alpha = 0.05$ (5%) or $\alpha = 0.01$ (1%).

### 4. p-value

The **p-value** is the probability of obtaining a test statistic _at least as extreme_ as the one observed, assuming the null hypothesis $H_0$ is true.

- A **small p-value** (typically $\leq \alpha$) indicates that the observed data is very unlikely under the null hypothesis. This provides strong evidence _against_ $H_0$, so we **reject $H_0$**.
- A **large p-value** ($> \alpha$) indicates that the observed data is likely under the null hypothesis. We **fail to reject $H_0$**.

### 5. Decision and Conclusion

The final step is to compare the p-value to the chosen significance level $\alpha$ and make a decision:

- If **p-value $\leq \alpha$**: Reject the null hypothesis $H_0$.
- If **p-value $> \alpha$**: Do not reject the null hypothesis $H_0$.

Your conclusion should always be stated in the context of the original problem.

---

## Example: One-Sample t-test

**Scenario:** A new algorithm is claimed to reduce the average page load time on a website. The historical average load time is 3.2 seconds. After implementing the new algorithm, a sample of 25 page loads has an average ($\bar{x}$) of 2.9 seconds with a sample standard deviation ($s$) of 0.5 seconds. Test the claim at the $\alpha = 0.05$ level.

**Step 1: Formulate Hypotheses**

- $H_0: \mu = 3.2$ seconds (The new algorithm made no improvement)
- $H_1: \mu < 3.2$ seconds (The new algorithm reduced the average load time)
  _This is a **left-tailed test**._

**Step 2: Calculate the Test Statistic**
We use the t-statistic because the population standard deviation is unknown and the sample size is small ($n=25$).
$$ t = \frac{\bar{x} - \mu}{s / \sqrt{n}} = \frac{2.9 - 3.2}{0.5 / \sqrt{25}} = \frac{-0.3}{0.1} = -3.0 $$
Degrees of freedom (df) = $n - 1 = 24$.

**Step 3: Find the p-value**
For a left-tailed t-test with $t = -3.0$ and $df = 24$, we find the area in the left tail. Using a t-distribution table or software, we find the p-value is approximately **0.003**.

**Step 4: Make a Decision**
Compare the p-value (0.003) to $\alpha$ (0.05). Since $0.003 < 0.05$, we **reject the null hypothesis $H_0$**.

**Step 5: State Conclusion**
There is sufficient evidence at the 0.05 significance level to conclude that the new algorithm has reduced the average page load time.

---

## Key Points & Summary

- **Purpose:** Hypothesis testing is a structured process for testing claims about population parameters using sample data.
- **Null Hypothesis ($H_0$):** The default assumption to be tested (always has an equality sign).
- **Alternative Hypothesis ($H_1$):** The claim we are trying to find evidence for.
- **Significance Level ($\alpha$):** The threshold for rejecting $H_0$. It's the maximum acceptable probability of a Type I error (rejecting a true $H_0$).
- **p-value:** The probability of seeing your results _if $H_0$ is true_. A small p-value is evidence against $H_0$.
- **Decision Rule:** If p-value $\leq \alpha$, reject $H_0$. If p-value $> \alpha$, fail to reject $H_0$.
- **Conclusion:** Always state your conclusion in the context of the original problem. "Rejecting $H_0$" is not the same as "proving $H_1$ is true." It means the sample data provides strong evidence in favor of $H_1$.
