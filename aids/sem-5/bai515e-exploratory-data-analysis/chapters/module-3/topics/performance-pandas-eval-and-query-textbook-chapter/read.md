# **Performance Pandas: eval and query**

## **Introduction**

In this chapter, we will explore the `eval` and `query` functions in the Performance Pandas tool, which are designed to simplify data analysis and visualization. These functions allow us to evaluate and query large datasets in a efficient and interactive manner.

## **What is eval?**

`eval` is a function in Performance Pandas that allows us to evaluate a string as a Python expression and return the result. It is essentially a powerful string manipulation function that enables us to perform complex calculations and data transformations.

## **Example Use Case:**

```python
import pandas as pd

# Create a sample DataFrame
data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 24, 35, 32]}
df = pd.DataFrame(data)

# Use eval to calculate the average age
result = eval('df["Age"].mean()')
print(result)  # Output: 30.25
```

In this example, we use the `eval` function to calculate the mean of the 'Age' column in the DataFrame. The `eval` function takes the string `'df["Age"].mean()'` as input, which is a Python expression that calculates the mean of the 'Age' column.

## **What is query?**

`query` is a function in Performance Pandas that allows us to filter a DataFrame based on a string query. It is a powerful tool for data filtering and selection.

## **Example Use Case:**

```python
import pandas as pd

# Create a sample DataFrame
data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 24, 35, 32],
        'Country': ['USA', 'UK', 'Australia', 'Germany']}
df = pd.DataFrame(data)

# Use query to filter the DataFrame
result = df.query('Age > 30 and Country == "USA"')
print(result)
```

In this example, we use the `query` function to filter the DataFrame to include only rows where the 'Age' column is greater than 30 and the 'Country' column is equal to 'USA'.

**Key Concepts:**

- `eval` allows us to evaluate a string as a Python expression and return the result.
- `query` allows us to filter a DataFrame based on a string query.
- `eval` and `query` are designed to simplify data analysis and visualization.
- These functions can be used to perform complex calculations and data transformations.

## **Best Practices:**

- Use `eval` and `query` sparingly, as they can be slow and may introduce security risks if not used carefully.
- Always validate and sanitize user input when using `eval`.
- Use `query` with caution, as it can return unexpected results if the query is not properly written.

By mastering the `eval` and `query` functions in Performance Pandas, you can efficiently analyze and visualize large datasets in an interactive and powerful way.
