# Reverse a List Without Creating New Node

## Overview

Reversing a linked list in-place involves changing the direction of next pointers without allocating new nodes. This fundamental operation demonstrates advanced pointer manipulation using three pointers to traverse and reverse links in a single pass.

## Key Points

- **In-Place Reversal**: Changes existing pointers without creating new nodes or using extra space
- **Three Pointers**: Uses prev, current, and next pointers for traversal and reversal
- **Algorithm**: Save next, reverse current's link, move all three pointers forward
- **Time Complexity**: O(n) single pass through list
- **Space Complexity**: O(1) only three pointer variables used
- **Final Step**: Update head to prev pointer after complete traversal
- **Iterative Approach**: Loop continues until current becomes NULL

## Important Concepts

- Initialize prev to NULL, current to head, next to NULL before loop
- In each iteration: save next node, reverse current link, advance all pointers
- Reversal happens by setting current->next = prev
- After reversal, original head becomes tail, original tail becomes head
- No new memory allocation required, pure pointer manipulation
- Final head update crucial: head = prev after loop completion

## Notes

- Practice tracing algorithm step-by-step with diagrams
- Understand the three-pointer dance: save, reverse, advance
- Remember initialization: prev=NULL is key to terminating reversed list
- Draw before and after diagrams showing reversed pointers
- Know this is standard interview question requiring O(1) space solution
