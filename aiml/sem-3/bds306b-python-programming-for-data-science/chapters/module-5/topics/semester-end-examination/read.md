python
# Load data
df = pd.read_csv('exam_data.csv')
# Group by 'Department' and calculate the mean of 'Score'
result = df.groupby('Department')['Score'].mean()
print(result)