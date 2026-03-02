# **Python Programming for Data Science**

## **Module: 6 hours**

## **Topic: Chapter 3 and Chapter 4**

### Introduction

In this module, we will be covering the basics of Python programming for data science. Chapter 3 focuses on data structures and Chapter 4 covers data analysis and visualization.

### Data Structures (Chapter 3)

#### 1. Lists

A list is a collection of items that can be of any data type, including strings, integers, floats, and other lists. Lists are denoted by square brackets `[]` and are ordered.

**Example:**

```python
fruits = ['apple', 'banana', 'orange']
print(fruits[0])  # Output: apple
```

#### 2. Tuples

A tuple is a collection of items that can be of any data type, including strings, integers, floats, and other tuples. Tuples are denoted by parentheses `()` and are ordered.

**Example:**

```python
colors = ('red', 'green', 'blue')
print(colors[0])  # Output: red
```

#### 3. Dictionaries

A dictionary is a collection of key-value pairs. Dictionaries are denoted by curly brackets `{}` and are unordered.

**Example:**

```python
person = {'name': 'John', 'age': 30}
print(person['name'])  # Output: John
```

#### 4. Sets

A set is an unordered collection of unique items. Sets are denoted by the `set()` function and are unordered.

**Example:**

```python
numbers = set([1, 2, 3, 4, 5])
print(numbers)  # Output: {1, 2, 3, 4, 5}
```

### Data Analysis and Visualization (Chapter 4)

#### 1. Importing Libraries

To perform data analysis and visualization, we need to import the necessary libraries. The most commonly used libraries are `pandas` for data manipulation and `matplotlib` and `seaborn` for visualization.

**Example:**

```python
import pandas as pd
import matplotlib.pyplot as plt
```

#### 2. Data Preprocessing

Data preprocessing involves cleaning and transforming the data into a suitable format for analysis. This includes handling missing values, removing duplicates, and encoding categorical variables.

**Example:**

```python
import pandas as pd

# Create a sample dataset
data = {'Name': ['John', 'Mary', 'David'],
        'Age': [25, 31, 42]}
df = pd.DataFrame(data)

# Handle missing values
df.fillna('Unknown', inplace=True)

# Remove duplicates
df.drop_duplicates(inplace=True)
```

#### 3. Data Visualization

Data visualization involves creating plots and charts to visualize the data. The most commonly used plots are bar charts, histograms, and line plots.

**Example:**

```python
import matplotlib.pyplot as plt

# Create a sample dataset
data = {'Fruit': ['Apple', 'Banana', 'Cherry'],
        'Quantity': [10, 20, 30]}
df = pd.DataFrame(data)

# Create a bar chart
plt.bar(df['Fruit'], df['Quantity'])
plt.xlabel('Fruit')
plt.ylabel('Quantity')
plt.title('Fruit Quantity')
plt.show()
```

### Key Concepts

- **Data structures**: Lists, tuples, dictionaries, sets
- **Data analysis**: Data preprocessing, visualization
- **Libraries**: Pandas, Matplotlib, Seaborn

### Practice Exercises

1.  Create a list of your favorite books and print the first book.
2.  Create a dictionary of your favorite foods and print the name of the main course.
3.  Create a set of your favorite colors and print the colors.
4.  Import the necessary libraries and create a sample dataset.
5.  Perform data preprocessing and create a bar chart to visualize the data.
