# Exploratory Data Analysis

## Module: Data Manipulation with Pandas - I: Introducing Pandas Objects, Handling Missing Data, Hierarchical Indexing

This module focuses on the fundamentals of Pandas, a powerful library in Python for data manipulation and analysis. It introduces Pandas objects, handling missing data, and hierarchical indexing. In this module, we will delve into the world of Exploratory Data Analysis (EDA) and cover all aspects of Pandas that are essential for data scientists and analysts.

### Chapter 13: Introduction to Pandas

Pandas is a popular open-source library in Python developed by Wes McKinney. It provides data structures and functions to efficiently handle and process large datasets, including tabular data such as spreadsheets and SQL tables.

#### Key Features of Pandas

- **Series**: A one-dimensional labeled array of values, similar to a column in a spreadsheet.
- **DataFrame**: A two-dimensional labeled data structure with columns of potentially different types, similar to an Excel spreadsheet or SQL table.

#### Installing Pandas

You can install Pandas using pip, the Python package manager:

```bash
pip install pandas
```

### Chapter 16: Handling Missing Data

Missing data is a common challenge in data analysis. Pandas provides several methods to handle missing data, including:

- **Drop Missing Values**: Remove rows or columns with missing values.
- **Fill Missing Values**: Replace missing values with a specific value, such as the mean or median.
- **Interpolate Missing Values**: Fill missing values using interpolation methods.

#### Example: Handling Missing Data

```python
import pandas as pd
import numpy as np

# Create a DataFrame with missing values
data = {
    'A': [1, 2, np.nan, 4],
    'B': [5, np.nan, 7, 8]
}
df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# Drop rows with missing values
df_dropped = df.dropna()

print("\nDataFrame after dropping rows with missing values:")
print(df_dropped)

# Fill missing values with the mean
df_filled = df.fillna(df.mean())

print("\nDataFrame after filling missing values with the mean:")
print(df_filled)

# Interpolate missing values
df_interpolated = df.interpolate()

print("\nDataFrame after interpolating missing values:")
print(df_interpolated)
```

### Chapter 17: Hierarchical Indexing

Hierarchical indexing is a feature of Pandas that allows you to create multiple levels of indexing for your DataFrames. This is useful for handling datasets with multiple variables and complex index structures.

#### Example: Hierarchical Indexing

```python
import pandas as pd

# Create a DataFrame with hierarchical indexing
data = {
    'Country': ['USA', 'USA', 'Canada', 'Canada'],
    'City': ['New York', 'Los Angeles', 'Toronto', 'Vancouver'],
    'Population': [8.4, 4, 2.7, 6.5]
}
df = pd.DataFrame(data)

print("DataFrame with hierarchical indexing:")
print(df)

# Accessing data using hierarchical indexing
print("\nAccessing data using hierarchical indexing:")
print(df.loc[('USA', 'New York')])

# Renaming the index
df.index = ['Country_' + x for x in df.index]
print("\nDataFrame with renamed index:")
print(df)
```

### Chapter 21: GroupBy and Aggregation

GroupBy and aggregation are essential tools for data analysis, allowing you to perform calculations on groups of data.

#### Example: GroupBy and Aggregation

```python
import pandas as pd

# Create a DataFrame
data = {
    'City': ['New York', 'New York', 'Los Angeles', 'Los Angeles', 'Chicago', 'Chicago'],
    'Year': [2015, 2016, 2015, 2016, 2015, 2016],
    'Sales': [100, 120, 80, 90, 120, 150]
}
df = pd.DataFrame(data)

print("DataFrame:")
print(df)

# GroupBy and aggregation
grouped = df.groupby('City')['Sales'].sum()
print("\nGroupBy and aggregation:")
print(grouped)

# Pivot table
pivot = df.pivot_table(index='City', columns='Year', values='Sales', aggfunc='sum')
print("\nPivot table:")
print(pivot)
```

### Further Reading

- Pandas documentation: <https://pandas.pydata.org/docs/>
- DataCamp's Pandas course: <https://www.datacamp.com/tracks/pandas-python>
- Kaggle's Pandas tutorial: <https://www.kaggle.com/pandas-tutorial>

By mastering Pandas, you can unlock the full potential of your data and become a proficient data analyst. Remember to practice regularly and explore the vast resources available online to deepen your knowledge.
