# Insertion Sort, Selection Sort, and Bubble Sort

## Introduction

Sorting is one of the most fundamental operations in computer science and forms the backbone of countless applications. From organizing student records in a university's database to arranging search results by relevance, sorting algorithms enable efficient data management and retrieval. In the context of the University of Delhi's Computer Science curriculum, understanding sorting algorithms is not merely an academic exercise—it is an essential skill that forms the foundation for more advanced algorithmic thinking.

This module explores three elementary sorting algorithms: **Bubble Sort**, **Selection Sort**, and **Insertion Sort**. While these algorithms are rarely used in production environments due to their quadratic time complexity, they serve as critical learning tools. They demonstrate fundamental algorithmic concepts such as comparisons, swaps, divide-and-conquer (implicitly), and in-place sorting. Moreover, these algorithms frequently appear in DU semester examinations, making mastery of them essential for academic success.

Understanding why these algorithms work, how they perform under different conditions, and when to apply each one develops the analytical mindset necessary for advanced algorithm design. We shall examine each algorithm's logic, analyze its time and space complexity, and explore practical scenarios where each algorithm might be preferred despite their theoretical limitations.

## Key Concepts

### Bubble Sort

**Bubble Sort** is the simplest sorting algorithm that works by repeatedly stepping through the list, comparing adjacent elements, and swapping them if they are in the wrong order. The algorithm gets its name because smaller elements "bubble" to the top of the array (beginning), while larger elements sink to the bottom (end).

The algorithm proceeds as follows: starting from the first element, compare each pair of adjacent elements. If the first element is greater than the second, swap them. Continue this process for all adjacent pairs in the first pass. After the first pass, the largest element will have moved to its correct position at the end of the array. Repeat this process for the remaining unsorted portion until no swaps are needed.

**Algorithm (Pseudocode):**
```
procedure bubbleSort(A : list of sortable items)
    n = length(A)
    for i = 0 to n-1 do
        swapped = false
        for j = 0 to n-i-2 do
            if A[j] > A[j+1] then
                swap(A[j], A[j+1])
                swapped = true
            end if
        end for
        if not swapped then
            break
        end if
    end for
end procedure
```

**Time Complexity:** O(n²) in worst and average cases, O(n) in best case (when array is already sorted). **Space Complexity:** O(1) as it sorts in-place.

### Selection Sort

**Selection Sort** improves upon bubble sort by reducing the number of swaps. While bubble sort may swap elements in every pass, selection sort makes only one swap per pass. The algorithm divides the input list into two parts: a sorted portion at the left end and an unsorted portion at the right end. Initially, the sorted portion is empty, and the unsorted portion is the entire list.

In each iteration, the algorithm finds the minimum (or maximum, depending on sorting order) element in the unsorted portion, swaps it with the first unsorted element, and moves the boundary between the sorted and unsorted portions one element to the right.

**Algorithm (Pseudocode):**
```
procedure selectionSort(A : list of sortable items)
    n = length(A)
    for i = 0 to n-2 do
        minIdx = i
        for j = i+1 to n-1 do
            if A[j] < A[minIdx] then
                minIdx = j
            end if
        end for
        if minIdx != i then
            swap(A[i], A[minIdx])
        end if
    end for
end procedure
```

**Time Complexity:** O(n²) in all cases (best, worst, and average)—this is because the algorithm must examine all remaining elements to find the minimum in each iteration. **Space Complexity:** O(1) in-place sorting.

### Insertion Sort

**Insertion Sort** is the most efficient among the three elementary sorting algorithms, especially for small datasets or nearly sorted arrays. It builds the final sorted array one item at a time, mimicking how a person might sort playing cards in their hands.

The algorithm iterates through an array of elements, removing one element per iteration and placing it in the correct position in the sorted portion of the array. Unlike bubble sort and selection sort, insertion sort is **adaptive**—it performs significantly better when the input is already substantially sorted.

**Algorithm (Pseudocode):**
```
procedure insertionSort(A : list of sortable items)
    for i = 1 to length(A)-1 do
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key do
            A[j+1] = A[j]
            j = j - 1
        end while
        A[j+1] = key
    end for
end procedure
```

**Time Complexity:** O(n²) in worst and average cases, O(n) in best case (already sorted array). **Space Complexity:** O(1) in-place sorting.

## Examples

### Example 1: Bubble Sort Step-by-Step

Sort the array: [5, 2, 8, 1, 9]

