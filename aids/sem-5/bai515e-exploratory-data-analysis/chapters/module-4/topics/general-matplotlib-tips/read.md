python
# Pyplot (Simple, but less control)
import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4])
plt.ylabel('Some Numbers')
plt.show()

# Object-Oriented (Recommended)
fig, ax = plt.subplots()  # Create a figure and a single axes
ax.plot([1, 2, 3, 4])     # Plot on that specific axes
ax.set_ylabel('Some Numbers') # Set label on that axes
plt.show()