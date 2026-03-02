python
import numpy as np

# Create a sample array
data_array = np.arange(10).reshape(2, 5)
print("Original Array:\n", data_array)

# Save the array to a file
np.save('my_data.npy', data_array)

# Load the array back from the file
loaded_array = np.load('my_data.npy')
print("\nLoaded Array:\n", loaded_array)