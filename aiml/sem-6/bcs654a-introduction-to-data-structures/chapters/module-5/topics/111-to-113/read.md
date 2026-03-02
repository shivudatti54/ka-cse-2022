# **11.1 Introduction to Sorting**

### What is Sorting?

Sorting is the process of arranging data in a specific order, usually in ascending or descending order, to make it easier to analyze or use. It is an essential technique in data structures and algorithms.

### Reasons for Sorting

- Easy to read and understand data
- Fast data retrieval and manipulation
- Improved data organization and management
- Simplified data analysis and visualization

### Types of Sorting

- **In-place sorting**: Sorting data without using extra memory
- **External sorting**: Sorting data using extra memory, usually for large datasets

### Common Sorting Algorithms

- **Bubble Sort**
- **Selection Sort**
- **Insertion Sort**

# **11.2 Bubble Sort**

### What is Bubble Sort?

Bubble sort is a simple sorting algorithm that works by repeatedly swapping the adjacent elements if they are in the wrong order.

### How Bubble Sort Works

1.  Start at the beginning of the array
2.  Compare adjacent elements and swap them if they are in the wrong order
3.  Repeat steps 1-2 until the end of the array is reached
4.  Repeat steps 1-3 until no more swaps are needed

### Example of Bubble Sort

Suppose we want to sort the array `[5, 2, 8, 3, 1]` using bubble sort:

| Iteration | Array             | Swaps             |
| --------- | ----------------- | ----------------- | --- |
| 1         | `[5, 2, 8, 3, 1]` | `[2, 5, 8, 3, 1]` | 1   |
| 2         | `[2, 5, 8, 3, 1]` | `[2, 3, 8, 5, 1]` | 1   |
| 3         | `[2, 3, 8, 5, 1]` | `[2, 3, 1, 5, 8]` | 1   |
| 4         | `[2, 3, 1, 5, 8]` | `[2, 3, 1, 5, 8]` | 0   |

### Implementation of Bubble Sort in Python

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

arr = [5, 2, 8, 3, 1]
print(bubble_sort(arr))
```

# **11.3 Selection Sort**

### What is Selection Sort?

Selection sort is a simple sorting algorithm that works by selecting the smallest (or largest) element from the unsorted part of the array and swapping it with the first element of the unsorted part.

### How Selection Sort Works

1.  Start at the beginning of the array
2.  Find the smallest (or largest) element in the unsorted part of the array
3.  Swap the smallest (or largest) element with the first element of the unsorted part
4.  Repeat steps 1-3 until the end of the array is reached

### Example of Selection Sort

Suppose we want to sort the array `[5, 2, 8, 3, 1]` using selection sort:

| Iteration | Array             | Smallest Element |
| --------- | ----------------- | ---------------- |
| 1         | `[5, 2, 8, 3, 1]` | `1`              |
| 2         | `[1, 2, 8, 3, 5]` | `1`              |
| 3         | `[1, 2, 3, 8, 5]` | `2`              |
| 4         | `[1, 2, 3, 5, 8]` | `3`              |
| 5         | `[1, 2, 3, 5, 8]` | `5`              |

### Implementation of Selection Sort in Python

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

arr = [5, 2, 8, 3, 1]
print(selection_sort(arr))
```
