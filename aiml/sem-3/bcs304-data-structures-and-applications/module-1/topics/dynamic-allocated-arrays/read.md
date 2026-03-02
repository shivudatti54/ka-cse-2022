# Dynamic Arrays in C


## Table of Contents

- [Dynamic Arrays in C](#dynamic-arrays-in-c)
- [1. Introduction and Theoretical Foundation](#1-introduction-and-theoretical-foundation)
  - [1.1 Formal Definition](#11-formal-definition)
  - [1.2 Static versus Dynamic Arrays: Comparative Analysis](#12-static-versus-dynamic-arrays-comparative-analysis)
- [2. Amortized Complexity Analysis](#2-amortized-complexity-analysis)
  - [2.1 The Amortized Cost Paradigm](#21-the-amortized-cost-paradigm)
  - [2.2 Theorem: Amortized O(1) Append with Doubling](#22-theorem-amortized-o1-append-with-doubling)
  - [2.3 Alternative Growth Strategies](#23-alternative-growth-strategies)
- [3. Data Structure Specification](#3-data-structure-specification)
  - [3.1 Structure Definition](#31-structure-definition)
  - [3.2 Memory Layout Diagram](#32-memory-layout-diagram)
- [4. Implementation in C](#4-implementation-in-c)
  - [4.1 Creation and Initialization](#41-creation-and-initialization)
  - [4.2 Resize Operation with Error Handling](#42-resize-operation-with-error-handling)
  - [4.3 Append Operation](#43-append-operation)
  - [4.4 Insertion at Arbitrary Position](#44-insertion-at-arbitrary-position)
  - [4.5 Deletion at Arbitrary Position](#45-deletion-at-arbitrary-position)
  - [4.6 Destruction and Cleanup](#46-destruction-and-cleanup)
- [5. Complexity Analysis of Operations](#5-complexity-analysis-of-operations)
- [6. Advanced Considerations](#6-advanced-considerations)
  - [6.1 Shrinking Strategy Analysis](#61-shrinking-strategy-analysis)
  - [6.2 Cache Locality Benefits](#62-cache-locality-benefits)
- [7. Assessment Questions](#7-assessment-questions)
  - [Question 1 (Numerical - Hard)](#question-1-numerical---hard)
  - [Question 2 (Application - Hard)](#question-2-application---hard)
  - [Question 3 (Analysis - Hard)](#question-3-analysis---hard)
  - [Question 4 (Numerical - Hard)](#question-4-numerical---hard)

## 1. Introduction and Theoretical Foundation

A **dynamic array** (also known as a resizable array or vector in C++/Java) is a random-access data structure that maintains a contiguous memory block capable of dynamically resizing itself during program execution. Unlike static arrays whose dimensions are fixed at compile time, dynamic arrays abstract away manual memory management while providing constant-time random access to stored elements.

### 1.1 Formal Definition

A dynamic array A is a tuple (data, size, capacity) where:

- `data`: A pointer to a contiguous heap-allocated memory region
- `size`: The number of elements currently stored (0 ≤ size ≤ capacity)
- `capacity`: The maximum number of elements the current allocation can hold

The fundamental invariant maintained is: `size ≤ capacity` at all times.

### 1.2 Static versus Dynamic Arrays: Comparative Analysis

| Property           | Static Array             | Dynamic Array                      |
| ------------------ | ------------------------ | ---------------------------------- |
| Memory Allocation  | Compile-time (stack/bss) | Runtime (heap via malloc)          |
| Size Determination | Fixed declaration        | Grows/shrinks dynamically          |
| Access Time        | O(1)                     | O(1)                               |
| Append (amortized) | O(1) if space available  | O(1) amortized                     |
| Insert at Position | O(n)                     | O(n)                               |
| Delete at Position | O(n)                     | O(n)                               |
| Memory Efficiency  | Fixed overhead           | Dynamic (may have unused capacity) |
| Deallocation       | Automatic (scope exit)   | Manual (free required)             |

## 2. Amortized Complexity Analysis

### 2.1 The Amortized Cost Paradigm

Amortized analysis provides a worst-case guarantee averaged over a sequence of operations, rather than individual operations. For dynamic array append operations with a doubling strategy (capacity doubles when full), we prove that the amortized cost is O(1).

### 2.2 Theorem: Amortized O(1) Append with Doubling

**Statement**: Let a dynamic array begin with capacity c₀ and double its capacity whenever size equals capacity. The amortized cost of n append operations is O(1).

**Proof using Aggregate Analysis**:

Consider n append operations on an initially empty dynamic array. Let capacities form the sequence: c₀, c₁, c₂, ..., cₖ where cᵢ = 2ⁱ × c₀ for i ≥ 0.

Let m be the largest integer such that the total elements stored up to some point equals or exceeds 2ᵐ × c₀.

The total cost comprises:

1. **Actual work in appends**: Each append that doesn't trigger resize performs O(1) work (writing one element). Let n₁ be the number of non-resize appends.
2. **Resize operations**: When resizing from capacity cᵢ₋₁ to cᵢ = 2 × cᵢ₋₁, we copy all existing cᵢ₋₁ elements. Total copy cost = c₀ + c₁ + c₂ + ... + cₖ₋₁.

Since capacities double, we have:
c₀ + c₁ + c₂ + ... + cₖ₋₁ = c₀(1 + 2 + 4 + ... + 2ᵏ⁻¹) = c₀(2ᵏ - 1) < 2cₖ

And since n ≤ cₖ + cₖ₋₁ (we never store more than roughly twice the final capacity), the total cost T(n) satisfies:

T(n) ≤ n + 2cₖ ≤ n + 2n = 3n = O(n)

Therefore, amortized cost per operation = T(n)/n = O(1). ∎

### 2.3 Alternative Growth Strategies

| Growth Factor (α)   | Advantages                         | Disadvantages                    |
| ------------------- | ---------------------------------- | -------------------------------- |
| α = 2 (doubling)    | Logarithmic amortized cost, simple | 50% space overhead at peak       |
| α = 1.5 (Fibonacci) | ~37% space overhead                | More complex resize calculations |
| α > 2               | Fewer resizes                      | Higher space overhead            |

The choice involves a space-time tradeoff: larger α reduces resize frequency but increases wasted memory.

## 3. Data Structure Specification

### 3.1 Structure Definition

```c
typedef struct {
 int *data; /* Pointer to heap-allocated buffer */
 size_t size; /* Current number of elements */
 size_t capacity; /* Total allocated capacity */
} DynArray;
```

**Invariant**: `data` points to a region of `capacity × sizeof(int)` bytes; the first `size` positions contain valid elements.

### 3.2 Memory Layout Diagram

```
Initial state (capacity=4, size=2):
┌─────────────────────────────────┐
│ data ──→ [10 | 20 | | ] │
└─────────────────────────────────┘
 ↑size=2 ↑capacity=4

After append(30), append(40):
┌─────────────────────────────────┐
│ data ──→ [10 | 20 | 30 | 40 ] │
└─────────────────────────────────┘
 ↑size=4 ↑capacity=4

After append(50) [triggers resize]:
┌─────────────────────────────────────────────────┐
│ data ──→ [10 | 20 | 30 | 40 | 50 | | | ]│
└─────────────────────────────────────────────────┘
 ↑size=5 ↑capacity=8
```

## 4. Implementation in C

### 4.1 Creation and Initialization

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define INITIAL_CAPACITY 4
#define GROWTH_FACTOR 2

DynArray *createDynArray(void) {
 DynArray *arr = (DynArray *)malloc(sizeof(DynArray));
 if (arr == NULL) {
 return NULL; /* Propagate allocation failure */
 }

 arr->data = (int *)malloc(INITIAL_CAPACITY * sizeof(int));
 if (arr->data == NULL) {
 free(arr);
 return NULL;
 }

 arr->size = 0;
 arr->capacity = INITIAL_CAPACITY;
 return arr;
}
```

### 4.2 Resize Operation with Error Handling

```c
int resize(DynArray *arr, size_t newCapacity) {
 if (newCapacity < arr->size) {
 return 0; /* Cannot shrink below current size */
 }

 int *newData = (int *)realloc(arr->data, newCapacity * sizeof(int));
 if (newData == NULL) {
 return 0; /* Original data remains valid */
 }

 arr->data = newData;
 arr->capacity = newCapacity;
 return 1;
}
```

### 4.3 Append Operation

```c
int append(DynArray *arr, int value) {
 /* Check if resize required */
 if (arr->size == arr->capacity) {
 size_t newCapacity = arr->capacity * GROWTH_FACTOR;
 if (!resize(arr, newCapacity)) {
 return 0; /* Resize failed */
 }
 }

 arr->data[arr->size++] = value;
 return 1;
}
```

### 4.4 Insertion at Arbitrary Position

```c
int insertAt(DynArray *arr, size_t pos, int value) {
 /* Validate position */
 if (pos > arr->size) {
 return 0;
 }

 /* Ensure capacity */
 if (arr->size == arr->capacity) {
 if (!resize(arr, arr->capacity * GROWTH_FACTOR)) {
 return 0;
 }
 }

 /* Shift elements right by one position */
 memmove(arr->data + pos + 1,
 arr->data + pos,
 (arr->size - pos) * sizeof(int));

 arr->data[pos] = value;
 arr->size++;
 return 1;
}
```

### 4.5 Deletion at Arbitrary Position

```c
int deleteAt(DynArray *arr, size_t pos) {
 if (pos >= arr->size) {
 return 0; /* Out of bounds */
 }

 /* Shift elements left, except for last element */
 if (pos < arr->size - 1) {
 memmove(arr->data + pos,
 arr->data + pos + 1,
 (arr->size - pos - 1) * sizeof(int));
 }

 arr->size--;

 /* Shrink if utilization drops below 25% */
 if (arr->size > 0 && arr->size <= arr->capacity / 4) {
 size_t newCapacity = arr->capacity / 2;
 if (newCapacity >= INITIAL_CAPACITY) {
 resize(arr, newCapacity);
 }
 }

 return 1;
}
```

### 4.6 Destruction and Cleanup

```c
void destroyDynArray(DynArray *arr) {
 if (arr != NULL) {
 free(arr->data);
 free(arr);
 }
}
```

## 5. Complexity Analysis of Operations

| Operation            | Best Case | Worst Case | Amortized |
| -------------------- | --------- | ---------- | --------- |
| get(index)           | O(1)      | O(1)       | O(1)      |
| set(index, value)    | O(1)      | O(1)       | O(1)      |
| append(value)        | O(1)      | O(n)       | O(1)      |
| insertAt(pos, value) | O(1)      | O(n)       | O(n)      |
| deleteAt(pos)        | O(1)      | O(n)       | O(n)      |
| resize(newCapacity)  | O(1)      | O(n)       | O(n)      |

## 6. Advanced Considerations

### 6.1 Shrinking Strategy Analysis

Automatic shrinking prevents memory waste when many deletions occur. Using a 50% threshold (shrink when size ≤ capacity/4) prevents Thrashing—repeated resize operations when hovering near the threshold. This creates a hysteresis effect ensuring Ω(n) operations between consecutive shrinks.

### 6.2 Cache Locality Benefits

Dynamic arrays provide superior cache performance compared to linked structures. Contiguous memory allocation enables:

- Prefetching of subsequent elements
- Reduced cache miss penalties
- Vectorized operations (SIMD) capability

---

## 7. Assessment Questions

### Question 1 (Numerical - Hard)

A dynamic array starts with capacity 4 and uses a doubling strategy (growth factor = 2). If we insert 50 elements sequentially using append, how many times is the resize operation executed, and what is the final capacity after all insertions?

**Answer**: Resize operations occur at sizes 4, 8, 16, 32 (4 times). Final capacity = 64.

### Question 2 (Application - Hard)

Consider a dynamic array with initial capacity 1 and growth factor 2. After inserting elements [1, 2, 3, 4, 5, 6, 7] in order and then deleting the last 3 elements, what is the theoretical memory waste (unused bytes) assuming each int is 4 bytes? Assume shrinking occurs when size ≤ capacity/4.

**Answer**: After 7 inserts: size=7, capacity=8. After 3 deletes: size=4, capacity=8. No shrink occurs (4 > 8/4 = 2). Memory used = 32 bytes, waste = 16 bytes.

### Question 3 (Analysis - Hard)

Prove that if we use a growth factor of α > 1 (not necessarily integer), the amortized cost of append remains O(1). What is the amortized cost expression in terms of α?

**Answer**: Total cost T(n) ≤ n + (α/(α-1)) × n = O(n). Therefore amortized cost = O(1) regardless of α > 1.

### Question 4 (Numerical - Hard)

A dynamic array has initial capacity 10 and uses a tripling strategy (growth factor = 3). Starting from empty, after how many append operations will the first resize occur, and what will be the capacity after the 25th append operation?

**Answer**: First resize at append 11 (when size reaches 10). After 25 appends: capacities go 10 → 30 → 90. Final capacity = 90.
