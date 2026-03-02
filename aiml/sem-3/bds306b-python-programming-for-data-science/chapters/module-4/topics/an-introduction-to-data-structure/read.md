python
# Creating a list of sensor readings
sensor_data = [23.5, 24.1, 22.8, 25.3, 21.9]

# Accessing elements (indexing starts at 0)
print(sensor_data[0])  # Output: 23.5

# Modifying an element (mutable)
sensor_data[4] = 22.0
print(sensor_data)      # Output: [23.5, 24.1, 22.8, 25.3, 22.0]

# Adding an element
sensor_data.append(26.1)
print(sensor_data)      # Output: [23.5, 24.1, 22.8, 25.3, 22.0, 26.1]