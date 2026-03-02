python
import numpy as np

# Creating an array from a list
list_1 = [1, 2, 3, 4, 5]
arr_1d = np.array(list_1)
print("1D Array:", arr_1d)

# Creating a 2D array (matrix)
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", arr_2d)

# Using built-in functions to create arrays
zeros_arr = np.zeros((3, 4))  # 3x4 array of zeros
ones_arr = np.ones((2, 2))    # 2x2 array of ones
range_arr = np.arange(0, 10, 2) # Array from 0 to 10 (exclusive), step 2: [0, 2, 4, 6, 8]