# Chi-Square Distribution as a Test of Goodness of Fit

## Table of Contents

- [Chi-Square Distribution as a Test of Goodness of Fit](#chi-square-distribution-as-a-test-of-goodness-of-fit)
- [Introduction](#introduction)
- [Core Concepts Explained](#core-concepts-explained)
  - [1. The Chi-Square Distribution](#1-the-chi-square-distribution)
  - [2. The Goodness of Fit Test](#2-the-goodness-of-fit-test)
  - [3. The Test Statistic](#3-the-test-statistic)
  - [4. Degrees of Freedom](#4-degrees-of-freedom)
  - [5. Decision Rule](#5-decision-rule)
- [Example: Testing a Fair Die](#example-testing-a-fair-die)
- [Key Points & Summary](#key-points--summary)

## Introduction

In Module 4 of Mathematics for Computer Science, we venture into **Statistical Inference**, which allows us to make conclusions about a population based on sample data. A crucial part of this is **hypothesis testing**. One specific and powerful test is the **Chi-Square ($\chi^2$) Test of Goodness of Fit**. This test is used to determine how well a set of observed sample data matches a theoretical or expected distribution. For computer scientists, this is invaluable in areas like data analysis, machine learning (e.g., evaluating classifier performance), network traffic modeling, and testing the randomness of algorithms.

## Core Concepts Explained

### 1. The Chi-Square Distribution

The $\chi^2$ distribution is a continuous probability distribution defined for positive values. It is characterized by its **degrees of freedom (df)**, which is its only parameter. The shape of the distribution is skewed to the right, but as the degrees of freedom increase, it becomes more symmetrical and approaches a normal distribution.

### 2. The Goodness of Fit Test

The "Goodness of Fit" test assesses whether the observed frequency distribution of a categorical variable differs significantly from a hypothesized theoretical distribution (e.g., Uniform, Binomial, Poisson, or a custom distribution).

**The Null and Alternative Hypotheses:**

- **$H_0$:** The observed data follows the hypothesized/theoretical distribution.
- **$H_1$:** The observed data does _not_ follow the hypothesized distribution.

### 3. The Test Statistic

The cornerstone of the test is the $\chi^2$ test statistic, calculated as:

$$\chi^2 = \sum \frac{(O_i - E_i)^2}{E_i}$$

Where:

- $O_i$ = Observed frequency for category $i$
- $E_i$ = Expected frequency for category $i$ (under the null hypothesis)
- The summation $\sum$ is over all categories $i = 1, 2, ..., k$

This formula quantifies the total discrepancy between what we observed ($O_i$) and what we expected ($E_i$) under the null hypothesis. A large value of the $\chi^2$ statistic indicates a large discrepancy, providing evidence against $H_0$.

### 4. Degrees of Freedom

The degrees of freedom for the goodness of fit test are crucial for determining the critical value from the $\chi^2$ distribution table. It is calculated as:
$$df = k - 1 - p$$
Where:

- $k$ = number of categories (or classes)
- $p$ = number of parameters estimated from the sample data to calculate the expected frequencies.

For many common tests (e.g., testing against a uniform distribution where no parameters are estimated), $p=0$, so $df = k - 1$.

### 5. Decision Rule

1. Calculate the test statistic $\chi^2$ using the formula.
2. Choose a **significance level** $\alpha$ (commonly 0.05 or 5%).
3. Find the **critical value** $\chi^2_{\alpha, df}$ from the $\chi^2$ distribution table.
4. Compare the calculated $\chi^2$ statistic to the critical value:

- If $\chi^2_{calculated} > \chi^2_{critical}$: **Reject $H_0$.** The observed distribution does not fit the expected distribution.
- If $\chi^2_{calculated} \le \chi^2_{critical}$: **Do not reject $H_0$.** There is no significant evidence that the observed distribution differs from the expected one.

---

## Example: Testing a Fair Die

A die is rolled 60 times. We want to test if the die is fair at a 5% significance level ($\alpha = 0.05$).

**Step 1: Hypotheses**

- $H_0$: The die is fair. The observed frequencies follow a uniform distribution.
- $H_1$: The die is not fair.

**Step 2: Collect Observed Data and Calculate Expected Frequencies**
For a fair die, the probability for each face is $1/6$. The expected frequency for each face is $60 \times (1/6) = 10$.

| Face (i) | Observed ($O_i$) | Expected ($E_i$) |
| :------: | :--------------: | :--------------: |
|    1     |        8         |        10        |
|    2     |        12        |        10        |
|    3     |        9         |        10        |
|    4     |        11        |        10        |
|    5     |        10        |        10        |
|    6     |        10        |        10        |

**Step 3: Compute the $\chi^2$ Test Statistic**

$$
\chi^2 = \sum \frac{(O_i - E_i)^2}{E_i} = \frac{(8-10)^2}{10} + \frac{(12-10)^2}{10} + \frac{(9-10)^2}{10} + \frac{(11-10)^2}{10} + \frac{(10-10)^2}{10} + \frac{(10-10)^2}{10}
$$

$$
\chi^2 = \frac{4}{10} + \frac{4}{10} + \frac{1}{10} + \frac{1}{10} + 0 + 0 = 1.0
$$

**Step 4: Determine Degrees of Freedom and Critical Value**

- Number of categories $k = 6$
- No parameters were estimated ($p=0$), so $df = k - 1 = 5$.
- From the $\chi^2$ table, the critical value for $df=5$ and $\alpha=0.05$ is $\chi^2_{critical} = 11.070$.

**Step 5: Make a Decision**
Since $\chi^2_{calculated} = 1.0 < 11.070 = \chi^2_{critical}$, we **fail to reject $H_0$**.

**Conclusion:** There is no significant evidence at the 5% level to conclude that the die is unfair. The observed data fits the distribution of a fair die.

---

## Key Points & Summary

- **Purpose:** The $\chi^2$ goodness of fit test is used to check if observed sample data conforms to an expected theoretical probability distribution.
- **Test Statistic:** $\chi^2 = \sum \frac{(O_i - E_i)^2}{E_i}$. It measures the total squared difference between observed and expected values, normalized by the expected values.
- **Decision Making:** Compare the calculated $\chi^2$ statistic to a critical value from the $\chi^2$ distribution table. Reject the null hypothesis ($H_0$) if the calculated value is larger.
- **Degrees of Freedom:** $df = k - 1 - p$. Correctly calculating $df$ is essential for finding the right critical value.
- **Assumptions:** The test requires a sufficiently large sample size. A common rule is that all expected frequencies ($E_i$) should be at least 5. For smaller samples, other tests may be more appropriate.
- **CS Applications:** This test is fundamental in data science for evaluating model fit, analyzing survey results, testing A/B scenarios in web development, and validating assumptions in machine learning algorithms.
