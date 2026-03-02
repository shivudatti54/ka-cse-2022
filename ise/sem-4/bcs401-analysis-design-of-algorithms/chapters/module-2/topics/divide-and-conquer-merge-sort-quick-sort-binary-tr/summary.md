# **DIVIDE AND CONQUER: Merge Sort, Quick Sort, Binary Tree Traversals, Multiplication of Large Integers and Strassen’s Matrix Multiplication**

### Overview

- Divide and Conquer is an algorithmic paradigm that solves problems by breaking them down into smaller sub-problems, solving each sub-problem, and combining the solutions to solve the original problem.

### Merge Sort

---

- **Definition:** Divide the array into two halves, recursively sort each half, and merge the two sorted halves.
- **Time Complexity:** O(n log n)
- **Space Complexity:** O(n)
- **Formula:** Merge sort can be represented as:
  \[ M(a, b) = \begin{cases} a & \text{if } b \leq a \\ b & \text{if } b > a \end{cases} \]
- **Algorithm:**
  1. If the array has only one element, return the array.
  2. Divide the array into two halves.
  3. Recursively sort each half.
  4. Merge the two sorted halves.

### Quick Sort

---

- **Definition:** Choose a pivot, partition the array around the pivot, and recursively sort the sub-arrays on either side of the pivot.
- **Time Complexity:** O(n log n) on average, O(n^2) in the worst case.
- **Space Complexity:** O(log n)
- **Formula:** Quick sort can be represented as:
  \[ Q(a, b) = \begin{cases} \text{Partition}(a, b) & \text{if } b > 0 \\ \text{sort}(a) & \text{if } b = 0 \end{cases} \]
- **Algorithm:**
  1. Choose a pivot.
  2. Partition the array around the pivot.
  3. Recursively sort the sub-array on the left side of the pivot.
  4. Recursively sort the sub-array on the right side of the pivot.

### Binary Tree Traversals

---

- **Definition:** Traverse a binary tree using various techniques (Pre-Order, In-Order, Post-Order).
- **Time Complexity:** O(n)
- **Space Complexity:** O(h)
- **Formula:** Not applicable.
- **Algorithm:**
  1. Pre-Order: Visit the root, traverse the left sub-tree, and traverse the right sub-tree.
  2. In-Order: Traverse the left sub-tree, visit the root, and traverse the right sub-tree.
  3. Post-Order: Traverse the left sub-tree, traverse the right sub-tree, and visit the root.

### Multiplication of Large Integers

---

- **Definition:** Multiply two large integers using the Karatsuba algorithm.
- **Time Complexity:** O(n^log2(3))
- **Space Complexity:** O(n)
- **Formula:** Karatsuba algorithm can be represented as:
  \[ K(a, b) = \begin{cases} ab & \text{if } a, b \leq 10^{n/2} \\ K_3(a, b/2) + K_3(b, a/2) + K_1(a, b/2) + K_1(b, a/2) & \text{otherwise} \end{cases} \]
- **Algorithm:**
  1. If the numbers are small enough, multiply them directly.
  2. Split the numbers into two parts.
  3. Recursively multiply each part.
  4. Combine the results.

### Strassen’s Matrix Multiplication

---

- **Definition:** Multiply two square matrices using the Strassen algorithm.
- **Time Complexity:** O(n^log2(7))
- **Space Complexity:** O(n^2)
- **Formula:** Strassen algorithm can be represented as:
  \[ S(a, b) = \begin{cases} ab & \text{if } a, b \leq n \\ S_1(a, b, n) + S_2(a, b, n) + S_3(a, b, n) + S_4(a, b, n) + S_5(a, b, n) + S_6(a, b, n) & \text{otherwise} \end{cases} \]
- **Algorithm:**
  1. If the matrices are small enough, multiply them directly.
  2. Divide each matrix into four quadrants.
  3. Recursively multiply each pair of quadrants.
  4. Combine the results using various formulas.

### Important Theorems and Definitions

---

- **Divide and Conquer Theorem:** A problem can be solved by dividing it into smaller sub-problems, solving each sub-problem, and combining the solutions.
- **Master Theorem:** A master theorem can be used to solve recurrence relations of the form:
  \[ T(n) = aT(\frac{n}{b}) + f(n) \]

Note: This summary is a concise version of the key points for each topic. It is recommended to review the algorithms and formulas in detail to understand the concepts better.
