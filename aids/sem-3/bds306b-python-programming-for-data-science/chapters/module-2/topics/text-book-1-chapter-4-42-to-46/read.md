# **Text Book 1: Chapter 4 (4.2 to 4.6)**

## **4.2: Introduction to Statistical Measures**

### What are Statistical Measures?

Statistical measures are used to summarize and describe the main features of a dataset. These measures provide a way to understand the central tendency, variability, and other characteristics of the data.

### Types of Statistical Measures

- **Mean**: The average value of a dataset.
- **Median**: The middle value of a dataset when it is sorted in ascending or descending order.
- **Mode**: The most frequently occurring value in a dataset.
- **Standard Deviation (SD)**: A measure of the amount of variation or dispersion of a set of values.

### Examples

- A manufacturer produces 10 toy cars with weights of 1.2 kg, 1.5 kg, 1.8 kg, 1.2 kg, 1.5 kg, 1.8 kg, 1.2 kg, 1.5 kg, 1.8 kg, and 1.2 kg. The mean weight is 1.4 kg, the median weight is 1.4 kg, the mode is 1.2 kg, and the standard deviation is 0.2 kg.

### Code

```python
import numpy as np

# Create a dataset
dataset = np.array([1.2, 1.5, 1.8, 1.2, 1.5, 1.8, 1.2, 1.5, 1.8, 1.2])

# Calculate mean
mean = np.mean(dataset)
print("Mean:", mean)

# Calculate median
median = np.median(dataset)
print("Median:", median)

# Calculate mode
from collections import Counter
mode = Counter(dataset).most_common(1)[0][0]
print("Mode:", mode)

# Calculate standard deviation
sd = np.std(dataset)
print("Standard Deviation:", sd)
```

## **4.3: Relating Statistical Measures to Real-World Data**

### Example 1: Exam Scores

| Student | Score |
| ------- | ----- |
| A       | 85    |
| B       | 90    |
| C       | 78    |
| D       | 92    |
| E       | 88    |

- Mean score: 86.4
- Median score: 88
- Mode score: 88
- Standard deviation: 4.3

### Example 2: Sales Data

| Region | Sales |
| ------ | ----- |
| North  | 100   |
| South  | 120   |
| East   | 90    |
| West   | 110   |

- Mean sales: 102.5
- Median sales: 110
- Mode sales: 120
- Standard deviation: 10.5

### Code

```python
import numpy as np

# Create datasets
exam_scores = np.array([85, 90, 78, 92, 88])
sales_data = np.array([100, 120, 90, 110])

# Calculate mean
mean_exam = np.mean(exam_scores)
mean_sales = np.mean(sales_data)
print("Mean Exam Scores:", mean_exam)
print("Mean Sales Data:", mean_sales)

# Calculate median
median_exam = np.median(exam_scores)
median_sales = np.median(sales_data)
print("Median Exam Scores:", median_exam)
print("Median Sales Data:", median_sales)

# Calculate mode
from collections import Counter
mode_exam = Counter(exam_scores).most_common(1)[0][0]
mode_sales = Counter(sales_data).most_common(1)[0][0]
print("Mode Exam Scores:", mode_exam)
print("Mode Sales Data:", mode_sales)

# Calculate standard deviation
sd_exam = np.std(exam_scores)
sd_sales = np.std(sales_data)
print("Standard Deviation Exam Scores:", sd_exam)
print("Standard Deviation Sales Data:", sd_sales)
```

## **4.4: Data Visualization**

### Types of Data Visualization

- **Bar Chart**: A graphical representation of categorical data.
- **Line Chart**: A graphical representation of continuous data.
- **Scatter Plot**: A graphical representation of the relationship between two variables.

### Best Practices

- Use clear and concise labels.
- Use color to differentiate between categories.
- Use size to represent magnitude.

### Code

