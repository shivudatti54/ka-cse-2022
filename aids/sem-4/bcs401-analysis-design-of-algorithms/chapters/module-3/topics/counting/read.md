# Counting Sort

## Introduction

Counting Sort is a non-comparison based sorting algorithm that achieves linear time complexity O(n + k), where n is the number of elements and k is the range of input values. Unlike comparison-based sorting algorithms such as QuickSort or MergeSort that rely on element comparisons, Counting Sort exploits the structure of integer keys by counting the frequency of each distinct value. This makes it particularly efficient for datasets where the range of input values (k) is not significantly larger than the number of elements (n).

The algorithm holds significant importance in the study of algorithm design because it demonstrates the power of the "space-time tradeoff" principle — using extra memory to achieve better time complexity. Counting Sort is stable, meaning it preserves the relative order of equal elements, which is crucial in certain applications like sorting records by multiple keys. It serves as a foundational example for understanding radix sort, bucket sort, and other distribution-based sorting techniques that form the backbone of modern computing applications.

## Key Concepts

### Fundamental Principle

Counting Sort works by determining, for each input element x, the number of elements less than x. This information is then used to place x directly into its correct position in the output array. The algorithm requires three arrays: the input array A of length n, an auxiliary counting array C of size k (range of values), and an output array B of length n.

The core idea involves two passes. In the first pass, we count the occurrences of each value by iterating through the input array and incrementing the corresponding index in the counting array. In the second pass, we use these counts to determine the correct positions, iterating through possible values and placing elements in their sorted positions in the output array.

### Algorithm Steps

The complete Counting Sort algorithm proceeds as follows. First, we find the maximum value k in the input array to determine the size of our counting array. Second, we initialize a counting array of size k+1 with all zeros. Third, we iterate through the input array and for each element A[i], we increment C[A[i]] to record its frequency. Fourth, we modify the counting array such that C[i] now stores the number of elements less than or equal to i by accumulating the counts: for i from 1 to k, set C[i] = C[i] + C[i-1]. Fifth, we iterate through the input array in reverse order (to maintain stability) and place each element A[j] at index C[A[j]] - 1 in the output array B, then decrement C[A[j]].

### Time and Space Complexity

The time complexity of Counting Sort is O(n + k) in all cases — best, average, and worst case. This is because the algorithm makes exactly three passes through the data, each taking linear time. The space complexity is O(n + k) due to the output array and counting array requirements. When k = O(n), the algorithm runs in O(n) time, making it superior to comparison-based sorting algorithms that have a theoretical lower bound of Ω(n log n).

### Stability in Counting Sort

Stability is a critical property of Counting Sort that makes it valuable in practical applications. An algorithm is stable if elements with equal keys maintain their relative order from input to output. Counting Sort achieves stability by processing the input array from right to left during the placement phase. This ensures that when multiple occurrences of the same value exist, they appear in the output in the same order as they appeared in the input, which is essential when sorting records by a secondary key.

### Limitations and Practical Considerations

Counting Sort has inherent limitations that restrict its applicability. First, it only works with integers or objects that can be mapped to a finite range of non-negative integers. Second, when the range k is significantly larger than n, the algorithm's space requirements become prohibitive. Third, the algorithm requires knowing or computing the maximum value in advance. Fourth, for floating-point numbers or strings, a transformation step is needed to convert them to integers. These limitations motivate the use of related algorithms like Radix Sort, which extends Counting Sort to handle larger integer ranges by processing digits iteratively.

## Examples

### Example 1: Basic Counting Sort

Sort the array A = [2, 5, 3, 0, 2, 3, 0, 3] using Counting Sort.

**Step 1: Find maximum value**
Maximum value k = 5

**Step 2: Initialize counting array C[0..5] with zeros**
C = [0, 0, 0, 0, 0, 0]

