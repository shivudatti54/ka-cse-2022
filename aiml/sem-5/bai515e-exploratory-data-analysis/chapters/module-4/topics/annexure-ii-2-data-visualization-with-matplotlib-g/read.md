# **Data Visualization with Matplotlib: Annexure-II 2**

## **General Matplotlib Tips**

- Matplotlib is a plotting library for creating static, animated, and interactive visualizations in Python.
- It provides a comprehensive set of tools for creating high-quality 2D and 3D plots.
- Matplotlib is used extensively in various fields, including physics, engineering, and data science.

### Key Concepts

- **Figure**: The top-level container for a plot.
- **Axes**: The container for a subplot.
- **Plot**: The actual graph that is displayed.

### Example Code

```python
import matplotlib.pyplot as plt

# Create a figure and a set of subplots
fig, ax = plt.subplots(2, 2, figsize=(8, 6))

# Create some data
x = range(10)
y = [i**2 for i in x]

# Plot some data on the axes
ax[0, 0].plot(x, y)
ax[0, 1].scatter(x, y)
ax[1, 0].bar(x, y)
ax[1, 1].hist(x, bins=5)

# Show the plot
plt.show()
```

## **Simple Line Plots**

A simple line plot is a type of plot that displays a line connecting a series of data points.

### Key Concepts

- **Line**: The line that connects the data points.
- **Data Points**: The individual points on the line.

### Example Code

```python
import matplotlib.pyplot as plt
import numpy as np

# Create some data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a simple line plot
plt.plot(x, y)

# Add title and labels
plt.title('Simple Line Plot')
plt.xlabel('x')
plt.ylabel('sin(x)')

# Show the plot
plt.show()
```

## **Simple Scatter Plots**

A simple scatter plot is a type of plot that displays a set of data points as individual dots.

### Key Concepts

- **Data Points**: The individual points on the scatter plot.
- **Scatter Plot**: The graph that displays the data points as individual dots.

### Example Code

```python
import matplotlib.pyplot as plt
import numpy as np

# Create some data
x = np.random.rand(100)
y = np.random.rand(100)

# Create a simple scatter plot
plt.scatter(x, y)

# Add title and labels
plt.title('Simple Scatter Plot')
plt.xlabel('x')
plt.ylabel('y')

# Show the plot
plt.show()
```

## **Visualization with Seaborn**

Seaborn is a visualization library based on matplotlib that provides a high-level interface for drawing attractive and informative statistical graphics.

### Key Concepts

- **Seaborn**: A visualization library based on matplotlib.
- **Distribution Plots**: Plots that display the distribution of a dataset.
- **Scatter Plots**: Plots that display the relationship between two variables.

### Example Code

```python
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Create some data
x = np.random.rand(100)
y = np.random.rand(100)

# Create a scatter plot with seaborn
sns.scatterplot(x=x, y=y)

# Add title and labels
plt.title('Scatter Plot with Seaborn')
plt.xlabel('x')
plt.ylabel('y')

# Show the plot
plt.show()
```

### Distribution Plots with Seaborn

Seaborn provides a range of distribution plots, including histograms, density plots, and kernel density estimates.

### Key Concepts

- **Histogram**: A plot that displays the distribution of a dataset.
- **Density Plot**: A plot that displays the density of a dataset.
- **Kernel Density Estimate**: A plot that estimates the density of a dataset.

### Example Code

```python
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Create some data
x = np.random.rand(100)

# Create a histogram with seaborn
sns.histplot(x=x, bins=10)

# Add title and labels
plt.title('Histogram with Seaborn')
plt.xlabel('x')
plt.ylabel('Frequency')

# Show the plot
plt.show()
```

### Kernel Density Estimate with Seaborn

Seaborn provides a kernel density estimate plot that estimates the density of a dataset.

### Key Concepts

- **Kernel Density Estimate**: A plot that estimates the density of a dataset.
- **Kernel Density Estimate Plot**: A plot that displays the kernel density estimate of a dataset.

### Example Code

```python
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Create some data
x = np.random.rand(100)

# Create a kernel density estimate plot with seaborn
sns.kdeplot(x=x)

# Add title and labels
plt.title('Kernel Density Estimate with Seaborn')
plt.xlabel('x')
plt.ylabel('Density')

# Show the plot
plt.show()
```
