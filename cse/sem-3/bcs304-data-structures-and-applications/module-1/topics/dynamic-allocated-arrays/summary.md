# Dynamic Arrays in C

## Overview

A dynamic array is a resizable array that can grow or shrink during program execution, managing its own memory on the heap using `malloc`, `realloc`, and `free`. It maintains an internal buffer larger than the current number of elements and reallocates this buffer when it becomes full.

## Key Points

- Dynamic arrays can grow or shrink at runtime, unlike static arrays with fixed sizes.
- Memory allocation is manual with `malloc`, and deallocation requires `free`.
- Automatic resizing occurs when appending to a full array.
- Random access is O(1), similar to static arrays.
- Insertion and deletion in the middle are O(n), as elements must be shifted.
- Amortized analysis shows append operations are O(1) on average.

## Important Definitions

- **Dynamic Array**: A resizable array that manages its memory on the heap.
- **Capacity**: The total allocated space in the array.
- **Size**: The number of elements currently stored in the array.
- **Amortized Analysis**: Analyzing the average time complexity of operations over a sequence.

## Key Formulas / Syntax

- `DynArray *arr = createDynArray();` to create a dynamic array.
- `append(arr, value)` to add an element, resizing if necessary.
- `int value = get(arr, index)` to retrieve an element at a given index.

## Comparisons

| Feature                | Static Array      | Dynamic Array    |
| ---------------------- | ----------------- | ---------------- |
| Size Change at Runtime | No                | Yes              |
| Memory Allocation      | Stack (Automatic) | Heap (Manual)    |
| Append When Full       | Not Possible      | Automatic Resize |
| Random Access          | O(1)              | O(1)             |

## Exam Tips

- Focus on the dynamic array struct definition and basic operations like append and get.
- Understand amortized analysis for append operations and why the growth factor must be multiplicative.
- Be aware of common pitfalls in C, such as forgetting to check `malloc`/`realloc` return values and not freeing memory.
- Practice explaining the thrashing problem and how shrinking at `capacity / 4` resolves it.
- Review dynamic stacks and queues as applications of dynamic arrays.
