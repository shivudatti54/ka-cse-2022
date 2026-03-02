# Chi-square Distribution as a Test of Goodness of Fit

## Table of Contents

1. [Introduction](#introduction)
2. [Historical Context](#historical-context)
3. [Definition and Properties](#definition-and-properties)
4. [The Chi-square Test of Goodness of Fit](#the-chi-square-test-of-goodness-of-fit)
5. [Assumptions and Limitations](#assumptions-and-limitations)
6. [Calculating the Chi-square Statistic](#calculating-the-chi-square-statistic)
7. [Interpreting the Results](#interpreting-the-results)
8. [Example and Case Studies](#example-and-case-studies)
9. [Applications and Modern Developments](#applications-and-modern-developments)
10. [Further Reading](#further-reading)

## Introduction

The Chi-square distribution is a fundamental concept in statistics that has numerous applications in data analysis, quality control, and machine learning. It is often used as a test of goodness of fit, which involves determining whether a set of observed frequencies in a sample significantly differ from the expected frequencies under a specific hypothesis. In this document, we will delve into the historical context, definition, properties, and applications of the Chi-square distribution as a test of goodness of fit.

## Historical Context

The Chi-square distribution has its roots in the work of Karl Pearson, an English mathematician and statistician, who introduced the concept of the Chi-square test of goodness of fit in the late 19th century. Pearson's work built upon earlier research by Francis Galton and Karl Pearson's collaboration on the study of the distribution of frequencies in a sample. The Chi-square test of goodness of fit gained popularity in the mid-20th century with the development of modern statistical theory and the availability of computational power.

## Definition and Properties

The Chi-square distribution is a discrete distribution that models the sum of squared differences between observed and expected frequencies. Let $X$ be a random variable that represents the number of successes in a sample, and $p$ be the probability of success. The expected frequency of successes for a given number of observations $n$ is given by $np$. The observed frequency of successes is denoted by $x$.

The Chi-square statistic is calculated as follows:

$$\chi^2 = \sum_{i=1}^k \frac{(x_i - np_i)^2}{np_i}$$

where $x_i$ is the observed frequency of the $i^{th}$ category, $np_i$ is the expected frequency of the $i^{th}$ category, and $k$ is the number of categories.

The Chi-square distribution has several key properties:

- The Chi-square distribution is an asymptotic distribution, meaning that it converges to a normal distribution as the sample size increases.
- The Chi-square distribution is symmetric about the mean, which is the number of degrees of freedom.
- The Chi-square distribution is always positive, meaning that it cannot take on negative values.

## The Chi-square Test of Goodness of Fit

The Chi-square test of goodness of fit is a statistical test that determines whether a set of observed frequencies in a sample significantly differ from the expected frequencies under a specific hypothesis. The null hypothesis typically states that the observed frequencies are consistent with the expected frequencies, while the alternative hypothesis states that the observed frequencies differ from the expected frequencies.

The test involves the following steps:

1.  Calculate the Chi-square statistic using the observed and expected frequencies.
2.  Determine the degrees of freedom, which is the number of categories minus one.
3.  Consult a Chi-square distribution table or use a statistical software package to obtain the critical value or p-value associated with the calculated Chi-square statistic.
4.  Compare the calculated Chi-square statistic to the critical value or p-value to determine whether the null hypothesis can be rejected.

## Assumptions and Limitations

The Chi-square test of goodness of fit assumes that the following conditions are met:

- The observed frequencies are non-negative and sum to the sample size.
- The expected frequencies are non-negative and sum to the sample size.
- The observed frequencies are consistent with the expected frequencies under the null hypothesis.
- The number of categories is less than or equal to the sample size.

However, there are several limitations to the Chi-square test of goodness of fit:

- The test assumes that the data are independent, which may not be the case in many real-world scenarios.
- The test does not account for non-normality of the data, which can lead to inaccurate results.
- The test can be sensitive to outliers, which can affect the accuracy of the results.

## Calculating the Chi-square Statistic

The Chi-square statistic can be calculated using the following formula:

$$\chi^2 = \sum_{i=1}^k \frac{(x_i - np_i)^2}{np_i}$$

where $x_i$ is the observed frequency of the $i^{th}$ category, $np_i$ is the expected frequency of the $i^{th}$ category, and $k$ is the number of categories.

## Interpreting the Results

The results of the Chi-square test of goodness of fit can be interpreted as follows:

- If the calculated Chi-square statistic is less than the critical value, the null hypothesis can be rejected, indicating that the observed frequencies differ significantly from the expected frequencies.
- If the calculated Chi-square statistic is greater than the critical value, the null hypothesis cannot be rejected, indicating that the observed frequencies are consistent with the expected frequencies.
- If the calculated Chi-square statistic is equal to the critical value, the null hypothesis is inconclusive, and further testing may be required.

## Example and Case Studies

### Example 1: Testing a Hypothesis about the Distribution of Exam Scores

Suppose we want to test the hypothesis that the distribution of exam scores is normal. We collect a sample of 100 exam scores and calculate the expected frequencies under the null hypothesis. We then calculate the Chi-square statistic using the observed and expected frequencies.

| Exam Score | Observed Frequency | Expected Frequency |
| ---------- | ------------------ | ------------------ |
| 60-69      | 15                 | 12.5               |
| 70-79      | 25                 | 20.0               |
| 80-89      | 30                 | 25.0               |
| 90-99      | 10                 | 10.0               |

The calculated Chi-square statistic is:

$$\chi^2 = \frac{(15 - 12.5)^2}{12.5} + \frac{(25 - 20.0)^2}{20.0} + \frac{(30 - 25.0)^2}{25.0} + \frac{(10 - 10.0)^2}{10.0} = 4.32$$

We consult a Chi-square distribution table and find that the critical value for 3 degrees of freedom is 7.81. Since the calculated Chi-square statistic (4.32) is less than the critical value, we reject the null hypothesis and conclude that the distribution of exam scores is not normal.

### Example 2: Testing a Hypothesis about the Distribution of Customer Satisfaction

Suppose we want to test the hypothesis that the distribution of customer satisfaction is binomial. We collect a sample of 100 customer surveys and calculate the observed and expected frequencies. We then calculate the Chi-square statistic using the observed and expected frequencies.

| Customer Satisfaction | Observed Frequency | Expected Frequency |
| --------------------- | ------------------ | ------------------ |
| 1                     | 10                 | 9.5                |
| 2                     | 20                 | 19.0               |
| 3                     | 30                 | 29.5               |
| 4                     | 20                 | 19.0               |

The calculated Chi-square statistic is:

$$\chi^2 = \frac{(10 - 9.5)^2}{9.5} + \frac{(20 - 19.0)^2}{19.0} + \frac{(30 - 29.5)^2}{29.5} + \frac{(20 - 19.0)^2}{19.0} = 0.63$$

We consult a Chi-square distribution table and find that the critical value for 3 degrees of freedom is 7.81. Since the calculated Chi-square statistic (0.63) is less than the critical value, we reject the null hypothesis and conclude that the distribution of customer satisfaction is not binomial.

## Applications and Modern Developments

The Chi-square test of goodness of fit has numerous applications in various fields, including:

- Quality control: The Chi-square test is used to determine whether a set of observed frequencies in a sample significantly differ from the expected frequencies under a specific hypothesis.
- Machine learning: The Chi-square test is used to evaluate the goodness of fit of a model to a set of data.
- Data analysis: The Chi-square test is used to determine whether a set of observed frequencies in a sample significantly differ from the expected frequencies under a specific hypothesis.

Recent developments in the field of machine learning have led to the development of alternative methods for evaluating the goodness of fit of a model, including:

- Cross-validation: Cross-validation is a technique used to evaluate the performance of a model on unseen data.
- Information criterion: Information criterion is a technique used to evaluate the goodness of fit of a model based on the amount of information it provides about the data.

## Further Reading

- "Karl Pearson: The Last of the Greats" by R. C. Burrows
- "The Chi-Squared Test: A Review" by J. A. B. Francis
- "The Chi-Squared Distribution: A Review" by A. S. Haldane
- "Machine Learning: A Statistical Perspective" by C. M. Bishop
- "Information Criteria for Model Selection" by J. M. Hurvich and C. H. Tsai
