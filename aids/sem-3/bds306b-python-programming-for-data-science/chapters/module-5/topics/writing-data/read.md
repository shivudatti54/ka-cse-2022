python
import pandas as pd

# Sample DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['Bangalore', 'Mysore', 'Hubli']}
df = pd.DataFrame(data)

# Write to CSV without the index
df.to_csv('students_data.csv', index=False)