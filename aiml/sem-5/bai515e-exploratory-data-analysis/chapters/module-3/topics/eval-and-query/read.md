python
import pandas as pd
df = pd.DataFrame({
    'Voltage_V': [5, 12, 3.3, 24, 5],
    'Current_A': [2, 1.5, 0.8, 0.5, 3],
    'Device': ['Sensor', 'Actuator', 'MCU', 'Display', 'Comm']
})
print(df)