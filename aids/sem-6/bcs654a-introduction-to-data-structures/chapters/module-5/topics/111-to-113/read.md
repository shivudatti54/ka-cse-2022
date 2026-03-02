# **11.1: Introduction to Sorting**

Sorting is the process of rearranging elements in a data structure to arrange them in a specific order, such as ascending or descending order. This topic provides an introduction to sorting and presents three basic sorting algorithms.

### Key Concepts

- **Sorting Algorithms**: Algorithms used to sort data in a specific order.
- **Data Structure**: A collection of elements, each with its own value or reference to another element.
- **Ordering**: The arrangement of elements in a data structure based on their values.

### Types of Sorting

There are two primary types of sorting:

- **Comparative Sorting**: This type of sorting involves comparing elements to determine their order.
- **Non-Comparative Sorting**: This type of sorting involves grouping elements based on their properties.

### Why is Sorting Important?

Sorting is essential in various applications, such as:

- **Database Management Systems**: Sorting data in databases is crucial for efficient data retrieval.
- **Data Analysis**: Sorting data is necessary for data analysis and visualization.
- **Algorithm Design**: Sorting is a fundamental component of many algorithms.

# **11.2: Bubble Sort**

Bubble sort is a simple sorting algorithm that works by repeatedly iterating through a data structure and swapping adjacent elements if they are in the wrong order.

### How Bubble Sort Works

1.  Start at the beginning of the data structure.
2.  Compare the current element with the next element.
3.  If the current element is greater than the next element, swap them.
4.  Repeat steps 2-3 until the end of the data structure.
5.  Repeat the process until no more swaps are necessary.

### Time Complexity of Bubble Sort

- Best-case time complexity: O(n)
- Average-case time complexity: O(n^2)
- Worst-case time complexity: O(n^2)

### Example Code (Python)

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
```

# **11.3: Selection Sort**

Selection sort is a sorting algorithm that works by repeatedly finding the minimum element from the unsorted part of the data structure and swapping it with the first unsorted element.

### How Selection Sort Works

1.  Start at the beginning of the data structure.
2.  Find the minimum element from the unsorted part of the data structure.
3.  Swap the minimum element with the first unsorted element.
4.  Repeat steps 2-3 until the end of the data structure.
5.  Repeat the process until no more swaps are necessary.

### Time Complexity of Selection Sort

- Best-case time complexity: O(n^2)
- Average-case time complexity: O(n^2)
- Worst-case time complexity: O(n^2)

### Example Code (Python)

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
```
