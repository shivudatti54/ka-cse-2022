python
import numpy as np

# Creates an array of integers (int32 or int64 depending on platform)
arr_int = np.array([1, 2, 3, 4])
print(arr_int.dtype)  # Output: int64

# Explicitly set the data type to 32-bit float
arr_float = np.array([1, 2, 3, 4], dtype='float32')
print(arr_float.dtype)  # Output: float32