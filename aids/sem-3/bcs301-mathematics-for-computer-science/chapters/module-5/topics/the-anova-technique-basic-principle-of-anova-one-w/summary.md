# Revision Notes: ANOVA Technique, Basic Principle of ANOVA, and More

===========================================================

### Basic Principles of ANOVA

- **ANOVA (Analysis of Variance)**: Statistical technique used to compare means of three or more samples to determine if at least one of the means is different.
- **F-Statistic**: Ratio of variance between groups to variance within groups, used to calculate p-value.
- **Null Hypothesis**: μ1 = μ2 = ... = μk (all means are equal)
- **Alternative Hypothesis**: Not all means are equal

### One-way ANOVA

- **Assumptions**:
  - Normality of residuals
  - Equal variances (homoscedasticity)
- **Formula**:
  - F = Σ(n_i(\bar{x}\_i - \bar{x})^2) / Σ(n_i(\bar{x}\_i - \bar{x})^2 + (n_i-1)s^2)
  - p-value = P(F > F\_(\alpha, k-1, \nu))
- **Used for**: Comparing means of three or more groups

### Two-way ANOVA

- **Design**: Two independent factors (A and B) with two levels each
- **Assumptions**:
  - Normality of residuals
  - Equality of variances (homoscedasticity)
  - Independence of observations
- **Formula**:
  - F = (MSB / MSE) \* F\_(\alpha, A-1, AB)
- **Used for**: Comparing means of three or more groups with two independent factors

### Latin-square Design

- **Definition**: Experimental design where each treatment is replicated in each run of the experiment
- **Advantages**:
  - Reduces error due to replication
  - Increases precision
- **Used for**: Two-way ANOVA with two independent factors

### Analysis of Co-Variance (ANCOVA)

- **Definition**: Statistical technique used to compare means of two or more groups while controlling for the effect of a third variable (covariate)
- **Formula**:
  - F = (MSA - MSB) / MSE
- **Used for**: Comparing means of two or more groups while controlling for the effect of a third variable

### Key Formulas and Theorems

- **F-Distribution**: Distribution of the F-statistic
- **T-Distribution**: Distribution of the t-statistic
- **Student's t-test**: Test statistic for comparing means of two groups
