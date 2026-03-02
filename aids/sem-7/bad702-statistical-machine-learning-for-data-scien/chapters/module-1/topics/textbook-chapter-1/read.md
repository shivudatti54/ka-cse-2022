# Statistical Machine Learning for Data Science

## Exploratory Data Analysis: Estimates of Locations and Variability

### Chapter 1: Introduction to Statistical Machine Learning

Statistical machine learning is a subfield of machine learning that focuses on statistical theory and methods for making predictions and decisions. It involves using statistical techniques to extract insights and knowledge from data.

### Estimating Locations

Estimating locations refers to estimating the central tendency of a dataset, which can be a single value (e.g., mean) or a range of values (e.g., median, interquartile range).

#### Mean

The mean is the most commonly used measure of central tendency. It is calculated by summing up all the values in the dataset and dividing by the number of observations.

- **Formula:** `mean = (sum of all values) / number of observations`
- **Example:** Suppose we have a dataset of exam scores with a mean of 80.
- **Interpretation:** The mean score is 80, which means that if we were to take the same exam again, we could expect to score an average of 80.

#### Median

The median is the middle value of a dataset when it is sorted in ascending order. If there is an even number of observations, the median is the average of the two middle values.

- **Formula:** `median = (middle value 1 + middle value 2) / 2`
- **Example:** Suppose we have a dataset of exam scores with a median of 75.
- **Interpretation:** The median score is 75, which means that half of the students scored above 75 and half scored below.

#### Mode

The mode is the most frequently occurring value in a dataset.

- **Formula:** `mode = most frequent value`
- **Example:** Suppose we have a dataset of favorite colors with a mode of blue.
- **Interpretation:** The most common color is blue.

### Estimating Variability

Estimating variability refers to estimating the spread or dispersion of a dataset.

#### Range

The range is the difference between the largest and smallest values in a dataset.

- **Formula:** `range = largest value - smallest value`
- **Example:** Suppose we have a dataset of exam scores with a range of 30.
- **Interpretation:** The scores vary by 30 points.

#### Interquartile Range (IQR)

The IQR is the difference between the 75th percentile (Q3) and the 25th percentile (Q1).

- **Formula:** `IQR = Q3 - Q1`
- **Example:** Suppose we have a dataset of exam scores with an IQR of 15.
- **Interpretation:** The middle 50% of the scores vary by 15 points.

#### Standard Deviation (SD)

The SD is a measure of the amount of variation or dispersion in a dataset.

- **Formula:** `SD = sqrt(sum of (each value - mean)^2 / number of observations)`
- **Example:** Suppose we have a dataset of exam scores with a SD of 10.
- **Interpretation:** The scores vary by 10 points on average.

### Exploring Data Distributions

Exploring data distributions involves understanding the shape and characteristics of a dataset.

#### Visualizations

Visualizations such as histograms, box plots, and density plots can help us understand the distribution of a dataset.

- **Example:** Suppose we have a dataset of exam scores. A histogram would show the distribution of scores, while a box plot would show the median, quartiles, and outliers.
- **Interpretation:** The histogram shows that the scores are skewed to the right, while the box plot shows that the median is 80 and the top 25% of scores are above 90.

#### Quantiles

Quantiles are measures of the distribution of a dataset, such as the first quartile (Q1), second quartile (Q2), and third quartile (Q3).

- **Formula:** `Q1 = (3/4) * (sum of all values)`, `Q2 = (1/2) * (sum of all values)`, `Q3 = (1/4) * (sum of all values)`
- **Example:** Suppose we have a dataset of exam scores with Q1 = 70, Q2 = 80, and Q3 = 90.
- **Interpretation:** The first 25% of scores are below 70, the middle 50% of scores are between 70 and 90, and the top 25% of scores are above 90.

### Exploring Binary Data

Exploring binary data involves understanding the distribution and characteristics of binary variables.

#### Frequency Tables

Frequency tables are used to count the number of observations in each category.

- **Example:** Suppose we have a dataset of binary variables (e.g., 0/1, yes/no, male/female).
- **Formula:** `frequency table = count of observations in each category`
- **Interpretation:** The frequency table shows the number of observations in each category.

#### Proportions

Proportions are used to express the relative frequency of each category.

- **Formula:** `proportion = count of observations in each category / total observations`
- **Example:** Suppose we have a dataset of binary variables with 10 observations in the "yes" category and 20 observations in the "no" category.
- **Interpretation:** The proportion of observations in the "yes" category is 0.5, while the proportion in the "no" category is 0.5.

#### Correlation Coefficient

The correlation coefficient is a measure of the strength and direction of the linear relationship between two continuous variables.

- **Formula:** `correlation coefficient = (sum of (x - mean_x) * (y - mean_y)) / sqrt(sum of (x - mean_x)^2 * sum of (y - mean_y)^2)`
- **Example:** Suppose we have a dataset of exam scores and hours studied with a correlation coefficient of 0.8.
- **Interpretation:** The scores and hours studied are strongly positively correlated, meaning that as hours studied increase, scores also tend to increase.
