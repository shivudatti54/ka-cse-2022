# Mathematics for Computer Science - Design of Experiments & ANOVA

## The ANOVA Technique

- **Basic Principle of ANOVA**: It is a statistical method used to test whether there are significant differences between group means.
  $$ F = \frac{MS*{between}}{MS*{within}} $$
  Where \( MS*{between} \) and \( MS*{within} \) denote the mean square between groups and within groups, respectively.

## Basic Principle of ANOVA

- **Analysis of Variance**: This is a statistical technique that uses variances to determine if different populations are significantly different from each other.
- **F-test**: Used to test the null hypothesis (all group means are equal) against the alternative hypothesis (at least one mean is different).

## One-way ANOVA

- Tests whether any of several groups have different population means.
  $$ F = \frac{MS*{between}}{MS*{within}} $$
- **F-distribution**: Assumes that data from each group are normally distributed and come from populations with the same variance.

## Two-way ANOVA

- Examines the effect of two categorical independent variables on a continuous dependent variable.
  $$ F_1 = \frac{\text{variance between groups A}}{\text{variance within groups A}} $$
  $$ F_2 = \frac{\text{variance between groups B}}{\text{variance within groups B}} $$
- **Interaction effects**: Whether the effect of one variable depends on the level of another.

## Latin-square Design

- Used to control for two sources of variability when there are multiple treatments.
  - Balanced arrangement where each treatment appears once in every row and column.
    $$ \text{Latin Square} = (R + C - G) / G $$
    Where \( R \) is the number of rows, \( C \) is the number of columns, and \( G \) is the number of treatments.

## Analysis of Co-Variance

- Combines ANOVA with regression analysis to control for covariates.
- Allows for more efficient use of resources by controlling variability due to confounding variables.
  $$ MS*{total} = MS*{covariate} + MS\_{error} $$

**Summary Notes:**

1. **ANOVA**: Used for comparing multiple group means; uses F-test and assumes normality and homogeneity of variances.
2. **One-way ANOVA**: Examines one independent variable with several levels; calculates \(F\) ratio to test significance.
3. **Two-way ANOVA**: Evaluates two independent variables simultaneously; tests main effects and interaction effects.
4. **Latin-square Design**: A balanced arrangement used when there are two sources of variability, ensuring each factor is randomly distributed.
5. **Analysis of Co-Variance (ANCOVA)**: Combines ANOVA with regression to control for confounding covariates by adding a linear model term.
