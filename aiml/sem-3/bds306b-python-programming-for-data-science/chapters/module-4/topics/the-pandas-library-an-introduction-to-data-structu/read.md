# **The pandas Library: An Introduction to Data Structures, Indexes, Operations, and Function Application**

## **1. Introduction to pandas Library**

The pandas Library is a powerful data manipulation and analysis tool for Python. It provides data structures and functions to efficiently handle and process large datasets. pandas is widely used in data science and scientific computing for data cleaning, transformation, and analysis.

**Key Features of pandas Library:**

- Data Structures: Series (1-dimensional labeled array) and DataFrame (2-dimensional labeled data structure with columns of potentially different types)
- Data Manipulation: Filtering, sorting, grouping, merging, reshaping, and pivoting data
- Data Analysis: Statistical functions, data visualization, and data cleaning

## **2. Data Structures in pandas Library**

### 2.1 Series

A Series is a one-dimensional labeled array of values. It is similar to a list, but with additional features such as labeling and indexing.

**Example:**

```python
import pandas as pd

# Create a Series
s = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
print(s)
```

Output:

```
a    1
b    2
c    3
d    4
e    5
dtype: int64
```

### 2.2 DataFrame

A DataFrame is a two-dimensional labeled data structure with columns of potentially different types. It is similar to an Excel spreadsheet or a table in a relational database.

**Example:**

```python
import pandas as pd

# Create a DataFrame
data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 24, 35, 32],
        'Country': ['USA', 'UK', 'Australia', 'Germany']}
df = pd.DataFrame(data)
print(df)
```

Output:

```
     Name  Age    Country
0    John   28        USA
1    Anna   24         UK
2   Peter   35  Australia
3   Linda   32    Germany
```

### 2.3 Indexing and Selecting Data

You can access specific data in a Series or DataFrame using indexing. There are several types of indexing:

- Integer indexing
- Label-based indexing
- Slicing
- Boolean indexing

**Example:**

```python
import pandas as pd

# Create a DataFrame
df = pd.DataFrame({'Name': ['John', 'Anna', 'Peter', 'Linda'],
                   'Age': [28, 24, 35, 32]},
                  index=['a', 'b', 'c', 'd'])

# Integer indexing
print(df[0])  # John
# Label-based indexing
print(df.loc['c'])  # Peter
# Slicing
print(df.loc['a':'c'])  # John: 28, Anna: 24, Peter: 35
# Boolean indexing
print(df[(df['Age'] > 30)])  # Peter: 35, Linda: 32
```

## **3. Data Manipulation and Transformation**

pandas provides various functions to manipulate and transform data. These include:

- Filtering
- Sorting
- Grouping
- Merging
- Reshaping
- Pivoting

**Example:**

```python
import pandas as pd

# Create a DataFrame
df = pd.DataFrame({'Name': ['John', 'Anna', 'Peter', 'Linda'],
                   'Age': [28, 24, 35, 32],
                   'Country': ['USA', 'UK', 'Australia', 'Germany']})

# Filtering
print(df[df['Age'] > 30])  # Peter: 35, Linda: 32
# Sorting
print(df.sort_values('Age'))  # John: 28, Anna: 24, Linda: 32, Peter: 35
# Grouping
print(df.groupby('Country')['Age'].mean())  # USA: 28, UK: 24, Australia: 35, Germany: 32
# Merging
df2 = pd.DataFrame({'Name': ['John', 'Anna', 'Peter', 'Linda'],
                    'Score': [90, 85, 95, 88]})
df = pd.merge(df, df2, on='Name')
print(df)  # John: 28, USA: 90, Anna: 24, UK: 85, Peter: 35, Australia: 95, Linda: 32, Germany: 88
```

## **4. Data Analysis**

pandas provides various functions to analyze data. These include:

- Statistical functions
- Data visualization
- Data cleaning

**Example:**

```python
import pandas as pd
import matplotlib.pyplot as plt

# Create a DataFrame
df = pd.DataFrame({'Name': ['John', 'Anna', 'Peter', 'Linda'],
                   'Age': [28, 24, 35, 32],
                   'Country': ['USA', 'UK', 'Australia', 'Germany']})

# Statistical functions
print(df['Age'].mean())  # 31.25
print(df['Age'].median())  # 33.0
print(df['Age'].std())  # 5.303003546057896
# Data visualization
df['Age'].plot.hist(bins=5)
plt.show()
```

## **5. Function Application**

pandas provides various functions to apply to data. These include:

- Apply() function
- Applymap() function
- Transform() function

**Example:**

```python
import pandas as pd

# Create a DataFrame
df = pd.DataFrame({'Name': ['John', 'Anna', 'Peter', 'Linda'],
                   'Age': [28, 24, 35, 32],
                   'Country': ['USA', 'UK', 'Australia', 'Germany']})

# Apply() function
def greet(name):
    return 'Hello ' + name

df['Greeting'] = df['Name'].apply(greet)
print(df)  # John: 28, USA: Hello John, Anna: 24, UK: Hello Anna, Peter: 35, Australia: Hello Peter, Linda: 32, Germany: Hello Linda
# Applymap() function
df['Age'] = df['Age'].apply(lambda x: x + 10)
print(df)  # John: 38, USA: 38, Anna: 34, UK: 34, Peter: 45, Australia: 45, Linda: 42, Germany: 42
# Transform() function
df['Age'] = df['Age'].transform(lambda x: x + 10)
print(df)  # John: 38, USA: 38, Anna: 34, UK: 34, Peter: 45, Australia: 45, Linda: 42, Germany: 42
```
