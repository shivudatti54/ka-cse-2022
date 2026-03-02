# **Lists: Lists, Operations on Lists**

### Introduction to Lists

In Python, a list is a data type that can store multiple values of any data type. Lists are ordered collections of values, which can be of any data type, including strings, integers, floats, and other lists.

## **Creating Lists**

Lists can be created using square brackets `[]` or the `list()` function.

- Using square brackets: `my_list = [1, 2, 3, 4, 5]`
- Using the `list()` function: `my_list = list([1, 2, 3, 4, 5])`

## **Indexing Lists**

Lists are zero-indexed, meaning the first element is at index 0.

- Accessing an element: `my_list[0]`
- Accessing multiple elements: `my_list[0:3]`

## **Slicing Lists**

Slicing allows you to extract a subset of elements from a list.

- Basic slicing: `my_list[1:3]`
- Slicing with step: `my_list[1:3:2]`
- Slicing with start and end indices: `my_list[1:3]` (same as above)

## **Operations on Lists**

### Append Method

The `append()` method adds an element to the end of the list.

- Example: `my_list = [1, 2, 3]; my_list.append(4); print(my_list)` (Output: `[1, 2, 3, 4]`)

### Insert Method

The `insert()` method inserts an element at a specified position.

- Example: `my_list = [1, 2, 3]; my_list.insert(1, 4); print(my_list)` (Output: `[1, 4, 2, 3]`)

### Remove Method

The `remove()` method removes the first occurrence of an element.

- Example: `my_list = [1, 2, 3]; my_list.remove(2); print(my_list)` (Output: `[1, 3]`)

### Sort Method

The `sort()` method sorts the list in ascending order.

- Example: `my_list = [3, 1, 2]; my_list.sort(); print(my_list)` (Output: `[1, 2, 3]`)

### Reverse Method

The `reverse()` method reverses the list.

- Example: `my_list = [1, 2, 3]; my_list.reverse(); print(my_list)` (Output: `[3, 2, 1]`)

### Pop Method

The `pop()` method removes and returns an element at a specified position.

- Example: `my_list = [1, 2, 3]; my_list.pop(1); print(my_list)` (Output: `[1, 3]`)

### List Comprehension

List comprehension is a concise way to create lists.

- Example: `my_list = [x for x in range(1, 6) if x % 2 == 0]` (Output: `[2, 4]`)

### Join Method

The `join()` method concatenates all elements in the list into a string.

- Example: `my_list = ['Hello', 'World']; print(' '.join(my_list))` (Output: `Hello World`)

---

### Tuples: Introduction, Creating, Indexing, Slicing, Operations on Tuples

====================================================================

#### Introduction to Tuples

Tuples are ordered, immutable collections of values. They are similar to lists but cannot be modified.

#### Creating Tuples

Tuples can be created using parentheses `()`.

- Example: `my_tuple = (1, 2, 3, 4, 5)`

#### Indexing Tuples

Tuples can be indexed just like lists.

- Accessing an element: `my_tuple[0]`
- Accessing multiple elements: `my_tuple[0:3]`

#### Slicing Tuples

Tuples can be sliced just like lists.

- Basic slicing: `my_tuple[1:3]`
- Slicing with step: `my_tuple[1:3:2]`
- Slicing with start and end indices: `my_tuple[1:3]` (same as above)

#### Operations on Tuples

Tuples cannot be modified, so we cannot use methods like `append()`, `insert()`, etc. However, we can use tuple methods like `count()`, `index()`, and `replace()`.

- Example: `my_tuple = (1, 2, 3); print(my_tuple.count(2))` (Output: `1`)

### Tuple Methods

#### count()

The `count()` method returns the number of occurrences of an element.

- Example: `my_tuple = (1, 2, 2, 3); print(my_tuple.count(2))` (Output: `2`)

#### index()

The `index()` method returns the index of the first occurrence of an element.

- Example: `my_tuple = (1, 2, 3); print(my_tuple.index(2))` (Output: `1`)

#### replace()

The `replace()` method replaces an element with another element.

- Example: `my_tuple = (1, 2, 3); my_tuple = my_tuple.replace(2, 4); print(my_tuple)` (Output: `(1, 4, 3)`)

#### tuple()

The `tuple()` function creates a tuple from an iterable.

- Example: `my_tuple = tuple([1, 2, 3]); print(my_tuple)` (Output: `(1, 2, 3)`)

Note: This is not a comprehensive list of tuple methods, but it covers some of the most commonly used ones.
