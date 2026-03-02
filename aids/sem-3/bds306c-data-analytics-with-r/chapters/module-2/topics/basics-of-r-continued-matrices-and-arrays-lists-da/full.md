# **Basics of R Continued: Matrices and Arrays, Lists, Data Frames, Factors, Strings, Dates and Times**

## **Chapter 2: Advanced Data Structures in R**

### 2.3 Matrices in R

---

In R, a matrix is a two-dimensional array of numbers. Matrices are used to represent data that has a fixed number of rows and columns, and are often used in linear algebra and statistical modeling.

#### Creating Matrices

---

Matrices can be created using the `matrix()` function in R. Here is an example of how to create a matrix:

```r
# Create a matrix
matrix_data <- matrix(c(1, 2, 3, 4, 5, 6, 7, 8, 9), nrow = 3, ncol = 3)
matrix_data
```

Output:

```r
     [,1] [,2] [,3]
[1,]    1    2    3
[2,]    4    5    6
[3,]    7    8    9
```

#### Matrix Operations

---

Matrices support various operations such as addition, subtraction, multiplication, and transposition. Here are some examples of matrix operations:

```r
# Create two matrices
matrix_data1 <- matrix(c(1, 2, 3, 4, 5, 6, 7, 8, 9), nrow = 3, ncol = 3)
matrix_data2 <- matrix(c(4, 5, 6, 7, 8, 9, 1, 2, 3), nrow = 3, ncol = 3)

# Addition
matrix_data1 + matrix_data2
```

Output:

```r
     [,1] [,2] [,3]
[1,]    5    7    9
[2,]    9   10   12
[3,.]   11   12   12
```

#### Matrix Dimensions

---

Matrix dimensions are specified using the `nrow` and `ncol` arguments in the `matrix()` function. Here is an example of how to create a matrix with specific dimensions:

```r
# Create a matrix with specific dimensions
matrix_data <- matrix(c(1, 2, 3, 4, 5), nrow = 2, ncol = 3)
matrix_data
```

Output:

```r
     [,1] [,2] [,3]
[1,]    1    2    3
[2,]    4    5    NA
```

### 2.4 Arrays in R

---

In R, an array is a multi-dimensional array of numbers. Arrays are used to represent data that has a variable number of rows and columns, and are often used in numerical computations.

#### Creating Arrays

---

Arrays can be created using the `array()` function in R. Here is an example of how to create an array:

```r
# Create an array
array_data <- array(c(1, 2, 3, 4, 5, 6, 7, 8, 9), dim = c(2, 3, 1))
array_data
```

Output:

```r
, , [1]
,,,
[1,]    1    2    3
[2,]    4    5    6

, , [2]
,,,
[1,]    7    8    9
[2,]    NA    NA    NA
```

#### Array Operations

---

Arrays support various operations such as addition, subtraction, multiplication, and indexing. Here are some examples of array operations:

```r
# Create two arrays
array_data1 <- array(c(1, 2, 3, 4, 5, 6, 7, 8, 9), dim = c(2, 3, 1))
array_data2 <- array(c(4, 5, 6, 7, 8, 9, 1, 2, 3), dim = c(2, 3, 1))

# Addition
array_data1 + array_data2
```

Output:

```r
, , [1]
,,,
[1,]    5    7    9
[2,]    9   11   13

, , [2]
,,,
[1,]    11   13   15
[2,]    NA    NA    NA
```

### 2.5 Lists in R

---

In R, a list is a collection of objects of different data types. Lists are used to represent data that has a variable number of elements, and are often used in data manipulation and analysis.

#### Creating Lists

---

Lists can be created using the `list()` function in R. Here is an example of how to create a list:

```r
# Create a list
list_data <- list("apple", 1, 2, 3)
list_data
```

Output:

```r
[[1]]
[1] "apple"

[[2]]
[1] 1

[[3]]
[1] 2

[[4]]
[1] 3
```

#### List Operations

---

Lists support various operations such as indexing, element-wise operations, and binding. Here are some examples of list operations:

```r
# Create two lists
list_data1 <- list("apple", 1, 2, 3)
list_data2 <- list("banana", 4, 5, 6)

# Indexing
list_data1[[1]]
```

