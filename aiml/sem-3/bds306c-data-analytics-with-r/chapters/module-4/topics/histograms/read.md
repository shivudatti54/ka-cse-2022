# Module 4: Data Visualization - Histograms in R

## 1. Introduction

A histogram is one of the most fundamental and powerful tools in exploratory data analysis (EDA). It provides a visual representation of the **distribution** of a continuous numerical variable. For data analysts and engineers, understanding the shape, center, and spread of your data is the first step before applying any complex models. R, with its rich graphical capabilities, offers excellent functions for creating insightful and customizable histograms.

## 2. Core Concepts

### What is a Histogram?

Unlike a bar chart which represents categorical data, a histogram represents **continuous data**. It divides the entire range of values of the variable into a series of intervals (called "bins" or "breaks") and counts how many values fall into each interval.

*   **Bins/Breaks:** The adjacent intervals into which the data is split. The choice of bin width is crucial, as it can change the histogram's appearance and interpretation.
*   **Frequency:** The height of each bar represents the frequency (count) of data points that fall into that bin's range.
*   **Density:** Sometimes, the y-axis is scaled to "density" so that the area of all bars sums to 1. This is useful for overlaying probability distributions.

### Why Use a Histogram?

*   **Understand Distribution:** Quickly see if the data is symmetric, skewed (left or right), bimodal (two peaks), or normal.
*   **Identify Central Tendency and Spread:** Get a visual sense of where the data is centered (mean, median) and how spread out it is (variance, standard deviation).
*   **Spot Outliers:** Identify unusual values that fall far from the main body of the data.
*   **Check Data Quality:** Reveal unexpected gaps or unusual patterns in the data.

## 3. Creating Histograms in R

The primary function for creating base histograms in R is `hist()`.

### Basic Syntax