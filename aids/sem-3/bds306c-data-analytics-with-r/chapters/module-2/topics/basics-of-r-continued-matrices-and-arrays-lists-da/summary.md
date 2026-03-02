# **Basics of R Continued: Matrices and Arrays, Lists, Data Frames, Factors, Strings, Dates and Times**

**Chapter 2: 2.3, 2.4, 2.5, 2.6, 2.7, 2.8.1, 2.8.2**

### 2.3: Matrices

- **Definition**: A matrix is a two-dimensional array of numbers.
- **Types of Matrices**:
  - **Square Matrix**: A matrix with the same number of rows and columns.
  - **Rectangular Matrix**: A matrix with a different number of rows and columns.
- **Matrix Operations**:
  - Addition
  - Multiplication (element-wise and matrix multiplication)
  - Transpose
- **Important Formula**:
  - Matrix addition: `A + B = (a11 + b11, a12 + b12, ..., a1n + bn1, a21 + b21, a22 + b22, ..., a2n + bn2, ..., an1 + bn1, an2 + bn2, ..., ann + bnn)`

### 2.4: Lists

- **Definition**: A list is a collection of elements of different data types.
- **Creating Lists**:
  - Using `c()` function (e.g., `c(1, 2, 3)`)
  - Using `list()` function (e.g., `list(1, 2, 3)`)
- **List Operations**:
  - Indexing (e.g., `list[[1]]`)
  - Subsetting (e.g., `list[1:2]`)
  - Length (e.g., `length(list)`)
- **Important Formula**:
  - `list[[i]]` to access the i-th element
  - `list[i:j]` to subset the list

### 2.5: Data Frames

- **Definition**: A data frame is a two-dimensional array of values with row and column names.
- **Creating Data Frames**:
  - Using `data.frame()` function (e.g., `data.frame(name = c("John", "Mary", "David"), age = c(25, 31, 42))`)
  - Using `as.data.frame()` function (e.g., `as.data.frame(matrix(c(1, 2, 3, 4, 5, 6), nrow = 2, dims = c(3, 2)))`)
- **Data Frame Operations**:
  - Selection (e.g., `df$name`)
  - Filtering (e.g., `df[df$name == "John", ]`)
  - Grouping (e.g., `group_by(df, name)`)
- **Important Formula**:
  - `df$name` to select the "name" column
  - `df[df$name == "John", ]` to filter rows where "name" is "John"

### 2.6: Factors

- **Definition**: A factor is a categorical variable with a specific set of levels.
- **Creating Factors**:
  - Using `factor()` function (e.g., `factor(c("Male", "Female", "Male"), levels = c("Male", "Female"))`)
- **Factor Operations**:
  - Level extraction (e.g., `levels(factor(x))`)
  - Level creation (e.g., `factor(c("Male", "Female", "Other"), levels = c("Male", "Female", "Other"))`)
- **Important Formula**:
  - `levels(factor(x))` to extract levels
  - `factor(c("Male", "Female", "Other"), levels = c("Male", "Female", "Other"))` to create a new factor

### 2.7: Strings

- **Definition**: A string is a sequence of characters.
- **String Operations**:
  - Concatenation (e.g., `paste("Hello", "World")`)
  - Substring extraction (e.g., `substr("Hello World", 6, 11)`)
  - String manipulation (e.g., `gsub("World", "Earth", "Hello World")`)
- **Important Formula**:
  - `paste(..., sep = "")` to concatenate strings
  - `substr(x, start, end)` to extract substrings

### 2.8.1: Dates and Times

- **Definition**: A date and time is a specific point in time.
- **Date and Time Operations**:
  - Date and time extraction (e.g., `as.Date("2022-01-01 12:00:00")`)
  - Date and time manipulation (e.g., `as.POSIXct("2022-01-01 12:00:00", tz = "UTC")`)
  - Date and time comparison (e.g., `as.Date("2022-01-01 12:00:00") > as.Date("2021-12-31 12:00:00")`)
- **Important Formula**:
  - `as.Date(x)` to extract dates
  - `as.POSIXct(x, tz = "UTC")` to extract times with time zone information
