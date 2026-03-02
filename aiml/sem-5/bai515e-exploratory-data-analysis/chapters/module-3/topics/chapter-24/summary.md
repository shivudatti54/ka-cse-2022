# Chapter 24: Exploratory Data Analysis

### Key Points

- **Vectorized String Operations**
  - String manipulation using pandas Series and string methods
  - Examples: `str.upper()`, `str.lower()`, `str.split()`, `str.find()`
  - Use cases: data preprocessing, text analysis
- **Working with Time Series**
  - Introduction to time series data
  - Types of time series: discrete, continuous
  - Common time series metrics: mean, median, standard deviation
  - Plotting time series data using `matplotlib`
- **High-Frequency Data (HFDS)**
  - Definition: financial data with very high frequency (e.g. intraday, intrahour)
  - Challenges: storage, processing, analysis
  - Applications: algorithmic trading, risk management
- **Time Series Decomposition**
  - Definition: separating time series into trend, seasonal, and residual components
  - Methods: STL decomposition, season-trend decomposition
  - Use cases: identifying seasonality, trend, and residual patterns

### Important Formulas and Definitions

- **Mean**: $\bar{x} = \frac{\sum x_i}{n}$
- **Median**: $m = \frac{\sum x_i}{n}$
- **Standard Deviation**: $\sigma = \sqrt{\frac{\sum (x_i - \bar{x})^2}{n}}$
- **Time Series Decomposition**: $TS = T_{trend} + T_{seasonal} + T_{residual}$

### Theorems and Concepts

- **No Free Lunch Theorem**: no algorithm can achieve optimal performance on all tasks and data
- **Kolmogorov-Smirnov Test**: testing for normality and homoscedasticity in time series data

Note: This summary is a concise revision guide and is not intended to be a comprehensive overview of the topic.
