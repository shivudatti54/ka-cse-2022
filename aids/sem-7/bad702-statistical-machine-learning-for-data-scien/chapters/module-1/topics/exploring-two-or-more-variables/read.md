# **Exploring Two or More Variables**

## **Introduction**

In exploratory data analysis, understanding the relationships between two or more variables is crucial for identifying patterns, correlations, and anomalies in the data. This topic delves into techniques for visualizing and analyzing multiple variables to gain insights into the data.

## **Definitions and Concepts**

- **Multivariate Analysis**: The analysis of two or more variables to understand their relationships and interactions.
- **Bivariate Analysis**: The analysis of two variables to understand their relationship.
- **Multidimensional Space**: A space where each dimension represents a variable.
- **Scatterplot Matrix**: A plot of multiple bivariate relationships between variables.

## **Visualizing Two or More Variables**

Visualizing two or more variables helps in understanding the relationships between them. There are several types of plots that can be used:

### Scatterplots

- **Scatterplot Matrix**: A matrix of scatterplots showing the bivariate relationships between variables.
- **Individual Scatterplot**: A plot showing the relationship between two variables.
- **Scatterplot with Regression Line**: A plot showing the relationship between two variables with a regression line.

### Heatmaps

- **Correlation Heatmap**: A heatmap showing the correlation between variables.
- **Variable Importance Heatmap**: A heatmap showing the importance of each variable in predicting a target variable.

### Box Plots

- **Box Plot**: A plot showing the distribution of a variable and outliers.
- **Multiple Box Plots**: A plot showing the distribution of multiple variables.

### Heatmap

- **Pairwise Heatmap**: A heatmap showing the correlation between pairs of variables.
- **Hierarchical Heatmap**: A heatmap showing the correlation between variables as they are ordered.

**Example**

Suppose we have a dataset of exam scores and hours studied for three students. We can use scatterplots and box plots to visualize the relationships between these variables.

| Student | Exam Score | Hours Studied |
| ------- | ---------- | ------------- |
| A       | 80         | 10            |
| B       | 70         | 12            |
| C       | 90         | 8             |

|               | Exam Score | Hours Studied |
| ------------- | ---------- | ------------- | --- |
| Exam Score    |            |               |
| Hours Studied |            |               |
| Exam Score    | 80         | 10            |     |
| Exam Score    | 70         | 12            |     |
| Exam Score    | 90         | 8             |     |
| Hours Studied | 10         | 80            |     |
| Hours Studied | 12         | 70            |     |
| Hours Studied | 8          | 90            |     |

From the scatterplot and box plot, we can see that there is a positive correlation between hours studied and exam score, and that student C has the highest exam score with the lowest hours studied.

## **Key Concepts**

- **Correlation**: A measure of the strength and direction of the linear relationship between two variables.
- **Variable Importance**: A measure of the importance of each variable in predicting a target variable.
- **Scatterplot Matrix**: A plot of multiple bivariate relationships between variables.
- **Heatmap**: A plot showing the correlation or importance of variables.

## **Code**

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create a sample dataset
data = {
    'Exam Score': [80, 70, 90],
    'Hours Studied': [10, 12, 8],
    'Student': ['A', 'B', 'C']
}

df = pd.DataFrame(data)

# Create a scatterplot matrix
plt.figure(figsize=(10, 8))
sns.pairplot(df)
plt.show()

# Create a heatmap of correlation between variables
corr_matrix = df[['Exam Score', 'Hours Studied']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', square=True)
plt.show()

# Create a box plot of exam scores
plt.figure(figsize=(8, 6))
sns.boxplot(x='Student', y='Exam Score', data=df)
plt.show()

# Create a box plot of hours studied
plt.figure(figsize=(8, 6))
sns.boxplot(x='Student', y='Hours Studied', data=df)
plt.show()
```

This code creates a scatterplot matrix, a heatmap of correlation between variables, and two box plots to visualize the distribution of exam scores and hours studied for each student.
