python
import pandas as pd

# Creating a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Age': [24, 27, 22, 32],
    'Branch': ['CSE', 'ECE', 'ME', 'CSE']
}

df = pd.DataFrame(data)
print(df)