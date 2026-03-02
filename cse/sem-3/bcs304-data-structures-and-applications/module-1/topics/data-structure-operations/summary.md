# Data Structure Operations

## Overview

Data structure operations are the fundamental actions that can be performed on data structures, including traversal, searching, insertion, deletion, sorting, and merging. Understanding these operations and their efficiency is crucial in data structures. This summary covers the key concepts, definitions, and comparisons of these operations.

## Key Points

- Traversal: Visiting every element of a data structure exactly once in a systematic manner.
- Searching: Finding the location of a given element in a data structure.
- Insertion: Adding a new element to a data structure at a specified position.
- Deletion: Removing an existing element from a data structure.
- Sorting: Arranging elements in a specific order (ascending or descending).
- Merging: Combining two sorted data structures into a single sorted structure.

## Important Definitions

- **Traversal**: The process of visiting every element of a data structure exactly once.
- **Binary Search**: A searching algorithm that works on sorted arrays by repeatedly dividing the search interval in half.
- **Merging**: The process of combining two sorted data structures into a single sorted structure.

## Key Formulas / Syntax

- Binary Search: `mid = (low + high) / 2`
- Merging: `c[k++] = (a[i] <= b[j]) ? a[i++] : b[j++]`

## Comparisons

| Feature          | Linear Search            | Binary Search      |
| ---------------- | ------------------------ | ------------------ |
| Data requirement | Any (sorted or unsorted) | Must be sorted     |
| Time complexity  | O(n)                     | O(log n)           |
| Approach         | Sequential               | Divide and conquer |
| Implementation   | Simple                   | Slightly complex   |

## Exam Tips

- List all six data structure operations.
- Practice tracing binary search on a given array.
- State the prerequisite for binary search (sorted array).
- Understand the shifting process for insertion and deletion.
- Be prepared to write C code for binary search and merging.
- Compare linear search and binary search, including time complexity and use cases.
