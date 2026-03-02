python
# Searching for a specific number in a list
numbers = [5, 12, 8, 19, 3, 7, 25]
search_for = 19

for num in numbers:
    print(f"Checking {num}...")
    if num == search_for:
        print(f"Found {search_for}! Stopping the search.")
        break  # Exit the loop immediately
# Control jumps here after the break
print("Search complete.")