# **The ANOVA Technique and Basic Principles**

- **Definition**: Analysis of Variance (ANOVA) is a statistical technique used to compare means of three or more samples to determine if at least one of the means is different.
- **Basic Principle**: ANOVA tests the null hypothesis that all group means are equal against the alternative hypothesis that at least one group mean is different.
- **Key Formulas**:
  - F-statistic: F = MSB / MSE
  - Mean Square Between (MSB) = Σ(Squared difference between group means) / (Number of groups - 1)
  - Mean Square Error (MSE) = Σ(Squared differences between individual observations and group means) / (Total number of observations - Number of groups)

# **One-way ANOVA**

- **Definition**: ANOVA used to compare means of three or more samples to determine if at least one of the means is different.
- **Null Hypothesis**: μ1 = μ2 = ... = μk (all group means are equal)
- **Alternative Hypothesis**: At least one group mean is different
- **Formula**: F = MSB / MSE
- **Key Assumptions**:
  - Independence of observations
  - Normality of residuals
  - Equal Variances

## **Two-way ANOVA**

- **Definition**: ANOVA used to compare means of three or more samples, with two independent factors.
- **Null Hypothesis**: μ11 = μ12 = ... = μ1k = μ21 = μ22 = ... = μ2k = μ31 = μ32 = ... = μ3k (all interaction and main effects are zero)
- **Alternative Hypothesis**: At least one main effect or interaction is different
- **Formula**: F = (MB/MSB) / (WM/MSE)
- **Key Assumptions**:
  - Independence of observations
  - Normality of residuals
  - Equal Variances

## **Latin-square Design**

- **Definition**: A design where each level of one factor is paired with each level of the other factor.
- **Advantages**: Increases precision, reduces error
- **Disadvantages**: Requires large sample size

## **Analysis of Co-Variance (ANCOVA)**

- **Definition**: ANCOVA used to compare means of three or more samples, while controlling for the effect of one or more covariates.
- **Null Hypothesis**: μ1 = μ2 = ... = μk (all group means are equal)
- **Alternative Hypothesis**: At least one group mean is different
- **Formula**: F = (MSB/MSA) / (MSE/MSEc)
- **Key Assumptions**:
  - Independence of observations
  - Normality of residuals
  - Equal Variances
