# Chapter 2: Analysis & Design of Algorithms

==========================================

## 2.1 Introduction to Algorithm Analysis

---

### Definition of Algorithm Analysis

Algorithm analysis is the process of determining the amount of time or space an algorithm requires to complete, usually in terms of its running time or memory usage.

### Importance of Algorithm Analysis

Algorithm analysis is essential in software development as it helps in:

- Evaluating the efficiency of an algorithm
- Comparing different algorithms for solving the same problem
- Predicting the performance of an algorithm on different inputs
- Identifying bottlenecks in an algorithm

### Types of Algorithm Analysis

---

There are two primary types of algorithm analysis:

- **Time Complexity Analysis**: focuses on the amount of time an algorithm takes to complete as a function of the size of the input
- **Space Complexity Analysis**: focuses on the amount of memory an algorithm uses as a function of the size of the input

### Measuring Algorithm Performance

---

Algorithm performance can be measured using several metrics:

- **Running Time**: the time an algorithm takes to complete
- **Space Complexity**: the amount of memory an algorithm uses
- **Complexity**: a mathematical representation of an algorithm's performance

### Big O Notation

---

Big O notation is a mathematical notation used to describe the upper bound of an algorithm's complexity. It is commonly used to express the time or space complexity of an algorithm.

### Examples of Big O Notation

- O(1) - constant time complexity
- O(log n) - logarithmic time complexity
- O(n) - linear time complexity
- O(n log n) - linearithmic time complexity
- O(n^2) - quadratic time complexity
- O(2^n) - exponential time complexity

### Key Concepts

- **Asymptotic Notation**: a mathematical notation used to describe the behavior of an algorithm as the input size approaches infinity
- **Upper Bound**: the maximum amount of time or space an algorithm can take to complete
- **Lower Bound**: the minimum amount of time or space an algorithm must take to complete

### Example: Analyzing the Time Complexity of a Sorting Algorithm

Suppose we have a sorting algorithm that takes O(n^2) time to complete. This means that the running time of the algorithm grows quadratically with the size of the input.

| Input Size (n) | Time Complexity (O(n^2)) |
| -------------- | ------------------------ |
| 10             | O(100)                   |
| 20             | O(400)                   |
| 30             | O(900)                   |

As we can see, the time complexity of the algorithm grows rapidly with the size of the input.

### Exercises

1.  Analyze the time complexity of the following algorithm:
    ```python
    def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
    for j in range(n - 1):
    if arr[j] > arr[j + 1]:
    arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

````
2.  What is the time complexity of the following algorithm:
    ```python
def recursive_factorial(n):
    if n == 0:
        return 1
    else:
        return n * recursive_factorial(n - 1)
````

3.  How would you analyze the time complexity of the following algorithm:
    ```python
    def merge_sort(arr):
    if len(arr) <= 1:
    return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)

def merge(left, right):
merged = []
left_index = 0
right_index = 0
while left_index < len(left) and right_index < len(right):
if left[left_index] <= right[right_index]:
merged.append(left[left_index])
left_index += 1
else:
merged.append(right[right_index])
right_index += 1
merged.extend(left[left_index:])
merged.extend(right[right_index:])
return merged

````
4.  What is the space complexity of the following algorithm:
    ```python
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
````
