# **Annexure-II 2 Data Visualization with MatPlotlib**

## **General Matplotlib Tips**

- Matplotlib is a plotting library for creating static, animated, and interactive visualizations in Python.
- Importing library: `import matplotlib.pyplot as plt`
- Creating a figure: `fig = plt.figure()`
- Displaying the figure: `plt.show()`
- Saving the figure: `plt.savefig('filename.png')`
- Displaying multiple plots on the same figure: `plt.plot(x, y1, label='Line 1'); plt.plot(x, y2, label='Line 2')`
- Labeling axes: `plt.xlabel('X-axis'); plt.ylabel('Y-axis')`
- Adding title: `plt.title('Title')`

## **Simple Line Plots**

- Creating a simple line plot: `plt.plot(x, y)`
- Adding markers: `plt.plot(x, y, marker='o')`
- Changing line style: `plt.plot(x, y, linestyle='--')`
- Displaying legend: `plt.legend()`

## **Simple Scatter Plots**

- Creating a simple scatter plot: `plt.scatter(x, y)`
- Changing marker size: `plt.scatter(x, y, s=100)`
- Displaying grid: `plt.grid(True)`

## **Visualization with Seaborn**

- Importing library: `import seaborn as sns`
- Creating a scatter plot: `sns.scatterplot(x, y)`
- Creating a bar plot: `sns.barplot(x, y)`
- Creating a box plot: `sns.boxplot(x, y)`
- Adding colors: `sns.scatterplot(x, y, color='red')`

## **Important Formulas, Definitions, and Theorems**

- **Mean**: The average value of a dataset, calculated as the sum of all values divided by the number of values.
- **Median**: The middle value of a dataset when it is sorted in ascending order.
- **Mode**: The value that appears most frequently in a dataset.
- **Standard Deviation**: A measure of the amount of variation or dispersion in a dataset.
- **Correlation Coefficient**: A measure of the strength and direction of the linear relationship between two variables.
