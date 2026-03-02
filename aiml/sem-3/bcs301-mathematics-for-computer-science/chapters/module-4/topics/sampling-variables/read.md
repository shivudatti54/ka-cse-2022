# Sampling Variables

## Introduction

Sampling variables form the foundation of statistical inference, a core area of study in the Statistical Inference 2 module for Computer Science students at the University of Delhi. In practical applications, we rarely have access to entire populations—we work with samples and use them to draw conclusions about larger groups. Understanding how sample statistics behave, how they vary from one sample to another, and how they relate to population parameters is essential for any data analysis task.

In the context of Computer Science, sampling variables are crucial for algorithm analysis, machine learning model evaluation, database sampling for query optimization, and performance benchmarking. When we collect data from a system or conduct experiments, we invariably work with samples. The theory of sampling variables tells us how to make valid inferences from these samples to the underlying populations from which they were drawn. This module builds directly on the Central Limit Theorem, which you will study subsequently, and provides the theoretical groundwork for hypothesis testing and confidence intervals.

This chapter explores the mathematical foundations of sampling, the relationship between population parameters and sample statistics, the concept of sampling distributions, and the critical role of standard error in statistical inference.

## Key Concepts

### Population and Sample: Fundamental Distinction

A **population** (denoted as P) is the complete set of all observations or measurements about which we want to draw conclusions. For example, the execution times of all possible inputs to an algorithm, the response times of all users of a web server, or the memory usage values across all program executions constitute populations.

A **sample** (denoted as S) is a subset of the population selected for study. We use sample data to make inferences about the population. The size of the sample is denoted by n, while the size of the population is denoted by N.

The process of selecting a sample from a population is called **sampling**. The primary goal of sampling is to obtain representative samples that accurately reflect the characteristics of the population.

### Parameters and Statistics: Key Difference

A **population parameter** is a numerical characteristic of the entire population. Parameters are usually unknown constants that we aim to estimate. Common parameters include:

- Population mean (μ) - the average of all observations in the population
- Population variance (σ²) - the measure of dispersion in the population
- Population standard deviation (σ) - the square root of population variance
- Population proportion (P) - the proportion of elements in the population with a certain characteristic

A **sample statistic** (or simply statistic) is a numerical characteristic computed from sample data. Statistics are used to estimate population parameters. Common statistics include:

- Sample mean (x̄) - the average of observations in the sample
- Sample variance (s²) - the measure of dispersion in the sample
- Sample standard deviation (s) - the square root of sample variance
- Sample proportion (p̂) - the proportion of elements in the sample with a certain characteristic

The relationship is fundamental: we use sample statistics as point estimates for population parameters.

### Types of Sampling Methods

**Simple Random Sampling**: Every member of the population has an equal chance of being selected, and each possible sample of size n has an equal probability of being chosen. This can be done with or without replacement.

- **Sampling without replacement**: Once an element is selected, it is removed from the population and cannot be selected again.
- **Sampling with replacement**: Selected elements are returned to the population and can be selected again.

**Stratified Sampling**: The population is divided into homogeneous subgroups (strata), and samples are drawn from each stratum, typically proportionally to the stratum's size in the population.

**Systematic Sampling**: Every k-th element is selected after a random starting point, where k = population size ÷ sample size.

**Cluster Sampling**: The population is divided into clusters, and a random sample of clusters is selected, with all observations in chosen clusters included in the sample.

For valid statistical inference, **simple random sampling** is the most fundamental and theoretically important method.

### Sampling Distribution

The **sampling distribution** of a statistic is the probability distribution of that statistic considered as a random variable, when repeated samples of size n are drawn from the population.

This is a critical concept: the sample statistic itself is a random variable because different samples yield different values. The sampling distribution describes this variability.

For example, if we repeatedly draw samples of size n from a population and compute the sample mean each time, the distribution of these sample means is the sampling distribution of the sample mean.

### Expected Value and Standard Error

The **expected value** (or mathematical expectation) of a sample statistic is the long-run average value of the statistic over an infinite number of samples.

For a simple random sample, the expected value of the sample mean equals the population mean:

E(x̄) = μ

This property is called **unbiasedness**—the sample mean is an unbiased estimator of the population mean.

The **standard error** (SE) of a statistic is the standard deviation of its sampling distribution. It measures the variability of the statistic across different samples.

For the sample mean when sampling from a infinite population:

SE(x̄) = σ / √n

When sampling from a finite population without replacement, we apply the finite population correction factor:

