# Input/Output Statements in Python
## Introduction

Input/Output (I/O) statements are a crucial part of any programming language, as they enable communication between the user and the program. In Python, I/O statements are used to read input from the user, display output to the user, and interact with files. Understanding I/O statements is essential for creating interactive and user-friendly programs.

In this topic, we will explore the different types of I/O statements in Python, including input statements, output statements, and file I/O. We will also discuss the importance of I/O statements in programming and provide examples of how to use them effectively.

## Key Concepts

### Input Statements

Input statements are used to read input from the user. Python provides a built-in function called `input()` that allows users to enter data. The `input()` function returns a string, which can be converted to other data types such as integers or floats.

### Output Statements

Output statements are used to display output to the user. Python provides two built-in functions called `print()` and `format()` that allow developers to display output. The `print()` function is used to display simple output, while the `format()` function is used to display formatted output.

### File I/O

File I/O is used to interact with files. Python provides several built-in functions that allow developers to read and write files. The `open()` function is used to open a file, while the `read()` and `write()` functions are used to read and write data to the file.

## Examples

### Example 1: Reading Input from the User

```
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("Hello, " + name + "! You are " + str(age) + " years old.")
```

### Example 2: Displaying Output to the User

```
name = "John Doe"
age = 30

print("Hello, {}! You are {} years old.".format(name, age))
```

### Example 3: Reading and Writing Files

```
file = open("example.txt", "w")
file.write("Hello, world!")
file.close()

file = open("example.txt", "r")
print(file.read())
file.close()
```

## Exam Tips

1. Understand the different types of I/O statements in Python, including input statements, output statements, and file I/O.
2. Know how to use the `input()` function to read input from the user.
3. Know how to use the `print()` and `format()` functions to display output to the user.
4. Understand how to use file I/O to interact with files.
5. Practice using I/O statements in different scenarios to become more comfortable with their use.
6. Be able to convert input data to different data types, such as integers or floats.
7. Understand the importance of closing files after use to prevent data loss.