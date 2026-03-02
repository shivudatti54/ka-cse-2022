# **The pandas Library: An Introduction to Data Structures, Indexes, Operations, and Function Application**

## **Table of Contents**

1. [Introduction to pandas](#introduction-to-pandas)
2. [Data Structures in pandas](#data-structures-in-pandas)
3. [Indexes in pandas](#indexes-in-pandas)
4. [Operations between data structures in pandas](#operations-between-data-structures-in-pandas)
5. [Function Application in pandas](#function-application-in-pandas)

## **1. Introduction to pandas**

pandas is a powerful and flexible open-source library in Python for data manipulation and analysis. It provides data structures and functions to efficiently handle structured data, including tabular data such as spreadsheets and SQL tables.

**Key Concepts:**

- **DataFrame**: A 2-dimensional labeled data structure with columns of potentially different types.
- **Series**: A 1-dimensional labeled array of values.
- **Index**: A way to label and access rows and columns in a DataFrame.

## **2. Data Structures in pandas**

pandas provides two primary data structures: Series and DataFrame.

### Series

A Series is a one-dimensional labeled array of values.

- **Example:** `s = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])`
- **Output:** `a    1
b    2
c    3
d    4
e    5
dtype: int64`

### DataFrame

A DataFrame is a two-dimensional labeled data structure with columns of potentially different types.

- **Example:** `df = pd.DataFrame({'Name': ['John', 'Anna', 'Peter', 'Linda'],
                       'Age': [28, 24, 35, 32],
                       'Country': ['USA', 'UK', 'Australia', 'Germany']},
                      index=['row1', 'row2', 'row3', 'row4'])`
- **Output:** `      Name  Age    Country
row1   John   28        USA
row2   Anna   24         UK
row3  Peter   35  Australia
row4  Linda   32    Germany`

## **3. Indexes in pandas**

Indexes are used to label and access rows and columns in a DataFrame.

- **Types of Indexes:**
  - **Integer Index:** A simple integer index with no labels.
  - **Label Index:** A label-based index with string values.
  - **Categorical Index:** A categorical index with string values and ordinal labels.

## **4. Operations between data structures in pandas**

pandas provides several functions to perform operations between data structures.

- **merge():** Merge two DataFrames based on a common column.
- **join():** Join two DataFrames based on a common index.
- **concat():** Concatenate two DataFrames horizontally or vertically.

## **5. Function Application in pandas**

pandas provides several functions to apply operations to data structures.

- **apply():** Apply a function to each row or column of a DataFrame.
- **map():** Apply a function to each element of a Series or DataFrame.
- **transform():** Apply a function to each element of a Series or DataFrame, returning a new Series or DataFrame.

**Key Concepts:**

- **Lambda functions:** Small, anonymous functions used with apply() and map().
- **NumPy functions:** Built-in functions for numerical operations, such as mean() and std().
