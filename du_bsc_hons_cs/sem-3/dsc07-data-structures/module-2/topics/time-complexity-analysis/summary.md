# Time Complexity Analysis
**Data Structures | BSc (Hons) Computer Science - Delhi University (NEP 2024 UGCF)**

## Introduction

Time Complexity analysis measures the amount of time an algorithm takes to complete as a function of input size. It is a critical concept in data structures that helps evaluate algorithm efficiency and scalability, forming an essential part of the Delhi University Computer Science syllabus.

## Key Concepts

### Asymptotic Notations
Used to describe the growth rate of functions:
- **Big O (O)**: Upper bound - worst-case scenario
- **Big Omega (Ω)**: Lower bound - best-case scenario
- **Big Theta (Θ)**: Tight bound - average case

### Types of Time Complexities (Ascending Order)
- **O(1)** – Constant Time: Array access, hash table lookup
- **O(log n)** – Logarithmic Time: Binary search, balanced BST operations
- **O(n)** – Linear Time: Linear search, traversing an array
- **O(n log n)** – Linearithmic Time: Merge sort, heap sort, quick sort (average)
- **O(n²)** – Quadratic Time: Bubble sort, insertion sort, nested loops
- **O(2ⁿ)** – Exponential Time: Recursive Fibonacci, subset generation
- **O(n!)** – Factorial Time: Permutations, traveling salesman (brute force)

### Important Points for Exam
- **Space-Time Tradeoff**: Reducing time complexity often requires more memory
- **Best, Average, Worst Case**: Always specify which case you're analyzing
- **Amortized Analysis**: Average performance over sequence of operations

### Common Formulae
- Sum of first n natural numbers: **n(n+1)/2 = O(n²)**
- Binary search recurrence: **T(n) = T(n/2) + O(1) = O(log n)**
- Merge sort recurrence: **T(n) = 2T(n/2) + O(n) = O(n log n)**

### Analyzing Code Snippets
1. Identify loops (for, while)
2. Count nested loop levels
3. Consider recursive calls
4. Ignore constants and lower-order terms

## Conclusion

Time Complexity Analysis is fundamental to algorithm design and optimization. Understanding Big O notation and various complexity classes enables efficient problem-solving and is crucial for succeeding in data structures examinations and practical programming interviews. Mastery of this topic is essential for every computer science graduate as prescribed in the DU NEP 2024 syllabus.