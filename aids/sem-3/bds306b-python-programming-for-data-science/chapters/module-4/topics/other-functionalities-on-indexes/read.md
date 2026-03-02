python
import pandas as pd

data = {
    'USN': ['01VTUCS001', '01VTUCS002', '01VTUEC045'],
    'Name': ['Alice', 'Bob', 'Charlie'],
    'CGPA': [9.5, 8.8, 7.9]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)