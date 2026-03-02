# Introduction to Data Structures - Summary

## Key Definitions and Concepts

- **Data**: Raw, unprocessed facts and figures without context or meaning
- **Information**: Processed, organized, and structured data that provides meaning and context
- **Data Structure**: A way of organizing and storing data that enables efficient access and modification
- **Abstract Data Type (ADT)**: A mathematical model defining a data type by its behavior through operations, without specifying implementation details
- **Algorithm Complexity**: A measure of the amount of resources (time and space) required by an algorithm

## Important Formulas and Theorems

- **Time Complexity (Big-O Notation)**: O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ)
- **Array Access Time**: O(1) - constant time due to direct address calculation
- **Linked List Traversal**: O(n) - requires sequential traversal
- **Binary Search**: O(log n) - divides search space in half each iteration

## Key Points

1. Data structures are classified into primitive (basic types) and non-primitive (derived types)
2. Non-primitive structures are either linear (array, linked list, stack, queue) or non-linear (tree, graph)
3. Abstract Data Types separate interface from implementation, enabling modular software design
4. Time complexity analysis helps predict algorithm performance as input size grows
5. Space complexity considers both input data space and auxiliary space requirements
6. Static data structures have fixed size (allocated at compile time), while dynamic structures grow/shrink at runtime
7. The choice of data structure depends on the operations performed most frequently
8. Common operations on all data structures include traversal, insertion, deletion, search, and sorting

## Common Mistakes to Avoid

1. Confusing data with information - they are not synonymous
2. Assuming one data structure is universally best - the choice depends on specific requirements
3. Ignoring the cost of operations when selecting data structures
4. Neglecting space complexity while focusing only on time complexity
5. Forgetting that Big-O notation describes asymptotic behavior for large inputs

## Revision Tips

1. Create a comparison table of all data structures with their operation complexities
2. Practice identifying whether a given problem requires linear or non-linear data structures
3. Review the Big-O notation hierarchy until you can recite it fluently
4. Relate abstract concepts to real-world examples like library organization, phone contacts, or social networks
5. Solve previous year exam questions on algorithm analysis to reinforce complexity concepts