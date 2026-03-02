# **Textbook 2: Ch**

## **Introduction to Data Structures**

## **What are Data Structures?**

- Data structures are the way we organize and store data in a computer program.
- They provide a way to efficiently store and retrieve data, making it easier to manipulate and analyze the data.
- Data structures can be thought of as the "blueprints" or "skeletons" of the data.

## **Types of Data Structures**

- **Sequential Data Structures**: These data structures store data in a linear sequence, such as arrays and linked lists.
- **Non-Sequential Data Structures**: These data structures store data in a non-linear sequence, such as trees and graphs.

## **Sorting: Introduction**

## **What is Sorting?**

- Sorting is the process of arranging data in a specific order, such as ascending or descending.
- Sorting can be used to organize data, make it easier to search and find specific data, and improve the efficiency of algorithms.

## **Why is Sorting Important?**

- Sorting is essential in many applications, such as data analysis, machine learning, and database management.
- Sorting can help to:
  - Reduce the time complexity of algorithms
  - Improve the efficiency of data retrieval
  - Facilitate data analysis and visualization

## **Sorting Algorithms**

### 1. Bubble Sort

## **What is Bubble Sort?**

- Bubble sort is a simple sorting algorithm that works by repeatedly swapping adjacent elements if they are in the wrong order.
- Bubble sort has a time complexity of O(n^2), making it less efficient than other sorting algorithms for large datasets.

## **How Does Bubble Sort Work?**

1.  Start with the first element of the array.
2.  Compare it with the next element.
3.  If the elements are in the wrong order, swap them.
4.  Repeat steps 2-3 until the end of the array is reached.
5.  Repeat the process until no more swaps are needed.

## **Example: Bubble Sort**

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(arr))
```

### 2. Selection Sort

## **What is Selection Sort?**

- Selection sort is a sorting algorithm that works by selecting the smallest (or largest) element from the unsorted portion of the array and moving it to the beginning (or end) of the array.
- Selection sort has a time complexity of O(n^2), making it less efficient than other sorting algorithms for large datasets.

## **How Does Selection Sort Work?**

1.  Start with the first element of the array.
2.  Find the smallest (or largest) element in the unsorted portion of the array.
3.  Swap the first element with the smallest (or largest) element.
4.  Repeat steps 2-3 until the end of the array is reached.

## **Example: Selection Sort**

```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
print(selection_sort(arr))
```

### 3. Insertion Sort

## **What is Insertion Sort?**

- Insertion sort is a sorting algorithm that works by iterating through the array one element at a time, inserting each element into its proper position in the sorted portion of the array.
- Insertion sort has a time complexity of O(n^2), making it less efficient than other sorting algorithms for large datasets.

## **How Does Insertion Sort Work?**

1.  Start with the first element of the array.
2.  Compare it with the elements in the sorted portion of the array.
3.  Insert the element into its proper position in the sorted portion.
4.  Repeat steps 2-3 until the end of the array is reached.

## **Example: Insertion Sort**

```python
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
print(insertion_sort(arr))
```

### Key Concepts

- **Time complexity**: A measure of the amount of time an algorithm takes to complete, usually expressed as a function of the size of the input.
- **Space complexity**: A measure of the amount of memory an algorithm uses, usually expressed as a function of the size of the input.
- **Big O notation**: A way of expressing the upper bound of an algorithm's time or space complexity.
- **Algorithm**: A set of instructions that solves a specific problem.

### Practice Problems

- Implement the sorting algorithms using Python.
- Compare the performance of the different sorting algorithms for large datasets.
- Discuss the trade-offs between the different sorting algorithms.
