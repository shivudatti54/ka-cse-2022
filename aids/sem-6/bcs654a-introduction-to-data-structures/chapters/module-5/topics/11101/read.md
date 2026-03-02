# **Introduction to Sorting Algorithms**

### Overview of Sorting Algorithms

Sorting algorithms are a crucial part of computer science, used to arrange data in a specific order. The goal of a sorting algorithm is to sort an unsorted list of elements into a sorted list, making it easier to access and analyze the data.

### Types of Sorting Algorithms

There are several types of sorting algorithms, each with its own strengths and weaknesses. The most common sorting algorithms include:

- **Bubble Sort**: Simple, easy to implement, but inefficient for large datasets.
- **Selection Sort**: Easy to implement, but inefficient for large datasets.
- **Insertion Sort**: Efficient for small datasets, but can be slow for large datasets.
- **Merge Sort**: Efficient for large datasets, but requires extra memory.
- **Quick Sort**: Fast and efficient, but can be slow for nearly sorted data.

### 11.10.1: Bubble Sort

**Definition:** Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.

**How Bubble Sort Works:**

1.  Start at the beginning of the list.
2.  Compare the first two elements. If they are in the wrong order, swap them.
3.  Move to the next two elements and repeat the comparison.
4.  Continue this process until the end of the list.
5.  Repeat steps 1-4 until no more swaps are needed.

**Example:**

Suppose we have the following list:

`[5, 2, 8, 3, 1, 6, 4]`

We start at the beginning of the list and compare the first two elements, `5` and `2`. Since `2` is less than `5`, we swap them.

`[2, 5, 8, 3, 1, 6, 4]`

We repeat this process until we reach the end of the list.

**Code Example (Python):**

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Test the function
arr = [5, 2, 8, 3, 1, 6, 4]
print(bubble_sort(arr))
```

**Time Complexity:** O(n^2)

**Space Complexity:** O(1)

### Conclusion

Bubble Sort is a simple sorting algorithm that can be effective for small datasets. However, its inefficiency for large datasets makes it less desirable for many applications.
