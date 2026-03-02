python
import pandas as pd

# Creating a structured dataset
data = {
    'timestamp': ['2023-10-27 10:00:00', '2023-10-27 10:01:00', '2023-10-27 10:02:00'],
    'sensor_id': [101, 101, 102],
    'temperature_c': [27.4, 27.6, 26.9],
    'status': ['OK', 'OK', 'LOW']
}

# Load into a DataFrame
df = pd.DataFrame(data)
print(df)