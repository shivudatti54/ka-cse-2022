python
        import pandas as pd
        # Load data from a CSV file
        data = pd.read_csv('sensor_readings.csv')
        # Display the first 5 rows
        print(data.head())
        # Get summary statistics (mean, std, min, max, etc.)
        print(data.describe())