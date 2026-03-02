# **Pandas in Depth: Data Manipulation**

## **Module 6: 6 hours**

## **Topic: Data Manipulation**

In this module, we will delve deeper into the data manipulation capabilities of the Pandas library. We will cover data preparation, concatenating data, transformation, discretization, binning, permutation, and string manipulation.

## **Data Preparation**

Data preparation is the process of cleaning and preprocessing data before it is used for analysis or modeling. This includes handling missing data, data normalization, and data transformation.

### Handling Missing Data

Missing data is a common problem in data analysis. Pandas provides several ways to handle missing data, including:

- **dropna()**: This function drops rows or columns with missing values.
- **fillna()**: This function fills missing values with a specified value.
- **isnull()**: This function returns a boolean array indicating whether a value is missing.

```python
import pandas as pd

# Create a sample DataFrame with missing values
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, None, 35],
    'City': ['New York', 'Paris', 'Berlin', 'London']
}
df = pd.DataFrame(data)

# Drop rows with missing values
df_dropped = df.dropna()
print(df_dropped)

# Fill missing values with a specified value
df_filled = df.fillna('Unknown')
print(df_filled)

# Check for missing values
missing_values = df.isnull()
print(missing_values)
```

### Data Normalization

Data normalization is the process of scaling numeric data to a common range. Pandas provides the `min_max_scaler` from the `sklearn.preprocessing` module.

```python
from sklearn.preprocessing import MinMaxScaler

# Create a sample DataFrame with numeric data
data = {
    'Age': [28, 24, 35, 32],
    'Height': [180, 165, 175, 168]
}
df = pd.DataFrame(data)

# Normalize data
scaler = MinMaxScaler()
normalized_data = scaler.fit_transform(df)
print(normalized_data)
```

### Data Transformation

Data transformation is the process of changing the format of data. Pandas provides several functions for data transformation, including:

- **astype()**: This function converts data type.
- **apply()**: This function applies a function to each element of a Series or DataFrame.
- **map()**: This function applies a function to each element of a Series or DataFrame.

```python
# Create a sample DataFrame with string data
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'City': ['New York', 'Paris', 'Berlin', 'London']
}
df = pd.DataFrame(data)

# Convert data type
df_converted = df.astype(str)
print(df_converted)

# Apply a function to each element of a Series
def convert_to_uppercase(s):
    return s.upper()

df_applied = df.apply(convert_to_uppercase)
print(df_applied)

# Apply a function to each element of a Series
def extract_name(s):
    return s.split('_')[0]

df_applied = df.map(extract_name)
print(df_applied)
```

## **Concatenating Data**

Concatenating data is the process of joining two or more DataFrames together. Pandas provides several functions for concatenating data, including:

- **concat()**: This function concatenates two or more DataFrames.
- **join()**: This function joins two or more DataFrames based on a common column.

```python
# Create two sample DataFrames
data1 = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, 35, 32]
}
df1 = pd.DataFrame(data1)

data2 = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'City': ['New York', 'Paris', 'Berlin', 'London']
}
df2 = pd.DataFrame(data2)

# Concatenate DataFrames
df_concat = pd.concat([df1, df2])
print(df_concat)

# Join DataFrames based on a common column
df_join = df1.join(df2, lsuffix='_1', rsuffix='_2')
print(df_join)
```

## **Transformation, Discretization, Binning, Permutation, and String Manipulation**

### Transformation

Transformation is the process of changing the format of data. Pandas provides several functions for transformation, including:

- **map()**: This function applies a function to each element of a Series or DataFrame.
- **apply()**: This function applies a function to each element of a Series or DataFrame.

```python
# Create a sample DataFrame with string data
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'City': ['New York', 'Paris', 'Berlin', 'London']
}
df = pd.DataFrame(data)

# Apply a function to each element of a Series
def extract_name(s):
    return s.split('_')[0]

df_applied = df.map(extract_name)
print(df_applied)

# Apply a function to each element of a Series
def convert_to_uppercase(s):
    return s.upper()

df_applied = df.apply(convert_to_uppercase)
print(df_applied)
```

### Discretization

Discretization is the process of dividing a continuous variable into discrete categories. Pandas provides several functions for discretization, including:

- **cut()**: This function divides a Series into discrete categories.

```python
# Create a sample DataFrame with numeric data
data = {
    'Age': [28, 24, 35, 32],
    'Income': [50000, 60000, 70000, 80000]
}
df = pd.DataFrame(data)

# Discretize data
df_discrete = df.apply(lambda x: pd.cut(x, bins=[0, 30000, 60000, 80000, 100000]))
print(df_discrete)
```

### Binning

Binning is the process of dividing a continuous variable into discrete categories based on the value of the variable. Pandas provides several functions for binning, including:

- **quantile()**: This function divides a Series into discrete categories based on the quantile of the data.
- **cut()**: This function divides a Series into discrete categories.

```python
# Create a sample DataFrame with numeric data
data = {
    'Age': [28, 24, 35, 32],
    'Income': [50000, 60000, 70000, 80000]
}
df = pd.DataFrame(data)

# Bin data
df_binned = df.apply(lambda x: pd.qcut(x, q=5))
print(df_binned)
```

### Permutation

Permutation is the process of rearranging the elements of a Series or DataFrame. Pandas provides several functions for permutation, including:

- **sample()**: This function returns a new DataFrame with a random sample of rows from the original DataFrame.

```python
# Create a sample DataFrame
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, 35, 32]
}
df = pd.DataFrame(data)

# Permute data
df_permuted = df.sample(n=4)
print(df_permuted)
```

### String Manipulation

String manipulation is the process of performing operations on strings. Pandas provides several functions for string manipulation, including:

- **str.lower()**: This function converts a Series or DataFrame to lowercase.
- **str.upper()**: This function converts a Series or DataFrame to uppercase.
- **str.split()**: This function splits a Series or DataFrame into substrings.

```python
# Create a sample DataFrame with string data
data = {
    'Name': ['John_Doe', 'Anna_Smith', 'Peter_Brown', 'Linda_Green'],
    'City': ['New York', 'Paris', 'Berlin', 'London']
}
df = pd.DataFrame(data)

# Convert data to lowercase
df_lower = df.apply(lambda x: x.str.lower())
print(df_lower)

# Convert data to uppercase
df_upper = df.apply(lambda x: x.str.upper())
print(df_upper)

# Split data into substrings
df_split = df.apply(lambda x: x.str.split('_', expand=True))
print(df_split)
```
