# **Central Limit Theorem and Confidence Limits for Unknown Mean**

## **Introduction**

In statistics, the Central Limit Theorem (CLT) states that given certain conditions, the distribution of the mean of a large sample of independent and identically distributed (i.i.d.) random variables will be approximately normally distributed, regardless of the original variable's distribution shape. This theorem has numerous applications in computer science, particularly in machine learning and data analysis.

In this study material, we will explore the Central Limit Theorem, confidence limits for unknown mean, and their significance in statistical inference.

## **Definitions**

- **Central Limit Theorem (CLT):** A theorem that describes the distribution of the mean of a large sample of i.i.d. random variables.
- **Mean:** The average value of a set of numbers.
- **Sample size:** The number of observations in the sample.
- **Confidence interval:** A range of values within which the true population mean is likely to lie.

## **Central Limit Theorem**

### Key Concepts

- **Large Sample Size:** The sample size must be sufficiently large to satisfy the CLT conditions.
- **Independence:** Observations must be independent and identically distributed.
- **Identical Distribution:** The original variable's distribution shape is identical across all observations.
- **Approximate Normal Distribution:** The distribution of the sample mean will be approximately normally distributed.

### Mathematical Representation

Let X1, X2, …, Xn be a random sample of size n from a population with mean μ and variance σ^2. The sample mean is given by:

X̄ = (1/n) \* ΣXi

According to the CLT, the distribution of X̄ will be approximately normal with a mean of μ and a variance of σ^2/n.

## **Confidence Limits for Unknown Mean**

### Definition

A confidence interval is a range of values within which the true population mean is likely to lie. The confidence interval is calculated using the sample mean and the standard error of the mean.

### Formula

The confidence interval for the population mean is given by:

X̄ ± (Z \* (σ/√n))

where:

- X̄ is the sample mean
- Z is the Z-score corresponding to the desired confidence level
- σ is the population standard deviation
- n is the sample size

### Types of Confidence Limits

- **Single-confidence interval:** A single range of values within which the true population mean is likely to lie.
- **Double-confidence interval:** Two ranges of values, one for the lower bound and one for the upper bound.

### Importance in Statistical Inference

---

Confidence limits are used to make inferences about a population mean based on a sample of data. They provide a range of values within which the true population mean is likely to lie, allowing us to make decisions about the population.

### Example

Suppose we want to estimate the average height of a population of adults in a city. We take a random sample of 100 adults and calculate the sample mean height to be 175.2 cm. Using a confidence interval with a confidence level of 95%, we calculate the range of values within which the true population mean height is likely to lie:

175.2 ± (1.96 \* (4/√100)) = (175.2 ± 0.8)

Therefore, we are 95% confident that the true population mean height lies between 174.4 cm and 176.0 cm.

## **Conclusion**

The Central Limit Theorem and confidence limits for unknown mean are essential concepts in statistical inference. The CLT provides a framework for understanding the distribution of the sample mean, while confidence limits allow us to make inferences about the population mean based on a sample of data. By understanding these concepts, we can make informed decisions about populations and make predictions about future outcomes.
