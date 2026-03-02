# Interthread Communication in Java

## Overview

Interthread communication allows threads to cooperate and share data safely. Java provides `wait()`, `notify()`, and `notifyAll()` methods (from Object class) for this purpose. These methods must be called from within a **synchronized context** to avoid race conditions.

## Key Points

- **wait()** — Thread releases the lock and enters waiting state until notified.
- **notify()** — Wakes up exactly one waiting thread (chosen by JVM).
- **notifyAll()** — Wakes up all waiting threads; they compete for the lock.
- Must always be called from **synchronized block or method** (IllegalMonitorStateException otherwise).
- Always use **wait() inside a while loop** to handle spurious wakeups.
- When notified, thread moves to **blocked state** and re-acquires the lock before resuming.
- Producer-Consumer problem is the classic use case for interthread communication.
- Threads can be suspended, resumed, or stopped using `suspend()`, `resume()`, and `stop()` methods.

## Important Definitions

- **Spurious Wakeup**: A wakeup without notify() being called; always check condition in while loop.
- **IllegalMonitorStateException**: Thrown when wait()/notify() called without owning the object's lock.
- **Blocking State**: Thread state when waiting for lock after being notified.
- **Synchronization**: Mechanism to control access to shared resources by multiple threads.

## Key Formulas / Syntax

```java
synchronized void produce(int value) {
 while (hasData) {
 try {
 wait();
 } catch (InterruptedException e) {
 }
 }
 data = value;
 hasData = true;
 notify();
}

synchronized int consume() {
 while (!hasData) {
 try {
 wait();
 } catch (InterruptedException e) {
 }
 }
 hasData = false;
 notify();
 return data;
}
```

## Comparisons

| Method        | Description                                | Use Case                           |
| ------------- | ------------------------------------------ | ---------------------------------- |
| `wait()`      | Releases the lock and waits until notified | Waiting for a condition to be met  |
| `notify()`    | Wakes up one waiting thread                | Signaling a waiting thread         |
| `notifyAll()` | Wakes up all waiting threads               | Signaling multiple waiting threads |

## Exam Tips

- Remember: **wait() releases lock**, notify() only signals — it does NOT release lock.
- Always use **while loop** with wait(), not if statement ( exam frequently tests this).
- The thread that gets notified first depends on JVM scheduling — not predictable.
- These methods belong to **Object class**, not Thread class.
- Common question: "Why wait() is always used in a while loop?" — Answer: To handle spurious wakeups.
- Be prepared to explain the Producer-Consumer problem and its solution using interthread communication.
