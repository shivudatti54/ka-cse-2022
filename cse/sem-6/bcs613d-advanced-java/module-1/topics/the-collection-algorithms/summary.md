# Collection Algorithms

## Overview

The Collections class provides static utility methods (algorithms) that operate on collections, including sorting, searching, shuffling, and finding extreme values. These polymorphic algorithms work with any collection implementing appropriate interfaces and provide optimized O(n log n) sorting and O(log n) binary search.

## Key Points

- **Sorting**: Collections.sort() uses modified mergesort with O(n log n) complexity
- **Binary Search**: Collections.binarySearch() requires sorted list, returns index or insertion point
- **Shuffling**: Collections.shuffle() randomly permutes list elements
- **Min/Max**: Collections.min() and max() find extreme values in O(n) time
- **Frequency**: Collections.frequency() counts occurrences of specified element
- **Copying**: Collections.copy() copies elements from source to destination list
- **Reverse**: Collections.reverse() reverses order of elements in list
- **Disjoint**: Collections.disjoint() checks if two collections have no common elements

## Important Concepts

- Arrays.sort() for arrays, Collections.sort() for Lists
- Binary search returns negative value if not found: -(insertion point) - 1
- List must be sorted before binary search, otherwise results undefined
- Arrays.asList() returns fixed-size list backed by array
- Arrays.toString() for printing, Arrays.deepToString() for multi-dimensional
- Arrays.equals() for comparison, Arrays.deepEquals() for nested arrays

## Notes

- Remember: binary search only works on sorted collections
- Arrays.asList() creates fixed-size list - can't add/remove elements
- Know time complexity: sort O(n log n), binary search O(log n)
