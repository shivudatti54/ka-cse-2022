# **Text Book 1: Chapter 7 (7.2 to 7.3)**

## **7.2: Introduction to Pandas**

### Overview

Pandas is a powerful open-source library in Python for data manipulation and analysis. It provides data structures and functions to efficiently handle structured data, including tabular data such as spreadsheets and SQL tables.

### Key Features

- **Data Structures**: Pandas introduces two primary data structures: Series (1-dimensional labeled array) and DataFrame (2-dimensional labeled data structure with columns of potentially different types).
- **Data Input/Output**: Pandas supports reading and writing data from various file formats, including CSV, Excel, JSON, and SQL databases.
- **Data Cleaning and Manipulation**: Pandas offers various functions for handling missing data, filtering, sorting, grouping, and merging data.

### Example Code

```python
import pandas as pd

# Create a sample DataFrame
data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 24, 35, 32],
        'Country': ['USA', 'UK', 'Australia', 'Germany']}
df = pd.DataFrame(data)

# Print the DataFrame
print(df)
```

Output:

```
     Name  Age    Country
0     John   28        USA
1     Anna   24         UK
2    Peter   35  Australia
3    Linda   32    Germany
```

### Key Concepts

- **Series**: A one-dimensional labeled array of values.
- **DataFrame**: A two-dimensional labeled data structure with columns of potentially different types.
- **Data Input/Output**: Reading and writing data from various file formats.
- **Data Cleaning and Manipulation**: Handling missing data, filtering, sorting, grouping, and merging data.

### Practice Problems

1.  Create a sample DataFrame and print its information.
2.  Read a CSV file into a DataFrame and print its contents.
3.  Filter a DataFrame to include only rows where the 'Age' column is greater than 30.

---

## **7.3: Data Structures and Operations**

### Overview

This chapter covers the basics of Pandas data structures and operations.

### Series Operations

- **Indexing**: Selecting a specific value or range of values in a Series.
- **Slicing**: Extracting a subset of values from a Series.
- **Arithmetic Operations**: Performing arithmetic operations on Series.

### DataFrame Operations

- **Indexing**: Selecting a specific row or column in a DataFrame.
- **Slicing**: Extracting a subset of rows or columns from a DataFrame.
- **GroupBy**: Partitioning a DataFrame into groups and performing aggregation operations.
- **Merging**: Combining two DataFrames based on a common column.

### Key Concepts

- **Indexing**: Selecting a specific value or range of values in a Series or DataFrame.
- **Slicing**: Extracting a subset of values from a Series or DataFrame.
- **Arithmetic Operations**: Performing arithmetic operations on Series.
- **GroupBy**: Partitioning a DataFrame into groups and performing aggregation operations.
- **Merging**: Combining two DataFrames based on a common column.

### Example Code

```python
import pandas as pd

# Create a sample Series
s = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])

# Print the Series
print(s)

# Indexing
print(s['a'])

# Slicing
print(s[1:3])

# Arithmetic Operations
s2 = s + 1
print(s2)

# GroupBy
df = pd.DataFrame({'Country': ['USA', 'USA', 'UK', 'UK'], 'Sales': [100, 200, 50, 75]})
grouped_df = df.groupby('Country')['Sales'].sum()
print(grouped_df)

# Merging
df1 = pd.DataFrame({'Name': ['John', 'Anna', 'Peter'], 'Age': [28, 24, 35]})
df2 = pd.DataFrame({'Name': ['John', 'Anna', 'Peter'], 'Country': ['USA', 'UK', 'Australia']})
merged_df = pd.merge(df1, df2, on='Name')
print(merged_df)
```

Output:

```
0    1
1    2
2    3
3    4
Name: a, dtype: int64

0    1
1    2
2    3
3    4
Name: [1, 2, 3, 4, 5], dtype: int64

    Country  Sales
Country
USA        300
UK          125
Name: Sales, dtype: int64

     Name  Age    Country
0     John   28        USA
1     Anna   24         UK
2    Peter   35  Australia

   Name  Age Country
0   John  28      USA
1  Anna  24       UK
2  Peter  35  Australia
```

### Key Concepts

- **Indexing**: Selecting a specific value or range of values in a Series or DataFrame.
- **Slicing**: Extracting a subset of values from a Series or DataFrame.
- **Arithmetic Operations**: Performing arithmetic operations on Series.
- **GroupBy**: Partitioning a DataFrame into groups and performing aggregation operations.
- **Merging**: Combining two DataFrames based on a common column.

### Practice Problems

1.  Create a sample Series and perform arithmetic operations on it.
2.  Create a sample DataFrame and perform grouping and aggregation operations on it.
3.  Create two sample DataFrames and merge them based on a common column.
