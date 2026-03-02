# **Python Programming for Data Science**

## **Module: 6 hours**

## **Topic: Text Book 2, Chapters 5 and 6**

### Chapter 5: Working with Strings

#### Introduction

---

In Python, strings are sequences of characters used to represent text. Strings can be used to store and manipulate text data.

#### String Basics

---

- A string is enclosed in single quotes or double quotes.
- Strings can contain any Unicode characters, including letters, numbers, and special characters.
- Strings are immutable, meaning that once a string is created, it cannot be changed.

#### String Operations

---

- **Concatenation**: The process of joining two or more strings together using the `+` operator.
  ```
  string1 = "Hello"
  string2 = "World"
  print(string1 + " " + string2)
  # Output: "Hello World"
  ```
- **Indexing**: The process of accessing a specific character in a string using its index.
  ```
  string = "Hello"
  print(string[0])  # Output: "H"
  ```
- **Slicing**: The process of accessing a subset of characters in a string using the `[start:stop]` syntax.
  ```
  string = "Hello"
  print(string[1:3])  # Output: "ell"
  ```
- **Length**: The number of characters in a string, accessed using the `len()` function.
  ```
  string = "Hello"
  print(len(string))  # Output: 5
  ```
- **Repetition**: The process of repeating a string using the `*` operator.
  ```
  string = "Hello"
  print(string * 3)  # Output: "HelloHelloHello"
  ```

#### Common String Methods

---

- **`strip()`**: Removes leading and trailing whitespace from a string.
  ```
  string = "   Hello   "
  print(string.strip())  # Output: "Hello"
  ```
- **`lower()`**: Converts a string to lowercase.
  ```
  string = "HELLO"
  print(string.lower())  # Output: "hello"
  ```
- **`upper()`**: Converts a string to uppercase.
  ```
  string = "hello"
  print(string.upper())  # Output: "HELLO"
  ```
- **`split()`**: Splits a string into a list of substrings based on a specified separator.
  ```
  string = "apple,banana,orange"
  print(string.split(","))  # Output: ["apple", "banana", "orange"]
  ```

#### Exercises

---

1.  Create a string containing your name and print it to the console.
2.  Concatenate two strings using the `+` operator and print the result.
3.  Access the second character in a string using indexing and print it to the console.
4.  Repeat a string three times using the `*` operator and print the result.

### Chapter 6: Working with Lists

#### Introduction

---

In Python, lists are ordered collections of items that can be of any data type, including strings, integers, and floats.

#### List Basics

---

- A list is enclosed in square brackets `[]`.
- Lists are ordered, meaning that items are accessed in a specific order.
- Lists can be modified after creation.

#### List Operations

---

- **Append**: Adds an item to the end of a list using the `append()` method.
  ```
  list = [1, 2, 3]
  list.append(4)
  print(list)  # Output: [1, 2, 3, 4]
  ```
- **Insert**: Inserts an item at a specified position in a list using the `insert()` method.
  ```
  list = [1, 2, 3]
  list.insert(1, 4)
  print(list)  # Output: [1, 4, 2, 3]
  ```
- **Remove**: Removes the first occurrence of an item in a list using the `remove()` method.
  ```
  list = [1, 2, 3]
  list.remove(2)
  print(list)  # Output: [1, 3]
  ```
- **Sort**: Sorts a list in ascending order using the `sort()` method.
  ```
  list = [3, 1, 2]
  list.sort()
  print(list)  # Output: [1, 2, 3]
  ```
- **Reverse**: Reverses the order of a list using the `reverse()` method.
  ```
  list = [1, 2, 3]
  list.reverse()
  print(list)  # Output: [3, 2, 1]
  ```

#### Common List Methods

---

- **`index()`**: Returns the index of the first occurrence of an item in a list.
  ```
  list = [1, 2, 3]
  print(list.index(2))  # Output: 1
  ```
- **`count()`**: Returns the number of occurrences of an item in a list.
  ```
  list = [1, 2, 2, 3]
  print(list.count(2))  # Output: 2
  ```
- **`extend()`**: Adds multiple items to the end of a list using the `extend()` method.
  ```
  list = [1, 2, 3]
  list.extend([4, 5, 6])
  print(list)  # Output: [1, 2, 3, 4, 5, 6]
  ```

#### Exercises

---

1.  Create a list containing your favorite colors and print it to the console.
2.  Append a new item to the end of a list using the `append()` method and print the result.
3.  Insert a new item at a specified position in a list using the `insert()` method and print the result.
4.  Remove the first occurrence of an item in a list using the `remove()` method and print the result.

I hope this study material helps you understand the concepts of working with strings and lists in Python. Practice these concepts to become proficient in Python programming for data science.
