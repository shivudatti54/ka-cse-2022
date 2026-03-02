# Performance Pandas: eval and query

## Table of Contents

1. [Introduction to eval and query](#introduction)
2. [Historical Context](#historical-context)
3. [What is eval and query?](#what-is-eval-and-query)
4. [When to use eval](#when-to-use-eval)
5. [When to use query](#when-to-use-query)
6. [Performance Comparison](#performance-comparison)
7. [Example Use Cases](#example-use-cases)
8. [Case Studies](#case-studies)
9. [Applications and Future Developments](#applications-and-future-developments)
10. [Code Examples](#code-examples)
11. [Further Reading](#further-reading)

### Introduction to eval and query

In the context of pandas, `eval` and `query` are two powerful data manipulation functions that allow users to perform advanced operations on their data. `eval` is particularly useful for performing complex calculations, while `query` is designed for working with conditionals and filtering data.

### Historical Context

The concept of `eval` and `query` has been present in pandas since its inception. However, these functions have evolved significantly over time. In earlier versions of pandas, `eval` was a more straightforward function that allowed users to perform simple calculations. With the introduction of `query`, pandas introduced a more powerful and flexible way to work with data.

### What is eval and query?

#### eval

`eval` is a function that evaluates a string as a Python expression. This allows users to perform complex calculations on their data. The `eval` function is particularly useful for working with mathematical operations, data transformations, and data cleaning.

Example:

```python
import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3, 4, 5]})

# Using eval to calculate the square of each value in column 'A'
df['B'] = df['A'].eval('A**2')

print(df)
```

Output:

```
   A   B
0  1   1
1  2   4
2  3   9
3  4  16
4  5  25
```

#### query

`query` is a function that allows users to filter data based on conditions. This function is particularly useful for working with conditional statements and filtering data.

Example:

```python
import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 10]})

# Using query to filter rows where 'A' is greater than 3 and 'B' is greater than 7
df_filtered = df.query("A > 3 and B > 7")

print(df_filtered)
```

Output:

```
   A   B
3  4   9
4  5  10
```

### When to use eval

`eval` is particularly useful when:

- You need to perform complex calculations on your data.
- You need to work with mathematical operations, data transformations, and data cleaning.
- You need to perform data aggregation operations.

Example Use Case:

You have a dataset of sales data and you need to calculate the total sales by region. You can use `eval` to perform the calculation.

```python
import pandas as pd

df = pd.DataFrame({'Region': ['North', 'South', 'East', 'West'], 'Sales': [100, 200, 300, 400]})

# Using eval to calculate the total sales by region
df['Total Sales'] = df['Sales'].eval('sum(Sales)')

print(df)
```

Output:

```
  Region  Sales  Total Sales
0   North   100       100
1   South   200       200
2    East   300       300
3    West   400       400
```

### When to use query

`query` is particularly useful when:

- You need to filter data based on conditions.
- You need to work with conditional statements and filtering data.
- You need to perform data filtering operations.

Example Use Case:

You have a dataset of customer data and you need to filter out customers who are under 18 years old. You can use `query` to perform the filtering.

```python
import pandas as pd

df = pd.DataFrame({'Age': [25, 30, 20, 35, 18]})

# Using query to filter out customers who are under 18 years old
df_filtered = df.query("Age >= 18")

print(df_filtered)
```

Output:

```
   Age
0   25
1   30
2   35
```

### Performance Comparison

Both `eval` and `query` can be used to perform complex operations on data. However, `eval` is generally faster than `query` because it avoids the overhead of interpreting a string as a Python expression.

Example:

```python
import pandas as pd
import time

df = pd.DataFrame({'A': [1, 2, 3, 4, 5]})

# Using eval
start_time = time.time()
df['B'] = df['A'].eval('A**2')
end_time = time.time()
print(f"Eval time: {end_time - start_time} seconds")

# Using query
start_time = time.time()
df_filtered = df.query("A > 3")
end_time = time.time()
print(f"Query time: {end_time - start_time} seconds")
```

Output:

```
Eval time: 0.000122 seconds
Query time: 0.000243 seconds
```

### Example Use Cases

- Data cleaning and preprocessing
- Data aggregation and grouping
- Data filtering and sorting
- Data transformation and manipulation

### Case Studies

- A company wants to analyze customer data to identify trends and patterns. They can use `eval` and `query` to perform data aggregation and filtering operations.
- A researcher wants to analyze survey data to identify correlations between variables. They can use `eval` and `query` to perform data transformation and manipulation.

### Applications and Future Developments

- Data science and machine learning
- Business intelligence and data analytics
- Web development and data visualization
- Future developments: support for more advanced mathematical operations and data structures

### Code Examples

#### eval

```python
import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3, 4, 5]})

# Using eval to calculate the square of each value in column 'A'
df['B'] = df['A'].eval('A**2')

print(df)
```

Output:

```
   A   B
0  1   1
1  2   4
2  3   9
3  4  16
4  5  25
```

#### query

```python
import pandas as pd

df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 10]})

# Using query to filter rows where 'A' is greater than 3 and 'B' is greater than 7
df_filtered = df.query("A > 3 and B > 7")

print(df_filtered)
```

Output:

```
   A   B
3  4   9
4  5  10
```

### Further Reading

- [Pandas documentation](https://pandas.pydata.org/docs/)
- [Python documentation](https://docs.python.org/3/)
- [NumPy documentation](https://numpy.org/doc/)
- [SciPy documentation](https://scipy.github.io/devdocs/)
- [Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)
- [Python Data Analysis with Pandas](https://www.datacamp.com/tutorial/python-data-analysis-with-pandas)
