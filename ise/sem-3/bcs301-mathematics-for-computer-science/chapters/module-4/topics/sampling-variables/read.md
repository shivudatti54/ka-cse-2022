# Sampling Variables

## Introduction

Sampling variables form the cornerstone of statistical inference, enabling us to draw meaningful conclusions about entire populations based on limited data. In the context of Computer Science and data analytics, understanding sampling variables is essential for designing efficient algorithms, performing hypothesis testing, and building predictive models. The concept bridges the gap between descriptive statistics and inferential statistics, providing the mathematical framework that allows us to make predictions with quantifiable uncertainty.

When we collect data from a population, we rarely have access to every single element. Instead, we select a sample and use statistical methods to infer properties about the larger group. The variables we obtain from these samples are called sampling variables, and their behavior follows specific mathematical properties that we can model and predict. This becomes particularly important in areas such as machine learning, where training data is always a subset of the potential data space, and in quality assurance, where testing every product is often impractical.

This topic develops the theoretical foundation necessary to understand how sample statistics behave as random variables. We will explore the mathematical properties of sample means, sample variances, and other sample statistics, which will be directly applied in subsequent topics covering the Central Limit Theorem, confidence intervals, and hypothesis testing.

## Key Concepts

### Population and Sample

A POPULATION denotes the complete set of all possible observations or measurements of interest. For example, the response times of all web servers in a network, or the execution times of an algorithm across all possible inputs. The population is characterized by parameters such as the population mean (μ) and population variance (σ²).

A SAMPLE is a subset of the population selected for study. We denote a sample of size n as (X₁, X₂, ..., Xₙ), where each Xᵢ represents a random variable. The sample is used to estimate population parameters. The key distinction is that while the population is fixed (though often unknown), the sample is random—the particular elements we select depend on the sampling method.

### Random Sampling

The most fundamental sampling method is SIMPLE RANDOM SAMPLING, where every possible sample of size n has an equal probability of being selected. When sampling WITH REPLACEMENT, each observation is returned to the population after being recorded, meaning the same element can appear multiple times in a sample. When sampling WITHOUT REPLACEMENT, once an element is selected, it cannot be selected again.

In statistical inference, we typically assume simple random sampling, which ensures that the sample observations X₁, X₂, ..., Xₙ are INDEPENDENT AND IDENTICALLY DISTRIBUTED (i.i.d.) random variables. This i.i.d. assumption is crucial because it allows us to apply many powerful statistical theorems.

### Sample Mean as a Random Variable

The sample mean, denoted by X̄, is computed as:

X̄ = (X₁ + X₂ + ... + Xₙ) / n

Since each Xᵢ is a random variable, X̄ is also a random variable with its own probability distribution called the SAMPLING DISTRIBUTION. The expected value (mean) of the sampling distribution is:

E(X̄) = μ

This demonstrates that the sample mean is an UNBIASED ESTIMATOR of the population mean—the expected value of our estimator equals the true population parameter.

The variance of the sample mean depends on whether we are sampling with or without replacement:

- Sampling WITH replacement: Var(X̄) = σ²/n
- Sampling WITHOUT replacement: Var(X̄) = (σ²/n) × [(N-n)/(N-1)]

where N is the population size and n is the sample size. The factor [(N-n)/(N-1)] is called the FINITE POPULATION CORRECTION (FPC). When N is much larger than n (a common scenario), this correction approaches 1 and can be ignored.

### Sample Variance

The sample variance S² is defined as:

S² = [Σ(Xᵢ - X̄)²] / (n-1)

The denominator uses (n-1) rather than n, making S² an unbiased estimator of the population variance σ². We have:

E(S²) = σ²

This is a remarkable result—the sample variance, with (n-1) in the denominator, exactly compensates for the underestimation that would occur if we used n. The quantity (n-1) is called the DEGREES OF FREEDOM.

The standard deviation of the sample mean, denoted as STANDARD ERROR (SE), is:

SE(X̄) = σ/√n (for infinite population)

SE(X̄) = (σ/√n) × √[(N-n)/(N-1)] (for finite population)

### Sampling Distribution of the Sample Mean

The behavior of the sample mean's distribution depends critically on the population distribution. If the population itself is normally distributed (Xᵢ ~ N(μ, σ²)), then the sample mean follows an exact normal distribution:

X̄ ~ N(μ, σ²/n)

