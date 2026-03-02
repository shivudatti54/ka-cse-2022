# Student's t-Distribution

## Introduction

The Student's t-distribution, commonly known as the t-distribution, is one of the most important probability distributions in statistical inference. It was originally discovered by William Sealy Gosset, a chemist working at the Guinness Brewery in Dublin, Ireland, who published his findings under the pseudonym "Student" in 1908. The t-distribution arises naturally when estimating the mean of a normally distributed population in situations where the sample size is small and the population standard deviation is unknown.

In the context of statistical inference, we often need to make conclusions about population parameters based on sample data. When working with large samples (typically n > 30), the Central Limit Theorem allows us to use the normal distribution for inference. However, in many practical scenarios, particularly in experimental sciences, quality testing, and small-scale research studies, we deal with small samples where the normal approximation may not be appropriate. The t-distribution provides the mathematical framework for making valid statistical inferences in such situations, accounting for the additional uncertainty introduced by estimating the population standard deviation from limited sample data.

For DU Computer Science students studying Statistical Inference, understanding the t-distribution is essential because it forms the foundation for hypothesis testing and confidence interval construction in scenarios involving small samples. This knowledge is particularly valuable in data science applications, algorithm analysis, and research methodology.

## Key Concepts

### Origin and Need for t-Distribution

When we have a sample of size n from a normal population with unknown mean μ and unknown variance σ², the sample mean X̄ follows a normal distribution with mean μ and variance σ²/n. However, since σ² is unknown, we must estimate it using the sample variance s². The quantity (n-1)s²/σ² follows a chi-square distribution with (n-1) degrees of freedom. The ratio of these two independent quantities—the standard normal variable (X̄ - μ)/(σ/√n) and the square root of the chi-square variable divided by its degrees of freedom—gives rise to the t-distribution with (n-1) degrees of freedom.

The key insight is that when σ is unknown (which is almost always the case in practice), using the sample standard deviation s instead of the population standard deviation σ introduces additional variability. This additional uncertainty causes the sampling distribution to have heavier tails than the standard normal distribution. The t-distribution accounts for this by having a shape parameter called degrees of freedom that adjusts the distribution's shape based on sample size.

### Definition and Properties

The t-distribution with ν (nu) degrees of freedom is defined as the distribution of the random variable T = Z/√(V/ν), where Z is a standard normal random variable and V is a chi-square random variable with ν degrees of freedom, independent of Z.

The probability density function of the t-distribution with ν degrees of freedom is given by:

f(t) = [Γ((ν+1)/2) / (√(νπ) × Γ(ν/2))] × (1 + t²/ν)^(-(ν+1)/2)

where Γ(.) denotes the gamma function.

The t-distribution has several important properties:

First, it is symmetric about zero, just like the normal distribution. The probability density function is bell-shaped but has heavier tails than the normal distribution. This means extreme values are more likely in a t-distribution compared to a normal distribution.

Second, as the degrees of freedom increase, the t-distribution approaches the standard normal distribution. For ν > 30, the two distributions are nearly identical, which explains why we can use the normal approximation for large samples.

Third, the mean of the t-distribution is zero for ν > 1, and the variance is ν/(ν-2) for ν > 2. The variance is always greater than 1 and approaches 1 as degrees of freedom increase.

### Degrees of Freedom

The degrees of freedom (df) in the t-distribution represent the number of independent observations used to estimate the population variance. For a sample of size n, we typically have n-1 degrees of freedom because we lose one degree of freedom when estimating the population mean using the sample mean. This concept is crucial because it determines which t-distribution to use in any given statistical procedure.

