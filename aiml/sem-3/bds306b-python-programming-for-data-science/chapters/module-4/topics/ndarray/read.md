python
import numpy as np

# 1. From a Python list (creates a 1D array)
list_1d = [1, 2, 3, 4]
arr_1d = np.array(list_1d)
print(arr_1d)         # Output: [1 2 3 4]
print("Shape:", arr_1d.shape) # Output: Shape: (4,)

# 2. From a nested list (creates a 2D array)
list_2d = [[1, 2, 3], [4, 5, 6]]
arr_2d = np.array(list_2d)
print(arr_2d)         # Output: [[1 2 3]
                      #          [4 5 6]]
print("Shape:", arr_2d.shape) # Output: Shape: (2, 3)

# 3. Using built-in functions
zeros_arr = np.zeros((3, 4))  # Creates a 3x4 array filled with 0.0
ones_arr = np.ones((2, 2))    # Creates a 2x2 array filled with 1.0
range_arr = np.arange(10)     # Similar to range(), creates [0 1 2 ... 9]