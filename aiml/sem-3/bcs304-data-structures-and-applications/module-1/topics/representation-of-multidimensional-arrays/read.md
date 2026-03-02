# Representation of Multidimensional Arrays


## Table of Contents

- [Representation of Multidimensional Arrays](#representation-of-multidimensional-arrays)
- [Introduction](#introduction)
- [2D Array: Logical View vs Physical View](#2d-array-logical-view-vs-physical-view)
  - [Logical View (Matrix)](#logical-view-matrix)
  - [Physical View (Linear Memory)](#physical-view-linear-memory)
- [Row-Major Order](#row-major-order)
  - [Concept](#concept)
  - [Address Formula (Row-Major, 0-Based Indexing)](#address-formula-row-major-0-based-indexing)
  - [Address Formula (Row-Major, 1-Based Indexing)](#address-formula-row-major-1-based-indexing)
  - [Worked Example 1 (Row-Major, 0-Based)](#worked-example-1-row-major-0-based)
  - [Worked Example 2 (Row-Major, 1-Based)](#worked-example-2-row-major-1-based)
- [Column-Major Order](#column-major-order)
  - [Concept](#concept)
  - [Address Formula (Column-Major, 0-Based Indexing)](#address-formula-column-major-0-based-indexing)
  - [Address Formula (Column-Major, 1-Based Indexing)](#address-formula-column-major-1-based-indexing)
  - [Worked Example 3 (Column-Major, 0-Based)](#worked-example-3-column-major-0-based)
  - [Worked Example 4 (Column-Major, 1-Based)](#worked-example-4-column-major-1-based)
- [C Code for 2D Array Operations](#c-code-for-2d-array-operations)
  - [Creating and Initializing a 2D Array](#creating-and-initializing-a-2d-array)
  - [Row-Major Traversal (Natural in C)](#row-major-traversal-natural-in-c)
  - [Column-Major Traversal](#column-major-traversal)
  - [Address Computation in C](#address-computation-in-c)
- [Generalization to 3D Arrays](#generalization-to-3d-arrays)
  - [Concept](#concept)
  - [Row-Major Address Formula (0-Based)](#row-major-address-formula-0-based)
  - [Worked Example 5 (3D Array)](#worked-example-5-3d-array)
- [General n-Dimensional Address Formula](#general-n-dimensional-address-formula)
- [Cache Performance: Why Traversal Order Matters](#cache-performance-why-traversal-order-matters)
  - [Spatial Locality](#spatial-locality)
  - [Row-Major Traversal in C (Cache-Friendly)](#row-major-traversal-in-c-cache-friendly)
  - [Column-Major Traversal in C (Cache-Unfriendly)](#column-major-traversal-in-c-cache-unfriendly)
  - [Practical Rule](#practical-rule)
- [Comparison: Row-Major vs Column-Major](#comparison-row-major-vs-column-major)
- [Additional Worked Numerical Examples](#additional-worked-numerical-examples)
  - [Example 6: Finding Array Element Given Address](#example-6-finding-array-element-given-address)
  - [Example 7: Total Memory and Range of Addresses](#example-7-total-memory-and-range-of-addresses)
- [Exam Tips](#exam-tips)

## Introduction

Computer memory is fundamentally **one-dimensional** -- it is a linear sequence of bytes, each with a unique address. However, many real-world problems require two-dimensional (matrices), three-dimensional (volumes), or even higher-dimensional data representations. When we declare a 2D array like `int A[3][4]`, the compiler must map this two-dimensional logical structure onto the one-dimensional physical memory. Understanding exactly how this mapping works is essential for:

- Computing the address of any element using a formula (frequently asked in exams)
- Writing cache-efficient code
- Understanding how C stores arrays internally

## 2D Array: Logical View vs Physical View

### Logical View (Matrix)

A 2D array `int A[3][4]` can be visualized as a matrix with 3 rows and 4 columns:

```
Col 0 Col 1 Col 2 Col 3
Row 0 [ A[0][0] A[0][1] A[0][2] A[0][3] ]
Row 1 [ A[1][0] A[1][1] A[1][2] A[1][3] ]
Row 2 [ A[2][0] A[2][1] A[2][2] A[2][3] ]
```

### Physical View (Linear Memory)

In memory, all 12 elements must be laid out sequentially. The question is: **in what order?** There are two standard conventions.

## Row-Major Order

### Concept

In **row-major order**, elements are stored **row by row**. The entire first row is placed first in memory, followed by the entire second row, and so on. This is the method used by **C, C++, and Java**.

```
Memory layout for A[3][4] in row-major:
A[0][0] A[0][1] A[0][2] A[0][3] A[1][0] A[1][1] A[1][2] A[1][3] A[2][0] A[2][1] A[2][2] A[2][3]
|-------- Row 0 --------| |-------- Row 1 --------| |-------- Row 2 --------|
```

### Address Formula (Row-Major, 0-Based Indexing)

For a 2D array `A[M][N]` (M rows, N columns), base address `B`, element size `w`:

```
Address(A[i][j]) = B + (i * N + j) * w
```

**Explanation of each term:**

- `i * N` = number of complete rows before row `i`, each containing `N` elements
- `j` = offset within row `i`
- `(i * N + j)` = total number of elements before `A[i][j]`
- Multiply by `w` to convert element count to byte offset

### Address Formula (Row-Major, 1-Based Indexing)

If the array indices start from 1 (common in exam questions), for `A[M][N]` with indices from `A[1][1]` to `A[M][N]`:

```
Address(A[i][j]) = B + ((i - 1) * N + (j - 1)) * w
```

### Worked Example 1 (Row-Major, 0-Based)

Given: `int A[3][4]`, base address `B = 1000`, `sizeof(int) = 4`
Find the address of `A[2][1]`.

```
Address(A[2][1]) = 1000 + (2 * 4 + 1) * 4 = 1000 + (8 + 1) * 4 = 1000 + 9 * 4 = 1000 + 36 = 1036
```

**Verification table** (all addresses in row-major):

| Element | Offset (i\*N+j) | Address = 1000 + offset\*4 |
| ------- | --------------- | -------------------------- |
| A[0][0] | 0\*4+0 = 0      | 1000                       |
| A[0][1] | 0\*4+1 = 1      | 1004                       |
| A[0][2] | 0\*4+2 = 2      | 1008                       |
| A[0][3] | 0\*4+3 = 3      | 1012                       |
| A[1][0] | 1\*4+0 = 4      | 1016                       |
| A[1][1] | 1\*4+1 = 5      | 1020                       |
| A[1][2] | 1\*4+2 = 6      | 1024                       |
| A[1][3] | 1\*4+3 = 7      | 1028                       |
| A[2][0] | 2\*4+0 = 8      | 1032                       |
| A[2][1] | 2\*4+1 = 9      | 1036                       |
| A[2][2] | 2\*4+2 = 10     | 1040                       |
| A[2][3] | 2\*4+3 = 11     | 1044                       |

### Worked Example 2 (Row-Major, 1-Based)

Given: `float A[4][5]` with indexing from `A[1][1]` to `A[4][5]`, base address `B = 2000`, `sizeof(float) = 4`
Find the address of `A[3][4]`.

```
Address(A[3][4]) = 2000 + ((3 - 1) * 5 + (4 - 1)) * 4 = 2000 + (2 * 5 + 3) * 4 = 2000 + (10 + 3) * 4 = 2000 + 13 * 4 = 2000 + 52 = 2052
```

## Column-Major Order

### Concept

In **column-major order**, elements are stored **column by column**. The entire first column is placed first, followed by the second column, and so on. This method is used by **FORTRAN and MATLAB**.

```
Memory layout for A[3][4] in column-major:
A[0][0] A[1][0] A[2][0] A[0][1] A[1][1] A[2][1] A[0][2] A[1][2] A[2][2] A[0][3] A[1][3] A[2][3]
|---- Col 0 ----| |---- Col 1 ----| |---- Col 2 ----| |---- Col 3 ----|
```

### Address Formula (Column-Major, 0-Based Indexing)

For a 2D array `A[M][N]` (M rows, N columns):

```
Address(A[i][j]) = B + (j * M + i) * w
```

**Explanation:**

- `j * M` = number of complete columns before column `j`, each containing `M` elements
- `i` = offset within column `j`

### Address Formula (Column-Major, 1-Based Indexing)

```
Address(A[i][j]) = B + ((j - 1) * M + (i - 1)) * w
```

### Worked Example 3 (Column-Major, 0-Based)

Given: `int A[3][4]`, base address `B = 1000`, `sizeof(int) = 4`
Find the address of `A[2][1]`.

```
Address(A[2][1]) = 1000 + (1 * 3 + 2) * 4 = 1000 + (3 + 2) * 4 = 1000 + 5 * 4 = 1000 + 20 = 1020
```

**Verification table** (all addresses in column-major):

| Element | Offset (j\*M+i) | Address = 1000 + offset\*4 |
| ------- | --------------- | -------------------------- |
| A[0][0] | 0\*3+0 = 0      | 1000                       |
| A[1][0] | 0\*3+1 = 1      | 1004                       |
| A[2][0] | 0\*3+2 = 2      | 1008                       |
| A[0][1] | 1\*3+0 = 3      | 1012                       |
| A[1][1] | 1\*3+1 = 4      | 1016                       |
| A[2][1] | 1\*3+2 = 5      | 1020                       |
| A[0][2] | 2\*3+0 = 6      | 1024                       |
| A[1][2] | 2\*3+1 = 7      | 1028                       |
| A[2][2] | 2\*3+2 = 8      | 1032                       |
| A[0][3] | 3\*3+0 = 9      | 1036                       |
| A[1][3] | 3\*3+1 = 10     | 1040                       |
| A[2][3] | 3\*3+2 = 11     | 1044                       |

Notice that `A[2][1]` is at address 1036 in row-major but 1020 in column-major -- same element, different physical location depending on the storage order.

### Worked Example 4 (Column-Major, 1-Based)

Given: `double A[5][3]` with indexing from `A[1][1]` to `A[5][3]`, base address `B = 500`, `sizeof(double) = 8`
Find the address of `A[4][2]`.

```
Address(A[4][2]) = 500 + ((2 - 1) * 5 + (4 - 1)) * 8 = 500 + (1 * 5 + 3) * 8 = 500 + 8 * 8 = 500 + 64 = 564
```

## C Code for 2D Array Operations

### Creating and Initializing a 2D Array

```c
#include <stdio.h>
#define ROWS 3
#define COLS 4

int main() {
 /* Static 2D array */
 int A[ROWS][COLS] = {
 {1, 2, 3, 4},
 {5, 6, 7, 8},
 {9, 10, 11, 12}
 };

 /* Dynamic 2D array using single malloc (row-major in memory) */
 int *B = (int *)malloc(ROWS * COLS * sizeof(int));

 /* Access B[i][j] as B[i * COLS + j] */
 free(B);
 return 0;
}
```

### Row-Major Traversal (Natural in C)

```c
void traverseRowMajor(int A[][COLS], int rows) {
 int i, j;
 printf("Row-major traversal:\n");
 for (i = 0; i < rows; i++) {
 for (j = 0; j < COLS; j++) {
 printf("%4d ", A[i][j]);
 }
 printf("\n");
 }
}
```

Memory access pattern: `A[0][0], A[0][1], A[0][2], A[0][3], A[1][0], ...`
This accesses elements in the **same order they are stored in memory** (in C), resulting in excellent cache performance.

### Column-Major Traversal

```c
void traverseColMajor(int A[][COLS], int rows) {
 int i, j;
 printf("Column-major traversal:\n");
 for (j = 0; j < COLS; j++) {
 for (i = 0; i < rows; i++) {
 printf("%4d ", A[i][j]);
 }
 printf("\n");
 }
}
```

Memory access pattern: `A[0][0], A[1][0], A[2][0], A[0][1], ...`
In C, this jumps across memory by `COLS * sizeof(int)` bytes between accesses, causing **cache misses**. This is slower than row-major traversal.

### Address Computation in C

```c
#include <stdio.h>

void computeAddress(int baseAddr, int i, int j, int M, int N, int w) {
 int rowMajorAddr, colMajorAddr;

 /* Row-major (0-based) */
 rowMajorAddr = baseAddr + (i * N + j) * w;

 /* Column-major (0-based) */
 colMajorAddr = baseAddr + (j * M + i) * w;

 printf("A[%d][%d]:\n", i, j);
 printf(" Row-major address: %d\n", rowMajorAddr);
 printf(" Column-major address: %d\n", colMajorAddr);
}

int main() {
 int base = 1000, M = 3, N = 4, w = 4;
 computeAddress(base, 0, 0, M, N, w);
 computeAddress(base, 1, 2, M, N, w);
 computeAddress(base, 2, 3, M, N, w);
 return 0;
}
```

**Output:**

```
A[0][0]:
 Row-major address: 1000
 Column-major address: 1000
A[1][2]:
 Row-major address: 1024
 Column-major address: 1028
A[2][3]:
 Row-major address: 1044
 Column-major address: 1044
```

## Generalization to 3D Arrays

### Concept

A 3D array `A[X][Y][Z]` can be visualized as `X` planes, each plane being a `Y x Z` matrix.

### Row-Major Address Formula (0-Based)

```
Address(A[i][j][k]) = B + (i * Y * Z + j * Z + k) * w
```

**Explanation:**

- `i * Y * Z` = number of elements in all planes before plane `i`
- `j * Z` = number of elements in all rows before row `j` in the current plane
- `k` = offset within the current row

### Worked Example 5 (3D Array)

Given: `int A[2][3][4]`, base address `B = 1000`, `sizeof(int) = 4`
Find the address of `A[1][2][3]`.

```
Address(A[1][2][3]) = 1000 + (1 * 3 * 4 + 2 * 4 + 3) * 4 = 1000 + (12 + 8 + 3) * 4 = 1000 + 23 * 4 = 1000 + 92 = 1092
```

**Verification:**
Total elements before `A[1][2][3]`:

- 1 complete plane of 3\*4 = 12 elements
- 2 complete rows of 4 elements = 8 elements
- 3 elements in the current row
- Total = 12 + 8 + 3 = 23 elements

## General n-Dimensional Address Formula

For an n-dimensional array `A[d1][d2]...[dn]` stored in row-major order with 0-based indexing:

```
Address(A[i1][i2]...[in]) = B + w * SUM(k=1 to n) of (ik * PRODUCT(l=k+1 to n) dl)
```

Each index `ik` is multiplied by the product of all dimensions that come after it. For example, in a 4D array `A[D1][D2][D3][D4]`:

```
Address(A[i][j][k][l]) = B + (i*D2*D3*D4 + j*D3*D4 + k*D4 + l) * w
```

The pattern is clear: each index is multiplied by the total number of elements in all subsequent dimensions.

## Cache Performance: Why Traversal Order Matters

### Spatial Locality

Modern CPUs load data in **cache lines** (typically 64 bytes). When you access `A[0][0]`, the CPU loads nearby memory into the cache. If the next access is `A[0][1]` (adjacent in memory for row-major), it is already in cache -- a **cache hit**.

### Row-Major Traversal in C (Cache-Friendly)

```c
/* FAST: sequential memory access */
int sum = 0;
for (i = 0; i < M; i++)
 for (j = 0; j < N; j++)
 sum += A[i][j];
```

Accessing elements in storage order means nearly every access is a cache hit.

### Column-Major Traversal in C (Cache-Unfriendly)

```c
/* SLOW: strided memory access */
int sum = 0;
for (j = 0; j < N; j++)
 for (i = 0; i < M; i++)
 sum += A[i][j];
```

Each access jumps `N * sizeof(int)` bytes forward, potentially causing a cache miss on every access. For large arrays, this can be **5-10x slower** than row-major traversal.

### Practical Rule

Since C uses row-major storage, always make the **rightmost index vary fastest** in nested loops for best performance.

## Comparison: Row-Major vs Column-Major

| Aspect               | Row-Major                 | Column-Major               |
| -------------------- | ------------------------- | -------------------------- |
| Storage order        | Row by row                | Column by column           |
| Used by              | C, C++, Java, Pascal      | FORTRAN, MATLAB, R         |
| Formula (0-based)    | B + (i*N + j) * w         | B + (j*M + i) * w          |
| Formula (1-based)    | B + ((i-1)_N + (j-1)) _ w | B + ((j-1)_M + (i-1)) _ w  |
| Fast traversal       | Outer loop on rows        | Outer loop on columns      |
| Cache-friendly in C  | Yes (matches storage)     | No (strides across memory) |
| A[0][0] address      | B                         | B                          |
| Last element address | B + (M*N - 1) * w         | B + (M*N - 1) * w          |

## Additional Worked Numerical Examples

### Example 6: Finding Array Element Given Address

An integer array `A[5][6]` is stored in row-major order. Base address = 100, sizeof(int) = 2. If a certain element is stored at address 136, find which element it is.

```
Address = B + (i * N + j) * w
136 = 100 + (i * 6 + j) * 2
36 = (i * 6 + j) * 2
18 = i * 6 + j
Now, 18 = 3 * 6 + 0, so i = 3, j = 0
Answer: The element is A[3][0]
```

### Example 7: Total Memory and Range of Addresses

For `short A[10][20]` (sizeof(short) = 2), base address = 5000:

- Total elements = 10 \* 20 = 200
- Total memory = 200 \* 2 = 400 bytes
- First address = 5000
- Last address = 5000 + (200 - 1) \* 2 = 5000 + 398 = 5398
- Address range: 5000 to 5399 (inclusive of all bytes)

## Exam Tips

- **Memorize both formulas** (row-major and column-major) for 0-based and 1-based indexing. questions almost always involve one of these.
- When a problem says "stored in row-major order," use `(i * N + j)`. When it says "column-major," use `(j * M + i)`. A common mistake is mixing up M and N.
- Always **identify whether the problem uses 0-based or 1-based indexing**. If the array is defined as `A[1:5][1:8]` or `A(1..5, 1..8)`, it is 1-based. If it is `A[5][8]` in C-style, it is 0-based.
- For 3D arrays, remember the formula has three terms: `i*Y*Z + j*Z + k`. Practice at least one 3D address calculation.
- In questions asking "how many elements precede A[i][j]?" the answer is directly the offset: `i*N + j` (row-major) or `j*M + i` (column-major).
- If a question gives you an address and asks which element is stored there, reverse-engineer the formula using integer division and modulo.
- Remember that **C always uses row-major order**. If a question involves C code, use the row-major formula.
- The total memory occupied by `A[M][N]` is always `M * N * sizeof(element)` regardless of row-major or column-major -- only the order of elements changes, not the total count.
- Cache performance questions: state that row-major traversal is faster in C because it exploits **spatial locality** -- adjacent elements in the loop are adjacent in memory.
