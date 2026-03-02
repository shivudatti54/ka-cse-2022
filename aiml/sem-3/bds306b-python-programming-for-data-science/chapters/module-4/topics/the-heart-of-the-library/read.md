python
    import pandas as pd

    # Create a sample DataFrame from a dictionary
    data = {
        'Sensor_ID': [101, 102, 103],
        'Temperature': [28.5, 22.1, 25.9],
        'Status': ['OK', 'FAIL', 'OK']
    }
    df = pd.DataFrame(data)

    # Select the 'Temperature' column
    temp_series = df['Temperature']
    print(temp_series)
    # Output: 
    # 0    28.5
    # 1    22.1
    # 2    25.9
    # Name: Temperature, dtype: float64