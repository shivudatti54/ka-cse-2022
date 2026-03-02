python
import numpy as np

# Define the structure of our data
dt = np.dtype([('name', 'U10'), ('age', np.int32), ('cgpa', np.float64)])

# Create an array with this dtype
data = np.array([('Alice', 22, 8.7), ('Bob', 23, 9.1), ('Charlie', 21, 7.8)], dtype=dt)
print(data)