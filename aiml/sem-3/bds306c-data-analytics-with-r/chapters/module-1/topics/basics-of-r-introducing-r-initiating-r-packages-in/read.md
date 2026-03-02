# **Basics of R**

### Table of Contents

1. [Introducing R](#introducing-r)
2. [Initiating R](#initiating-r)
3. [Packages in R](#packages-in-r)
4. [Environments and Functions](#environments-and-functions)
5. [Flow Controls](#flow-controls)
6. [Loops](#loops)
7. [Basic Data Types in R](#basic-data-types-in-r)
8. [Vectors](#vectors)

### 1. Introducing R

---

## **What is R?**

R is a free and open-source programming language and software environment for statistical computing and graphics. It is widely used for data analysis, data visualization, and machine learning.

**Key Features of R:**

- Interactive shell for exploratory data analysis
- Extensive libraries and packages for various tasks
- Support for various data formats
- Large community of users and contributors

## **Why Use R?**

- R is particularly useful for statistical analysis and data visualization
- R is free and open-source, making it accessible to everyone
- R has a large and active community of users and contributors

### 2. Initiating R

---

## **Opening R**

To open R, follow these steps:

- Download and install R from the official website: <https://www.r-project.org/>
- Double-click the R icon to open the R environment
- Alternatively, you can open R from the command line by typing `R`

## **R Environment**

The R environment is the interface where you can write and execute R code. It includes:

- **Console**: a text-based interface for inputting and executing R code
- **Graphical User Interface (GUI)**: a visual interface for data visualization and other tasks

### 3. Packages in R

---

## **What are Packages?**

Packages are collections of R functions, datasets, and documentation that provide specific functionality. They can be installed and loaded into the R environment.

## **Installing Packages**

Packages can be installed using the `install.packages()` function. For example:

```R
install.packages("ggplot2")
```

## **Loading Packages**

Packages can be loaded into the R environment using the `library()` function. For example:

```R
library(ggplot2)
```

### 4. Environments and Functions

---

## **R Environments**

An R environment is a container that stores R objects, such as variables, functions, and datasets. There are several types of R environments, including:

- **Global Environment**: the top-level environment for the R session
- **User Environment**: a user-specific environment that can be loaded into the global environment

## **Functions**

Functions are reusable code blocks that perform specific tasks. In R, functions are defined using the `function()` keyword. For example:

```R
my_function <- function(x) {
  return(x^2)
}
```

### 5. Flow Controls

---

## **Conditional Statements**

Conditional statements are used to control the flow of R code based on conditions. There are two types of conditional statements in R:

- **If Statement**: used to execute a block of code if a condition is true
- **If-Else Statement**: used to execute a block of code if a condition is true, and another block of code if the condition is false

## **Loops**

Loops are used to repeat a block of code for multiple iterations. There are two types of loops in R:

- **For Loop**: used to iterate over a sequence of values
- **While Loop**: used to iterate until a condition is false

### 6. Loops

---

## **For Loops**

For loops are used to iterate over a sequence of values. The syntax for a for loop in R is:

```R
for (i in seq) {
  # code to be executed
}
```

For example:

```R
for (i in 1:10) {
  print(i)
}
```

### 7. Basic Data Types in R

---

## **Numeric Data Types**

Numeric data types are used to store numerical values. There are two types of numeric data types in R:

- **Integer**: whole numbers, such as 1, 2, etc.
- **Double**: decimal numbers, such as 1.5, 2.5, etc.

## **Character Data Types**

Character data types are used to store strings of text. There are two types of character data types in R:

- **Character**: strings of text, such as "hello", "world", etc.
- **Factor**: categorical variables, such as levels of a categorical variable

### 8. Vectors

---

Vectors are a type of R data structure that stores a collection of values of the same type. There are several types of vectors in R:

- **Integer Vector**: a vector of integers
- **Real Vector**: a vector of real numbers
- **Character Vector**: a vector of characters
- **Logical Vector**: a vector of logical values

For example:

```R
x <- c(1, 2, 3, 4, 5)
y <- c("hello", "world", "R")
```
