# Linked Lists: Additional List Operations - Summary

## Key Definitions and Concepts

- CONCATENATION: Joining two linked lists by linking the last node of the first list to the head of the second list, creating a single combined list

- REVERSAL: Transforming a linked list so each node's next pointer references the previous node instead of the next, effectively inverting the list direction

- TWO-POINTER TECHNIQUE: Using two pointers moving at different speeds (or positions) to solve problems in single pass, commonly applied in finding nth from end and cycle detection

- CYCLE/LOOP: A condition where traversal never terminates because some node's next pointer references a previously visited node

- FLOYD'S ALGORITHM: Cycle detection using slow and fast pointers moving at different speeds; if they meet, a cycle exists

## Important Formulas and Theorems

- Finding nth from end: Move fast pointer n positions ahead, then move both simultaneously until fast reaches NULL

- Cycle detection: If slow and fast pointers meet during traversal, a cycle exists in the linked list

- Cycle start finding: Reset one pointer to head, move both one step at a time; they meet at cycle origin

- Middle element: When fast reaches NULL, slow is at the middle (for odd length) or second middle (for even length)

- Splitting list: When fast reaches end, slow is at the division point between first and second halves

## Key Points

- Concatenation takes O(n) time to find the tail of the first list; the actual linking is O(1)

- Iterative reversal uses O(n) time and O(1) space; recursive reversal uses O(n) stack space

- The two-pointer technique converts O(2n) two-pass solutions into O(n) single-pass solutions

- Floyd's cycle detection guarantees O(n) time and O(1) space complexity

- Removing duplicates from sorted lists requires only pointer manipulation, no extra memory needed

- Circular linked lists never have NULL pointers; traversal must use cycle detection conditions

- Always handle edge cases: empty list, single node, operation at head/tail positions

## Common Mistakes to Avoid

- Losing access to remaining nodes by not saving the next pointer before modifying current->next

- Not handling edge cases, particularly when n equals list length or exceeds it

- Using recursive solutions without considering stack overflow for large lists

- Forgetting to set the last node's next to NULL when splitting a list, creating unintended cycles

- Not checking for NULL pointers before dereferencing, causing segmentation faults

## Revision Tips

- Practice drawing pointer manipulations on paper—this develops muscle memory for exam problems

- Memorize the two-pointer patterns: they apply to multiple operations and are frequently asked

- Write out the complete code for reversal, nth-from-end, and cycle detection from memory

- Understand why O(1) space solutions matter; examiners frequently ask for optimization

- Review the mathematical relationship in cycle detection: understanding the proof helps retention