# Two Way ANOVA - Summary

## Key Definitions

- **Factor**: An independent categorical variable with two or more levels; in Two Way ANOVA, we consider exactly two factors (say, Factor A with *a* levels and Factor B with *b* levels).

- **Interaction Effect**: The effect where the impact of one factor depends on the level of another factor; represented as $(\alpha\beta)_{ij}$ in the model equation.

- **Main Effect**: The individual effect of one factor on the response variable, averaged across all levels of the other factor.

- **Cell Mean**: The average response for a specific combination of factor levels (level *i* of Factor A and level *j* of Factor B).

- **Replication**: Multiple independent observations taken under identical treatment conditions.

## Important Formulas

**Linear Model:**
$$Y_{ijk} = \mu + \alpha_i + \beta_j + (\alpha\beta)_{ij} + \epsilon_{ijk}$$

**Sum of Squares Decomposition:**
$$SS_T = SS_A + SS_B + SS_{AB} + SS_E$$

**Degrees of Freedom:**
- Factor A: $a - 1$
- Factor B: $b - 1$
- Interaction: $(a - 1)(b - 1)$
- Error: $ab(n - 1)$
- Total: $abn - 1$

**F-Statistics:**
$$F = \frac{\text{Mean Square for Effect}}{\text{Mean Square Error}}$$

## Key Points

1. Two Way ANOVA examines both main effects (individual factor impacts) and interaction effects (combined factor influence).

2. The interaction effect is tested before interpreting main effects; significant interaction often renders main effect interpretation meaningless.

3. With $n$ replications per cell, we have a balanced design; unbalanced designs require more complex analysis.

4. The error term $\epsilon_{ijk}$ is assumed to follow $N(0, \sigma^2)$ for valid F-tests.

5. Interaction can be synergistic (effects combine to exceed sum) or antagonistic (effects partially cancel).

6. In computer science, Two Way ANOVA is valuable for comparing algorithms across different data sets, hardware configurations, or software environments.

7. Post-hoc tests are necessary when significant effects are found to identify specific level differences.

## Common Mistakes

1. **Confusing degrees of freedom**: Using $ab - 1$ instead of $(a-1)(b-1)$ for interaction degrees of freedom.

2. **Ignoring interaction**: Jumping to interpret main effects without checking if interaction is significant first.

3. **Misreading interaction plots**: Concluding no interaction exists when lines are not parallel, without formal statistical testing.

4. **Violation of assumptions**: Applying Two Way ANOVA without checking normality, homogeneity of variance, and independence assumptions.

5. **Over-interpreting non-significant results**: Concluding "no difference exists" when failing to reject null hypothesis, rather than saying "insufficient evidence to detect difference."