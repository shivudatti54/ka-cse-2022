## Table of Contents

- [Latin-Square Design](#latin-square-design)
- [Introduction](#introduction)
- [When to Use Latin-Square Design](#when-to-use-latin-square-design)
- [Layout Construction](#layout-construction)
  - [Example: 4 x 4 Latin Square](#example-4-x-4-latin-square)
  - [Example: 3 x 3 Latin Square](#example-3-x-3-latin-square)
- [Model](#model)
- [Hypotheses](#hypotheses)
- [Sum of Squares Partitioning](#sum-of-squares-partitioning)
- [Correction Factor Method](#correction-factor-method)
- [Degrees of Freedom](#degrees-of-freedom)
- [Mean Squares](#mean-squares)
- [F-Statistics](#f-statistics)
- [ANOVA Table for Latin-Square Design](#anova-table-for-latin-square-design)
- [Decision Rule](#decision-rule)
- [Worked Example: 4 x 4 Latin Square](#worked-example-4-x-4-latin-square)
- [Advantages of Latin-Square Design](#advantages-of-latin-square-design)
- [Limitations of Latin-Square Design](#limitations-of-latin-square-design)
- [Key Points for exams](#key-points-for-exams)
  - [Further Reading](#further-reading)

### Latin-Square Design

## Introduction

A Latin-square design (LSD) is a special experimental design used to control for two sources of extraneous variation (nuisance variables) while testing the effect of a single treatment factor. The design arranges treatments in a square layout such that each treatment appears exactly once in each row and exactly once in each column. This ensures that the effects of the two blocking variables (rows and columns) are balanced out, leading to a more precise estimate of the treatment effect.

## When to Use Latin-Square Design

- When there are two nuisance factors (blocking variables) that may affect the response.
- When the number of levels of the treatment factor equals the number of levels of each blocking factor.
- When the experimenter wants to control for two sources of variation without testing their interaction.
- Example: Testing the effect of 4 fertilizers on yield, controlling for both field location (rows) and time period (columns).

## Layout Construction

For a p x p Latin square (p treatments, p rows, p columns):

- Arrange a p x p grid.
- Assign p treatments (usually labeled A, B, C, D, ...) so that each treatment appears exactly once in each row and exactly once in each column.

### Example: 4 x 4 Latin Square

|       | Col 1 | Col 2 | Col 3 | Col 4 |
| ----- | ----- | ----- | ----- | ----- |
| Row 1 | A     | B     | C     | D     |
| Row 2 | B     | C     | D     | A     |
| Row 3 | C     | D     | A     | B     |
| Row 4 | D     | A     | B     | C     |

### Example: 3 x 3 Latin Square

|       | Col 1 | Col 2 | Col 3 |
| ----- | ----- | ----- | ----- |
| Row 1 | A     | B     | C     |
| Row 2 | B     | C     | A     |
| Row 3 | C     | A     | B     |

## Model

The statistical model for a Latin-square design is:

x_ij(k) = mu + alpha_i + beta_j + tau_k + e_ij(k)

Where:

- x_ij(k) = observation in row i, column j, receiving treatment k
- mu = overall mean
- alpha_i = effect of the ith row
- beta_j = effect of the jth column
- tau_k = effect of the kth treatment
- e_ij(k) = random error term

## Hypotheses

**For Treatments:**

- H0: tau_1 = tau_2 = ... = tau_p = 0 (no treatment effect)
- H1: At least one tau_k is not zero

**For Rows (optional test):**

- H0: alpha_1 = alpha_2 = ... = alpha_p = 0
- H1: At least one alpha_i is not zero

**For Columns (optional test):**

- H0: beta_1 = beta_2 = ... = beta_p = 0
- H1: At least one beta_j is not zero

## Sum of Squares Partitioning

SST = SSR + SSC + SSTr + SSE

Where:

- **SST (Total Sum of Squares):** sum over all observations of (x_ij(k) - x_bar)^2
- **SSR (Row Sum of Squares):** p \* sum_i (x_bar_i. - x_bar)^2
- **SSC (Column Sum of Squares):** p \* sum*j (x_bar*.j - x_bar)^2
- **SSTr (Treatment Sum of Squares):** p \* sum*k (x_bar*..k - x_bar)^2
- **SSE (Error Sum of Squares):** SST - SSR - SSC - SSTr

## Correction Factor Method

- G = Grand Total of all observations
- N = p^2 (total number of observations)
- CF = G^2 / N
- SST = (Sum of squares of all observations) - CF
- SSR = (Sum of Row Totals^2) / p - CF
- SSC = (Sum of Column Totals^2) / p - CF
- SSTr = (Sum of Treatment Totals^2) / p - CF
- SSE = SST - SSR - SSC - SSTr

## Degrees of Freedom

| Source     | Degrees of Freedom |
| ---------- | ------------------ |
| Rows       | p - 1              |
| Columns    | p - 1              |
| Treatments | p - 1              |
| Error      | (p - 1)(p - 2)     |
| Total      | p^2 - 1            |

**Verification:** (p-1) + (p-1) + (p-1) + (p-1)(p-2) = 3(p-1) + (p-1)(p-2) = (p-1)(3 + p - 2) = (p-1)(p+1) = p^2 - 1

## Mean Squares

- MSR = SSR / (p - 1)
- MSC = SSC / (p - 1)
- MSTr = SSTr / (p - 1)
- MSE = SSE / [(p - 1)(p - 2)]

## F-Statistics

- F_Treatments = MSTr / MSE (primary test of interest)
- F_Rows = MSR / MSE (optional)
- F_Columns = MSC / MSE (optional)

## ANOVA Table for Latin-Square Design

| Source     | SS   | df         | MS                     | F               |
| ---------- | ---- | ---------- | ---------------------- | --------------- |
| Rows       | SSR  | p - 1      | MSR = SSR/(p-1)        | F_R = MSR/MSE   |
| Columns    | SSC  | p - 1      | MSC = SSC/(p-1)        | F_C = MSC/MSE   |
| Treatments | SSTr | p - 1      | MSTr = SSTr/(p-1)      | F_Tr = MSTr/MSE |
| Error      | SSE  | (p-1)(p-2) | MSE = SSE/[(p-1)(p-2)] |                 |
| Total      | SST  | p^2 - 1    |                        |                 |

## Decision Rule

At significance level alpha:

- If F_Treatments > F_critical(alpha, p-1, (p-1)(p-2)), reject H0. The treatments have a significant effect.
- If F_Treatments <= F_critical, fail to reject H0.

## Worked Example: 4 x 4 Latin Square

**Problem:** An experiment uses a 4 x 4 Latin-square design to test the effect of four treatments (A, B, C, D) while controlling for two blocking factors (rows and columns). The observed values are:

|       | Col 1 | Col 2 | Col 3 | Col 4 |
| ----- | ----- | ----- | ----- | ----- |
| Row 1 | A=12  | B=15  | C=20  | D=18  |
| Row 2 | B=17  | C=22  | D=14  | A=10  |
| Row 3 | C=24  | D=16  | A=8   | B=19  |
| Row 4 | D=13  | A=9   | B=21  | C=25  |

Test at alpha = 0.05 whether the treatments differ significantly.

**Solution:**

**Step 1: Identify values and compute totals.**

p = 4, N = 16

Row Totals:

- R1 = 12 + 15 + 20 + 18 = 65
- R2 = 17 + 22 + 14 + 10 = 63
- R3 = 24 + 16 + 8 + 19 = 67
- R4 = 13 + 9 + 21 + 25 = 68

Column Totals:

- C1 = 12 + 17 + 24 + 13 = 66
- C2 = 15 + 22 + 16 + 9 = 62
- C3 = 20 + 14 + 8 + 21 = 63
- C4 = 18 + 10 + 19 + 25 = 72

Treatment Totals:

- T_A = 12 + 10 + 8 + 9 = 39
- T_B = 15 + 17 + 19 + 21 = 72
- T_C = 20 + 22 + 24 + 25 = 91
- T_D = 18 + 14 + 16 + 13 = 61

Grand Total: G = 65 + 63 + 67 + 68 = 263

**Step 2: Correction Factor.**

CF = G^2 / N = 263^2 / 16 = 69169 / 16 = 4323.06

**Step 3: Compute SST.**

Sum of all x^2 = 12^2 + 15^2 + 20^2 + 18^2 + 17^2 + 22^2 + 14^2 + 10^2 + 24^2 + 16^2 + 8^2 + 19^2 + 13^2 + 9^2 + 21^2 + 25^2
= 144 + 225 + 400 + 324 + 289 + 484 + 196 + 100 + 576 + 256 + 64 + 361 + 169 + 81 + 441 + 625 = 4735

SST = 4735 - 4323.06 = 411.94

**Step 4: Compute SSR (Rows).**

SSR = (R1^2 + R2^2 + R3^2 + R4^2) / p - CF
SSR = (65^2 + 63^2 + 67^2 + 68^2) / 4 - 4323.06
SSR = (4225 + 3969 + 4489 + 4624) / 4 - 4323.06
SSR = 17307 / 4 - 4323.06 = 4326.75 - 4323.06 = 3.69

**Step 5: Compute SSC (Columns).**

SSC = (C1^2 + C2^2 + C3^2 + C4^2) / p - CF
SSC = (66^2 + 62^2 + 63^2 + 72^2) / 4 - 4323.06
SSC = (4356 + 3844 + 3969 + 5184) / 4 - 4323.06
SSC = 17353 / 4 - 4323.06 = 4338.25 - 4323.06 = 15.19

**Step 6: Compute SSTr (Treatments).**

SSTr = (T_A^2 + T_B^2 + T_C^2 + T_D^2) / p - CF
SSTr = (39^2 + 72^2 + 91^2 + 61^2) / 4 - 4323.06
SSTr = (1521 + 5184 + 8281 + 3721) / 4 - 4323.06
SSTr = 18707 / 4 - 4323.06 = 4676.75 - 4323.06 = 353.69

**Step 7: Compute SSE.**

SSE = SST - SSR - SSC - SSTr = 411.94 - 3.69 - 15.19 - 353.69 = 39.37

**Step 8: Degrees of freedom.**

- df_R = p - 1 = 3
- df_C = p - 1 = 3
- df_Tr = p - 1 = 3
- df_E = (p-1)(p-2) = 3 \* 2 = 6
- df_Total = p^2 - 1 = 15

**Step 9: Mean Squares.**

- MSR = 3.69 / 3 = 1.23
- MSC = 15.19 / 3 = 5.06
- MSTr = 353.69 / 3 = 117.90
- MSE = 39.37 / 6 = 6.56

**Step 10: F-statistics.**

- F_Tr = MSTr / MSE = 117.90 / 6.56 = 17.97
- F_R = MSR / MSE = 1.23 / 6.56 = 0.19
- F_C = MSC / MSE = 5.06 / 6.56 = 0.77

**Step 11: ANOVA Table.**

| Source     | SS     | df  | MS     | F     |
| ---------- | ------ | --- | ------ | ----- |
| Rows       | 3.69   | 3   | 1.23   | 0.19  |
| Columns    | 15.19  | 3   | 5.06   | 0.77  |
| Treatments | 353.69 | 3   | 117.90 | 17.97 |
| Error      | 39.37  | 6   | 6.56   |       |
| Total      | 411.94 | 15  |        |       |

**Step 12: Decision.**

F_critical(0.05, 3, 6) = 4.76

- F_Tr = 17.97 > 4.76: Reject H0 for treatments. The four treatments differ significantly.
- F_R = 0.19 < 4.76: Fail to reject H0 for rows. Row blocking was not significant.
- F_C = 0.77 < 4.76: Fail to reject H0 for columns. Column blocking was not significant.

**Conclusion:** The treatments have a statistically significant effect on the response variable at the 5% level. The row and column blocking factors did not show significant effects, though they still served to reduce experimental error.

## Advantages of Latin-Square Design

1. Controls for two sources of variation simultaneously.
2. Requires fewer experimental units than a full factorial design.
3. Each treatment is equally represented across rows and columns, providing balanced comparisons.

## Limitations of Latin-Square Design

1. The number of rows, columns, and treatments must all be equal (p x p).
2. Assumes no interaction between rows, columns, and treatments.
3. Error degrees of freedom can be small, especially for small p, reducing the power of the test.
4. Not suitable when interaction effects are expected.

## Key Points for exams

- Know how to construct a Latin square for given p.
- Remember the SS partitioning: SST = SSR + SSC + SSTr + SSE.
- Error df = (p-1)(p-2); this is a commonly asked formula.
- Use the correction factor method for efficient hand computation.
- Always construct the complete ANOVA table with all four sources.
- The treatment F-test is the primary test; row and column tests are optional.

### Further Reading

Refer to your prescribed textbook and official course materials.
