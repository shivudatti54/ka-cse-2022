# **Text Book 1: Chapter 7 (7.2 to 7.3)**

## **7.2: Introduction to Pandas**

### Overview

Pandas is a powerful Python library used for data manipulation and analysis. It provides data structures and functions to efficiently handle structured data, including tabular data such as spreadsheets and SQL tables.

### Key Features

- Data structures: Series (1-dimensional labeled array) and DataFrame (2-dimensional labeled data structure with columns of potentially different types)
- Data manipulation: filtering, sorting, grouping, merging, reshaping
- Data analysis: data cleaning, data transformation, data visualization

### Example Use Case

Suppose we have a CSV file containing information about students and their scores in different subjects. We can use Pandas to read the CSV file, filter the data to only include students who scored above 80 in all subjects, and then group the data by subject and calculate the average score.

```python
import pandas as pd

# Read the CSV file
df = pd.read_csv('students.csv')

# Filter the data to only include students who scored above 80 in all subjects
df_filtered = df[df['Math'] > 80] & df[df['Science'] > 80] & df[df['English'] > 80]

# Group the data by subject and calculate the average score
df_grouped = df_filtered.groupby('Subject')['Score'].mean()

print(df_grouped)
```

### Definition

- **Series**: A one-dimensional labeled array of values, similar to a column in a spreadsheet.
- **DataFrame**: A two-dimensional labeled data structure with columns of potentially different types, similar to an Excel spreadsheet or a SQL table.

### Key Concepts

- **Indexing**: Using labels to access specific rows and columns in a Series or DataFrame.
- **Label-based vs. Position-based Indexing**: Label-based indexing uses labels to access rows and columns, while position-based indexing uses integer positions.
- **Axis**: The axis of a DataFrame can be either 0 (row axis) or 1 (column axis).

### Example Code

```python
import pandas as pd

# Create a sample DataFrame
data = {'Name': ['John', 'Jane', 'Bob'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)

# Access a specific row using indexing
print(df.loc[0])

# Access a specific column using indexing
print(df.loc[:, 'Name'])

# Access a specific row and column using indexing
print(df.loc[0, 'Name'])

# Access a specific row using label-based indexing
print(df['Name'])

# Access a specific column using label-based indexing
print(df['Age'])
```

---

## **7.3: Working with Missing Data**

### Overview

Missing data is a common problem in data analysis, where some values are not available or are unknown. Pandas provides several ways to handle missing data, including detecting and filling missing values.

### Key Features

- **Detecting Missing Data**: using the `isnull()` and `notnull()` methods to detect missing values
- **Filling Missing Data**: using the `fillna()` method to fill missing values with a specified value
- **Handling Missing Data**: using the `dropna()` method to drop rows or columns with missing values

### Example Use Case

Suppose we have a DataFrame containing information about customers and their orders. We can use Pandas to detect and fill missing values in the `Quantity` column.

```python
import pandas as pd

# Create a sample DataFrame
data = {'Customer ID': [1, 2, 3],
        'Quantity': [10, None, 20]}
df = pd.DataFrame(data)

# Detect missing values
print(df.isnull())

# Fill missing values with 0
df['Quantity'] = df['Quantity'].fillna(0)

# Print the updated DataFrame
print(df)
```

### Definition

- **Missing Value**: A value that is not available or is unknown.
- **Imputation**: The process of replacing missing values with a specified value.

### Key Concepts

- **NaT (Not a Time)**: A special value used to represent missing values in time-series data.
- **NaN (Not a Number)**: A special value used to represent missing values in numerical data.
- **Forward Fill**: The process of filling missing values by propagating the value from the previous row.
- **Backward Fill**: The process of filling missing values by propagating the value from the next row.

### Example Code

```python
import pandas as pd
import numpy as np

# Create a sample DataFrame
data = {'Value': [10, np.nan, 20]}
df = pd.DataFrame(data)

# Detect missing values
print(df.isnull())

# Fill missing values with the mean
df['Value'] = df['Value'].fillna(df['Value'].mean())

# Print the updated DataFrame
print(df)
```

---

## **Additional Tips and Tricks**

- Use the `info()` method to display a concise summary of the DataFrame, including the index dtype and column dtypes, non-nullable counts, and memory usage.
- Use the `describe()` method to display a summary of the DataFrame, including the count, mean, standard deviation, minimum, 25%, 50%, 75%, and maximum values.
- Use the `corr()` method to calculate the pairwise correlation between columns.
- Use the `crosstab()` method to calculate the cross-tabulation of two variables.

### Exercises

---

1.  Create a sample DataFrame containing information about students and their scores in different subjects. Use Pandas to filter the data to only include students who scored above 80 in all subjects.
2.  Create a sample DataFrame containing information about customers and their orders. Use Pandas to detect and fill missing values in the `Quantity` column.
3.  Create a sample DataFrame containing information about stock prices. Use Pandas to calculate the pairwise correlation between the `Open` and `Close` columns.

### Conclusion

---

In this module, we learned how to work with Pandas, including creating and manipulating DataFrames, handling missing data, and performing data analysis. We also learned about the different data structures and functions provided by Pandas, including Series and DataFrame, index-based and label-based indexing, and data manipulation and analysis functions. With this knowledge, you can now apply Pandas to real-world problems and unlock the full potential of Python for data science.