**Pass 1:**
- Compare 5 and 2: 5 > 2, swap → [2, 5, 8, 1, 9]
- Compare 5 and 8: 5 < 8, no swap → [2, 5, 8, 1, 9]
- Compare 8 and 1: 8 > 1, swap → [2, 5, 1, 8, 9]
- Compare 8 and 9: 8 < 9, no swap → [2, 5, 1, 8, 9]

**Pass 2:**
- Compare 2 and 5: 2 < 5, no swap → [2, 5, 1, 8, 9]
- Compare 5 and 1: 5 > 1, swap → [2, 1, 5, 8, 9]
- Compare 5 and 8: 5 < 8, no swap → [2, 1, 5, 8, 9]

**Pass 3:**
- Compare 2 and 1: 2 > 1, swap → [1, 2, 5, 8, 9]
- Compare 2 and 5: 2 < 5, no swap → [1, 2, 5, 8, 9]

**Pass 4:**
- Compare 1 and 2: 1 < 2, no swap → [1, 2, 5, 8, 9]

Array is sorted: [1, 2, 5, 8, 9]

### Example 2: Selection Sort Step-by-Step

Sort the array: [64, 25, 12, 22, 11]

**i = 0:** Find minimum in [64, 25, 12, 22, 11] → minimum is 11 at index 4
- Swap A[0] and A[4]: [11, 25, 12, 22, 64]

**i = 1:** Find minimum in [25, 12, 22, 64] → minimum is 12 at index 2
- Swap A[1] and A[2]: [11, 12, 25, 22, 64]

**i = 2:** Find minimum in [25, 22, 64] → minimum is 22 at index 3
- Swap A[2] and A[3]: [11, 12, 22, 25, 64]

**i = 3:** Find minimum in [25, 64] → minimum is 25 at index 3
- No swap needed: [11, 12, 22, 25, 64]

Sorted array: [11, 12, 22, 25, 64]

### Example 3: Insertion Sort Step-by-Step

Sort the array: [12, 11, 13, 5, 6]

**i = 1:** key = 11, compare with 12: 12 > 11, shift 12 → [12, 12, 13, 5, 6], place 11 → [11, 12, 13, 5, 6]

**i = 2:** key = 13, compare with 12: 12 < 13, no shift → [11, 12, 13, 5, 6]

**i = 3:** key = 5, compare with 13: 13 > 5, shift → [11, 12, 13, 13, 6]
- Compare with 12: 12 > 5, shift → [11, 12, 12, 13, 6]
- Compare with 11: 11 > 5, shift → [11, 11, 12, 13, 6]
- Place 5 → [5, 11, 12, 13, 6]

**i = 4:** key = 6, compare with 13: 13 > 6, shift → [5, 11, 12, 13, 13]
- Compare with 12: 12 > 6, shift → [5, 11, 12, 12, 13]
- Compare with 11: 11 > 6, shift → [5, 11, 11, 12, 13]
- Place 6 → [5, 6, 11, 12, 13]

Sorted array: [5, 6, 11, 12, 13]

## Exam Tips

For DU semester examinations, keep the following points in mind:

1. **Time Complexities are Crucial:** Be prepared to state and justify the worst-case, best-case, and average-case time complexities for all three algorithms. Bubble sort and insertion sort have O(n) best case, while selection sort remains O(n²) in all cases.

2. **Adaptive Property Matters:** Remember that insertion sort is adaptive—it runs in O(n) time when the array is already sorted or nearly sorted. This is a key distinction that examiners frequently test.

3. **Space Complexity is O(1) for All:** All three algorithms are in-place sorting algorithms with constant space complexity. This makes them memory-efficient for small datasets.

4. **Swap Counts Differ:** Bubble sort may perform O(n²) swaps in the worst case, while selection sort performs exactly (n-1) swaps. This is a common examination question.

5. **Stability Definition:** A sorting algorithm is stable if elements with equal keys maintain their relative order. Among these three, insertion sort and bubble sort are stable, while selection sort is not stable.

6. **Practical Applications:** Insertion sort is actually used in practice for small arrays (typically n < 50) and for nearly sorted data. The Python sorting algorithm (Timsort) uses insertion sort for small chunks.

7. **Trace Algorithms for Small Inputs:** Examination questions often require you to trace through an algorithm with a specific input array. Practice tracing by hand for arrays of size 5-10 elements.

8. **Compare and Contrast:** Prepare a comparison table showing time complexities, space complexities, stability, and adaptive properties of all three algorithms. This helps in answering "differentiate between" type questions.