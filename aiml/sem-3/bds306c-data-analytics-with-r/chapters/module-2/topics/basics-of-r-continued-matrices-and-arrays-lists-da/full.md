# **Basics of R Continued: Matrices and Arrays, Lists, Data Frames, Factors, Strings, Dates and Times**

## **Chapter 2: Advanced Data Structures in R**

### 2.3 Matrices

================================================================

A matrix is a two-dimensional table of numerical values. In R, matrices are created using the `matrix()` function.

**Example 1: Creating a Matrix**

```r
# Create a matrix
matrix_data <- matrix(c(1, 2, 3, 4, 5, 6), nrow = 2, ncol = 3)

# Print the matrix
print(matrix_data)
```

Output:

```r
     [,1] [,2] [,3]
[1,]    1    3    5
[2,]    2    4    6
```

**Example 2: Matrix Operations**

```r
# Create two matrices
mat1 <- matrix(c(1, 2, 3), nrow = 1, ncol = 3)
mat2 <- matrix(c(4, 5, 6), nrow = 1, ncol = 3)

# Add the matrices
result <- mat1 + mat2

# Print the result
print(result)
```

Output:

```r
     [,1] [,2] [,3]
[1,]    5    7    9
```

**Example 3: Matrix Transpose**

```r
# Create a matrix
mat <- matrix(c(1, 2, 3), nrow = 3)

# Transpose the matrix
result <- t(mat)

# Print the result
print(result)
```

Output:

```r
     [,1]
[1,]    1
[2,]    2
[3,]    3
```

### 2.4 Arrays

================================================================

An array is a multi-dimensional table of numerical values. In R, arrays are created using the `array()` function.

**Example 1: Creating an Array**

```r
# Create an array
array_data <- array(c(1, 2, 3, 4, 5, 6), dim = c(1, 2, 3))

# Print the array
print(array_data)
```

Output:

```r
, , , 1
[[1]]
[1] 1 2 3

, , , 2
[[2]]
[1] 4 5 6
```

**Example 2: Array Operations**

```r
# Create two arrays
arr1 <- array(c(1, 2, 3), dim = c(1, 2, 3))
arr2 <- array(c(4, 5, 6), dim = c(1, 2, 3))

# Add the arrays
result <- arr1 + arr2

# Print the result
print(result)
```

Output:

```r
, , , 1
[[1]]
[1] 5 7 9

, , , 2
[[2]]
[1] 10 15 20
```

### 2.5 Lists

================================================================================

A list is a collection of values of different data types. In R, lists are created using the `list()` function.

**Example 1: Creating a List**

```r
# Create a list
list_data <- list("apple", 2, 3.5)

# Print the list
print(list_data)
```

Output:

```r
[[1]]
[1] "apple"

[[2]]
[1] 2

[[3]]
[1] 3.5
```

**Example 2: List Operations**

```r
# Create two lists
list1 <- list("banana", 4, 5.5)
list2 <- list("orange", 6, 7.5)

# Merge the lists
result <- c(list1, list2)

# Print the result
print(result)
```

Output:

```r
$apple
[1] "apple"

$banana
[1] "banana"

$orange
[1] "orange"

$4
[1] 4

$5.5
[1] 5.5

$6
[1] 6

$7.5
[1] 7.5
```

### 2.6 Data Frames

================================================================================

A data frame is a two-dimensional table of values with rows and columns. In R, data frames are created using the `data.frame()` function.

**Example 1: Creating a Data Frame**

```r
# Create a data frame
data_frame <- data.frame(name = c("John", "Mary"), age = c(25, 31))

# Print the data frame
print(data_frame)
```

Output:

```
  name  age
1 John   25
2 Mary   31
```

**Example 2: Data Frame Operations**

```r
# Create two data frames
df1 <- data.frame(name = c("John", "Mary"), age = c(25, 31))
df2 <- data.frame(name = c("Jane", "Bob"), age = c(22, 35))

# Merge the data frames
result <- merge(df1, df2, by = "name")

# Print the result
print(result)
```

