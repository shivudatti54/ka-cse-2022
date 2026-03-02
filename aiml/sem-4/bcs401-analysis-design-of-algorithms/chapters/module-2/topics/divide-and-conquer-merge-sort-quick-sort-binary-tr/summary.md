# **DIVIDE AND CONQUER: Merge Sort, Quick Sort, Binary Tree Traversals, Multiplication of Large Integers and Strassen’s Matrix Multiplication**

### Overview

- Divide and Conquer is a problem-solving strategy that breaks down complex problems into smaller sub-problems.
- It involves dividing the problem into smaller instances of the same problem, solving each instance, and then combining the solutions.

### Key Concepts

- **Merge Sort**
  - Divide: Divide the array into two halves.
  - Conquer: Recursively sort each half.
  - Combine: Merge the sorted halves.
- **Quick Sort**
  - Choose a pivot element.
  - Partition: Divide the array around the pivot.
  - Recursively sort: Sort the sub-arrays.
- **Binary Tree Traversals**
  - Inorder: Left-root-right.
  - Preorder: Root-left-right.
  - Postorder: Left-right-root.

### Important Formulas and Definitions

- **Merge Sort**
  - Time complexity: O(n log n)
  - Space complexity: O(n)
- **Quick Sort**
  - Time complexity: O(n log n) on average, O(n^2) in worst case.
  - Space complexity: O(log n)
- **Binary Tree Traversals**
  - Inorder traversal: Sum of node values.
  - Preorder traversal: Count of node values.
  - Postorder traversal: Product of node values.

### Multiplication of Large Integers

- **Carry and Reduce**
  - Multiply each digit of the first number with each digit of the second number.
  - Add the partial products and reduce the carry.

### Strassen’s Matrix Multiplication

- **Divide and Conquer**
  - Divide the matrices into four quadrants.
  - Multiply the quadrants and combine the results.
- **Time Complexity**
  - O(n^2.81) using the Strassen algorithm.
  - O(n^3) using the standard matrix multiplication algorithm.

### Important Theorems

- **Divide and Conquer Theorem**
  - Any problem that can be solved by a divide-and-conquer approach can be solved in O(n log n) time.
- **Strassen's Theorem**
  - The Strassen algorithm has a better time complexity than the standard matrix multiplication algorithm for large matrices.
