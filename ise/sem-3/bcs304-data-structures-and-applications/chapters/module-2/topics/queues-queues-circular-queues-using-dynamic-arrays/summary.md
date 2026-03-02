# **Queues: Queues, Circular Queues, Using Dynamic Arrays, Multiple Stacks and queues**

## **Key Concepts**

- **Definition of a Queue**: A linear data structure that follows the FIFO (First-In-First-Out) principle, where elements are added at one end (enqueue) and removed from the other end (dequeue).
- **Queue Operations**:
  - Enqueue (add)
  - Dequeue (remove)
  - Peek (view front element)
  - Is Empty
  - Is Full
- **Properties of a Queue**:
  - FIFO (First-In-First-Out)
  - LIFO (Last-In-First-Out) for circular queues
- **Types of Queues**:
  - Linear Queue
  - Circular Queue
  - Stack (special case of queue)
- **Using Dynamic Arrays**: Representing queues using dynamic arrays, where elements are added and removed from the ends.
- **Multiple Stacks and Queues**: Implementing queues using multiple stacks, where elements are added and removed from the top of the stack.

## **Formulas and Theorems**

- **Queue Formula**:
  - | | = | | (size of queue)
  - | | = | (queue is empty) or | | > 0 (queue is not empty)
- **Circular Queue Formula**:
  - | | = | | (mod n) (where n is the size of the queue)
  - | | = | (queue is empty) or | | > 0 (queue is not empty)

## **Important Notes**

- The time complexity of queue operations is O(1) for dequeue and enqueue, and O(n) for peek and is empty.
- The space complexity of queue operations is O(n), where n is the number of elements in the queue.
- Circular queues have the same operations as linear queues, but with the added complexity of dealing with the circular nature of the data structure.
