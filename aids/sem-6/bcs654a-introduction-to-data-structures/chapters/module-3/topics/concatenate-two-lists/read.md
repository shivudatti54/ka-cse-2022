python
# Initialize two lists
list1 = [10, 20, 30]
list2 = [40, 50, 60]

# Concatenate using the '+' operator
concatenated_list = list1 + list2
print("List 1:", list1) # Original lists remain unchanged
print("List 2:", list2)
print("Concatenated List:", concatenated_list) # Output: [10, 20, 30, 40, 50, 60]

# Alternative method using extend() which modifies list1 in-place
list1.extend(list2)
print("List1 after extend():", list1) # Output: [10, 20, 30, 40, 50, 60]