# Bivariate Data and Multivariate Data

## Overview

Bivariate analysis studies relationships between two variables, while multivariate analysis extends to three or more variables. Understanding these relationships is essential for feature selection, model building, and interpretation in machine learning where most real-world datasets are inherently multivariate.

## Key Points

- **Bivariate Data Types**: Numerical vs Numerical (height/weight), Categorical vs Categorical (gender/preference), Numerical vs Categorical (salary/department)
- **Scatter Plots**: Reveal direction (positive/negative), strength (tight/scattered), form (linear/non-linear), and outliers in numerical-numerical relationships
- **Covariance**: Measures joint variability Cov(X,Y) = Σ[(Xi-X̄)(Yi-Ȳ)]/(n-1); positive (increase together), negative (inverse), zero (no linear relation); scale-dependent limitation
- **Pearson Correlation (r)**: r = Cov(X,Y)/(σx\*σy); standardized to [-1,+1]; +0.7 to +1.0 (strong positive), -1.0 to -0.7 (strong negative); assumes linearity and normality
- **Spearman Rank Correlation**: rs = 1 - 6Σdi²/n(n²-1); used for ordinal data, outliers, or monotonic non-linear relationships
- **Correlation vs Causation**: Association does not imply direct influence; hidden confounders can cause both variables (ice cream sales and drowning both caused by hot weather)

## Important Concepts

- Cross-tabulation with Chi-square test for categorical-categorical relationships
- Heatmaps visualize correlation matrices for many variables showing pairwise correlations at a glance
- Multivariate data challenges: visualization beyond 3D difficult, non-linear complex relationships, curse of dimensionality, invisible pairwise interactions
- Parallel coordinates plot: each variable gets vertical axis, observations as polylines connecting values across axes
- Dimensionality reduction (PCA, t-SNE) projects high-dimensional data to 2D/3D for visualization

## Notes

- Always define both covariance and correlation, explaining why correlation is preferred (scale-free)
- Memorize Pearson correlation formula and interpretation table for r values
- Correlation vs causation with ice cream/drowning example is very common exam question
- Know when to use Spearman vs Pearson: Spearman for ordinal/non-linear, Pearson for continuous/linear
- Practice computing correlation from small datasets - frequently asked
- List 3 visualization techniques each for bivariate (scatter, heatmap, pair plot) and multivariate (parallel coordinates, radar charts, 3D scatter)
