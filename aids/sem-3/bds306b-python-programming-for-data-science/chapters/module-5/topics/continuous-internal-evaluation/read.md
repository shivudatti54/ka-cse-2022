python
# CIE Practical Exam Example Solution
import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the data
df = pd.read_csv('student_marks.csv')

# 2. Calculate total and average
df['Total_Marks'] = df[['Marks_Subject1', 'Marks_Subject2', 'Marks_Subject3']].sum(axis=1)
df['Average_Marks'] = df['Total_Marks'] / 3

# 3. Find student with highest total
top_student = df.loc[df['Total_Marks'].idxmax()]
print(f"Top Student: {top_student['Name']} with {top_student['Total_Marks']} marks")

# 4. Plot average per subject
subject_means = df[['Marks_Subject1', 'Marks_Subject2', 'Marks_Subject3']].mean()
subject_means.plot(kind='bar', title='Average Marks per Subject')
plt.xlabel('Subject')
plt.ylabel('Average Marks')
plt.show()