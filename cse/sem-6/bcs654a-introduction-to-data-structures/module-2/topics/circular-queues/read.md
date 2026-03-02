# Circular Queues

## Introduction to Circular Queues

A Circular Queue, also known as a Ring Buffer, is a linear data structure that follows the First-In-First-Out (FIFO) principle. Unlike a standard linear queue, a circular queue treats its underlying array as if the first and last elements are connected, forming a circle. This design overcomes a major limitation of linear queue implementations using arrays: inefficient space utilization.

In a standard linear queue, when elements are dequeued from the front, the space they occupied becomes unused. Even if there's empty space at the front, new elements can only be enqueued at the rear. A circular queue solves this problem by reusing the empty spaces created at the front after dequeuing operations.

## Key Concepts and Terminology

- **Front (Head):** The index pointing to the first element in the queue, the one to be dequeued next.
- **Rear (Tail):** The index pointing to the last element in the queue, where the next element will be enqueued.
- **Enqueue:** The operation of adding an element to the rear of the queue.
- **Dequeue:** The operation of removing an element from the front of the queue.
- **Capacity:** The maximum number of elements the queue can hold.
- **Circular Increment:** The mechanism to move the `front` or `rear` pointer to the next position, wrapping around to the start of the array when the end is reached. This is typically done using modulo arithmetic (`index = (index + 1) % capacity`).

## Operations on Circular Queues

The primary operations on a circular queue are:

1. **`enqueue(value)`**: Adds an element `value` to the rear of the queue.
2. **`dequeue()`**: Removes and returns the element from the front of the queue.
3. **`isEmpty()`**: Checks if the queue is empty.
4. **`isFull()`**: Checks if the queue is full.
5. **`peek()` / `front()`**: Returns the element at the front without removing it.

### Implementation Details (Using Arrays)

A circular queue is implemented using an array and two integer pointers: `front` and `rear`.

**Initial State:**
Both `front` and `rear` are set to -1, indicating an empty queue.

```
Queue: [ -, -, -, -, - ] (Capacity = 5)
front = -1
rear = -1
```

**Enqueue Operation:**

1. Check if the queue is full.
2. For the first element, set both `front` and `rear` to 0.
3. For subsequent elements, update the `rear` pointer using circular increment: `rear = (rear + 1) % capacity`.
4. Insert the new element at `array[rear]`.

**Dequeue Operation:**

1. Check if the queue is empty.
2. Retrieve the value from `array[front]`.
3. If the queue has only one element (`front == rear`), reset the queue by setting both to -1.
4. Otherwise, update the `front` pointer using circular increment: `front = (front + 1) % capacity`.

**Checking for Full and Empty Conditions:**
This is the most critical aspect. The conditions differ based on the implementation strategy. A common and efficient approach is to always keep one slot empty to distinguish between the full and empty states.

- **`isEmpty()`**: `(front == -1 && rear == -1)` OR `(front == rear)` (if using a different strategy)
- **`isFull()`**: `((rear + 1) % capacity == front)`

**Why keep one slot empty?** If `front` and `rear` become equal after an enqueue operation, it would be ambiguous: does it mean the queue is full or empty? Sacrificing one slot resolves this ambiguity.

## Example Walkthrough with ASCII Diagrams

Let's trace the operations on a circular queue of capacity 5.

**1. Initialization:**

```
front = -1
rear = -1
Queue: [ -, -, -, -, - ]
```

**2. Enqueue(10):** (First element)

```
front = 0
rear = 0
Queue: [ 10, -, -, -, - ]
```

**3. Enqueue(20):**

```
rear = (0 + 1) % 5 = 1
front = 0
rear = 1
Queue: [ 10, 20, -, -, - ]
```

**4. Enqueue(30), Enqueue(40):**

```
front = 0
rear = 3
Queue: [ 10, 20, 30, 40, - ]
```

**5. Dequeue():** (Removes 10)

```
front = (0 + 1) % 5 = 1
Value 10 is removed.
Queue: [ -, 20, 30, 40, - ]
front=1, rear=3
```

**6. Enqueue(50):**

```
rear = (3 + 1) % 5 = 4
Queue: [ -, 20, 30, 40, 50 ]
front=1, rear=4
```

**7. Enqueue(60):**

```
rear = (4 + 1) % 5 = 0
Check isFull: (0 == front)? 0 != 1 -> Not full.
Queue: [ 60, 20, 30, 40, 50 ]
front=1, rear=0 <-- Rear has wrapped around!
```

This demonstrates the circular nature. The queue is now logically: `[20@front, 30, 40, 50, 60@rear]`.

**8. Check isFull():**
`(rear + 1) % capacity = (0 + 1) % 5 = 1`. Since `front` is 1, `(1 == 1)` is true. The queue is full.

```
[ 60, 20, 30, 40, 50 ] is considered full (1 slot sacrificed).
```

**9. Dequeue():** (Removes 20)

```
front = (1 + 1) % 5 = 2
Queue: [ 60, -, 30, 40, 50 ]
front=2, rear=0
```

