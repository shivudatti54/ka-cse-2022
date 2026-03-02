python
# Import the necessary library
import matplotlib.pyplot as plt

# Define the data
hours = [1, 2, 3, 4, 5, 6]  # Independent variable (x-axis)
temperature = [22, 23, 25, 27, 24, 21]  # Dependent variable (y-axis)

# Create the figure and axis objects
fig, ax = plt.subplots(figsize=(8, 5))  # figsize controls plot dimensions

# Plot the data
ax.plot(hours, temperature, marker='o', linestyle='-', color='b', label='Sensor Temp')

# Add labels and title
ax.set_xlabel('Time (Hours)')
ax.set_ylabel('Temperature (°C)')
ax.set_title('Temperature Readings Over Time')

# Add a legend and grid for better readability
ax.legend()
ax.grid(True)

# Display the plot
plt.show()