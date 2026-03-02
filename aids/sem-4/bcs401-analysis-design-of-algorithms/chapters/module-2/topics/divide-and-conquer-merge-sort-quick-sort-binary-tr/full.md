# DIVIDE AND CONQUER: Merge Sort, Quick Sort, Binary Tree Traversals, Multiplication of Large Integers and Strassen’s Matrix Multiplication

## Table of Contents

1. [Introduction](#introduction)
2. [Merge Sort](#merge-sort)
   - [History](#history)
   - [How it Works](#how-it-works)
   - [Time Complexity](#time-complexity)
   - [Space Complexity](#space-complexity)
   - [Example](#example)
3. [Quick Sort](#quick-sort)
   - [History](#history)
   - [How it Works](#how-it-works)
   - [Time Complexity](#time-complexity)
   - [Space Complexity](#space-complexity)
   - [Example](#example)
4. [Binary Tree Traversals](#binary-tree-traversals)
   - [In-Order Traversal](#in-order-traversal)
   - [Pre-Order Traversal](#pre-order-traversal)
   - [Post-Order Traversal](#post-order-traversal)
   - [Level Order Traversal](#level-order-traversal)
   - [Tree Traversal Examples](#tree-traversal-examples)
5. [Multiplication of Large Integers](#multiplication-of-large-integers)
   - [Carry-Over Method](#carry-over-method)
   - [Modular Multiplication Method](#modular-multiplication-method)
   - [Example](#example)
6. [Strassen’s Matrix Multiplication](#strassen’s-matrix-multiplication)
   - [History](#history)
   - [How it Works](#how-it-works)
   - [Time Complexity](#time-complexity)
   - [Space Complexity](#space-complexity)
   - [Example](#example)
7. [Conclusion](#conclusion)
8. [Further Reading](#further-reading)

## Introduction

Divide and Conquer (D&C) is a problem-solving strategy used to break down complex problems into smaller sub-problems, solve each sub-problem, and then combine the solutions to solve the original problem. This approach is widely used in computer science to solve a variety of problems, including sorting, searching, and matrix multiplication.

In this section, we will explore five different Divide and Conquer algorithms:

1. Merge Sort
2. Quick Sort
3. Binary Tree Traversals
4. Multiplication of Large Integers
5. Strassen’s Matrix Multiplication

Each of these algorithms has its own unique characteristics, strengths, and weaknesses.

## Merge Sort

Merge Sort is a popular sorting algorithm that uses the Divide and Conquer approach to sort arrays of integers.

### History

Merge Sort was first proposed by John von Neumann in 1945.

### How it Works

Merge Sort works by dividing the input array into two halves until each half has only one element. Then, it merges the halves in sorted order. The algorithm uses a recursive approach to divide the array into smaller sub-arrays.

Here is a step-by-step illustration of the Merge Sort algorithm:

1. Divide the input array into two halves.
2. Recursively call Merge Sort on each half.
3. Merge the two sorted halves into a single sorted array.

### Time Complexity

The time complexity of Merge Sort is O(n log n), where n is the size of the input array.

### Space Complexity

The space complexity of Merge Sort is O(n), as we need to store the temporary arrays used during the merge process.

### Example

Suppose we want to sort the following array: `[5, 2, 8, 3, 1, 6, 4]`.

We divide the array into two halves: `[5, 2, 8, 3]` and `[1, 6, 4]`.

We recursively call Merge Sort on each half:

- `[5, 2, 8, 3]` becomes `[2, 3, 5, 8]`
- `[1, 6, 4]` becomes `[1, 4, 6]`

We then merge the two sorted halves: `[2, 3, 5, 8]` and `[1, 4, 6]`. The resulting sorted array is `[1, 2, 3, 4, 5, 6, 8]`.

## Quick Sort

Quick Sort is another popular sorting algorithm that uses the Divide and Conquer approach to sort arrays of integers.

### History

Quick Sort was first proposed by Tony Hoare in 1959.

### How it Works

Quick Sort works by selecting a pivot element from the input array, partitioning the array around the pivot, and recursively sorting the sub-arrays on either side of the pivot.

Here is a step-by-step illustration of the Quick Sort algorithm:

1. Select a pivot element from the input array.
2. Partition the array around the pivot element.
3. Recursively call Quick Sort on the sub-array to the left of the pivot.
4. Recursively call Quick Sort on the sub-array to the right of the pivot.

### Time Complexity

The time complexity of Quick Sort is O(n log n) on average, but it can be O(n^2) in the worst case.

### Space Complexity

The space complexity of Quick Sort is O(log n), as we need to store the recursive call stack.

### Example

Suppose we want to sort the following array: `[5, 2, 8, 3, 1, 6, 4]`.

We select the pivot element as 5.

We partition the array around the pivot: `[2, 3, 1, 6, 4]` and `[8, 5]`.

We recursively call Quick Sort on the sub-arrays:

- `[2, 3, 1, 6, 4]` becomes `[1, 2, 3, 4, 6]`
- `[8, 5]` becomes `[5, 8]`

We then combine the sorted sub-arrays: `[1, 2, 3, 4, 5, 6, 8]`.

## Binary Tree Traversals

Binary Tree Traversals are a fundamental concept in computer science that involves traversing a binary tree data structure.

### In-Order Traversal

In-Order Traversal visits the left subtree, the root node, and then the right subtree.

### Pre-Order Traversal

Pre-Order Traversal visits the root node, the left subtree, and then the right subtree.

### Post-Order Traversal

Post-Order Traversal visits the left subtree, the right subtree, and then the root node.

### Level Order Traversal

Level Order Traversal visits each level of the binary tree from left to right.

### Tree Traversal Examples

Suppose we have the following binary tree:

```
    4
   / \
  2   6
 / \   \
1   3   5
```

We can perform an in-order traversal of the tree, visiting each node in the following order: `1, 2, 3, 4, 5, 6`.

We can perform a pre-order traversal of the tree, visiting each node in the following order: `4, 2, 1, 3, 6, 5`.

We can perform a post-order traversal of the tree, visiting each node in the following order: `1, 3, 2, 5, 6, 4`.

## Multiplication of Large Integers

Multiplication of large integers is a fundamental problem in computer science that involves multiplying two large integers using a divide-and-conquer approach.

### Carry-Over Method

The carry-over method involves multiplying the two integers digit by digit and adding the carry-over value at each step.

### Modular Multiplication Method

The modular multiplication method involves multiplying the two integers modulo a large number, reducing the intermediate results to avoid overflow.

### Example

Suppose we want to multiply the following two integers: `123456789` and `987654321`.

We can use the carry-over method to multiply the two integers.

1. Multiply the least significant digits: `9 * 1 = 9`
2. Multiply the next digits and add the carry-over: `8 * 2 = 16`, add 9 = 25
3. Multiply the next digits and add the carry-over: `7 * 3 = 21`, add 25 = 46
4. Multiply the next digits and add the carry-over: `6 * 4 = 24`, add 46 = 70
5. Multiply the next digits and add the carry-over: `5 * 5 = 25`, add 70 = 95
6. Multiply the next digits and add the carry-over: `4 * 6 = 24`, add 95 = 119
7. Multiply the next digits and add the carry-over: `3 * 7 = 21`, add 119 = 140
8. Multiply the next digits and add the carry-over: `2 * 8 = 16`, add 140 = 156
9. Multiply the next digits and add the carry-over: `1 * 9 = 9`, add 156 = 165
10. Multiply the most significant digits and add the carry-over: `1 * 1 = 1`, add 165 = 166

The final product is `166,667,890,321`.

## Strassen’s Matrix Multiplication

Strassen’s Matrix Multiplication is a fast algorithm for multiplying two large matrices using a divide-and-conquer approach.

### History

Strassen’s Matrix Multiplication was first proposed by Volker Strassen in 1969.

### How it Works

Strassen’s Matrix Multiplication involves dividing the two input matrices into seven smaller sub-matrices, multiplying the sub-matrices using a divide-and-conquer approach, and then combining the results to produce the final product.

Here is a step-by-step illustration of the Strassen’s Matrix Multiplication algorithm:

1. Divide the two input matrices into seven smaller sub-matrices: `A = [A11, A12; A21, A22]` and `B = [B11, B12; B21, B22]`.
2. Compute the following seven products: `M1 = (A11 + A22) * (B11 + B22)`, `M2 = (A21 + A22) * B11`, `M3 = A11 * (B12 - B22)`, `M4 = A22 * (B21 - B11)`, `M5 = (A11 + A12) * B22`, `M6 = (A21 - A11) * (B11 + B12)`, `M7 = (A12 - A22) * (B21 + B22)`.
3. Compute the final product: `C = M1 + M4 - M5 + M7`.
4. Combine the results to produce the final product: `C = [C11, C12; C21, C22]`.

### Time Complexity

The time complexity of Strassen’s Matrix Multiplication is O(n^2.81), where n is the size of the input matrices.

### Space Complexity

The space complexity of Strassen’s Matrix Multiplication is O(n^2), as we need to store the seven sub-matrices.

The final answer is: There is no final answer, as this is a comprehensive overview of five Divide and Conquer algorithms.
