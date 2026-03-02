# Additional List Operations - Summary

## Key Definitions and Concepts

- **Concatenation**: Joining two linked lists by connecting the last node of the first list to the head of the second list
- **Reversal**: Transforming a linked list so that the head becomes the tail, with all next pointers redirected
- **Nth Node from End**: Finding a node at position n counting backwards from the last node
- **Cycle Detection**: Determining whether a linked list contains a closed loop structure
- **Node Swapping**: Exchanging positions of two nodes by updating their connections rather than values

## Important Formulas and Theorems

- **Floyd's Cycle Algorithm**: Uses two pointers moving at speeds 1x and 2x;相遇 indicates cycle existence
- **Middle Node Finding**: Slow pointer advances 1 step, fast pointer advances 2 steps; when fast reaches end, slow is at middle
- **Two-Pointer Nth-from-End**: Maintain gap of n nodes between two pointers; second pointer reaches end时，第一个指向目标节点

## Key Points

- All basic additional operations achieve O(n) time complexity with O(1) space complexity when designed optimally
- Two-pointer techniques eliminate the need for multiple list traversals in several operations
- NULL pointer checks are essential before any node access to prevent runtime crashes
- Recursive solutions, while elegant, may cause stack overflow for large lists and use O(n) space
- Cycle detection has practical importance in detecting programming errors and system design flaws
- Reversing linked lists is a fundamental technique used in many complex algorithmic problems
- Edge cases (empty list, single node, operation at boundaries) require separate handling in robust code

## Common Mistakes to Avoid

- Forgetting to update the tail pointer after insertion or deletion operations
- Not handling the case when the node to be deleted is the head node
- Losing node references before completing pointer updates (common in reversal and swapping)
- Not accounting for modulo operations when rotation amount exceeds list length
- Assuming list length without traversing or calculating it first

## Revision Tips

- Practice drawing pointer manipulations step-by-step for each operation
- Memorize the two-pointer and runner technique patterns as they apply to multiple problems
- Write and trace code for cycle detection using the tortoise-hare approach
- Focus on understanding why iterative solutions are preferred over recursive ones
- Review previous year question papers to identify frequently examined operations