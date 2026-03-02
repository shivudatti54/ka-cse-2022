# **BRUTE FORCE APPROACHES: Selection Sort and Bubble Sort**

## **Introduction**

In algorithmic problem solving, a brute force approach is a method where the algorithm tries all possible solutions to a problem. This approach is typically used when the problem has a small number of possible solutions or when the problem is relatively simple. In this section, we will explore two popular brute force algorithms: Selection Sort and Bubble Sort.

## **What is a Brute Force Algorithm?**

A brute force algorithm is an algorithm that uses a trial-and-error approach to solve a problem. It tries all possible solutions to a problem until it finds the correct one. Brute force algorithms are often used when the problem has a small number of possible solutions or when the problem is relatively simple.

## **Selection Sort**

### Definition

Selection Sort is a brute force algorithm that sorts an array of elements by repeatedly finding the minimum element from the unsorted part of the array and swapping it with the first unsorted element.

### How it Works

Here is a step-by-step explanation of how Selection Sort works:

1.  Start at the beginning of the array.
2.  Find the minimum element in the unsorted part of the array.
3.  Swap the minimum element with the first unsorted element.
4.  Repeat steps 1-3 until the entire array is sorted.

### Example

Suppose we have an array of integers: `[5, 2, 8, 3, 1, 6, 4]`.

1.  Start at the beginning of the array: `[5, 2, 8, 3, 1, 6, 4]`.
2.  Find the minimum element in the unsorted part of the array ( `[2, 3, 1, 6, 4]` ): `2`.
3.  Swap the minimum element with the first unsorted element: `[2, 8, 3, 1, 6, 4]`.
4.  Repeat steps 1-3 until the entire array is sorted: `[1, 2, 3, 4, 5, 6, 8]`.

### Code

Here is an example implementation of Selection Sort in Python:

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

# Test the function
arr = [5, 2, 8, 3, 1, 6, 4]
print(selection_sort(arr))  # Output: [1, 2, 3, 4, 5, 6, 8]
```

## **Bubble Sort**

### Definition

Bubble Sort is a brute force algorithm that sorts an array of elements by repeatedly swapping adjacent elements if they are in the wrong order.

### How it Works

Here is a step-by-step explanation of how Bubble Sort works:

1.  Start at the beginning of the array.
2.  Compare the first two elements of the array.
3.  If the elements are in the wrong order, swap them.
4.  Repeat steps 1-3 until the entire array is sorted.

### Example

Suppose we have an array of integers: `[5, 2, 8, 3, 1, 6, 4]`.

1.  Start at the beginning of the array: `[5, 2, 8, 3, 1, 6, 4]`.
2.  Compare the first two elements: `5` and `2`. They are in the wrong order, so swap them: `[2, 5, 8, 3, 1, 6, 4]`.
3.  Repeat steps 1-2 until the entire array is sorted: `[1, 2, 3, 4, 5, 6, 8]`.

### Code

Here is an example implementation of Bubble Sort in Python:

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Test the function
arr = [5, 2, 8, 3, 1, 6, 4]
print(bubble_sort(arr))  # Output: [1, 2, 3, 4, 5, 6, 8]
```

## **Key Concepts**

- Brute force algorithms try all possible solutions to a problem.
- Selection Sort and Bubble Sort are two popular brute force algorithms for sorting arrays.
- Selection Sort finds the minimum element in the unsorted part of the array and swaps it with the first unsorted element.
- Bubble Sort repeatedly compares adjacent elements and swaps them if they are in the wrong order.
