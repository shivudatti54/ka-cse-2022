# **Annexure-II 2 Data Visualization with MatPlotlib: General Matplotlib Tips, Simple Line Plots, Simple Scatter Plots, Visualization with Seaborn**

## **Table of Contents**

1. [Introduction](#introduction)
2. [Historical Context](#historical-context)
3. [General Matplotlib Tips](#general-matplotlib-tips)
4. [Simple Line Plots](#simple-line-plots)
5. [Simple Scatter Plots](#simple-scatter-plots)
6. [Visualization with Seaborn](#visualization-with-seaborn)
7. [Case Studies and Applications](#case-studies-and-applications)
8. [Further Reading](#further-reading)

## **Introduction**

Data visualization is an essential step in the exploratory data analysis (EDA) process. It helps to identify patterns, trends, and correlations in the data, making it easier to understand and communicate insights. In this annexure, we will focus on using Matplotlib, a popular Python library for data visualization, to create simple line plots, scatter plots, and visualize data using Seaborn.

## **Historical Context**

Matplotlib was first released in 2003 by John Hunter, a statistician and data scientist. Since then, it has become one of the most widely used data visualization libraries in Python. Seaborn, on the other hand, was released in 2010 by Wes McKinney, a data scientist and statistician. Seaborn is built on top of Matplotlib and provides a high-level interface for creating attractive and informative statistical graphics.

## **General Matplotlib Tips**

Here are some general tips for using Matplotlib:

### 1. Importing Matplotlib

To use Matplotlib, you need to import it in your Python script or code.

```python
import matplotlib.pyplot as plt
```

### 2. Creating a Figure and Axis

To create a new figure and axis, use:

```python
fig, ax = plt.subplots()
```

### 3. Setting the Title and Labels

To set the title and labels, use:

```python
ax.set_title('Title')
ax.set_xlabel('X-axis label')
ax.set_ylabel('Y-axis label')
```

### 4. Plotting Data

To plot data, use the `plot()` function:

```python
ax.plot(x, y)
```

### 5. Customizing the Plot

To customize the plot, use various options and functions provided by Matplotlib. For example:

```python
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.grid(True)
```

### 6. Saving the Plot

To save the plot, use:

```python
plt.savefig('plot.png')
```

### 7. Displaying the Plot

To display the plot, use:

```python
plt.show()
```

## **Simple Line Plots**

A simple line plot is a basic plot that connects points with a line. Here is an example:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10, 0.1)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title('Simple Line Plot')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
plt.show()
```

This code creates a line plot of the sine function.

## **Simple Scatter Plots**

A simple scatter plot is a plot that displays points as scatter plots. Here is an example:

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(100)
y = np.random.rand(100)

fig, ax = plt.subplots()
ax.scatter(x, y)
ax.set_title('Simple Scatter Plot')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
plt.show()
```

This code creates a scatter plot of random data.

## **Visualization with Seaborn**

Seaborn is a high-level interface for creating attractive and informative statistical graphics. Here is an example of a scatter plot created with Seaborn:

```python
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(100)
y = np.random.rand(100)

sns.scatterplot(x=x, y=y)
plt.title('Scatter Plot with Seaborn')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
```

This code creates a scatter plot of random data using Seaborn.

## **Case Studies and Applications**

Here are some case studies and applications of Matplotlib and Seaborn:

- **Analyzing Stock Prices**: Use Matplotlib to create line plots and scatter plots to analyze stock prices over time.
- **Visualizing Customer Data**: Use Seaborn to create scatter plots and bar charts to visualize customer data, such as demographics and purchase history.
- **Exploring Climate Data**: Use Matplotlib to create line plots and scatter plots to explore climate data, such as temperature and precipitation patterns.

## **Further Reading**

Here are some resources for further learning:

- **Matplotlib Documentation**: [https://matplotlib.org/stable/tutorials/index.html](https://matplotlib.org/stable/tutorials/index.html)
- **Seaborn Documentation**: [https://seaborn.pydata.org/tutorial.html](https://seaborn.pydata.org/tutorial.html)
- **Python Data Analysis**: [https://www.python-data-analysis.org/](https://www.python-data-analysis.org/)
- **Data Visualization with Python**: [https://www.datacamp.com/tutorial/data-visualization-python](https://www.datacamp.com/tutorial/data-visualization-python)
