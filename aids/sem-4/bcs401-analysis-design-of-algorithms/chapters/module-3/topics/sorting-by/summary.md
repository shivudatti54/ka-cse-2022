# Sorting by Distribution - Summary

## Key Definitions and Concepts
- DISTRIBUTION SORTING: A sorting paradigm that maps elements to bucket indices based on key values, achieving better than O(n log n) complexity under specific conditions
- COUNTING SORT: Non-comparative sorting algorithm using count array to determine positions, optimal when range k = O(n)
- RADIX SORT: Processes keys digit-by-digit using a stable subroutine, achieving O(d(n + k)) complexity
- BUCKET SORT: Distributes elements into buckets using a hash function, achieving O(n) average case for uniform distributions
- STABILITY: Property ensuring equal elements maintain relative order; critical for multi-pass sorting operations

## Important Formulas and Theorems
- Counting Sort Time: O(n + k) where k is the range of input values
- Radix Sort Time: O(d(n + k)) where d is number of digits and k is the radix base
- Bucket Sort Average Time: O(n + k) when distribution is uniform
- Lower Bound: Distribution sorting can exceed Ω(n log n) because it doesn't rely solely on element comparisons

## Key Points
- Distribution sorting breaks the comparison-based sorting barrier by exploiting key structure
- Counting Sort requires knowing the range beforehand and uses O(n + k) auxiliary space
- Radix Sort treats sorting as multiple passes of stable digit sorting; LSD works for any equal-length keys
- Bucket Sort performance degrades severely with poor distribution; input analysis is essential
- All distribution sorts trade space for time, exemplifying the Space-Time Tradeoff principle
- Stability in Counting Sort requires backward traversal during output placement
- Practical implementation constants often favor quicksort for small n despite theoretical advantages

## Common Mistakes to Avoid
- Confusing the time complexity formulas or applying them under wrong conditions
- Forgetting that distribution sorting requires additional space proportional to range
- Not considering stability requirements when selecting sorting algorithms
- Applying Bucket Sort to non-uniformly distributed data without analyzing consequences
- Overlooking the constant factors that make distribution sort slower for small datasets

## Revision Tips
- Practice implementing Counting Sort from scratch, focusing on cumulative count calculation
- Work through Radix Sort examples with different digit positions to understand the passes
- Compare distribution sorting with comparison sorting using various input sizes and ranges
- Memorize the conditions under which each distribution sort outperforms comparison sorts
- Review past DU examination questions on this topic for pattern recognition