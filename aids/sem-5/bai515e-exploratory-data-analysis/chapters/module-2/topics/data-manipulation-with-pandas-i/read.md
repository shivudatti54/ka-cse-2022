python
import pandas as pd

# Creating a Series from a list
student_ages = pd.Series([21, 22, 20, 23, 21], index=['R101', 'R102', 'R103', 'R104', 'R105'])
print(student_ages)