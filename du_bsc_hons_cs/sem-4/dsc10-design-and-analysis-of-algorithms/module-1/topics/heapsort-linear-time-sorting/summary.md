# Heapsort and Linear Time Sorting

## Introduction

Sorting algorithms are fundamental in computer science, classified into **comparison-based** (Ω(n log n) lower bound) and **non-comparison-based** (linear time O(n)) methods. Heapsort achieves O(n log n) using a binary heap data structure, while linear time sorts exploit key properties for specialized scenarios.

---

## Heapsort

- **Data Structure**: Binary Heap (complete binary tree stored as array)
  - Max-Heap: Parent ≥ Children (for ascending order)
  - Min-Heap: Parent ≤ Children (for descending order)

- **Key Operations**:
  - `HEAPIFY`: Maintains heap property at a node (O(log n))
  - `BUILD-MAX-HEAP`: Converts unsorted array to heap (O(n))
  - `EXTRACT-MAX`: Removes and returns maximum element

- **Algorithm**:
  1. Build max-heap from unsorted array
  2. Swap root (maximum) with last element
  3. Reduce heap size, heapify root
  4. Repeat until heap size = 1

- **Time Complexity**: O(n log n) in all cases
- **Space Complexity**: O(1) auxiliary
- **Properties**: In-place, not stable, not adaptive

---

## Linear Time Sorting Algorithms

### Counting Sort
- **Assumption**: Keys are integers in range [0, k]
- **Process**: Count occurrences of each key, compute cumulative counts, place elements
- **Time**: O(n + k), **Space**: O(n + k)
- **Stable**: Yes
- **Use Case**: When range (k) is not significantly larger than n

### Radix Sort
- **Method**: Sort digit-by-digit (least significant to most significant)
- **Sub-algorithm**: Uses stable sort (usually counting sort) per digit
- **Time**: O(d × (n + k)) where d = digits, k = base
- **Stable**: Yes
- **Use Case**: Integers, fixed-length strings

### Bucket Sort
- **Method**: Distribute elements into buckets using hash function, sort each bucket (usually insertion sort), concatenate
- **Time**: O(n) average (O(n²) worst if poorly distributed)
- **Stable**: Depends on bucket sort algorithm
- **Use Case**: Input uniformly distributed over range

---

## Comparison Table

| Algorithm | Best | Average | Worst | Space | Stable |
|-----------|------|---------|-------|-------|--------|
| Heapsort | n log n | n log n | n log n | 1 | No |
| Counting | n + k | n + k | n + k | n + k | Yes |
| Radix | d(n+k) | d(n+k) | d(n+k) | n + k | Yes |
| Bucket | n | n | n² | n | Usually |

---

## Conclusion

Heapsort provides guaranteed O(n log n) performance with O(1) space, ideal for memory-constrained environments. Linear time sorts (Counting, Radix, Bucket) surpass this bound when specific conditions are met—Counting for small integer ranges, Radix for multiple-digit numbers, and Bucket for uniformly distributed data. Understanding trade-offs between stability, space, and input constraints is essential for selecting the appropriate algorithm in practice.

*Reference: Delhi University BSc (H) DSA Syllabus – Sorting Algorithms Unit*