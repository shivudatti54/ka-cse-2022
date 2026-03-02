# Selection Sort


## Table of Contents

- [Selection Sort](#selection-sort)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [How Selection Sort Works](#how-selection-sort-works)
  - [Algorithm Steps](#algorithm-steps)
  - [C Implementation](#c-implementation)
  - [Time Complexity Analysis](#time-complexity-analysis)
  - [Space Complexity](#space-complexity)
  - [Stability Consideration](#stability-consideration)
- [Examples](#examples)
  - [Example 1: Tracing Selection Sort](#example-1-tracing-selection-sort)
  - [Example 2: Selection Sort for Descending Order](#example-2-selection-sort-for-descending-order)
- [Exam Tips](#exam-tips)

## Introduction

Selection Sort is one of the fundamental sorting algorithms taught in computer science programs, particularly important for students learning C programming and data structures. Unlike more complex algorithms, Selection Sort embodies a straightforward approach: repeatedly finding the minimum element from the unsorted portion and moving it to the beginning of the array.

The algorithm gets its name from its method of selection - it systematically selects the smallest (or largest, depending on sorting order) element from the unsorted portion and places it in its correct position. While not the most efficient for large datasets with O(n²) time complexity, Selection Sort offers valuable insights into algorithmic thinking and serves as an excellent introduction to sorting techniques.

For DU students preparing for semester examinations, understanding Selection Sort is essential because it demonstrates key concepts like in-place sorting, stability considerations, and the trade-offs between time and space complexity. The algorithm frequently appears in practical applications where memory is at a premium, as it requires only O(1) auxiliary space.

## Key Concepts

### How Selection Sort Works

Selection Sort operates by dividing the array into two distinct portions: the sorted portion at the beginning and the unsorted portion occupying the rest. Initially, the sorted portion is empty, and the entire array is unsorted. The algorithm then proceeds iteratively, selecting the minimum element from the unsorted portion and swapping it with the first element of the unsorted portion, thereby expanding the sorted portion by one element.

The process continues until the unsorted portion becomes empty. After each iteration, one element finds its final sorted position at the beginning of the array. This methodical approach ensures that after n-1 passes (the nth pass becomes unnecessary as only one element remains), the entire array becomes sorted.

### Algorithm Steps

1. Set the first unsorted position as the current minimum (let i = 0)
2. Scan through the remaining unsorted elements to find the actual minimum
3. Swap the current minimum with the first unsorted position
4. Move the boundary between sorted and unsorted one position right
5. Repeat until the entire array is sorted

### C Implementation

```c
#include <stdio.h>

void selectionSort(int arr[], int n) {
    int i, j, min_idx, temp;
    
    // One by one move boundary of unsorted subarray
    for (i = 0; i < n - 1; i++) {
        // Find the minimum element in unsorted array
        min_idx = i;
        for (j = i + 1; j < n; j++) {
            if (arr[j] < arr[min_idx]) {
                min_idx = j;
            }
        }
        
        // Swap the found minimum element with the first element
        if (min_idx != i) {
            temp = arr[i];
            arr[i] = arr[min_idx];
            arr[min_idx] = temp;
        }
    }
}

void printArray(int arr[], int size) {
    int i;
    for (i = 0; i < size; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int main() {
    int arr[] = {64, 25, 12, 22, 11};
    int n = sizeof(arr) / sizeof(arr[0]);
    
    printf("Original array: ");
    printArray(arr, n);
    
    selectionSort(arr, n);
    
    printf("Sorted array: ");
    printArray(arr, n);
    
    return 0;
}
```

### Time Complexity Analysis

The time complexity of Selection Sort remains O(n²) for all cases - best, average, and worst. This consistency stems from the algorithm's nature: regardless of the initial arrangement of elements, it always performs the same number of comparisons. For each of the n-1 passes, the inner loop performs (n-i-1) comparisons, leading to a total of n(n-1)/2 comparisons, which simplifies to O(n²).

The outer loop runs (n-1) times, while the inner loop's comparison count decreases with each iteration: (n-1), (n-2), (n-3), ..., 1. The total number of comparisons equals the sum of this arithmetic series, yielding (n-1)(n)/2 = (n²-n)/2, which is asymptotically O(n²).

### Space Complexity

Selection Sort is classified as an in-place sorting algorithm with O(1) auxiliary space complexity. The algorithm modifies the original array through swapping and requires only a constant number of additional variables (min_idx and temp). This makes Selection Sort memory-efficient, as it does not require additional memory proportional to the input size.

### Stability Consideration

Selection Sort is NOT a stable sorting algorithm by default. Stability in sorting means that elements with equal values maintain their relative order from the original array. In the standard implementation, when the minimum element is swapped with the first unsorted position, elements between these positions shift, potentially changing their relative order. For example, if we have [2a, 1, 2b] and sort in ascending order, we might get [1, 2b, 2a], where 2a and 2b have changed positions.

## Examples

### Example 1: Tracing Selection Sort

Sort the array [29, 10, 14, 37, 13] in ascending order using Selection Sort.

**Pass 1:** Starting from index 0
- Compare 29 with 10 → min = 10
- Compare 10 with 14 → min = 10
- Compare 10 with 37 → min = 10
- Compare 10 with 13 → min = 10
- Swap arr[0] and arr[1]
- Array becomes: [10, 29, 14, 37, 13]
- Sorted portion: [10]

**Pass 2:** Starting from index 1
- Compare 29 with 14 → min = 14
- Compare 14 with 37 → min = 14
- Compare 14 with 13 → min = 13
- Swap arr[1] and arr[3]
- Array becomes: [10, 13, 14, 37, 29]
- Sorted portion: [10, 13]

**Pass 3:** Starting from index 2
- Compare 14 with 37 → min = 14
- Compare 14 with 29 → min = 14
- No swap needed (14 is already at correct position)
- Array remains: [10, 13, 14, 37, 29]
- Sorted portion: [10, 13, 14]

**Pass 4:** Starting from index 3
- Compare 37 with 29 → min = 29
- Swap arr[3] and arr[4]
- Array becomes: [10, 13, 14, 29, 37]
- Sorted portion: [10, 13, 14, 29]

**Final Sorted Array:** [10, 13, 14, 29, 37]

### Example 2: Selection Sort for Descending Order

Sort [5, 2, 9, 1, 7] in descending order.

For descending order, we select the MAXIMUM element instead of minimum:

**Pass 1:** Find maximum from indices 0-4
- Maximum = 9 (at index 2)
- Swap arr[0] and arr[2]
- Array: [9, 2, 5, 1, 7]

**Pass 2:** Find maximum from indices 1-4
- Maximum = 7 (at index 4)
- Swap arr[1] and arr[4]
- Array: [9, 7, 5, 1, 2]

**Pass 3:** Find maximum from indices 2-4
- Maximum = 5 (at index 2)
- Already in correct position
- Array: [9, 7, 5, 1, 2]

**Pass 4:** Find maximum from indices 3-4
- Maximum = 2 (at index 4)
- Swap arr[3] and arr[4]
- Array: [9, 7, 5, 2, 1]

**Result:** [9, 7, 5, 2, 1]

## Exam Tips

1. **Remember the key characteristic:** Selection Sort makes exactly n(n-1)/2 comparisons regardless of input order - this distinguishes it from algorithms like Bubble Sort that perform fewer comparisons on sorted input.

2. **Time complexity answer must be precise:** Always state O(n²) for all three cases (best, average, worst) in examinations, as Selection Sort does not benefit from any initial ordering.

3. **Space complexity is O(1):** Selection Sort is in-place, requiring only constant extra memory. This is a frequently tested concept in DU exams.

4. **Distinguish from Bubble Sort:** While both are O(n²), Selection Sort reduces swaps to O(n) while Bubble Sort may require O(n²) swaps. This is an important comparative analysis point.

5. **Algorithm tracing is essential:** Be able to manually trace through an array with 5-6 elements showing each pass and the state of the array after each pass.

6. **Code writing practice:** Practice writing the complete Selection Sort function in C, including the nested loops and the swap operation.

7. **Understand why it's not stable:** Remember that swapping elements that are far apart can change the relative order of equal elements, making Selection Sort unstable.