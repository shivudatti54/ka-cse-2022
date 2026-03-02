# **Python Programming for Data Science**

## **Module: 6 hr**

## **Topic: Text Book 2: Chapter 5 and Chapter 6**

### Introduction

In this module, we will cover two important chapters from the textbook: Chapter 5 and Chapter 6. These chapters will introduce you to more advanced concepts in Python programming for data science, including data structures, file input/output, and working with dates and times.

### Chapter 5: Data Structures

#### Introduction

In this chapter, we will learn about two important data structures in Python: lists and tuples.

#### Lists

A list is a collection of items that can be of any data type, including strings, integers, floats, and other lists. Lists are denoted by square brackets `[]` and are used to store multiple values.

**Example: Creating a List**

```python
# Create a list of strings
fruits = ['apple', 'banana', 'orange']

# Print the list
print(fruits)  # Output: ['apple', 'banana', 'orange']
```

#### Tuples

A tuple is a collection of items that cannot be modified. Tuples are denoted by parentheses `()` and are used to store multiple values that should not be changed.

**Example: Creating a Tuple**

```python
# Create a tuple of integers
numbers = (1, 2, 3, 4, 5)

# Print the tuple
print(numbers)  # Output: (1, 2, 3, 4, 5)
```

#### Key Concepts

- Lists are mutable, meaning they can be modified after creation.
- Tuples are immutable, meaning they cannot be modified after creation.
- Lists are denoted by square brackets `[]`, while tuples are denoted by parentheses `()`.

### Chapter 6: File Input/Output

#### Introduction

In this chapter, we will learn how to read and write files in Python.

#### Reading Files

To read a file, we can use the `open()` function, which returns a file object. We can then use the `read()` method to read the contents of the file.

**Example: Reading a File**

```python
# Open a file
file = open('example.txt', 'r')

# Read the contents of the file
contents = file.read()

# Print the contents
print(contents)

# Close the file
file.close()
```

#### Writing Files

To write to a file, we can use the `open()` function with the `'w'` mode, which creates a new file and truncates its contents. We can then use the `write()` method to write to the file.

**Example: Writing to a File**

```python
# Open a file
file = open('example.txt', 'w')

# Write to the file
file.write('Hello, world!')

# Close the file
file.close()
```

#### Key Concepts

- The `open()` function returns a file object, which can be used to read and write to a file.
- The `read()` method reads the contents of a file, while the `write()` method writes to a file.
- The `'r'` mode reads from a file, while the `'w'` mode writes to a file.

### Conclusion

In this module, we have covered two important chapters from the textbook: Chapter 5 and Chapter 6. We have learned about data structures, including lists and tuples, and file input/output, including reading and writing files. With this knowledge, you will be able to write more complex programs in Python and work with data in a variety of formats.
