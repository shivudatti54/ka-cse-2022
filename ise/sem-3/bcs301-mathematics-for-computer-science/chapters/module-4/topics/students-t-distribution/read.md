# Student's t-Distribution

## Introduction

The Student's t-distribution, commonly referred to as the t-distribution, is one of the most fundamental probability distributions in statistical inference. It was originally discovered by William Sealy Gosset, a chemist working at the Guinness Brewery in Dublin, Ireland, who published his findings under the pseudonym "Student" in 1908. The t-distribution arises when estimating the mean of a normally distributed population in situations where the sample size is small and the population standard deviation is unknown.

In the context of statistical inference for Computer Science students, the t-distribution plays a critical role in hypothesis testing and confidence interval construction when working with small samples. Unlike the normal distribution, the t-distribution has heavier tails, which accounts for the additional uncertainty introduced when estimating the population standard deviation from sample data. This characteristic makes it particularly valuable in real-world scenarios where large samples are not always feasible, such as in A/B testing of software features, performance benchmarking of algorithms, and analysis of experimental data from controlled studies.

The t-distribution approaches the standard normal distribution as the degrees of freedom increase, providing a natural bridge between small-sample and large-sample statistical methods. This property ensures that practitioners can use a unified framework for statistical inference regardless of sample size, which is particularly important in computational applications where efficiency and consistency of methods matter.

## Key Concepts

### Definition and Probability Density Function

The Student's t-distribution is defined by a single parameter called degrees of freedom, denoted by ν (nu). When we have a sample of size n drawn from a normal population, the degrees of freedom equal n - 1. This reduction by one occurs because we use the sample data to estimate the population standard deviation, thereby consuming one degree of freedom.

The probability density function (PDF) of the t-distribution with ν degrees of freedom is given by:

f(t) = Γ((ν+1)/2) / (√(νπ) × Γ(ν/2)) × (1 + t²/ν)^(-(ν+1)/2)

where Γ() represents the gamma function. This formula might appear complex, but in practice, statisticians rely on t-tables or computational functions to obtain probabilities and critical values.

### Properties of the t-Distribution

The t-distribution possesses several important properties that make it mathematically tractable and practically useful. First, it is symmetric around zero, just like the standard normal distribution. This symmetry implies that the mean, median, and mode of the distribution are all zero. Second, the variance of the t-distribution exists only when ν > 2, and it equals ν/(ν-2) for those degrees of freedom. For ν ≤ 2, the variance is infinite, reflecting the heavy-tailed nature of the distribution.

The shape of the t-distribution depends critically on the degrees of freedom parameter. With very few degrees of freedom (such as ν = 1 or ν = 2), the distribution has extremely heavy tails, meaning that extreme values occur with much higher probability than under the normal distribution. As the degrees of freedom increase, the t-distribution becomes increasingly concentrated around zero and approaches the standard normal distribution. By the time we reach ν = 30, the two distributions are nearly indistinguishable for most practical purposes.

### Relationship to Sampling Distribution

The theoretical foundation of the t-distribution lies in the ratio of two random variables: a standard normal variable divided by the square root of an independent chi-square variable divided by its degrees of freedom. Mathematically, if Z is a standard normal random variable and V is a chi-square random variable with ν degrees of freedom, then T = Z / √(V/ν) follows a t-distribution with ν degrees of freedom.

In practical sampling theory, this relationship manifests when we consider the sampling distribution of the t-statistic. Suppose we draw a random sample of size n from a normal population with unknown mean μ and unknown standard deviation σ. The t-statistic is computed as:

t = (x̄ - μ) / (s/√n)

where x̄ is the sample mean, s is the sample standard deviation, and n is the sample size. This t-statistic follows a t-distribution with n - 1 degrees of freedom, regardless of the actual values of μ and σ, provided the population is normally distributed.

### The t-Test

The primary application of the t-distribution is in conducting hypothesis tests about population means. There are three main variants of the t-test: one-sample t-test, two-sample independent t-test, and paired t-test. Each variant uses the t-distribution to determine whether observed differences between sample statistics and population parameters (or between two samples) are statistically significant.

In a one-sample t-test, we compare the sample mean to a known or hypothesized population mean. The test statistic follows a t-distribution with n - 1 degrees of freedom under the null hypothesis. For example, if a software company claims that their new algorithm has an average execution time of 50 milliseconds, and we test this claim using a sample of 15 runs, we would use a one-sample t-test to determine whether the sample evidence supports or contradicts the claim.

