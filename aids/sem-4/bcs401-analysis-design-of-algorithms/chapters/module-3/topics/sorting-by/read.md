# Sorting by Distribution

## Introduction

Sorting by distribution represents a fundamental paradigm in the field of algorithm design, distinct from comparison-based sorting methods like quicksort or mergesort. While comparison-based sorting algorithms have a theoretical lower bound of Ω(n log n) time complexity, distribution-based sorting algorithms can achieve linear time O(n) under certain conditions by leveraging the structure and properties of the input data.

The Transform-and-Conquer design technique underlies many distribution sorting algorithms, where the problem is transformed into a simpler form before solving. In the context of sorting by distribution, the key transformation involves mapping elements to a discrete range of indices based on their key values, allowing for efficient placement without direct comparisons between elements. This approach exemplifies the Space-Time Tradeoff principle—using additional memory space to achieve superior time performance.

Understanding distribution sorting is crucial for computer science students at Delhi University, as these algorithms form the backbone of many real-world applications including database indexing, radix sort implementations, and efficient searching operations. The ability to choose between comparison-based and distribution-based sorting based on input characteristics demonstrates advanced algorithmic thinking essential for competitive programming and technical interviews.

## Key Concepts

### Fundamental Principle of Distribution Sorting

Distribution sorting algorithms work by distributing elements into multiple buckets or bins based on their key values, then processing each bucket individually. The core idea involves three main steps: distribution (placing elements into buckets based on some property), sorting within buckets (often using another sorting algorithm or exploiting ordered properties), and concatenation (merging all buckets in order).

The effectiveness of distribution sorting depends critically on the range of possible key values relative to the number of elements. When the range is relatively small (O(n)), these algorithms achieve O(n) time complexity. When the range is large, the performance degrades, making it essential to analyze input characteristics before selecting an appropriate algorithm.

### Counting Sort

Counting Sort is the quintessential distribution-based sorting algorithm that works optimally when the range of input values (k) is not significantly larger than the number of elements (n). The algorithm creates a counting array of size k+1, where each position stores the count of occurrences of that particular value. By accumulating these counts, we can determine the final positions of each element.

The algorithm maintains stability—the property that equal elements maintain their relative order from input to output—which is crucial for applications like multi-level sorting. Counting Sort achieves O(n + k) time complexity and O(n + k) space complexity, making it preferable over O(n log n) comparison sorts when k = O(n).

### Radix Sort

Radix Sort extends the distribution sorting principle to handle larger key ranges by processing keys digit-by-digit or character-by-character. The algorithm can be implemented in two ways: Least Significant Digit (LSD) first or Most Significant Digit (MSD) first. LSD radix sort typically uses counting sort as the subroutine for sorting by individual digits, while MSD radix sort often uses recursion with smaller subproblems.

The time complexity of Radix Sort is O(d(n + k)), where d is the number of digits and k is the base (radix). For fixed-length keys with n elements, this becomes O(n). The space complexity remains O(n + k), and stability depends on the underlying sorting algorithm used for digit sorting.

### Bucket Sort

Bucket Sort distributes elements uniformly across a fixed number of buckets using a hash function or mathematical mapping. When the input is uniformly distributed over an interval, the expected number of elements per bucket becomes O(1), leading to O(n) average-case performance. Insertion Sort or another efficient algorithm typically sorts elements within each bucket.

The effectiveness of Bucket Sort hinges critically on the quality of distribution. Poor distribution (where all elements fall into few buckets) degenerates to O(n²) complexity, while good distribution achieves linear expected time. This demonstrates the practical importance of understanding input distributions when selecting sorting algorithms.

### Stability in Distribution Sorting

Stability refers to the preservation of relative order among equal elements during sorting. Counting Sort and Radix Sort (when implemented with stable subroutines) are inherently stable, making them suitable for secondary sort operations. This property is essential in scenarios where multiple sorting passes are applied, such as sorting records by multiple keys.

## Examples

### Example 1: Counting Sort on Integer Array

Problem: Sort the array [2, 5, 3, 2, 4, 5, 1, 3] using Counting Sort.

Solution:
Step 1: Find the range
Maximum value = 5, Minimum value = 1
Range k = 5

Step 2: Create and populate count array
Initialize count[0 to 5] = [0, 0, 0, 0, 0, 0]
Traverse input array:
count[2]++ → count[2] = 1
count[5]++ → count[5] = 1
count[3]++ → count[3] = 1
count[2]++ → count[2] = 2
count[4]++ → count[4] = 1
count[5]++ → count[5] = 2
count[1]++ → count[1] = 1
count[3]++ → count[3] = 2
Final count array: [0, 1, 2, 2, 1, 2]

