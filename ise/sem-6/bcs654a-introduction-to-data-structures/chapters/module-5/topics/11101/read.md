**11.10.1 Introduction to Sorting Algorithms**

**What is Sorting?**

Sorting is the process of arranging elements in a specific order, usually in ascending or descending order, based on certain criteria. It is an essential operation in data structures and is used in various applications, such as database management, file management, and data analysis.

**Types of Sorting Algorithms**

There are several types of sorting algorithms, including:

- **Comparison Sorts**: These algorithms compare elements and swap them if they are in the wrong order.
- **Non-Comparison Sorts**: These algorithms do not compare elements and instead use mathematical formulas to sort the data.
- **In-Place Sorts**: These algorithms sort the data in place, without requiring extra memory.

**Sorting Algorithms**

### 1. Bubble Sort

Bubble sort is a simple comparison sort that works by repeatedly swapping the adjacent elements if they are in the wrong order.

**How Bubble Sort Works**

1. Start from the first element of the array.
2. Compare the current element with the next element.
3. If the current element is greater than the next element, swap them.
4. Repeat steps 2-3 until the end of the array is reached.
5. Repeat steps 1-4 until no swaps are needed, indicating that the array is sorted.

**Example in Python**

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
print("Sorted array:", bubble_sort(arr))
```

### 2. Selection Sort

Selection sort is a comparison sort that works by selecting the smallest (or largest) element from the unsorted part of the array and swapping it with the first element of the unsorted part.

**How Selection Sort Works**

1. Start from the first element of the array.
2. Find the smallest (or largest) element in the unsorted part of the array.
3. Swap the smallest (or largest) element with the first element of the unsorted part.
4. Repeat steps 1-3 until the end of the array is reached.

**Example in Python**

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

arr = [64, 34, 25, 12, 22, 11, 90]
print("Sorted array:", selection_sort(arr))
```

### 3. Insertion Sort

Insertion sort is a comparison sort that works by inserting each element into its proper position in the already sorted part of the array.

**How Insertion Sort Works**

1. Start from the second element of the array.
2. Compare the current element with the elements before it.
3. Insert the current element into its proper position.
4. Repeat steps 1-3 until the end of the array is reached.

**Example in Python**

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
print("Sorted array:", insertion_sort(arr))
```

**Key Concepts**

- **Time Complexity**: The time taken to sort the array, usually expressed in Big O notation (e.g., O(n^2), O(n log n)).
- **Space Complexity**: The extra memory required to sort the array, usually expressed in Big O notation (e.g., O(1), O(n)).
- **Stability**: The property of a sorting algorithm to preserve the relative order of equal elements.

**Conclusion**

Sorting is an essential operation in data structures, and there are several sorting algorithms available, each with its own strengths and weaknesses. Bubble sort, selection sort, and insertion sort are some of the most common sorting algorithms, each with its own implementation and use cases. Understanding the time and space complexity, stability, and key concepts of these algorithms is crucial for selecting the right algorithm for a particular problem.
