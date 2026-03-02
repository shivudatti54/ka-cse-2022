# **Python Programming for Data Science**

## **Module 6: Data Manipulation and Analysis**

### Overview

In this module, we will dive into the world of data manipulation and analysis using Python. We will cover the basics of data structures, data cleaning, and data visualization. This is a crucial aspect of data science, as it enables us to extract insights from raw data.

### Chapter 3: Data Structures

#### Introduction

Data structures are the building blocks of any data science project. They determine how data is stored, accessed, and manipulated. In this chapter, we will cover the following data structures:

- Lists
- Tuples
- Dictionaries
- Sets

#### Lists

Lists are ordered collections of items that can be of any data type, including strings, integers, floats, and other lists. Lists are denoted by square brackets `[]`.

```python
# Creating a list
my_list = [1, 2, 3, 4, 5]
print(my_list)

# Accessing elements
print(my_list[0])  # Output: 1
print(my_list[4])  # Output: 5

# Modifying elements
my_list[0] = 10
print(my_list)  # Output: [10, 2, 3, 4, 5]

# Appending elements
my_list.append(6)
print(my_list)  # Output: [10, 2, 3, 4, 5, 6]

# Removing elements
my_list.remove(2)
print(my_list)  # Output: [10, 3, 4, 5, 6]
```

#### Tuples

Tuples are ordered, immutable collections of items. Tuples are denoted by parentheses `()`.

```python
# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)

# Accessing elements
print(my_tuple[0])  # Output: 1
print(my_tuple[4])  # Output: 5

# Trying to modify a tuple will result in an error
try:
    my_tuple[0] = 10
except TypeError:
    print("Tuples are immutable")
```

#### Dictionaries

Dictionaries are unordered collections of key-value pairs. Dictionaries are denoted by curly brackets `{}`.

```python
# Creating a dictionary
my_dict = {"name": "John", "age": 30, "city": "New York"}
print(my_dict)

# Accessing elements
print(my_dict["name"])  # Output: John
print(my_dict["age"])   # Output: 30

# Modifying elements
my_dict["age"] = 31
print(my_dict)  # Output: {"name": "John", "age": 31, "city": "New York"}

# Adding new elements
my_dict["country"] = "USA"
print(my_dict)  # Output: {"name": "John", "age": 31, "city": "New York", "country": "USA"}
```

#### Sets

Sets are unordered collections of unique items. Sets are denoted by the `set()` function or by using the `{}` syntax.

```python
# Creating a set
my_set = set([1, 2, 3, 4, 5])
print(my_set)

# Adding elements
my_set.add(6)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

# Removing elements
my_set.remove(2)
print(my_set)  # Output: {1, 3, 4, 5, 6}

# Trying to add a duplicate element will result in an error
try:
    my_set.add(3)
except KeyError:
    print("Sets only store unique elements")
```

### Chapter 4: Data Cleaning

#### Introduction

Data cleaning is the process of removing errors, inconsistencies, and irrelevant data from a dataset. This is a crucial step in data science, as it enables us to improve the accuracy and reliability of our models.

#### Handling Missing Values

Missing values are values that are not present in a dataset. There are several ways to handle missing values, including:

- **Listwise deletion**: This involves removing entire rows or columns that contain missing values.
- **Pairwise deletion**: This involves removing only the specific rows or columns that contain missing values.
- **Mean/Median Imputation**: This involves replacing missing values with the mean or median of the relevant column.
- **Regression Imputation**: This involves using regression models to predict missing values.

```python
import pandas as pd
import numpy as np

# Creating a sample dataset with missing values
data = {
    "Name": ["John", "Mary", np.nan, "David"],
    "Age": [25, 31, 42, np.nan],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}
df = pd.DataFrame(data)

# Handling missing values using mean imputation
df_imputed = df.fillna(df.mean())
print(df_imputed)

# Handling missing values using regression imputation
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy="median")
df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)
print(df_imputed)
```

#### Handling Outliers

Outliers are values that are significantly different from the rest of the data. There are several ways to handle outliers, including:

- **Winsorization**: This involves replacing a portion of the data with a value closer to the median.
- **Truncation**: This involves removing a portion of the data that is above or below a certain threshold.
- **Regression**: This involves using regression models to predict the outliers.

```python
import numpy as np
import pandas as pd
from scipy import stats

# Creating a sample dataset with outliers
data = {
    "Score": [90, 70, 40, 100, 50, 70, 90]
}
df = pd.DataFrame(data)

# Handling outliers using winsorization
df_winsorized = df.apply(lambda x: x.apply(lambda y: stats.norm.ppf(0.5 + 0.1 * (y - x.mean())) if np.abs(y - x.mean()) > 1.5 * x.std() else y))
print(df_winsorized)

# Handling outliers using truncation
df_truncated = df[df["Score"] >= df["Score"].quantile(0.05)]
print(df_truncated)
```

#### Handling Duplicates

Duplicates are values that are identical in a dataset. There are several ways to handle duplicates, including:

- **Listwise deletion**: This involves removing entire rows that contain duplicates.
- **Pairwise deletion**: This involves removing only the specific rows that contain duplicates.
- **Random sampling**: This involves randomly selecting a subset of the data to replace the duplicates.

```python
import pandas as pd

# Creating a sample dataset with duplicates
data = {
    "Name": ["John", "Mary", "John", "David"],
    "Age": [25, 31, 25, 42]
}
df = pd.DataFrame(data)

# Handling duplicates using listwise deletion
df_deleted = df.drop_duplicates()
print(df_deleted)

# Handling duplicates using pairwise deletion
df_deleted = df.drop_duplicates(subset=["Name"])
print(df_deleted)

# Handling duplicates using random sampling
from random import sample
df_sampled = df.sample(frac=0.5)
print(df_sampled)
```

### Conclusion

In this chapter, we covered the basics of data structures, data cleaning, and data visualization. We learned how to create and manipulate lists, tuples, dictionaries, and sets, and how to handle missing values, outliers, and duplicates. We also learned how to use various methods to clean and preprocess data. In the next chapter, we will dive into the world of data visualization and learn how to create informative and engaging visualizations using Python.
