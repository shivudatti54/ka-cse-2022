# **Find the 25th and 75th Percentiles and Calculate the Interquartile Range (IQR)**

### What are Percentiles?

---

Percentiles are a measure of central tendency used to divide a dataset into equal parts based on the value of its elements. In a dataset, the 25th percentile, also known as the first quartile (Q1), is the value below which 25% of the data falls. Similarly, the 75th percentile, also known as the third quartile (Q3), is the value below which 75% of the data falls.

### Why Calculate Percentiles?

---

Calculating percentiles is crucial in data analysis as it provides a better understanding of the data's distribution. Percentiles are used in various statistical techniques, including the calculation of the interquartile range (IQR).

### What is the Interquartile Range (IQR)?

---

The interquartile range (IQR) is the difference between the 75th percentile (Q3) and the 25th percentile (Q1) of a dataset. IQR is a measure of the spread or dispersion of the data. It is widely used in statistical analysis and data visualization.

### Calculating Percentiles

---

To calculate the 25th and 75th percentiles, the following steps can be followed:

#### Step 1: Arrange Data in Ascending Order

- Arrange the dataset in ascending order to make it easier to calculate the percentiles.

#### Step 2: Calculate the Position of the Percentile

- Calculate the position of the percentile using the following formula:

Position = (Percentile / 100) \* N

where:

- Position is the position of the percentile
- Percentile is the percentile value (25 or 75)
- N is the total number of data points

#### Step 3: Calculate the Percentile Value

- Calculate the percentile value using the following formula:

Percentile Value = (Position - 1) \* (Maximum Value - Minimum Value) + Minimum Value

where:

- Percentile Value is the calculated percentile value
- Maximum Value is the maximum value in the dataset
- Minimum Value is the minimum value in the dataset

### Example

---

Suppose we have a dataset of exam scores: 80, 70, 90, 85, 95, 75, 90.

#### Step 1: Arrange Data in Ascending Order

The dataset in ascending order is: 70, 75, 80, 85, 90, 90, 95.

#### Step 2: Calculate the Position of the Percentile

- For the 25th percentile (Q1): Position = (25 / 100) \* 7 = 1.75
- For the 75th percentile (Q3): Position = (75 / 100) \* 7 = 5.25

#### Step 3: Calculate the Percentile Value

- For Q1: Percentile Value = (1.75 - 1) \* (95 - 70) + 70 = 82.5
- For Q3: Percentile Value = (5.25 - 1) \* (95 - 70) + 70 = 87.5

Therefore, the 25th percentile (Q1) is 82.5 and the 75th percentile (Q3) is 87.5.

### Calculating IQR

---

The IQR is calculated by subtracting the Q1 value from the Q3 value:

IQR = Q3 - Q1
= 87.5 - 82.5
= 5

### Key Concepts

---

- Percentiles are a measure of central tendency used to divide a dataset into equal parts.
- The 25th percentile (Q1) is the value below which 25% of the data falls, and the 75th percentile (Q3) is the value below which 75% of the data falls.
- The IQR is the difference between the Q3 and Q1 values and is a measure of the spread or dispersion of the data.

### Practice Problems

---

1. Calculate the 50th percentile (median) of the dataset: 10, 20, 30, 40, 50.
2. Calculate the IQR of the dataset: 25, 30, 35, 40, 45.

### Answer Key

---

1. The 50th percentile (median) is 35.
2. The IQR is 10.
