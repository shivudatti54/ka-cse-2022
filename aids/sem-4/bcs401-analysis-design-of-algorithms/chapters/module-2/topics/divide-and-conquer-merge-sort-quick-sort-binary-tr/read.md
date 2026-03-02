# Divide and Conquer Algorithms

=====================================

## Introduction

---

Divide and Conquer is a popular approach to solving complex problems by breaking them down into smaller sub-problems, solving each sub-problem, and combining the solutions to solve the original problem. This technique is used in various fields, including computer science, mathematics, and engineering.

## Merge Sort

---

### Definition

Merge Sort is a Divide and Conquer algorithm that splits an input array into two halves, recursively sorts each half, and then merges the two sorted halves.

### Algorithm

1.  If the input array has only one element, return it (base case).
2.  Split the array into two halves, `left` and `right`.
3.  Recursively call Merge Sort on `left` and `right`.
4.  Merge the two sorted halves into a single sorted array.

### Example

Suppose we want to sort the array `[3, 6, 1, 8, 2, 4]`.

1.  Split the array into `left = [3, 6, 1]` and `right = [8, 2, 4]`.
2.  Recursively call Merge Sort on `left` and `right`.
3.  Sort `left` to `[1, 3, 6]` and `right` to `[2, 4, 8]`.
4.  Merge the two sorted halves to get `[1, 2, 3, 4, 6, 8]`.

### Code

```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result
```

## Quick Sort

---

### Definition

Quick Sort is a Divide and Conquer algorithm that selects a pivot element, partitions the array around the pivot, and recursively sorts the sub-arrays.

### Algorithm

1.  If the input array has only one element, return it (base case).
2.  Choose a pivot element from the array.
3.  Partition the array into three sub-arrays: `left`, `pivot`, and `right`, where all elements less than the pivot are in `left`, all elements equal to the pivot are in `pivot`, and all elements greater than the pivot are in `right`.
4.  Recursively call Quick Sort on `left` and `right`.

### Example

Suppose we want to sort the array `[3, 6, 1, 8, 2, 4]`.

1.  Choose the pivot element `5`.
2.  Partition the array to get `left = [1, 2, 3]`, `pivot = [5]`, and `right = [6, 8, 4]`.
3.  Recursively call Quick Sort on `left` and `right`.
4.  Sort `left` to `[1, 2, 3]` and `right` to `[4, 6, 8]`.
5.  Merge the two sorted halves to get `[1, 2, 3, 4, 5, 6, 8]`.

### Code

```python
def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)
```

## Binary Tree Traversals

---

### Definition

A binary tree is a tree data structure in which each node has at most two children, referred to as the left child and the right child.

### Types of Traversals

There are three types of traversals:

- **In-Order Traversal**: Left subtree + Current node + Right subtree
- **Pre-Order Traversal**: Current node + Left subtree + Right subtree
- **Post-Order Traversal**: Left subtree + Right subtree + Current node

### Example

Suppose we have the following binary tree:

        1
       / \
      2   3
     / \   \
    4   5   6

### In-Order Traversal

1.  Left subtree: `4`, `5`
2.  Current node: `2`
3.  Right subtree: `3`, `6`
4.  Result: `[4, 2, 5, 3, 6]`

### Pre-Order Traversal

1.  Current node: `1`
2.  Left subtree: `2`, `4`
3.  Right subtree: `3`, `5`, `6`
4.  Result: `[1, 2, 4, 3, 5, 6]`

### Post-Order Traversal

1.  Left subtree: `4`, `5`
2.  Right subtree: `3`, `6`
3.  Current node: `2`
4.  Result: `[4, 5, 2, 3, 6]`

### Code

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def in_order_traversal(node):
    if node:
        in_order_traversal(node.left)
        print(node.data, end=" ")
        in_order_traversal(node.right)

def pre_order_traversal(node):
    if node:
        print(node.data, end=" ")
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)

