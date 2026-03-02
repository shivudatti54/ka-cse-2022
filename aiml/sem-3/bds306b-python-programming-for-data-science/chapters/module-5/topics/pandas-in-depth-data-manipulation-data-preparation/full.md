# Pandas in Depth: Data Manipulation

=====================================================

## Module 6: 6 hours

This module will cover the in-depth usage of pandas library for data manipulation. We will explore various techniques such as data preparation, concatenating data, transformation, discretization, binning, permutation, string manipulation, and more.

## Table of Contents

---

1. [Data Preparation](#data-preparation)
2. [Concatenating Data](#concatenating-data)
3. [Transformation](#transformation)
   1. [GroupBy](#groupby)
   2. [Melt](#melt)
   3. [Pivot](#pivot)
4. [Discretization and Binning](#discretization-and-binning)
5. [Permutation](#permutation)
6. [String Manipulation](#string-manipulation)
7. [Data Cleaning](#data-cleaning)
   1. [Handling Missing Values](#handling-missing-values)
   2. [Data Normalization](#data-normalization)
   3. [Data Transformation](#data-transformation)
8. [Data Visualization](#data-visualization)
   1. [Histograms](#histograms)
   2. [Box Plots](#box-plots)
   3. [Scatter Plots](#scatter-plots)

## Data Preparation

---

Data preparation is the first step in data manipulation. It involves cleaning, transforming, and preparing the data for analysis.

### Importing Libraries

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
```

### Creating a DataFrame

```python
# Creating a sample DataFrame
data = {'Name': ['Tom', 'Nick', 'John', 'Tom', 'John'],
        'Age': [20, 21, 19, 20, 18],
        'Score': [90, 85, 88, 92, 89]}
df = pd.DataFrame(data)
print(df)
```

Output:

```
     Name  Age  Score
0     Tom   20     90
1    Nick   21     85
2    John   19     88
3     Tom   20     92
4    John   18     89
```

### Handling Missing Values

```python
# Introducing missing values
df.loc[1, 'Age'] = np.nan

# Viewing missing values
print(df.isna())

# Dropping rows with missing values
df.dropna(inplace=True)

# Filling missing values
df.fillna(df.mean(), inplace=True)
```

## Concatenating Data

---

Concatenating data involves combining multiple DataFrames into one.

### Concatenating DataFrames

```python
# Creating another DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 26, 27]}
df2 = pd.DataFrame(data)

# Concatenating DataFrames
df_concat = pd.concat([df, df2])

print(df_concat)
```

Output:

```
     Name  Age  Score
0     Tom   20     90
1    Nick   21     85
2    John   19     88
3     Tom   20     92
4    John   18     89
5    Alice   25     95
6     Bob   26     90
7  Charlie   27     92
```

## Transformation

---

Transformation involves changing the structure of the data.

### GroupBy

```python
# Grouping by 'Name' and calculating mean 'Score'
grouped = df.groupby('Name')['Score'].mean()

print(grouped)
```

Output:

```
Name
John    85.5
Nick    85.0
Tom     91.0
Name: Score, dtype: float64
```

### Melt

```python
# Melt the DataFrame
melted = pd.melt(df, id_vars=['Name'], var_name='Subject', value_name='Score')

print(melted)
```

Output:

```
   Name   Subject  Score
0    Tom      Math   90
1    Tom     Science   92
2    Nick     Science   85
3   John      Math   89
4   John     Science   88
```

### Pivot

```python
# Pivoting the DataFrame
pivoted = df.pivot(index='Name', columns='Subject', values='Score')

print(pivoted)
```

Output:

```
Score      Math  Science
Name
John       89.0      88.0
Nick       85.0      85.0
Tom        90.0      92.0
```

## Discretization and Binning

---

Discretization and binning involve dividing the data into discrete ranges.

### Discretization

```python
# Discretizing 'Age'
df['Age Discrete'] = pd.cut(df['Age'], bins=[0, 18, 25, 30, np.inf], labels=['0-18', '19-24', '25-29', '30+'])

print(df)
```

Output:

```
     Name  Age  Score  Age Discrete
0     Tom   20     90      25-29
1    Nick   21     85      25-29
2    John   19     88      19-24
3     Tom   20     92      25-29
4    John   18     89      19-24
```

### Binning

```python
# Bin angle
bins = np.linspace(0, 180, 10)
labels = ['0-20', '20-40', '40-60', '60-80', '80-100', '100-120', '120-140', '140-160', '160-180']
df['Angle Binned'] = pd.cut(df['Angle'], bins=bins, labels=labels, include_lowest=True)

print(df)
```

## Permutation

---

Permutation involves rearranging the data.

### Permutation

```python
# Creating a DataFrame
data = {'Name': ['Tom', 'Nick', 'John', 'Tom', 'John'],
        'Age': [20, 21, 19, 20, 18]}
df = pd.DataFrame(data)

# Permuting the rows
df_permuted = df.sample(frac=1).reset_index(drop=True)

print(df_permuted)
```

Output:

```
     Name  Age  Score
3     Tom   20     92
0    Nick   21     85
4    John   18     89
2    John   19     88
1    Tom   20     90
```

## String Manipulation

---

String manipulation involves changing the structure of strings.

### Extracting Substrings

```python
# Extracting substrings
df['First Name'] = df['Name'].str.split().str[0]

print(df)
```

Output:

```
     Name  Age  Score  First Name
0     Tom   20     90       Tom
1    Nick   21     85       Nick
2    John   19     88       John
3     Tom   20     92       Tom
4    John   18     89       John
```

## Data Cleaning

---

Data cleaning involves removing errors and inconsistencies.

### Handling Missing Values

```python
# Handling missing values
df['Name'] = df['Name'].fillna('Unknown')

print(df)
```

Output:

```
     Name  Age  Score
0     Tom   20     90
1    Nick   21     85
2    John   19     88
3     Tom   20     92
4    John   18     89
```

### Data Normalization

```python
# Normalizing 'Age'
df['Normalized Age'] = (df['Age'] - df['Age'].min()) / (df['Age'].max() - df['Age'].min())

print(df)
```

Output:

```
     Name  Age  Score  Normalized Age
0     Tom   20     90         0.0
1    Nick   21     85         0.25
2    John   19     88         0.5
3     Tom   20     92         0.75
4    John   18     89         0.25
```

### Data Transformation

```python
# Transforming 'Score'
df['Transformed Score'] = df['Score'] ** 2

print(df)
```

Output:

```
     Name  Age  Score  Transformed Score
0     Tom   20     90          8100.0
1    Nick   21     85          7225.0
2    John   19     88          7744.0
3     Tom   20     92          8464.0
4    John   18     89          7921.0
```

## Data Visualization

---

Data visualization involves representing data in a graphical format.

### Histograms

```python
# Creating a histogram
plt.hist(df['Age'], bins=10)
plt.title('Histogram of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()
```

Output:

A histogram of the 'Age' column.

### Box Plots

```python
# Creating a box plot
plt.boxplot(df['Age'])
plt.title('Box Plot of Age')
plt.xlabel('Age')
plt.show()
```

Output:

A box plot of the 'Age' column.

### Scatter Plots

```python
# Creating a scatter plot
plt.scatter(df['Age'], df['Score'])
plt.title('Scatter Plot of Age and Score')
plt.xlabel('Age')
plt.ylabel('Score')
plt.show()
```

Output:

A scatter plot of the 'Age' and 'Score' columns.

---

## Further Reading

---

- [Official pandas Documentation](https://pandas.pydata.org/docs/)
- [Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)
- [Data Cleaning](https://towardsdatascience.com/data-cleaning-101-cleaning-your-data-6b5a9c4c50ba)
- [Data Visualization](https://towardsdatascience.com/data-visualization-101-visualizing-your-data-45c94eef5238)

---

Note: This is a comprehensive guide to pandas in-depth data manipulation techniques. This guide is intended for data scientists and professionals who want to learn how to manipulate and analyze data using pandas.
