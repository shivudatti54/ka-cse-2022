python
import numpy as np

# Create a 1D array from a list
arr_1d = np.array([1, 2, 3, 4, 5])
print(arr_1d)  # Output: [1 2 3 4 5]

# Create a 2D array (matrix)
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr_2d)
# Output:
# [[1 2 3]
#  [4 5 6]]

# Create special arrays
zeros_arr = np.zeros((3, 4))  # 3x4 array filled with 0.0
ones_arr = np.ones((2, 2))    # 2x2 array filled with 1.0
range_arr = np.arange(10)     # Similar to range(10): [0 1 2 3 4 5 6 7 8 9]