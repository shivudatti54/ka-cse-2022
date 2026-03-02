# **Basics of R Continued: Matrices and Arrays, Lists, Data Frames, Factors, Strings, Dates and Times**

**Chapter 2:**
**Section 2.3-2.8.2**
===========================================================

### 2.3 Matrices in R

In R, a matrix is a two-dimensional array of values. It is a fundamental data structure in R used for storing and manipulating data.

**Definition:** A matrix is a rectangular array of numerical values, arranged in rows and columns.

**Key Concepts:**

- **Rows:** The horizontal arrangement of values in a matrix.
- **Columns:** The vertical arrangement of values in a matrix.
- **Dimnames:** The names assigned to the dimensions of a matrix.

**Creating a Matrix:**

You can create a matrix in R using the `matrix()` function or the `array()` function.

```r
# Using matrix()
matrix(c(1, 2, 3, 4, 5, 6), nrow = 2, ncol = 3)

# Using array()
array(c(1, 2, 3, 4, 5, 6), dim = c(2, 3))
```

### 2.4 Vectors in R

A vector is a one-dimensional array of values. It is a fundamental data structure in R used for storing and manipulating data.

**Definition:** A vector is a collection of values of the same data type stored in a single sequence.

**Key Concepts:**

- **Elements:** The individual values in a vector.
- **Length:** The number of elements in a vector.

**Creating a Vector:**

You can create a vector in R using the `c()` function.

```r
c(1, 2, 3, 4, 5)
```

### 2.5 Lists in R

A list is an R data structure that can store multiple values of different data types. Lists are useful for storing and manipulating complex data.

**Definition:** A list is an ordered collection of values of different data types.

**Key Concepts:**

- **Elements:** The individual values in a list.
- **Names:** The names assigned to the elements of a list.

**Creating a List:**

You can create a list in R using the `list()` function.

```r
list(1, 2, 3, "hello")
```

### 2.6 Data Frames in R

A data frame is a two-dimensional array of values, where each row represents a single observation, and each column represents a variable. Data frames are useful for storing and manipulating tabular data.

**Definition:** A data frame is a table of values, where each row represents a single observation, and each column represents a variable.

**Key Concepts:**

- **Rows:** The horizontal arrangement of values in a data frame.
- **Columns:** The vertical arrangement of values in a data frame.
- **Names:** The names assigned to the columns of a data frame.

**Creating a Data Frame:**

You can create a data frame in R using the `data.frame()` function.

```r
data.frame(name = c("John", "Mary", "David"),
           age = c(25, 31, 42))
```

### 2.7 Factors in R

A factor is a type of data in R that represents a categorical variable. Factors are useful for storing and manipulating categorical data.

**Definition:** A factor is a type of data in R that represents a categorical variable.

**Key Concepts:**

- **Levels:** The distinct categories of a factor.
- **Levels argument:** The argument used to specify the levels of a factor.

**Creating a Factor:**

You can create a factor in R using the `factor()` function.

```r
factor(c("male", "female", "male"))
```

### 2.7.2 Strings in R

A string is a sequence of characters in R. Strings are useful for storing and manipulating text data.

**Definition:** A string is a sequence of characters in R.

**Key Concepts:**

- **Elements:** The individual characters in a string.
- **Length:** The number of characters in a string.

**Creating a String:**

You can create a string in R using the `paste()` function or the `char()` function.

```r
paste("Hello", " ", "World")
char(6, "Hello, World!")
```

### 2.8 Dates and Times in R

Dates and times are used to represent dates and times in R. Dates and times are useful for storing and manipulating temporal data.

**Definition:** A date and time is a combination of a date and a time.

**Key Concepts:**

- **Date and time classes:** The built-in classes in R used to represent dates and times.
- **Format:** The way in which dates and times are displayed in R.

**Creating a Date and Time:**

You can create a date and time in R using the `Sys.time()` function or the `as.Date()` function.

```r
Sys.time()
as.Date("2022-02-26")
```
