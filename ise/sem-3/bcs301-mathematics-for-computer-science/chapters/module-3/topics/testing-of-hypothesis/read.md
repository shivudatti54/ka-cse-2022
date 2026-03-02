# Statistical Inference 1: Testing of Hypothesis

## Introduction

In the field of Computer Science, we are constantly inundated with data. From A/B testing website layouts to evaluating the performance of a new machine learning algorithm, we need objective methods to draw meaningful conclusions from this data. Statistical Hypothesis Testing provides a rigorous, mathematical framework for making data-driven decisions. It allows us to test assumptions (hypotheses) about a population parameter (like mean or proportion) based on sample data, quantifying the strength of the evidence rather than relying on intuition.

## Core Concepts

### 1. The Hypotheses

Every hypothesis test involves formulating two mutually exclusive statements:

- **Null Hypothesis ($H_0$):** This is the default assumption, the status quo, or a statement of "no effect" or "no difference." It is always stated with an equality sign ($=$, $\leq$, $\geq$).
  - _Example:_ The new algorithm's average processing time is **equal to** the old one ($\mu_{new} = \mu_{old}$).

- **Alternative Hypothesis ($H_1$ or $H_a$):** This is what the researcher wants to prove. It contradicts the null hypothesis and is a statement of change, difference, or effect.
  - _Example:_ The new algorithm's average processing time is **less than** the old one ($\mu_{new} < \mu_{old}$). This is a _one-tailed_ test.

### 2. Test Statistic

This is a standardized value calculated from the sample data. It measures how far the sample statistic (e.g., sample mean $\bar{x}$) is from the hypothesized population parameter (e.g., $\mu_0$), in terms of standard errors. The formula depends on the parameter being tested.
For a population mean with large samples or known population standard deviation ($\sigma$), the test statistic is a **Z-score**:
$$ Z = \frac{\bar{x} - \mu_0}{\sigma/\sqrt{n}} $$

### 3. Level of Significance ($\alpha$) and p-value

- **Significance Level ($\alpha$):** This is the probability of rejecting the null hypothesis when it is actually true (Type I Error). It's a threshold set by the researcher _before_ conducting the test. Common values are 0.05 (5%) or 0.01 (1%). It defines the critical region.

- **p-value:** This is the probability of obtaining a test statistic _at least as extreme_ as the one observed, assuming the null hypothesis $H_0$ is true. It is the **observed level of significance**.
  - **Decision Rule:** If the p-value $\leq \alpha$, we **reject $H_0$**. The result is statistically significant.
  - If the p-value $> \alpha$, we **fail to reject $H_0$**.

### 4. Types of Errors

Since decisions are based on sample data, errors can occur:
| Decision | $H_0$ is True | $H_0$ is False |
| :--- | :--- | :--- |
| **Reject $H_0$** | Type I Error ($\alpha$) | Correct Decision |
| **Fail to Reject $H_0$** | Correct Decision | Type II Error ($\beta$) |

The power of a test ($1 - \beta$) is the probability of correctly rejecting a false $H_0$.

## Example: One-Sample Z-test

**Scenario:** A cloud server claims its average response time is 50 ms. You suspect it's slower. You sample 100 requests and find a sample mean ($\bar{x}$) of 52 ms. The population standard deviation ($\sigma$) is known to be 10 ms. Test at $\alpha = 0.05$.

**1. Formulate Hypotheses:**

- $H_0: \mu = 50$ ms (The claim is true)
- $H_1: \mu > 50$ ms (The server is slower)

**2. Calculate Test Statistic:**
$$ Z = \frac{\bar{x} - \mu_0}{\sigma/\sqrt{n}} = \frac{52 - 50}{10/\sqrt{100}} = \frac{2}{1} = 2.0 $$

**3. Determine p-value and Conclude:**
The calculated Z-score is 2.0. This is a one-tailed test. The p-value is the area to the _right_ of Z=2.0 under the standard normal curve.
From Z-tables, this area is $P(Z > 2.0) = 1 - 0.9772 = 0.0228$.
Since p-value (0.0228) < $\alpha$ (0.05), we **reject the null hypothesis**.
There is sufficient statistical evidence at the 5% level to conclude that the average response time is greater than 50 ms.

## Key Points & Summary

- **Framework:** Hypothesis testing is a structured process for testing claims about population parameters using sample data.
- **Core Components:** The procedure revolves around defining $H_0$ & $H_1$, choosing $\alpha$, calculating a test statistic, and using the p-value to make an objective decision.
- **p-value is Key:** A small p-value provides strong evidence against the null hypothesis. "Small" is defined by the chosen $\alpha$.
- **Not Proof:** Failing to reject $H_0$ does not prove it is true; it merely means there isn't enough evidence against it.
- **CS Applications:** This is fundamental for tasks like network performance analysis, algorithm comparison, quality assurance in software development, and evaluating models in data science and machine learning.
- **Next Steps:** This introduction often uses the Z-test. The next step is to learn about the t-test (used when $\sigma$ is unknown) and tests for proportions and variances.
