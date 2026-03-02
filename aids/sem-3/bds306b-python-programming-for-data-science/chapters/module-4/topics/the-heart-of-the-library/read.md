python
import numpy as np

# From a Python list
list_1d = [1, 2, 3, 4]
arr_1d = np.array(list_1d)
print("1D Array:", arr_1d)

# A 2D array (matrix)
list_2d = [[1, 2, 3], [4, 5, 6]]
arr_2d = np.array(list_2d)
print("2D Array:\n", arr_2d)

# Using built-in functions
zeros_arr = np.zeros((3, 4))  # Creates a 3x4 array filled with 0.0
ones_arr = np.ones((2, 2))    # Creates a 2x2 array filled with 1.0
range_arr = np.arange(10, 25, 5) # Like range(), but returns an array: [10, 15, 20]