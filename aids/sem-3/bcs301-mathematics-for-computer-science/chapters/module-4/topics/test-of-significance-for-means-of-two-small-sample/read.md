# **Test of Significance for Means of Two Small Samples**

## **Introduction**

In statistical inference, the test of significance for means of two small samples is a statistical method used to compare the means of two groups to determine if there is a significant difference between them. This method is commonly used in computer science to evaluate the effectiveness of different algorithms, software, or hardware.

## **Definitions**

- **Sample mean**: The average value of a dataset.
- **Population mean**: The average value of a population.
- **Sample standard deviation**: A measure of the spread or dispersion of a dataset.
- **Hypothesis testing**: A method used to make conclusions about a population based on a sample of data.

## **The Problem**

When comparing the means of two small samples, we may want to determine if there is a significant difference between them. However, due to the small sample size, the normal distribution assumption may not be met, and the standard error of the difference between the means may be large.

## **The Solution**

To address this problem, we can use the following approach:

- Use a non-parametric test, such as the Wilcoxon signed-rank test or the Mann-Whitney U test, to compare the means of the two samples.
- Alternatively, we can use the paired t-test if the samples are matched or paired.

## **The Paired t-Test**

The paired t-test is a parametric test used to compare the means of two related samples. The test assumes that the samples are paired and that the differences between the pairs are normally distributed.

### Formula

The formula for the paired t-test is as follows:

t = (x̄1 - x̄2) / (s_p \* sqrt(1/n1 + 1/n2))

where:

- x̄1 and x̄2 are the sample means
- s_p is the pooled standard deviation
- n1 and n2 are the sample sizes

### Example

Suppose we want to compare the means of two samples of employees' salaries. The sample means are $50,000 and $60,000, and the sample sizes are 10 and 15, respectively. The pooled standard deviation is 15,000.

Using the formula, we get:

t = (50,000 - 60,000) / (15,000 \* sqrt(1/10 + 1/15))
t = -10,000 / (15,000 \* sqrt(11/30))
t = -10,000 / (15,000 \* 0.475)
t = -2.06

The critical t-value for a two-tailed test with 23 degrees of freedom is approximately 2.069. Since our calculated t-value (-2.06) is less than the critical t-value, we reject the null hypothesis and conclude that there is a significant difference between the two sample means.

## **The Wilcoxon Signed-Rank Test**

The Wilcoxon signed-rank test is a non-parametric test used to compare the means of two related samples. The test does not assume any distribution of the data.

### Formula

The formula for the Wilcoxon signed-rank test is as follows:

W = Σ|d_i|

where:

- d_i is the difference between the paired observations

### Example

Suppose we want to compare the means of two samples of employees' salaries. The paired observations are as follows:

| Employee | Salary |
| -------- | ------ |
| 1        | 50,000 |
| 2        | 55,000 |
| 3        | 60,000 |
| 4        | 65,000 |
| 5        | 70,000 |
| 6        | 75,000 |
| 7        | 80,000 |
| 8        | 85,000 |
| 9        | 90,000 |
| 10       | 95,000 |

We calculate the differences between the paired observations:

| Employee | Difference (d_i) |
| -------- | ---------------- |
| 1        | -5,000           |
| 2        | -10,000          |
| 3        | -15,000          |
| 4        | -20,000          |
| 5        | -25,000          |
| 6        | -30,000          |
| 7        | -35,000          |
| 8        | -40,000          |
| 9        | -45,000          |
| 10       | -50,000          |

We then rank the absolute differences, ignoring tied values:

| d_i    | Rank |
| ------ | ---- |
| 5,000  | 1    |
| 10,000 | 2    |
| 15,000 | 3    |
| 20,000 | 4    |
| 25,000 | 5    |
| 30,000 | 6    |
| 35,000 | 7    |
| 40,000 | 8    |
| 45,000 | 9    |
| 50,000 | 10   |

We then sum the ranks of the positive differences:

W = 1 + 3 + 5 + 7 = 16

The critical value for the Wilcoxon signed-rank test with 10 degrees of freedom is approximately 15. The calculated W-value (16) is greater than the critical value, so we fail to reject the null hypothesis and conclude that there is no significant difference between the two sample means.

## **Key Concepts**

- **Non-parametric tests**: Tests that do not assume any distribution of the data.
- **Paired t-test**: A parametric test used to compare the means of two related samples.
- **Wilcoxon signed-rank test**: A non-parametric test used to compare the means of two related samples.
- **Sample size**: The number of observations in a sample.
- **Standard error of the difference between the means**: A measure of the variability of the difference between the means.

## **Applications**

- **Computer science**: To evaluate the effectiveness of different algorithms, software, or hardware.
- **Business**: To compare the means of two related variables, such as employee salaries or customer satisfaction.
- **Medicine**: To compare the means of two related variables, such as blood pressure or cholesterol levels.
