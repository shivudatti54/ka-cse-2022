# Creating Multiple Threads in Java


## Table of Contents

- [Creating Multiple Threads in Java](#creating-multiple-threads-in-java)
- [Introduction](#introduction)
- [Why Multithreading?](#why-multithreading)
- [Key Components](#key-components)
  - [1. Runnable Interface](#1-runnable-interface)
  - [2. Thread Class](#2-thread-class)
  - [3. Thread Lifecycle](#3-thread-lifecycle)
  - [4. Thread Priorities](#4-thread-priorities)
  - [5. Synchronization](#5-synchronization)
- [Creating Multiple Threads](#creating-multiple-threads)
  - [Step 1: Implement Runnable](#step-1-implement-runnable)
  - [Step 2: Create Runnable and Thread Objects](#step-2-create-runnable-and-thread-objects)
  - [Step 3: Start the Threads](#step-3-start-the-threads)
  - [Step 4: Wait for Completion](#step-4-wait-for-completion)
- [Example Code](#example-code)
- [Comparison of Runnable Interface and Extending Thread Class](#comparison-of-runnable-interface-and-extending-thread-class)
- [Exam Tips](#exam-tips)
- [Key Takeaways](#key-takeaways)

=====================================================

## Introduction

---

Java supports multithreading to execute multiple tasks concurrently. Threads are lightweight subprocesses that share the same memory space, allowing efficient parallel execution. In this topic, we will cover creating threads using the **Runnable interface**, which is the preferred approach over extending the Thread class.

## Why Multithreading?

---

Multithreading is essential in modern software development because it allows programs to:

- Improve responsiveness by performing tasks concurrently
- Increase throughput by utilizing multiple CPU cores
- Enhance user experience by reducing wait times

## Key Components

---

To create multiple threads in Java, you need to understand the following key components:

### 1. Runnable Interface

The **Runnable interface** defines a single method `run()` that contains the code to be executed by the thread. By implementing Runnable, you can define a task that can be executed by a thread.

### 2. Thread Class

The **Thread class** wraps the Runnable object and provides methods to control the thread's execution. Creating a Thread object does not create a new execution thread; instead, it creates a new Thread object that can be started using the `start()` method.

### 3. Thread Lifecycle

A thread goes through the following stages:

1. **Creation**: A new Thread object is created using the Thread class.
2. **Start**: The `start()` method is called to create a new execution thread.
3. **Execution**: The `run()` method is executed by the new thread.
4. **Termination**: The thread completes its execution and terminates.

### 4. Thread Priorities

Thread priorities determine the order in which threads are executed. Threads with higher priorities are executed before threads with lower priorities.

### 5. Synchronization

Synchronization is the process of coordinating the execution of multiple threads to prevent data inconsistencies.

## Creating Multiple Threads

---

To create multiple threads, follow these steps:

### Step 1: Implement Runnable

Define a class that implements the Runnable interface:

```java
class MyTask implements Runnable {
 private String threadName;

 public MyTask(String name) {
 this.threadName = name;
 }

 @Override
 public void run() {
 // task code here
 }
}
```

### Step 2: Create Runnable and Thread Objects

Create Runnable objects and pass them to Thread objects:

```java
MyTask task1 = new MyTask("Thread-1");
MyTask task2 = new MyTask("Thread-2");
MyTask task3 = new MyTask("Thread-3");

Thread t1 = new Thread(task1);
Thread t2 = new Thread(task2);
Thread t3 = new Thread(task3);
```

### Step 3: Start the Threads

Call the `start()` method to create new execution threads:

```java
t1.start();
t2.start();
t3.start();
```

### Step 4: Wait for Completion

Use the `join()` method to wait for all threads to complete:

```java
try {
 t1.join();
 t2.join();
 t3.join();
} catch (InterruptedException e) {
 e.printStackTrace();
}
```

## Example Code

---

Here's an example code that demonstrates creating multiple threads:

```java
class MyTask implements Runnable {
 private String threadName;

 public MyTask(String name) {
 this.threadName = name;
 }

 @Override
 public void run() {
 for (int i = 0; i < 5; i++) {
 System.out.println(threadName + " is running, count: " + i);
 try {
 Thread.sleep(500); // Simulate some work with a delay
 } catch (InterruptedException e) {
 System.out.println(threadName + " was interrupted.");
 }
 }
 System.out.println(threadName + " exiting.");
 }
}

public class MultipleThreadsDemo {
 public static void main(String[] args) {
 System.out.println("Main thread started.");

 MyTask task1 = new MyTask("Thread-1");
 MyTask task2 = new MyTask("Thread-2");
 MyTask task3 = new MyTask("Thread-3");

 Thread t1 = new Thread(task1);
 Thread t2 = new Thread(task2);
 Thread t3 = new Thread(task3);

 t1.start();
 t2.start();
 t3.start();

 try {
 t1.join();
 t2.join();
 t3.join();
 } catch (InterruptedException e) {
 e.printStackTrace();
 }

 System.out.println("Main thread exiting.");
 }
}
```

## Comparison of Runnable Interface and Extending Thread Class

---

| Feature     | Runnable Interface                      | Extending Thread Class     |
| ----------- | --------------------------------------- | -------------------------- |
| Inheritance | Can extend another class                | Cannot extend other class  |
| Reusability | Task can be reused                      | Thread cannot be reused    |
| Memory      | Preferred - less memory                 | Less preferred             |
| Flexibility | Better separation of task and execution | Task and execution coupled |

## Exam Tips

---

- Always call `start()`, never `run()`. Calling `run()` executes in the main thread, not a new thread.
- The `join()` method is commonly asked in exams for synchronizing thread completion.
- Be prepared to predict output - threads may execute in any order due to concurrency.
- Runnable is preferred over Thread extension because Java supports single inheritance.
- Don't forget to handle `InterruptedException` when using `sleep()` or `join()`.

## Key Takeaways

---

- Multithreading is essential in modern software development for improving responsiveness and throughput.
- The Runnable interface defines a task that can be executed by a thread.
- The Thread class wraps the Runnable object and provides methods to control the thread's execution.
- Creating multiple threads involves implementing Runnable, creating Thread objects, starting the threads, and waiting for completion.
- The `join()` method is used to wait for all threads to complete.
- Runnable is preferred over Thread extension due to its flexibility and reusability.