```python
import matplotlib.pyplot as plt
import numpy as np

# Create datasets
exam_scores = np.array([85, 90, 78, 92, 88])
sales_data = np.array([100, 120, 90, 110])

# Create bar chart
plt.bar(['Exam Scores', 'Sales Data'], [np.mean(exam_scores), np.mean(sales_data)])
plt.xlabel('Category')
plt.ylabel('Value')
plt.title('Bar Chart Example')
plt.show()

# Create line chart
plt.plot(exam_scores, label='Exam Scores')
plt.plot(sales_data, label='Sales Data')
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('Line Chart Example')
plt.legend()
plt.show()

# Create scatter plot
plt.scatter(exam_scores, sales_data)
plt.xlabel('Exam Scores')
plt.ylabel('Sales Data')
plt.title('Scatter Plot Example')
plt.show()
```

## **4.5: Statistical Measures for Continuous Data**

### Types of Statistical Measures

- **Mean**: The average value of a dataset.
- **Median**: The middle value of a dataset when it is sorted in ascending or descending order.
- **Mode**: The most frequently occurring value in a dataset.
- **Standard Deviation (SD)**: A measure of the amount of variation or dispersion of a set of values.
- **Variance**: The average of the squared differences from the mean.

### Examples

- A student's height in cm: 165, 170, 160, 180, 168
- A company's stock prices: 100, 120, 90, 110, 130

### Code

```python
import numpy as np

# Create datasets
heights = np.array([165, 170, 160, 180, 168])
stock_prices = np.array([100, 120, 90, 110, 130])

# Calculate mean
mean_height = np.mean(heights)
mean_stock_price = np.mean(stock_prices)
print("Mean Height:", mean_height)
print("Mean Stock Price:", mean_stock_price)

# Calculate median
median_height = np.median(heights)
median_stock_price = np.median(stock_prices)
print("Median Height:", median_height)
print("Median Stock Price:", median_stock_price)

# Calculate mode
from collections import Counter
mode_height = Counter(heights).most_common(1)[0][0]
mode_stock_price = Counter(stock_prices).most_common(1)[0][0]
print("Mode Height:", mode_height)
print("Mode Stock Price:", mode_stock_price)

# Calculate standard deviation
sd_height = np.std(heights)
sd_stock_price = np.std(stock_prices)
print("Standard Deviation Height:", sd_height)
print("Standard Deviation Stock Price:", sd_stock_price)

# Calculate variance
var_height = np.var(heights)
var_stock_price = np.var(stock_prices)
print("Variance Height:", var_height)
print("Variance Stock Price:", var_stock_price)
```

## **4.6: Statistical Measures for Categorical Data**

### Types of Statistical Measures

- **Mode**: The most frequently occurring value in a dataset.
- **Median**: The middle value of a dataset when it is sorted in ascending or descending order.
- **Standard Deviation (SD)**: A measure of the amount of variation or dispersion of a set of values.

### Examples

- A survey of favorite colors: Red, Blue, Green, Red, Blue, Green
- A survey of favorite foods: Pizza, Burger, Sandwich, Pizza, Burger, Sandwich

### Code

```python
import numpy as np
from collections import Counter

# Create datasets
favorite_colors = np.array(['Red', 'Blue', 'Green', 'Red', 'Blue', 'Green'])
favorite_foods = np.array(['Pizza', 'Burger', 'Sandwich', 'Pizza', 'Burger', 'Sandwich'])

# Calculate mode
mode_favorite_colors = Counter(favorite_colors).most_common(1)[0][0]
mode_favorite_foods = Counter(favorite_foods).most_common(1)[0][0]
print("Mode Favorite Colors:", mode_favorite_colors)
print("Mode Favorite Foods:", mode_favorite_foods)

# Calculate median
median_favorite_colors = np.median(favorite_colors)
median_favorite_foods = np.median(favorite_foods)
print("Median Favorite Colors:", median_favorite_colors)
print("Median Favorite Foods:", median_favorite_foods)

# Calculate standard deviation
sd_favorite_colors = np.std(favorite_colors)
sd_favorite_foods = np.std(favorite_foods)
print("Standard Deviation Favorite Colors:", sd_favorite_colors)
print("Standard Deviation Favorite Foods:", sd_favorite_foods)
```