Output:

```r
[1] "apple"
```

### 2.6 Data Frames in R

---

In R, a data frame is a two-dimensional array of objects of different data types. Data frames are used to represent data that has a fixed number of rows and columns, and are often used in data manipulation and analysis.

#### Creating Data Frames

---

Data frames can be created using the `data.frame()` function in R. Here is an example of how to create a data frame:

```r
# Create a data frame
data_frame <- data.frame(name = c("John", "Mary", "Bob"), age = c(25, 31, 42))
data_frame
```

Output:

```
  name age
1  John  25
2  Mary  31
3   Bob  42
```

#### Data Frame Operations

---

Data frames support various operations such as filtering, grouping, and merging. Here are some examples of data frame operations:

```r
# Create two data frames
data_frame1 <- data.frame(name = c("John", "Mary", "Bob"), age = c(25, 31, 42))
data_frame2 <- data.frame(name = c("John", "Mary", "Bob"), age = c(25, 31, 42))

# Filtering
data_frame1[data_frame1$age > 30, ]
```

Output:

```
  name age
2  Mary  31
3   Bob  42
```

### 2.7 Factors in R

---

In R, a factor is a type of data that is used to represent categorical data. Factors are used to perform statistical analysis and are often used in data manipulation and analysis.

#### Creating Factors

---

Factors can be created using the `factor()` function in R. Here is an example of how to create a factor:

```r
# Create a factor
factor_data <- factor(c("apple", "banana", "apple", "banana"))
factor_data
```

Output:

```
[1] apple  banana  apple  banana
Levels: apple banana
```

#### Factor Operations

---

Factors support various operations such as indexing, element-wise operations, and binding. Here are some examples of factor operations:

```r
# Create two factors
factor_data1 <- factor(c("apple", "banana", "apple", "banana"))
factor_data2 <- factor(c("orange", "grape", "orange", "grape"))

# Indexing
factor_data1[1]
```

Output:

```
[1] apple
```

### 2.7.2 String Manipulation

---

In R, strings are used to represent text data. Strings can be manipulated using various functions such as `strsplit()`, `strptime()`, and `strsplit()`. Here are some examples of string manipulation:

```r
# Create a string
string_data <- "Hello World"

# Split the string into words
strsplit(string_data, " ")
```

Output:

```r
[[1]]
[1] "Hello"   "World"
```

### 2.8 Dates and Times in R

---

In R, dates and times are used to represent temporal data. Dates and times can be manipulated using various functions such as `as.Date()`, `as.POSIXct()`, and `format()`. Here are some examples of date and time manipulation:

```r
# Create a date
date_data <- as.Date("2022-01-01")

# Create a time
time_data <- as.POSIXct("2022-01-01 12:00:00")

# Format the date and time
format(date_data, "%Y-%m-%d")
format(time_data, "%Y-%m-%d %H:%M:%S")
```

Output:

```
[1] "2022-01-01"
[1] "2022-01-01 12:00:00"
```

### 2.8.1 Date and Time Operations

---

Dates and times can be manipulated using various operations such as adding, subtracting, and comparing. Here are some examples of date and time operations:

```r
# Create two dates
date_data1 <- as.Date("2022-01-01")
date_data2 <- as.Date("2022-01-02")

# Add 1 day to date_data1
date_data1 + 1
```

Output:

```
[1] "2022-01-02"
```

### 2.8.2 Date and Time Formatting

---

Dates and times can be formatted using various functions such as `format()`, `strftime()`, and `ymd()`. Here are some examples of date and time formatting:

```r
# Create a date
date_data <- as.Date("2022-01-01")

# Format the date
format(date_data, "%Y-%m-%d %H:%M:%S")
```

Output:

```
[1] "2022-01-01 00:00:00"
```

### Further Reading

---

- [The R Programming Language](https://cran.r-project.org/doc/manuals/R-intro.html)
- [Data Analysis with R](https://cran.r-project.org/doc/manuals/r-release/R-intro.html)
- [R for Data Science](https://r4ds.had.co.nz/)
- [Data Structures in R](https://www.rforge.net/Rdoc/R-2.10.0/Data.Generics/html/Vector.html)
