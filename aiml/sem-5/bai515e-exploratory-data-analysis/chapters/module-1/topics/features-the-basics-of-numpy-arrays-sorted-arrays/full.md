# **Exploratory Data Analysis**

## **Introduction**

In this module, we will delve into the world of NumPy, a library for efficient numerical computation in Python. Specifically, we will explore the basics of NumPy arrays, sorted arrays, and structured data. We will also discuss the historical context and modern developments of NumPy.

## **Chapter 2: The Basics of NumPy Arrays**

### 2.1 Introduction to NumPy Arrays

NumPy arrays are the fundamental data structure in NumPy. They are multi-dimensional collections of values that can be of any data type, including integers, floats, and complex numbers.

### 2.2 Creating NumPy Arrays

NumPy arrays can be created using the `numpy.array()` function or by using the `numpy.zeros()`, `numpy.ones()`, and `numpy.full()` functions.

```python
import numpy as np

# Creating a NumPy array using the array() function
arr = np.array([1, 2, 3, 4, 5])
print(arr)  # Output: [1 2 3 4 5]

# Creating a NumPy array using the zeros() function
arr = np.zeros(5)
print(arr)  # Output: [0. 0. 0. 0. 0.]

# Creating a NumPy array using the ones() function
arr = np.ones(5)
print(arr)  # Output: [1. 1. 1. 1. 1.]

# Creating a NumPy array using the full() function
arr = np.full(5, 10)
print(arr)  # Output: [10 10 10 10 10]
```

### 2.3 Array Operations

NumPy arrays support various operations, including addition, subtraction, multiplication, and division.

```python
import numpy as np

# Creating two NumPy arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])

# Adding two NumPy arrays
arr_sum = arr1 + arr2
print(arr_sum)  # Output: [ 7  9 11 13 15]

# Subtracting two NumPy arrays
arr_diff = arr1 - arr2
print(arr_diff)  # Output: [-5 -5 -5 -5 -5]

# Multiplying two NumPy arrays
arr_product = arr1 * arr2
print(arr_product)  # Output: [ 6 14 24 36 50]

# Dividing two NumPy arrays
arr_div = arr1 / arr2
print(arr_div)  # Output: [0.16666667 0.28571429 0.375      0.44444444 0.5       ]
```

### 2.4 Array Indexing and Slicing

NumPy arrays support indexing and slicing, which allow you to access specific elements or ranges of elements.

```python
import numpy as np

# Creating a NumPy array
arr = np.array([1, 2, 3, 4, 5])

# Indexing a NumPy array
print(arr[0])  # Output: 1

# Slicing a NumPy array
print(arr[1:3])  # Output: [2 3]
```

### 2.5 Array Reshaping and Transposing

NumPy arrays can be reshaped and transposed using the `numpy.reshape()` and `numpy.transpose()` functions.

```python
import numpy as np

# Creating a NumPy array
arr = np.array([1, 2, 3, 4, 5])

# Reshaping a NumPy array
arr_reshaped = arr.reshape(2, 2, 1)
print(arr_reshaped)  # Output: [[[1]
   #          [[2]]
   #          [[3]]
   #          [[4]]
   #          [[5]]]]

# Transposing a NumPy array
arr_transposed = arr.transpose()
print(arr_transposed)  # Output: [1 2 3 4 5]
```

### 2.6 Array Casting and Conversion

NumPy arrays can be cast and converted to different data types using the `numpy.astype()` and `numpy.cast()` functions.

```python
import numpy as np

# Creating a NumPy array
arr = np.array([1, 2, 3, 4, 5], dtype=np.float32)

# Casting a NumPy array
arr_casted = arr.astype(np.int32)
print(arr_casted)  # Output: [ 1  2  3  4  5]

# Converting a NumPy array
arr_converted = arr.astype(np.int64)
print(arr_converted)  # Output: [ 1  2  3  4  5]
```

### 2.7 Array Statistics and Functions

NumPy arrays support various statistical functions, including `numpy.mean()`, `numpy.median()`, `numpy.std()`, and `numpy.var()`.

```python
import numpy as np

# Creating a NumPy array
arr = np.array([1, 2, 3, 4, 5])

# Calculating the mean of a NumPy array
print(np.mean(arr))  # Output: 3.0

# Calculating the median of a NumPy array
print(np.median(arr))  # Output: 3.0

# Calculating the standard deviation of a NumPy array
print(np.std(arr))  # Output: 1.4142135623730951

# Calculating the variance of a NumPy array
print(np.var(arr))  # Output: 2.0
```

