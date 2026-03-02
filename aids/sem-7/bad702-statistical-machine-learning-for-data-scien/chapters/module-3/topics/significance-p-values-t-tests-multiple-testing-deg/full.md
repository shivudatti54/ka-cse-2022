# Significance & p-values, t-tests, multiple testing, degrees of freedom

## Introduction

In the realm of statistical machine learning, testing hypotheses and evaluating the significance of results is crucial for making informed decisions. This module delves into the world of significance testing, covering the concepts of p-values, t-tests, multiple testing, and degrees of freedom. We'll explore the historical context, modern developments, and provide numerous examples, case studies, and applications to solidify your understanding.

### Historical Context

The concept of significance testing dates back to the early 20th century. Karl Pearson, a British statistician, introduced the idea of hypothesis testing in his 1908 paper, "On the method of normal equations in the theory of statistics." However, it wasn't until the 1930s that the p-value was formally introduced by Ronald Fisher and Jerzy Neyman.

The p-value, or probability value, is the probability of observing results at least as extreme as the ones observed during the experiment, assuming that the null hypothesis is true. The null hypothesis is a statement of no effect or no difference, while the alternative hypothesis is a statement of an effect or difference.

### Significance Tests

Significance tests are used to determine whether the observed results are statistically significant, indicating that the null hypothesis can be rejected. There are two types of significance tests:

1.  **One-Sample Tests**: These tests are used to compare the mean of a sample to a known population mean. Examples include the t-test and the z-test.
2.  **Two-Sample Tests**: These tests are used to compare the means of two independent samples. Examples include the independent samples t-test and the two-sample z-test.

### p-values

The p-value is a crucial component of significance testing. It represents the probability of observing results at least as extreme as the ones observed during the experiment, assuming that the null hypothesis is true.

Here's an example to illustrate the concept of p-values:

Suppose we conduct a survey to determine whether the average height of students in a particular school is greater than 175 cm. We collect data from 100 students and find that the average height is 180 cm with a standard deviation of 5 cm. We perform a one-sample t-test to compare the sample mean to the known population mean of 175 cm.

The p-value represents the probability of observing a sample mean of 180 cm or greater, assuming that the true population mean is 175 cm. If the p-value is less than a predetermined significance level (e.g., 0.05), we reject the null hypothesis and conclude that the average height of students in the school is statistically significantly greater than 175 cm.

Here's a diagram illustrating the concept of p-values:

| Hypothesis  | Null Hypothesis | Alternative Hypothesis | p-value  |
| ----------- | --------------- | ---------------------- | -------- |
| H0: μ = 175 | μ ≠ 175         | μ > 175                | P-value  |
| H0: μ = 175 | μ ≠ 175         | μ < 175                | P-value  |
| H0: μ = 175 | μ ≠ 175         | μ = 175                | 0 (or 1) |

### t-tests

The t-test is a type of significance test used to compare the means of two independent samples. It's a widely used test for comparing the means of two groups.

Here's an example to illustrate the concept of t-tests:

Suppose we conduct an experiment to compare the average height of students in two different schools. We collect data from 100 students in each school and find that the average height in School A is 180 cm with a standard deviation of 5 cm, while the average height in School B is 185 cm with a standard deviation of 5 cm. We perform an independent samples t-test to compare the two sample means.

The t-test calculates a test statistic (t) and a p-value, which represents the probability of observing results at least as extreme as the ones observed during the experiment, assuming that the two samples come from populations with the same mean. If the p-value is less than a predetermined significance level (e.g., 0.05), we reject the null hypothesis and conclude that the two schools have significantly different average heights.

Here's a diagram illustrating the concept of t-tests:

| Hypothesis  | Null Hypothesis | Alternative Hypothesis | Test Statistic (t)                      | p-value |
| ----------- | --------------- | ---------------------- | --------------------------------------- | ------- |
| H0: μ1 = μ2 | μ1 ≠ μ2         | μ1 > μ2                | t = (x̄1 - x̄2) / sqrt(s1^2/n1 + s2^2/n2) | P-value |
| H0: μ1 = μ2 | μ1 ≠ μ2         | μ1 < μ2                | t = (x̄1 - x̄2) / sqrt(s1^2/n1 + s2^2/n2) | P-value |

### Multiple Testing

Multiple testing is a concern when conducting multiple significance tests. As the number of tests increases, the probability of observing a significant result by chance alone also increases.

Here's an example to illustrate the concept of multiple testing:

Suppose we conduct 10 experiments to compare the average height of students in 10 different schools. We perform an independent samples t-test for each experiment and find that the p-value is less than 0.05 for each experiment.

If we were to multiply the number of tests by the significance level (e.g., 10 x 0.05 = 0.5), we would expect to observe at least one significant result by chance alone. This highlights the problem of multiple testing and the need to adjust the significance level or use alternative methods to account for the multiple tests.

### Degrees of Freedom

Degrees of freedom (df) is a measure of the amount of information available to estimate the population parameters. In the context of significance tests, df is used to calculate the test statistic and p-value.

Here's an example to illustrate the concept of degrees of freedom:

Suppose we conduct an independent samples t-test to compare the means of two samples. The sample sizes are 100 and 100, and the variances are equal. In this case, the degrees of freedom for the t-test is:

df = n1 + n2 - 2 = 100 + 100 - 2 = 198

The degrees of freedom represents the number of independent observations that are used to estimate the population parameters.

Here's a diagram illustrating the concept of degrees of freedom:

| Hypothesis  | Null Hypothesis | Alternative Hypothesis | Degrees of Freedom (df) |
| ----------- | --------------- | ---------------------- | ----------------------- |
| H0: μ1 = μ2 | μ1 ≠ μ2         | μ1 > μ2                | df = n1 + n2 - 2        |
| H0: μ1 = μ2 | μ1 ≠ μ2         | μ1 < μ2                | df = n1 + n2 - 2        |

### Conclusion

In conclusion, significance testing is a crucial component of statistical machine learning. Understanding the concepts of p-values, t-tests, multiple testing, and degrees of freedom is essential for making informed decisions in a wide range of applications.

### Further Reading

- Fisher, R. A., & Neyman, J. (1935). Tests of significance. Proceedings of the Royal Society of London. Series A, Mathematical and Physical Sciences, 151, 253-304.
- Neyman, J., & Pearson, E. S. (1933). On the use and interpretation of certain tests of significance and of their relation to the theory of probability. Proceedings of the Royal Society of London. Series A, Mathematical and Physical Sciences, 136(820), 286-322.
- Rohlf, F. J. (2019). Introductory Biostatistics: A Modern Approach. Springer.

## Example Use Cases

- A/B Testing: In A/B testing, we want to determine whether a new version of a website is more effective than the current version. We conduct an A/B test by randomly splitting the traffic between the two versions. We collect data on the conversion rate and calculate the p-value to determine whether the difference is statistically significant.
- Hypothesis Testing: In hypothesis testing, we want to determine whether a new medication is effective in treating a particular disease. We conduct a hypothesis test by collecting data on the treatment outcomes and calculating the p-value to determine whether the difference is statistically significant.
- Resampling: In resampling, we want to determine whether a new algorithm is more accurate than the current algorithm. We conduct a resampling test by randomly sampling data from the population and calculating the p-value to determine whether the difference is statistically significant.
