python
import pandas as pd
import numpy as np

# Create a Series from a list
student_marks = pd.Series([85, 92, 78, 90, 88])
print("Series from a list:")
print(student_marks)
print("\n") # Adds a newline for clarity

# Create a Series with a custom index
student_marks_named = pd.Series([85, 92, 78, 90, 88], index=['Alice', 'Bob', 'Charlie', 'Diana', 'Evan'])
print("Series with a custom index:")
print(student_marks_named)