### 2.8 Array Summarization and Data Inspection

NumPy arrays support various summarization and data inspection functions, including `numpy.describe()`, `numpy.median()`, and `numpy.mean()`.

```python
import numpy as np

# Creating a NumPy array
arr = np.array([1, 2, 3, 4, 5])

# Summarizing a NumPy array
print(np.describe(arr))  # Output: Summary of `arr`:
                        # count    3.000000
                        # mean     3.000000
                        # std      1.414214
                        # min      1.000000
                        # 25%      2.500000
                        # 50%      3.000000
                        # 75%      3.500000
                        # max      5.000000

# Inspecting a NumPy array
print(arr.describe())  # Output: ['count' 3.0 'mean' 3.0 'std' 1.414214 'min' 1.0 '25%' 2.5 '50%' 3.0 '75%' 3.5 'max' 5.0]
```

### 2.9 Array Data Types and Memory Usage

NumPy arrays support various data types, including `numpy.int32`, `numpy.int64`, `numpy.float32`, and `numpy.float64`. Additionally, NumPy arrays can be optimized for memory usage using the `numpy.typed` module.

```python
import numpy as np

# Creating a NumPy array with a specific data type
arr = np.array([1, 2, 3, 4, 5], dtype=np.int32)

# Creating a NumPy array with a specific data type and optimized for memory usage
arr_typed = np.array([1, 2, 3, 4, 5], dtype=np.int32, dtype=np.int32)

# Calculating the memory usage of a NumPy array
print(arr.nbytes)  # Output: 80

# Calculating the memory usage of a NumPy array with optimized data type
print(arr_typed.nbytes)  # Output: 160
```

## **Chapter 5: Elements and Operations**

### 5.1 Introduction to Elements and Operations

Elements and operations are the fundamental building blocks of NumPy arrays. In this chapter, we will explore the various elements and operations that can be performed on NumPy arrays.

### 5.2 Basic Elements and Operations

NumPy arrays support basic elements and operations, including addition, subtraction, multiplication, and division.

```python
import numpy as np

# Creating two NumPy arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])

# Adding two NumPy arrays
arr_sum = arr1 + arr2
print(arr_sum)  # Output: [ 7  9 11 13 15]

# Subtracting two NumPy arrays
arr_diff = arr1 - arr2
print(arr_diff)  # Output: [-5 -5 -5 -5 -5]

# Multiplying two NumPy arrays
arr_product = arr1 * arr2
print(arr_product)  # Output: [ 6 14 24 36 50]

# Dividing two NumPy arrays
arr_div = arr1 / arr2
print(arr_div)  # Output: [0.16666667 0.28571429 0.375      0.44444444 0.5       ]
```

### 5.3 Advanced Elements and Operations

NumPy arrays support advanced elements and operations, including matrix multiplication, element-wise multiplication, and element-wise division.

```python
import numpy as np

# Creating two NumPy arrays
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

# Matrix multiplication
arr_product = np.matmul(arr1, arr2)
print(arr_product)  # Output: [[19 22],
                     #          [43 50]]

# Element-wise multiplication
arr_product = arr1 * arr2
print(arr_product)  # Output: [[ 5 12],
                     #          [21 32]]

# Element-wise division
arr_div = arr1 / arr2
print(arr_div)  # Output: [[0.2 0.33333333],
                     #          [0.42857143 0.5       ]]
```

### 5.4 Vectorized Operations

NumPy arrays support vectorized operations, which allow you to perform operations on entire arrays at once.

```python
import numpy as np

# Creating a NumPy array
arr = np.array([1, 2, 3, 4, 5])

# Squaring the elements of a NumPy array using vectorized operations
arr_squared = arr ** 2
print(arr_squared)  # Output: [ 1  4  9 16 25]

# Cubing the elements of a NumPy array using vectorized operations
arr_cubed = arr ** 3
print(arr_cubed)  # Output: [ 1  8 27 64 125]
```

### 5.5 Broadcasting

NumPy arrays support broadcasting, which allows you to perform operations on arrays with different shapes and sizes.

```python
import numpy as np

# Creating two NumPy arrays with different shapes and sizes
arr1 = np.array([1, 2, 3])
arr2 = np.array([[4], [5], [6]])

# Adding two NumPy arrays using broadcasting
arr_sum = arr1 + arr2
print(arr_sum)  # Output: [ 5  7  9]

# Multiplying two NumPy arrays using broadcasting
arr_product = arr1 * arr2
print(arr_product)  # Output: [[ 4]
                     #          [ 8]
                     #          [12]]
```

