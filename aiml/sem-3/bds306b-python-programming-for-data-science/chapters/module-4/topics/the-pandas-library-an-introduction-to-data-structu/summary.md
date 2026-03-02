# **The pandas Library: Revision Notes**

## **Introduction to Data Structure**

- **Series**: 1-dimensional labeled array of values, similar to a column in a spreadsheet.
  - `Series(data, index, name)`: Create a pandas Series.
  - `df['column_name']`: Access a column of a DataFrame.
- **DataFrame**: 2-dimensional labeled data structure with columns of potentially different types.
  - `DataFrame(data, index, columns, dtype=None)`: Create a pandas DataFrame.

## **Other Functionalities on Indexes**

- **Indexing**: Access specific rows and columns using labels.
  - `df.loc[row_index, column_name]`: Access a value at a specific row and column.
  - `df.iloc[row_offset, column_offset]`: Access a value at a specific row and column offset.
- **Reshaping**: Modify the shape of a DataFrame using `melt` and `pivot`.
- **GroupBy**: Group a DataFrame by one or more columns and perform aggregation operations.
  - `df.groupby(by)`: Group a DataFrame by one or more columns.

## **Operations between Data Structures**

- **Merging and Joining**: Combine DataFrames based on common columns.
  - `df1.merge(df2, on='column_name')`: Merge two DataFrames based on a common column.
- **Pivot Table**: Create a pivot table to summarize data.
  - `pd.pivot_table(df, values='column_name', index='column_name', aggfunc='mean')`: Create a pivot table.

## **Function Application**

- **Map Function**: Apply a function to each element of a Series.
  - `df['column_name'].map(function)`: Apply a function to each element of a Series.
- **Apply Function**: Apply a function to each row of a DataFrame.
  - `df.apply(function)`: Apply a function to each row of a DataFrame.

## **Important Formulas, Definitions, Theorems**

- **Mean, Median, Mode**: Basic statistics.
  - `mean = sum(x)` / `n`
  - `median = median(x)`
  - `mode = argmax(x)`
- **Correlation Coefficient**: Measure of correlation between two variables.
  - `corr(x, y) = cov(x, y) / (std(x) * std(y))`

## **Quick Revision Tips**

- Practice indexing and selecting data.
- Familiarize yourself with common DataFrames operations.
- Review statistics and data visualization concepts.
