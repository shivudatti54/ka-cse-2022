# Learning Objectives

After studying this topic, you should be able to:

1.  Define a circular queue and explain why it is needed compared to a linear queue, specifically addressing the memory wastage problem in linear queues.
2.  Identify and explain the functions of the 'front' and 'rear' pointers in a circular queue implementation.
3.  Explain the concept of circular increment using modular arithmetic with the formula `(index + 1) % capacity` for wrapping pointers.
4.  Trace the step-by-step execution of enqueue and dequeue operations on a circular queue, including pointer updates and wrap-around behavior.
5.  Implement a circular queue in C using an array representation, including the isEmpty, isFull, enqueue, and dequeue functions.
6.  Derive and apply the conditions to check for empty state `(front == -1 && rear == -1)` and full state `((rear + 1) % capacity == front)` in the standard implementation.
7.  Compare and contrast circular queues with linear queues in terms of memory efficiency, time complexity, and use cases.
8.  Justify why one slot is sacrificed in circular queue implementation and explain how this design resolves the ambiguity between full and empty states.
9.  List and describe at least three practical applications of circular queues in real-world systems such as CPU scheduling, buffering, and printer spooling.
