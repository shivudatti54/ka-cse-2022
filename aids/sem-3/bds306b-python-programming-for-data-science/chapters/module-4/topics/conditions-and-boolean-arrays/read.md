python
import numpy as np

# Create a sample array
arr = np.array([12, 15, 18, 21, 24, 27])

# Check which elements are greater than 20
boolean_mask = arr > 20
print(boolean_mask)
# Output: [False False False  True  True  True]