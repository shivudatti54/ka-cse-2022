python
# Create a sample list (could be a NumPy array in real scenarios)
data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Extract elements from index 2 to 5 (5 is exclusive)
print(data[2:6])   # Output: [30, 40, 50, 60]

# Extract everything from the beginning up to index 4 (exclusive)
print(data[:4])    # Output: [10, 20, 30, 40]

# Extract everything from index 5 to the end
print(data[5:])    # Output: [60, 70, 80, 90, 100]

# Extract every other element
print(data[::2])   # Output: [10, 30, 50, 70, 90]

# Reverse the list
print(data[::-1])  # Output: [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]

# Get the last 3 elements
print(data[-3:])   # Output: [80, 90, 100]