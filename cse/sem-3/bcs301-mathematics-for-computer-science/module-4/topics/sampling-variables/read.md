# Statistical Inference 2 - Sampling Variables

## Table of Contents

- [Statistical Inference 2 - Sampling Variables](#statistical-inference-2---sampling-variables)
- [Introduction](#introduction)
- [Core Concepts of Sampling Variables](#core-concepts-of-sampling-variables)
  - [1. What is a Sampling Variable?](#1-what-is-a-sampling-variable)
  - [2. Sampling Distribution](#2-sampling-distribution)
  - [3. Standard Error (SE)](#3-standard-error-se)
  - [4. The Central Limit Theorem (CLT) - The Crown Jewel](#4-the-central-limit-theorem-clt---the-crown-jewel)
- [Example: API Response Time](#example-api-response-time)
- [Key Points & Summary](#key-points--summary)

## Introduction

In the world of Computer Science, data is the new currency. From training machine learning models to A/B testing website features, we constantly draw conclusions from data. However, we rarely have access to an entire population of data. This is where **sampling variables** become critical. They are the bridge that allows us to use a manageable subset of data (a sample) to make reliable inferences about a larger population, forming the backbone of statistical inference.

## Core Concepts of Sampling Variables

### 1. What is a Sampling Variable?

A **sampling variable** is not a single variable but a _statistic_ (like the sample mean, `X̄`) calculated from a sample. Because each sample we draw is random, the value of this statistic will vary from sample to sample. Therefore, a sampling variable is itself a random variable. Its probability distribution is called the **sampling distribution**.

- **Population Parameter (θ):** A fixed, unknown value describing a population (e.g., true mean `μ`, true proportion `p`).
- **Sample Statistic (`θ̂`):** A value calculated from a sample used to _estimate_ the parameter (e.g., sample mean `X̄`, sample proportion `p̂`).
- **Sampling Variable:** The random variable representing all possible values the sample statistic can take.

### 2. Sampling Distribution

The sampling distribution is the probability distribution of a sampling variable. It tells us how the statistic would behave if we took many, many samples from the same population.

**Key Idea:** While individual data points in a population can have any distribution, the sampling distribution of the mean tends to become **Normal** (Gaussian) as the sample size increases, thanks to the **Central Limit Theorem (CLT)**.

### 3. Standard Error (SE)

The **Standard Error** is the standard deviation of a sampling distribution. It measures the variability or precision of the sample statistic (like `X̄`).

- **Formula for the Mean:** If the population standard deviation is `σ`, the standard error of the sample mean is `SE = σ / √n`, where `n` is the sample size.
- **Why it matters:** A smaller SE indicates that your sample statistic is likely closer to the true population parameter. Increasing your sample size (`n`) reduces the SE, leading to more precise estimates.

### 4. The Central Limit Theorem (CLT) - The Crown Jewel

The CLT is the fundamental theorem that justifies the use of sample statistics to make inferences about population parameters.

> **Statement:** For a sufficiently large sample size (`n` > 30 is a common rule of thumb), the sampling distribution of the sample mean (`X̄`) will be approximately normally distributed **regardless of the shape of the population distribution**, with:
>
> - Mean = Population mean (`μ`)
> - Standard Deviation = Standard Error (`σ / √n`)

**Implication for CS:** This is incredibly powerful. It means we can apply normal probability principles to analyze sample means from non-normal data, such as website load times, user engagement metrics, or API response times.

## Example: API Response Time

Imagine you are a data engineer analyzing the response time of a cloud API. The population distribution of all response times is highly right-skewed (most requests are fast, a few are very slow), with a mean `μ = 120 ms` and standard deviation `σ = 40 ms`.

You decide to take a random sample of `n = 50` requests and calculate the mean response time, `X̄`.

1. **Sampling Variable:** `X̄` (the sample mean).
2. **According to CLT:** The distribution of `X̄` will be approximately Normal.

- Mean of `X̄` = `μ = 120 ms`
- Standard Error (SE) = `σ / √n = 40 / √50 ≈ 5.66 ms`

3. **Inference:** You can now use the normal distribution to find probabilities. For example, the probability that your sample's mean response time is greater than 125 ms is `P(X̄ > 125)`.

To find this, calculate the Z-score:
`Z = (125 - 120) / 5.66 ≈ 0.88`
`P(Z > 0.88) = 1 - 0.8106 = 0.1894` (from Z-table).

There is an ~19% chance that a sample of 50 requests would have a mean response time above 125 ms, even though the true population mean is 120 ms.

## Key Points & Summary

- **Purpose:** Sampling variables allow us to quantify the uncertainty in our estimates when working with samples instead of entire populations.
- **Sampling Distribution:** The probability distribution of a sample statistic (e.g., `X̄`) over many samples. Its spread is measured by the Standard Error (SE).
- **Standard Error (SE):** `σ / √n`. It decreases as sample size increases, leading to more precise estimates.
- **Central Limit Theorem (CLT):** The cornerstone of statistical inference. It states that for large `n`, the sampling distribution of the mean is normal, enabling probability calculations and the construction of confidence intervals (the next key topic).
- **Relevance for CS:** Essential for machine learning (e.g., evaluating model performance), network analysis (e.g., estimating packet loss), business intelligence (e.g., estimating user conversion rates), and any form of data-driven decision-making.
