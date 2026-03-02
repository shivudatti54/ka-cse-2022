# **Test of Significance for Means of Two Small Samples**

## **1. Introduction**

In this topic, we will be learning about the test of significance for means of two small samples. This test is used to determine if there is a significant difference between the means of two independent groups.

## **2. Assumptions**

Before performing the test of significance for means of two small samples, we need to check the following assumptions:

- **Independence**: The two samples must be independent of each other.
- **Normality**: The data in both samples must be normally distributed.
- **Equal Variance**: The variances of the two samples must be equal.

If these assumptions are not met, alternative tests may be necessary.

## **3. Types of Tests**

There are two types of tests of significance for means of two small samples:

- **Paired Samples T-Test**: Used when the two samples are paired or matched.
- **Independent Samples T-Test**: Used when the two samples are independent.

## **4. Paired Samples T-Test**

The paired samples t-test is used to determine if there is a significant difference between the means of two related groups.

**Formula:**

μx - μy = (x̄ - ȳ) ± t(1-α/2) \* (s_p \* √(1/n_p + 1/n_m))

where:

- μx and μy are the means of the two samples.
- x̄ and ȳ are the sample means.
- s_p is the pooled standard deviation.
- n_p and n_m are the sample sizes.

**Example:**

Suppose we have two samples of exam scores:

Sample A: 80, 70, 90
Sample B: 75, 85, 95

We want to determine if there is a significant difference between the means of the two samples.

First, we calculate the sample means:

x̄ = (80 + 70 + 90) / 3 = 80
ȳ = (75 + 85 + 95) / 3 = 85

Next, we calculate the pooled standard deviation:

s_p = √(((n_p - 1) \* s_p^2 + (n_m - 1) \* s_m^2) / (n_p + n_m - 2))

where s_p and s_m are the sample standard deviations.

Assuming the sample standard deviations are 10 and 15, respectively, we can calculate the pooled standard deviation:

s_p = √(((3 - 1) \* 10^2 + (3 - 1) \* 15^2) / (3 + 3 - 2)) = √((80 + 270) / 4) = √57.5 = 7.6

Finally, we can calculate the test statistic:

t = (x̄ - ȳ) / (s_p \* √(1/n_p + 1/n_m)) = (80 - 85) / (7.6 \* √(1/3 + 1/3)) = -5 / 5.32 = -0.94

The p-value for this test is approximately 0.342, which is greater than the significance level of 0.05. Therefore, we fail to reject the null hypothesis and conclude that there is no significant difference between the means of the two samples.

## **5. Independent Samples T-Test**

The independent samples t-test is used to determine if there is a significant difference between the means of two independent groups.

**Formula:**

t = (x̄ - ȳ) / (s_p \* √(1/n_p + 1/n_m))

where:

- x̄ and ȳ are the sample means.
- s_p is the pooled standard deviation.
- n_p and n_m are the sample sizes.

**Example:**

Suppose we have two samples of exam scores:

Sample A: 80, 70, 90
Sample B: 75, 85, 95

We want to determine if there is a significant difference between the means of the two samples.

First, we calculate the sample means:

x̄ = (80 + 70 + 90) / 3 = 80
ȳ = (75 + 85 + 95) / 3 = 85

Next, we calculate the pooled standard deviation:

s_p = √(((n_p - 1) \* s_p^2 + (n_m - 1) \* s_m^2) / (n_p + n_m - 2))

where s_p and s_m are the sample standard deviations.

Assuming the sample standard deviations are 10 and 15, respectively, we can calculate the pooled standard deviation:

s_p = √(((3 - 1) \* 10^2 + (3 - 1) \* 15^2) / (3 + 3 - 2)) = √((80 + 270) / 4) = √57.5 = 7.6

Finally, we can calculate the test statistic:

t = (x̄ - ȳ) / (s_p \* √(1/n_p + 1/n_m)) = (80 - 85) / (7.6 \* √(1/3 + 1/3)) = -5 / 5.32 = -0.94

The p-value for this test is approximately 0.342, which is greater than the significance level of 0.05. Therefore, we fail to reject the null hypothesis and conclude that there is no significant difference between the means of the two samples.

## **6. Conclusion**

In conclusion, the test of significance for means of two small samples is a powerful tool for determining if there is a significant difference between the means of two independent or paired groups. By understanding the assumptions, types of tests, and formulas involved, you can apply this test to real-world data to make informed decisions.

**Key Concepts:**

- **Paired Samples T-Test**: Used when the two samples are paired or matched.
- **Independent Samples T-Test**: Used when the two samples are independent.
- **Pooled Standard Deviation**: Used to calculate the standard deviation of the combined sample.
- **Test Statistic**: Used to calculate the difference between the sample means.
- **P-Value**: Used to determine the probability of observing the test statistic under the null hypothesis.
