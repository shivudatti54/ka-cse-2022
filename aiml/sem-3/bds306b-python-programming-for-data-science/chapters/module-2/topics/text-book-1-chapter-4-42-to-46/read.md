# **Text Book 1: Chapter 4 (4.2 to 4.6)**

## **4.2: Introduction to Data Structures**

### Overview

In this section, we will introduce the concept of data structures, which are essential in programming for data science. A data structure is a way of organizing and storing data in a computer so that it can be efficiently accessed and manipulated.

### Definition

A data structure is a collection of data elements, each of which represents a value or a relationship between values.

### Examples

- A list of numbers represents a data structure.
- A dictionary of names and ages represents a data structure.

### Key Concepts

- **Homogeneous**: A collection of data elements of the same type.
- **Heterogeneous**: A collection of data elements of different types.
- **Ordered**: A collection of data elements in a specific order.
- **Unordered**: A collection of data elements without a specific order.

### Python Implementation

In Python, we can create data structures using built-in data types such as lists, tuples, dictionaries, and sets.

### Code Example

```python
# Create a list of numbers
numbers = [1, 2, 3, 4, 5]
print(numbers)

# Create a dictionary of names and ages
people = {"John": 25, "Jane": 30, "Bob": 35}
print(people)
```

## **4.3: Lists**

### Overview

In this section, we will introduce the concept of lists, which are ordered collections of data elements in Python.

### Definition

A list is a collection of data elements of the same type, which can be of different data types such as integers, floats, strings, or other lists.

### Key Concepts

- **Indexing**: Accessing elements in a list by their index.
- **Slicing**: Accessing a subset of elements in a list.
- **Append**: Adding elements to the end of a list.
- **Insert**: Adding elements at a specific position in a list.

### Python Implementation

```python
# Create a list of numbers
numbers = [1, 2, 3, 4, 5]
print(numbers)

# Access an element by its index
print(numbers[0])

# Slice a subset of elements
print(numbers[1:3])

# Append an element to the end of the list
numbers.append(6)
print(numbers)

# Insert an element at a specific position
numbers.insert(2, 10)
print(numbers)
```

## **4.4: Tuples**

### Overview

In this section, we will introduce the concept of tuples, which are ordered collections of data elements in Python.

### Definition

A tuple is a collection of data elements of the same type, which can be of different data types such as integers, floats, strings, or other tuples.

### Key Concepts

- **Immutability**: Tuples cannot be modified after creation.
- **Indexing**: Accessing elements in a tuple by their index.
- **Slicing**: Accessing a subset of elements in a tuple.

### Python Implementation

```python
# Create a tuple of numbers
numbers = (1, 2, 3, 4, 5)
print(numbers)

# Access an element by its index
print(numbers[0])

# Slice a subset of elements
print(numbers[1:3])
```

## **4.5: Dictionaries**

### Overview

In this section, we will introduce the concept of dictionaries, which are unordered collections of key-value pairs in Python.

### Definition

A dictionary is a collection of key-value pairs, where each key is unique and maps to a specific value.

### Key Concepts

- **Key**: A unique identifier for a value.
- **Value**: The data associated with a key.
- **Lookup**: Accessing a value by its key.
- **Insertion**: Adding a new key-value pair to a dictionary.

### Python Implementation

```python
# Create a dictionary of names and ages
people = {"John": 25, "Jane": 30, "Bob": 35}
print(people)

# Access a value by its key
print(people["John"])

# Insert a new key-value pair
people["Alice"] = 20
print(people)
```

## **4.6: Sets**

### Overview

In this section, we will introduce the concept of sets, which are unordered collections of unique data elements in Python.

### Definition

A set is an unordered collection of unique data elements, which can be of different data types such as integers, floats, strings, or other sets.

### Key Concepts

- **Uniqueness**: Sets only contain unique elements.
- **Indexing**: Accessing elements in a set by their index (not applicable).
- **Slicing**: Accessing a subset of elements in a set.
- **Union**: Combining two or more sets into a single set.

### Python Implementation

```python
# Create a set of numbers
numbers = {1, 2, 3, 4, 5}
print(numbers)

# Access a subset of elements
print(numbers[1:3])

# Create a union of two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))
```
