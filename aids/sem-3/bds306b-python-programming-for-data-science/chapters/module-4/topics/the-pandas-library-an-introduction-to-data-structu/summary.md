# **The pandas Library: Revision Notes**

## **I. Introduction**

- The pandas library is a powerful data analysis tool in Python.
- It provides data structures and functions to efficiently handle and process data.

## **II. Data Structures**

- **Series**: a one-dimensional labeled array of values.
- **DataFrame**: a two-dimensional labeled data structure with columns of potentially different types.
- **Index**: a label-based data structure for indexing and selecting data.

## **III. Indexing and Selecting Data**

- **Label-based indexing**: using the index to select specific data.
- **Intervals**: selecting data within a specified range (e.g., `df.loc[1:3]`).
- **Booleans**: selecting data using condition-based indexing (e.g., `df[df['column'] > 0]`).

## **IV. Operations between Data Structures**

- **Merge**: combining two DataFrames based on a common column (e.g., `pd.merge(df1, df2, on='column')`).
- **Join**: combining two DataFrames based on a common index (e.g., `df1.join(df2)`).
- **Concatenate**: combining two DataFrames into a single DataFrame (e.g., `pd.concat([df1, df2])`).

## **V. Function Application**

- **Apply**: applying a function to each element in a Series or DataFrame (e.g., `df.apply(func)`).
- **Map**: applying a function to each element in a Series or DataFrame (e.g., `df.map(func)`).

## **VI. Important Formulas and Theorems**

- **Mean**: `μ = (Σx) / n`
- **Standard Deviation**: `σ = √((Σ(x - μ)^2) / (n - 1))`
- **Correlation Coefficient**: `ρ = Cov(X, Y) / (σ_X * σ_Y)`

Note: This summary is a concise revision guide and is not intended to be an exhaustive or comprehensive resource.
