# Linked Lists: Additional List Operations - Summary

## Key Definitions and Concepts

- TWO-POINTER TECHNIQUE: Using two pointers moving at different speeds (slow by 1, fast by 2) to solve problems in single traversal
- FLOYD'S CYCLE DETECTION: Algorithm using slow and fast pointers to detect loops in O(n) time
- IN-PLACE REVERSAL: Modifying links without creating new nodes, achieving O(1) auxiliary space

## Important Formulas and Theorems

- Middle element: Use condition `while(fast && fast->next)` for traversal
- Nth from end: Move fast pointer k-1 steps ahead, then move both until fast reaches end
- Cycle start: Reset slow to head after detection, move both by one until they meet at cycle origin
- Merge complexity: O(m + n) where m and n are list lengths

## Key Points

- Reversal requires three pointers: previous, current, and next to preserve list access during modification
- Two-pointer approach finds middle in single pass without storing addresses or counting nodes
- For Nth from end, handle cases where n exceeds list length by checking pointer validity
- Floyd's algorithm detects cycles but requires additional steps to find cycle start point
- Merging sorted lists uses a dummy node to simplify head pointer management
- Removing duplicates from sorted lists compares consecutive nodes; unsorted lists require different approaches
- All operations aim for O(n) time and O(1) space unless problem specifies otherwise

## Common Mistakes to Avoid

- Losing reference to next node before changing current->next pointer during reversal
- Not handling empty list or single-node list as edge cases in all operations
- Incorrect fast pointer movement conditions leading to NULL pointer dereference
- Forgetting to set tail pointer to NULL after reversal or cycle removal

## Revision Tips

- Practice drawing pointer diagrams for each operation—this clarifies the logic
- Memorize the two-pointer template as it applies to multiple problems
- Focus on edge case handling: empty list, single node, operations at head/tail
- Implement all operations from scratch without referring to notes before exams
- Solve at least 5 problems from each operation type to build confidence