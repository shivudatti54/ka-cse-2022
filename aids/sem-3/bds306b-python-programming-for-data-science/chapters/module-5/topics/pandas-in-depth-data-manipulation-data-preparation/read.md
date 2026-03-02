# **Pandas in Depth: Data Manipulation**

**Module 6: 6 hours**

**Topic: Data Manipulation**

## **Table of Contents**

1. [Data Preparation](#data-preparation)
2. [Concatenating Data](#concatenating-data)
3. [Data Transformation](#data-transformation)
4. [Discretization](#discretization)
5. [Binning](#binning)
6. [Permutation](#permutation)
7. [String Manipulation](#string-manipulation)
8. [Data Analysis and Visualization](#data-analysis-and-visualization)

## **1. Data Preparation**

### Definition

Data preparation is the process of cleaning, transforming, and selecting data to prepare it for analysis.

### Importance

Good data preparation is essential for accurate analysis and modeling.

### Techniques

- **Handling Missing Values**: Replace or impute missing values.
- **Data Cleaning**: Remove duplicates, outliers, and incorrect data.
- **Data Normalization**: Scale data to a common range.
- **Data Transformation**: Convert data types and units.

**Example Code**

```python
import pandas as pd

# Create a sample DataFrame
data = {
    'Name': ['John', 'Mary', None],
    'Age': [25, 31, 42]
}
df = pd.DataFrame(data)

# Handle missing values
df.fillna('Unknown', inplace=True)

# Print the DataFrame
print(df)
```

## **2. Concatenating Data**

### Definition

Concatenating data involves combining multiple DataFrames into a single DataFrame.

### Importance

Concatenating data is useful for combining data from multiple sources.

### Techniques

- **Horizontal Concatenation**: Combine DataFrames using `pd.concat()`.
- **Vertical Concatenation**: Combine DataFrames using `pd.concat()` with `axis=1`.

**Example Code**

```python
import pandas as pd

# Create sample DataFrames
df1 = pd.DataFrame({'Name': ['John', 'Mary'], 'Age': [25, 31]})
df2 = pd.DataFrame({'Name': ['Jane', 'Bob'], 'Age': [27, 35]})

# Concatenate horizontally
df_concat = pd.concat([df1, df2], axis=1)

# Print the concatenated DataFrame
print(df_concat)
```

## **3. Data Transformation**

### Definition

Data transformation involves changing the format of data to make it more suitable for analysis.

### Importance

Data transformation is essential for preparing data for analysis.

### Techniques

- **Scaling**: Scale data using `StandardScaler` or `MinMaxScaler`.
- **Encoding**: Encode categorical variables using `LabelEncoder` or `OneHotEncoder`.
- **Normalization**: Normalize data using `StandardScaler` or `MinMaxScaler`.

**Example Code**

```python
from sklearn.preprocessing import StandardScaler
import pandas as pd

# Create a sample DataFrame
data = {
    'Price': [100, 200, 300],
    'Rating': [4, 3, 5]
}
df = pd.DataFrame(data)

# Scale the data using StandardScaler
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df[['Price']])

# Print the scaled data
print(scaled_data)
```

## **4. Discretization**

### Definition

Discretization involves dividing continuous data into discrete intervals.

### Importance

Discretization is useful for categorical analysis.

### Techniques

- **Binning**: Divide continuous data into bins using `pd.cut()`.
- **Interval Estimation**: Estimate continuous data into intervals using `np.linspace()`.

**Example Code**

```python
import pandas as pd
import numpy as np

# Create a sample DataFrame
data = {
    'Age': [22, 25, 30, 35, 40]
}
df = pd.DataFrame(data)

# Bin the data using pd.cut()
binned_data = pd.cut(df['Age'], bins=[20, 30, 40, 50])

# Print the binned data
print(binned_data)
```

## **5. Binning**

### Definition

Binning involves dividing continuous data into discrete intervals.

### Importance

Binning is useful for categorical analysis.

### Techniques

- **Equal Interval Binning**: Divide continuous data into equal intervals using `np.linspace()`.
- **Quantile Binning**: Divide continuous data into quantiles using `np.percentile()`.

**Example Code**

```python
import pandas as pd
import numpy as np

# Create a sample DataFrame
data = {
    'Score': [20, 25, 30, 35, 40]
}
df = pd.DataFrame(data)

# Bin the data using np.linspace()
binned_data = pd.cut(df['Score'], bins=np.linspace(0, 100, 5))

# Print the binned data
print(binned_data)
```

## **6. Permutation**

### Definition

Permutation involves rearranging the order of data.

### Importance

Permutation is useful for creating permutations of data.

### Techniques

- **Permutation Test**: Create permutations of data using `np.random.permutation()`.
- **Model Evaluation**: Evaluate model performance using permutation.

**Example Code**

```python
import pandas as pd
import numpy as np

# Create a sample DataFrame
data = {
    'Score': [20, 25, 30, 35, 40]
}
df = pd.DataFrame(data)

# Create permutations of the data
permutations = np.random.permutation(df['Score'])

# Print the permutations
print(permutations)
```

## **7. String Manipulation**

### Definition

String manipulation involves changing the format of strings.

### Importance

String manipulation is useful for data preprocessing.

### Techniques

- **String Cleaning**: Remove punctuation and special characters using `re.sub()`.
- **String Encoding**: Encode strings using `LabelEncoder` or `OneHotEncoder`.

**Example Code**

```python
import pandas as pd
import re
import numpy as np

# Create a sample DataFrame
data = {
    'Name': ['John@Doe', 'Mary Smith', 'Bob Johnson']
}
df = pd.DataFrame(data)

# Clean the strings using re.sub()
cleaned_data = df['Name'].apply(lambda x: re.sub(r'[^a-zA-Z0-9\s]', '', x))

# Print the cleaned data
print(cleaned_data)
```

## **8. Data Analysis and Visualization**

### Definition

Data analysis and visualization involve exploring and representing data.

### Importance

Data analysis and visualization are essential for understanding data.

### Techniques

- **Data Exploration**: Explore data using `df.describe()`.
- **Data Visualization**: Visualize data using `matplotlib` or `seaborn`.

**Example Code**

```python
import pandas as pd
import matplotlib.pyplot as plt

# Create a sample DataFrame
data = {
    'Score': [20, 25, 30, 35, 40]
}
df = pd.DataFrame(data)

# Plot a histogram of the data
plt.hist(df['Score'])
plt.show()
```

This study material covers the essential techniques for data manipulation using pandas in Python. It provides a comprehensive overview of data preparation, concatenating, transformation, discretization, binning, permutation, string manipulation, and data analysis and visualization.