This exact relationship holds regardless of sample size when the population is normal. When the population is not normal, the Central Limit Theorem (covered in the next topic) tells us that the sampling distribution of X̄ approaches normality as sample size increases.

### Chi-Square Distribution in Sampling

The quantity (n-1)S²/σ² follows a chi-square distribution with (n-1) degrees of freedom:

(n-1)S²/σ² ~ χ²ₙ₋₁

This result is fundamental because it allows us to make inferences about the population variance. The chi-square distribution is skewed for small degrees of freedom but becomes more symmetric as degrees of freedom increase.

### Joint Distribution of Sample Mean and Sample Variance

For a normal population, the sample mean X̄ and sample variance S² are INDEPENDENT random variables. This independence is a special property of the normal distribution and is crucial for deriving the t-distribution used in small sample inference.

## Examples

### Example 1: Computing Sample Statistics

Suppose the CPU processing times (in milliseconds) for a algorithm across 5 independent runs are: 12, 15, 14, 11, 18.

Calculate the sample mean, sample variance, and standard error.

SOLUTION:

Sample mean: X̄ = (12 + 15 + 14 + 11 + 18) / 5 = 70/5 = 14 ms

Deviations from mean: -2, 1, 0, -3, 4

Squared deviations: 4, 1, 0, 9, 16

Sum of squared deviations: 4 + 1 + 0 + 9 + 16 = 30

Sample variance: S² = 30/(5-1) = 30/4 = 7.5 ms²

Sample standard deviation: S = √7.5 ≈ 2.74 ms

Standard error (assuming large population): SE = S/√5 = 2.74/2.24 ≈ 1.22 ms

### Example 2: Probability Calculation Using Sampling Distribution

The response time of a server is normally distributed with mean μ = 200 ms and standard deviation σ = 40 ms. For a random sample of n = 16 observations, find the probability that the sample mean exceeds 210 ms.

SOLUTION:

Since the population is normal, X̄ ~ N(μ, σ²/n)

Variance of X̄: σ²/n = 40²/16 = 1600/16 = 100

Standard deviation of X̄: √100 = 10 ms

We need P(X̄ > 210)

Standardize: Z = (210 - 200)/10 = 10/10 = 1

P(X̄ > 210) = P(Z > 1) = 0.1587

Therefore, there is approximately a 15.87% chance that the sample mean exceeds 210 ms.

### Example 3: Determining Required Sample Size

A data analyst wants to estimate the mean execution time of an algorithm to within ±5 milliseconds with 95% confidence. Previous data suggests the execution times have a standard deviation of σ = 30 ms. What sample size is required?

SOLUTION:

For 95% confidence, Zₐ/₂ = 1.96

The margin of error is: E = Zₐ/₂ × (σ/√n)

We need: 5 = 1.96 × (30/√n)

Solving: √n = 1.96 × 30 / 5 = 58.8 / 5 = 11.76

n = (11.76)² = 138.3

Therefore, we need at least 139 observations to achieve the desired precision.

## Exam Tips

1. REMEMBER THE DIFFERENCE BETWEEN PARAMETERS AND STATISTICS: Population characteristics (μ, σ²) are parameters; sample characteristics (X̄, S²) are statistics. Statistics are random variables; parameters are fixed (though unknown) constants.

2. UNDERSTAND WHY (n-1) APPEARS IN SAMPLE VARIANCE: The denominator (n-1) provides unbiasedness. Using n would systematically underestimate the population variance. This is a frequently tested concept.

3. KNOW THE EXPECTED VALUES: E(X̄) = μ and E(S²) = σ² are the two most important expectation results. Commit these to memory as they form the basis for understanding unbiased estimation.

4. STANDARD ERROR VS STANDARD DEVIATION: The standard deviation describes variability in the population or sample. The standard error describes the variability of the sample mean itself—a measure of how precisely X̄ estimates μ.

5. NORMAL POPULATION ASSUMPTION: When the population is normally distributed, X̄ and S² are independent. This independence is essential for deriving the t-distribution and is a key assumption in small sample inference.

6. FINITE POPULATION CORRECTION: When sampling without replacement from a finite population, include the FPC factor √[(N-n)/(N-1)]. When n < 0.05N, the FPC is approximately 1 and can be ignored.

7. DISTINGUISH BETWEEN SAMPLING DISTRIBUTIONS: The sampling distribution of X̄ has mean μ and variance σ²/n. The distribution of the population has mean μ and variance σ². The sampling distribution is always narrower (less variable) than the population distribution.