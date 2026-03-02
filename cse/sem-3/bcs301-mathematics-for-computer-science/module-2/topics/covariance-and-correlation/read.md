# Covariance and Correlation: Measuring Joint Variability

## Table of Contents

- [Covariance and Correlation: Measuring Joint Variability](#covariance-and-correlation-measuring-joint-variability)
- [1. Introduction](#1-introduction)
- [2. Core Concepts](#2-core-concepts)
  - [Covariance](#covariance)
  - [Correlation (Pearson Correlation Coefficient)](#correlation-pearson-correlation-coefficient)
- [3. Example](#3-example)
- [4. Key Points & Summary](#4-key-points--summary)

## 1. Introduction

In the study of Joint Probability Distributions (Module 2), we often need to understand the _relationship_ between two random variables, X and Y. Do they tend to move together? If one increases, does the other tend to increase or decrease? Or is there no discernible pattern? Covariance and Correlation are two fundamental statistical measures that provide a precise, quantitative answer to these questions. They are crucial in fields like data science, machine learning, and signal processing, where understanding variable relationships is key.

## 2. Core Concepts

### Covariance

Covariance measures the _direction_ of the linear relationship between two random variables.

- **Definition:** The covariance of two random variables X and Y is the expected value of the product of their deviations from their respective means.
  $$\text{Cov}(X, Y) = E[(X - E[X])(Y - E[Y])]$$
  where \(E[X]\) and \(E[Y]\) are the expected values (means) of X and Y.

- **Simplified Calculation Formula:** A more practical formula for calculation is:
  $$\text{Cov}(X, Y) = E[XY] - E[X]E[Y]$$
  This is often easier to compute from a joint probability distribution.

- **Interpreting the Sign:** The sign of the covariance is its most useful property:
- **Cov(X, Y) > 0 (Positive):** Indicates that as X increases, Y tends to increase.
- **Cov(X, Y) < 0 (Negative):** Indicates that as X increases, Y tends to decrease.
- **Cov(X, Y) = 0 (Zero):** Suggests there is no _linear_ relationship between the variables. They are called **uncorrelated**.

**Limitation of Covariance:** A major drawback of covariance is that its magnitude is not scale-invariant. It depends on the units of measurement of X and Y, making it difficult to interpret the _strength_ of the relationship.

### Correlation (Pearson Correlation Coefficient)

Correlation fixes the scaling problem of covariance. It is a dimensionless measure that quantifies both the _direction_ and _strength_ of the linear relationship between two variables.

- **Definition:** The correlation coefficient, denoted by \(\rho\) (rho) for populations or \(r\) for samples, is the covariance normalized by the product of the standard deviations of the variables.
  $$\rho_{X,Y} = \frac{\text{Cov}(X, Y)}{\sigma_X \sigma_Y}$$
  where \(\sigma_X\) and \(\sigma_Y\) are the standard deviations of X and Y.

- **Properties:**
- **Range:** The value of \(\rho\) always lies between -1 and +1.
- \(\rho = +1\): Perfect positive linear relationship.
- \(\rho = -1\): Perfect negative linear relationship.
- \(\rho = 0\): No linear relationship.
- **Interpretation:** The closer the value is to ±1, the stronger the linear relationship. The sign indicates the direction.

## 3. Example

Let's calculate the covariance and correlation for a simple joint probability distribution.

Consider two discrete random variables, X and Y, with the following joint PMF:

|         | Y=1 | Y=2 | Y=3 |
| :------ | :-- | :-- | :-- |
| **X=1** | 0.1 | 0.2 | 0.1 |
| **X=2** | 0.2 | 0.1 | 0.3 |

**Step 1: Find Marginal Distributions and Means**

- \(P(X=1) = 0.1+0.2+0.1 = 0.4\), \(P(X=2) = 0.2+0.1+0.3 = 0.6\)
  \(E[X] = (1)(0.4) + (2)(0.6) = 1.6\)
- \(P(Y=1) = 0.1+0.2 = 0.3\), \(P(Y=2)=0.2+0.1=0.3\), \(P(Y=3)=0.1+0.3=0.4\)
  \(E[Y] = (1)(0.3) + (2)(0.3) + (3)(0.4) = 2.1\)

**Step 2: Calculate E[XY]**
\(E[XY] = \sum\_{\text{all x,y}} x \cdot y \cdot P(X=x, Y=y)\)
\(= (1)(1)(0.1) + (1)(2)(0.2) + (1)(3)(0.1) + (2)(1)(0.2) + (2)(2)(0.1) + (2)(3)(0.3) \)
\(= 0.1 + 0.4 + 0.3 + 0.4 + 0.4 + 1.8 = 3.4\)

**Step 3: Compute Covariance**
\(\text{Cov}(X, Y) = E[XY] - E[X]E[Y] = 3.4 - (1.6)(2.1) = 3.4 - 3.36 = 0.04\)
A positive value suggests a very weak positive relationship.

**Step 4: Compute Standard Deviations & Correlation**
First, find \(E[X^2] = (1)^2(0.4) + (2)^2(0.6) = 0.4 + 2.4 = 2.8\)
\(\sigma_X = \sqrt{E[X^2] - (E[X])^2} = \sqrt{2.8 - (1.6)^2} = \sqrt{2.8 - 2.56} = \sqrt{0.24} \approx 0.49\)

Similarly, \(E[Y^2] = (1)^2(0.3) + (2)^2(0.3) + (3)^2(0.4) = 0.3 + 1.2 + 3.6 = 5.1\)
\(\sigma_Y = \sqrt{5.1 - (2.1)^2} = \sqrt{5.1 - 4.41} = \sqrt{0.69} \approx 0.83\)

Now, find correlation:
\(\rho = \frac{\text{Cov}(X, Y)}{\sigma_X \sigma_Y} = \frac{0.04}{(0.49)(0.83)} \approx \frac{0.04}{0.4067} \approx 0.098\)

This value is very close to zero, confirming an extremely weak (almost non-existent) positive linear relationship between X and Y in this distribution.

## 4. Key Points & Summary

| Aspect             | Covariance                             | Correlation                                                |
| :----------------- | :------------------------------------- | :--------------------------------------------------------- |
| **Definition**     | \(\text{Cov}(X,Y) = E[XY] - E[X]E[Y]\) | \(\rho = \frac{\text{Cov}(X,Y)}{\sigma_X \sigma_Y}\)       |
| **Measures**       | Direction of linear relationship       | Both **direction** and **strength** of linear relationship |
| **Range**          | \(-\infty\) to \(+\infty\)             | **-1 to +1** (Normalized, dimensionless)                   |
| **Scale**          | Scale-dependent (sensitive to units)   | Scale-invariant (not sensitive to units)                   |
| **Interpretation** | Sign is meaningful, magnitude is not   | Both sign and magnitude are meaningful and interpretable   |

**Crucial Note:** Correlation only measures _linear_ relationships. A correlation of zero does not prove independence; it only means there is no linear dependence. Variables could have a strong non-linear relationship (e.g., parabolic) and still have \(\rho \approx 0\).
