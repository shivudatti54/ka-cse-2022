# **Basics of R Continued**

**Chapter 2: Matrices and Arrays, Lists, Data Frames, Factors, Strings, Dates and Times**

### 2.3 Matrices

- A matrix is a two-dimensional table of numbers with rows and columns.
- Elements are identified by their row and column index (e.g., `a[1,2]`)
- Matrix operations:
  - Addition: `a + b` (element-wise)
  - Multiplication: `a * b` (element-wise)
  - Transpose: `t(a)` (swap rows and columns)

### 2.4 Arrays

- An array is a matrix with additional dimensions.
- Elements are identified by their row, column, and dimension index (e.g., `a[1,2,3]`)
- Array operations:
  - Addition: `a + b` (element-wise)
  - Multiplication: `a * b` (element-wise)

### 2.5 Lists

- A list is a collection of elements of different data types.
- Elements are identified by their position in the list (e.g., `list[1]`)
- List operations:
  - Indexing: `list[1]`
  - Length: `length(list)`

### 2.6 Data Frames

- A data frame is a table with rows and columns, similar to a spreadsheet.
- Elements are identified by their row and column index (e.g., `df[1,2]`)
- Data frame operations:
  - Selection: `df[1:3, 1:2]`
  - Filtering: `df[df$column == "value"]`

### 2.7 Factors

- A factor is a categorical variable.
- Elements are identified by their position in the factor (e.g., `factor[1]`)
- Factor operations:
  - Levels: `factor$levels`
  - Levels names: `factor$levels <- names(factor)`

### 2.7.2 String Functions

- String functions:
  - `str()`: print the structure of a string
  - `gsub()`: substitute a pattern in a string
  - `regexpr()`: search for a pattern in a string

### 2.8.1 Data Types

- Character: a sequence of characters (e.g., `"hello"`)
- Integer: an integer value (e.g., `1`)
- Float: a floating-point number (e.g., `3.14`)
- Date: a date value (e.g., ` Sys.Date()`)

### 2.8.2 Time Functions

- Date and time functions:
  - `Sys.Date()`: get the current date
  - `Sys.time()`: get the current time
  - `format()`: format a date and time value

Note: This is not an exhaustive list, but rather a concise summary of the key points.
