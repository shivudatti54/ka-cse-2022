# **Lists and Tuples in Python Programming for Data Science**

## **List Introduction**

A list in Python is a collection of items that can be of any data type, including strings, integers, floats, and other lists. Lists are denoted by square brackets `[]` and are ordered, meaning that the order of the items in the list matters.

## **Creating Lists**

There are several ways to create a list in Python:

- Using square brackets `[]` and separating the items with commas: `my_list = [1, 2, 3, 4, 5]`
- Using the `list()` function: `my_list = list([1, 2, 3, 4, 5])`
- Using a list literal with multiple lines: `my_list = [
    1,
    2,
    3,
    4,
    5
]`

## **Indexing Lists**

Indexing is used to access specific items in a list. The index of an item is the position of the item in the list, starting from 0.

- To access an item at a specific index, use square brackets `[]` and the index: `my_list[0]`
- To assign a value to a specific index, use square brackets `[]` and the index: `my_list[0] = 10`
- To get the length of a list, use the `len()` function: `len(my_list)`

## **Slicing Lists**

Slicing is used to extract a subset of items from a list. The syntax for slicing is `my_list[start:stop:step]`, where:

- `start`: The starting index of the slice (inclusive)
- `stop`: The ending index of the slice (exclusive)
- `step`: The increment between indices

- To get a slice of the entire list, use `my_list[:]`
- To get a slice starting from the beginning of the list, use `my_list[:]`
- To get a slice ending at the end of the list, use `my_list[:]`
- To get a slice with a step of 2, use `my_list[::2]`

## **Operations on Lists**

### 1. Append

The `append()` method is used to add an item to the end of a list.

- `my_list.append(10)`
- `my_list.append([1, 2, 3])`

### 2. Insert

The `insert()` method is used to insert an item at a specific index in a list.

- `my_list.insert(0, 10)`
- `my_list.insert(3, [1, 2, 3])`

### 3. Remove

The `remove()` method is used to remove the first occurrence of an item in a list.

- `my_list.remove(10)`
- `my_list.remove([1, 2, 3])`

### 4. Sort

The `sort()` method is used to sort a list in ascending order.

- `my_list.sort()`

### 5. Reverse

The `reverse()` method is used to reverse the order of a list.

- `my_list.reverse()`

### 6. Pop

The `pop()` method is used to remove and return an item at a specific index in a list.

- `my_list.pop(0)`
- `my_list.pop(3)`
- `my_list.pop()`

## Tuples Introduction

A tuple in Python is a collection of items that can be of any data type, including strings, integers, floats, and other tuples. Tuples are denoted by parentheses `()` and are ordered, meaning that the order of the items in the tuple matters.

## Creating Tuples

There are several ways to create a tuple in Python:

- Using parentheses `()` and separating the items with commas: `my_tuple = (1, 2, 3, 4, 5)`
- Using the `tuple()` function: `my_tuple = tuple([1, 2, 3, 4, 5])`
- Using a tuple literal with multiple lines: `my_tuple = (
    1,
    2,
    3,
    4,
    5
)`
