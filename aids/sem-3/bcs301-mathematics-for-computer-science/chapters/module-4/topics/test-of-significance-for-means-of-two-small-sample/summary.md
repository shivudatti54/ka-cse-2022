# Test of Significance for Means of Two Small Samples

=============================================

## Key Definitions

- **Hypothesis testing**: A statistical method used to make conclusions about a population based on a sample of data.
- **Null hypothesis (H0)**: A statement of no effect or no difference.
- **Alternative hypothesis (H1)**: A statement of an effect or difference.
- **Type I error**: Rejecting the null hypothesis when it is true.
- **Type II error**: Failing to reject the null hypothesis when it is false.

## Key Formulas and Theorems

- **Z-test statistic**: $z = \frac{\bar{X}_1 - \bar{X}_2}{\sigma_p \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}}$, where $\bar{X}_1$ and $\bar{X}_2$ are sample means, $\sigma_p$ is the pooled standard deviation, and $n_1$ and $n_2$ are sample sizes.
- **Pooled standard deviation**: $\sigma_p = \sqrt{\frac{(n_1 - 1)s_1^2 + (n_2 - 1)s_2^2}{n_1 + n_2 - 2}}$, where $s_1$ and $s_2$ are sample standard deviations.
- **Test statistic**: $t = \frac{\bar{X}_1 - \bar{X}_2}{s_p \sqrt{\frac{1}{n_1} + \frac{1}{n_2}}}$, where $s_p$ is the pooled standard deviation.
- **Degrees of freedom**: $df = n_1 + n_2 - 2$.

## Key Points

- Use the Z-test statistic for large samples.
- Use the t-test statistic for small samples.
- Calculate the pooled standard deviation to combine sample variances.
- Specify the alternative hypothesis (e.g., H1: $\mu_1 - \mu_2 \neq 0$).
- Determine the significance level (e.g., $\alpha = 0.05$).
- Choose a critical region (e.g., reject H0 if $z > z_{\alpha}$ or $t > t_{\alpha}$).
- Calculate the p-value to determine the probability of observing the test statistic under the null hypothesis.

## Important Theorems

- **Central Limit Theorem (CLT)**: The sampling distribution of the sample mean is approximately normal with mean $\mu$ and standard deviation $\frac{\sigma}{\sqrt{n}}$.
- **Independence of events**: If two events are independent, the probability of both events occurring is the product of their individual probabilities.
