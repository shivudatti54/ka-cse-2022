python
# Group by column and calculate mean
grouped = df.groupby('Category')['Sales'].mean()

# Multiple aggregation functions
result = df.groupby('Department').agg({'Salary': ['mean', 'sum'], 'Age': 'max'})