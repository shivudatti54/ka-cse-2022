python
# Writing to a text file
with open('data.txt', 'w') as file:
    file.write("Name,Age,City\n")
    file.write("Alice,28,Bengaluru\n")
    file.write("Bob,32,Mysuru\n")

# Reading the entire content
with open('data.txt', 'r') as file:
    content = file.read()
    print(content)

# Reading line by line (memory-efficient for large files)
with open('data.txt', 'r') as file:
    for line in file:
        print(line.strip())  # .strip() removes the newline character