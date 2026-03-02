# Synchronization in Java

## Overview

Synchronization in Java is a mechanism that prevents data corruption by ensuring that only one thread can access shared data at a time. The `synchronized` keyword ensures that only one thread can execute a synchronized method or block at a time by using intrinsic locks (monitors) associated with Java objects.

## Key Points

- **Race conditions** occur when multiple threads access/modify shared data concurrently without coordination
- The `synchronized` keyword prevents concurrent access to critical sections of code
- Can be applied to **methods** (entire method synchronized) or **blocks** (finer-grained control)
- Every Java object has an intrinsic lock (monitor) used for synchronization
- When a thread enters a synchronized method/block, it **acquires the lock**
- Other threads attempting to acquire the same lock are **blocked** until the lock is released
- Lock is automatically released when the thread exits the synchronized block/method
- **Deadlocks** can occur when two or more threads are blocked forever, waiting for each other
- **Starvation** can occur when a thread is unable to access a shared resource due to other threads holding onto it for an extended period

## Important Definitions

- **Race Condition**: Unpredictable behavior when multiple threads access shared data simultaneously
- **Monitor**: A synchronization construct that controls access to an object; every Java object can act as a monitor
- **Intrinsic Lock (Monitor Lock)**: A lock associated with every Java object that synchronized code uses
- **Deadlock**: Situation where two or more threads are blocked forever, waiting for each other
- **Starvation**: Situation where a thread is unable to access a shared resource due to other threads holding onto it for an extended period

## Key Formulas / Syntax

```java
// Synchronized Method
synchronized void methodName() { /* code */ }

// Synchronized Block
synchronized(lockObject) { /* code */ }

// wait() and notify() methods
wait();
notify();
notifyAll();
```

## Comparisons

| Feature        | Synchronized Methods                                   | Synchronized Blocks                           |
| -------------- | ------------------------------------------------------ | --------------------------------------------- |
| **Scope**      | Entire method is synchronized                          | Only a specific block of code is synchronized |
| **Lock**       | Lock is acquired on the object the method is called on | Lock is acquired on the specified object      |
| **Efficiency** | Less efficient than synchronized blocks                | More efficient than synchronized methods      |

## Exam Tips

- Remember: **synchronized** keyword is Java's implementation of monitors
- For exams, be prepared to identify race conditions in code snippets and suggest synchronized solutions
- Synchronized blocks are more efficient than synchronized methods as they lock only the critical section
- The lock is automatically released when the method/block completes or throws an exception
- Multiple locks can exist simultaneously on different objects for different threads
- Be aware of potential deadlocks and starvation scenarios in multithreaded programming.
