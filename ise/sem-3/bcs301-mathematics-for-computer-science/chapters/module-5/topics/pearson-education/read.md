**Subject:** Mathematics for Computer Science
**Module:** Module 5: Design of Experiments & ANOVA
**Topic:** Pearson's Correlation Coefficient (r)

### Introduction

In computer science, we often need to analyze relationships between variables. For instance, does the number of CPU cores affect a program's execution time? Does the amount of training data improve a machine learning model's accuracy? **Pearson's Correlation Coefficient**, often denoted as **'r'**, is a fundamental statistical tool that quantifies the strength and direction of a _linear_ relationship between two continuous variables. It's a crucial concept in data analysis, predictive modeling, and algorithm optimization, providing a numerical value between -1 and +1 to describe the association.

### Core Concepts

#### 1. What is Pearson's r?

Pearson's correlation coefficient (r) measures the degree to which a change in one continuous variable is associated with a proportional change in another. It indicates both the **direction** and the **magnitude** of a linear relationship.

- **Range:** The value of `r` always lies between -1 and +1.
- **Direction:**
  - **Positive Correlation (r > 0):** As one variable increases, the other tends to increase. (e.g., Years of experience vs. Salary).
  - **Negative Correlation (r < 0):** As one variable increases, the other tends to decrease. (e.g., Page load time vs. User engagement).
  - **No Correlation (r ≈ 0):** There is no apparent linear relationship between the variables.
- **Strength:** The closer the value is to ±1, the stronger the linear relationship.
  - `r = ±0.9` to `±1`: Very strong
  - `r = ±0.7` to `±0.9`: Strong
  - `r = ±0.5` to `±0.7`: Moderate
  - `r = ±0.3` to `±0.5`: Weak
  - `r = ±0` to `±0.3`: Very weak or none

#### 2. The Formula

The most common formula for calculating Pearson's r for a sample of data is:

`r = (Σ[(xᵢ - x̄)(yᵢ - ȳ)]) / (√[Σ(xᵢ - x̄)²] √[Σ(yᵢ - ȳ)²])`

Where:

- `xᵢ`, `yᵢ` are the individual sample points.
- `x̄`, `ȳ` are the sample means of variables X and Y.
- The numerator `Σ[(xᵢ - x̄)(yᵢ - ȳ)]` is the **sum of products of deviations**, which captures the covariation of X and Y.
- The denominator `(√[Σ(xᵢ - x̄)²] √[Σ(yᵢ - ȳ)²])` is the product of the standard deviations of X and Y, which normalizes the coefficient to the -1 to +1 range.

#### 3. Example for Computer Science

Imagine you are analyzing the relationship between the **size of a dataset (X, in GB)** and the **training time of a model (Y, in minutes)**. You collect the following data:

| Data Size (GB) | Training Time (min) |
| :------------- | :------------------ |
| 1              | 5                   |
| 2              | 9                   |
| 3              | 12                  |
| 4              | 16                  |
| 5              | 20                  |

**Step 1: Calculate Means**
`x̄` = (1+2+3+4+5)/5 = 3
`ȳ` = (5+9+12+16+20)/5 = 12.4

**Step 2: Calculate Deviations and Products**
| x | y | (x - x̄) | (y - ȳ) | (x - x̄)(y - ȳ) | (x - x̄)² | (y - ȳ)² |
|---|----|----------|----------|----------------|----------|----------|
|1 |5 | -2 | -7.4 | 14.8 | 4 | 54.76 |
|2 |9 | -1 | -3.4 | 3.4 | 1 | 11.56 |
|3 |12 | 0 | -0.4 | 0 | 0 | 0.16 |
|4 |16 | 1 | 3.6 | 3.6 | 1 | 12.96 |
|5 |20 | 2 | 7.6 | 15.2 | 4 | 57.76 |
|**Σ**| | | | **37.0** | **10** | **137.2**|

**Step 3: Plug into the formula**
`r = 37.0 / (√10 * √137.2) = 37.0 / (3.162 * 11.713) ≈ 37.0 / 37.06 ≈ 0.998`

**Interpretation:** An `r` value of `0.998` indicates an extremely strong positive linear correlation. As the data size increases, the training time increases almost perfectly in a linear fashion. This is a valuable insight for predicting resource requirements.

### Important Limitations

- **Correlation ≠ Causation:** A high `r` value does **not** mean one variable causes the other. There might be a hidden confounding factor.
- **Only Linear Relationships:** Pearson's r only captures linear trends. It can be close to zero for strong non-linear relationships (e.g., a parabolic curve).
- **Sensitive to Outliers:** A single outlier can significantly inflate or deflate the value of `r`.

### Key Points & Summary

- **Purpose:** Pearson's Correlation Coefficient (r) measures the strength and direction of a **linear** relationship between two continuous variables.
- **Range:** `-1 ≤ r ≤ +1`
  - `+1`: Perfect positive linear correlation.
  - `-1`: Perfect negative linear correlation.
  - `0`: No linear correlation.
- **Interpretation:** The sign (+/-) indicates the direction, while the absolute value indicates the strength.
- **Computer Science Applications:** Widely used in data analytics, feature selection for machine learning, performance analysis, and algorithm benchmarking.
- **Caution:** It is a measure of association, not causation. Always visualize your data (e.g., using a scatter plot) alongside calculating `r` to check for linearity and outliers.
