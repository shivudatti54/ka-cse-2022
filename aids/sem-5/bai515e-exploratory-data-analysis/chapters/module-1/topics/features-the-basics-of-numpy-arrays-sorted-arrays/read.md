# Features, The Basics of NumPy Arrays, Sorted Arrays, Structured Data: NumPy’s Structured Arrays

===========================================================

## Table of Contents

---

1. [Features](#features)
2. [The Basics of NumPy Arrays](#the-basics-of-numpy-arrays)
3. [Sorted Arrays](#sorted-arrays)
4. [Structured Data: NumPy’s Structured Arrays](#structured-data-numpy’s-structured-arrays)

## Features

---

### Definition:

In NumPy, a feature is a column in a structured array that stores data of a specific type, such as integers, floats, or strings.

### Characteristics:

- Each feature has a specific data type.
- Features are stored in a specific order.
- Features can be accessed using their column index.

### Example:

```python
import numpy as np

# Create a sample structured array
data = np.array([
    ["John", 25, 100],
    ["Mary", 31, 200],
    ["Jane", 22, 50]
], dtype=[("name", "S10"), ("age", int), ("salary", int)])

print(data)
# Output:
# [(' John', 25, 100)
#  ('Mary', 31, 200)
#  ('Jane', 22, 50)]
```

## The Basics of NumPy Arrays

---

### Definition:

A NumPy array is a multi-dimensional collection of values of the same data type stored in a contiguous block of memory.

### Characteristics:

- NumPy arrays support operations like indexing, slicing, and arithmetic.
- NumPy arrays are homogeneous, meaning all elements must be of the same data type.
- NumPy arrays are not zero-filled, meaning they do not contain null values.

### Example:

```python
import numpy as np

# Create a sample NumPy array
data = np.array([1, 2, 3, 4, 5])

print(data)
# Output: [1 2 3 4 5]
```

## Sorted Arrays

---

### Definition:

A sorted array is a NumPy array that has been sorted in ascending or descending order.

### Characteristics:

- Sorted arrays support operations like indexing and slicing.
- Sorted arrays are homogeneous, meaning all elements must be of the same data type.

### Example:

```python
import numpy as np

# Create a sample NumPy array
data = np.array([5, 2, 8, 1, 9])

# Sort the array in ascending order
data_sorted = np.sort(data)

print(data_sorted)
# Output: [1 2 5 8 9]
```

## Structured Data: NumPy’s Structured Arrays

---

### Definition:

A structured array is a NumPy array that stores data of different types in separate columns.

### Characteristics:

- Structured arrays support operations like indexing and slicing.
- Structured arrays are homogeneous, meaning all elements must be of the same data type.

### Example:

```python
import numpy as np

# Create a sample structured array
data = np.array([
    ["John", 25, 100],
    ["Mary", 31, 200],
    ["Jane", 22, 50]
], dtype=[("name", "S10"), ("age", int), ("salary", int)])

print(data)
# Output:
# [(' John', 25, 100)
#  ('Mary', 31, 200)
#  ('Jane', 22, 50)]
```

### Accessing Features:

```python
import numpy as np

# Create a sample structured array
data = np.array([
    ["John", 25, 100],
    ["Mary", 31, 200],
    ["Jane", 22, 50]
], dtype=[("name", "S10"), ("age", int), ("salary", int)])

# Access the 'name' feature
print(data["name"])
# Output: [' John' 'Mary' 'Jane']

# Access the 'age' feature
print(data["age"])
# Output: [25 31 22]

# Access the 'salary' feature
print(data["salary"])
# Output: [100 200 50]
```

### Modifying Features:

```python
import numpy as np

# Create a sample structured array
data = np.array([
    ["John", 25, 100],
    ["Mary", 31, 200],
    ["Jane", 22, 50]
], dtype=[("name", "S10"), ("age", int), ("salary", int)])

# Modify the 'name' feature
data["name"] = ["Johny", "Maryy", "Janny"]

# Modify the 'age' feature
data["age"] = [26, 32, 23]

# Modify the 'salary' feature
data["salary"] = [150, 300, 75]

print(data)
# Output:
# [(' Johny', 26, 150)
#  ('Maryy', 32, 300)
#  ('Janny', 23, 75)]
```
