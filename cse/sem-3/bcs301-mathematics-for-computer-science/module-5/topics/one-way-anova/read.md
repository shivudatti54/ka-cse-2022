## Table of Contents

- [One-Way ANOVA (Analysis of Variance)](#one-way-anova-analysis-of-variance)
- [Introduction](#introduction)
- [Hypotheses](#hypotheses)
- [Assumptions of One-Way ANOVA](#assumptions-of-one-way-anova)
- [Notation and Setup](#notation-and-setup)
- [Sum of Squares Partitioning](#sum-of-squares-partitioning)
- [Degrees of Freedom](#degrees-of-freedom)
- [Mean Squares](#mean-squares)
- [F-Statistic](#f-statistic)
- [ANOVA Table](#anova-table)
- [Decision Rule](#decision-rule)
- [Worked Example 1](#worked-example-1)
- [Worked Example 2](#worked-example-2)
- [Worked Example 3 (Accepting H0)](#worked-example-3-accepting-h0)
- [Important Formulas Summary](#important-formulas-summary)
- [Key Points for Exams](#key-points-for-exams)
  - [Further Reading](#further-reading)

### One-Way ANOVA (Analysis of Variance)

## Introduction

One-way ANOVA (Analysis of Variance) is a statistical technique used to test whether there are significant differences between the means of two or more independent groups based on a single factor (independent variable). It extends the two-sample t-test to three or more groups. The "one-way" refers to the fact that only one factor is being studied.

## Hypotheses

- **Null Hypothesis (H0):** All population group means are equal.
  H0: mu_1 = mu_2 = mu_3 = ... = mu_k

- **Alternative Hypothesis (H1):** At least one population mean is different from the others.
  H1: Not all mu_i are equal (i = 1, 2, ..., k)

## Assumptions of One-Way ANOVA

1. **Independence:** Observations are independent of each other.
2. **Normality:** The populations from which the samples are drawn are normally distributed.
3. **Homogeneity of Variances:** The populations have equal variances (homoscedasticity).

## Notation and Setup

Let:

- k = number of groups (levels of the factor)
- n_i = number of observations in group i
- N = total number of observations = n_1 + n_2 + ... + n_k
- x_ij = jth observation in the ith group
- x_bar_i = mean of the ith group = (sum of x_ij for j=1 to n_i) / n_i
- x_bar = grand mean = (sum of all observations) / N

## Sum of Squares Partitioning

The fundamental principle of ANOVA is the partitioning of total variation into components:

**Total Sum of Squares (SST):**
SST = sum over all i,j of (x_ij - x_bar)^2

This measures the total variability in the data.

**Between-Groups Sum of Squares (SSB):**
SSB = sum over i of n_i \* (x_bar_i - x_bar)^2

This measures the variability due to differences between group means.

**Within-Groups Sum of Squares (SSW):**
SSW = sum over all i,j of (x_ij - x_bar_i)^2

This measures the variability within each group (random error).

**Key Identity:**
SST = SSB + SSW

## Degrees of Freedom

- df_Total = N - 1
- df_Between = k - 1
- df_Within = N - k

**Verification:** df_Total = df_Between + df_Within, i.e., (N - 1) = (k - 1) + (N - k)

## Mean Squares

Mean squares are obtained by dividing the sum of squares by the corresponding degrees of freedom:

- **Mean Square Between (MSB):** MSB = SSB / (k - 1)
- **Mean Square Within (MSW):** MSW = SSW / (N - k)

## F-Statistic

The test statistic is:

F = MSB / MSW

Under H0, the F-statistic follows an F-distribution with (k - 1) and (N - k) degrees of freedom.

## ANOVA Table

| Source of Variation   | Sum of Squares | Degrees of Freedom | Mean Square     | F-Statistic |
| --------------------- | -------------- | ------------------ | --------------- | ----------- |
| Between Groups        | SSB            | k - 1              | MSB = SSB/(k-1) | F = MSB/MSW |
| Within Groups (Error) | SSW            | N - k              | MSW = SSW/(N-k) |             |
| Total                 | SST            | N - 1              |                 |             |

## Decision Rule

At significance level alpha:

- If F_calculated > F_critical(alpha, k-1, N-k), reject H0. Conclude that at least one group mean is significantly different.
- If F_calculated <= F_critical, fail to reject H0. There is insufficient evidence to conclude that the means differ.

## Worked Example 1

**Problem:** A professor wants to compare the average scores of students taught by three different teaching methods. The scores are:

| Method A | Method B | Method C |
| -------- | -------- | -------- |
| 85       | 90       | 70       |
| 78       | 88       | 65       |
| 82       | 95       | 72       |
| 80       | 92       | 68       |
| 75       | 85       | 75       |

Test at alpha = 0.05 whether the teaching methods have a significant effect on scores.

**Solution:**

**Step 1: Compute group means and grand mean.**

- n_A = n_B = n_C = 5, k = 3, N = 15
- x_bar_A = (85 + 78 + 82 + 80 + 75) / 5 = 400 / 5 = 80
- x_bar_B = (90 + 88 + 95 + 92 + 85) / 5 = 450 / 5 = 90
- x_bar_C = (70 + 65 + 72 + 68 + 75) / 5 = 350 / 5 = 70
- Grand mean x_bar = (400 + 450 + 350) / 15 = 1200 / 15 = 80

**Step 2: Compute SSB (Between Groups).**

SSB = 5*(80 - 80)^2 + 5*(90 - 80)^2 + 5*(70 - 80)^2
SSB = 5*(0) + 5*(100) + 5*(100)
SSB = 0 + 500 + 500 = 1000

**Step 3: Compute SSW (Within Groups).**

For Method A: (85-80)^2 + (78-80)^2 + (82-80)^2 + (80-80)^2 + (75-80)^2 = 25 + 4 + 4 + 0 + 25 = 58
For Method B: (90-90)^2 + (88-90)^2 + (95-90)^2 + (92-90)^2 + (85-90)^2 = 0 + 4 + 25 + 4 + 25 = 58
For Method C: (70-70)^2 + (65-70)^2 + (72-70)^2 + (68-70)^2 + (75-70)^2 = 0 + 25 + 4 + 4 + 25 = 58

SSW = 58 + 58 + 58 = 174

**Step 4: Verify SST = SSB + SSW.**

SST = 1000 + 174 = 1174

**Step 5: Compute degrees of freedom.**

- df_Between = k - 1 = 3 - 1 = 2
- df_Within = N - k = 15 - 3 = 12
- df_Total = N - 1 = 14

**Step 6: Compute Mean Squares.**

- MSB = SSB / df_Between = 1000 / 2 = 500
- MSW = SSW / df_Within = 174 / 12 = 14.5

**Step 7: Compute F-statistic.**

F = MSB / MSW = 500 / 14.5 = 34.48

**Step 8: ANOVA Table.**

| Source  | SS   | df  | MS   | F     |
| ------- | ---- | --- | ---- | ----- |
| Between | 1000 | 2   | 500  | 34.48 |
| Within  | 174  | 12  | 14.5 |       |
| Total   | 1174 | 14  |      |       |

**Step 9: Decision.**

F_critical(0.05, 2, 12) = 3.89 (from F-distribution table)

Since F_calculated (34.48) > F_critical (3.89), we reject H0.

**Conclusion:** There is a statistically significant difference between the mean scores of the three teaching methods at the 5% significance level.

## Worked Example 2

**Problem:** Four types of fertilizers are tested on crop yield (in kg). The yields are:

| Fertilizer 1 | Fertilizer 2 | Fertilizer 3 | Fertilizer 4 |
| ------------ | ------------ | ------------ | ------------ |
| 23           | 28           | 20           | 25           |
| 25           | 30           | 18           | 27           |
| 20           | 25           | 22           | 23           |

Test at alpha = 0.05 whether different fertilizers produce significantly different yields.

**Solution:**

**Step 1: Compute group means and grand mean.**

- k = 4, n_i = 3 for all groups, N = 12
- x_bar_1 = (23 + 25 + 20) / 3 = 68 / 3 = 22.67
- x_bar_2 = (28 + 30 + 25) / 3 = 83 / 3 = 27.67
- x_bar_3 = (20 + 18 + 22) / 3 = 60 / 3 = 20.00
- x_bar_4 = (25 + 27 + 23) / 3 = 75 / 3 = 25.00
- Grand mean x_bar = (68 + 83 + 60 + 75) / 12 = 286 / 12 = 23.83

**Step 2: Compute SSB.**

SSB = 3*(22.67 - 23.83)^2 + 3*(27.67 - 23.83)^2 + 3*(20.00 - 23.83)^2 + 3*(25.00 - 23.83)^2
SSB = 3*(1.3456) + 3*(14.7456) + 3*(14.6689) + 3*(1.3689)
SSB = 4.04 + 44.24 + 44.01 + 4.11
SSB = 96.40

**Step 3: Compute SSW.**

For Fertilizer 1: (23-22.67)^2 + (25-22.67)^2 + (20-22.67)^2 = 0.1089 + 5.4289 + 7.1289 = 12.67
For Fertilizer 2: (28-27.67)^2 + (30-27.67)^2 + (25-27.67)^2 = 0.1089 + 5.4289 + 7.1289 = 12.67
For Fertilizer 3: (20-20)^2 + (18-20)^2 + (22-20)^2 = 0 + 4 + 4 = 8.00
For Fertilizer 4: (25-25)^2 + (27-25)^2 + (23-25)^2 = 0 + 4 + 4 = 8.00

SSW = 12.67 + 12.67 + 8.00 + 8.00 = 41.34

**Step 4: Degrees of freedom.**

- df_Between = 4 - 1 = 3
- df_Within = 12 - 4 = 8
- df_Total = 12 - 1 = 11

**Step 5: Mean Squares.**

- MSB = 96.40 / 3 = 32.13
- MSW = 41.34 / 8 = 5.17

**Step 6: F-statistic.**

F = 32.13 / 5.17 = 6.22

**Step 7: ANOVA Table.**

| Source  | SS     | df  | MS    | F    |
| ------- | ------ | --- | ----- | ---- |
| Between | 96.40  | 3   | 32.13 | 6.22 |
| Within  | 41.34  | 8   | 5.17  |      |
| Total   | 137.74 | 11  |       |      |

**Step 8: Decision.**

F_critical(0.05, 3, 8) = 4.07

Since F_calculated (6.22) > F_critical (4.07), we reject H0.

**Conclusion:** There is a statistically significant difference in crop yields among the four fertilizers at the 5% significance level.

## Worked Example 3 (Accepting H0)

**Problem:** Three brands of batteries are tested for their lifetimes (hours):

| Brand X | Brand Y | Brand Z |
| ------- | ------- | ------- |
| 50      | 52      | 49      |
| 48      | 50      | 51      |
| 51      | 49      | 50      |
| 49      | 51      | 48      |

Test at alpha = 0.05 whether the brands differ significantly.

**Solution:**

- k = 3, n_i = 4, N = 12
- x_bar_X = (50+48+51+49)/4 = 49.5
- x_bar_Y = (52+50+49+51)/4 = 50.5
- x_bar_Z = (49+51+50+48)/4 = 49.5
- Grand mean x_bar = (198+202+198)/12 = 598/12 = 49.83

SSB = 4*(49.5-49.83)^2 + 4*(50.5-49.83)^2 + 4*(49.5-49.83)^2
SSB = 4*(0.1089) + 4*(0.4489) + 4*(0.1089) = 0.4356 + 1.7956 + 0.4356 = 2.67

SSW (within each group):
Brand X: (0.5)^2+(-1.5)^2+(1.5)^2+(-0.5)^2 = 0.25+2.25+2.25+0.25 = 5.0
Brand Y: (1.5)^2+(-0.5)^2+(-1.5)^2+(0.5)^2 = 2.25+0.25+2.25+0.25 = 5.0
Brand Z: (-0.5)^2+(1.5)^2+(0.5)^2+(-1.5)^2 = 0.25+2.25+0.25+2.25 = 5.0

SSW = 5.0 + 5.0 + 5.0 = 15.0

ANOVA Table:

| Source  | SS    | df  | MS    | F    |
| ------- | ----- | --- | ----- | ---- |
| Between | 2.67  | 2   | 1.335 | 0.80 |
| Within  | 15.0  | 9   | 1.667 |      |
| Total   | 17.67 | 11  |       |      |

F_critical(0.05, 2, 9) = 4.26

Since F_calculated (0.80) < F_critical (4.26), we fail to reject H0.

**Conclusion:** There is no statistically significant difference in the mean lifetimes of the three battery brands at the 5% significance level.

## Important Formulas Summary

1. SST = SSB + SSW
2. MSB = SSB / (k - 1)
3. MSW = SSW / (N - k)
4. F = MSB / MSW
5. Grand mean = (Sum of all observations) / N
6. Correction Factor (CF) = (Grand Total)^2 / N
7. SST = Sum of squares of all observations - CF
8. SSB = (Sum of (Group Total)^2 / n_i) - CF

## Key Points for Exams

- Always state the hypotheses clearly.
- Show the complete ANOVA table in your solution.
- Clearly state degrees of freedom.
- Compare F_calculated with F_critical and state the conclusion.
- Use the correction factor method for faster computation.
- Remember: SST = SSB + SSW always holds.

### Further Reading

Refer to your prescribed textbook and official course materials.
