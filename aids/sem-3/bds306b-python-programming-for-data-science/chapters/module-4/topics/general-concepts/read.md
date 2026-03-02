python
import pandas as pd

# Create a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['Bengaluru', 'Mysuru', 'Hubli']
}
df = pd.DataFrame(data)
print(df)