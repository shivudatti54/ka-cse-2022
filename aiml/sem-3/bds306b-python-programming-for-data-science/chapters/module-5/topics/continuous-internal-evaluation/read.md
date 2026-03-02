python
import pandas as pd

# 1. Load the data
df = pd.read_csv('student_marks.csv')

# 2. Find average marks per subject
average_marks = df.groupby('Subject')['Marks'].mean()

# 3. Find and display the subject with the highest average
highest_subject = average_marks.idxmax()
highest_avg = average_marks.max()

print(f"The subject with the highest average marks is {highest_subject} with an average of {highest_avg:.2f}")