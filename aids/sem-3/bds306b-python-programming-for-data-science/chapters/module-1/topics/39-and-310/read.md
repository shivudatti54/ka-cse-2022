# **3.9 and 3.10: Data Structures in Python**

## **Introduction**

In this module, we will explore two fundamental data structures in Python: lists and tuples. These data structures are used to store and manipulate collections of data.

### Lists

#### Definition

A list is a collection of items that can be of any data type, including strings, integers, floats, and other lists. Lists are denoted by square brackets `[]` and are ordered, meaning that the order of the items in the list matters.

#### Characteristics

- Ordered: Lists maintain the order in which items were added.
- Indexable: Items in a list can be accessed using their index (position in the list).
- Mutable: Lists can be modified after creation.

#### Example

```python
# Create a list
fruits = ['apple', 'banana', 'cherry']

# Accessing an item in the list
print(fruits[0])  # Output: apple

# Modifying an item in the list
fruits[0] = 'grape'
print(fruits)  # Output: ['grape', 'banana', 'cherry']

# Adding an item to the list
fruits.append('orange')
print(fruits)  # Output: ['grape', 'banana', 'cherry', 'orange']
```

### Tuples

#### Definition

A tuple is a collection of items that can be of any data type, including strings, integers, floats, and other tuples. Tuples are denoted by parentheses `()` and are ordered, meaning that the order of the items in the tuple matters.

#### Characteristics

- Ordered: Tuples maintain the order in which items were added.
- Indexable: Items in a tuple can be accessed using their index (position in the tuple).
- Immutable: Tuples cannot be modified after creation.

#### Example

```python
# Create a tuple
colors = ('red', 'green', 'blue')

# Accessing an item in the tuple
print(colors[0])  # Output: red

# Trying to modify an item in the tuple will raise an error
try:
    colors[0] = 'yellow'
except TypeError:
    print("Tuples are immutable")
```

### Key Concepts

- **Indexing**: Accessing an item in a list or tuple using its index.
- **Slicing**: Accessing a subset of items in a list or tuple.
- **Append**: Adding an item to the end of a list or tuple.
- **Insert**: Adding an item at a specific position in a list or tuple.
- **Remove**: Removing an item from a list or tuple.
- **Tuple vs. List**: Tuples are immutable, while lists are mutable.

### Exercises

1.  Create a list of your favorite foods and access the first item using indexing.
2.  Create a tuple of your favorite colors and try to modify the first item (this should raise an error).
3.  Create a list of numbers and use slicing to get the first three items.
4.  Create a tuple of numbers and use slicing to get the last two items.

By the end of this module, you should be able to work with lists and tuples in Python, including indexing, slicing, appending, inserting, removing, and comparing them. Practice these concepts through the exercises to reinforce your understanding.
