# **INTRODUCTION TO DATA STRUCTURES**

## **Sorting: Introduction, Bubble Sort, Selection Sort, Insertion Sort**

## **Introduction**

Sorting is an essential operation in computer science that involves arranging elements of a collection in a specific order. It is a fundamental technique used in various applications, including data processing, searching, and database management. In this module, we will explore the basics of sorting, as well as three common algorithms: Bubble Sort, Selection Sort, and Insertion Sort.

### What is Sorting?

Sorting is the process of arranging elements of a collection in a specific order, such as ascending or descending order. The goal of sorting is to optimize the performance of subsequent operations, such as searching or inserting elements, by reducing the complexity of the data.

### Types of Sorting

There are several types of sorting algorithms, including:

- **Comparison-based sorting**: This type of sorting algorithm compares elements and swaps them if they are in the wrong order.
- **Non-comparison-based sorting**: This type of sorting algorithm uses mathematical formulas or other techniques to sort elements without comparing them.

### Importance of Sorting

Sorting is an essential operation in various applications, including:

- **Data processing**: Sorting is used to process large datasets efficiently.
- **Searching**: Sorting is used to improve the efficiency of search algorithms.
- **Database management**: Sorting is used to manage large datasets in databases.

### Algorithms

In this module, we will explore three common sorting algorithms:

### Bubble Sort

**Bubble Sort** is a simple sorting algorithm that works by repeatedly iterating through the collection and swapping adjacent elements if they are in the wrong order.

**How Bubble Sort Works**

1. Start at the beginning of the collection.
2. Compare the current element with the next element.
3. If the current element is greater than the next element, swap them.
4. Repeat steps 2-3 until the end of the collection.
5. Repeat the process until no more swaps are needed.

**Example**

Suppose we have the following collection: `[5, 2, 8, 3, 1]`

1. Start at the beginning of the collection: `[5, 2, 8, 3, 1]`
2. Compare the first element (5) with the second element (2). Swap them: `[2, 5, 8, 3, 1]`
3. Compare the second element (2) with the third element (8). No swap: `[2, 5, 8, 3, 1]`
4. Repeat steps 2-3 until the end of the collection: `[1, 2, 3, 5, 8]`

### Selection Sort

**Selection Sort** is a simple sorting algorithm that works by repeatedly finding the minimum element in the unsorted portion of the collection and swapping it with the first element of the unsorted portion.

**How Selection Sort Works**

1. Start at the beginning of the collection.
2. Find the minimum element in the unsorted portion of the collection.
3. Swap the minimum element with the first element of the unsorted portion.
4. Repeat steps 1-3 until the end of the collection.

**Example**

Suppose we have the following collection: `[5, 2, 8, 3, 1]`

1. Start at the beginning of the collection: `[5, 2, 8, 3, 1]`
2. Find the minimum element (1) in the unsorted portion of the collection: `[5, 2, 8, 3, 1]`
3. Swap the minimum element with the first element (5): `[1, 2, 8, 3, 5]`
4. Repeat steps 1-3 until the end of the collection: `[1, 2, 3, 5, 8]`

### Insertion Sort

**Insertion Sort** is a simple sorting algorithm that works by iterating through the collection one element at a time and inserting each element into its correct position in the sorted portion of the collection.

**How Insertion Sort Works**

1. Start at the beginning of the collection.
2. Iterate through the collection one element at a time.
3. Insert each element into its correct position in the sorted portion of the collection.
4. Repeat steps 1-3 until the end of the collection.

**Example**

Suppose we have the following collection: `[5, 2, 8, 3, 1]`

1. Start at the beginning of the collection: `[5, 2, 8, 3, 1]`
2. Insert the first element (5) into its correct position: `[5, 2, 8, 3, 1]`
3. Insert the second element (2) into its correct position: `[2, 5, 8, 3, 1]`
4. Insert the third element (8) into its correct position: `[2, 5, 8, 3, 1]`
5. Insert the fourth element (3) into its correct position: `[2, 3, 5, 8, 1]`
6. Insert the fifth element (1) into its correct position: `[1, 2, 3, 5, 8]`

### Key Concepts

- **Bubble Sort**: a simple sorting algorithm that works by repeatedly iterating through the collection and swapping adjacent elements if they are in the wrong order.
- **Selection Sort**: a simple sorting algorithm that works by repeatedly finding the minimum element in the unsorted portion of the collection and swapping it with the first element of the unsorted portion.
- **Insertion Sort**: a simple sorting algorithm that works by iterating through the collection one element at a time and inserting each element into its correct position in the sorted portion of the collection.
- **Comparison-based sorting**: a type of sorting algorithm that compares elements and swaps them if they are in the wrong order.
- **Non-comparison-based sorting**: a type of sorting algorithm that uses mathematical formulas or other techniques to sort elements without comparing them.
