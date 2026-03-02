python
import pandas as pd

# Create a Series from a list
data = [85, 92, 78, 90, 88]
student_marks = pd.Series(data, index=['Student1', 'Student2', 'Student3', 'Student4', 'Student5'])
print(student_marks)