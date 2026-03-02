# The RandomAccess Interface

## Overview

RandomAccess is a marker interface (no methods) that indicates a List implementation supports fast constant-time random access to elements. It helps generic algorithms optimize their behavior based on whether indexed access or sequential iteration is more efficient for a particular List type.

## Key Points

- **Marker Interface**: Contains no methods, serves as a tag for runtime type information
- **Performance Indicator**: Signals O(1) indexed access vs O(n) sequential access
- **Classes Implementing**: ArrayList, Vector, Stack, CopyOnWriteArrayList implement RandomAccess
- **Classes Not Implementing**: LinkedList and AbstractSequentialList do not implement it
- **Algorithm Optimization**: Use instanceof check to choose index-based or iterator-based approach
- **Collections Framework Usage**: Collections.binarySearch(), shuffle(), and sort() use RandomAccess checks
- **Index vs Iterator**: For RandomAccess lists use get(i), for others use enhanced for-loop or iterator

## Important Concepts

- ArrayList: get(index) is O(1), LinkedList: get(index) is O(n)
- Enhanced for-loop automatically uses optimal iteration method
- Index-based loop on LinkedList causes O(n²) performance
- Iterator-based access is O(n) for both ArrayList and LinkedList
- Binary search uses different algorithms based on RandomAccess

## Notes

- Remember: RandomAccess has NO methods - it's just a marker
- In exams, know which classes implement RandomAccess (ArrayList yes, LinkedList no)
- Always use enhanced for-loop or iterator for LinkedList traversal