Now, `enqueue(70)` would be possible at index `(0+1)%5=1`.

## Comparison with Linear Queue

| Feature               | Linear Queue                                                                                                                                  | Circular Queue                                                                                                                     |
| :-------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------- |
| **Memory Efficiency** | Poor. Dequeued spaces are wasted.                                                                                                             | Excellent. Reuses dequeued spaces.                                                                                                 |
| **Time Complexity**   | Enqueue: O(1), Dequeue: O(1) (Amortized for dynamic arrays, but worst-case O(n) for shift operations in a simple static array implementation) | Enqueue: O(1), Dequeue: O(1)                                                                                                       |
| **Implementation**    | Simpler. Straightforward increment of pointers.                                                                                               | More complex. Requires modulo arithmetic for pointer updates.                                                                      |
| **Use Case**          | Suitable where the queue size is predictable and fixed, and memory is not a major constraint.                                                 | Essential for scenarios requiring efficient memory usage and continuous data processing (e.g., resource sharing, traffic systems). |

## Applications of Circular Queues

1. **CPU Scheduling:** Operating systems often use circular queues to manage processes in scheduling algorithms like Round Robin.
2. **Memory Management:** Used in buffering data streams, such as in disk scheduling or network traffic management, where a continuous flow of data needs to be handled.
3. **Traffic Signal Systems:** The sequence of light changes can be modeled using a circular queue.
4. **Music Playlists:** A playlist that loops back to the beginning after the last song is played is a real-world example of circular queue logic.
5. **Producer-Consumer Problem:** Circular queues are ideal for a shared buffer where a producer adds data and a consumer removes data concurrently.

## Sample C Code Implementation

```c
#include <stdio.h>
#include <stdlib.h>
#define SIZE 5

typedef struct {
 int items[SIZE];
 int front;
 int rear;
} CircularQueue;

void initializeQueue(CircularQueue *q) {
 q->front = -1;
 q->rear = -1;
}

int isEmpty(CircularQueue *q) {
 return (q->front == -1 && q->rear == -1);
}

int isFull(CircularQueue *q) {
 return ((q->rear + 1) % SIZE == q->front);
}

void enqueue(CircularQueue *q, int value) {
 if (isFull(q)) {
 printf("Queue is full. Cannot enqueue %d\n", value);
 return;
 }
 if (isEmpty(q)) {
 // First element
 q->front = 0;
 q->rear = 0;
 } else {
 q->rear = (q->rear + 1) % SIZE;
 }
 q->items[q->rear] = value;
 printf("Enqueued %d\n", value);
}

int dequeue(CircularQueue *q) {
 if (isEmpty(q)) {
 printf("Queue is empty. Cannot dequeue.\n");
 return -1; // Error value
 }
 int dequeuedValue = q->items[q->front];
 if (q->front == q->rear) {
 // Queue will become empty after this dequeue
 initializeQueue(q);
 } else {
 q->front = (q->front + 1) % SIZE;
 }
 printf("Dequeued %d\n", dequeuedValue);
 return dequeuedValue;
}

void display(CircularQueue *q) {
 if (isEmpty(q)) {
 printf("Queue is empty.\n");
 return;
 }
 printf("Queue elements: ");
 int i = q->front;
 // Traverse from front to rear, handling the wrap-around
 while (1) {
 printf("%d ", q->items[i]);
 if (i == q->rear) break;
 i = (i + 1) % SIZE;
 }
 printf("\n");
}

// Driver code to test the implementation
int main() {
 CircularQueue q;
 initializeQueue(&q);

 enqueue(&q, 10);
 enqueue(&q, 20);
 enqueue(&q, 30);
 enqueue(&q, 40);
 display(&q); // Output: 10 20 30 40

 dequeue(&q); // Removes 10
 dequeue(&q); // Removes 20
 display(&q); // Output: 30 40

 enqueue(&q, 50);
 enqueue(&q, 60);
 enqueue(&q, 70); // This will fail because (rear+1)%SIZE == front -> queue is full
 display(&q); // Output: 30 40 50 60

 return 0;
}
```

## Exam Tips

1. **Remember the Conditions:** Memorize the exact conditions for `isEmpty` and `isFull` for the "one slot empty" implementation. A common mistake is to check `front == rear` for empty, which is only true initially or after a full dequeue in this specific implementation.
2. **Modulo is Key:** The modulo operation `% capacity` is essential for the circular increment. Always use it when updating `front` or `rear`.
3. **Draw Diagrams:** In exams, when asked to trace operations, draw the array and update the pointers step-by-step. This visual aid prevents calculation errors during wrap-around.
4. **Edge Cases:** Pay special attention to the first enqueue (setting both pointers to 0) and the dequeue that leads to an empty queue (resetting both pointers to -1).
5. **Understand the Trade-off:** Be prepared to explain _why_ a circular queue is used instead of a linear one (memory efficiency) and what its limitation is (fixed size, one slot sacrificed).
