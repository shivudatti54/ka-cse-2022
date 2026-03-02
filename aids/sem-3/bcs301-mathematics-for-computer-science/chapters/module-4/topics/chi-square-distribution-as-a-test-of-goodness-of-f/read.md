# **Chi-square Distribution as a Test of Goodness of Fit**

## **Introduction**

In statistical inference, a goodness of fit test is used to determine how well observed data fit a known distribution. The chi-square distribution is a widely used test for goodness of fit, and it is an essential concept in statistics for computer science. This study material will cover the definition, calculation, and interpretation of the chi-square distribution as a test of goodness of fit.

## **Definition**

The chi-square distribution is a discrete probability distribution that arises from the distribution of a sum of squares of multiple independent random variables. In the context of goodness of fit testing, the chi-square distribution is used to determine how well observed frequencies match a population distribution.

## **The Chi-square Test**

The chi-square test of goodness of fit is a statistical test that checks whether the observed frequencies in a sample are significantly different from the expected frequencies under a specific null hypothesis. The null hypothesis states that the observed frequencies are consistent with a known population distribution.

## **Null and Alternative Hypotheses**

- Null Hypothesis (H0): The observed frequencies are consistent with a known population distribution.
- Alternative Hypothesis (H1): The observed frequencies are not consistent with a known population distribution.

## **Calculating the Chi-square Statistic**

The chi-square statistic is calculated as follows:

χ² = Σ [(observed frequency - expected frequency)^2 / expected frequency]

where Σ denotes the sum of the squared differences from expected frequencies, divided by the expected frequencies.

## **Interpretation of the Chi-square Statistic**

The chi-square statistic follows a chi-square distribution with k-1 degrees of freedom, where k is the number of categories in the observed data. The degrees of freedom represent the number of parameters estimated in the null hypothesis.

- If the calculated chi-square statistic is less than the critical value from the chi-square distribution with k-1 degrees of freedom, the null hypothesis is not rejected.
- If the calculated chi-square statistic is greater than the critical value, the null hypothesis is rejected.

## **Example**

Suppose we have a sample of exam scores with the following frequencies:

| Score | Frequency |
| ----- | --------- |
| A     | 10        |
| B     | 20        |
| C     | 30        |
| D     | 40        |

We want to test whether the observed frequencies are consistent with a normal distribution. We calculate the expected frequencies under the null hypothesis:

| Score | Expected Frequency           |
| ----- | ---------------------------- |
| A     | (10 + 20 + 30 + 40) / 4 = 15 |
| B     | (10 + 20 + 30 + 40) / 4 = 20 |
| C     | (10 + 20 + 30 + 40) / 4 = 25 |
| D     | (10 + 20 + 30 + 40) / 4 = 30 |

We then calculate the chi-square statistic:

χ² = [(10-15)^2 / 15] + [(20-20)^2 / 20] + [(30-25)^2 / 25] + [(40-30)^2 / 30]
= 2.67 + 0 + 0.67 + 2
= 5.34

With 3 degrees of freedom, the critical value from the chi-square distribution is 7.82. Since our calculated chi-square statistic (5.34) is less than the critical value, we fail to reject the null hypothesis and conclude that the observed frequencies are consistent with a normal distribution.

## **Key Concepts**

- Chi-square distribution
- Goodness of fit test
- Null hypothesis
- Alternative hypothesis
- Chi-square statistic
- Degrees of freedom

## **References**

- "Biostatistics" by Bradley Efron and Larry Wasserman
- "Statistics for Computer Science" by John W. Tukey
