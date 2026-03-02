python
# Import necessary libraries
import matplotlib.pyplot as plt
import pandas as pd

# Suppose 'df' is your DataFrame loaded with the concrete data
# df = pd.read_csv('concrete_data.csv')

# Create the scatter plot
plt.figure(figsize=(8, 5))  # Set figure size
plt.scatter(df['Cement_Content'], df['Compressive_Strength'], alpha=0.6)  # alpha controls transparency

# Add labels and title (CRUCIAL for a good plot)
plt.xlabel('Cement Content (kg per m³)')
plt.ylabel('Compressive Strength (MPa)')
plt.title('Relationship between Cement Content and Concrete Strength')
plt.grid(True, linestyle='--', alpha=0.7)  # Add a grid for better readability

# Display the plot
plt.show()