SE(x̄) = (σ / √n) × √[(N - n) / (N - 1)]

### Sampling Distribution of the Sample Mean

If we draw simple random samples of size n from a population with mean μ and standard deviation σ, the sampling distribution of the sample mean has:

- Mean: μ (same as population mean)
- Standard deviation (standard error): σ/√n

This holds regardless of the shape of the population distribution, provided samples are independent. This is the theoretical foundation for the Central Limit Theorem.

### Sampling Distribution of Sample Variance

The sample variance s² is calculated as:

s² = Σ(xi - x̄)² / (n - 1)

The sample variance is also an unbiased estimator: E(s²) = σ².

The sampling distribution of s² follows a chi-square distribution with (n-1) degrees of freedom when the population is normally distributed:

(n - 1)s² / σ² ~ χ²(n-1)

This relationship is fundamental to many hypothesis tests and confidence interval constructions.

### Law of Large Numbers

The Law of Large Numbers states that as the sample size n increases, the sample mean x̄ converges in probability to the population mean μ. Formally:

lim(n→∞) P(|x̄ - μ| < ε) = 1 for any ε > 0

This law justifies using larger samples to get more reliable estimates of population parameters.

## Examples

### Example 1: Computing Sample Statistics

A software company wants to estimate the average response time of their server. They collect a random sample of 5 response times (in milliseconds): 120, 135, 128, 142, 125.

Calculate:
(a) Sample mean (x̄)
(b) Sample variance (s²)
(c) Sample standard deviation (s)

**Solution:**

(a) Sample mean:
x̄ = (120 + 135 + 128 + 142 + 125) / 5
x̄ = 650 / 5
x̄ = 130 ms

(b) Sample variance:
First, compute deviations from mean: (120-130)², (135-130)², (128-130)², (142-130)², (125-130)²
= 100 + 25 + 4 + 144 + 25 = 298

s² = 298 / (5-1) = 298 / 4 = 74.5 ms²

(c) Sample standard deviation:
s = √74.5 = 8.63 ms

### Example 2: Standard Error Calculation

A database administrator samples 36 query execution times from a large system. Historical data shows the population standard deviation is σ = 12 milliseconds. Calculate the standard error of the sample mean.

**Solution:**

Given: n = 36, σ = 12 ms

SE(x̄) = σ / √n = 12 / √36 = 12 / 6 = 2 ms

This means that the standard deviation of the sampling distribution of the sample mean is 2 ms. In repeated sampling, we expect the sample means to vary with a standard deviation of 2 ms.

### Example 3: Effect of Sample Size on Standard Error

A machine learning engineer is training models and measuring accuracy. The population standard deviation of model accuracy is known to be σ = 5%. Compare the standard error for sample sizes of n = 25, n = 100, and n = 400.

**Solution:**

Using SE = σ/√n:

For n = 25: SE = 5/√25 = 5/5 = 1.0%
For n = 100: SE = 5/√100 = 5/10 = 0.5%
For n = 400: SE = 5/√400 = 5/20 = 0.25%

This illustrates the square root relationship: to halve the standard error, we need to quadruple the sample size. This has practical implications for experimental design—when higher precision is needed, sample size must increase substantially.

## Exam Tips

1. **Distinguish between parameters and statistics**: Remember that parameters describe populations (unknown, fixed) while statistics describe samples (known, computed from data). Parameters are denoted by Greek letters (μ, σ, P), while statistics are denoted by Roman letters (x̄, s, p̂).

2. **Understand the standard error formula**: For the sample mean, SE = σ/√n. This is the most frequently tested formula. Know when to apply the finite population correction factor: only when sampling without replacement from a finite population.

3. **Remember unbiasedness properties**: The sample mean x̄ is an unbiased estimator of μ, and the sample variance s² (using n-1 in denominator) is an unbiased estimator of σ². This is a common exam question.

4. **Know the relationship between sample size and precision**: As n increases, the standard error decreases (but at a diminishing rate due to the square root). This means larger samples yield more precise estimates.

5. **Sampling distribution vs population distribution**: These are different concepts. The population distribution describes how individual observations are distributed, while the sampling distribution describes how the sample statistic varies across samples.

6. **Application to real scenarios**: In exam questions, you may need to identify whether a value is a parameter or statistic, calculate standard errors, or determine appropriate sample sizes for desired precision levels.

7. **Connect to Central Limit Theorem**: The sampling distribution of x̄ approaches a normal distribution as n increases, regardless of population shape. This connection will be essential for subsequent topics on confidence intervals and hypothesis testing.