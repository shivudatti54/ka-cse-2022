# **Exploratory Data Analysis Revision Notes**

### Module: Data Manipulation with Pandas - I: Introducing Pandas Objects, Handling Missing Data, Hierarchical

#### Chapter 13: Introduction to Pandas

- **Pandas Overview**
  - Library for data manipulation and analysis
  - Provides data structures (Series, DataFrame) and functions for data cleaning and manipulation
- **Importing Pandas**
  - `import pandas as pd`

#### Chapter 16: Series and Indexing

- **Series Overview**
  - One-dimensional labeled array of values
  - Index and columns provide labels for data
- **Indexing and Selecting Data**
  - Basic indexing: `df['column_name']`
  - Label-based indexing: `df.loc[labels]`
  - Integer-based indexing: `df.iloc[row_start : row_end]`
- **Data Operations**
  - Arithmetic operations: `df['column_name'] + df['another_column']`
  - Comparison operations: `df['column_name'] == 'value'`

#### Chapter 17: DataFrames

- **DataFrame Overview**
  - Two-dimensional labeled data structure with columns of potentially different types
- **Creating DataFrames**
  - From scalar values: `pd.DataFrame(data)`
  - From lists or dictionaries: `pd.DataFrame(data, columns=...)`
- **Data Operations**
  - Basic operations: `df['column_name']`
  - Merge and join operations: `pd.concat()`, `pd.merge()`

#### Chapter 21: Handling Missing Data

- **Missing Data Overview**
  - Data that is not present or recorded for a particular value
- **Detecting Missing Data**
  - `df.isnull()`
  - `df.notnull()`
- **Handling Missing Data**
  - Drop missing values: `df.dropna()`
  - Fill missing values: `df.fillna(value)`

## Formulas, Definitions, and Theorems

- **Mean**: $\bar{x} = \frac{1}{n} \sum_{i=1}^{n} x_i$
- **Standard Deviation**: $\sigma = \sqrt{\frac{1}{n-1} \sum_{i=1}^{n} (x_i - \bar{x})^2}$
- **Correlation Coefficient**: $\rho = \frac{\sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y})}{\sqrt{\sum_{i=1}^{n} (x_i - \bar{x})^2} \sqrt{\sum_{i=1}^{n} (y_i - \bar{y})^2}}$
