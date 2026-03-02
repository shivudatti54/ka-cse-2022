# Text Book 1: Chapter 7 (7.2 to 7.3) - Python Programming for Data Science

## 7.2 - Introduction to Pandas

### Overview

Pandas is one of the most widely used libraries in Python for data manipulation and analysis. It provides high-performance data structures and functions for efficiently handling structured data, including tabular data such as spreadsheets and SQL tables.

### Historical Context

Pandas was created by Wes McKinney in 2008. Initially, it was called "Data Analysis Library" and was primarily designed for data manipulation and analysis. Over time, it has become one of the most popular libraries in Python, widely used in data science, scientific computing, and other fields.

### Modern Developments

In recent years, Pandas has undergone significant changes and improvements. Some of the notable developments include:

- The introduction of the `DataFrame` data structure, which provides a two-dimensional table of data with columns of potentially different types.
- The addition of new data structures, such as `Series` and `Panel`, which provide more flexibility for handling different types of data.
- The improvement of data manipulation and analysis functions, such as `merge`, `groupby`, and `pivot_table`.

### Key Concepts

- **Series**: A one-dimensional labeled array of values.
- **DataFrame**: A two-dimensional labeled data structure with columns of potentially different types.
- **Panel**: A three-dimensional labeled data structure with a hierarchical structure.

### Example Code

```python
import pandas as pd

# Create a sample DataFrame
data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 24, 35, 32],
        'Country': ['USA', 'UK', 'Australia', 'Germany']}
df = pd.DataFrame(data)

print(df)

# Print the first few rows of the DataFrame
print(df.head())

# Print the column names
print(df.columns)

# Print the data types of each column
print(df.dtypes)
```

### Case Study

Suppose we have a dataset of customer information, including their names, ages, and countries of residence. We want to analyze this data to identify trends and patterns.

```python
import pandas as pd

# Create a sample DataFrame
data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 24, 35, 32],
        'Country': ['USA', 'UK', 'Australia', 'Germany']}
df = pd.DataFrame(data)

# Print the summary statistics of the data
print(df.describe())

# Group the data by country and calculate the mean age
grouped = df.groupby('Country')['Age'].mean()
print(grouped)

# Plot a histogram of the data
import matplotlib.pyplot as plt
plt.hist(df['Age'], bins=10)
plt.show()
```

## 7.3 - Data Import and Export

### Overview

Data import and export are essential steps in the data science workflow. Pandas provides several ways to import and export data from various sources, including CSV, Excel, and SQL databases.

### Key Functions

- **`read_csv()`**: Import data from a CSV file.
- **`read_excel()`**: Import data from an Excel file.
- **`read_sql()`**: Import data from a SQL database.

### Example Code

```python
import pandas as pd

# Import data from a CSV file
data = pd.read_csv('data.csv')
print(data)

# Import data from an Excel file
data = pd.read_excel('data.xlsx')
print(data)

# Import data from a SQL database
import sqlite3
conn = sqlite3.connect('data.db')
data = pd.read_sql_query('SELECT * FROM table', conn)
print(data)
```

### Case Study

Suppose we have a CSV file containing data on the sales of a company. We want to import this data into a Pandas DataFrame and analyze it.

```python
import pandas as pd

# Import the data from the CSV file
data = pd.read_csv('sales.csv')

# Print the summary statistics of the data
print(data.describe())

# Group the data by region and calculate the total sales
grouped = data.groupby('Region')['Sales'].sum()
print(grouped)

# Plot a bar chart of the top 5 regions by sales
import matplotlib.pyplot as plt
plt.bar(grouped.index, grouped.values)
plt.show()
```

### Further Reading

- "Python Data Science Handbook" by Jake VanderPlas
- "Pandas Tutorial" by DataCamp
- "Data Analysis with Pandas" by Wes McKinney (author of Pandas)
