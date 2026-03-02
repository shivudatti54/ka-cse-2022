python
# Imagine we are processing a large dataset of sensor readings
sensor_readings = [23.5, 24.1, 25.8, 19.7, 22.3, 105.2, 21.9] # 105.2 is an obvious outlier (error)

# We want to find the first error (value > 100) and stop processing further to save time.
for reading in sensor_readings:
    if reading > 100:
        print(f"Error detected: {reading}. Stopping processing.")
        break  # Exits the for loop immediately
    print(f"Processing valid reading: {reading}")

# The loop stops after finding 105.2. The remaining values (21.9) are not processed.