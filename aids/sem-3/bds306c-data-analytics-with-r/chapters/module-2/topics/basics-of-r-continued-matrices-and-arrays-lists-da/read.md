# **Basics of R Continued**

## **Chapter 2: Data Structures**

### 2.3 Matrices and Arrays

A matrix is a two-dimensional array of numbers, while an array is a one-dimensional array of numbers. In R, matrices and arrays are created using the `matrix()` and `array()` functions respectively.

## **Matrix Creation**

```r
# Create a matrix
matrix_data <- matrix(c(1, 2, 3, 4, 5, 6), nrow = 2, ncol = 3)

# Print the matrix
print(matrix_data)
```

Output:

```r
     [,1] [,2] [,3]
[1,]    1    2    3
[2,]    4    5    6
```

### 2.4 Lists

A list is a collection of objects of different data types. Lists are created using the `list()` function in R.

## **List Creation**

```r
# Create a list
list_data <- list("Name" = "John", Age = 25, City = "New York")

# Print the list
print(list_data)
```

Output:

```r
$name
[1] "John"
$Age
[1] 25
$City
[1] "New York"
```

### 2.5 Data Frames

A data frame is a two-dimensional table of data with rows and columns. Data frames are created using the `data.frame()` function in R.

## **Data Frame Creation**

```r
# Create a data frame
data_frame <- data.frame(Name = c("John", "Jane", "Bob"), Age = c(25, 30, 35))

# Print the data frame
print(data_frame)
```

Output:

```
  Name Age
1 John  25
2 Jane  30
3  Bob  35
```

### 2.6 Factors

A factor is a data type in R that represents categorical data. Factors are created using the `factor()` function in R.

## **Factor Creation**

```r
# Create a factor
factor_data <- factor(c("Male", "Female", "Male"))

# Print the factor
print(factor_data)
```

Output:

```
 [1] Male Female Male
 Levels: Female Male
```

### 2.7.2 Character Strings

A character string is a type of string data in R. Character strings are used to store text data.

## **Character String Operations**

```r
# Create a character string
char_str <- "Hello World"

# Print the character string
print(char_str)
```

Output:

```
[1] "Hello World"
```

### 2.7.2.1 String Manipulation

R provides several functions for string manipulation, including `strsplit()`, `paste()`, and `gsub()`. These functions can be used to split, combine, and replace text data.

```r
# Split a string into individual words
words <- strsplit(char_str, " ")[[1]]

# Print the individual words
print(words)
```

Output:

```
[1] "Hello" "World"
```

### 2.8.1 Dates and Times

R provides several functions for working with dates and times, including `as.Date()` and `as.POSIXct()`. These functions can be used to convert date and time data into R's date and time formats.

```r
# Create a date object
date_obj <- as.Date("2022-01-01")

# Print the date object
print(date_obj)
```

Output:

```
[1] "2022-01-01"
```

### 2.8.2 Date and Time Operations

R provides several functions for performing date and time operations, including `difftime()` and `format()`. These functions can be used to calculate the difference between two dates and times, and to format date and time data into specific formats.

```r
# Calculate the difference between two dates
diff <- difftime(date_obj, as.Date("2022-01-02"))

# Print the difference
print(diff)
```

Output:

```
[1] 1 day
```
