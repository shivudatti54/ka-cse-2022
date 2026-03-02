python
# Import the necessary library
import matplotlib.pyplot as plt

# Sample data
temp = [25, 30, 35, 40, 45, 50, 55, 60]  # Temperature in °C
power = [220, 215, 208, 200, 190, 180, 170, 165]  # Power output in Watts

# Create the scatter plot
plt.figure(figsize=(8, 5))  # Set the figure size
plt.scatter(temp, power, color='blue', alpha=0.7)  # Plot data points

# Add labels and title
plt.xlabel('Temperature (°C)')
plt.ylabel('Power Output (Watts)')
plt.title('Solar Panel Efficiency: Power vs. Temperature')

# Add a grid for better readability
plt.grid(True, linestyle='--', alpha=0.6)

# Display the plot
plt.show()