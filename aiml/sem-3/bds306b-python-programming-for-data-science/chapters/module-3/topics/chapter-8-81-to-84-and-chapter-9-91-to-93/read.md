**Chapter 8: Data Manipulation and Analysis**

### 8.1 Data Cleaning and Preprocessing

==========================

Data cleaning and preprocessing is an essential step in data science. It involves identifying and correcting errors, missing values, and inconsistencies in the data.

**Why is data cleaning important?**

- Improves data quality
- Increases accuracy of models
- Enhances overall performance of the analysis

**Techniques for data cleaning:**

- **Handling missing values:**
  - Listwise deletion
  - Pairwise deletion
  - Mean/median imputation
  - Forward/backward fill
- **Data normalization:**
  - Min-max scaling
  - Standardization
- **Data transformation:**
  - Log transformation
  - Square root transformation

**Example Code:**

```python
import pandas as pd
import numpy as np

# Create a sample dataset
data = {'Name': ['John', 'Anna', 'Peter', np.nan],
        'Age': [28, 24, 35, 32],
        'Salary': [50000, 60000, 70000, 80000]}

df = pd.DataFrame(data)

# Handle missing values
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())

print(df)
```

### 8.2 Data Merging and Joining

==========================

Data merging and joining are techniques used to combine data from multiple sources into a single dataset.

**Types of joins:**

- **Inner join:** Returns only the rows that have a match in both tables.
- **Left join:** Returns all the rows from the left table and the matching rows from the right table.
- **Right join:** Returns all the rows from the right table and the matching rows from the left table.
- **Full outer join:** Returns all the rows from both tables.

**Example Code:**

```python
import pandas as pd

# Create two sample datasets
data1 = {'Name': ['John', 'Anna', 'Peter'],
         'Age': [28, 24, 35]}

data2 = {'Name': ['John', 'Anna', 'Linda'],
         'Salary': [50000, 60000, 70000]}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Perform an inner join
df = pd.merge(df1, df2, on='Name', how='inner')

print(df)
```

### 8.3 Data Grouping and Aggregation

==========================

Data grouping and aggregation are techniques used to summarize and analyze data.

**Types of grouping:**

- **Single group:** Groups all the rows into a single group.
- **Multiple groups:** Groups the rows into multiple groups.

**Aggregation functions:**

- **Mean:** Calculates the average value of a column.
- **Median:** Calculates the middle value of a column.
- **Sum:** Calculates the total value of a column.

**Example Code:**

```python
import pandas as pd

# Create a sample dataset
data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 24, 35, 32],
        'City': ['New York', 'Paris', 'Tokyo', 'Beijing']}

df = pd.DataFrame(data)

# Group by city and calculate the mean age
grouped = df.groupby('City')['Age'].mean()

print(grouped)
```

### 8.4 Data Visualization

==========================

Data visualization is the process of creating graphical representations of data.

**Types of visualizations:**

- **Scatter plot:** Displays the relationship between two variables.
- **Bar chart:** Displays the distribution of a variable.
- **Histogram:** Displays the distribution of a variable.

**Example Code:**

```python
import matplotlib.pyplot as plt
import numpy as np

# Create a sample dataset
data = {'Age': [28, 24, 35, 32],
        'Salary': [50000, 60000, 70000, 80000]}

df = pd.DataFrame(data)

# Create a scatter plot
plt.scatter(df['Age'], df['Salary'])
plt.show()
```

# **Chapter 9: Data Analysis**

### 9.1 Descriptive Statistics

==========================

Descriptive statistics are used to summarize and describe the main features of a dataset.

**Types of descriptive statistics:**

- **Mean:** Calculates the average value of a variable.
- **Median:** Calculates the middle value of a variable.
- **Mode:** Calculates the most frequently occurring value of a variable.
- **Standard deviation:** Calculates the spread of a variable.

**Example Code:**

```python
import pandas as pd

# Create a sample dataset
data = {'Age': [28, 24, 35, 32],
        'Salary': [50000, 60000, 70000, 80000]}

df = pd.DataFrame(data)

# Calculate descriptive statistics
print(df.describe())
```

### 9.2 Inferential Statistics

==========================

Inferential statistics are used to make conclusions about a population based on a sample of data.

**Types of inferential statistics:**

- **Hypothesis testing:** Used to test a hypothesis about a population.
- **Confidence intervals:** Used to estimate a population parameter.

**Example Code:**

```python
import scipy.stats as stats

# Create a sample dataset
data = [28, 24, 35, 32]

# Calculate the sample mean and standard deviation
sample_mean = sum(data) / len(data)
sample_std = (sum((x - sample_mean) ** 2 for x in data) / len(data)) ** 0.5

# Calculate the confidence interval
confidence_interval = stats.t.interval(0.95, len(data) - 1, loc=sample_mean, scale=sample_std / (len(data) ** 0.5))

print(confidence_interval)
```

### 9.3 Regression Analysis

==========================

Regression analysis is used to model the relationship between two or more variables.

**Types of regression analysis:**

- **Linear regression:** Used to model a linear relationship between two variables.
- **Multiple regression:** Used to model a non-linear relationship between two or more variables.

**Example Code:**

```python
import statsmodels.api as sm

# Create a sample dataset
data = {'Age': [28, 24, 35, 32],
        'Salary': [50000, 60000, 70000, 80000]}

df = pd.DataFrame(data)

# Create a linear regression model
X = sm.add_constant(df['Age'])
model = sm.OLS(df['Salary'], X).fit()

print(model.summary())
```

I hope this study material helps you to better understand the concepts of Chapter 8 (8.1 to 8.4) and Chapter 9 (9.1 to 9.3) of Python Programming for Data Science.
