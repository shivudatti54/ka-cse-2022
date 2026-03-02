# Creating a Thread in Java

## Table of Contents

- [Creating a Thread in Java](#creating-a-thread-in-java)
- [Introduction](#introduction)
- [Why Use Threads?](#why-use-threads)
- [Creating a Thread](#creating-a-thread)
  - [1. Extending the `Thread` Class](#1-extending-the-thread-class)
  - [2. Implementing the `Runnable` Interface](#2-implementing-the-runnable-interface)
- [Starting a Thread](#starting-a-thread)
- [Thread States](#thread-states)
- [Example Use Case](#example-use-case)
- [Comparison of Thread Creation Methods](#comparison-of-thread-creation-methods)
- [Using isAlive() and join()](#using-isalive-and-join)
- [Thread Priorities](#thread-priorities)
- [Synchronization](#synchronization)
- [Interthread Communication](#interthread-communication)
- [Suspending, Resuming, and Stopping Threads](#suspending-resuming-and-stopping-threads)
- [Obtaining a Thread’s State](#obtaining-a-threads-state)
- [Enumerations](#enumerations)
- [Type Wrappers](#type-wrappers)
- [Autoboxing](#autoboxing)
- [Exam Tips](#exam-tips)
- [Key Takeaways](#key-takeaways)

=====================================================

## Introduction

---

In Java, threads are lightweight subprocesses that enable parallel execution of tasks within a single program. Creating a thread allows your program to perform multiple tasks simultaneously, improving responsiveness and throughput. In this topic, we will explore the basics of creating a thread in Java.

## Why Use Threads?

---

Threads are useful in various scenarios, such as:

- GUI development: Performing time-consuming tasks in the background while keeping the UI responsive.
- Server programming: Handling multiple client requests concurrently.
- Task parallelization: Dividing a large task into smaller subtasks that can be executed simultaneously.

## Creating a Thread

---

There are two primary methods for creating threads in Java:

### 1. Extending the `Thread` Class

To create a thread by extending the `Thread` class, follow these steps:

- Create a subclass of `Thread`.
- Override the `run()` method, which contains the code that executes concurrently when the thread is started.

```java
class MyThread extends Thread {
 @Override
 public void run() {
 for (int i = 0; i < 5; i++) {
 System.out.println("Thread is running: " + i);
 try {
 Thread.sleep(500); // Pauses the thread for 500ms
 } catch (InterruptedException e) {
 e.printStackTrace();
 }
 }
 }
}
```

### 2. Implementing the `Runnable` Interface

Alternatively, you can create a thread by implementing the `Runnable` interface:

- Create a class that implements `Runnable`.
- Implement the `run()` method, which contains the code that executes concurrently when the thread is started.

```java
class MyRunnable implements Runnable {
 @Override
 public void run() {
 for (int i = 0; i < 5; i++) {
 System.out.println("Runnable is running: " + i);
 try {
 Thread.sleep(500); // Pauses the thread for 500ms
 } catch (InterruptedException e) {
 e.printStackTrace();
 }
 }
 }
}
```

To start a thread using the `Runnable` interface, create an instance of `Thread` and pass the `Runnable` object to its constructor:

```java
Thread thread = new Thread(new MyRunnable());
thread.start();
```

## Starting a Thread

---

To start a thread, call the `start()` method on the thread object:

```java
MyThread thread = new MyThread();
thread.start();
```

**Important:** Always use `start()`, not `run()`. Calling `run()` directly executes the code in the current thread, whereas `start()` creates a new thread and invokes `run()`.

## Thread States

---

A thread goes through several states during its lifecycle:

- **New**: The thread is created but has not started yet.
- **Runnable**: The thread is ready to run but may be waiting for system resources.
- **Running**: The thread is executing its code.
- **Blocked**: The thread is waiting for a resource or is paused.
- **Terminated**: The thread has completed its execution.

## Example Use Case

---

Here's an example that demonstrates the concurrent execution of two threads:

```java
public class ThreadDemo {
 public static void main(String[] args) {
 // Create an instance of the thread subclass
 MyThread thread = new MyThread();
 // Start the thread (invokes the run() method)
 thread.start();
 // Code in the main thread continues concurrently
 for (int i = 0; i < 5; i++) {
 System.out.println("Main thread: " + i);
 }
 }
}
```

## Comparison of Thread Creation Methods

---

| Method                  | Description                                                     | Advantages                                    | Disadvantages       |
| ----------------------- | --------------------------------------------------------------- | --------------------------------------------- | ------------------- |
| Extending `Thread`      | Create a subclass of `Thread` and override `run()`              | Simple to implement                           | Limited flexibility |
| Implementing `Runnable` | Create a class that implements `Runnable` and implement `run()` | More flexible, can be used with other classes | Requires more code  |

## Using isAlive() and join()

---

The `isAlive()` method checks if a thread is alive, i.e., if it has started and has not yet terminated.

```java
MyThread thread = new MyThread();
thread.start();
System.out.println(thread.isAlive()); // prints: true
```

The `join()` method waits for a thread to terminate.

```java
MyThread thread = new MyThread();
thread.start();
thread.join(); // waits for thread to terminate
```

## Thread Priorities

---

Thread priorities determine the order in which threads are executed. Threads with higher priorities are executed before threads with lower priorities.

```java
MyThread thread = new MyThread();
thread.setPriority(Thread.MAX_PRIORITY); // sets thread priority to maximum
```

## Synchronization

---

Synchronization is used to ensure that only one thread can access a shared resource at a time.

```java
synchronized (this) {
 // code that accesses shared resource
}
```

## Interthread Communication

---

Interthread communication is used to communicate between threads.

```java
wait(); // causes current thread to wait
notify(); // wakes up waiting thread
```

## Suspending, Resuming, and Stopping Threads

---

Threads can be suspended, resumed, and stopped using the following methods:

```java
suspend(); // suspends thread
resume(); // resumes suspended thread
stop(); // stops thread
```

## Obtaining a Thread’s State

---

A thread's state can be obtained using the following methods:

```java
isAlive(); // checks if thread is alive
isInterrupted(); // checks if thread is interrupted
isDaemon(); // checks if thread is daemon
```

## Enumerations

---

Enumerations are used to define a fixed set of constants.

```java
enum Color {
 RED, GREEN, BLUE
}
```

## Type Wrappers

---

Type wrappers are used to wrap primitive types in objects.

```java
Integer i = new Integer(10);
```

## Autoboxing

---

Autoboxing is used to automatically convert between primitive types and their corresponding type wrappers.

```java
Integer i = 10; // autoboxing
int j = i; // unboxing
```

## Exam Tips

---

- Remember that calling `run()` directly does not create a new thread; always use `start()`.
- Know the difference between the `Thread` class and the `Runnable` interface.
- Be aware that `Thread.sleep()` is a static method that throws a checked `InterruptedException`.
- Understand the question pattern: "What happens if you call `thread.run()` instead of `thread.start()`?" (Answer: Runs in main thread, no concurrent execution)

## Key Takeaways

---

- Threads enable parallel execution of tasks within a single program.
- Create a thread by extending the `Thread` class or implementing the `Runnable` interface.
- Always use `start()`, not `run()`, to start a thread.
- Understand the different states of a thread's lifecycle.
- Use synchronization to ensure that only one thread can access a shared resource at a time.
- Use interthread communication to communicate between threads.
- Use thread priorities to determine the order in which threads are executed.
- Use enumerations to define a fixed set of constants.
- Use type wrappers to wrap primitive types in objects.
- Use autoboxing to automatically convert between primitive types and their corresponding type wrappers.
