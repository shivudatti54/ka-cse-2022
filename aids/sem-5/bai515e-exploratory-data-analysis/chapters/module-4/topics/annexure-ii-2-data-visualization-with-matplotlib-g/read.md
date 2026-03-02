# Annexure-II 2 Data Visualization with MatPlotlib

=============================================

## Introduction

---

Data visualization is a crucial step in exploratory data analysis (EDA). It helps in understanding the distribution of data, identifying patterns, and making informed decisions. In this annexure, we will cover general Matplotlib tips, simple line plots, simple scatter plots, and visualization with Seaborn.

## General Matplotlib Tips

---

### Importing Matplotlib

To start with Matplotlib, you need to import it into your Python script or code. You can do this by using the following command:

```python
import matplotlib.pyplot as plt
```

### Setting Plot Style

Matplotlib has several built-in plot styles that you can use to customize your plots. You can set the plot style using the `style` function:

```python
import matplotlib.pyplot as plt
plt.style.use('ggplot')
```

### Adding Titles and Labels

To add titles and labels to your plots, you can use the `suptitle` and `title` functions:

```python
import matplotlib.pyplot as plt
plt.title('Line Plot Example')
plt.suptitle('Line Plot Example')
```

### Saving Plots

To save your plots, you can use the `savefig` function:

```python
import matplotlib.pyplot as plt
plt.savefig('line_plot.png')
```

## Simple Line Plots

---

A line plot is a type of plot that displays a line connecting a set of data points. Here's an example of a simple line plot:

```python
import matplotlib.pyplot as plt
import numpy as np

# Create data points
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create the plot
plt.plot(x, y)

# Add title and labels
plt.title('Line Plot Example')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# Show the plot
plt.show()
```

### Customizing Line Plots

You can customize your line plots by adding different colors, line styles, and markers. Here are some examples:

```python
import matplotlib.pyplot as plt
import numpy as np

# Create data points
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create the plot
plt.plot(x, y1, label='Sine', color='blue', linestyle='--', marker='o')
plt.plot(x, y2, label='Cosine', color='red', linestyle='-', marker='s')

# Add title and labels
plt.title('Line Plot Example')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.legend()

# Show the plot
plt.show()
```

## Simple Scatter Plots

---

A scatter plot is a type of plot that displays a set of data points as dots on a grid. Here's an example of a simple scatter plot:

```python
import matplotlib.pyplot as plt
import numpy as np

# Create data points
x = np.random.rand(100)
y = np.random.rand(100)

# Create the plot
plt.scatter(x, y)

# Add title and labels
plt.title('Scatter Plot Example')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# Show the plot
plt.show()
```

### Customizing Scatter Plots

You can customize your scatter plots by adding different colors and sizes. Here are some examples:

```python
import matplotlib.pyplot as plt
import numpy as np

# Create data points
x = np.random.rand(100)
y = np.random.rand(100)

# Create the plot
plt.scatter(x, y, c=np.random.rand(100), s=np.random.rand(100))

# Add title and labels
plt.title('Scatter Plot Example')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# Show the plot
plt.show()
```

## Visualization with Seaborn

---

Seaborn is a visualization library built on top of Matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics. Here's an example of a simple scatter plot using Seaborn:

```python
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Create data points
x = np.random.rand(100)
y = np.random.rand(100)

# Create the plot
sns.scatterplot(x=x, y=y)

# Add title and labels
plt.title('Scatter Plot Example')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# Show the plot
plt.show()
```

### Customizing Seaborn Plots

You can customize your Seaborn plots by adding different colors, sizes, and styles. Here are some examples:

```python
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Create data points
x = np.random.rand(100)
y = np.random.rand(100)

# Create the plot
sns.scatterplot(x=x, y=y, color='blue', size=100, style='s')

# Add title and labels
plt.title('Scatter Plot Example')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# Show the plot
plt.show()
```

## Conclusion

---

In this annexure, we covered general Matplotlib tips, simple line plots, simple scatter plots, and visualization with Seaborn. We also discussed how to customize your plots by adding different colors, sizes, and styles. By mastering these skills, you can create informative and attractive statistical graphics that help you communicate your findings effectively.
