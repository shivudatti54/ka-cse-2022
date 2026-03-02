# Linear Search

## Overview

Linear search is the simplest searching algorithm that sequentially checks each element in a collection until finding the target or reaching the end. It works on both sorted and unsorted data but has O(n) time complexity.

## Key Points

- **Sequential Access**: Check elements one by one from beginning to end
- **Works on Any Data**: No requirement for sorted or organized data
- **Time Complexity**: O(n) worst and average case, O(1) best case (element at beginning)
- **Space Complexity**: O(1) using only few variables
- **Algorithm**: Loop through array, compare each element with target
- **Termination**: Return index when found, return -1 if entire array traversed
- **Simple Implementation**: Easy to understand and code, no preprocessing needed

## Important Concepts

- Best case: element at first position, 1 comparison
- Worst case: element at last position or not present, n comparisons
- Average case: element in middle, n/2 comparisons
- Suitable for small datasets or unsorted data
- No advantage for sorted data unlike binary search
- Can be used on any data structure supporting sequential access

## Notes

- Practice implementing for both arrays and linked lists
- Understand when linear search is appropriate choice
- Know advantages: simplicity, works on unsorted data
- Know disadvantages: slow for large datasets
- Be able to trace algorithm showing comparisons made