The two-sample independent t-test compares means from two independent samples, such as comparing the execution times of two different algorithms. The degrees of freedom for this test depend on both sample sizes and are typically calculated using Welch's formula when the population variances cannot be assumed equal. The paired t-test, on the other hand, applies when the samples are related or matched, such as measuring the same set of algorithms on the same test data before and after optimization.

### Confidence Intervals using t-Distribution

Beyond hypothesis testing, the t-distribution is essential for constructing confidence intervals for population means when the population standard deviation is unknown. A (1 - α) × 100% confidence interval for the population mean μ is given by:

x̄ ± t(α/2, n-1) × (s/√n)

where t(α/2, n-1) is the critical t-value with n - 1 degrees of freedom that leaves an area of α/2 in each tail of the distribution. The width of this confidence interval depends on the sample standard deviation, the sample size, and the chosen confidence level. Larger samples and smaller confidence levels produce narrower intervals, providing more precise estimates of the population mean.

## Examples

### Example 1: One-Sample t-Test

A data science student claims that the average processing time for a machine learning model on a particular dataset is 120 seconds. To test this claim, a researcher collects data from 10 independent runs of the model and obtains the following processing times (in seconds): 118, 122, 119, 125, 121, 117, 123, 120, 124, 119. Using α = 0.05, test whether the average processing time differs significantly from 120 seconds.

**Step 1: State the hypotheses**

H₀: μ = 120 seconds (null hypothesis)
H₁: μ ≠ 120 seconds (alternative hypothesis, two-tailed test)

**Step 2: Calculate sample statistics**

Sample mean: x̄ = (118 + 122 + 119 + 125 + 121 + 117 + 123 + 120 + 124 + 119) / 10 = 120.8 seconds

First, compute deviations from mean: -2.8, 1.2, -1.8, 4.2, 0.2, -3.8, 2.2, -0.8, 3.2, -1.8

Squared deviations: 7.84, 1.44, 3.24, 17.64, 0.04, 14.44, 4.84, 0.64, 10.24, 3.24

Sum of squared deviations = 63.6

Sample variance: s² = 63.6 / (10 - 1) = 63.6 / 9 = 7.067

Sample standard deviation: s = √7.067 = 2.66 seconds

**Step 3: Compute the t-statistic**

t = (x̄ - μ) / (s/√n) = (120.8 - 120) / (2.66/√10) = 0.8 / 0.84 = 0.952

**Step 4: Determine critical value**

Degrees of freedom: df = n - 1 = 9

For a two-tailed test with α = 0.05 and df = 9, the critical t-values are ±2.262 (from t-table)

**Step 5: Make decision**

Since |t| = 0.952 < 2.262, we fail to reject the null hypothesis.

**Conclusion:** At the 5% significance level, there is insufficient evidence to conclude that the average processing time differs from 120 seconds. The student's claim is supported by the sample data.

### Example 2: Confidence Interval for Mean

A computer science professor wants to estimate the average time students take to complete a programming assignment. A random sample of 12 students yields the following completion times (in minutes): 45, 52, 48, 55, 50, 47, 53, 49, 51, 46, 54, 50. Construct a 95% confidence interval for the population mean completion time.

**Step 1: Calculate sample statistics**

Sample sum: 45 + 52 + 48 + 55 + 50 + 47 + 53 + 49 + 51 + 46 + 54 + 50 = 590

Sample mean: x̄ = 590 / 12 = 49.17 minutes

Deviations from mean: -4.17, 2.83, -1.17, 5.83, 0.83, -2.17, 3.83, -0.17, 1.83, -3.17, 4.83, 0.83

Squared deviations: 17.39, 8.01, 1.37, 34.01, 0.69, 4.71, 14.67, 0.03, 3.35, 10.05, 23.33, 0.69

Sum = 117.30

Sample variance: s² = 117.30 / (12 - 1) = 117.30 / 11 = 10.66

Sample standard deviation: s = √10.66 = 3.27 minutes

**Step 2: Find critical t-value**

Degrees of freedom: df = 12 - 1 = 11

For 95% confidence level with df = 11, t(0.025, 11) = 2.201

**Step 3: Calculate margin of error**

Margin of error = t × (s/√n) = 2.201 × (3.27/√12) = 2.201 × 0.944 = 2.08 minutes

**Step 4: Construct confidence interval**

95% CI: 49.17 ± 2.08 = (47.09, 51.25) minutes

**Interpretation:** We are 95% confident that the true average completion time for all students lies between 47.09 and 51.25 minutes.

### Example 3: Two-Sample Independent t-Test

