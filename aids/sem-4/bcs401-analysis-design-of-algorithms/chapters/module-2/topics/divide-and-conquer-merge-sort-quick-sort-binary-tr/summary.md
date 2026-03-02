# **DIVIDE AND CONQUER: Merge Sort, Quick Sort, Binary Tree Traversals, Multiplication of Large Integers and Strassen’s Matrix Multiplication**

## **I. Merge Sort**

- **Definition:** Divide-and-conquer algorithm that splits an array into two halves, recursively sorts them, and merges them.
- **Time Complexity:** O(n log n)
- **Space Complexity:** O(n)
- **Formula:** `M[i] = M[2i] + M[2i+1]`

## **II. Quick Sort**

- **Definition:** Divide-and-conquer algorithm that selects a pivot, partitions the array around it, and recursively sorts the subarrays.
- **Time Complexity:** O(n log n) on average, O(n^2) in worst case
- **Space Complexity:** O(log n)
- **Formula:** `pivot = median(arr[0], arr[1], ..., arr[n-1])`
- **Partition Scheme:**
  - `left < pivot`
  - `right > pivot`
  - `i = left`

## **III. Binary Tree Traversals**

- **Definition:** Traversal algorithms for binary trees, including inorder, preorder, and postorder traversals.
- **Formula:**
  - Inorder: `visit(node.left) -> visit(node) -> visit(node.right)`
  - Preorder: `visit(node) -> visit(node.left) -> visit(node.right)`
  - Postorder: `visit(node.left) -> visit(node.right) -> visit(node)`

## **IV. Multiplication of Large Integers**

- **Definition:** Algorithm for multiplying two large integers using a divide-and-conquer approach.
- **Time Complexity:** O(log n)
- **Space Complexity:** O(log n)
- **Formula:** `a*b = (a/2)*(b/2) + (a/2)*(b/2) + (a/2)*(b/2)`

## **V. Strassen’s Matrix Multiplication**

- **Definition:** Divide-and-conquer algorithm for matrix multiplication.
- **Time Complexity:** O(n^2.81)
- **Space Complexity:** O(n^2)
- **Formula:** `C = A*B = (A11+A22)*(B11+B22) + (A12-A21)*(B21+B12) + (A11-A22)*(B11-B22) + (A21+A12)*(B21-B12) + (A11+A22)*(B11-B21) + (A12-A21)*(B22-B11)`
