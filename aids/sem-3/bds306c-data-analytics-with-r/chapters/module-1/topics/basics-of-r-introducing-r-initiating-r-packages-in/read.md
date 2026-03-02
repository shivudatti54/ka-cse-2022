# **Basics of R**

## **Introduction to R**

R is a popular, free, and open-source programming language for statistical computing and graphics. It is widely used in data analysis, machine learning, and data visualization.

### Key Features of R

- Interpreted language
- Built-in graphics and statistical analysis
- Large community of users and developers
- Extensive libraries and packages for data analysis
- Cross-platform compatibility

### Installing R

To install R, follow these steps:

- Download the R installer from the official R website.
- Follow the installation instructions for your operating system.
- Once installed, launch R from the start menu or by typing "R" in the terminal.

### Initializing R

When you first launch R, you will see a prompt that looks like this:

```
>
```

This is the R console, where you can write and execute R code. To initialize R, simply type "R" and press enter.

### Packages in R

---

R has a vast collection of packages that provide additional functionality for data analysis and other tasks. To install a package, use the following command:

```r
install.packages("package_name")
```

Replace "package_name" with the name of the package you want to install.

### Environments in R

---

In R, an environment is a collection of variables and functions that can be used to organize and manage your code. There are three types of environments in R:

- **Global Environment**: This is the top-level environment in R, where you can store global variables and functions.
- **Working Environment**: This is the current environment where you can store variables and functions that you are working on.
- **Loaded Packages**: When you load a package, it creates a new environment that is specific to that package.

### Functions in R

---

In R, a function is a block of code that performs a specific task. Functions can be defined using the `function()` keyword.

```r
function_name <- function(input) {
  # code here
}
```

To call a function, use the following syntax:

```r
function_name(input)
```

### Flow Control in R

---

Flow control statements in R allow you to control the flow of your code based on conditions and logic. The most common flow control statements in R are:

- **if()**: Used to execute a block of code if a condition is true.
- **else()**: Used to execute a block of code if a condition is false.
- **for()**: Used to execute a block of code repeatedly for a specified number of times.
- **while()**: Used to execute a block of code repeatedly while a condition is true.

### Loops in R

---

Loops in R allow you to execute a block of code repeatedly for a specified number of times. The most common types of loops in R are:

- **for()**: Used to execute a block of code repeatedly for a specified number of times.
- **while()**: Used to execute a block of code repeatedly while a condition is true.

### Basic Data Types in R

---

R has several basic data types that can be used to store and manipulate data.

- **Numeric**: Used to store numerical values.
- **Character**: Used to store strings of text.
- **Logical**: Used to store true or false values.
- **Factor**: Used to store categorical data.

### Vectors in R

---

Vectors in R are a collection of values of the same type. Vectors are denoted by the `$` symbol. Here is an example of a vector:

```r
numbers <- c(1, 2, 3, 4, 5)
```

Vectors can be created in several ways:

- **Using the c() function**: `c(1, 2, 3, 4, 5)`
- **Using the seq() function**: `seq(1, 5)`
- **Using the rep() function**: `rep(1:5, 1)`

Vectors can be manipulated in several ways:

- **Using indexing**: `numbers[1]`
- **Using slicing**: `numbers[1:3]`
- **Using concatenation**: `numbers <- c(numbers, 6)`
