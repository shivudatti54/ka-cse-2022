# **Pandas in Depth: Data Manipulation**

## **I. Data Preparation**

- **Data Cleaning**: Handling missing values, removing duplicates, and data normalization
  - `df.dropna()`, `df.drop_duplicates()`, `df.fillna()`
- **Data Standardization**: Scaling numeric data to a common range
  - `StandardScaler` from `sklearn.preprocessing`

## **II. Concatenating Data**

- **Horizontal Concatenation**: Joining two or more DataFrames side by side
  - `pd.concat([df1, df2], axis=1)`
- **Vertical Concatenation**: Joining two or more DataFrames bottom to top
  - `pd.concat([df1, df2], axis=0)`

## **III. Data Transformation**

- **Discretization**: Converting continuous data into discrete categories
  - `pd.cut()`, `pd.qcut()`
- **Binning**: Dividing continuous data into fixed intervals
  - `pd.qcut()`, `pd.cut()`

## **IV. Data Permutation**

- **Random Permutation**: Shuffling rows of a DataFrame randomly
  - `df.sample(frac=1)`

## **V. String Manipulation**

- **String Splitting**: Splitting strings into lists of substrings
  - `df['column'].str.split()`
- **String Joining**: Joining lists of substrings into a single string
  - `df['column'].str.join()`

## **VI. Data Types**

- **Integer and Float Data Types**: Handling integer and float data
  - `pd.to_numeric()`
- **String Data Type**: Handling string data
  - `pd.to_categorical()`

**Important Formulas and Definitions:**

- **Mean**: Average of a set of numbers
  - `df['column'].mean()`
- **Median**: Middle value of a set of numbers
  - `df['column'].median()`
- **Standard Deviation**: Measure of spread or dispersion of a set of numbers
  - `df['column'].std()`

**Important Theorems:**

- **Central Limit Theorem**: States that the distribution of sample means approaches a normal distribution as the sample size increases
- **Law of Large Numbers**: States that the average of a large number of independent and identically distributed random variables is equal to the population mean.
