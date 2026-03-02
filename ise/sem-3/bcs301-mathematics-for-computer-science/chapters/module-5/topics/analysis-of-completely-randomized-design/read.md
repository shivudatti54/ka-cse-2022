# Analysis of Completely Randomized Design

====================================================

## Introduction

---

In experimental design, a completely randomized design (CRD) is a type of experimental design where all treatments are randomly assigned to experimental units. This study will provide an overview of the analysis of completely randomized design, including the assumptions, methods, and examples.

## Assumptions

---

- Each experimental unit is randomly assigned to a treatment.
- The treatments are mutually exclusive and exhaustive.
- There are no interactions between treatments.
- The observations are independent.

## Methods

---

The analysis of completely randomized design involves the following steps:

1. **Data Analysis**: The data is analyzed using statistical methods to determine the effects of treatments.
2. **Anova**: The analysis of variance (ANOVA) is used to test the hypothesis that the treatment means are equal.
3. **Post-Hoc Tests**: Post-hoc tests are used to compare the treatment means.

## ANOVA

---

The ANOVA model for CRD is:

Yijk = μ + Ti + εijk

where:

- Yijk is the observation in the ith treatment and jth experimental unit.
- μ is the overall mean.
- Ti is the effect of the ith treatment.
- εijk is the error term.

## Example

---

Suppose we want to compare the yield of two different varieties of wheat. We have three experimental units for each treatment. The yield data is:

| Treatment | Experimental Unit | Yield (kg) |
| --------- | ----------------- | ---------- |
| A         | 1                 | 200        |
| A         | 2                 | 220        |
| A         | 3                 | 210        |
| B         | 1                 | 240        |
| B         | 2                 | 250        |
| B         | 3                 | 260        |

Using ANOVA, we can test the hypothesis that the treatment means are equal:

| Source    | SS  | df  | MS  | F     |
| --------- | --- | --- | --- | ----- |
| Treatment | 120 | 2   | 60  | 10.00 |
| Error     | 80  | 8   | 10  |       |

The F-statistic is 10.00, which is greater than the critical value of 3.18. Therefore, we reject the null hypothesis and conclude that the treatment means are not equal.

## Post-Hoc Tests

---

Post-hoc tests are used to compare the treatment means. For example, we can use the Tukey's HSD test to compare the treatment means:

| Treatment | Mean   | HSD   |
| --------- | ------ | ----- |
| A         | 214.33 | 20.83 |
| B         | 246.67 | 20.83 |

The HSD (honest significance difference) is 20.83. Therefore, we can conclude that there is a significant difference between treatment A and treatment B.

## Key Concepts

---

- **Randomization**: The process of assigning treatments to experimental units randomly.
- **Mutual Exclusivity**: The treatment means must be mutually exclusive and exhaustive.
- **Independence**: The observations must be independent.
- **ANOVA**: The analysis of variance is used to test the hypothesis that the treatment means are equal.
- **Post-Hoc Tests**: Post-hoc tests are used to compare the treatment means.

## Practice Problems

---

1. Analyze the data using ANOVA and post-hoc tests to compare the treatment means.
2. Determine the significance level for the ANOVA test.
3. Calculate the HSD for the post-hoc test.

## References

---

- [1] Montgomery, D. C. (2009). Design and analysis of experiments. Prentice Hall.
- [2] Snell, B. B. (1968). The analysis of experimental designs. Springer-Verlag.

Note: The practice problems and references are not provided as they are not part of the original study material.
