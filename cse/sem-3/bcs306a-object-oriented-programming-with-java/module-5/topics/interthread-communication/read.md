# Interthread Communication in Java

## Table of Contents

- [Interthread Communication in Java](#interthread-communication-in-java)
- [Introduction](#introduction)
- [The Need for Interthread Communication](#the-need-for-interthread-communication)
- [Methods for Interthread Communication](#methods-for-interthread-communication)
  - [wait()](#wait)
  - [notify()](#notify)
  - [notifyAll()](#notifyall)
- [Synchronized Context Requirement](#synchronized-context-requirement)
- [Producer-Consumer Example](#producer-consumer-example)
- [Handling Spurious Wakeups](#handling-spurious-wakeups)
- [Comparison of Interthread Communication Methods](#comparison-of-interthread-communication-methods)
- [Key Points](#key-points)
- [Exam Tips](#exam-tips)
- [Real-World Applications](#real-world-applications)

## Introduction

Interthread communication is a crucial aspect of multithreaded programming in Java. It allows threads to cooperate and share data safely. Java provides `wait()`, `notify()`, and `notifyAll()` methods (from the Object class) for this purpose. These methods must be called from within a **synchronized context** to avoid race conditions.

## The Need for Interthread Communication

In multithreaded programming, threads often need to communicate with each other to achieve a common goal. For example, in a producer-consumer scenario, the producer thread produces data, and the consumer thread consumes it. Without proper communication, the consumer thread may try to consume data before it is produced, leading to errors.

## Methods for Interthread Communication

Java provides the following methods for interthread communication:

### wait()

The current thread releases the lock and waits until notified.

### notify()

Wakes up one waiting thread.

### notifyAll()

Wakes up all waiting threads.

These methods must be called from within a **synchronized block or method** to avoid `IllegalMonitorStateException`.

## Synchronized Context Requirement

To use `wait()`, `notify()`, and `notifyAll()` methods, a thread must own the object's lock. This can be achieved by calling these methods from within a **synchronized block or method**.

## Producer-Consumer Example

The producer-consumer problem is a classic use case for interthread communication. Here's an example implementation:

```java
class SharedBuffer {
 private int data;
 private boolean hasData = false;

 synchronized void produce(int value) {
 while (hasData) {
 try {
 wait();
 } catch (InterruptedException e) {
 Thread.currentThread().interrupt();
 }
 }
 data = value;
 hasData = true;
 System.out.println("Produced: " + value);
 notify();
 }

 synchronized int consume() {
 while (!hasData) {
 try {
 wait();
 } catch (InterruptedException e) {
 Thread.currentThread().interrupt();
 }
 }
 hasData = false;
 System.out.println("Consumed: " + data);
 notify();
 return data;
 }
}
```

## Handling Spurious Wakeups

A spurious wakeup occurs when a thread is awakened without a corresponding `notify()` call. To handle spurious wakeups, always use `wait()` in a while loop:

```java
while (condition) {
 try {
 wait();
 } catch (InterruptedException e) {
 Thread.currentThread().interrupt();
 }
}
```

## Comparison of Interthread Communication Methods

| Method        | Description                                | Use Case                           |
| ------------- | ------------------------------------------ | ---------------------------------- |
| `wait()`      | Releases the lock and waits until notified | Waiting for a condition to be met  |
| `notify()`    | Wakes up one waiting thread                | Signaling a waiting thread         |
| `notifyAll()` | Wakes up all waiting threads               | Signaling multiple waiting threads |

## Key Points

- `wait()` releases the lock, while `notify()` only signals waiting threads.
- Always use `wait()` in a while loop to handle spurious wakeups.
- The thread that gets notified first depends on JVM scheduling — it's not predictable.
- These methods belong to the **Object class**, not the Thread class.

## Exam Tips

- Remember: `wait()` releases the lock, while `notify()` only signals waiting threads.
- Always use `wait()` in a while loop to handle spurious wakeups.
- Common question: "Why is `wait()` always used in a while loop?" — Answer: To handle spurious wakeups.

## Real-World Applications

Interthread communication is used in various real-world applications, such as:

- Message queues
- Thread pools
- Event systems

By following these guidelines and best practices, you can effectively use interthread communication in your Java programs to achieve safe and efficient multithreading.
