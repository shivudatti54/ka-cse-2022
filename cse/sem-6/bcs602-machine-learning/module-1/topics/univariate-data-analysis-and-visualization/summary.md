# Univariate Data Analysis and Visualization

## Overview

Univariate analysis is the simplest form of statistical analysis, focusing on a single variable at a time. It serves as the foundational step in data exploration, helping identify patterns, anomalies, and distributions before building complex ML models.

## Key Points

- **Central Tendency**: Mean (average), Median (middle value), Mode (most frequent) - choose based on data distribution
- **Dispersion Measures**: Range, Variance, Standard Deviation, IQR quantify data spread
- **Distribution Shape**: Skewness measures asymmetry (positive/negative/zero); Kurtosis measures tailedness (leptokurtic/mesokurtic/platykurtic)
- **Numerical Data Analysis**: Use mean/median/mode, variance/SD, histograms, box plots for continuous and discrete data
- **Categorical Data Analysis**: Use mode, frequency tables, bar charts, pie charts for nominal and ordinal data
- **Outlier Detection**: Z-score method (±3 SD), IQR method (Q1-1.5×IQR, Q3+1.5×IQR), visual inspection via box plots
- **Missing Value Treatment**: Deletion (remove records), Imputation (replace with mean/median/mode), Prediction (use ML)

## Important Concepts

- Histograms display distribution of numerical data by grouping into bins
- Box plots show five-number summary: minimum, Q1, median, Q3, maximum
- For skewed data, use median; for normal distributions, use mean
- Univariate analysis crucial for feature understanding, data preprocessing, feature selection, and assumption checking in ML

## Notes

- Remember formulas for mean, median, variance, and standard deviation - frequently tested
- Know which visualizations to use: histograms for numerical data, bar charts for categorical
- Practice calculating measures from small datasets
- Understand outlier detection methods and when to apply them
- Relate concepts to ML: explain how univariate analysis helps in feature engineering
