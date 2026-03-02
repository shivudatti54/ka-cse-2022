# Annexure-II 2 Data Visualization with MatPlotlib: General Matplotlib Tips, Simple Line Plots, Simple Scatter Plots, Visualization with Seaborn Textboo

## Introduction

Data visualization is a crucial step in exploratory data analysis (EDA). It allows us to extract insights and patterns from data, making it easier to understand complex relationships and trends. In this annexure, we will delve into the world of data visualization using Matplotlib, a powerful Python library for creating static, animated, and interactive visualizations.

## Historical Context

Matplotlib was first released in 2003 by John D. Hunter. It was initially designed to create high-quality 2D and 3D plots, charts, and graphs. Over the years, Matplotlib has evolved to support various visualization tools and techniques, including line plots, scatter plots, and more.

## General Matplotlib Tips

### 1. Customizing the Appearance

Matplotlib provides various options to customize the appearance of your plots. For example, you can change the line color, marker style, and font size using the following code:

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(x, y, marker='o', linestyle='-', color='red', markersize=10, linewidth=2)
plt.show()
```

In this example, we added a red circle marker, a solid line, and increased the font size.

### 2. Adding Legends and Labels

You can add legends and labels to your plots using the following code:

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [1, 4, 9, 16, 25]
y2 = [2, 5, 8, 11, 14]

plt.plot(x, y1, marker='o', linestyle='-', color='red', markersize=10, linewidth=2)
plt.plot(x, y2, marker='s', linestyle='--', color='blue', markersize=8, linewidth=1)
plt.legend(['Line 1', 'Line 2'])
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
```

In this example, we added a legend with two lines and labels for the x and y axes.

## Simple Line Plots

Line plots are a popular choice for visualizing trends and patterns in data. You can use the following code to create a simple line plot:

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(x, y)
plt.show()
```

This code creates a simple line plot with x values on the x-axis and y values on the y-axis.

## Simple Scatter Plots

Scatter plots are useful for visualizing the relationship between two variables. You can use the following code to create a simple scatter plot:

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.scatter(x, y)
plt.show()
```

This code creates a simple scatter plot with x values on the x-axis and y values on the y-axis.

## Visualization with Seaborn

Seaborn is a visualization library built on top of Matplotlib. It provides a high-level interface for creating attractive and informative statistical graphics. Here's an example of how to use Seaborn to create a scatter plot:

```python
import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset('tips')

sns.scatterplot(x='total_bill', y='tip', data=tips)
plt.show()
```

In this example, we used Seaborn to create a scatter plot of the total bill vs. tip from the tips dataset.

## Case Study: Visualizing COVID-19 Data

Let's use Matplotlib and Seaborn to visualize COVID-19 data. We'll use the pneumonia dataset from Kaggle to demonstrate how to create a line plot and scatter plot.

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
pneumonia = pd.read_csv('pneumonia.csv')

# Create a line plot of the total cases
plt.figure(figsize=(10,6))
sns.lineplot(x=pneumonia['Date'], y=pneumonia['Total Cases'])
plt.title('Total Cases of Pneumonia')
plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.show()

# Create a scatter plot of the total cases vs. total deaths
plt.figure(figsize=(10,6))
sns.scatterplot(x=pneumonia['Total Cases'], y=pneumonia['Total Deaths'])
plt.title('Total Cases vs. Total Deaths of Pneumonia')
plt.xlabel('Total Cases')
plt.ylabel('Total Deaths')
plt.show()
```

In this example, we used Matplotlib and Seaborn to create a line plot and scatter plot of the total cases and total deaths of pneumonia.

## Modern Developments

Matplotlib and Seaborn continue to evolve, with new features and tools being added regularly. Some of the modern developments include:

- **3D plotting**: Matplotlib now supports 3D plotting, allowing you to create complex 3D visualizations.
- **Interactive visualizations**: Matplotlib and Seaborn now support interactive visualizations, allowing you to hover over data points to see additional information.
- **Web-based visualizations**: Matplotlib and Seaborn now support web-based visualizations, allowing you to share your visualizations with others.

## Conclusion

Data visualization is a crucial step in exploratory data analysis (EDA). Matplotlib and Seaborn are powerful libraries for creating high-quality visualizations. By mastering these libraries, you can extract insights and patterns from data, making it easier to understand complex relationships and trends.

## Further Reading

- Matplotlib documentation: <https://matplotlib.org/stable/tutorials/index.html>
- Seaborn documentation: <https://seaborn.pydata.org/tutorial.html>
- Kaggle tutorials: <https://www.kaggle.com/tutorials>
- DataCamp courses: <https://www.datacamp.com/courses>

Note: This annexure provides a comprehensive overview of Matplotlib and Seaborn. For more information, please refer to the documentation and tutorials provided above.
