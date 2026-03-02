# **Chi-Square Distribution as a Test of Goodness of Fit**

## **Introduction**

In statistical inference, a goodness of fit test is used to determine whether a population's distribution of data is consistent with a hypothesized distribution. The chi-square distribution is a widely used test statistic for goodness of fit, and is an essential tool in many fields, including computer science, medicine, and social sciences. In this section, we will delve into the historical context, mathematical foundations, and practical applications of the chi-square distribution as a test of goodness of fit.

## **Historical Context**

The chi-square distribution has its roots in the works of Karl Pearson, an English statistician who developed the chi-square test of goodness of fit in the early 20th century [1]. Pearson's test was designed to test the hypothesis that a population's distribution of data was consistent with a specific distribution, such as a normal distribution or a binomial distribution. The test statistic, which is now known as the chi-square statistic, is calculated as the sum of the squared differences between observed and expected frequencies.

## **Mathematical Foundations**

Let's consider a simple example to illustrate the concept of the chi-square distribution. Suppose we want to test whether a population's distribution of exam scores is consistent with a normal distribution. We collect a sample of exam scores and calculate the expected frequencies under the assumption that the data follows a normal distribution. We then calculate the chi-square statistic as follows:

χ² = Σ [(observed frequency - expected frequency)² / expected frequency]

where χ² is the chi-square statistic, observed frequency is the actual frequency of each score, and expected frequency is the frequency under the assumption of a normal distribution.

The chi-square distribution is a continuous probability distribution that is used to approximate the distribution of the chi-square statistic. The distribution has a symmetric, bell-shaped curve, with a single peak at the mean (0).

## **Properties of the Chi-Square Distribution**

The chi-square distribution has several important properties that make it a useful test statistic:

- The chi-square distribution is symmetric around the mean (0).
- The chi-square distribution is skewed to the right, meaning that it is more likely to take on larger values.
- The chi-square distribution has a single peak, which corresponds to the mean (0).

## **Calculating the Chi-Square Statistic**

To calculate the chi-square statistic, we need to calculate the expected frequencies under the assumption of a specific distribution. The expected frequencies can be calculated using the following formula:

expected frequency = (observed frequency \* total sample size) / total expected frequency

where total sample size is the total number of observations in the sample, and total expected frequency is the sum of the expected frequencies for all categories.

Once we have calculated the expected frequencies, we can calculate the chi-square statistic using the following formula:

χ² = Σ [(observed frequency - expected frequency)² / expected frequency]

## **Interpretation of the Chi-Square Statistic**

The chi-square statistic is used to determine whether the observed frequencies are significantly different from the expected frequencies. The critical region for the chi-square distribution is typically in the right tail (i.e., values greater than the critical value). If the calculated chi-square statistic falls within the critical region, we reject the null hypothesis that the population's distribution of data is consistent with the hypothesized distribution.

## **Example: Testing a Normal Distribution**

Suppose we want to test whether a population's distribution of exam scores is consistent with a normal distribution. We collect a sample of exam scores and calculate the observed frequencies as follows:

| Exam Score | Observed Frequency |
| ---------- | ------------------ |
| 60-69      | 10                 |
| 70-79      | 20                 |
| 80-89      | 30                 |
| 90-99      | 40                 |

Assuming a normal distribution, we calculate the expected frequencies as follows:

| Exam Score | Expected Frequency |
| ---------- | ------------------ |
| 60-69      | 15                 |
| 70-79      | 25                 |
| 80-89      | 35                 |
| 90-99      | 45                 |

We then calculate the chi-square statistic as follows:

χ² = [(10-15)² / 15] + [(20-25)² / 25] + [(30-35)² / 35] + [(40-45)² / 45]
= 0.53 + 0.4 + 0.2 + 0.1
= 1.44

Using a chi-square distribution table or calculator, we find that the critical value for χ² with 3 degrees of freedom is approximately 7.81. Since our calculated chi-square statistic (1.44) is less than the critical value, we fail to reject the null hypothesis that the population's distribution of exam scores is consistent with a normal distribution.

## **Case Study: Goodness of Fit Test for a Binomial Distribution**

Suppose we want to test whether a population's distribution of coin tosses is consistent with a binomial distribution. We collect a sample of 10 coin tosses and calculate the observed frequencies as follows:

| Number of Heads | Observed Frequency |
| --------------- | ------------------ |
| 0               | 1                  |
| 1               | 2                  |
| 2               | 3                  |
| 3               | 2                  |
| 4               | 1                  |
| 5               | 1                  |

Assuming a binomial distribution with a probability of success equal to 0.5, we calculate the expected frequencies as follows:

| Number of Heads | Expected Frequency |
| --------------- | ------------------ |
| 0               | 1.25               |
| 1               | 2.5                |
| 2               | 3.75               |
| 3               | 2.5                |
| 4               | 1.25               |
| 5               | 1.25               |

We then calculate the chi-square statistic as follows:

χ² = [(1-1.25)² / 1.25] + [(2-2.5)² / 2.5] + [(3-3.75)² / 3.75] + [(2-2.5)² / 2.5] + [(1-1.25)² / 1.25] + [(1-1.25)² / 1.25]
= 0.2 + 0.2 + 0.2 + 0.2 + 0.2 + 0.2
= 1.2

Using a chi-square distribution table or calculator, we find that the critical value for χ² with 6 degrees of freedom is approximately 12.59. Since our calculated chi-square statistic (1.2) is less than the critical value, we fail to reject the null hypothesis that the population's distribution of coin tosses is consistent with a binomial distribution.

## **Applications of the Chi-Square Distribution**

The chi-square distribution has many applications in various fields, including:

- **Goodness of fit tests**: The chi-square distribution is used to test whether a population's distribution of data is consistent with a hypothesized distribution.
- **Hypothesis testing**: The chi-square distribution is used to test hypotheses about a population's distribution of data.
- **Regression analysis**: The chi-square distribution is used to test the significance of regression coefficients.
- **Time series analysis**: The chi-square distribution is used to test the significance of time series patterns.

## **Software Implementation**

The chi-square distribution can be implemented using various software packages, including:

- **R**: The `chisq.test()` function in R can be used to calculate the chi-square statistic and test the significance of a hypothesized distribution.
- **Python**: The `scipy.stats` module in Python can be used to calculate the chi-square statistic and test the significance of a hypothesized distribution.
- **MATLAB**: The `chisqtest()` function in MATLAB can be used to calculate the chi-square statistic and test the significance of a hypothesized distribution.

## **Further Reading**

- **Pearson, K. (1900). On the influence of early treatment on the results of medical and surgical treatment. Proceedings of the Royal Society of London, 72, 542-548.**
- **Fisher, R. A. (1922). On the 'probable error' of a coefficient of correlation deduced from a sample. Proceedings of the Royal Society of London, 115, 107-118.**
- **Agresti, A. (1996). An introduction to categorical data analysis. John Wiley & Sons.**
- **Hogg, R. V., & Ledford, A. T. (1997). Introduction to probability and statistical inference. Brooks/Cole Publishing Company.**