A software company wants to compare the memory usage of two different image compression algorithms. Algorithm A is tested on 8 images, yielding mean memory usage of 256 MB with a standard deviation of 18 MB. Algorithm B is tested on 10 images, yielding mean memory usage of 238 MB with a standard deviation of 22 MB. Test whether there is a significant difference in mean memory usage between the two algorithms at α = 0.05. Assume the population variances are equal.

**Step 1: State the hypotheses**

H₀: μ₁ = μ₂ (no difference in mean memory usage)
H₁: μ₁ ≠ μ₂ (significant difference exists)

**Step 2: Calculate pooled standard deviation**

Since we assume equal variances, we need to calculate the pooled variance:

s²p = ((n₁ - 1)s₁² + (n₂ - 1)s₂²) / (n₁ + n₂ - 2)
     = ((8 - 1)(18)² + (10 - 1)(22)²) / (8 + 10 - 2)
     = (7 × 324 + 9 × 484) / 16
     = (2268 + 4356) / 16
     = 6624 / 16
     = 414

Pooled standard deviation: sp = √414 = 20.35 MB

**Step 3: Compute t-statistic**

t = (x̄₁ - x̄₂) / (sp × √(1/n₁ + 1/n₂))
  = (256 - 238) / (20.35 × √(1/8 + 1/10))
  = 18 / (20.35 × √(0.125 + 0.10))
  = 18 / (20.35 × √0.225)
  = 18 / (20.35 × 0.474)
  = 18 / 9.65
  = 1.865

**Step 4: Determine degrees of freedom and critical value**

df = n₁ + n₂ - 2 = 8 + 10 - 2 = 16

For two-tailed test with α = 0.05 and df = 16, critical value = ±2.120

**Step 5: Make decision**

Since |t| = 1.865 < 2.120, we fail to reject H₀.

**Conclusion:** At the 5% significance level, there is no statistically significant difference in mean memory usage between Algorithm A and Algorithm B. The observed difference of 18 MB could have occurred by chance.

## Exam Tips

WHEN SOLVING T-DISTRIBUTION PROBLEMS IN EXAMS, ALWAYS FIRST IDENTIFY THE TYPE OF TEST (ONE-SAMPLE, TWO-SAMPLE, OR PAIRED) AND THE CORRESPONDING DEGREES OF freedom formula. For one-sample tests, df = n - 1; for two-sample tests with equal variances, df = n₁ + n₂ - 2; for paired samples, df = n - 1 where n is the number of pairs.

REMEMBER THAT THE T-DISTRIBUTION IS SYMMETRIC, which means P(T > t) = P(T < -t). This property simplifies probability calculations and helps in understanding two-tailed tests. When reading t-tables, note that most tables provide right-tail probabilities, so you may need to adjust for one-tailed versus two-tailed tests.

KNOW THE RELATIONSHIP BETWEEN T-DISTRIBUTION AND NORMAL DISTRIBUTION: as degrees of freedom increase beyond 30, the t-distribution closely approximates the standard normal distribution. In many practical situations with large samples, z-values and t-values can be used interchangeably, though using the t-distribution is always correct when σ is unknown.

FOR CONFIDENCE INTERVALS, ALWAYS CHECK WHETHER YOU SHOULD USE T OR Z. Use t when the population standard deviation is unknown (which is almost always the case in practice) and use z only when σ is known or when n is very large (typically n > 30). The exam should specify which to use.

WHEN POPULATION VARIANCES ARE UNEQUAL IN TWO-SAMPLE TESTS, use Welch's t-test formula for degrees of freedom: df ≈ (s₁²/n₁ + s₂²/n₂)² / [((s₁²/n₁)²/(n₁-1)) + ((s₂²/n₂)²/(n₂-1))]. This is a more robust approach than assuming equal variances.

ALWAYS STATE YOUR CONCLUSION IN THE CONTEXT OF THE PROBLEM, not just in statistical terms. For example, say "there is sufficient evidence to conclude that Algorithm A is faster" rather than just "reject H₀."

KEEP TRACK OF WHETHER YOUR TEST IS ONE-TAILED OR TWO-TAILED. A one-tailed test at α = 0.05 uses the same critical value as a two-tailed test at α = 0.10, but they test different hypotheses. The alternative hypothesis determines the direction of the test.

PRACTICE WITH T-TABLES: Exam questions typically provide t-tables, to read them correctly. Most so learn tables give critical values for the upper tail, so for a two-tailed test at significance level α, look up t(α/2, df) in the table.