# **Sets: Creating, Operations, Introduction to Dictionaries, and Loops**

## **Introduction**

In this module, we will explore the concepts of sets and dictionaries in Python. Sets are unordered collections of unique elements, while dictionaries are data structures that store mappings of unique keys to values. We will cover the creation, operations, and use of sets and dictionaries, as well as some advanced concepts like nested dictionaries and looping over dictionaries.

## **Sets: Creating and Operations**

### Defining Sets

In Python, a set is defined using the `set()` function or the `set()` syntax. You can create a set from a list, tuple, or other set.

```python
# Creating a set from a list
my_set = set([1, 2, 3, 4, 5])
print(my_set)  # {1, 2, 3, 4, 5}

# Creating a set from a tuple
my_set = set((1, 2, 3, 4, 5))
print(my_set)  # {1, 2, 3, 4, 5}
```

### Set Operations

Sets support various operations, including union, intersection, difference, and symmetric difference.

- **Union**: Returns a set containing all elements from both sets.

      ```python

  set1 = {1, 2, 3}
  set2 = {3, 4, 5}
  print(set1.union(set2)) # {1, 2, 3, 4, 5}

````

*   **Intersection**: Returns a set containing elements common to both sets.

    ```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.intersection(set2))  # {3}
````

- **Difference**: Returns a set containing elements in `set1` but not in `set2`.

      ```python

  set1 = {1, 2, 3}
  set2 = {3, 4, 5}
  print(set1.difference(set2)) # {1, 2}

````

*   **Symmetric Difference**: Returns a set containing elements in either `set1` or `set2` but not in both.

    ```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.symmetric_difference(set2))  # {1, 2, 4, 5}
````

### Set Membership

You can check if an element is in a set using the `in` operator.

```python
my_set = {1, 2, 3}
print(2 in my_set)  # True
print(4 in my_set)  # False
```

### Set Additions and Removals

You can add elements to a set using the `add()` method and remove elements using the `remove()` or `discard()` method.

```python
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  # {1, 2, 3, 4}
my_set.remove(2)
print(my_set)  # {1, 3, 4}
my_set.discard(5)
print(my_set)  # {1, 3, 4}
```

### Set Union and Intersection

You can calculate the union and intersection of two sets using the `union()` and `intersection()` methods, respectively.

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))  # {1, 2, 3, 4, 5}
print(set1.intersection(set2))  # {3}
```

## **Dictionaries: Creating, Operations, and Loops**

### Defining Dictionaries

In Python, a dictionary is defined using the `dict()` function or the `dict()` syntax. You can create a dictionary from a list of key-value pairs.

```python
# Creating a dictionary from a list of key-value pairs
my_dict = dict([('name', 'John'), ('age', 30)])
print(my_dict)  # {'name': 'John', 'age': 30}
```

### Dictionary Operations

Dictionaries support various operations, including key-value lookups, updates, and deletions.

- **Key-Value Lookup**: Access a value using its corresponding key.

      ```python

  my_dict = {'name': 'John', 'age': 30}
  print(my_dict['name']) # John

````

*   **Key-Value Update**: Update a value using its corresponding key.

    ```python
my_dict = {'name': 'John', 'age': 30}
my_dict['age'] = 31
print(my_dict)  # {'name': 'John', 'age': 31}
````

- **Key Deletion**: Delete a key-value pair.

      ```python

  my_dict = {'name': 'John', 'age': 30}
  del my_dict['name']
  print(my_dict) # {'age': 30}

````

### Nested Dictionaries

You can create nested dictionaries using the same syntax as regular dictionaries.

```python
# Creating a nested dictionary
my_dict = {'name': 'John', 'age': 30, 'address': {'street': '123 Main St', 'city': 'Anytown'}}
print(my_dict['address']['street'])  # 123 Main St
````

### Looping over Dictionaries

You can loop over dictionaries using the `.items()`, `.keys()`, and `.values()` methods.

- **Looping over Key-Value Pairs**:

      ```python

  my_dict = {'name': 'John', 'age': 30}
  for key, value in my_dict.items():
  print(f"{key}: {value}")

# Output:

# name: John

# age: 30

````

*   **Looping over Keys**:

    ```python
my_dict = {'name': 'John', 'age': 30}
for key in my_dict.keys():
    print(key)
# Output:
# name
# age
````

- **Looping over Values**:

      ```python

  my_dict = {'name': 'John', 'age': 30}
  for value in my_dict.values():
  print(value)

# Output:

# John

# 30

```

This concludes the study material for Sets: Creating, Operations, Introduction to Dictionaries, and Loops in Python. Practice these concepts to become proficient in working with sets and dictionaries in Python.
```
