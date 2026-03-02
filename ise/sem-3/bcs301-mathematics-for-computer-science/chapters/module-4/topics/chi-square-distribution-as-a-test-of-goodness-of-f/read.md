# Chi-Square Distribution as a Test of Goodness of Fit

### Introduction

In statistics, the chi-square distribution is a widely used test for determining whether there is a significant difference between observed frequencies and expected frequencies. This study material will cover the concept of goodness of fit, the chi-square distribution, and how to apply it as a test of goodness of fit.

### Goodness of Fit

Goodness of fit refers to the degree to which observed frequencies match expected frequencies in a dataset. A good fit indicates that the observed frequencies are close to the expected frequencies, while a poor fit indicates that the observed frequencies are significantly different from the expected frequencies.

### Chi-Square Distribution

The chi-square distribution is a discrete probability distribution that is commonly used in statistical hypothesis testing. It is used to determine whether observed frequencies are significantly different from expected frequencies. The chi-square distribution is calculated using the following formula:

χ² = Σ [(observed frequency - expected frequency)^2 / expected frequency]

Where:

- χ² is the chi-square statistic
- Σ is the sum of the squared differences between observed and expected frequencies
- observed frequency is the frequency of the observed value
- expected frequency is the frequency of the expected value

### Conditions for Goodness of Fit Test

Before applying the goodness of fit test using the chi-square distribution, the following conditions must be met:

- The data should be categorical and not continuous
- The data should be independent of each other
- The sample size should be sufficiently large
- The expected frequencies should be greater than 5

### Assumptions of Goodness of Fit Test

The goodness of fit test assumes the following:

- The data is randomly sampled from the population
- The data is independent of each other
- The expected frequencies are greater than 5

### Steps to Apply Goodness of Fit Test

To apply the goodness of fit test using the chi-square distribution, follow these steps:

1. **State the null and alternative hypotheses**: The null hypothesis states that the observed frequencies are equal to the expected frequencies, while the alternative hypothesis states that the observed frequencies are not equal to the expected frequencies.
2. **Calculate the expected frequencies**: Calculate the expected frequencies using the formula: expected frequency = (row total \* column total) / grand total
3. **Calculate the chi-square statistic**: Calculate the chi-square statistic using the formula: χ² = Σ [(observed frequency - expected frequency)^2 / expected frequency]
4. **Determine the degrees of freedom**: Determine the degrees of freedom using the formula: degrees of freedom = (number of rows - 1) \* (number of columns - 1)
5. **Obtain the critical value or p-value**: Obtain the critical value or p-value using a chi-square distribution table or calculator
6. **Make a decision**: Make a decision based on the p-value. If the p-value is less than the significance level (usually 0.05), reject the null hypothesis.

### Example

Suppose we have a dataset with the following categories:

| Category | Observed Frequency | Expected Frequency |
| -------- | ------------------ | ------------------ |
| A        | 10                 | 12                 |
| B        | 8                  | 10                 |
| C        | 12                 | 14                 |
| D        | 6                  | 8                  |

To apply the goodness of fit test using the chi-square distribution, we first calculate the expected frequencies using the formula:

| Category | Expected Frequency   |
| -------- | -------------------- |
| A        | (10 \* 24) / 40 = 12 |
| B        | (8 \* 24) / 40 = 10  |
| C        | (12 \* 24) / 40 = 14 |
| D        | (6 \* 24) / 40 = 8   |

Next, we calculate the chi-square statistic using the formula:

χ² = [(10 - 12)^2 / 12] + [(8 - 10)^2 / 10] + [(12 - 14)^2 / 14] + [(6 - 8)^2 / 8]
= 0.44 + 0.16 + 0.07 + 0.25
= 0.92

We then determine the degrees of freedom using the formula:

degrees of freedom = (number of rows - 1) \* (number of columns - 1)
= (4 - 1) \* (2 - 1)
= 3

We obtain the critical value or p-value using a chi-square distribution table or calculator. Suppose the critical value is 7.81 with 3 degrees of freedom. Since the calculated chi-square statistic (0.92) is less than the critical value, we fail to reject the null hypothesis.

### Conclusion

The goodness of fit test using the chi-square distribution is a widely used statistical test for determining whether observed frequencies are significantly different from expected frequencies. By following the steps outlined in this study material, you can apply the goodness of fit test to determine whether your dataset meets the requirements for the test.
