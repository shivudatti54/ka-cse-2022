# Significance & p-values, t-tests, multiple testing, degrees of freedom

### Definitions

- **p-value**: probability of obtaining a result at least as extreme as the observed result, assuming the null hypothesis is true
- **Degrees of freedom (df)**: measure of the amount of information available for estimating the variance of a statistic, often used in t-tests
- **Hypothesis testing**: statistical method for making inferences about a population parameter based on a sample of data

### Significance Testing

- **Null hypothesis (H0)**: no effect or no difference
- **Alternative hypothesis (H1)**: there is an effect or a difference
- **p-value**: compared to the significance level (α), if p < α, reject H0
- **Significance level (α)**: threshold for rejecting the null hypothesis, typically set at 0.05

### t-tests

- **t-test**: statistical test for comparing the means of two groups
- **Sample size (n)**: number of observations in each group
- **Standard error (SE)**: estimate of the standard deviation of the mean
- **t-statistic**: calculated as (x̄1 - x̄2) / SE
- **p-value**: compared to α, if p < α, reject H0
- **Formula**: t = (x̄1 - x̄2) / (SE \* √(1/n1 + 1/n2))

### Multiple Testing

- **Multiple comparisons correction**: method for adjusting p-values to account for multiple tests
- **Bonferroni correction**: simple method for correcting p-values, adjusts α by dividing by the number of tests
- **Holm-Bonferroni method**: more conservative method for correcting p-values, adjusts α by dividing by the number of tests, then subtracting the previous corrected α

### Degrees of Freedom

- **df = n1 + n2 - 2**, where n1 and n2 are the sample sizes of the two groups
- **df = N - k**, where N is the total sample size and k is the number of parameters estimated

### Theorems

- **Central Limit Theorem (CLT)**: states that the distribution of the sample mean will be approximately normal for large sample sizes, regardless of the underlying distribution
- **Independence Assumption**: states that the observations in the sample should be independent of each other

### Important Formulas

- **t-test formula**: t = (x̄1 - x̄2) / (SE \* √(1/n1 + 1/n2))
- **p-value formula**: p = P(T > t), where T is the t-statistic
- **Degrees of freedom formula**: df = n1 + n2 - 2
