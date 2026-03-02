# Using isAlive() and join()

## Overview

The `isAlive()` method in Java is used to check whether a thread is still executing. It returns `true` if the thread has been started but not yet reached its `run()` method completion. This is useful for coordinating between threads in multi-threaded programs. The `join()` method is used to wait for a thread to complete its execution.

## Key Points

- **isAlive()** returns `true` when thread is started and not yet finished; returns `false` before start or after completion
- The method is typically used in the main thread to poll and wait for child thread completion
- Combining `isAlive()` with `Thread.sleep()` creates a polling mechanism
- **join()** is the preferred method over isAlive() for waiting on thread completion
- join() blocks the calling thread until the target thread terminates completely
- **Thread Priorities**: Threads have priorities that determine their execution order
- **Synchronization**: Mechanism to ensure data consistency in multithreaded programs

## Important Definitions

- **Thread**: A lightweight subprocess; smallest unit of execution in Java
- **isAlive()**: Method that checks if a thread is currently executing
- **join()**: Method that waits for a thread to complete before continuing
- **Polling**: Repeatedly checking a condition (like isAlive()) in a loop
- **Synchronization**: Mechanism to ensure data consistency in multithreaded programs

## Key Formulas / Syntax

```java
// isAlive() usage
Thread t = new MyThread();
t.start();
while (t.isAlive()) {
 // wait
}

// join() usage (preferred)
t.start();
try {
 t.join();
} catch (InterruptedException e) {}
System.out.println("After thread completion");
```

## Comparisons

| Feature         | isAlive() + Loop         | join() Method              |
| --------------- | ------------------------ | -------------------------- |
| Approach        | Polling (active waiting) | Blocking (passive waiting) |
| CPU Usage       | Wastes CPU cycles        | Efficient                  |
| Code Complexity | More verbose             | Simpler code               |
| Recommended     | Not recommended          | Recommended                |

## Exam Tips

- Remember: isAlive() returns false BEFORE start() and AFTER completion
- join() is the standard way to wait for thread completion in exams
- Always wrap join() and sleep() in try-catch for InterruptedException
- Common question: "Difference between isAlive() and join()"
- Key advantage of join(): it doesn't waste CPU cycles like polling with isAlive()
- Understand thread priorities and synchronization concepts in multithreaded programming.
