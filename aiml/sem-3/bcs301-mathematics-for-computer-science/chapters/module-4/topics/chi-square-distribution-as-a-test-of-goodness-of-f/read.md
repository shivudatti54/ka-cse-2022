# Chi-Square Distribution as a Test of Goodness of Fit

=====================================================

## Introduction

---

The Chi-Square (χ²) distribution is a fundamental concept in statistics used to test the goodness of fit of a theoretical distribution to a sample of data. In this study material, we will cover the definition, properties, and application of the Chi-Square distribution as a test of goodness of fit.

## Definition and Assumptions

---

- The Chi-Square distribution is a discrete distribution that models the sum of squared standard normal random variables.
- It is used to test the goodness of fit of a theoretical distribution to a sample of data.
- The assumptions for using the Chi-Square distribution include:
  - The data should be categorical (nominal or ordinal).
  - The data should be independent.
  - The expected frequencies should be greater than 5.

## Calculating the Chi-Square Statistic

---

To calculate the Chi-Square statistic, we use the following formula:

χ² = Σ [(observed frequency - expected frequency)^2 / expected frequency]

where:

- χ² is the Chi-Square statistic.
- Σ denotes the sum over all categories.
- observed frequency is the number of observations in each category.
- expected frequency is the number of observations in each category under the null hypothesis.

## Example: Calculating the Chi-Square Statistic

---

Suppose we have a sample of 100 students with the following sex distribution:

| Sex    | Observed Frequency |
| ------ | ------------------ |
| Male   | 60                 |
| Female | 40                 |

We assume that the null hypothesis is that the sex distribution is equal (p = 0.5). The expected frequencies are:

| Sex    | Expected Frequency |
| ------ | ------------------ |
| Male   | 50                 |
| Female | 50                 |

We can calculate the Chi-Square statistic as follows:

χ² = [(60-50)^2/50] + [(40-50)^2/50] = 0.8 + 0.8 = 1.6

## Degrees of Freedom

---

The degrees of freedom for the Chi-Square distribution are calculated as:

df = k - 1

where:

- k is the number of categories.

## Example: Degrees of Freedom

---

Suppose we have a sample of 100 students with the following sex distribution:

| Sex    | Observed Frequency |
| ------ | ------------------ |
| Male   | 60                 |
| Female | 40                 |

We have 2 categories (Male and Female). The degrees of freedom are:

df = 2 - 1 = 1

## Significance Level and Critical Region

---

The significance level (α) is the probability of rejecting the null hypothesis when it is true. The critical region is the region of the Chi-Square distribution where the null hypothesis is rejected.

## Example: Significance Level and Critical Region

---

Suppose we have a Chi-Square distribution with 1 degree of freedom and a significance level of 0.05. The critical region is the upper 0.05 tail of the Chi-Square distribution.

## Conclusion

---

In conclusion, the Chi-Square distribution is a powerful tool for testing the goodness of fit of a theoretical distribution to a sample of data. By calculating the Chi-Square statistic, determining the degrees of freedom, and comparing it to the critical region, we can determine whether the null hypothesis should be rejected.

### Key Concepts

- Chi-Square distribution
- Goodness of fit
- Null hypothesis
- Expected frequencies
- Degrees of freedom
- Significance level
- Critical region

### Example Problems

1.  Calculate the Chi-Square statistic for the following data:
    - | Category | Observed Frequency |
    - | --- | --- |
    - | A | 20 |
    - | B | 30 |
    - | C | 50 |
2.  Determine the degrees of freedom for the following data:
    - | Category | Observed Frequency |
    - | --- | --- |
    - | A | 15 |
    - | B | 25 |
    - | C | 60 |
3.  Calculate the Chi-Square statistic for the following data:
    - | Category | Observed Frequency |
    - | --- | --- |
    - | X | 8 |
    - | Y | 12 |
    - | Z | 80 |
    - | W | 100 |

### Solutions

1.  χ² = [(20-15)^2/15] + [(30-25)^2/25] + [(50-60)^2/60] = 0.1 + 0.4 + 1.0 = 1.5
2.  df = 3 - 1 = 2
3.  χ² = [(8-10)^2/10] + [(12-10)^2/10] + [(80-80)^2/80] + [(100-80)^2/80] = 0.2 + 0.2 + 0 + 5.0 = 5.4
