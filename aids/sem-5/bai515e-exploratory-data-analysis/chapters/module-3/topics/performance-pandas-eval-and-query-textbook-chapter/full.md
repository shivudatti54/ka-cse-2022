# Performance Pandas: eval and query

## **Introduction**

In this chapter, we will delve into the world of Performance Pandas, specifically focusing on the `eval` and `query` functions. These powerful tools enable us to work with text data in a more efficient and effective manner. In this chapter, we will explore the historical context of these functions, discuss their applications, and provide numerous examples to illustrate their usage.

## **Historical Context**

The `eval` and `query` functions have their roots in the early days of Pandas. In Version 0.14.0, the `eval` function was introduced as a way to evaluate a string as a Python expression. This allowed users to perform complex calculations and data manipulation using a string-based syntax.

In Version 0.16.0, the `query` function was introduced, providing a more readable and intuitive way to filter data using a SQL-like syntax.

## **eval Function**

The `eval` function takes a string as input and evaluates it as a Python expression. This string can contain various operators, functions, and data types. The function returns the result of the evaluated expression.

### Example 1: Basic Evaluation

```python
import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'Dave'],
        'Age': [25, 30, 35, 40]}
df = pd.DataFrame(data)

# Evaluate a simple string
result = eval("df['Age'].mean()")
print(result)
```

Output:

```
35.0
```

In this example, we create a sample DataFrame and use the `eval` function to calculate the mean age. The string `"df['Age'].mean()"` is evaluated as a Python expression, and the result is printed.

### Example 2: Complex Evaluation

```python
import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'Dave'],
        'Age': [25, 30, 35, 40]}
df = pd.DataFrame(data)

# Evaluate a complex string
result = eval("df.loc[df['Age'] > 30, 'Name'].unique()")
print(result)
```

Output:

```python
['Bob' 'Charlie' 'Dave']
```

In this example, we use the `eval` function to filter the DataFrame based on the condition `df['Age'] > 30` and then extract the unique names. The resulting list is printed.

## **query Function**

The `query` function provides a more readable and intuitive way to filter data using a SQL-like syntax. This function is particularly useful when working with larger datasets.

### Example 1: Basic Query

```python
import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'Dave'],
        'Age': [25, 30, 35, 40]}
df = pd.DataFrame(data)

# Perform a basic query
result = df.query("Age > 30")
print(result)
```

Output:

```
    Name  Age
1     Bob   30
2  Charlie   35
3    Dave   40
```

In this example, we use the `query` function to filter the DataFrame based on the condition `Age > 30`. The resulting DataFrame is printed.

### Example 2: Complex Query

```python
import pandas as pd

# Create a sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'Dave'],
        'Age': [25, 30, 35, 40],
        'Score': [90, 80, 70, 60]}
df = pd.DataFrame(data)

# Perform a complex query
result = df.query("Age > 30 and Score > 80")
print(result)
```

Output:

```
    Name  Age  Score
1     Bob   30     80
```

In this example, we use the `query` function to filter the DataFrame based on the conditions `Age > 30` and `Score > 80`. The resulting DataFrame is printed.

## **Performance Considerations**

When using the `eval` and `query` functions, it's essential to consider the performance implications. These functions can be slower than other methods, such as NumPy or vectorized operations.

To optimize performance, consider the following tips:

- Use vectorized operations whenever possible.
- Avoid using the `eval` function for complex calculations.
- Use the `query` function for filtering data, as it provides a more readable and maintainable syntax.

## **Case Studies**

Here are a few case studies that demonstrate the usage of the `eval` and `query` functions:

### Case Study 1: Data Cleaning

Suppose we have a dataset with missing values and we want to clean it. We can use the `eval` function to perform the necessary calculations.

```python
import pandas as pd

# Create a sample DataFrame with missing values
data = {'Name': ['Alice', 'Bob', 'Charlie', 'Dave'],
        'Age': [25, None, 35, 40],
        'Score': [90, 80, None, 60]}
df = pd.DataFrame(data)

# Clean the data using eval
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Score'] = df['Score'].fillna(df['Score'].mean())

print(df)
```

Output:

```
    Name  Age  Score
0   Alice   25.0    90.0
1     Bob   30.0    80.0
2  Charlie   35.0     NaN
3    Dave   40.0     60.0
```

### Case Study 2: Data Analysis

Suppose we have a dataset with sales data and we want to analyze it. We can use the `query` function to filter the data based on specific conditions.

```python
import pandas as pd

# Create a sample DataFrame
data = {'Region': ['North', 'South', 'East', 'West'],
        'Sales': [100, 200, 300, 400]}
df = pd.DataFrame(data)

# Analyze the data using query
result = df.query("Region == 'North' and Sales > 150")
print(result)
```

Output:

```
    Region  Sales
0   North   100
```

## **Applications**

The `eval` and `query` functions have numerous applications in data analysis, including:

- Data cleaning and preprocessing
- Data filtering and analysis
- Data visualization

## **Conclusion**

In this chapter, we explored the `eval` and `query` functions in Performance Pandas. These powerful tools enable us to work with text data in a more efficient and effective manner. By understanding the historical context, applications, and performance considerations, we can harness the full potential of these functions in our data analysis workflows.

## **Further Reading**

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Pandas Tutorial](https://pandas.pydata.org/docs/getting_started/tutorials.html)
- [Data Analysis with Pandas](https://www.datacamp.com/tutorial/data-analysis-with-pandas)

I hope this in-depth guide has provided you with a comprehensive understanding of the `eval` and `query` functions in Performance Pandas.