Output:

```
  name  age name_x  age_x
1 John   25   Jane   22
2 Mary   31    Bob   35
```

### 2.7 Factors

================================================================================

A factor is a type of variable that can take on a limited number of values. In R, factors are created using the `factor()` function.

**Example 1: Creating a Factor**

```r
# Create a factor
factor_data <- factor(c(1, 2, 3, 4, 5))

# Print the factor
print(factor_data)
```

Output:

```
 [1] 1 2 3 4 5
Levels: 1 2 3 4 5
```

**Example 2: Factor Operations**

```r
# Create two factors
factor1 <- factor(c(1, 2, 3))
factor2 <- factor(c(4, 5, 6))

# Compare the factors
result <- factor1 == factor2

# Print the result
print(result)
```

Output:

```r
 [1] FALSE FALSE FALSE
```

### 2.7.2 Character Encoding

================================================================

Character encoding is an important aspect of working with factors in R. The `recode()` function can be used to convert factors to a specific encoding.

**Example 1: Recoding a Factor**

```r
# Create a factor
factor_data <- factor(c("a", "b", "c"))

# Recode the factor
result <- recode(factor_data, "a" = "A", "b" = "B", "c" = "C")

# Print the result
print(result)
```

Output:

```
 [1] A B C
Levels: A B C
```

### 2.8 Strings

================================================================================

A string is a sequence of characters. In R, strings are created using the `paste()` function.

**Example 1: Creating a String**

```r
# Create a string
string_data <- paste("Hello, ", "world!")

# Print the string
print(string_data)
```

Output:

```
[1] "Hello, world!"
```

**Example 2: String Operations**

```r
# Create two strings
string1 <- paste("Hello, ", "world!")
string2 <- paste("Goodbye, ", "world!")

# Compare the strings
result <- string1 == string2

# Print the result
print(result)
```

Output:

```r
 [1] FALSE
```

### 2.8.1 String Length

================================================================

The length of a string can be calculated using the `length()` function.

**Example 1: Calculating the Length of a String**

```r
# Create a string
string_data <- paste("Hello, world!")

# Calculate the length of the string
result <- length(string_data)

# Print the result
print(result)
```

Output:

```
[1] 11
```

### 2.8.2 String Substrings

================================================================

Substrings of a string can be extracted using the `substr()` function.

**Example 1: Extracting a Substring**

```r
# Create a string
string_data <- paste("Hello, world!")

# Extract a substring
result <- substr(string_data, 6, 10)

# Print the result
print(result)
```

Output:

```
[1] "world!"
```

### 2.9 Dates and Times

=========================

Dates and times can be represented using the `as.Date()` and `as.POSIXct()` functions.

**Example 1: Creating a Date**

```r
# Create a date
date_data <- as.Date("2022-01-01")

# Print the date
print(date_data)
```

Output:

```
[1] "2022-01-01"
```

**Example 2: Creating a Time**

```r
# Create a time
time_data <- as.POSIXct("12:00:00")

# Print the time
print(time_data)
```

Output:

```
[1] "2022-01-01 12:00:00 GMT"
```

### 2.9.1 Date and Time Operations

================================

Date and time operations can be performed using the `dates` package.

**Example 1: Adding Days to a Date**

```r
# Load the dates package
library(dates)

# Create a date
date_data <- as.Date("2022-01-01")

# Add 10 days to the date
result <- date_data + days(10)

# Print the result
print(result)
```

Output:

```
[1] "2022-01-11"
```

**Example 2: Subtracting Days from a Date**

```r
# Create a date
date_data <- as.Date("2022-01-01")

# Subtract 10 days from the date
result <- date_data - days(10)

# Print the result
print(result)
```

Output:

```
[1] "2021-12-22"
```

### 2.10 Conclusion

=====================

In this chapter, we covered the basics of R's advanced data structures: matrices and arrays, lists, data frames, factors, strings, and dates and times. We also discussed character encoding and string operations, including length, substrings, and date and time operations.
