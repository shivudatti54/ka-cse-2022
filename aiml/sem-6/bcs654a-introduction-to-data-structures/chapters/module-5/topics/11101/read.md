# **11.10.1 Introduction to Sorting Algorithms**

### What is Sorting?

Sorting is the process of arranging elements in a specific order, usually in ascending or descending order, within a collection of data. It is a fundamental operation in computer science and is used extensively in various applications, such as databases, file systems, web browsers, and more.

### Types of Sorting Algorithms

There are several sorting algorithms, each with its own strengths and weaknesses. The three sorting algorithms covered in this module are:

- Bubble Sort
- Selection Sort
- Insertion Sort

### Bubble Sort

Bubble sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.

**How Bubble Sort Works:**

1.  Start at the beginning of the list.
2.  Compare the first two elements. If they are in the wrong order, swap them.
3.  Move to the next pair of elements and repeat the comparison and swap process.
4.  Continue this process until the end of the list is reached.
5.  Repeat the process until no more swaps are needed, indicating that the list is sorted.

**Example of Bubble Sort:**

Suppose we have the following list of integers: [5, 2, 8, 3, 1, 6, 4]

1.  Start at the beginning of the list: [5, 2, 8, 3, 1, 6, 4]
2.  Compare the first two elements: 5 and 2. Since 2 is less than 5, no swap is needed.
3.  Move to the next pair of elements: 2 and 8. Since 2 is less than 8, no swap is needed.
4.  Move to the next pair of elements: 8 and 3. Since 3 is less than 8, swap them: [5, 2, 3, 8, 1, 6, 4]
5.  Repeat the process until the end of the list is reached: [1, 2, 3, 4, 5, 6, 8]

**Time Complexity of Bubble Sort:**

The time complexity of bubble sort is O(n^2), where n is the number of elements in the list. This is because the algorithm repeatedly compares each pair of elements and swaps them if necessary, resulting in a quadratic time complexity.

### Selection Sort

Selection sort is another simple sorting algorithm that works by repeatedly finding the minimum element from the unsorted part of the list and swapping it with the first element of the unsorted part.

**How Selection Sort Works:**

1.  Start at the beginning of the list.
2.  Find the minimum element in the unsorted part of the list.
3.  Swap the minimum element with the first element of the unsorted part.
4.  Move to the next element in the list and repeat the process.
5.  Continue this process until the end of the list is reached.

**Example of Selection Sort:**

Suppose we have the following list of integers: [5, 2, 8, 3, 1, 6, 4]

1.  Start at the beginning of the list: [5, 2, 8, 3, 1, 6, 4]
2.  Find the minimum element in the unsorted part of the list: 1.
3.  Swap the minimum element with the first element of the unsorted part: [1, 2, 8, 3, 5, 6, 4]
4.  Repeat the process until the end of the list is reached: [1, 2, 3, 4, 5, 6, 8]

**Time Complexity of Selection Sort:**

The time complexity of selection sort is O(n^2), where n is the number of elements in the list. This is because the algorithm repeatedly finds the minimum element and swaps it with the first element of the unsorted part, resulting in a quadratic time complexity.

### Insertion Sort

Insertion sort is a simple sorting algorithm that works by iterating through the list one element at a time, inserting each element into its proper position within the previously sorted part of the list.

**How Insertion Sort Works:**

1.  Start at the beginning of the list.
2.  Iterate through the list one element at a time.
3.  For each element, compare it with the elements in the previously sorted part of the list.
4.  Insert the element into its proper position within the previously sorted part of the list.
5.  Continue this process until the end of the list is reached.

**Example of Insertion Sort:**

Suppose we have the following list of integers: [5, 2, 8, 3, 1, 6, 4]

1.  Start at the beginning of the list: [5, 2, 8, 3, 1, 6, 4]
2.  Iterate through the list one element at a time:
    - 5: Compare with 2, 8, 3, 1, 6, 4. Insert at the beginning: [5, 2, 8, 3, 1, 6, 4]
    - 2: Compare with 8, 3, 1, 6, 4. Insert at the beginning: [2, 5, 8, 3, 1, 6, 4]
    - 8: Compare with 3, 1, 6, 4. Insert at the beginning: [2, 5, 8, 3, 1, 6, 4]
    - 3: Compare with 1, 6, 4. Insert at the beginning: [2, 5, 8, 3, 1, 6, 4]
    - 1: Compare with 6, 4. Insert at the beginning: [2, 5, 8, 3, 1, 6, 4]
    - 6: Compare with 4. Insert at the beginning: [2, 5, 8, 3, 1, 6, 4]
    - 4: Insert at the beginning: [2, 5, 8, 3, 1, 6, 4]
3.  Continue this process until the end of the list is reached: [2, 3, 4, 5, 1, 6, 8]

**Time Complexity of Insertion Sort:**

The time complexity of insertion sort is O(n^2), where n is the number of elements in the list. This is because the algorithm repeatedly compares each element with the elements in the previously sorted part of the list, resulting in a quadratic time complexity.

### Key Concepts

- **Time complexity:** A measure of the amount of time an algorithm takes to complete, typically expressed as a function of the size of the input.
- **Space complexity:** A measure of the amount of memory an algorithm uses, typically expressed as a function of the size of the input.
- **Sorting algorithms:** A set of algorithms designed to sort data in a specific order.
- **Bubble sort:** A simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order.
- **Selection sort:** A simple sorting algorithm that works by repeatedly finding the minimum element from the unsorted part of the list and swapping it with the first element of the unsorted part.
- **Insertion sort:** A simple sorting algorithm that works by iterating through the list one element at a time, inserting each element into its proper position within the previously sorted part of the list.