When comparing two independent samples, the degrees of freedom are calculated differently depending on whether the two populations have equal or unequal variances. For equal variances (pooled t-test), the degrees of freedom are n₁ + n₂ - 2. For unequal variances (Welch's t-test), we use a more complex formula that accounts for the different variances.

### One-Sample t-Test

The one-sample t-test is used to test hypotheses about the population mean when the population standard deviation is unknown. The test statistic is calculated as:

t = (X̄ - μ₀) / (s/√n)

where X̄ is the sample mean, μ₀ is the hypothesized population mean, s is the sample standard deviation, and n is the sample size.

This test statistic follows a t-distribution with n-1 degrees of freedom under the null hypothesis. We compare the calculated t-value with the critical t-value from the t-distribution table at the chosen significance level to make a decision about the null hypothesis.

### Two-Sample t-Test

The two-sample t-test extends the one-sample case to compare means from two independent populations. There are two variants depending on whether the variances of the two populations are assumed equal or unequal.

For the equal variance case (pooled t-test), we first calculate a pooled estimate of the common variance using both samples, then compute the test statistic using this pooled variance. The degrees of freedom in this case are n₁ + n₂ - 2.

For the unequal variance case (Welch's t-test), we do not pool the variances and use a modified formula for the test statistic. The degrees of freedom are calculated using Welch-Satterthwaite approximation, which accounts for the different variances and sample sizes.

### Confidence Intervals using t-Distribution

Just as we use the t-distribution for hypothesis testing, we also use it for constructing confidence intervals when the population standard deviation is unknown. A (1-α) × 100% confidence interval for the population mean μ is given by:

X̄ ± t(α/2, n-1) × (s/√n)

where t(α/2, n-1) is the critical t-value with n-1 degrees of freedom that leaves an area of α/2 in each tail of the t-distribution.

The width of the confidence interval depends on three factors: the sample standard deviation (more variability leads to wider intervals), the sample size (larger samples lead to narrower intervals), and the confidence level (higher confidence leads to wider intervals).

### Relationship to Other Distributions

The t-distribution is intimately connected to other important distributions in statistical inference. As mentioned earlier, when the degrees of freedom ν approaches infinity, the t-distribution converges to the standard normal distribution. The t-distribution can also be related to the F-distribution through the relationship that t² with ν degrees of freedom follows an F-distribution with 1 and ν degrees of freedom in the numerator and denominator respectively.

## Examples

### Example 1: One-Sample t-Test

A computer science professor claims that the average time taken by students to complete a programming assignment is 45 minutes. A random sample of 15 students was selected, and their completion times (in minutes) were recorded: 52, 48, 55, 43, 47, 51, 44, 49, 53, 46, 50, 54, 42, 56, 45. Using α = 0.05, test whether the professor's claim is justified.

Solution:

First, calculate the sample statistics:

Sample size: n = 15
Sample mean: X̄ = (52+48+55+43+47+51+44+49+53+46+50+54+42+56+45)/15 = 735/15 = 49

To calculate the sample standard deviation, we need the squared deviations from the mean. Computing these:

(52-49)² = 9, (48-49)² = 1, (55-49)² = 36, (43-49)² = 36, (47-49)² = 4, (51-49)² = 4, (44-49)² = 25, (49-49)² = 0, (53-49)² = 16, (46-49)² = 9, (50-49)² = 1, (54-49)² = 25, (42-49)² = 49, (56-49)² = 49, (45-49)² = 16

Sum of squared deviations = 9+1+36+36+4+4+25+0+16+9+1+25+49+49+16 = 280

Sample variance: s² = 280/(15-1) = 280/14 = 20
Sample standard deviation: s = √20 = 4.47

Calculate the test statistic:
t = (X̄ - μ₀)/(s/√n) = (49 - 45)/(4.47/√15) = 4/(4.47/3.87) = 4/1.15 = 3.48

Degrees of freedom: df = n-1 = 14

Critical value: For α = 0.05 (two-tailed) with df = 14, t(0.025, 14) = 2.145

Since |3.48| > 2.145, we REJECT the null hypothesis. There is sufficient evidence at the 5% significance level to conclude that the average completion time is different from 45 minutes. The professor's claim is NOT justified.

### Example 2: Confidence Interval for Population Mean

A software company wants to estimate the average memory usage (in MB) of a particular application. A sample of 10 runs was taken, and the memory usage values were: 128, 135, 142, 129, 138, 131, 144, 127, 140, 133. Construct a 95% confidence interval for the true average memory usage.

Solution:

Sample size: n = 10

Sample mean: X̄ = (128+135+142+129+138+131+144+127+140+133)/10 = 1347/10 = 134.7

Calculate sample standard deviation:
Deviations from mean: -6.7, 0.3, 7.3, -5.7, 3.3, -3.7, 9.3, -7.7, 5.3, -1.7
Squared deviations: 44.89, 0.09, 53.29, 32.49, 10.89, 13.69, 86.49, 59.29, 28.09, 2.89
Sum = 332.1

Sample variance: s² = 332.1/(10-1) = 332.1/9 = 36.9
Sample standard deviation: s = √36.9 = 6.07

Degrees of freedom: df = 10-1 = 9

Critical t-value: For 95% confidence level with df = 9, t(0.025, 9) = 2.262

Margin of error: t × (s/√n) = 2.262 × (6.07/√10) = 2.262 × 1.92 = 4.34

95% Confidence Interval: 134.7 ± 4.34 = (130.36, 139.04)

Interpretation: We are 95% confident that the true average memory usage of the application lies between 130.36 MB and 139.04 MB.

### Example 3: Paired t-Test

A data analyst wants to test whether a new optimization technique reduces the execution time (in milliseconds) of a data processing algorithm. The execution times before and after optimization for 8 different datasets are recorded:

Before: 245, 198, 267, 189, 224, 256, 201, 238
After: 228, 185, 251, 178, 209, 239, 190, 221

Using α = 0.01, test whether the optimization technique significantly reduces execution time.

Solution:

This is a paired design, so we use the paired t-test. First, calculate the differences (Before - After):

245-228 = 17, 198-185 = 13, 267-251 = 16, 189-178 = 11, 224-209 = 15, 256-239 = 17, 201-190 = 11, 238-221 = 17

Sample statistics for differences:
n = 8, mean difference: d̄ = (17+13+16+11+15+17+11+17)/8 = 117/8 = 14.625

Standard deviation of differences:
Squared deviations from mean: (17-14.625)² = 5.64, (13-14.625)² = 2.64, (16-14.625)² = 1.89, (11-14.625)² = 13.14, (15-14.625)² = 0.14, (17-14.625)² = 5.64, (11-14.625)² = 13.14, (17-14.625)² = 5.64
Sum = 47.67
s² = 47.67/(8-1) = 6.81
s = √6.81 = 2.61

Test statistic: t = d̄/(s/√n) = 14.625/(2.61/√8) = 14.625/0.92 = 15.90

Degrees of freedom: df = 8-1 = 7

Critical value: For α = 0.01 (one-tailed) with df = 7, t(0.01, 7) = 2.998

Since 15.90 > 2.998, we REJECT the null hypothesis. There is strong evidence at the 1% significance level that the optimization technique significantly reduces execution time.

## Exam Tips

For DU semester examinations on Student's t-distribution, keep the following points in mind:

1. ALWAYS check whether the population standard deviation is known or unknown. If unknown (which is the typical case), you MUST use the t-distribution rather than the z-distribution.

2. Remember that degrees of freedom determine which specific t-distribution to use. For a one-sample test, df = n-1. For two independent samples with equal variances, df = n₁ + n₂ - 2. Always specify the degrees of freedom when reading or using t-tables.

3. The t-distribution approaches the normal distribution as sample size increases. For practical purposes, when n > 30, you can use the normal approximation. However, this does not mean you should always use z-tests for n > 30—it depends on whether σ is known.

4. In hypothesis testing, clearly state the null and alternative hypotheses. For two-tailed tests, the rejection region is in both tails. For one-tailed tests, identify whether it is left-tailed or right-tailed based on the alternative hypothesis.

5. When constructing confidence intervals using t-distribution, remember that the critical value t(α/2, df) depends on both the confidence level and the degrees of freedom. Higher confidence levels and smaller sample sizes lead to larger critical values and hence wider intervals.

6. For paired designs, ALWAYS use the paired t-test rather than the two-sample t-test. The differences must be calculated first, then the one-sample t-test is applied to these differences.

7. The assumption of normality is important for valid t-test results. For small samples (n < 30), you should check for normality using graphical methods or normality tests. For large samples, the t-test is robust to moderate departures from normality.

8. In practical exam questions, pay attention to whether the test is one-tailed or two-tailed, as this affects both the critical value and the p-value calculation. The decision rule should clearly state the rejection criterion.

9. When comparing two means, check whether the variances can be assumed equal. Use Levene's test or Bartlett's test if required. If variances are unequal, use Welch's t-test which does not assume equal variances.

10. Understand the relationship between t-distribution and other distributions: t² with ν df follows F(1, ν) distribution. This relationship is useful in ANOVA and regression analysis.