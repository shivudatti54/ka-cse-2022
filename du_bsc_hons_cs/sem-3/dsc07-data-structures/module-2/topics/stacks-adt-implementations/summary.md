# Stacks ADT Implementations

## Introduction

A **Stack** is a fundamental linear data structure following the **LIFO** (Last In, First Out) principle. It is an Abstract Data Type (ADT) that restricts insertions and deletions to one end called the **top**. This topic is essential in the Delhi University NEP 2024 UGCF syllabus for BSc (Hons) Computer Science.

---

## Key Operations (ADT)

- **push(item)**: Insert element at the top — O(1)
- **pop()**: Remove and return element from top — O(1)
- **peek() / top()**: View element at top without removing — O(1)
- **isEmpty()**: Check if stack is empty — O(1)
- **isFull()**: Check if stack is full (array implementation) — O(1)

---

## Implementation Methods

### 1. Array-Based Implementation (Static)

- Uses a fixed-size array with a **top** pointer initialized to -1
- **Advantages**: Simple, no memory overhead per element, fast access
- **Disadvantages**: Fixed capacity, limited size, stack overflow possible
- **Space Complexity**: O(n)

### 2. Linked List-Based Implementation (Dynamic)

- Uses nodes with data and pointer to next node; **top** points to first node
- **Advantages**: Dynamic size (no fixed limit), no overflow (until memory), efficient memory usage
- **Disadvantages**: Extra memory for pointers, slightly complex implementation
- **Space Complexity**: O(n)

---

## Time & Space Complexity

| Operation | Array | Linked List |
|-----------|-------|-------------|
| Push      | O(1)  | O(1)        |
| Pop       | O(1)  | O(1)        |
| Peek      | O(1)  | O(1)        |
| Space     | O(n)  | O(n)        |

---

## Applications

- Expression evaluation (infix, prefix, postfix)
- Function call management (recursion)
- Undo mechanisms in editors
- Parentheses matching
- Backtracking algorithms
- Tower of Hanoi problem

---

## Conclusion

Stack is a crucial ADT with two primary implementations: **array-based** (static, fixed size) and **linked list-based** (dynamic, flexible). Understanding their trade-offs in time and space complexity is vital for exam success and practical programming. Both implementations support O(1) fundamental operations, making stacks efficient for LIFO-based applications.