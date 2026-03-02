# **Chapter-2: Understanding Data**

## **2.6: Bivariate Data**

### Definition

Bivariate data refers to data that consists of two variables. Each observation in the dataset is described by the values of these two variables.

### Types of Bivariate Data

- **Discrete Bivariate Data**: Each variable can take on distinct, separate values. Examples include categorical data (e.g., gender, color) and count data (e.g., number of students).
- **Continuous Bivariate Data**: Each variable can take on any value within a given range or interval. Examples include numerical data (e.g., height, weight) and interval data (e.g., IQ scores).

### Types of Relationships Between Variables

- **Positive Correlation**: When one variable increases, the other variable also tends to increase. For example, as income increases, the likelihood of owning a house also tends to increase.
- **Negative Correlation**: When one variable increases, the other variable tends to decrease. For example, as the number of students increases, the average grade point average tends to decrease.
- **No Correlation**: There is no significant relationship between the two variables.

### Measuring Bivariate Relationships

- **Correlation Coefficient**: Measures the strength and direction of the linear relationship between two variables. The most common correlation coefficient is the Pearson correlation coefficient (r).
- **Spearman's Rank Correlation Coefficient**: Measures the rank correlation between two variables. It is used for non-linear relationships or when the data is not normally distributed.

### Example

Suppose we are analyzing the relationship between the number of hours studied and the score on a math test. We collect data on 10 students and calculate the hours studied and test scores for each student.

| Student ID | Hours Studied | Test Score |
| ---------- | ------------- | ---------- |
| 1          | 5             | 80         |
| 2          | 3             | 70         |
| 3          | 7             | 85         |
| 4          | 4             | 75         |
| 5          | 6             | 82         |
| 6          | 2             | 60         |
| 7          | 8             | 88         |
| 8          | 3             | 72         |
| 9          | 5             | 80         |
| 10         | 7             | 85         |

We can calculate the correlation coefficient (r) to measure the strength of the relationship between hours studied and test score.

### Code

```python
import numpy as np

# Define the data
hours_studied = np.array([5, 3, 7, 4, 6, 2, 8, 3, 5, 7])
test_score = np.array([80, 70, 85, 75, 82, 60, 88, 72, 80, 85])

# Calculate the correlation coefficient (r)
r = np.corrcoef(hours_studied, test_score)[0, 1]

print("Correlation Coefficient (r):", r)
```

## **2.7: Multivariate Data**

### Definition

Multivariate data refers to data that consists of more than two variables. Each observation in the dataset is described by the values of these multiple variables.

### Types of Multivariate Data

- **Multivariate Normal Distribution**: A distribution with multiple variables, each with a mean and standard deviation. Examples include stock prices and exchange rates.
- **Multivariate Skewness Distribution**: A distribution with multiple variables, each with a mean, standard deviation, and skewness. Examples include income and education.

### Types of Relationships Between Variables

- **Linear Multivariate Relationship**: The relationship between multiple variables can be modeled as a linear equation.
- **Non-Linear Multivariate Relationship**: The relationship between multiple variables cannot be modeled as a linear equation.
- **Multicollinearity**: When two or more independent variables are highly correlated, making it difficult to estimate the coefficients of the multiple linear regression model.

### Measuring Multivariate Relationships

- **Multivariate Correlation Matrix**: Measures the correlation between multiple variables.
- **Multivariate Regression**: Models the relationship between multiple independent variables and a dependent variable.
- ** Principal Component Analysis (PCA)**: Reduces the dimensionality of multivariate data by identifying the most important features.

### Example

Suppose we are analyzing the relationship between a person's income, education level, and occupation. We collect data on 100 individuals and calculate the income, education level, and occupation for each person.

| Individual ID | Income | Education Level | Occupation  |
| ------------- | ------ | --------------- | ----------- |
| 1             | 50000  | Bachelor's      | Engineer    |
| 2             | 60000  | Master's        | Doctor      |
| 3             | 70000  | Bachelor's      | Lawyer      |
| ...           | ...    | ...             | ...         |
| 100           | 40000  | High School     | Salesperson |

We can calculate the correlation matrix to measure the relationships between income, education level, and occupation.

### Code

```python
import numpy as np
import pandas as pd

# Define the data
data = {
    "Income": [50000, 60000, 70000, ... , 40000],
    "Education Level": ["Bachelor's", "Master's", "Bachelor's", ... , "High School"],
    "Occupation": ["Engineer", "Doctor", "Lawyer", ... , "Salesperson"]
}

df = pd.DataFrame(data)

# Calculate the correlation matrix
corr_matrix = df.corr()

print("Correlation Matrix:")
print(corr_matrix)
```

## **2.8: Essential Concepts**

### Scaling and Normalization

- **Standardization**: Scaling the data to have a mean of 0 and a standard deviation of 1.
- **Normalization**: Scaling the data to be within a specific range (e.g., 0 to 1).

### Feature Selection

- **Unsupervised Feature Selection**: Selecting features based on the data themselves, without any prior knowledge of the target variable.
- **Supervised Feature Selection**: Selecting features based on the target variable, using techniques such as recursive feature elimination (RFE).

### Dimensionality Reduction

- **Principal Component Analysis (PCA)**: Reducing the dimensionality of multivariate data by identifying the most important features.
- **t-Distributed Stochastic Neighbor Embedding (t-SNE)**: Visualizing high-dimensional data in a lower-dimensional space.

### Data Preprocessing

- **Handling Missing Values**: Replacing missing values with mean, median, or imputed values.
- **Handling Outliers**: Removing or transforming outliers using techniques such as winsorization.

### Example

Suppose we are analyzing the relationship between a person's age, height, and weight. We collect data on 100 individuals and calculate the age, height, and weight for each person.

| Individual ID | Age | Height | Weight |
| ------------- | --- | ------ | ------ |
| 1             | 25  | 175    | 65     |
| 2             | 30  | 180    | 70     |
| 3             | 35  | 185    | 75     |
| ...           | ... | ...    | ...    |
| 100           | 40  | 190    | 80     |

We can scale the data to have a mean of 0 and a standard deviation of 1 using standardization.

### Code

```python
import numpy as np
from sklearn.preprocessing import StandardScaler

# Define the data
data = np.array([[25, 175, 65], [30, 180, 70], [35, 185, 75], ... , [40, 190, 80]])

# Create a StandardScaler object
scaler = StandardScaler()

# Fit and transform the data
scaled_data = scaler.fit_transform(data)

print("Scaled Data:")
print(scaled_data)
```
