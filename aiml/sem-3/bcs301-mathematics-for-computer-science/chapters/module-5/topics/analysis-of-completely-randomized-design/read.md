# Analysis of Completely Randomized Design

=============================================

## Overview

---

The Completely Randomized Design (CRD) is a common experimental design used in statistical analysis. In this study material, we will explore the definition, assumptions, and analysis of the CRD.

## Definition

---

The Completely Randomized Design (CRD) is a type of experimental design where all treatments are randomly assigned to the experimental units. In other words, each treatment is assigned to a random set of experimental units without any prior knowledge of the outcome.

## Assumptions

---

The analysis of CRD assumes the following conditions:

- **Randomization**: Each experimental unit is assigned to a treatment randomly.
- **Independence**: The assignment of each experimental unit to a treatment does not affect the outcome.
- **Homogeneity of variance**: The variance of the response variable is constant across all treatments.
- **Normality**: The response variable follows a normal distribution.

## Analysis of CRD

---

The analysis of CRD involves two main steps:

### Step 1: Analysis of Variance (ANOVA)

ANOVA is used to test the significance of the treatment effects. The null hypothesis is:

- **H0**: The treatment effects are zero (i.e., there is no significant difference between the treatments).
- **H1**: The treatment effects are not zero (i.e., there is a significant difference between the treatments).

The ANOVA statistic is calculated as:

- **MS**: Mean squared (response variable)
- **MSA**: Mean squared (treatment)
- **MSE**: Mean squared (error)

The ANOVA F-statistic is calculated as:

- **F**: F-ratio = MSA / MSE

### Step 2: Post-hoc Analysis

Post-hoc analysis is used to determine which treatments are significantly different from each other. Common post-hoc tests include:

- **Tukey's HSD**: Used to compare all possible pairs of treatments.
- **LSD**: Used to compare all possible pairs of treatments.
- **LMRT**: Used to compare all possible pairs of treatments.

## Example

---

Suppose we want to compare the growth of three different types of grass (Treatment A, B, and C) using a CRD. We have 20 experimental units, each with three replicates.

| Treatment | Replicate 1 | Replicate 2 | Replicate 3 |
| --------- | ----------- | ----------- | ----------- |
| A         | 10.2        | 11.5        | 12.1        |
| B         | 9.8         | 10.2        | 11.0        |
| C         | 10.5        | 11.2        | 12.3        |

We perform ANOVA to test for significant treatment effects.

| Source    | SS   | df  | MS  | F   |
| --------- | ---- | --- | --- | --- |
| Treatment | 15.6 | 2   | 7.8 | 3.4 |
| Error     | 24.4 | 16  | 1.5 |     |

The ANOVA F-statistic is 3.4, which is greater than the critical F-value (F0.05, 2, 16). Therefore, we reject the null hypothesis and conclude that there are significant treatment effects.

## Conclusion

---

In conclusion, the Completely Randomized Design (CRD) is a widely used experimental design for statistical analysis. The analysis of CRD involves ANOVA and post-hoc tests to determine the significance of treatment effects. Understanding the assumptions, analysis, and post-hoc tests is essential for conducting a valid analysis of CRD.

### Key Concepts

- **Completely Randomized Design**: A type of experimental design where all treatments are randomly assigned to experimental units.
- **Analysis of Variance (ANOVA)**: A statistical technique used to test the significance of treatment effects.
- **Post-hoc analysis**: A statistical technique used to determine which treatments are significantly different from each other.
- **Assumptions**: Randomization, independence, homogeneity of variance, and normality.

### Study Tips

- Understand the definition and assumptions of CRD.
- Learn the ANOVA and post-hoc tests.
- Practice analyzing CRD data using real-world examples.

### References

- [Book Title]: [Author's Name], [Publisher's Name], [Year of Publication].
- [Online Resource]: [URL or Citation].