**Step 3: Count occurrences**
Traverse A: increment C[A[i]]
C[0]++ → C[0] = 1 (for A[3]=0)
C[2]++ → C[2] = 1 (for A[0]=2)
C[3]++ → C[3] = 1 (for A[2]=3)
C[5]++ → C[5] = 1 (for A[1]=5)
C[2]++ → C[2] = 2 (for A[4]=2)
C[3]++ → C[3] = 2 (for A[5]=3)
C[0]++ → C[0] = 2 (for A[6]=0)
C[3]++ → C[3] = 3 (for A[7]=3)

After counting: C = [2, 0, 2, 3, 0, 1]

**Step 4: Cumulative count**
C[i] = C[i] + C[i-1]
C[0] = 2
C[1] = 2 + 0 = 2
C[2] = 2 + 2 = 4
C[3] = 4 + 3 = 7
C[4] = 7 + 0 = 7
C[5] = 7 + 1 = 8

After cumulative: C = [2, 2, 4, 7, 7, 8]

**Step 5: Place elements (right to left for stability)**
Initialize B = [0, 0, 0, 0, 0, 0, 0, 0]

Process A[7]=3: C[3]=7, place at B[6], C[3]=6
Process A[6]=0: C[0]=2, place at B[1], C[0]=1
Process A[5]=3: C[3]=6, place at B[5], C[3]=5
Process A[4]=2: C[2]=4, place at B[3], C[2]=3
Process A[3]=3: C[3]=5, place at B[4], C[3]=4
Process A[2]=3: C[3]=4, place at B[3], C[3]=3
Process A[1]=5: C[5]=8, place at B[7], C[5]=7
Process A[0]=2: C[2]=3, place at B[2], C[2]=2

Result: B = [0, 0, 2, 2, 3, 3, 3, 5]

### Example 2: Small Range

Sort the array A = [1, 4, 1, 2, 7, 5, 2] using Counting Sort.

**Solution:**
k = 7, C = [0, 0, 0, 0, 0, 0, 0, 0]
Count: C[1]=2, C[2]=2, C[4]=1, C[5]=1, C[7]=1
After cumulative: C[0]=0, C[1]=2, C[2]=4, C[3]=4, C[4]=5, C[5]=6, C[6]=6, C[7]=7
Placing elements (right to left): B = [1, 1, 2, 2, 4, 5, 7]

### Example 3: Stability Demonstration

Sort these pairs by age: [(John, 25), (Mary, 23), (Alice, 25), (Bob, 23)].

**Solution:**
Ages: [25, 23, 25, 23]
After Counting Sort: B = [23, 23, 25, 25]
Because we process right-to-left, both 23s and both 25s maintain input order.
Output: [(Mary, 23), (Bob, 23), (John, 25), (Alice, 25)]

## Exam Tips

1. **Understand the difference between comparison-based and non-comparison sorts**: Counting Sort does not use comparisons between elements, which allows it to bypass the Ω(n log n) lower bound.

2. **Remember the time complexity formula**: O(n + k) where n is array size and k is the range. This simplifies to O(n) only when k = O(n).

3. **Stability is crucial**: Always process from right to left to maintain stability. This frequently appears in exam questions asking why we traverse in reverse.

4. **Space complexity matters**: In interviews and exams, mention that Counting Sort requires O(n + k) space, making it unsuitable when k >> n.

5. **Know when to apply Counting Sort**: It works best for small integer ranges, not for large numbers or floating-point values without preprocessing.

6. **Connection to Radix Sort**: Counting Sort serves as the inner sorting algorithm for Radix Sort, which processes digits from least significant to most significant.

7. **Prove stability in exams**: Explain that processing input in reverse ensures that for equal elements, the one appearing later in input gets placed later in output, preserving relative order.

8. **Comparison with other sorts**: Be prepared to compare Counting Sort with QuickSort, MergeSort, and HeapSort regarding time complexity, space complexity, stability, and comparison-based vs distribution-based approaches.