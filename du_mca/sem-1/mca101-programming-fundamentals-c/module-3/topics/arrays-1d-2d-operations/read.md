# Arrays (1D & 2D) Operations

## Introduction
Arrays are fundamental data structures that store elements of the same type in contiguous memory locations. In computer science, 1D arrays represent linear collections while 2D arrays model matrix-like structures. Their importance stems from:
- O(1) random access time complexity
- Memory efficiency for homogeneous data
- Foundation for complex data structures (heaps, hash tables)
- Wide applications in scientific computing, image processing, and database systems

In industry, 1D arrays are used in audio signal processing and financial time-series analysis, while 2D arrays form the basis of digital images (pixel matrices), spreadsheet applications, and game boards. Understanding array operations is crucial for algorithm optimization and memory management.

## Key Concepts
1. **Declaration & Initialization**
   - 1D: `int arr[5] = {1,2,3,4,5};`
   - 2D: `int matrix[3][3] = {{1,2,3},{4,5,6},{7,8,9}};`
   
2. **Memory Layout**
   - Row-major (C/C++) vs Column-major (Fortran) ordering
   - Address calculation: `address(arr[i][j]) = base + (i * n + j) * size`

3. **Core Operations**
   - Traversal: Nested loops for 2D arrays
   - Insertion/Deletion: Shifting elements with O(n) complexity
   - Searching: Linear (O(n)) vs Binary (O(log n))
   - Sorting: Bubble, Selection, and QuickSort implementations

4. **Special Operations**
   - Matrix addition/multiplication
   - Transpose: `matrix[j][i] = matrix[i][j]`
   - Boundary elements traversal

## Examples

**Example 1: Binary Search in 1D Array**
```c
int binarySearch(int arr[], int l, int r, int x) {
    while (l <= r) {
        int mid = l + (r - l)/2;
        if (arr[mid] == x) return mid;
        if (arr[mid] < x) l = mid + 1;
        else r = mid - 1;
    }
    return -1;
}
// Time Complexity: O(log n)
```

**Example 2: Matrix Multiplication**
```c
void multiply(int A[][N], int B[][M], int C[][M], int rows) {
    for(int i=0; i<rows; i++) {
        for(int j=0; j<M; j++) {
            C[i][j] = 0;
            for(int k=0; k<N; k++)
                C[i][j] += A[i][k] * B[k][j];
        }
    }
}
// Complexity: O(n³) for N x N matrices
```

## Exam Tips
1. Always validate array indices to prevent buffer overflow
2. Remember C arrays are zero-indexed
3. For 2D array parameters, column size must be specified in function declarations
4. Matrix multiplication requires columns of A = rows of B
5. Sorting algorithms' time complexities vary: Bubble Sort (O(n²)) vs QuickSort (O(n log n))
6. Use pointer arithmetic for efficient array traversal
7. Trace row-major storage when calculating element addresses