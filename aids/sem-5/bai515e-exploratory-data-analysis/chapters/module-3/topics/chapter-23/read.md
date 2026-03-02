# **Chapter 23: Exploratory Data Analysis**

## **Introduction**

Exploratory Data Analysis (EDA) is the process of summarizing and visualizing the main features of a dataset in order to understand its distribution, relationships, and patterns. In this chapter, we will focus on using the Pandas library to manipulate and analyze data.

## **Vectorized String Operations**

Pandas provides a variety of vectorized string operations that allow us to perform operations on strings in a efficient and scalable way.

### String Methods

- **str.startswith()**: Checks if a string starts with a specified substring.
- **str.endswith()**: Checks if a string ends with a specified substring.
- **str.isupper()**: Checks if all characters in a string are uppercase.
- **str.islower()**: Checks if all characters in a string are lowercase.
- **str.strip()**: Removes leading and trailing whitespace from a string.
- **str.split()**: Splits a string into a list of substrings based on a specified separator.

### Example

```python
import pandas as pd

# Create a sample DataFrame
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, 35, 32]
}
df = pd.DataFrame(data)

# Use vectorized string operations
df['Name'] = df['Name'].str.upper()
print(df)

# Output:
#     Name  Age
# 0    JOHN   28
# 1    ANNA   24
# 2   PETER   35
# 3   LINDA   32
```

## **Working with Time Series Data**

Pandas provides a variety of functions and methods for working with time series data.

### Time Series Index

- **pd.DatetimeIndex**: A DatetimeIndex object represents a sequence of dates and times.
- **pd PeriodIndex**: A PeriodIndex object represents a sequence of periods.

### Time Series Resampling

- **resample()**: Resamples a time series to a specified frequency.
- **asfreq()**: Returns a new time series with the same values, but at a specified frequency.

### Rolling and Expanding Operations

- **roll()**: Applies a function over a window of rows.
- **expanding()**: Applies a function over a window of rows, but also includes the current row.

### Example

```python
import pandas as pd
import numpy as np

# Create a sample time series
data = pd.DataFrame({'Value': np.random.randn(10)})
data.index = pd.date_range('2022-01-01', periods=10, freq='D')

# Work with time series data
print(data.resample('M').mean())

# Output:
#            Value
# Month      0.032662
# 2022-01    0.032662
# 2022-02    0.032662
# 2022-03    0.032662
# 2022-04    0.032662
# 2022-05    0.032662
# 2022-06    0.032662
# 2022-07    0.032662
# 2022-08    0.032662
# 2022-09    0.032662
```

## **High-Performance Data Manipulation**

Pandas provides a variety of high-performance functions and methods for manipulating data.

### Chunking Data

- **read_csv()**: Reads a CSV file in chunks.
- **read_excel()**: Reads an Excel file in chunks.
- **to_csv()**: Writes a DataFrame to a CSV file in chunks.

### Example

```python
import pandas as pd

# Create a large DataFrame
data = {'A': range(1000000)}
df = pd.DataFrame(data)

# Use chunking to read the DataFrame in chunks
chunk_size = 100000
chunks = []
for i in range(0, len(df), chunk_size):
    chunks.append(df.iloc[i:i+chunk_size])

# Write the chunked DataFrame to a CSV file
for chunk in chunks:
    chunk.to_csv('chunk_' + str(i//chunk_size) + '.csv', index=False)
```

This code reads a large DataFrame in chunks, and writes each chunk to a separate CSV file.