def post_order_traversal(node):
    if node:
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        print(node.data, end=" ")
```

## Multiplication of Large Integers

---

### Definition

Multiplication of large integers is a mathematical operation that combines two or more integers to produce a single integer.

### Algorithm

1.  Convert each integer to a string.
2.  Pad the shorter string with leading zeros.
3.  Multiply the two strings digit-wise.
4.  Add the partial products together.

### Example

Suppose we want to multiply `123` and `456`.

1.  Convert to strings: `123` and `456`.
2.  Pad with leading zeros: `00123` and `0456`.
3.  Multiply digit-wise: `00123 * 0456 = 0567218`.
4.  Add the partial products together: `0567218 + 0 = 567218`.

### Code

```python
def multiply_large_integers(a, b):
    a_str = str(a).zfill(len(b))
    b_str = str(b).zfill(len(a))

    result = 0
    for i in range(len(b_str)):
        partial_product = int(a_str[i]) * int(b_str[i])
        result += partial_product

    return result
```

## Strassen’s Matrix Multiplication

---

### Definition

Strassen’s Matrix Multiplication is an algorithm for multiplying two large matrices using a divide-and-conquer approach.

### Algorithm

1.  Split the matrices into four quadrants.
2.  Compute the following seven products:
    - `M1 = A11 * D11 + A12 * D21`
    - `M2 = A11 * D12 + A12 * D22`
    - `M3 = A21 * D11 + A22 * D21`
    - `M4 = A21 * D12 + A22 * D22`
    - `M5 = A11 * D22 + A12 * D21 - A21 * D11 - A22 * D12`
    - `M6 = A11 * D21 + A12 * D22 - A21 * D11 + A22 * D12`
    - `M7 = A11 * D12 + A12 * D22`
3.  Combine the products to get the final result:
    - `C11 = M1 + M4 - M5 + M7`
    - `C12 = M3 + M5`
    - `C21 = M2 + M4`
    - `C22 = M1 + M3 - M2 + M6`

### Example

Suppose we want to multiply the matrices `A` and `B`.

```python
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

C = strassen_matrix_multiplication(A, B)
```

### Code

```python
def strassen_matrix_multiplication(A, B):
    n = len(A)

    if n == 1:
        return [[A[0][0] * B[0][0]]]

    mid = n // 2

    A11, A12, A21, A22 = [A[i][j] for i in range(mid) for j in range(mid)]
    B11, B12, B21, B22 = [B[i][j] for i in range(mid) for j in range(mid)]

    M1 = strassen_matrix_multiplication([[A11 + A12, A21 + A22], [A11 + A12, A21 + A22]], [[B11 + B12, B21 + B22], [B11 + B12, B21 + B22]])
    M2 = strassen_matrix_multiplication([[A11 + A12, A21 + A22], [B11 + B12, B21 + B22]], [[B11 + B12, B21 + B22], [B11 + B12, B21 + B22]])
    M3 = strassen_matrix_multiplication([[A11 + A12, A21 + A22], [B11 - B12, B21 - B22]], [[B11 - B12, B21 - B22], [B11 + B12, B21 + B22]])
    M4 = strassen_matrix_multiplication([[A11 - A12, A21 - A22], [B11 + B12, B21 + B22]], [[B11 + B12, B21 + B22], [B11 - B12, B21 - B22]])
    M5 = strassen_matrix_multiplication([[A11 + A12, A21 + A22], [B11 - B12, B21 - B22]], [[B11 - B12, B21 - B22], [B11 + B12, B21 + B22]])
    M6 = strassen_matrix_multiplication([[A11 + A12, A21 - A22], [B11 + B12, B21 + B22]], [[B11 + B12, B21 + B22], [B11 - B12, B21 - B22]])
    M7 = strassen_matrix_multiplication([[A11 + A12, A21 + A22], [B11 + B12, B21 - B22]], [[B11 + B12, B21 - B22], [B11 - B12, B21 + B22]])

    C11 = M1[0][0] + M4[0][0] - M5[0][0] + M7[0][0]
    C12 = M3[0][0] + M5[0][1]
    C21 = M2[0][0] + M4[0][1]
    C22 = M1[0][1] + M3[0][1] - M2[0][1] + M6[0][1]

    C11 = C11 + [[C11, C12], [C21, C22]]
    if n == 2:
        return [[A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]], [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]]]
    else:
        return C11

# Example usage:
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
C = strassen_matrix_multiplication(A, B)
```

Note: The above code is a simplified version of Strassen's Matrix Multiplication algorithm. It does not handle errors and is not optimized for performance.
