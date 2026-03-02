# Randomized Block Design Summary

## Definitions and Concepts

- **Randomized Block Design (RBD):** An experimental design that accounts for variability by grouping similar subjects into blocks and randomly assigning treatments to these blocks.
- **Blocks:** Groups of units that are homogeneous with respect to the response variable.

## Key Points

- **Design Structure:**
  - Treatments are assigned randomly within each block.
  - Each treatment appears once in each block.

- **ANOVA Setup:**
  - Treatment effect (β)
  - Block effect (γi): The fixed effect of block i
  - Error effect (εij): Residuals, random and independent with mean zero

  \[ Y*{ijk} = \mu + (\beta_i + \gamma*{ik} + \epsilon\_{ijk}) \]

- **ANOVA Table:**
  \[
  \begin{array}{c|cc}
  & \text{Treatment Effects} & \text{Block Effects} \\
  \hline
  \text{Treatment Sum of Squares (SST)} & SST = \sum (\bar{Y}_j - \bar{Y})^2 & SS_{Treatments} = \sum n*i (\bar{Y}*{i.} - \bar{Y})^2 \\
  \text{Error Sum of Squares (SSR)} & SSR = \sum \left( Y*{ijk} - \bar{Y}*{j} \right)^2 & SS*{Blocks} = \sum n_i (\bar{Y}*{..i} - \bar{Y})^2 \\
  \end{array}
  \]

- **Estimation of Parameters:**
  - Treatment effect: \( \hat{\beta}_i = \frac{\sum Y_{ij}}{r_i} \)
  - Block effect: \( \hat{\gamma}_{ik} = \bar{Y}_{k.} - \bar{Y}\_{..k} \)

- **Hypothesis Testing:**
  - Null Hypothesis (H0): All treatment effects are equal to zero.
  - Alternative Hypothesis (Ha): At least one treatment effect is not equal to zero.

  Test Statistic:
  \[
  F = \frac{MS*{Treatments}}{MS*{Error}}
  \]

- **Randomized Block Design vs. Completely Randomized Design:**
  - RBD controls for variability between blocks.
  - CRD does not account for such variability and assumes all units are equivalent.

## Important Formulas

- Sum of Squares Total (SST):
  \[ SST = \sum (\bar{Y}_j - \bar{Y})^2 + \sum (\bar{Y}_{i.} - \bar{Y})^2 + \sum (\bar{Y}\_{..i} - \bar{Y})^2 \]

- Sum of Squares Between Treatments (SST):
  \[ SST = \sum n*i (\bar{Y}*{i.} - \bar{Y})^2 \]

- Sum of Squares Within Blocks (SSR):
  \[ SSR = \sum \left( Y*{ijk} - \bar{Y}*{j} \right)^2 \]

## Theorems and Properties

- **Block Effect:**
  - Each block effect is a fixed parameter in RBD.
- **Error Variance:**
  - Error variance \( \sigma^2 = \frac{\text{SSR}}{df\_{error}} \)

## Conclusion

Randomized Block Design is crucial for controlling variability and ensuring more accurate estimates of treatment effects. It's particularly useful when the experiment has a natural grouping that can be considered as blocks, such as different soils or different experimental conditions.

---

This summary provides a concise overview of Randomized Block Design with key points, formulas, and concepts essential for understanding this experimental design method in the context of Design of Experiments and Analysis of Variance (ANOVA).
