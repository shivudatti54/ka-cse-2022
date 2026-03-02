# Introduction to Sorting: 11.1 to 11.3

## 11.1: What is Sorting?

Sorting is the process of arranging a set of elements in a specific order, such as ascending or descending order. It is a fundamental operation in computer science and is used in a wide range of applications, including databases, file systems, and web search engines.

### Types of Sorting

There are several types of sorting algorithms, including:

- **Comparative Sorting**: This is the most common type of sorting, where each element is compared to others and rearranged accordingly.
- **Non-Comparative Sorting**: This type of sorting uses a different approach, such as counting or dynamic programming, to sort the elements.
- **In-Place Sorting**: This type of sorting does not require any additional storage, as it sorts the elements in place.
- **External Sorting**: This type of sorting requires additional storage, as it sorts large datasets that do not fit in memory.

### Need for Sorting

Sorting is essential in many applications, including:

- **Database Query Optimization**: Sorting is used to optimize database queries by rearranging the results in a specific order.
- **File System Organization**: Sorting is used to organize files in a file system, making it easier to find and retrieve files.
- **Web Search Engine**: Sorting is used to rank web pages in a search engine, making it easier for users to find what they are looking for.

## 11.2: Bubble Sort

Bubble sort is a simple sorting algorithm that works by repeatedly iterating through the elements and swapping adjacent elements if they are in the wrong order.

### How Bubble Sort Works

1.  Start at the beginning of the array.
2.  Compare the first two elements. If they are in the wrong order, swap them.
3.  Move to the next two elements and repeat the process.
4.  Continue this process until the end of the array is reached.
5.  Repeat the process until no more swaps are needed.

### Example of Bubble Sort

Suppose we have the following array:

```
[5, 2, 8, 1, 9]
```

After running bubble sort on this array, we get:

```
[1, 2, 5, 8, 9]
```

### Code for Bubble Sort

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
```

## 11.3: Selection Sort

Selection sort is another simple sorting algorithm that works by repeatedly finding the minimum element from the unsorted portion of the array and swapping it with the first element of the unsorted portion.

### How Selection Sort Works

1.  Start at the beginning of the array.
2.  Find the minimum element in the unsorted portion of the array.
3.  Swap the minimum element with the first element of the unsorted portion.
4.  Move to the next element and repeat the process.
5.  Continue this process until the end of the array is reached.

### Example of Selection Sort

Suppose we have the following array:

```
[5, 2, 8, 1, 9]
```

After running selection sort on this array, we get:

```
[1, 2, 5, 8, 9]
```

### Code for Selection Sort

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
```

## Key Concepts

- **Comparative Sorting**: This is the most common type of sorting, where each element is compared to others and rearranged accordingly.
- **Bubble Sort**: A simple sorting algorithm that works by repeatedly iterating through the elements and swapping adjacent elements if they are in the wrong order.
- **Selection Sort**: A simple sorting algorithm that works by repeatedly finding the minimum element from the unsorted portion of the array and swapping it with the first element of the unsorted portion.
- **In-Place Sorting**: This type of sorting does not require any additional storage, as it sorts the elements in place.
