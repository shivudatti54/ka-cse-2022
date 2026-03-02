python
import matplotlib.pyplot as plt
import numpy as np

# Create data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create Figure and Axes objects explicitly
fig, ax = plt.subplots(figsize=(8, 5)) # figsize (width, height) in inches

# Plot on the specific Axes
ax.plot(x, y, label='sin(x)', color='blue', linestyle='--')
ax.set_xlabel('X Axis')  # Set label on the Axes
ax.set_ylabel('Y Axis')
ax.set_title('A Sine Wave')
ax.legend()
ax.grid(True)

plt.show() # Display the figure