Step 3: Compute cumulative counts
count[1] = 1
count[2] = 1 + 2 = 3
count[3] = 3 + 2 = 5
count[4] = 5 + 1 = 6
count[5] = 6 + 2 = 8

Step 4: Build output array (traverse input in reverse for stability)
Starting from right: index 7, value 3
Position = count[3] - 1 = 5 - 1 = 4
output[4] = 3, count[3] = 4
Continuing similarly...
Final sorted array: [1, 2, 2, 3, 3, 4, 5, 5]

### Example 2: LSD Radix Sort

Problem: Sort [329, 457, 657, 839, 436, 720, 355] using LSD Radix Sort with base 10.

Solution:
Pass 1 (ones digit):
329→9, 457→7, 657→7, 839→9, 436→6, 720→0, 355→5
Distribution into buckets 0-9:
Bucket 0: [720]
Bucket 5: [355]
Bucket 6: [436]
Bucket 7: [457, 657]
Bucket 9: [329, 839]
Concatenation: [720, 355, 436, 457, 657, 329, 839]

Pass 2 (tens digit):
720→2, 355→5, 436→3, 457→5, 657→5, 329→2, 839→3
Distribution:
Bucket 2: [720, 329]
Bucket 3: [436, 839]
Bucket 5: [355, 457, 657]
Concatenation: [720, 329, 436, 839, 355, 457, 657]

Pass 3 (hundreds digit):
720→7, 329→3, 436→4, 839→8, 355→3, 457→4, 657→6
Distribution:
Bucket 3: [329, 355]
Bucket 4: [436, 457]
Bucket 6: [657]
Bucket 7: [720]
Bucket 8: [839]
Concatenation: [329, 355, 436, 457, 657, 720, 839]

Final sorted array: [329, 355, 436, 457, 657, 720, 839]

### Example 3: Bucket Sort with Uniform Distribution

Problem: Sort [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68] into 10 buckets.

Solution:
Step 1: Distribute elements into buckets using key = floor(10 × value)
0.78 → floor(7.8) = 7
0.17 → floor(1.7) = 1
0.39 → floor(3.9) = 3
0.26 → floor(2.6) = 2
0.72 → floor(7.2) = 7
0.94 → floor(9.4) = 9
0.21 → floor(2.1) = 2
0.12 → floor(1.2) = 1
0.23 → floor(2.3) = 2
0.68 → floor(6.8) = 6

Buckets:
Bucket 0: []
Bucket 1: [0.17, 0.12]
Bucket 2: [0.26, 0.21, 0.23]
Bucket 3: [0.39]
Bucket 4: []
Bucket 5: []
Bucket 6: [0.68]
Bucket 7: [0.78, 0.72]
Bucket 8: []
Bucket 9: [0.94]

Step 2: Sort each bucket (using insertion sort)
Bucket 1: [0.12, 0.17]
Bucket 2: [0.21, 0.23, 0.26]
Bucket 6: [0.68]
Bucket 7: [0.72, 0.78]
Bucket 9: [0.94]

Step 3: Concatenate in order
Final sorted array: [0.12, 0.17, 0.21, 0.23, 0.26, 0.39, 0.68, 0.72, 0.78, 0.94]

## Exam Tips

1. TIME COMPLEXITY DISTINCTIONS: Remember that Counting Sort achieves O(n + k), Radix Sort achieves O(d(n + k)), and Bucket Sort achieves O(n) average case. Always specify the conditions under which these complexities hold.

2. STABILITY MATTERS: Counting Sort and Radix Sort (with stable inner sort) are stable, while Bucket Sort's stability depends on the inner sorting algorithm used. Stability is often tested in exam questions.

3. WHEN TO USE WHAT: Use Counting Sort when range k = O(n), use Radix Sort for fixed-length keys with larger ranges, and use Bucket Sort when input is uniformly distributed over a known range.

4. COMPARISON VS DISTRIBUTION: Remember the fundamental difference—distribution sorting doesn't compare elements directly but uses key-based mapping, breaking the Ω(n log n) barrier.

5. RADIX SORT VARIANTS: LSD Radix Sort produces correct results for any base when sorting equal-length strings/numbers, while MSD Radix Sort requires careful handling of variable-length keys.

6. PRACTICAL CONSIDERATIONS: In real implementations, the constant factors for distribution sorting can be higher than comparison sorts, making quicksort preferable for small datasets despite theoretical advantages.

7. SPACE-TIME TRADEOFF: All distribution sorting algorithms use O(n + k) auxiliary space, demonstrating the classic space-time tradeoff principle in algorithm design.

8. STABILITY IMPLEMENTATION: For Counting Sort, traverse the input array from right to left to ensure stability in the output array—this is a common exam requirement.