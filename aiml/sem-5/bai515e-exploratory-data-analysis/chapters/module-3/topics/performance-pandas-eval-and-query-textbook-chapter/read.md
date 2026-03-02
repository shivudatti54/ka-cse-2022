# Performance Pandas: eval and query

## Chapter 22 - Exploratory Data Analysis

### Overview

In this chapter, we will delve into the world of performance pandas and explore the `eval` and `query` functions. These functions enable us to access and manipulate data in a more efficient and flexible manner.

### eval Function

The `eval` function is used to evaluate a string as a Python expression and return the result. This function is useful when we need to perform complex calculations or data manipulation operations.

#### Syntax

```python
pandas.eval(expression, engine='python', engine='numpy', **options)
```

#### Parameters

- `expression`: The string expression to be evaluated.
- `engine`: The engine to be used for evaluation (default is 'python').
- `options`: Additional options for the evaluation process (optional).

#### Example

```python
import pandas as pd

# Create a DataFrame
data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 24, 35, 32]}
df = pd.DataFrame(data)

# Evaluate a string expression using the eval function
result = df['Age'].mean()
print(result)
```

In this example, we create a DataFrame and then use the `eval` function to calculate the mean of the 'Age' column.

```python
# Evaluate a more complex string expression using the eval function
result = df.loc[df['Age'] > 30, 'Name'].value_counts()
print(result)
```

In this example, we use the `eval` function to select rows where the 'Age' column is greater than 30 and then calculate the value count of the 'Name' column.

### query Function

The `query` function is used to query the DataFrame based on a string expression. This function is useful when we need to filter data based on specific conditions.

#### Syntax

```python
df.query(expression)
```

#### Parameters

- `expression`: The string expression to be used for querying the DataFrame.

#### Example

```python
import pandas as pd

# Create a DataFrame
data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 24, 35, 32],
        'Country': ['USA', 'UK', 'Australia', 'Germany']}
df = pd.DataFrame(data)

# Query the DataFrame using the query function
result = df.query('Age > 30 and Country == "USA'")
print(result)
```

In this example, we create a DataFrame and then use the `query` function to select rows where the 'Age' column is greater than 30 and the 'Country' column is equal to 'USA'.

### High-Level Query Language

The `query` function supports a high-level query language that allows us to filter data using a more intuitive syntax.

#### Syntax

```python
df.query('condition1 and condition2')
```

#### Parameters

- `condition1`: The first condition to filter the data.
- `condition2`: The second condition to filter the data.

#### Example

```python
import pandas as pd

# Create a DataFrame
data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 24, 35, 32],
        'Country': ['USA', 'UK', 'Australia', 'Germany']}
df = pd.DataFrame(data)

# Query the DataFrame using the query function
result = df.query('Country == "USA" and Age > 30')
print(result)
```

In this example, we create a DataFrame and then use the `query` function to select rows where the 'Country' column is equal to 'USA' and the 'Age' column is greater than 30.

### Conclusion

In this chapter, we explored the `eval` and `query` functions in pandas. These functions enable us to access and manipulate data in a more efficient and flexible manner. We learned how to use the `eval` function to evaluate string expressions and the `query` function to query the DataFrame based on specific conditions. We also learned how to use the high-level query language to filter data in a more intuitive syntax.
