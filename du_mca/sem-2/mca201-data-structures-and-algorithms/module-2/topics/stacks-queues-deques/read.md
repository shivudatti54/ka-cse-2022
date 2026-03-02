# Stacks, Queues, and Deques

## Introduction
Stacks, queues, and deques are fundamental linear data structures in computer science that enforce specific insertion/removal policies. Their constrained access patterns make them ideal for solving numerous computational problems efficiently.

Stacks follow Last-In-First-Out (LIFO) principle, crucial for function call management, undo mechanisms, and syntax parsing. Queues implement First-In-First-Out (FIFO) behavior, essential in job scheduling, buffering, and BFS algorithms. Deques (double-ended queues) allow insertion/removal at both ends, enabling advanced patterns like sliding window algorithms and palindrome checking.

These structures form the building blocks for complex systems - from OS process scheduling to compiler design. Their efficient implementations (O(1) operations) make them indispensable in performance-critical applications.

## Key Concepts
1. **Stack Operations**:
   - Push: Add to top (O(1))
   - Pop: Remove from top (O(1))
   - Peek: View top element
   - Implementation variants: Array-based (fixed size) vs Linked List (dynamic)

2. **Queue Operations**:
   - Enqueue: Add to rear (O(1))
   - Dequeue: Remove from front (O(1))
   - Circular Queue: Efficient array implementation
   - Priority Queue: Specialized variant using heaps

3. **Deque Operations**:
   - AddFront/AddRear
   - RemoveFront/RemoveRear
   - Implementations: Doubly linked list or dynamic array

4. **Time Complexities**:
   - All basic operations: O(1)
   - Search operations: O(n)
   - Space: O(n) for storage

5. **Real-world Applications**:
   - Stack: Browser history, DFS, Tower of Hanoi
   - Queue: Printer spooling, CPU scheduling
   - Deque: Steal-job algorithms, LRU cache

## Examples

**Example 1: Implement Stack using Queues**
```python
class StackUsingQueues:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
    
    def push(self, x):
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1
    
    def pop(self):
        return self.q1.popleft()
```

**Example 2: Circular Queue Implementation**
```java
class CircularQueue {
    private int[] data;
    private int front, rear, size;
    
    public CircularQueue(int k) {
        data = new int[k];
        front = -1; rear = -1;
    }
    
    public boolean enQueue(int value) {
        if (isFull()) return false;
        if (isEmpty()) front = 0;
        rear = (rear + 1) % data.length;
        data[rear] = value;
        return true;
    }
}
```

**Example 3: Deque-Based Palindrome Checker**
```python
def is_palindrome(s):
    dq = deque(s.lower().replace(" ", ""))
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True
```

## Exam Tips
1. Always mention time complexities for operations during implementation questions
2. For array-based implementations, emphasize overflow/underflow checks
3. Remember circular queue's (rear+1)%size calculation pattern
4. In stack-based DFS questions, track visited nodes explicitly
5. For deque problems, consider both front and rear manipulation possibilities
6. Practice edge cases: empty/full structures, single-element cases
7. Real-world application questions often appear - prepare 2-3 examples per structure