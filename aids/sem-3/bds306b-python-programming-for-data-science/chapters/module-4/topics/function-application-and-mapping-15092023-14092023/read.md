python
import pandas as pd

# Create a Series of temperatures in Celsius
temps = pd.Series([22, 18, 35, 16])
print("Celsius:", temps.values)

# Define a function to convert Celsius to Fahrenheit
def celsius_to_fahr(temp_c):
    return (temp_c * 9/5) + 32

# Apply the function to each element in the Series
temps_fahr = temps.apply(celsius_to_fahr)
print("Fahrenheit:", temps_fahr.values)