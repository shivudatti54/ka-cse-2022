# Chapter 23: Exploratory Data Analysis

======================================================

## Table of Contents

---

1. [Introduction](#introduction)
2. [Importing Libraries and Loading Data](#importing-libraries-and-loading-data)
3. [Exploratory Data Analysis](#exploratory-data-analysis)
   - [Data Preprocessing](#data-preprocessing)
   - [Summary Statistics](#summary-statistics)
   - [Data Visualization](#data-visualization)
4. [Working with Time Series Data](#working-with-time-series-data)
   - [Time Series Decomposition](#time-series-decomposition)
   - [Trend Removal](#trend-removal)
   - [Seasonal Decomposition](#seasonal-decomposition)
5. [High-Performance Data Manipulation](#high-performance-data-manipulation)
   - [Vectorized String Operations](#vectorized-string-operations)
   - [Handling Missing Data](#handling-missing-data)
6. [Advanced Techniques](#advanced-techniques)
   - [Data Imputation](#data-imputation)
   - [Feature Engineering](#feature-engineering)
7. [Case Study: Exploring a Real-World Dataset](#case-study-exploring-a-real-world-dataset)
8. [Conclusion](#conclusion)

## Introduction

---

Exploratory data analysis (EDA) is a crucial step in the data science workflow. It involves using various statistical and visualization techniques to gain insights into the characteristics of the data, identify patterns and correlations, and prepare the data for modeling. In this chapter, we will delve into the world of EDA, covering topics such as data preprocessing, summary statistics, data visualization, time series analysis, and high-performance data manipulation.

## Importing Libraries and Loading Data

---

Before we begin, let's import the necessary libraries and load a sample dataset.

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller
```

Let's load the `tips` dataset from the `seaborn` library.

```python
tips = sns.load_dataset('tips')
```

## Exploratory Data Analysis

---

### Data Preprocessing

Data preprocessing involves cleaning and preparing the data for analysis. This may include handling missing values, removing duplicates, and encoding categorical variables.

```python
# Handle missing values
tips.fillna(tips.mean(), inplace=True)

# Remove duplicates
tips.drop_duplicates(inplace=True)

# Encode categorical variables
tips['sex'] = tips['sex'].map({'Male': 0, 'Female': 1})
```

### Summary Statistics

Summary statistics provide a quick overview of the data's distribution and central tendency.

```python
# Calculate summary statistics
print(tips.describe())
```

### Data Visualization

Data visualization is an essential step in EDA, as it allows us to visualize the data's distribution and patterns.

```python
# Create a histogram of the total bill
plt.hist(tips['total_bill'], bins=20)
plt.title('Histogram of Total Bill')
plt.show()

# Create a scatter plot of total bill vs. tip
plt.scatter(tips['total_bill'], tips['tip'])
plt.title('Scatter Plot of Total Bill vs. Tip')
plt.show()
```

## Working with Time Series Data

---

Time series data is a sequence of data points recorded at regular time intervals. EDA for time series data involves decomposing the data into its trend, seasonality, and residuals.

### Time Series Decomposition

Time series decomposition involves breaking down the data into its trend, seasonality, and residuals.

```python
# Perform time series decomposition
decomposition = seasonal_decompose(tips['total_bill'], model='additive')
trend = decomposition.trend
seasonal = decomposition.seasonal
residual = decomposition.resid

# Plot the decomposition
plt.plot(tips['total_bill'], label='Original')
plt.plot(trend, label='Trend')
plt.plot(seasonal, label='Seasonal')
plt.plot(residual, label='Residual')
plt.legend()
plt.show()
```

### Trend Removal

Trend removal involves removing the trend from the data.

```python
# Remove the trend
trend_removed = decomposition.trend.argsort()[-10:]
trend_removed = trend.remove(trend_removed)

# Plot the trend-removed data
plt.plot(tips['total_bill'], label='Original')
plt.plot(trend_removed, label='Trend-Removed')
plt.legend()
plt.show()
```

### Seasonal Decomposition

Seasonal decomposition involves breaking down the data into its seasonality and residuals.

```python
# Perform seasonal decomposition
seasonal_decomposition = seasonal_decompose(tips['total_bill'], model='multiplicative')
seasonal = seasonal_decomposition.seasonal

# Plot the seasonal decomposition
plt.plot(tips['total_bill'], label='Original')
plt.plot(seasonal, label='Seasonal')
plt.legend()
plt.show()
```

## High-Performance Data Manipulation

---

High-performance data manipulation involves using vectorized operations to perform data manipulation tasks.

### Vectorized String Operations

Vectorized string operations involve using NumPy's vectorized operations to perform string manipulation tasks.

```python
# Convert the 'sex' column to uppercase
tips['sex'] = tips['sex'].apply(lambda x: x.upper())

# Split the 'day' column into 'day' and 'month'
tips['day'] = tips['day'].apply(lambda x: x.split('-'))

# Create a new column 'day_of_week'
tips['day_of_week'] = tips['day'].apply(lambda x: x[0])

# Print the resulting DataFrame
print(tips)
```

### Handling Missing Data

Handling missing data involves using specialized techniques to impute or remove missing values.

```python
# Impute missing values using mean
tips['total_bill'].fillna(tips['total_bill'].mean(), inplace=True)

# Remove rows with missing values
tips.dropna(inplace=True)

# Print the resulting DataFrame
print(tips)
```

## Advanced Techniques

---

### Data Imputation

Data imputation involves using statistical techniques to impute missing values.

```python
# Impute missing values using mean
tips['total_bill'].fillna(tips['total_bill'].mean(), inplace=True)

# Impute missing values using median
tips['tip'].fillna(tips['tip'].median(), inplace=True)

# Print the resulting DataFrame
print(tips)
```

### Feature Engineering

Feature engineering involves creating new features from existing ones.

```python
# Create a new feature 'day_of_week'
tips['day_of_week'] = tips['day'].apply(lambda x: x[0])

# Create a new feature 'month'
tips['month'] = tips['day'].apply(lambda x: x[1])

# Print the resulting DataFrame
print(tips)
```

## Case Study: Exploring a Real-World Dataset

---

Let's explore the `airbnb` dataset, which contains information about Airbnb listings.

```python
# Import the necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Airbnb dataset
airbnb = sns.load_dataset('airbnb')

# Print the first few rows of the dataset
print(airbnb.head())

# Calculate summary statistics
print(airbnb.describe())

# Create a histogram of the price
plt.hist(airbnb['price'], bins=20)
plt.title('Histogram of Price')
plt.show()

# Create a scatter plot of price vs. reviews
plt.scatter(airbnb['price'], airbnb['reviews'])
plt.title('Scatter Plot of Price vs. Reviews')
plt.show()
```

## Conclusion

---

In this chapter, we explored the world of exploratory data analysis (EDA), covering topics such as data preprocessing, summary statistics, data visualization, time series analysis, and high-performance data manipulation. We also examined advanced techniques such as data imputation and feature engineering. We applied these techniques to a real-world dataset, the `airbnb` dataset, to gain insights into its characteristics and patterns. By mastering EDA techniques, you can gain a deeper understanding of your data and make informed decisions.

## Further Reading

---

- [Data Analysis with Python](https://www.datacamp.com/tutorial/data-analysis-with-python)
- [Exploratory Data Analysis with Pandas](https://www.datacamp.com/tutorial/exploratory-data-analysis-with-pandas)
- [Time Series Analysis with Python](https://www.datacamp.com/tutorial/time-series-analysis-with-python)
- [High-Performance Data Manipulation with Pandas](https://www.datacamp.com/tutorial/high-performance-data-manipulation-with-pandas)
- [Data Imputation and Feature Engineering](https://www.datacamp.com/tutorial/data-imputation-and-feature-engineering)
