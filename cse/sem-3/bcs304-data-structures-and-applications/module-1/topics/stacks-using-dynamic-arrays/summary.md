# Stacks Using Dynamic Arrays

## Overview

A dynamic array stack is a data structure that resizes its underlying array at runtime using `realloc`, addressing the limitations of fixed-size array stacks. It starts with a small initial capacity and doubles its size when the array becomes full, achieving amortized O(1) push time. This strategy is known as the doubling strategy or geometric growth.

## Key Points

- A dynamic array stack resizes its underlying array at runtime using `realloc`.
- The doubling strategy doubles the capacity when the array is full, achieving amortized O(1) push time.
- Shrinking the array is optional but important for memory efficiency in long-running applications.
- The "halve at quarter" strategy is preferred for shrinking to avoid thrashing.
- Dynamic array stacks have a growth factor, typically doubling (factor of 2).
- Amortized analysis considers the average time complexity of an operation over a sequence of operations.

## Important Concepts

- **Dynamic Array Stack**: A stack that resizes its underlying array at runtime using `realloc`.
- **Doubling Strategy**: A strategy that doubles the capacity when the array is full.
- **Amortized O(1)**: The average time complexity of an operation over a sequence of operations.
- **Thrashing**: The scenario where alternating push/pop operations at the boundary repeatedly trigger resize and shrink.

## Notes

- Always assign the `realloc` return value to a temporary pointer first to avoid memory leaks on failure.
- Include the `destroy` function (freeing memory) in your implementation to show proper memory management.
- Understand why "halve at quarter" is preferred over "halve at half" to avoid thrashing.
- Be ready to explain the **amortized O(1)** analysis and the doubling strategy.
