# **Revision Notes for Chapter 6 (Sections 6.3) - Analysis & Design of Algorithms**

## **Important Definitions**

- **Time complexity** (Big O notation): a measure of an algorithm's performance, expressed in terms of the number of operations it performs.
- **Space complexity**: a measure of an algorithm's memory usage.

## **Key Concepts**

- **Upper and Lower Bounds**:
  - Upper bound: an overestimation of the algorithm's performance.
  - Lower bound: an underestimation of the algorithm's performance.
- **Big O Notation**: a way to describe the upper bound of an algorithm's performance.
- **Average Case Time Complexity**: the expected time taken by an algorithm to complete, assuming a random input.
- **Worst Case Time Complexity**: the maximum time taken by an algorithm to complete, assuming the worst possible input.

## **Important Formulas and Theorems**

- **Master Theorem**: a method for solving recurrence relations.
  - **T(n) = aT(n/b) + f(n)**
    - Case 1: T(n) = T(n/b) + f(n)
    - Case 2: T(n) = aT(n/b)
    - Case 3: T(n) = f(n)
- **Big O Notation Rules**:
  - O(1) = constant time complexity
  - O(log n) = logarithmic time complexity
  - O(n) = linear time complexity
  - O(n log n) = linearithmic time complexity
  - O(n^2) = quadratic time complexity
  - O(2^n) = exponential time complexity
  - O(n!) = factorial time complexity

## **Important Algorithms**

- **Binary Search**: a search algorithm that finds an element in a sorted array.
- **Merge Sort**: a sorting algorithm that divides the array into smaller chunks and sorts them recursively.

## **Key Takeaways**

- Understand the concept of time complexity and its importance in algorithm design.
- Learn how to analyze the time complexity of an algorithm using the Master Theorem.
- Familiarize yourself with Big O notation rules and how to apply them to real-world problems.
