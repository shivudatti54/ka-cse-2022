python
import numpy as np

arr_1d = np.array([10, 20, 30, 40, 50, 60, 70])

# Get elements from index 1 to 4 (5 is exclusive)
print(arr_1d[1:5])   # Output: [20 30 40 50]

# Get elements from the beginning to index 3
print(arr_1d[:4])    # Output: [10 20 30 40]

# Get elements from index 2 to the end
print(arr_1d[2:])    # Output: [30 40 50 60 70]

# Get every other element
print(arr_1d[::2])   # Output: [10 30 50 70]

# Reverse the array
print(arr_1d[::-1])  # Output: [70 60 50 40 30 20 10]