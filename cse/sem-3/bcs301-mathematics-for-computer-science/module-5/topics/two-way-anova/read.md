## Table of Contents

- [Two-Way ANOVA (Analysis of Variance)](#two-way-anova-analysis-of-variance)
- [Introduction](#introduction)
- [Types of Two-Way ANOVA](#types-of-two-way-anova)
- [Hypotheses](#hypotheses)
- [Notation and Setup](#notation-and-setup)
- [Sum of Squares Partitioning](#sum-of-squares-partitioning)
  - [Without Replication (n = 1 per cell, N = a \* b):](#without-replication-n--1-per-cell-n--a--b)
  - [With Replication (n > 1 per cell, N = a _ b _ n):](#with-replication-n--1-per-cell-n--a--b--n)
- [Degrees of Freedom](#degrees-of-freedom)
- [Mean Squares](#mean-squares)
- [F-Statistics](#f-statistics)
- [ANOVA Table (With Replication)](#anova-table-with-replication)
- [ANOVA Table (Without Replication)](#anova-table-without-replication)
- [Correction Factor Method](#correction-factor-method)
- [Worked Example 1: Two-Way ANOVA Without Replication](#worked-example-1-two-way-anova-without-replication)
- [Worked Example 2: Two-Way ANOVA With Replication](#worked-example-2-two-way-anova-with-replication)
- [Understanding Interaction Effects](#understanding-interaction-effects)
- [Key Points for Exams](#key-points-for-exams)
  - [Further Reading](#further-reading)

### Two-Way ANOVA (Analysis of Variance)

## Introduction

Two-way ANOVA is an extension of one-way ANOVA that examines the effect of two independent categorical variables (factors) on a continuous dependent variable. It allows researchers to study not only the main effects of each factor individually but also the interaction effect between the two factors. This makes two-way ANOVA a powerful tool for analyzing experiments where two factors may simultaneously influence the outcome.

## Types of Two-Way ANOVA

1. **Two-way ANOVA without replication:** Each cell (combination of factor levels) has exactly one observation. Interaction effects cannot be tested.
2. **Two-way ANOVA with replication:** Each cell has multiple observations. Both main effects and interaction effects can be tested.

## Hypotheses

Three sets of hypotheses are tested simultaneously:

**For Factor A (Row factor, with 'a' levels):**

- H0_A: There is no significant effect of Factor A on the dependent variable (all row means are equal).
- H1_A: Factor A has a significant effect (at least one row mean differs).

**For Factor B (Column factor, with 'b' levels):**

- H0_B: There is no significant effect of Factor B on the dependent variable (all column means are equal).
- H1_B: Factor B has a significant effect (at least one column mean differs).

**For Interaction (A x B):**

- H0_AB: There is no interaction effect between Factor A and Factor B.
- H1_AB: There is a significant interaction effect.

## Notation and Setup

Let:

- a = number of levels of Factor A
- b = number of levels of Factor B
- n = number of replications per cell (for replicated design)
- N = total number of observations = a _ b _ n
- x_ijk = kth observation in cell (i, j), i.e., ith level of A and jth level of B
- x_bar = grand mean

## Sum of Squares Partitioning

### Without Replication (n = 1 per cell, N = a \* b):

SST = SSA + SSB + SSE

Where:

- **SST (Total):** sum over all (x_ij - x_bar)^2
- **SSA (Factor A):** b \* sum_i (x_bar_i. - x_bar)^2 where x_bar_i. is the mean of row i
- **SSB (Factor B):** a \* sum*j (x_bar*.j - x*bar)^2 where x_bar*.j is the mean of column j
- **SSE (Error):** SST - SSA - SSB

### With Replication (n > 1 per cell, N = a _ b _ n):

SST = SSA + SSB + SSAB + SSE

Where:

- **SSAB (Interaction):** n \* sum*i sum_j (x_bar_ij - x_bar_i. - x_bar*.j + x_bar)^2
- **SSE (Error):** sum_i sum_j sum_k (x_ijk - x_bar_ij)^2

## Degrees of Freedom

| Source              | df (Without Replication) | df (With Replication) |
| ------------------- | ------------------------ | --------------------- |
| Factor A            | a - 1                    | a - 1                 |
| Factor B            | b - 1                    | b - 1                 |
| Interaction (A x B) | Not estimable            | (a - 1)(b - 1)        |
| Error               | (a - 1)(b - 1)           | ab(n - 1)             |
| Total               | ab - 1                   | abn - 1               |

## Mean Squares

- MSA = SSA / (a - 1)
- MSB = SSB / (b - 1)
- MSAB = SSAB / [(a - 1)(b - 1)] (with replication only)
- MSE = SSE / df_Error

## F-Statistics

- F_A = MSA / MSE (tests the main effect of Factor A)
- F_B = MSB / MSE (tests the main effect of Factor B)
- F_AB = MSAB / MSE (tests the interaction effect, with replication only)

## ANOVA Table (With Replication)

| Source              | SS   | df         | MS                       | F               |
| ------------------- | ---- | ---------- | ------------------------ | --------------- |
| Factor A            | SSA  | a - 1      | MSA = SSA/(a-1)          | F_A = MSA/MSE   |
| Factor B            | SSB  | b - 1      | MSB = SSB/(b-1)          | F_B = MSB/MSE   |
| Interaction (A x B) | SSAB | (a-1)(b-1) | MSAB = SSAB/[(a-1)(b-1)] | F_AB = MSAB/MSE |
| Error               | SSE  | ab(n-1)    | MSE = SSE/[ab(n-1)]      |                 |
| Total               | SST  | abn - 1    |                          |                 |

## ANOVA Table (Without Replication)

| Source             | SS  | df         | MS                     | F             |
| ------------------ | --- | ---------- | ---------------------- | ------------- |
| Factor A (Rows)    | SSA | a - 1      | MSA = SSA/(a-1)        | F_A = MSA/MSE |
| Factor B (Columns) | SSB | b - 1      | MSB = SSB/(b-1)        | F_B = MSB/MSE |
| Error              | SSE | (a-1)(b-1) | MSE = SSE/[(a-1)(b-1)] |               |
| Total              | SST | ab - 1     |                        |               |

## Correction Factor Method

- CF = (Grand Total)^2 / N
- SST = (Sum of all x_ij^2 or x_ijk^2) - CF
- SSA = (Sum of Row Totals^2) / (b\*n) - CF
- SSB = (Sum of Column Totals^2) / (a\*n) - CF
- SSAB = (Sum of Cell Totals^2) / n - CF - SSA - SSB (with replication)
- SSE = SST - SSA - SSB - SSAB (with replication) or SST - SSA - SSB (without replication)

## Worked Example 1: Two-Way ANOVA Without Replication

**Problem:** An experiment studies the effect of 3 different algorithms (Factor A) and 4 different datasets (Factor B) on computation time (in seconds). Each algorithm is run once on each dataset.

|             | Dataset 1 | Dataset 2 | Dataset 3 | Dataset 4 |
| ----------- | --------- | --------- | --------- | --------- |
| Algorithm 1 | 12        | 14        | 11        | 13        |
| Algorithm 2 | 18        | 20        | 16        | 22        |
| Algorithm 3 | 10        | 12        | 9         | 11        |

Test at alpha = 0.05 whether algorithms and datasets have significant effects on computation time.

**Solution:**

**Step 1: Compute totals and means.**

- a = 3 (algorithms), b = 4 (datasets), N = 12

Row totals:

- R1 = 12 + 14 + 11 + 13 = 50
- R2 = 18 + 20 + 16 + 22 = 76
- R3 = 10 + 12 + 9 + 11 = 42

Column totals:

- C1 = 12 + 18 + 10 = 40
- C2 = 14 + 20 + 12 = 46
- C3 = 11 + 16 + 9 = 36
- C4 = 13 + 22 + 11 = 46

Grand Total (G) = 50 + 76 + 42 = 168

**Step 2: Correction Factor.**

CF = G^2 / N = 168^2 / 12 = 28224 / 12 = 2352

**Step 3: Compute SST.**

Sum of all x_ij^2 = 12^2 + 14^2 + 11^2 + 13^2 + 18^2 + 20^2 + 16^2 + 22^2 + 10^2 + 12^2 + 9^2 + 11^2
= 144 + 196 + 121 + 169 + 324 + 400 + 256 + 484 + 100 + 144 + 81 + 121 = 2540

SST = 2540 - 2352 = 188

**Step 4: Compute SSA (Algorithms / Rows).**

SSA = (R1^2 + R2^2 + R3^2) / b - CF
SSA = (50^2 + 76^2 + 42^2) / 4 - 2352
SSA = (2500 + 5776 + 1764) / 4 - 2352
SSA = 10040 / 4 - 2352 = 2510 - 2352 = 158

**Step 5: Compute SSB (Datasets / Columns).**

SSB = (C1^2 + C2^2 + C3^2 + C4^2) / a - CF
SSB = (40^2 + 46^2 + 36^2 + 46^2) / 3 - 2352
SSB = (1600 + 2116 + 1296 + 2116) / 3 - 2352
SSB = 7128 / 3 - 2352 = 2376 - 2352 = 24

**Step 6: Compute SSE.**

SSE = SST - SSA - SSB = 188 - 158 - 24 = 6

**Step 7: Degrees of freedom.**

- df_A = a - 1 = 2
- df_B = b - 1 = 3
- df_E = (a-1)(b-1) = 2 \* 3 = 6
- df_Total = ab - 1 = 11

**Step 8: Mean Squares and F-statistics.**

- MSA = 158 / 2 = 79
- MSB = 24 / 3 = 8
- MSE = 6 / 6 = 1

- F_A = 79 / 1 = 79.0
- F_B = 8 / 1 = 8.0

**Step 9: ANOVA Table.**

| Source         | SS  | df  | MS  | F    |
| -------------- | --- | --- | --- | ---- |
| Algorithms (A) | 158 | 2   | 79  | 79.0 |
| Datasets (B)   | 24  | 3   | 8   | 8.0  |
| Error          | 6   | 6   | 1   |      |
| Total          | 188 | 11  |     |      |

**Step 10: Decision.**

- F_critical(0.05, 2, 6) = 5.14: Since F_A = 79.0 > 5.14, reject H0_A. Algorithms differ significantly.
- F_critical(0.05, 3, 6) = 4.76: Since F_B = 8.0 > 4.76, reject H0_B. Datasets differ significantly.

**Conclusion:** Both the algorithm type and the dataset have a statistically significant effect on computation time at the 5% level.

## Worked Example 2: Two-Way ANOVA With Replication

**Problem:** A company tests the effect of 2 training methods (Factor A) and 2 work shifts (Factor B) on productivity. Each combination has 3 replicates.

|          | Shift 1    | Shift 2    |
| -------- | ---------- | ---------- |
| Method 1 | 45, 50, 48 | 40, 42, 38 |
| Method 2 | 55, 58, 52 | 48, 50, 46 |

Test at alpha = 0.05 for main effects and interaction.

**Solution:**

a = 2, b = 2, n = 3, N = 12

**Step 1: Cell totals and means.**

- Cell (1,1): 45+50+48 = 143, mean = 47.67
- Cell (1,2): 40+42+38 = 120, mean = 40.00
- Cell (2,1): 55+58+52 = 165, mean = 55.00
- Cell (2,2): 48+50+46 = 144, mean = 48.00

Row totals: R1 = 143+120 = 263, R2 = 165+144 = 309
Column totals: C1 = 143+165 = 308, C2 = 120+144 = 264
Grand Total: G = 263 + 309 = 572

**Step 2: CF = 572^2 / 12 = 327184 / 12 = 27265.33**

**Step 3: SST.**

Sum of all x^2 = 45^2+50^2+48^2+40^2+42^2+38^2+55^2+58^2+52^2+48^2+50^2+46^2
= 2025+2500+2304+1600+1764+1444+3025+3364+2704+2304+2500+2116 = 27650

SST = 27650 - 27265.33 = 384.67

**Step 4: SSA (Training Methods / Rows).**

SSA = (R1^2 + R2^2) / (b\*n) - CF = (263^2 + 309^2) / 6 - 27265.33
= (69169 + 95481) / 6 - 27265.33 = 164650 / 6 - 27265.33 = 27441.67 - 27265.33 = 176.33

**Step 5: SSB (Shifts / Columns).**

SSB = (C1^2 + C2^2) / (a\*n) - CF = (308^2 + 264^2) / 6 - 27265.33
= (94864 + 69696) / 6 - 27265.33 = 164560 / 6 - 27265.33 = 27426.67 - 27265.33 = 161.33

**Step 6: SSAB (Interaction).**

Sum of Cell Totals^2 / n = (143^2 + 120^2 + 165^2 + 144^2) / 3
= (20449 + 14400 + 27225 + 20736) / 3 = 82810 / 3 = 27603.33

SSAB = 27603.33 - CF - SSA - SSB = 27603.33 - 27265.33 - 176.33 - 161.33 = 0.33

**Step 7: SSE.**

SSE = SST - SSA - SSB - SSAB = 384.67 - 176.33 - 161.33 - 0.33 = 46.67

**Step 8: Degrees of freedom.**

- df_A = a - 1 = 1
- df_B = b - 1 = 1
- df_AB = (a-1)(b-1) = 1
- df_E = ab(n-1) = 2*2*2 = 8
- df_Total = abn - 1 = 11

**Step 9: Mean Squares and F-statistics.**

- MSA = 176.33 / 1 = 176.33
- MSB = 161.33 / 1 = 161.33
- MSAB = 0.33 / 1 = 0.33
- MSE = 46.67 / 8 = 5.83

- F_A = 176.33 / 5.83 = 30.24
- F_B = 161.33 / 5.83 = 27.67
- F_AB = 0.33 / 5.83 = 0.06

**Step 10: ANOVA Table.**

| Source            | SS     | df  | MS     | F     |
| ----------------- | ------ | --- | ------ | ----- |
| Methods (A)       | 176.33 | 1   | 176.33 | 30.24 |
| Shifts (B)        | 161.33 | 1   | 161.33 | 27.67 |
| Interaction (AxB) | 0.33   | 1   | 0.33   | 0.06  |
| Error             | 46.67  | 8   | 5.83   |       |
| Total             | 384.67 | 11  |        |       |

**Step 11: Decision (F_critical(0.05, 1, 8) = 5.32).**

- F_A = 30.24 > 5.32: Reject H0_A. Training methods have a significant effect.
- F_B = 27.67 > 5.32: Reject H0_B. Work shifts have a significant effect.
- F_AB = 0.06 < 5.32: Fail to reject H0_AB. No significant interaction effect.

**Conclusion:** Both training method and work shift significantly affect productivity, but there is no significant interaction between the two factors.

## Understanding Interaction Effects

An interaction effect means that the effect of one factor depends on the level of the other factor. For example, if Method 1 works better in Shift 1 but Method 2 works better in Shift 2, there is an interaction. When the interaction is significant, main effects should be interpreted cautiously because the effect of each factor is not consistent across levels of the other factor.

## Key Points for Exams

- Clearly distinguish between two-way ANOVA with and without replication.
- State all three sets of hypotheses when interaction can be tested.
- Use the correction factor method for efficient computation.
- Always construct the complete ANOVA table.
- Interpret each F-test separately for Factor A, Factor B, and Interaction.
- If interaction is significant, note that main effects must be interpreted with caution.
- Verify: SST = SSA + SSB + SSAB + SSE (with replication) or SST = SSA + SSB + SSE (without replication).

### Further Reading

Refer to your prescribed textbook and official course materials.
