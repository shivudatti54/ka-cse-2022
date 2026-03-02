# One Way ANOVA - Summary

## Key Definitions

- **One Way ANOVA**: A statistical technique used to test whether there are statistically significant differences between the means of three or more independent groups.

- **Between-Group Variation (SSB)**: The variation in data attributable to differences between group means and the overall mean.

- **Within-Group Variation (SSW)**: The variation in data attributable to differences within each group around their respective group means.

- **F-statistic**: The ratio of mean square between groups to mean square within groups; follows an F-distribution under the null hypothesis.

- **Grand Mean (x̄..)**: The overall mean of all observations across all groups.

## Important Formulas

- **Total Sum of Squares**: $SST = \sum_{j=1}^{k} \sum_{i=1}^{n_j} (x_{ij} - \bar{x}_{..})^2$

- **Between-Group Sum of Squares**: $SSB = \sum_{j=1}^{k} n_j(\bar{x}_j - \bar{x}_{..})^2$

- **Within-Group Sum of Squares**: $SSW = \sum_{j=1}^{k} \sum_{i=1}^{n_j} (x_{ij} - \bar{x}_j)^2$

- **Mean Square Between**: $MSB = \frac{SSB}{k-1}$

- **Mean Square Within**: $MSW = \frac{SSW}{N-k}$

- **F-statistic**: $F = \frac{MSB}{MSW}$

## Key Points

1. ANOVA tests H₀: μ₁ = μ₂ = ... = μₖ against H₁: at least one μᵢ differs.

2. The four ANOVA assumptions are: independence, normality, homogeneity of variances, and interval/ratio scale measurement.

3. ANOVA partitions total variation into between-group and within-group components.

4. A significant F-test indicates that some difference exists but doesn't identify which specific groups differ.

5. With only two groups, ANOVA reduces to the t-test (F = t²).

6. Effect size can be measured using eta-squared: η² = SSB/SST.

7. Post-hoc tests (Tukey HSD, Bonferroni) are needed after significant ANOVA to determine specific group differences.

## Common Mistakes

1. **Assuming ANOVA identifies which groups differ**: Remember ANOVA only detects the existence of differences; post-hoc tests are required to identify specific differences.

2. **Ignoring assumption checking**: Failing to verify normality and homogeneity of variances can lead to invalid conclusions.

3. **Confusing degrees of freedom**: Confusing df₁ = k-1 with df₂ = N-k leads to incorrect critical value lookup.

4. **Interpreting non-significant results as equality**: Failing to reject H₀ means insufficient evidence of difference, not proof of equality.