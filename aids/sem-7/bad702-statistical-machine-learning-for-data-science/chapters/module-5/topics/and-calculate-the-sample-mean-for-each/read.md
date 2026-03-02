python
import pandas as pd

# Sample data: Exam scores of 10 students
data = {'student_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'score': [85, 90, 78, 92, 88, 75, 81, 95, 86, 79]}

# Create a DataFrame
df = pd.DataFrame(data)

# Calculate the sample mean of the 'score' column
sample_mean = df['score'].mean()
print(f"The sample mean of the exam scores is: {sample_mean}")