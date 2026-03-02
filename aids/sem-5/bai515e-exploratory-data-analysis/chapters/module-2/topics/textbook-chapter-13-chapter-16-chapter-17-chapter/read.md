# **Exploratory Data Analysis with Pandas**

## **Table of Contents**

1. [Introduction to Pandas Objects](#introduction-to-pandas-objects)
2. [Handling Missing Data](#handling-missing-data)
3. [Hierarchical Indexing](#hierarchical-indexing)
4. [Example Exercises](#example-exercises)

## **Introduction to Pandas Objects**

- **Pandas**: A powerful library in Python for data manipulation and analysis.
- **Series**: A one-dimensional labeled array of values, similar to a column in a spreadsheet.
- **DataFrame**: A two-dimensional labeled data structure with columns of potentially different types, similar to a spreadsheet or SQL table.

### Creating Pandas Objects

- Create a pandas Series:
  ```python
  import pandas as pd

# Create a pandas Series

data = {'Name': ['Tom', 'Nick', 'John'],
'Age': [20, 21, 19]}
series = pd.Series(data)
print(series)

````
*   Create a pandas DataFrame:
    ```python
import pandas as pd

# Create a pandas DataFrame
data = {'Name': ['Tom', 'Nick', 'John'],
        'Age': [20, 21, 19],
        'Country': ['USA', 'Canada', 'USA']}
df = pd.DataFrame(data)
print(df)
````

## **Handling Missing Data**

- **Missing Values**: Unknown or undefined values in a dataset.
- **Types of Missing Values**: `NaN` (Not a Number), `NULL`, `None`
- **How to Handle Missing Values**: Replace, Impute, Interpolate

### Handling Missing Values with Pandas

- Check for missing values:
  ```python
  import pandas as pd

# Create a pandas DataFrame with missing values

data = {'Name': ['Tom', 'Nick', 'John'],
'Age': [20, 21, None]}
df = pd.DataFrame(data)
print(df.isnull()) # Returns a boolean mask for missing values

````
*   Replace missing values:
    ```python
import pandas as pd

# Create a pandas DataFrame with missing values
data = {'Name': ['Tom', 'Nick', 'John'],
        'Age': [20, 21, None]}
df = pd.DataFrame(data)
df['Age'].fillna(18, inplace=True)  # Replace missing value with 18
print(df)
````

## **Hierarchical Indexing**

- **Hierarchical Indexing**: A multi-level index that allows for more complex data structures.
- **Types of Hierarchical Indexes**: Multi-level, Hierarchical, Interval
- **How to Create Hierarchical Indexes**: Use `pd.MultiIndex` or `pd.IntervalIndex`

### Creating Hierarchical Indexes with Pandas

- Create a multi-level index:
  ```python
  import pandas as pd

# Create a pandas DataFrame with a multi-level index

data = {'City': ['New York', 'Chicago', 'Los Angeles'],
'State': ['NY', 'IL', 'CA'],
'Population': [8500000, 2700000, 4000000]}
df = pd.DataFrame(data)
print(df.index)

````
*   Create an interval index:
    ```python
import pandas as pd

# Create a pandas DataFrame with an interval index
data = {'Time': [pd.Timestamp('2022-01-01'), pd.Timestamp('2022-01-02'), pd.Timestamp('2022-01-03')],
        'Temperature': [20, 25, 30]}
df = pd.DataFrame(data)
print(df.index)
````

## **Example Exercises**

1.  Create a pandas Series and DataFrame with some sample data, and then handle missing values using the `fillna` method.
2.  Create a pandas DataFrame with a multi-level index, and then perform some basic data analysis operations (e.g., filtering, grouping).
3.  Create a pandas DataFrame with an interval index, and then perform some basic data analysis operations (e.g., filtering, grouping).

## **Conclusion**

In this study material, we covered the basics of pandas objects, handling missing data, and hierarchical indexing. We learned how to create pandas Series and DataFrames, handle missing values, and create hierarchical indexes. Practice these concepts to become proficient in exploratory data analysis with pandas.
