# Exploratory Data Analysis Revision Notes

## Module: Data Manipulation with Pandas - I

### Chapter 13: Introduction to Pandas

- **Pandas Overview**:
  - Pandas is a Python library used for data manipulation and analysis.
  - It provides data structures and functions to efficiently handle structured data.
- **Importing Pandas**:
  - `import pandas as pd`
- **Creating a DataFrame**:
  - `df = pd.DataFrame(data, columns=['column1', 'column2'])`

### Chapter 16: Handling Missing Data

- **Types of Missing Data**:
  - Missing completely at random (MCAR)
  - Missing at random (MAR)
  - Missing not at random (MNAR)
- **Handling Missing Data**:
  - Dropping rows with missing values (`df.dropna()`)
  - Filling missing values (`df.fillna()`)
  - Imputing missing values (`df.fillna(mean_value)`)

### Chapter 17: Hierarchical Indexing

- **Hierarchical Indexing**:
  - Multi-level indexing for DataFrames and Series.
  - Creating a hierarchical index (`df.index = pd.MultiIndex.from_tuples(...)`)
- **Accessing Hierarchical Index**:
  - `df.loc[tuple]`
  - `df.iloc[tuple]`

### Chapter 21: Data Reshaping and Merging

- **Data Reshaping**:
  - Melting and pivoting DataFrames (`pd.melt()`, `pd.pivot_table()`)
- **Data Merging**:
  - Inner join (`df.merge(other_df, on='column_name', how='inner')`)
  - Outer join (`df.merge(other_df, on='column_name', how='outer')`)

### Important Formulas and Definitions

- **Mean Absolute Error (MAE)**: `MAE = (1/n) * sum(abs(y_true - y_pred))`
- **Mean Squared Error (MSE)**: `MSE = (1/n) * sum((y_true - y_pred)^2)`
- **Coefficient of Determination (R-squared)**: `R-squared = (1 - (SSE / SST)) * 100`

### Important Theorems

- **No Free Lunch Theorem**: "There is no free lunch in computation."
- **Data Quality Theorem**: "The quality of data is the quality of the information derived from it."
