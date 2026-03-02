python
    import numpy as np # The standard convention

    # From a list
    arr_1d = np.array([1, 2, 3, 4, 5])
    arr_2d = np.array([[1, 2, 3], [4, 5, 6]])

    # Using built-in functions
    zeros_arr = np.zeros((3, 4))     # Array of zeros
    ones_arr = np.ones((2, 2))       # Array of ones
    range_arr = np.arange(0, 10, 2)  # Array from 0 to 10 (exclusive), step 2 -> [0, 2, 4, 6, 8]