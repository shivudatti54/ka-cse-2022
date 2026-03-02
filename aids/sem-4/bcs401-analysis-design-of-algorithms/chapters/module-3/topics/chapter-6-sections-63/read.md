# **Chapter 6: Analysis & Design of Algorithms**

# **Module: TRANSFORM-AND-CONQUER: Balanced Search Trees, Heaps and Heapsort**

## **Section 6.3: Analysis of Algorithms**

### 6.3.1: Introduction to Algorithm Analysis

Algorithm analysis is the process of measuring the complexity of an algorithm. It involves analyzing the number of steps an algorithm takes to complete a task, and expressing this in terms of the size of the input.

### 6.3.2: Big O Notation

Big O notation is a way of expressing the upper bound of an algorithm's complexity. It is defined as:

- O(f(n)) = a sequence of numbers such that there exists an N such that for all n > N, |f(n)/g(n)| <= c

In simpler terms, big O notation tells us the upper bound of an algorithm's complexity. It is usually represented as O(f(n)) where f(n) is the number of operations performed by the algorithm.

### 6.3.3: Types of Big O Notation

There are several types of big O notation, including:

- **O(1)**: Constant time complexity. This means that the algorithm's complexity is independent of the size of the input.
- **O(log n)**: Logarithmic time complexity. This means that the algorithm's complexity decreases as the size of the input increases.
- **O(n)**: Linear time complexity. This means that the algorithm's complexity increases linearly with the size of the input.
- **O(n log n)**: Linearithmic time complexity. This means that the algorithm's complexity increases with the square root of the size of the input.
- **O(n^2)**: Quadratic time complexity. This means that the algorithm's complexity increases rapidly with the size of the input.

### 6.3.4: Upper and Lower Bounds

Upper bounds are used to describe the maximum amount of time an algorithm can take to complete. Lower bounds are used to describe the minimum amount of time an algorithm must take to complete.

### 6.3.5: Example: Finding an Element in an Array

Suppose we want to find an element in an array of size n. We can use the following algorithm:

- Iterate through each element in the array
- Compare the element to the target element
- If they match, return the index of the element

The time complexity of this algorithm is O(n) because we have to check each element in the array.

### 6.3.6: Example: Binary Search

Suppose we want to find an element in a sorted array of size n. We can use the following algorithm:

- Find the middle element of the array
- Compare the middle element to the target element
- If they match, return the index of the element
- If the target element is less than the middle element, repeat the process with the left half of the array
- If the target element is greater than the middle element, repeat the process with the right half of the array

The time complexity of this algorithm is O(log n) because we are halving the size of the array with each iteration.

### 6.3.7: Analysis of an Algorithm

To analyze an algorithm, we need to count the number of operations performed by the algorithm and express this in terms of the size of the input.

Here are the steps to analyze an algorithm:

1.  Identify the input to the algorithm
2.  Identify the operations performed by the algorithm
3.  Count the number of operations performed by the algorithm
4.  Express the number of operations in terms of the size of the input
5.  Determine the upper bound of the algorithm's complexity

### 6.3.8: Example: Analysis of the Merge Sort Algorithm

Suppose we want to analyze the time complexity of the merge sort algorithm.

- Input: An array of size n
- Operations:
  - Divide the array into two halves
  - Recursively sort the two halves
  - Merge the two sorted halves
- Time complexity:
  - The time complexity of the merge sort algorithm is O(n log n) because we are dividing the array in half with each iteration and merging the two halves.

### 6.3.9: Conclusion

Algorithm analysis is an essential part of computer science. It helps us understand the complexity of an algorithm and determine whether it is efficient or not. By analyzing an algorithm, we can identify the upper and lower bounds of its complexity and determine the best way to implement it.
