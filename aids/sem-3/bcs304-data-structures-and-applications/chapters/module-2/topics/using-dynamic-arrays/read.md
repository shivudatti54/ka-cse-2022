# Using Dynamic Arrays

## Introduction

Dynamic arrays represent one of the most fundamental data structure implementations in computer science, serving as the backbone for stack and queue operations in countless applications. Unlike static arrays that require fixed memory allocation at compile time, dynamic arrays provide the flexibility of growing and shrinking during program execution, making them ideal for implementing abstract data types like stacks and queues where the size cannot be predicted in advance.

In the context of data structures, using dynamic arrays to implement stacks and queues offers significant advantages over fixed-size array implementations. The primary benefit lies in memory efficiency—developers no longer need to overestimate storage requirements to prevent overflow, nor do they face the limitation of being constrained by a predetermined maximum size. When implementing stacks using dynamic arrays, the array expands automatically when more elements need to be pushed beyond its current capacity, and similarly for queues. This dynamic nature transforms what was once a rigid, fixed-capacity structure into a flexible, self-managing container that adapts to runtime requirements.

The concept becomes particularly important in the University of Delhi's Computer Science curriculum, where understanding the internal workings of data structures is essential for developing efficient software solutions. Dynamic array implementations demonstrate critical concepts including amortized analysis, memory management, and the trade-offs between array-based and linked-list-based implementations. These implementations form the foundation for understanding more complex data structures and algorithms that students will encounter throughout their careers.

## Key Concepts

### Dynamic Array Fundamentals

A dynamic array is a random access, resizable list data structure that allows elements to be added or removed dynamically. Unlike static arrays, dynamic arrays maintain a capacity (the amount of allocated memory) separate from the actual size (the number of elements currently stored). When the size exceeds the capacity, the array must be resized—typically by allocating a new, larger array and copying all existing elements to this new memory location.

The implementation strategy usually involves doubling the capacity when resizing is needed. This approach provides amortized O(1) time complexity for the push operation, meaning while individual operations might occasionally require O(n) time (during resize), the average cost per operation remains constant. The mathematical reasoning behind this lies in the geometric series formed by the copy operations: copying 1 element costs 1 unit, then 2 elements costs 2 units, then 4 costs 4, and so on. The sum of these copy operations across n insertions equals 2n, giving an average cost of O(1) per insertion.

### Stack Implementation Using Dynamic Arrays

A stack is a Last-In-First-Out (LIFO) data structure that supports two primary operations: push (adding an element to the top) and pop (removing the top element). When implementing a stack using dynamic arrays, we maintain an array, a variable tracking the current size, and a variable for capacity.

The push operation first checks if the current size equals the capacity. If true, a resize operation is triggered (typically doubling the capacity). Then the new element is placed at the index equal to the current size, and the size is incremented. The pop operation retrieves the element at index (size - 1), decrements the size, and returns the element. Importantly, we should also consider whether to shrink the array when the size falls significantly below capacity—a common strategy involves reducing capacity by half when size drops to one-fourth of capacity.

### Queue Implementation Using Dynamic Arrays

A queue follows the First-In-First-Out (FIFO) principle, with enqueue (insert at rear) and dequeue (remove from front) operations. Implementing a queue using a simple dynamic array presents a challenge: as elements are dequeued from the front, the front index keeps increasing, eventually reaching the end of the array even when the queue contains few elements. This phenomenon is called "queue desertion."

Two primary solutions exist for this problem. The first involves shifting all elements toward the front after each dequeue operation, but this results in O(n) time complexity for dequeue. The second solution, more efficient, maintains both front and rear indices and treats the array as circular—when the rear index reaches the end, it wraps around to the beginning. This circular array approach, combined with dynamic resizing, provides O(1) amortized time complexity for both enqueue and dequeue operations.

### Memory Management and Resizing Strategies

The efficiency of dynamic array implementations heavily depends on the resizing strategy employed. Three common approaches exist: incremental resizing (increasing capacity by a fixed amount), doubling (doubling capacity when full), and fractional resizing (increasing capacity by a fraction of current capacity).

The choice of strategy significantly impacts performance. Incremental resizing with a small increment leads to O(n) amortized time for push operations because many resize operations occur, each requiring element copying. Doubling provides O(1) amortized time but may waste memory during moderate usage. The optimal strategy often depends on specific use cases and memory constraints.

### Amortized Analysis

Understanding amortized analysis is crucial for evaluating dynamic array performance. Amortized analysis provides a different perspective from worst-case analysis by considering the total cost of a sequence of operations distributed across all operations. For a dynamic array stack, while a single push might require O(n) time during resize, performing n pushes costs only O(n) total, making the amortized cost O(1) per operation.

