python
import numpy as np

# Define the structure of our data
student_dtype = np.dtype([
    ('usn', np.int32),       # Field 1: USN as a 32-bit integer
    ('name', 'U20'),         # Field 2: Name as a Unicode string of max length 20
    ('cgpa', np.float64),    # Field 3: CGPA as a 64-bit float
    ('branch', 'U10')        # Field 4: Branch as a string of max length 10
])