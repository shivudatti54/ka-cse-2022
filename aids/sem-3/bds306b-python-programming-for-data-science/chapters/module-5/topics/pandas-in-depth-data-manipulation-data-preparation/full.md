# Pandas in Depth: Data Manipulation

### Table of Contents

1. [Introduction](#introduction)
2. [Data Preparation](#data-preparation)
   - [Handling Missing Data](#handling-missing-data)
   - [Data Cleaning](#data-cleaning)
   - [Data Transformation](#data-transformation)
3. [Concatenating Data](#concatenating-data)
   - [Merging and Joining Data](#merging-and-joining-data)
   - [Pandas Concatenation](#pandas-concatenation)
4. [Data Transformation and Discretization](#data-transformation-and-discretization)
   - [Discretization](#discretization)
   - [Binning](#binning)
   - [Data Transformation](#data-transformation)
5. [Permutation and Sampling](#permutation-and-sampling)
   - [Shuffling Data](#shuffling-data)
   - [Random Sampling](#random-sampling)
   - [Stratified Sampling](#stratified-sampling)
6. [String Manipulation](#string-manipulation)
   - [String Preprocessing](#string-preprocessing)
   - [Text Analysis](#text-analysis)
7. [Data Analysis and Visualization](#data-analysis-and-visualization)
8. [Conclusion](#conclusion)
9. [Further Reading](#further-reading)

### Introduction

Pandas is a powerful Python library used for data manipulation and analysis. It provides data structures and functions to efficiently handle and process large datasets. In this module, we will delve into the world of Pandas, exploring its capabilities in data preparation, concatenating data, transformation, discretization, permutation, string manipulation, and data analysis.

### Data Preparation

---

Data preparation is the process of cleaning, transforming, and normalizing data before it can be used for analysis. This step is crucial in data science, as it can significantly impact the accuracy and reliability of the results.

#### Handling Missing Data

---

Missing data is a common problem in datasets. Pandas provides several methods to handle missing data.

- **`isnull()`**: This function returns a boolean mask indicating whether the values are missing or not.
- **`fillna()`**: This function replaces missing values with a specified value.
- **`dropna()`**: This function drops rows or columns with missing values.

```python
import pandas as pd
import numpy as np

# Create a DataFrame with missing values
data = {
    'Name': ['John', 'Alice', 'Bob', np.nan],
    'Age': [25, 30, np.nan, 35]
}
df = pd.DataFrame(data)

# Handle missing values using isnull()
print(df.isnull())

# Handle missing values using fillna()
df['Name'] = df['Name'].fillna('Unknown')

# Handle missing values using dropna()
df = df.dropna()
```

#### Data Cleaning

---

Data cleaning involves removing or transforming data that is incorrect, redundant, or irrelevant.

- **`df.drop()`**: This function removes rows or columns from the DataFrame.
- **`df.rename()`**: This function renames columns in the DataFrame.
- **`df.sort_values()`**: This function sorts the DataFrame by one or more columns.

```python
# Remove rows with missing values
df = df.dropna()

# Rename columns
df = df.rename(columns={'Age': 'Age_Given'})

# Sort data by Name
df = df.sort_values(by='Name')
```

#### Data Transformation

---

Data transformation involves changing the structure or format of the data.

- **`df.astype()`**: This function converts the data type of a column or multiple columns.
- **`df.apply()`**: This function applies a function to each element of a column or multiple columns.
- **`df.map()`**: This function applies a function to each element of a column or multiple columns.

```python
# Convert 'Age_Given' to integer
df['Age_Given'] = df['Age_Given'].astype(int)

# Apply a function to each element of 'Name'
df['Name'] = df['Name'].apply(lambda x: x.upper())

# Map a function to each element of 'Age_Given'
df['Age'] = df['Age_Given'].map(lambda x: x + 5)
```

### Concatenating Data

---

Concatenating data involves combining two or more DataFrames into one.

#### Merging and Joining Data

---

Merging and joining data involve combining data from two or more DataFrames based on a common column.

- **`pd.merge()`**: This function merges two DataFrames based on a common column.
- **`pd.join()`**: This function joins two DataFrames based on a common column.

```python
# Merge two DataFrames
df1 = pd.DataFrame({
    'Name': ['John', 'Alice', 'Bob'],
    'Age': [25, 30, 35]
})
df2 = pd.DataFrame({
    'Name': ['John', 'Alice', 'Bob'],
    'City': ['New York', 'London', 'Paris']
})
merged_df = pd.merge(df1, df2, on='Name')

# Join two DataFrames
df1 = pd.DataFrame({
    'Name': ['John', 'Alice', 'Bob'],
    'Age': [25, 30, 35]
})
df2 = pd.DataFrame({
    'Name': ['John', 'Alice', 'Bob'],
    'City': ['New York', 'London', 'Paris']
})
joined_df = pd.join(df1, df2, on='Name')
```

#### Pandas Concatenation

---

Pandas provides several methods to concatenate DataFrames.

- **`pd.concat()`**: This function concatenates two or more DataFrames.
- **`pd.concat()` with axis**: This function concatenates DataFrames along a specified axis.

```python
# Concatenate two DataFrames
df1 = pd.DataFrame({
    'Name': ['John', 'Alice', 'Bob'],
    'Age': [25, 30, 35]
})
df2 = pd.DataFrame({
    'Name': ['John', 'Alice', 'Bob'],
    'Age': [25, 30, 35]
})
concatenated_df = pd.concat([df1, df2])

# Concatenate DataFrames along axis 0
df1 = pd.DataFrame({
    'Name': ['John', 'Alice', 'Bob'],
    'Age': [25, 30, 35]
})
df2 = pd.DataFrame({
    'Name': ['John', 'Alice', 'Bob'],
    'Age': [25, 30, 35]
})
concatenated_df = pd.concat([df1, df2], axis=0)
```

### Data Transformation and Discretization

---

Data transformation and discretization involve changing the structure or format of the data.

#### Discretization

---

Discretization involves dividing the data into discrete intervals or categories.

- **`pd.cut()`**: This function divides the data into discrete intervals or categories.

```python
# Discretize 'Age_Given' into intervals
df['Age_Cut'] = pd.cut(df['Age_Given'], bins=[20, 30, 40, 50, np.inf])
```

#### Binning

---

Binning involves dividing the data into discrete intervals or categories.

- **`pd.cut()`**: This function divides the data into discrete intervals or categories.

```python
# Bin 'Age_Given' into intervals
df['Age_Bin'] = pd.cut(df['Age_Given'], bins=[20, 30, 40, 50, np.inf])
```

#### Data Transformation

---

Data transformation involves changing the structure or format of the data.

- **`df.astype()`**: This function converts the data type of a column or multiple columns.
- **`df.apply()`**: This function applies a function to each element of a column or multiple columns.
- **`df.map()`**: This function applies a function to each element of a column or multiple columns.

```python
# Convert 'Age_Given' to integer
df['Age_Given'] = df['Age_Given'].astype(int)

# Apply a function to each element of 'Name'
df['Name'] = df['Name'].apply(lambda x: x.upper())

# Map a function to each element of 'Age_Given'
df['Age'] = df['Age_Given'].map(lambda x: x + 5)
```

### Permutation and Sampling

---

Permutation and sampling involve randomly rearranging or selecting data.

#### Shuffling Data

---

Shuffling data involves randomly rearranging the rows of the DataFrame.

- **`df.sample()`**: This function randomly samples the rows of the DataFrame.
- **`df.sample(frac=0.5)`**: This function randomly samples 50% of the rows of the DataFrame.

```python
# Shuffle data
df = df.sample()

# Randomly sample 50% of data
df = df.sample(frac=0.5)
```

#### Random Sampling

---

Random sampling involves randomly selecting rows from the DataFrame.

- **`df.sample(n)`**: This function randomly samples n rows from the DataFrame.
- **`df.sample(n, replace=False)`**: This function randomly samples n rows from the DataFrame without replacement.

```python
# Randomly sample 10 rows
df = df.sample(n=10)

# Randomly sample 10 rows without replacement
df = df.sample(n=10, replace=False)
```

#### Stratified Sampling

---

Stratified sampling involves randomly selecting rows from the DataFrame while maintaining the proportion of each subgroup.

- **`df.sample(frac=0.5, replace=False)`**: This function randomly samples the data with replacement using stratified sampling.
- **`df.sample(frac=0.5, replace=False, stratify='Age')`**: This function randomly samples the data with replacement using stratified sampling and maintaining the proportion of each subgroup.

```python
# Randomly sample the data with replacement using stratified sampling
df = df.sample(frac=0.5, replace=False)

# Randomly sample the data with replacement using stratified sampling and maintaining the proportion of each subgroup
df = df.sample(frac=0.5, replace=False, stratify='Age')
```

### String Manipulation

---

String manipulation involves performing operations on strings.

- **`df.apply()`**: This function applies a function to each element of a column or multiple columns.
- **`df.map()`**: This function applies a function to each element of a column or multiple columns.
- **`df.applymap()`**: This function applies a function to each element of a DataFrame or multiple DataFrames.

```python
# Apply a function to each element of 'Name'
df['Name'] = df['Name'].apply(lambda x: x.upper())

# Map a function to each element of 'Age_Given'
df['Age'] = df['Age_Given'].map(lambda x: x + 5)

# Apply a function to each element of the DataFrame
df.apply(lambda x: x.upper())
```

### Data Analysis and Visualization

---

Data analysis and visualization involve extracting insights from the data.

- **`df.describe()`**: This function provides summary statistics for the DataFrame.
- **`df.groupby()`**: This function groups the DataFrame by one or more columns.
- **`df.pivot_table()`**: This function creates a pivot table from the DataFrame.

```python
# Extract summary statistics
df.describe()

# Group data by 'Age'
df.groupby('Age').sum()

# Create a pivot table
df.pivot_table(index='Name', columns='Age', values='Score')
```

### Conclusion

==============

In this module, we have covered the basics of Pandas, including data preparation, concatenating data, transformation, discretization, permutation, string manipulation, and data analysis. We have also discussed the importance of data cleaning, handling missing data, and data visualization. By mastering these skills, you can efficiently handle and process large datasets, extract insights, and make informed decisions.

### Further Reading

==================

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)
- [Data Analysis with Python](https://www.datacamp.com/tutorial/data-analysis-with-python)
- [Data Visualization with Python](https://www.datacamp.com/tutorial/data-visualization-with-python)

By reading these resources, you can further improve your skills in data science and machine learning with Python.
