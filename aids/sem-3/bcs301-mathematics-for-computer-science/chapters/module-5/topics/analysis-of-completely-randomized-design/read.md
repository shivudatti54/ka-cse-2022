# Analysis of Completely Randomized Design

### Overview

A Completely Randomized Design (CRD) is a type of experimental design where all treatments are randomly assigned to experimental units. This study will provide an overview of the CRD, its assumptions, advantages, and limitations, as well as a step-by-step guide on how to analyze it using Analysis of Variance (ANOVA).

### Definitions

- **Experimental Design**: A plan for conducting an experiment to test hypotheses about the relationship between variables.
- **Treatment**: A specific level of a factor being tested.
- **Experimental Unit**: The entity being tested, such as a plant or a mouse.
- **Randomization**: The process of allocating experimental units to treatments randomly.

### Assumptions of CRD

- **Independence**: Experimental units must be independent of each other.
- **Randomization**: Treatments must be assigned randomly to experimental units.
- **Normality**: The response variable must be normally distributed.
- **Homogeneity of Variance**: The variance of the response variable must be the same across all treatments.

### Advantages of CRD

- **Easy to implement**: CRD is a simple and straightforward design.
- **Fast**: CRD is a fast design, as it does not require multiple runs.
- **Cost-effective**: CRD is a cost-effective design, as it does not require specialized equipment.

### Limitations of CRD

- **Lack of control**: CRD does not allow for control of extraneous variables.
- **Limited generalizability**: CRD results may not be generalizable to other populations.
- **Not suitable for large datasets**: CRD is not suitable for large datasets, as it can lead to overfitting.

### Analysis of CRD using ANOVA

ANOVA is a statistical technique used to analyze CRD. The steps to analyze CRD using ANOVA are:

#### Step 1: Calculate the mean and standard deviation of the response variable

- Calculate the mean (x̄) and standard deviation (σ) of the response variable for each treatment.

#### Step 2: Calculate the sum of squares between (SSB) and within (SSW)

- **SSB**: Calculate the sum of squares between (SSB) as the sum of the squared differences between each treatment mean and the grand mean.
- **SSW**: Calculate the sum of squares within (SSW) as the sum of the squared differences between each experimental unit and its treatment mean.

#### Step 3: Calculate the mean square between (MSB) and within (MSW)

- **MSB**: Calculate the mean square between (MSB) as SSB / (number of treatments - 1).
- **MSW**: Calculate the mean square within (MSW) as SSW / (total number of experimental units - number of treatments).

#### Step 4: Calculate the F-statistic

- Calculate the F-statistic as MSB / MSW.

#### Step 5: Determine the significance of the F-statistic

- Compare the F-statistic to the critical F-value from the F-distribution to determine the significance of the results.

### Example

Suppose we want to test the effect of three different levels of a fertilizer on the growth of a plant. We conduct a CRD with 30 experimental units, 10 in each treatment. The response variable is the plant height (cm). The results of the ANOVA analysis are:

| Source | SS   | df  | MS   | F   |
| ------ | ---- | --- | ---- | --- |
| B      | 120  | 2   | 60   | 2.5 |
| W      | 1100 | 28  | 39.3 |     |
| Total  | 1220 | 30  |      |     |

In this example, the F-statistic is 2.5, which is greater than the critical F-value from the F-distribution (p < 0.05). Therefore, we reject the null hypothesis that the fertilizer has no effect on plant growth.

## Key Concepts

- **Degrees of freedom**: The number of values in the numerator and denominator of a fraction.
- **Sum of squares**: A measure of the total variation in a dataset.
- **Mean square**: The average of the sum of squares.
- **F-statistic**: A ratio of the mean square between and mean square within.
- **Critical F-value**: The F-statistic value that separates the significant from the non-significant results.

## Conclusion

The analysis of completely randomized design is a widely used statistical technique used to analyze experimental data. By understanding the assumptions, advantages, and limitations of CRD, researchers can design and analyze experiments to test hypotheses about the relationship between variables. The step-by-step guide to analyzing CRD using ANOVA provides a clear and concise approach to analyzing experimental data.
