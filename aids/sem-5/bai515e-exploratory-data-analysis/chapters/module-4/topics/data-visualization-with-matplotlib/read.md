python
import matplotlib.pyplot as plt
import numpy as np

# Create some sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create Figure and Axes objects explicitly
fig, ax = plt.subplots(figsize=(8, 5)) # fig is the Figure, ax is the Axes

# Plot on the specific Axes
ax.plot(x, y, label='sin(x)', color='blue', linestyle='-')
ax.set_xlabel('X-axis')  # Set label for x-axis
ax.set_ylabel('Y-axis')  # Set label for y-axis
ax.set_title('A Simple Sine Wave') # Set title
ax.legend()  # Show legend

plt.show()  # Display the figure