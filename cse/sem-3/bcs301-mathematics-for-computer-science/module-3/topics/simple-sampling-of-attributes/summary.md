# Simple Sampling Of Attributes - Summary

## Key Definitions

- **Attribute**: A qualitative characteristic that can only be classified into two categories (success/failure, defective/non-defective)
- **Population Proportion (p)**: The true proportion of elements in the entire population possessing the attribute of interest
- **Sample Proportion (p̂)**: The proportion of elements in the sample possessing the attribute, calculated as p̂ = x/n where x is the number of successes and n is sample size
- **Standard Error**: The standard deviation of the sampling distribution of the sample proportion
- **Finite Population Correction**: A factor applied to adjust the standard error when sampling without replacement from a finite population

## Important Formulas

- Sample Proportion: p̂ = x/n
- Standard Error (estimated): SE(p̂) = √[p̂(1-p̂)/n]
- Standard Error (theoretical): SE(p̂) = √[p(1-p)/n]
- Finite Population Correction: FPC = √[(N-n)/(N-1)]
- Adjusted Standard Error: SE(adjusted) = SE × FPC
- Large Sample Conditions: np̂ ≥ 5 and n(1-p̂) ≥ 5

## Key Points

1. Attribute sampling deals with categorical characteristics where each element either possesses or lacks the attribute
2. The sample proportion p̂ is an unbiased estimator of the population proportion p
3. The binomial distribution provides the theoretical foundation for attribute sampling
4. For large samples, the sampling distribution of p̂ approximates a normal distribution
5. The standard error decreases as sample size increases, leading to more precise estimates
6. The finite population correction reduces standard error when sampling a substantial fraction of the population
7. Large sample conditions must be verified before applying normal approximation methods
8. Attribute sampling has direct applications in software testing, network analysis, and database quality assurance

## Common Mistakes

1. **Confusing attributes with variables**: Using variable sampling formulas for attribute data leads to incorrect results
2. **Ignoring finite population correction**: Failing to apply FPC when sampling more than 10% of a finite population
3. **Using normal approximation without checking conditions**: Applying z-tests or confidence intervals when np̂ or n(1-p̂) is less than 5
4. **Mixing up p and p̂**: Using population proportion p in standard error formula when only sample proportion p̂ is available
5. **Incorrect interpretation of confidence level**: Believing a specific confidence interval has a 95% probability of containing the parameter rather than understanding the long-run frequency interpretation