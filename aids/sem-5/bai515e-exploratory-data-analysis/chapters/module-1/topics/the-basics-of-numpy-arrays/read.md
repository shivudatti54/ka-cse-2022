python
import numpy as np

# From a Python list (1-Dimensional)
list_1d = [1, 2, 3, 4, 5]
arr_1d = np.array(list_1d)
print("1D Array:", arr_1d) # Output: [1 2 3 4 5]

# From a nested list (2-Dimensional - a matrix)
list_2d = [[1, 2, 3], [4, 5, 6]]
arr_2d = np.array(list_2d)
print("2D Array:\n", arr_2d)
# Output:
# [[1 2 3]
#  [4 5 6]]

# Using built-in functions
zeros_arr = np.zeros((3, 4))  # Creates a 3x4 array filled with 0.0
ones_arr = np.ones((2, 2))    # Creates a 2x2 array filled with 1.0
range_arr = np.arange(0, 10, 2) # Like range(): [0, 2, 4, 6, 8]