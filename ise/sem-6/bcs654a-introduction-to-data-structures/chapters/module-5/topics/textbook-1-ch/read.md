# **INTRODUCTION TO DATA STRUCTURES: SORTING**

**Module: Sorting: Introduction, Bubble Sort, Selection Sort, Insertion Sort**

**Textbook 1: Ch**

## **Introduction**

Sorting is a fundamental operation in computer science that involves arranging a set of elements in a specific order, such as ascending or descending order. This topic will introduce the concept of sorting, its importance, and the basic algorithms used for sorting.

## **Why Sorting?**

Sorting is essential in many applications, including:

- Data analysis and visualization
- Database management
- Algorithmic complexity analysis
- Resource allocation

## **Types of Sorting**

There are several types of sorting algorithms, including:

- **Comparison-based sorting**: This type of sorting algorithms compare elements to determine their order.
- **Non-comparison-based sorting**: This type of sorting algorithms use a different approach to sort data, such as counting sort or radix sort.

## **Sorting Algorithms**

### 1. Bubble Sort

**Definition:** Bubble sort is a simple sorting algorithm that works by repeatedly swapping adjacent elements if they are in the wrong order.

**How it works:**

1. Start from the first element of the array.
2. Compare the current element with the next element.
3. If the current element is greater than the next element, swap them.
4. Repeat steps 2-3 until the end of the array is reached.
5. Repeat the process until no more swaps are needed.

**Example:**

Suppose we have an array of integers: `[5, 2, 8, 3, 1]`.

1. Start with the first element (5) and compare it with the next element (2). Swap them to get `[2, 5, 8, 3, 1]`.
2. Repeat the process with the next element (8) and the next element (3). Swap them to get `[2, 5, 3, 8, 1]`.
3. Repeat the process until no more swaps are needed. The final sorted array is `[1, 2, 3, 5, 8]`.

**Time Complexity:** O(n^2)

**Space Complexity:** O(1)

### 2. Selection Sort

**Definition:** Selection sort is a sorting algorithm that works by repeatedly finding the minimum element from the unsorted part of the array and swapping it with the first element of the unsorted part.

**How it works:**

1. Start from the first element of the array.
2. Find the minimum element from the unsorted part of the array.
3. Swap the minimum element with the first element of the unsorted part.
4. Repeat steps 2-3 until the end of the array is reached.

**Example:**

Suppose we have an array of integers: `[5, 2, 8, 3, 1]`.

1. Start with the first element (5) and find the minimum element from the rest of the array (2). Swap them to get `[2, 5, 8, 3, 1]`.
2. Repeat the process with the next element (8) and find the minimum element from the rest of the array (3). Swap them to get `[2, 3, 5, 8, 1]`.
3. Repeat the process until no more swaps are needed. The final sorted array is `[1, 2, 3, 5, 8]`.

**Time Complexity:** O(n^2)

**Space Complexity:** O(1)

### 3. Insertion Sort

**Definition:** Insertion sort is a sorting algorithm that works by repeatedly inserting elements into the sorted part of the array.

**How it works:**

1. Start from the first element of the array.
2. Compare the current element with the previous elements.
3. If the current element is smaller than the previous elements, insert it into the correct position.
4. Repeat steps 2-3 until the end of the array is reached.

**Example:**

Suppose we have an array of integers: `[5, 2, 8, 3, 1]`.

1. Start with the first element (5) and compare it with the next element (2). Insert it into the correct position to get `[2, 5, 8, 3, 1]`.
2. Repeat the process with the next element (8) and insert it into the correct position to get `[2, 5, 8, 3, 1]`.
3. Repeat the process until no more elements are inserted. The final sorted array is `[1, 2, 3, 5, 8]`.

**Time Complexity:** O(n^2)

**Space Complexity:** O(1)

## **Conclusion**

Sorting is a fundamental operation in computer science that involves arranging a set of elements in a specific order. The three sorting algorithms discussed in this topic, bubble sort, selection sort, and insertion sort, have their own strengths and weaknesses. Understanding the time and space complexity of these algorithms is essential for choosing the right sorting algorithm for a particular problem.
