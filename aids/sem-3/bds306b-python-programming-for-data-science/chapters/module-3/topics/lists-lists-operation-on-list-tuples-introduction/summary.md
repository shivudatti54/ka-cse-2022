# **Lists: Lists, Operations on Lists, Tuples: Introduction, Creation, Indexing and Slicing, Operations on Tuples**

## **Lists**

- **Definition:** A mutable collection of items that can be of any data type, including strings, integers, floats, and other lists.
- **Key Operations:**
  - **Append:** `lst.append(item)`, adds an item to the end of the list.
  - **Insert:** `lst.insert(index, item)`, inserts an item at a specified position.
  - **Remove:** `lst.remove(item)`, removes the first occurrence of an item.
  - **Sort:** `lst.sort()`, sorts the list in ascending order.
  - **Reverse:** `lst.reverse()`, reverses the order of the list.
- **Indexing and Slicing:**
  - **Indexing:** `lst[index]`, accesses the item at a specified position.
  - **Slicing:** `lst[start:stop:step]`, extracts a subset of items from the list.

## **Tuples**

- **Definition:** An immutable collection of items that can be of any data type, including strings, integers, floats, and other tuples.
- **Key Operations:**
  - **Indexing:** `tuple[index]`, accesses the item at a specified position.
  - **Slicing:** `tuple[start:stop:step]`, extracts a subset of items from the tuple.
- **Importance:** Tuples are used to represent fixed-size collections of data, and are often used in combination with lists.

## **Formulas and Definitions**

- **Indexing Formula:** `lst[index] = lst[index]` (accessing an item at a specified position)
- **Slicing Formula:** `lst[start:stop:step]` (extracting a subset of items from the list)
- **List Comprehension Formula:** `[expression for item in lst]` (creating a new list from an existing list)

## **Theorems**

- None explicitly stated, but the following principles are useful:
  - **Associativity:** `lst1 + lst2 + lst3` = `(lst1 + lst2) + lst3` (associative property of list concatenation)
  - **Commutativity:** `lst1 + lst2` = `lst2 + lst1` (commutative property of list concatenation)
