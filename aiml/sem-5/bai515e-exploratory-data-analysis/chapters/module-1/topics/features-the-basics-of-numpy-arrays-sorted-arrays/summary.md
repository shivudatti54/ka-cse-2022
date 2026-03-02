# **Features, NumPy Arrays, Sorted Arrays, Structured Data Summary**

### Chapter 2: Features

- **Data Types**: NumPy supports various data types, including:
  - Integer types (int8, int16, int32, int64)
  - Floating-point types (float16, float32, float64)
  - Complex types (complex64, complex128)
  - Boolean type (bool)
- **Arrays**: A NumPy array is a collection of elements of the same data type stored in a single block of memory.
- **Arrays vs Lists**: NumPy arrays are more memory-efficient and faster for operations than Python lists.

### Chapter 5: The Basics of NumPy Arrays

- **Array Creation**: Arrays can be created using the `numpy.array()` function or the `numpy.arange()` function.
- **Array Indexing**: Arrays can be indexed using integer values, allowing for element access and manipulation.
- **Array Slicing**: Arrays can be sliced using a subset of indices, allowing for partial data extraction.

### Chapter 11: Sorted Arrays

- **Sorting**: Arrays can be sorted using the `numpy.sort()` function.
- **Sorting Algorithms**: NumPy uses the Timsort algorithm, which is a hybrid sorting algorithm derived from merge sort and insertion sort.
- **Stability**: The sorting algorithm used by NumPy is stable, meaning that the order of equal elements is preserved.

### Chapter 12: Structured Data

- **Structured Arrays**: A structured array is a composed data type that stores data of different types in a single array.
- **Field Descriptors**: Structured arrays are defined using field descriptors, which specify the data type and name of each field.
- **Structured Array Creation**: Structured arrays can be created using the `numpy.dtype` object.

### Important Formulas, Definitions, and Theorems

- **Mean**: $\bar{x} = \frac{\sum x_i}{n}$
- **Median**: $median(x) = \text{middle value of the sorted array}$
- **Standard Deviation**: $\sigma = \sqrt{\frac{\sum (x_i - \bar{x})^2}{n}}$
- **Variance**: $\sigma^2 = \frac{\sum (x_i - \bar{x})^2}{n}$
- **Timsort**: A hybrid sorting algorithm derived from merge sort and insertion sort.
