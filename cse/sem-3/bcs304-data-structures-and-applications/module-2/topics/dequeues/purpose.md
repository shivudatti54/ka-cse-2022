# Learning Objectives

After studying this topic, you should be able to:

1. Define a deque (double-ended queue) and distinguish it from standard queues and stacks in terms of allowed operations
2. Identify and explain the four primary operations of a deque: insertFront, insertRear, deleteFront, and deleteRear
3. Differentiate between input-restricted deque and output-restricted deque by listing which operations are permitted in each type
4. Explain why circular arrays are used in deque implementation and describe how the modulo operator enables index wrap-around
5. Implement the insertFront, insertRear, deleteFront, and deleteRear operations using circular array logic with correct index calculations
6. Trace through a sequence of deque operations to determine the final array state, front index, rear index, and element order
7. Analyze how a deque can simulate both stack (LIFO) and queue (FIFO) operations using appropriate combinations of insertion and deletion
8. Evaluate real-world applications (palindrome checking, sliding window maximum, undo-redo systems) to determine where a deque is the appropriate data structure
