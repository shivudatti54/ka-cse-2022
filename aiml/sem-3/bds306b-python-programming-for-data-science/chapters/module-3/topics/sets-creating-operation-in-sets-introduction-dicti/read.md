# **Sets: Creating, Operation in Sets, Introduction to Dictionaries**

### Introduction

In Python programming, sets are an essential data structure used for storing and manipulating a collection of unique elements. In this module, we will explore the concept of sets, including creating sets, operations in sets, and introduce dictionaries. We will also discuss nested dictionaries and looping over dictionaries.

### Sets

A set is an unordered collection of unique elements. Sets are represented by the `set()` function in Python.

**Creating Sets**

You can create a set by passing a list of elements to the `set()` function. For example:

```python
# Creating a set from a list
my_set = set([1, 2, 2, 3, 4, 4, 5])
print(my_set)  # Output: {1, 2, 3, 4, 5}
```

As you can see, the duplicates are removed from the set.

**Operations in Sets**

Sets support the following operations:

- Union: `A ∪ B` - returns a set containing all elements from both sets.
- Intersection: `A ∩ B` - returns a set containing elements common to both sets.
- Difference: `A - B` - returns a set containing elements in `A` but not in `B`.
- Symmetric Difference: `A Δ B` - returns a set containing elements in `A` or `B` but not both.

Example:

```python
# Creating two sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Performing operations
print(set1.union(set2))  # Output: {1, 2, 3, 4, 5, 6}
print(set1.intersection(set2))  # Output: {3, 4}
print(set1.difference(set2))  # Output: {1, 2}
print(set1.symmetric_difference(set2))  # Output: {1, 2, 5, 6}
```

### Introduction to Dictionaries

A dictionary is an unordered collection of key-value pairs. Dictionaries are represented by the `dict()` function in Python.

**Creating Dictionaries**

You can create a dictionary by passing a list of key-value pairs to the `dict()` function. For example:

```python
# Creating a dictionary
my_dict = dict([('name', 'John'), ('age', 30)])
print(my_dict)  # Output: {'name': 'John', 'age': 30}
```

As you can see, the dictionary is created with the given key-value pairs.

### Operations in Dictionaries

Dictionaries support the following operations:

- Accessing elements: `dictionary[key]`
- Updating elements: `dictionary[key] = value`
- Adding elements: `dictionary[key] = value`
- Removing elements: `del dictionary[key]`
- Getting the number of elements: `len(dictionary)`

Example:

```python
# Creating a dictionary
my_dict = {'name': 'John', 'age': 30}

# Performing operations
print(my_dict['name'])  # Output: John
my_dict['city'] = 'New York'
print(my_dict)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}
del my_dict['age']
print(my_dict)  # Output: {'name': 'John', 'city': 'New York'}
print(len(my_dict))  # Output: 2
```

### Nested Dictionaries

A nested dictionary is a dictionary whose values are also dictionaries. You can create a nested dictionary by passing another dictionary as the value to the `dict()` function. For example:

```python
# Creating a nested dictionary
person = {'name': 'John', 'age': 30, 'address': {'street': '123 Main St', 'city': 'New York', 'state': 'NY'}}
print(person)  # Output: {'name': 'John', 'age': 30, 'address': {'street': '123 Main St', 'city': 'New York', 'state': 'NY'}}
```

As you can see, the nested dictionary is created with the given key-value pairs.

### Looping Over Dictionaries

You can loop over a dictionary using a `for` loop. For example:

```python
# Creating a dictionary
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# Looping over the dictionary
for key, value in my_dict.items():
    print(f"{key}: {value}")
```

Output:

```
name: John
age: 30
city: New York
```

This loop iterates over the key-value pairs of the dictionary and prints the key and value for each pair.
