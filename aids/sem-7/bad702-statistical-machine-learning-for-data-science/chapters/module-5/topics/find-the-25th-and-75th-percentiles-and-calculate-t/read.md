# Calculating Percentiles and the Interquartile Range (IQR)

**Module 5: Exploratory Data Analysis & Robust Statistics**

## Introduction

In the realm of Statistical Machine Learning and Data Science, raw data is our raw material. Before we can build sophisticated models, we must first understand the underlying distribution of our data. Measures like the mean and standard deviation are useful but can be highly sensitive to extreme values, or **outliers**. This module introduces robust statistical measures—specifically percentiles and the Interquartile Range (IQR)—which are fundamental for describing the spread and center of a dataset and for identifying outliers effectively.

## Core Concepts

### 1. Percentiles

A **percentile** is a measure used in statistics indicating the value below which a given percentage of observations in a group of observations falls. For example, the 25th percentile (also known as the first quartile, Q1) is the value below which 25% of the data can be found. The 75th percentile (or third quartile, Q3) is the value below which 75% of the data lies.

### 2. Quartiles

Quartiles are specific percentiles that divide the data into four equal parts:
*   **First Quartile (Q1):** The 25th percentile.
*   **Second Quartile (Q2):** The 50th percentile, which is also the **median**.
*   **Third Quartile (Q3):** The 75th percentile.

### 3. The Interquartile Range (IQR)

The **Interquartile Range (IQR)** is a measure of statistical dispersion and is calculated as the difference between the third quartile (Q3) and the first quartile (Q1).
\boxed{IQR = Q_3 - Q_1}
The IQR represents the range of the middle 50% of the data. It is a **robust statistic**, meaning it is not skewed by extreme outliers, unlike the range (max - min).

## Calculation Methodology

The process for finding quartiles can vary slightly. A common method for an ordered dataset (ascending order) with `n` values is as follows:

1.  **Find the Median (Q2):** This splits the data into two halves.
    *   If `n` is odd, the median is the middle value.
    *   If `n` is even, the median is the average of the two middle values.

2.  **Find Q1:** The median of the **lower half** of the data (excluding the overall median if `n` is odd).
3.  **Find Q3:** The median of the **upper half** of the data (excluding the overall median if `n` is odd).
4.  **Calculate IQR:** Subtract Q1 from Q3 (`IQR = Q3 - Q1`).

## Example

Let's calculate the quartiles and IQR for the following dataset representing the scores of 15 students on a test:
`Scores: [55, 66, 72, 73, 75, 78, 82, 84, 85, 88, 90, 92, 94, 95, 98]`

**Step 1: Order the Data.** The data is already in ascending order.
**Step 2: Find the Median (Q2).** Since `n=15` (odd), the median is the 8th value.
`Q2 = 84`

**Step 3: Find Q1.** The lower half is the first 7 values: `[55, 66, 72, 73, 75, 78, 82]`. The median of this lower half is the 4th value.
`Q1 = 73`

**Step 4: Find Q3.** The upper half is the last 7 values: `[85, 88, 90, 92, 94, 95, 98]`. The median of this upper half is the 4th value.
`Q3 = 92`

**Step 5: Calculate the IQR.**
`IQR = Q3 - Q1 = 92 - 73 = 19`

This means the middle 50% of the students scored between 73 and 92, with an IQR of 19 points.

## Application in Machine Learning: Outlier Detection

The IQR is crucial for identifying outliers. A common rule of thumb is that any data point that falls more than **1.5 × IQR** above Q3 or below Q1 can be considered an outlier.

*   **Lower Bound:** $Q1 - 1.5 \times IQR$
*   **Upper Bound:** $Q3 + 1.5 \times IQR$

In our example:
*   Lower Bound: $73 - 1.5 \times 19 = 73 - 28.5 = 44.5$
*   Upper Bound: $92 + 1.5 \times 19 = 92 + 28.5 = 120.5$

Since all our data points lie between 44.5 and 120.5, this particular dataset contains **no outliers**.

## Key Points & Summary

| Concept | Description | Importance |
| :--- | :--- | :--- |
| **Percentile** | Value below which a given percentage of data lies. | Describes relative standing of a data point. |
| **Quartiles** | Specific percentiles (Q1=25th, Q2=50th, Q3=75th) that split data into four parts. | Provides a five-number summary (Min, Q1, Med, Q3, Max). |
| **IQR** | $IQR = Q_3 - Q_1$; the range of the middle 50% of the data. | **Robust measure of spread** unaffected by extreme outliers. |
| **Application** | Used to detect outliers ($< Q1 - 1.5IQR$ or $> Q3 + 1.5IQR$). | Critical for data preprocessing and cleaning in ML pipelines. |

**Summary:** Understanding and calculating percentiles, quartiles, and the IQR is a fundamental skill for any data scientist. These robust measures provide a deeper insight into the variability and central tendency of your data than traditional measures, forming an essential part of Exploratory Data Analysis (EDA) and preparing your data for machine learning algorithms.