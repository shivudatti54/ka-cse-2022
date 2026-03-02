# Double-Ended Queues (Deque)

## Overview

A double-ended queue (deque) is a flexible queue variation allowing insertion and deletion at both front and rear ends. This provides versatility for algorithms requiring access from either end while maintaining queue structure.

## Key Points

- **Dual-End Operations**: Insert and delete possible at both front and rear
- **Four Main Operations**: insertFront, insertRear, deleteFront, deleteRear
- **Input-Restricted Deque**: Insertion at one end only, deletion from both ends
- **Output-Restricted Deque**: Insertion at both ends, deletion from one end only
- **Flexibility**: Can function as both stack and queue
- **Applications**: A-Steal work scheduling, palindrome checking, sliding window problems
- **Implementation**: Can use doubly linked list or circular array

## Important Concepts

- Combines capabilities of both stack and queue
- More operations than regular queue but same O(1) complexity
- Input-restricted allows controlled insertion with flexible removal
- Output-restricted allows flexible insertion with controlled removal
- Palindrome checking uses symmetrical insertion and deletion
- Sliding window algorithms efficiently use deque for maintaining elements

## Notes

- Understand difference between input-restricted and output-restricted variants
- Practice operations showing elements can be added/removed from either end
- Know applications that specifically benefit from dual-end access
- Be able to compare deque with regular queue and stack
- Remember deque provides maximum flexibility among linear structures
