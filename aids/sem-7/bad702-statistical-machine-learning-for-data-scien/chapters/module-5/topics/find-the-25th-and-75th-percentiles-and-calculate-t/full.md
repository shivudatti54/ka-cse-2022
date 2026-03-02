# Find the 25th and 75th Percentiles and Calculate the Interquartile Range (IQR)

===========================================================

## Introduction

---

In statistics, percentiles are used to divide a dataset into equal-sized groups based on the value of the data points. The 25th percentile, also known as the first quartile (Q1), is the value below which 25% of the data points fall, while the 75th percentile, also known as the third quartile (Q3), is the value below which 75% of the data points fall. The interquartile range (IQR) is the difference between the 75th percentile (Q3) and the 25th percentile (Q1).

## Historical Context

---

The concept of percentiles dates back to the early 20th century, when the German statistician Karl Pearson introduced the idea of dividing a dataset into equal-sized groups based on the value of the data points. The term "percentile" was later coined by the American statistician and educator, William F. Gosset, who used it to describe the value below which 1% of the data points fell. The interquartile range, on the other hand, was introduced by the American statistician and educator, Francis Galton, who used it to describe the difference between the 75th and 25th percentiles.

## Modern Developments

---

In recent years, the use of percentiles and IQR has become increasingly popular in data science and machine learning. This is due to their ability to provide a quick and easy way to summarize and visualize large datasets. Additionally, the use of percentiles and IQR has become more widespread in fields such as finance, economics, and medicine, where they are used to analyze and interpret large datasets.

## What are Percentiles?

---

Percentiles are used to divide a dataset into equal-sized groups based on the value of the data points. The value of each percentile is calculated by finding the value below which a certain percentage of the data points fall. For example, the 25th percentile is the value below which 25% of the data points fall.

There are several types of percentiles, including:

- **First quartile (Q1)**: the 25th percentile
- **Second quartile (Q2)**: the 50th percentile (also known as the median)
- **Third quartile (Q3)**: the 75th percentile
- **Fourth quartile (Q4)**: the 100th percentile

## How to Calculate Percentiles

---

There are several methods for calculating percentiles, including:

- **Insertion sort**: a simple method for sorting a small dataset
- **Quick sort**: a fast method for sorting a large dataset
- **Binary search**: a method for finding the value of a percentile in a sorted dataset

However, for large datasets, it is often more efficient to use a method such as **Rank Correlation Coefficient** or **Percentile Estimation**.

## Interquartile Range (IQR)

---

The interquartile range (IQR) is the difference between the 75th percentile (Q3) and the 25th percentile (Q1). It is a measure of the spread of the middle 50% of the data points.

IQR can be used to:

- **Detect outliers**: values that are more than 1.5 times the IQR away from Q1 or Q3 are considered to be outliers
- **Compare datasets**: IQR can be used to compare the spread of different datasets
- **Identify skewness**: IQR can be used to identify whether a dataset is skewed to the left or right

## Calculating IQR

---

IQR can be calculated using the following formula:

```
IQR = Q3 - Q1
```

Where Q3 is the 75th percentile and Q1 is the 25th percentile.

## Example

---

Suppose we have a dataset of exam scores that are normally distributed with a mean of 80 and a standard deviation of 10. We want to find the 25th and 75th percentiles and calculate the interquartile range (IQR).

First, we need to calculate the z-scores for the 25th and 75th percentiles.

```
z1 = (Q1 - μ) / σ
z2 = (Q3 - μ) / σ
```

Where Q1 and Q3 are the 25th and 75th percentiles, μ is the mean, and σ is the standard deviation.

Next, we can use a z-score table or calculator to find the z-scores.

```
z1 = (-1) / 1.482 = -0.67
z2 = (1) / 1.482 = 0.67
```

Now that we have the z-scores, we can use a standard normal distribution table or calculator to find the percentiles.

```
P(Z < -0.67) = 0.2500
P(Z > 0.67) = 0.7500
```

Therefore, the 25th percentile (Q1) is -1 and the 75th percentile (Q3) is 1.

Finally, we can calculate the IQR.

```
IQR = Q3 - Q1 = 1 - (-1) = 2
```

## Case Study

---

Suppose we are a manager at a company that manufactures products. We have a dataset of production times for a new product that we want to analyze.

The dataset contains the following values:

- 5.2 hours
- 4.8 hours
- 6.1 hours
- 5.5 hours
- 4.9 hours
- 6.3 hours
- 5.8 hours
- 5.1 hours
- 4.7 hours
- 6.9 hours

We want to find the 25th and 75th percentiles and calculate the interquartile range (IQR).

First, we need to sort the dataset in ascending order.

```
4.7 hours
4.8 hours
4.9 hours
5.1 hours
5.2 hours
5.5 hours
5.8 hours
6.1 hours
6.3 hours
6.9 hours
```

Next, we can calculate the z-scores for the 25th and 75th percentiles.

```
z1 = (Q1 - μ) / σ
z2 = (Q3 - μ) / σ
```

Where Q1 and Q3 are the 25th and 75th percentiles, μ is the mean, and σ is the standard deviation.

To calculate the mean and standard deviation, we can use the following formulas:

```
μ = (Σx) / N
σ = √(Σ(x - μ)^2 / (N - 1))
```

Where x is each value in the dataset, N is the number of values in the dataset, and Σ is the sum of the values.

After calculating the mean and standard deviation, we can use a z-score table or calculator to find the z-scores.

```
μ = 5.4 hours
σ = 0.7 hours
z1 = (-1.4) / 1.482 = -0.94
z2 = (1.4) / 1.482 = 0.94
```

Now that we have the z-scores, we can use a standard normal distribution table or calculator to find the percentiles.

```
P(Z < -0.94) = 0.1787
P(Z > 0.94) = 0.3213
```

Therefore, the 25th percentile (Q1) is 5.1 hours and the 75th percentile (Q3) is 6.3 hours.

Finally, we can calculate the IQR.

```
IQR = Q3 - Q1 = 6.3 - 5.1 = 1.2 hours
```

## Applications

---

Percentiles and IQR have many applications in data science and machine learning, including:

- **Data visualization**: percentiles can be used to create visualizations that show the distribution of data points.
- **Outlier detection**: IQR can be used to detect outliers in a dataset.
- **Regression analysis**: percentiles can be used as a dependent variable in regression analysis.
- **Time series analysis**: percentiles can be used to analyze time series data.

## Further Reading

---

- **"The Practice of Statistics"** by David S. Moore, George P. McGraw-Hill, and Ronald P. Wilson
- **"ALLISON Data Analysis Using Regression and Multilevel/Hierarchical Models"** by Thomas M. Allison
- **"R for Data Science"** by Hadley Wickham and Garrett Grolemund
