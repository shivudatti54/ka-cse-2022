python
    # Creating a list of sensor readings
    temperature_readings = [23.5, 24.1, 22.8, 21.9, 25.2]
    print(temperature_readings[0])  # Output: 23.5 (Indexing)
    print(temperature_readings[1:3]) # Output: [24.1, 22.8] (Slicing)

    # Modifying the list (Mutable)
    temperature_readings.append(26.0)  # Adds 26.0 to the end
    temperature_readings[2] = 23.0     # Changes the third element
    print(temperature_readings) # Output: [23.5, 24.1, 23.0, 21.9, 25.2, 26.0]