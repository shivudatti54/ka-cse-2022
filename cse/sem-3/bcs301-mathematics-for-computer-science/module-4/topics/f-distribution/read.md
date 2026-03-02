# F-Distribution

## Table of Contents

- [F-Distribution](#f-distribution)
- [Introduction](#introduction)
- [Definition of the F-Distribution](#definition-of-the-f-distribution)
  - [Intuition](#intuition)
- [Probability Density Function (PDF)](#probability-density-function-pdf)
- [Properties of the F-Distribution](#properties-of-the-f-distribution)
  - [1. Non-Negative Values](#1-non-negative-values)
  - [2. Asymmetric (Positively Skewed)](#2-asymmetric-positively-skewed)
  - [3. Shape Depends on Both Degrees of Freedom](#3-shape-depends-on-both-degrees-of-freedom)
  - [4. Mean](#4-mean)
  - [5. Variance](#5-variance)
  - [6. Mode](#6-mode)
  - [7. Reciprocal Property](#7-reciprocal-property)
  - [8. Relationship to Other Distributions](#8-relationship-to-other-distributions)
- [F-Table Usage](#f-table-usage)
  - [How to Read the F-Table](#how-to-read-the-f-table)
  - [Decision Rule](#decision-rule)
  - [Important Notes on F-Tables](#important-notes-on-f-tables)
- [F-Test for Equality of Two Variances](#f-test-for-equality-of-two-variances)
  - [Setup](#setup)
  - [Hypotheses](#hypotheses)
  - [Test Statistic](#test-statistic)
  - [Decision](#decision)
- [Worked Examples](#worked-examples)
  - [Example 1: F-Test for Equality of Two Variances](#example-1-f-test-for-equality-of-two-variances)
  - [Example 2: One-Tailed F-Test](#example-2-one-tailed-f-test)
  - [Example 3: Computing Mean and Variance of an F-Distribution](#example-3-computing-mean-and-variance-of-an-f-distribution)
- [Applications of the F-Distribution](#applications-of-the-f-distribution)
  - [1. Analysis of Variance (ANOVA)](#1-analysis-of-variance-anova)
  - [2. Regression Analysis](#2-regression-analysis)
  - [3. Comparing Variability](#3-comparing-variability)
  - [4. Equality of Variances Assumption Check](#4-equality-of-variances-assumption-check)
- [Summary Table](#summary-table)
- [Exam Tips](#exam-tips)

## Introduction

The F-distribution (also called the Fisher-Snedecor distribution) is a continuous probability distribution that arises frequently in statistical inference, particularly in the analysis of variance (ANOVA) and in testing the equality of two population variances. It is named after Sir Ronald A. Fisher, who first described it, and George W. Snedecor, who popularized its use.

The F-distribution plays a central role in Module 4 (Statistical Inference) of BCS301, as it extends the ideas of sampling distributions (like the chi-square and t-distributions) to problems involving the comparison of variability across two or more populations.

---

## Definition of the F-Distribution

If X1 and X2 are two **independent** chi-square random variables with degrees of freedom d1 and d2 respectively, then the random variable

```
F = (X1 / d1) / (X2 / d2)
```

follows an **F-distribution with d1 (numerator) and d2 (denominator) degrees of freedom**, written as:

```
F ~ F(d1, d2)
```

Here:

- **d1** = degrees of freedom of the numerator (also called df1 or v1)
- **d2** = degrees of freedom of the denominator (also called df2 or v2)

### Intuition

The F-distribution measures the ratio of two variance estimates. If two populations truly have the same variance, the ratio of their sample variances will cluster around 1. The F-distribution tells us how likely different ratio values are under that assumption.

---

## Probability Density Function (PDF)

The probability density function of the F-distribution with parameters d1 and d2 is:

```
f(x; d1, d2) = [sqrt( ((d1 * x)^d1 * d2^d2) / (d1 * x + d2)^(d1+d2) )] / [x * B(d1/2, d2/2)]
```

where:

- x > 0
- B(a, b) is the **Beta function**: B(a, b) = Gamma(a) \* Gamma(b) / Gamma(a + b)
- Gamma() is the Gamma function

Equivalently, using the Beta function form:

```
f(x; d1, d2) = (1 / B(d1/2, d2/2)) * (d1/d2)^(d1/2) * x^(d1/2 - 1) * (1 + (d1/d2)*x)^(-(d1+d2)/2)
```

for x > 0, and f(x) = 0 for x <= 0.

---

## Properties of the F-Distribution

### 1. Non-Negative Values

The F-distribution is defined only for x >= 0. Since it is a ratio of two positive quantities (mean squares), it cannot take negative values.

### 2. Asymmetric (Positively Skewed)

The F-distribution is **right-skewed** (positively skewed). It is not symmetric about any value. The skewness decreases as both d1 and d2 increase.

### 3. Shape Depends on Both Degrees of Freedom

The shape of the F-distribution changes with different combinations of d1 and d2:

- Small d1 and d2: Highly skewed with a long right tail
- Large d1 and d2: Approaches a symmetric, bell-shaped curve (approximates the normal distribution)

### 4. Mean

The mean of the F-distribution exists only when d2 > 2:

```
Mean = E(F) = d2 / (d2 - 2), for d2 > 2
```

Note that the mean depends **only on d2** (the denominator degrees of freedom) and is always slightly greater than 1.

### 5. Variance

The variance exists only when d2 > 4:

```
Var(F) = [2 * d2^2 * (d1 + d2 - 2)] / [d1 * (d2 - 2)^2 * (d2 - 4)], for d2 > 4
```

### 6. Mode

The mode exists when d1 > 2:

```
Mode = [(d1 - 2) / d1] * [d2 / (d2 + 2)], for d1 > 2
```

### 7. Reciprocal Property

If F ~ F(d1, d2), then:

```
1/F ~ F(d2, d1)
```

This means the reciprocal of an F-distributed variable is also F-distributed, but with the degrees of freedom swapped.

### 8. Relationship to Other Distributions

- **Chi-square distribution:** If X ~ chi-square(d), then X/d approaches 1 as d grows. The F-distribution is built from two such chi-square variables.
- **t-distribution:** If T ~ t(n), then T^2 ~ F(1, n). The square of a t-distributed variable with n degrees of freedom follows an F-distribution with 1 and n degrees of freedom.
- **Normal distribution approximation:** For large d1 and d2, the F-distribution approaches a normal distribution.

---

## F-Table Usage

The F-table provides **critical values** of the F-distribution for given significance levels (alpha), d1, and d2.

### How to Read the F-Table

1. **Choose the significance level** (commonly alpha = 0.05 or 0.01).
2. **Identify d1** (numerator degrees of freedom) -- this determines the **column**.
3. **Identify d2** (denominator degrees of freedom) -- this determines the **row**.
4. **Look up the critical value** F_alpha(d1, d2) at the intersection.

### Decision Rule

For a right-tailed test at significance level alpha:

- If the computed F-statistic > F_alpha(d1, d2), **reject H0**.
- If the computed F-statistic <= F_alpha(d1, d2), **fail to reject H0**.

### Important Notes on F-Tables

- F-tables are typically one-tailed (right-tail).
- For a **two-tailed** test at significance level alpha, use F\_(alpha/2) for the upper critical value.
- For the lower critical value: F*(1-alpha/2)(d1, d2) = 1 / F*(alpha/2)(d2, d1) (reciprocal property).

---

## F-Test for Equality of Two Variances

The most common application of the F-distribution at this level is testing whether two populations have equal variances.

### Setup

Given two independent random samples:

- Sample 1: size n1, sample variance s1^2, from a normal population with variance sigma1^2
- Sample 2: size n2, sample variance s2^2, from a normal population with variance sigma2^2

### Hypotheses

**Two-tailed test:**

- H0: sigma1^2 = sigma2^2 (the two population variances are equal)
- H1: sigma1^2 != sigma2^2

**One-tailed test (right-tailed):**

- H0: sigma1^2 <= sigma2^2
- H1: sigma1^2 > sigma2^2

### Test Statistic

```
F = s1^2 / s2^2
```

where by convention, the **larger sample variance** is placed in the numerator so that F >= 1.

Under H0, this statistic follows:

```
F ~ F(d1, d2)
```

where d1 = n1 - 1 and d2 = n2 - 1.

### Decision

- **Right-tailed test:** Reject H0 if F > F_alpha(d1, d2).
- **Two-tailed test:** Reject H0 if F > F\_(alpha/2)(d1, d2).

---

## Worked Examples

### Example 1: F-Test for Equality of Two Variances

**Problem:** Two machines produce bolts. A sample of 10 bolts from Machine A has a variance of 0.045 mm^2, and a sample of 8 bolts from Machine B has a variance of 0.018 mm^2. At the 5% significance level, test whether the two machines produce bolts with equal variance.

**Solution:**

**Step 1: State the hypotheses.**

- H0: sigma_A^2 = sigma_B^2 (equal variances)
- H1: sigma_A^2 != sigma_B^2 (two-tailed test)

**Step 2: Identify given data.**

- n1 = 10, s1^2 = 0.045 (Machine A -- larger variance goes in numerator)
- n2 = 8, s2^2 = 0.018 (Machine B)
- alpha = 0.05

**Step 3: Compute degrees of freedom.**

- d1 = n1 - 1 = 10 - 1 = 9
- d2 = n2 - 1 = 8 - 1 = 7

**Step 4: Compute the F-statistic.**

```
F = s1^2 / s2^2 = 0.045 / 0.018 = 2.5
```

**Step 5: Find the critical value from F-table.**
For a two-tailed test at alpha = 0.05, we use alpha/2 = 0.025.
From the F-table: F_0.025(9, 7) = 4.82 (approximately).

**Step 6: Make the decision.**
Since F = 2.5 < 4.82, we **fail to reject H0**.

**Conclusion:** At the 5% level of significance, there is no sufficient evidence to conclude that the variances of the two machines are different.

---

### Example 2: One-Tailed F-Test

**Problem:** A company claims that the variability of scores on a training exam is lower for Method B than for Method A. A random sample of 16 trainees using Method A has a sample variance of 120, and a random sample of 21 trainees using Method B has a sample variance of 50. Test the company's claim at the 5% significance level.

**Solution:**

**Step 1: State the hypotheses.**

- H0: sigma_A^2 <= sigma_B^2 (Method A variance is not greater)
- H1: sigma_A^2 > sigma_B^2 (Method A has greater variance, i.e., Method B is less variable)

**Step 2: Identify given data.**

- n1 = 16, s1^2 = 120 (Method A -- larger variance in numerator)
- n2 = 21, s2^2 = 50 (Method B)
- alpha = 0.05

**Step 3: Compute degrees of freedom.**

- d1 = n1 - 1 = 16 - 1 = 15
- d2 = n2 - 1 = 21 - 1 = 20

**Step 4: Compute the F-statistic.**

```
F = s1^2 / s2^2 = 120 / 50 = 2.4
```

**Step 5: Find the critical value from the F-table.**
For a one-tailed test at alpha = 0.05:
From the F-table: F_0.05(15, 20) = 2.20 (approximately).

**Step 6: Make the decision.**
Since F = 2.4 > 2.20, we **reject H0**.

**Conclusion:** At the 5% level of significance, there is sufficient evidence to support the company's claim that Method B has lower variability than Method A.

---

### Example 3: Computing Mean and Variance of an F-Distribution

**Problem:** Find the mean and variance of the F-distribution with d1 = 6 and d2 = 10.

**Solution:**

**Mean:**

```
E(F) = d2 / (d2 - 2) = 10 / (10 - 2) = 10 / 8 = 1.25
```

(Valid since d2 = 10 > 2.)

**Variance:**

```
Var(F) = [2 * d2^2 * (d1 + d2 - 2)] / [d1 * (d2 - 2)^2 * (d2 - 4)]
 = [2 * 100 * (6 + 10 - 2)] / [6 * 64 * 6]
 = [2 * 100 * 14] / [6 * 64 * 6]
 = 2800 / 2304
 = 1.2153 (approximately)
```

(Valid since d2 = 10 > 4.)

---

## Applications of the F-Distribution

### 1. Analysis of Variance (ANOVA)

ANOVA uses the F-test to determine whether there are statistically significant differences among the means of three or more groups. The F-statistic in ANOVA is:

```
F = Mean Square Between Groups (MSB) / Mean Square Within Groups (MSW)
```

If this ratio is significantly large, it indicates that at least one group mean differs from the others.

### 2. Regression Analysis

In multiple regression, the overall F-test checks whether at least one predictor variable has a non-zero coefficient:

```
F = (SSR / k) / (SSE / (n - k - 1))
```

where SSR = sum of squares due to regression, SSE = sum of squares due to error, k = number of predictors, and n = total observations.

### 3. Comparing Variability

In quality control and manufacturing, the F-test is used to compare the variability of two processes or machines to ensure consistency.

### 4. Equality of Variances Assumption Check

Before performing a two-sample t-test, the F-test can be used to verify the assumption that the two populations have equal variances (homoscedasticity).

---

## Summary Table

| Property      | Formula / Value                                     |
| ------------- | --------------------------------------------------- |
| Parameters    | d1 (numerator df), d2 (denominator df)              |
| Support       | x >= 0                                              |
| Mean          | d2 / (d2 - 2), for d2 > 2                           |
| Variance      | 2*d2^2*(d1+d2-2) / [d1*(d2-2)^2*(d2-4)], for d2 > 4 |
| Mode          | [(d1-2)/d1] \* [d2/(d2+2)], for d1 > 2              |
| Skewness      | Right-skewed (positive)                             |
| Reciprocal    | If F ~ F(d1,d2), then 1/F ~ F(d2,d1)                |
| Relation to t | If T ~ t(n), then T^2 ~ F(1,n)                      |

---

## Exam Tips

1. **Always place the larger variance in the numerator** when computing the F-statistic for a variance comparison test. This ensures F >= 1 and simplifies the use of right-tailed F-tables.
2. **Remember the degrees of freedom:** d1 = n1 - 1 (numerator), d2 = n2 - 1 (denominator). Do not confuse which is which.
3. **Two-tailed vs. one-tailed:** For a two-tailed test, use alpha/2 when looking up the critical value in the F-table.
4. **Know the mean formula:** E(F) = d2 / (d2 - 2). This is a frequently tested short-answer question.
5. **Connection to t-distribution:** T^2 = F(1, n) is a commonly asked relationship.
6. **State conclusions clearly:** Always write the conclusion in the context of the problem, not just "reject" or "fail to reject."
