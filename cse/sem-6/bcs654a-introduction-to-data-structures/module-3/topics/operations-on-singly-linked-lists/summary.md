# Operations on Singly Linked Lists - Summary

## Overview

Singly linked list operations encompass insertion, deletion, traversal, searching, and advanced algorithms including reversal and cycle detection. These operations leverage dynamic memory allocation and pointer manipulation to provide flexible data management capabilities superior to static arrays for certain applications.

## Key Operations and Complexities

| Operation | Beginning | End | Position/Value |
|-----------|-----------|-----|-----------------|
| Insertion | O(1) | O(n) | O(n) |
| Deletion | O(1) | O(n) | O(n) |
| Search | - | - | O(n) |

## Advanced Algorithms

**Reverse Operation:** Uses three-pointer technique (prev, current, next) to reverse direction of each link in single pass. Time: O(n), Space: O(1).

**Find Middle:** Employs slow/fast pointer technique where slow moves one node per iteration and fast moves two. When fast reaches end, slow indicates middle. Time: O(n), Space: O(1).

**Cycle Detection:** Floyd's algorithm uses two pointers at different speeds. If they meet, cycle exists. Mathematical proof establishes that fast pointer will always catch slow pointer within cycle length iterations. Time: O(n), Space: O(1).

## Critical Implementation Details

- Insert at beginning: Create node, point to current head, update head pointer
- Delete operation: Must locate previous node to update its next pointer correctly
- Reverse iteratively: Save next node before modifying current pointer to avoid losing reference
- Two-pointer technique: Solves multiple problems (middle, cycle, palindrome) efficiently
- Edge cases: Always validate empty list, single node, NULL pointers, and out-of-bounds positions
- Memory management: Free deleted nodes to prevent memory leaks; check malloc return values

## Study Notes

Practice drawing pointer diagrams for each operation to visualize memory changes. Master the fundamental pattern: save next pointer, modify current link, advance pointers forward. Memorize time complexities as they frequently appear in technical interviews and examinations. Understand why deletion requires tracking the previous node—key conceptual difference from arrays.

## Proof Summary

**Floyd's Cycle Detection Proof:** Let cycle length be c. When slow enters cycle at position a, fast is somewhere in cycle. Each iteration reduces distance between them by 1. Maximum c iterations guarantee meeting, proving O(n) detection.

**Space Complexity Proof (Reverse):** Only three pointers (prev, current, next) are allocated regardless of list size n, establishing O(1) auxiliary space.