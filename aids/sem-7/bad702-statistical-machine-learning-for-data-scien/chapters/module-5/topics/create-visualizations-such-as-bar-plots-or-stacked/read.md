# **Create Visualizations: Bar Plots and Stacked Bar Charts**

## **Introduction**

In this section, we will explore the use of visualizations to understand the relationship between satisfaction level and repeat purchases. We will cover the basics of bar plots and stacked bar charts, and provide examples of how to create these visualizations using Python and popular data visualization libraries.

## **Bar Plots**

A bar plot is a type of visualization that displays categorical data as rectangular bars. Each bar represents a category, and the height of the bar represents the value for that category.

**Key Features of Bar Plots:**

- **Categorical Data**: Bar plots are used to display categorical data, such as satisfaction levels or repeat purchase rates.
- **Rectangular Bars**: Each bar in a bar plot represents a category, and the height of the bar represents the value for that category.
- **Comparison**: Bar plots allow for easy comparison between categories.

**Example Code:**

```python
import matplotlib.pyplot as plt
import numpy as np

# Create sample data
satisfaction_levels = [4, 3, 5, 4, 3, 4, 5, 4, 3, 5]
repeat_purchases = [10, 5, 15, 10, 5, 15, 10, 5, 15, 10]

# Create bar plot
plt.bar(range(len(satisfaction_levels)), satisfaction_levels)
plt.bar(range(len(repeat_purchases)), repeat_purchases)

# Add labels and title
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Satisfaction Levels and Repeat Purchases')

# Show plot
plt.show()
```

## **Stacked Bar Charts**

A stacked bar chart is a type of bar plot that displays multiple categories on top of each other. Each category is represented by a different color, and the height of the bar represents the value for that category.

**Key Features of Stacked Bar Charts:**

- **Multiple Categories**: Stacked bar charts display multiple categories, allowing for easy comparison between categories.
- **Color-Coded**: Each category is represented by a different color, making it easy to distinguish between categories.
- **Multi-Level**: Stacked bar charts display multiple levels of data, allowing for easy interpretation of complex data.

**Example Code:**

```python
import matplotlib.pyplot as plt
import numpy as np

# Create sample data
satisfaction_levels = [4, 3, 5, 4, 3, 4, 5, 4, 3, 5]
repeat_purchases = [10, 5, 15, 10, 5, 15, 10, 5, 15, 10]
price_levels = [20, 30, 40, 20, 30, 40, 20, 30, 40, 20]

# Create stacked bar chart
plt.bar(['Satisfaction'], [4], color='blue')
plt.bar(['Repeat Purchase'], [10], color='red', bottom=4)
plt.bar(['Price Level'], [20], color='green', bottom=[4, 10])
plt.bar(['Satisfaction & Repeat Purchase'], [5], color='blue', bottom=[4, 20])
plt.bar(['Satisfaction & Price Level'], [15], color='red', bottom=[4, 20])
plt.bar(['Repeat Purchase & Price Level'], [20], color='green', bottom=[4, 20, 15])

# Add labels and title
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Satisfaction Levels, Repeat Purchases, and Price Levels')

# Show plot
plt.show()
```

## **Interpretation**

To interpret the results of the bar plot or stacked bar chart, consider the following:

- **Trends**: Look for trends in the data, such as an increase or decrease in satisfaction levels or repeat purchases over time.
- **Comparisons**: Compare the values between categories to identify differences or similarities.
- **Interactions**: Consider the interactions between categories, such as the relationship between satisfaction levels and repeat purchases.

By using bar plots and stacked bar charts, you can effectively communicate complex data insights to stakeholders and make data-driven decisions.
