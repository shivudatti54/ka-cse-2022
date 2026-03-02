# Concatenate Two Lists

## Overview

Concatenating two linked lists combines them into a single list by linking the last node of the first list to the first node of the second list. This operation demonstrates list traversal and pointer manipulation to merge data structures.

## Key Points

- **Joining Lists**: Connect tail of first list to head of second list
- **Traversal Required**: Must traverse first list to find its last node, O(n)
- **Simple Link**: Set last node's next pointer to second list's head
- **Head Preservation**: First list's head remains as combined list's head
- **Empty List Handling**: If first empty return second, if second empty return first
- **No New Nodes**: Uses existing nodes, only modifies one pointer
- **Result**: Single merged list with all elements from both lists in order

## Important Concepts

- Find last node of first list by traversing until next == NULL
- Link last->next = secondHead to join the lists
- Return firstHead as the new combined list head
- Special cases: either or both lists could be empty
- Order preserved: first list elements followed by second list elements
- Efficient operation changing only one pointer

## Notes

- Practice implementing with proper NULL checks
- Draw diagrams showing before and after concatenation
- Understand time complexity O(n) due to traversal of first list
- Remember to handle all cases: both non-empty, one empty, both empty
- Know that tail pointer in first list would make this O(1) operation
