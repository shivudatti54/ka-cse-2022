# Standard Error - Summary

## Key Definitions
- **Standard Error (SE)**: The standard deviation of a sampling distribution; measures the precision of a sample statistic as an estimate of a population parameter
- **Sampling Distribution**: The probability distribution of a statistic (like the mean) obtained by repeated sampling from the same population
- **Standard Error of the Mean (SEM)**: The standard deviation of the distribution of sample means

## Important Formulas
- **SE of Mean (σ known):** $SE(\bar{X}) = \frac{\sigma}{\sqrt{n}}$
- **SE of Mean (σ unknown):** $SE(\bar{X}) = \frac{s}{\sqrt{n}}$
- **SE of Proportion:** $SE(p) = \sqrt{\frac{p(1-p)}{n}}$
- **SE of Difference of Means:** $SE(\bar{X}_1 - \bar{X}_2) = \sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}$
- **Finite Population Correction:** $SE_{corrected} = SE \times \sqrt{\frac{N-n}{N-1}}$

## Key Points
- Standard error decreases as sample size increases (proportional to 1/√n)
- To halve the standard error, sample size must be increased by a factor of 4
- Standard error quantifies uncertainty in estimates; smaller SE means more precise estimates
- The Central Limit Theorem ensures the sampling distribution approaches normality for large n
- SE is essential for constructing confidence intervals and conducting hypothesis tests
- In machine learning, SE helps assess model performance variability across different training sets
- The distinction between SD (data variability) and SE (estimate precision) is critical

## Common Mistakes
- Confusing standard deviation with standard error—this is the most frequent error
- Using population standard deviation formula when only sample standard deviation is available
- Forgetting to take the square root when calculating SE of the mean (dividing by n instead of √n)
- Applying the wrong formula for proportions when the sample size is small relative to population