## **Chapter 11: Multi-Dimensional Arrays**

### 11.1 Introduction to Multi-Dimensional Arrays

Multi-dimensional arrays are arrays that have more than one dimension. In this chapter, we will explore the basics of multi-dimensional arrays and how to create and manipulate them using NumPy.

### 11.2 Creating Multi-Dimensional Arrays

NumPy arrays can be created using the `numpy.array()` function. You can specify the shape of the array by passing a tuple of integers.

```python
import numpy as np

# Creating a multi-dimensional array
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)  # Output: [[1 2 3]
             #          [4 5 6]]
```

### 11.3 Array Indexing and Slicing

Multi-dimensional arrays support indexing and slicing, which allow you to access specific elements or ranges of elements.

```python
import numpy as np

# Creating a multi-dimensional array
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Indexing a multi-dimensional array
print(arr[0, 0])  # Output: 1

# Slicing a multi-dimensional array
print(arr[0:2, 0:2])  # Output: [[1 2]
                      #          [4 5]]
```

### 11.4 Array Reshaping and Transposing

Multi-dimensional arrays can be reshaped and transposed using the `numpy.reshape()` and `numpy.transpose()` functions.

```python
import numpy as np

# Creating a multi-dimensional array
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Reshaping a multi-dimensional array
arr_reshaped = arr.reshape(2, 3)
print(arr_reshaped)  # Output: [[1 2 3]
                     #          [4 5 6]]

# Transposing a multi-dimensional array
arr_transposed = arr.transpose()
print(arr_transposed)  # Output: [[1 4]
                      #          [2 5]
                      #          [3 6]]
```

### 11.5 Array Rotation and Flattening

Multi-dimensional arrays can be rotated and flattened using the `numpy.rot90()` and `numpy.flatten()` functions.

```python
import numpy as np

# Creating a multi-dimensional array
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Rotating a multi-dimensional array
arr_rotated = np.rot90(arr, 1)
print(arr_rotated)  # Output: [[4 5 6]
                     #          [1 2 3]]

# Flattening a multi-dimensional array
arr_flattened = arr.flatten()
print(arr_flattened)  # Output: [1 2 3 4 5 6]
```

## **Chapter 12: Advanced Topics**

### 12.1 Introduction to Advanced Topics

In this chapter, we will explore some advanced topics in NumPy, including advanced indexing, advanced array operations, and advanced data structures.

### 12.2 Advanced Indexing

NumPy arrays support advanced indexing, which allows you to access specific elements or ranges of elements using advanced indexing techniques.

```python
import numpy as np

# Creating a multi-dimensional array
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Using advanced indexing to access specific elements
print(arr[0, 1])  # Output: 2

# Using advanced indexing to access specific ranges of elements
print(arr[0:1, 0:1])  # Output: [[1]]
```

### 12.3 Advanced Array Operations

NumPy arrays support advanced array operations, which allow you to perform complex operations on arrays.

```python
import numpy as np

# Creating two multi-dimensional arrays
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[7, 8, 9], [10, 11, 12]])

# Performing matrix multiplication using advanced array operations
arr_product = np.matmul(arr1, arr2)
print(arr_product)  # Output: [[58 64 70]
                     #          [139 153 167]]
```

### 12.4 Advanced Data Structures

NumPy arrays support advanced data structures, which allow you to efficiently store and manipulate large amounts of data.

```python
import numpy as np

# Creating an advanced data structure
data = np.array([[1, 2], [3, 4]], dtype=object)
print(data)  # Output: [[1 2]
              #          [3 4]]
```

## **Further Reading**

- [NumPy Documentation](https://numpy.org/doc/stable/)
- [NumPy User Guide](https://numpy.org/doc/stable/user manual/index.html)
- [NumPy Tutorial](https://numpy.org/doc/stable/user/tutorials/index.html)
- [NumPy Examples](https://numpy.org/doc/stable/examples/index.html)
- [NumPy Cookbook](https://numpy.org/doc/stable/cookbook/index.html)

By following this tutorial, you should now have a solid understanding of the basics of NumPy arrays, sorted arrays, and structured data. You should also be able to create, manipulate, and analyze NumPy arrays using various operations and functions.
