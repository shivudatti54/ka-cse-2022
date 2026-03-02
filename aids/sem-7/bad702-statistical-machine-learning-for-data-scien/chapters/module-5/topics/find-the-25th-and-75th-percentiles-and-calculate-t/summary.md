# **Find the 25th and 75th Percentiles and Calculate the Interquartile Range (IQR)**

- **Definition:**
  - Percentiles: Quantiles that divide a dataset into equal parts, representing a certain percentage of the data.
  - Interquartile Range (IQR): The difference between the 75th percentile (Q3) and the 25th percentile (Q1) of a dataset.

- **Formulas:**
  - Q1 (25th percentile): `Q1 = x[√(n-1)]`
  - Q3 (75th percentile): `Q3 = x[√(n-1)] + 3 * √(n-1)`
  - IQR: `IQR = Q3 - Q1`

- **Theorems:**
  - **Interquartile Range**: The IQR is a measure of the spread or dispersion of a dataset, which is more robust than the range or variance.
- **Calculating IQR:**
  - Identify the first quartile (Q1) and the third quartile (Q3) in the dataset.
  - Calculate the IQR using the formula: `IQR = Q3 - Q1`

- **Example:**
  - Suppose we have a dataset: `[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]`
  - Q1: 40
  - Q3: 70
  - IQR: 70 - 40 = 30

- **Importance:**
  - IQR is used to detect outliers and to understand the spread of a dataset in a robust way.
  - It is commonly used in statistical analysis and data visualization.