## Examples

### Example 1: Dynamic Stack Implementation

Consider implementing a dynamic stack to store integers with an initial capacity of 1. We will trace through operations: push(5), push(10), push(15), pop(), push(20), push(25), pop().

Initial state: capacity = 1, size = 0, array = [null]

Push(5): size (0) < capacity (1), so no resize needed. Array becomes [5], size = 1

Push(10): size (1) == capacity (1), resize triggered. New array of capacity 2 allocated, element copied: array = [5, 10], size = 2

Push(15): size (2) == capacity (2), resize triggered again. New array of capacity 4 allocated, both elements copied: array = [5, 10, 15], size = 3

Pop(): Returns element at index 2 (value 15), decrements size to 2. Array remains [5, 10, 15] but size is 2, so effective content is [5, 10]

Push(20): size (2) < capacity (4), no resize. Array becomes [5, 10, 20], size = 3

Push(25): size (3) < capacity (4), no resize. Array becomes [5, 10, 20, 25], size = 4

Pop(): Returns element at index 3 (value 25), size decrements to 3

Final stack contains [5, 10, 20] with top at index 2

### Example 2: Circular Queue with Dynamic Resizing

Implement a circular queue with dynamic arrays starting capacity 4. Operations: enqueue(1), enqueue(2), enqueue(3), dequeue(), dequeue(), enqueue(4), enqueue(5), enqueue(6), enqueue(7)

Initial: front = 0, rear = 0, size = 0, capacity = 4, array = [null, null, null, null]

Enqueue(1): size (0) < capacity (4). Add at rear: array[0] = 1, rear = 1, size = 1

Enqueue(2): array[1] = 2, rear = 2, size = 2

Enqueue(3): array[2] = 3, rear = 3, size = 3

Dequeue(): Remove from front. Return array[0] = 1, front = 1, size = 2. Array now conceptually holds [null, 2, 3, null]

Dequeue(): Return array[1] = 2, front = 2, size = 1. Conceptual content: [null, null, 3, null]

Enqueue(4): rear (3) < capacity (4). array[3] = 4, rear = 4 (or 0 with wrap), size = 2

Enqueue(5): rear (4) equals capacity, need resize. Create new array capacity 8, copy elements starting from front. New array = [3, 4, 5, null...]. front = 0, rear = 3, size = 3

Enqueue(6): array[3] = 6, rear = 4, size = 4

Enqueue(7): array[4] = 7, rear = 5, size = 5

Final queue contains elements [3, 4, 5, 6, 7] in that order

### Example 3: Analyzing Time Complexity

For a dynamic array implementation starting with capacity 1, calculate the total operations required to insert 1000 elements and determine the amortized cost.

The resizing sequence will be: capacity 1 → 2 → 4 → 8 → 16 → 32 → 64 → 128 → 256 → 512 → 1024

Total element copies = 1 + 2 + 4 + 8 + 16 + 32 + 64 + 128 + 256 + 512 = 1023

Total operations (copies + inserts) = 1000 (inserts) + 1023 (copies) = 2023

Amortized cost per operation = 2023 / 1000 ≈ 2.02, which is O(1)

This demonstrates why dynamic arrays achieve constant amortized time despite occasional expensive resize operations.

## Exam Tips

For DU semester examinations, several key points require special attention regarding dynamic array implementations. First, always remember to distinguish between capacity and size—capacity represents allocated memory while size indicates the number of elements actually stored. This distinction frequently appears in exam questions testing conceptual understanding.

Second, be prepared to trace through operations step-by-step, maintaining both front and rear pointers for queues and understanding wrap-around behavior. Examiners commonly present a sequence of operations and ask students to determine the final state of the array or queue.

Third, understanding the mathematical basis for amortized O(1) time complexity is essential. Students should be able to explain why doubling strategy yields constant amortized time rather than just memorizing the result.

Fourth, when comparing array-based and linked-list-based implementations, remember that arrays provide better cache locality and O(1) random access, while linked lists offer O(1) insertion/deletion at known positions and no memory wastage from resizing.

Fifth, edge cases deserve special attention—operations on empty structures (underflow) and operations when the structure is full (overflow in fixed-size implementations, automatic resize in dynamic implementations).

Sixth, the circular queue concept is particularly important as it enables O(1) dequeuing without element shifting. Students must understand how front and rear indices move and when wrap-around occurs.

Seventh, memory leak prevention through proper deallocation should not be overlooked, especially in C/C++ implementations where the student is responsible for memory management.

Finally, practice drawing memory representations showing how elements are stored, which indices are valid, and what values the pointers hold after each operation.