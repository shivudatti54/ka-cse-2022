# **Basics of R: Introducing R, Initiating R, Packages in R, Environments and Functions, Flow Controls, Loops, Basic Data Types in R, Vectors**

## **Table of Contents**

1. [Introduction to R](#introduction-to-r)
2. [Initiating R](#initiating-r)
3. [Packages in R](#packages-in-r)
4. [Environments and Functions](#environments-and-functions)
5. [Flow Controls](#flow-controls)
6. [Loops](#loops)
7. [Basic Data Types in R](#basic-data-types-in-r)
8. [Vectors](#vectors)

## **Introduction to R**

R is a popular, open-source programming language and environment for statistical computing and graphics. Developed in the 1990s by Ross Ihaka and Robert Gentleman at the University of Auckland, R is widely used by data analysts, data scientists, and statisticians for data analysis, machine learning, and visualization.

R's history dates back to 1993 when the first version, R 1.0, was released. Since then, R has undergone significant updates and enhancements, with the current version being R 4.1.0. R's popularity can be attributed to its flexibility, customizability, and extensive libraries and packages available for data analysis and visualization.

## **Initiating R**

To initiate R, you can follow these steps:

### Using R from the Command Line

1. Open a terminal or command prompt on your computer.
2. Type `R` and press Enter to start R.
3. R will display the R console, where you can execute R commands and interact with the environment.

### Using R from an Integrated Development Environment (IDE)

1. Install an R IDE, such as RStudio, R Commander, or Tidyverse, on your computer.
2. Launch the IDE and select the R environment.
3. The IDE will display the R console, where you can execute R commands and interact with the environment.

### Using R from a Web Browser

1. Open a web browser and navigate to the R console at <https://rstudio.cloud/running-r-in-a-browser/>
2. Log in to the RStudio Cloud account (free trial available).
3. Select the R environment and start a new R session.
4. The R console will be displayed in the web browser, where you can execute R commands and interact with the environment.

## **Packages in R**

In R, a package is a collection of R functions, data, and documentation that provides a specific functionality. R has an extensive library of packages available, which can be installed using the `install.packages()` function.

Here's an example of installing the `ggplot2` package:

```r
# Install the ggplot2 package
install.packages("ggplot2")
```

Once installed, the `ggplot2` package can be loaded using the `library()` function:

```r
# Load the ggplot2 package
library(ggplot2)
```

## **Environments and Functions**

In R, an environment is a collection of objects, including variables, functions, and data frames. Functions are reusable blocks of code that perform a specific task. In R, functions can be defined using the `function()` syntax.

Here's an example of defining a simple function:

```r
# Define a function to calculate the mean of a vector
mean_vector <- function(x) {
  mean(x)
}

# Test the function
x <- c(1, 2, 3, 4, 5)
print(mean_vector(x))
```

## **Flow Controls**

Flow controls are used to control the flow of execution in R. There are two main types of flow controls: conditional and loop-based.

### Conditional Flow Control

R provides several conditional flow control statements, including `if()`, `ifelse()`, and `switch()`.

Here's an example of using the `if()` statement:

```r
# Define a variable
x <- 5

# Use the if() statement to print a message
if (x > 10) {
  print("x is greater than 10")
} else {
  print("x is less than or equal to 10")
}

# Output: x is less than or equal to 10
```

### Loop-Based Flow Control

R provides several loop-based flow control statements, including `for()`, `while()`, and `repeat()`.

Here's an example of using the `for()` loop:

```r
# Define a vector
x <- c(1, 2, 3, 4, 5)

# Use the for() loop to print each element of the vector
for (i in 1:length(x)) {
  print(x[i])
}

# Output:
# [1] 1
# [1] 2
# [1] 3
# [1] 4
# [1] 5
```

## **Loops**

Loops are used to repeat a block of code for a specified number of iterations. R provides several types of loops, including `for()`, `while()`, and `repeat()`.

Here's an example of using the `for()` loop:

```r
# Define a variable
x <- 0

# Use the for() loop to increment x by 1 until it reaches 5
for (i in 1:5) {
  x <- x + 1
  print(x)
}

# Output:
# [1] 1
# [1] 2
# [1] 3
# [1] 4
# [1] 5
```

## **Basic Data Types in R**

R provides several basic data types, including:

- **Numeric**: represents numerical values.
- **Character**: represents text values.
- **Logical**: represents boolean values.
- **Complex**: represents complex numbers.

Here's an example of creating each type of data:

```r
# Numeric value
x <- 5
print(class(x))  # [1] "numeric"

# Character value
y <- "hello"
print(class(y))  # [1] "character"

# Logical value
z <- TRUE
print(class(z))  # [1] "logical"

# Complex value
w <- complex(3, 4)
print(class(w))  # [1] "complex"
```

## **Vectors**

Vectors are R's primary data structure. A vector is a collection of values of the same type stored in a one-dimensional array.

Here's an example of creating a vector:

```r
# Create a vector of numbers
x <- c(1, 2, 3, 4, 5)
print(class(x))  # [1] "numeric"

# Create a vector of text
y <- c("apple", "banana", "cherry")
print(class(y))  # [1] "character"

# Create a vector of logical values
z <- c(TRUE, FALSE, TRUE, FALSE, TRUE)
print(class(z))  # [1] "logical"
```

## **Further Reading**

For more information on R and its applications, refer to the following resources:

- The official R documentation: <https://cran.r-project.org/doc/manuals/r-release/index.html>
- RStudio: <https://www.rstudio.com/>
- DataCamp's R course: <https://www.datacamp.com/courses/r-programming>
- Coursera's R specialization: <https://www.coursera.org/specializations/r>

By following this chapter, you have gained a solid understanding of the basics of R, including initializing R, installing packages, defining functions, controlling flow, and working with basic data types and vectors. With this knowledge, you are ready to move on to more advanced topics in R programming.
