# Merge Sort & Quick Sort – Quick Revision

**Design and Analysis of Algorithms (DAA)**
*BSc (Hons) CS – Delhi University (NEP 2024)*

---

## Introduction

Merge Sort and Quick Sort are two fundamental **comparison-based sorting algorithms** based on the **Divide and Conquer** paradigm. They are essential for understanding efficient sorting and are part of the Delhi University syllabus for DAA.

---

## Merge Sort

- **Approach**: Recursively divide the array into two halves until single elements remain, then merge them in sorted order.
- **Algorithm Steps**:
  1. **Divide**: Split array into two halves
  2. **Conquer**: Recursively sort both halves
  3. **Merge**: Combine sorted halves into one sorted array
- **Time Complexity**: O(n log n) in all cases (Best, Average, Worst)
- **Space Complexity**: O(n) — requires auxiliary array for merging
- **Stability**: **Stable** — equal elements maintain their relative order
- **Use Cases**: Preferred for linked lists and external sorting (large files)

---

## Quick Sort

- **Approach**: Select a **pivot** element, partition the array around the pivot, then recursively sort partitions.
- **Algorithm Steps**:
  1. **Choose Pivot**: Select an element (first, last, random, or median)
  2. **Partition**: Rearrange so elements < pivot are on left, > pivot on right
  3. **Recursively Sort**: Apply Quick Sort to left and right partitions
- **Time Complexity**:
  - Best/Average: O(n log n)
  - Worst: O(n²) — occurs when pivot is smallest/largest element
- **Space Complexity**: O(log n) for recursion stack (average case)
- **Stability**: **Unstable** — may change relative order of equal elements
- **Use Cases**: Preferred for arrays due to in-place sorting and cache efficiency

---

## Key Comparison

| Feature | Merge Sort | Quick Sort |
|---------|------------|------------|
| **Worst Case** | O(n log n) | O(n²) |
| **Space** | O(n) | O(log n) |
| **Stability** | Stable | Unstable |
| **In-Place** | No | Yes |

---

## Conclusion

Both algorithms are optimal comparison sorts with O(n log n) average time. **Merge Sort** guarantees O(n log n) performance and stability but needs extra space. **Quick Sort** is faster in practice due to cache locality and in-place sorting, though worst-case can degrade. Understanding their trade-offs is crucial for algorithm selection in real-world applications.