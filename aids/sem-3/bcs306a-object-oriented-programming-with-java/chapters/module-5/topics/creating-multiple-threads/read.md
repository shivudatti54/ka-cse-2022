# Module 5: Creating Multiple Threads in Java

## Introduction

In the previous modules, you learned about the fundamentals of threads and how a single thread of execution works. However, the true power of multithreading is realized when multiple threads run concurrently within a single program. This allows for the design of highly responsive and efficient applications that can perform several tasks simultaneously, such as a web server handling multiple client requests or a GUI application running a background calculation without freezing the user interface. This section delves into the techniques for creating and managing multiple threads in Java.

## Core Concepts

There are two primary ways to create a thread in Java:
1. By extending the `Thread` class.
2. By implementing the `Runnable` interface.

While both are valid, **implementing `Runnable` is generally preferred** because it offers greater flexibility. Since Java doesn't support multiple inheritance, a class that extends `Thread` cannot extend any other class. However, a class can implement multiple interfaces, including `Runnable`, allowing it to inherit from another class if needed.

To create multiple threads, you simply create multiple instances of your thread class (whether it extends `Thread` or is passed to a `Thread` constructor via a `Runnable`).

### The `Runnable` Interface and `Thread` Class

The `Runnable` interface defines a single method: `public void run()`. This method contains the code that constitutes the new thread's task.

The `Thread` class is the core class that controls thread execution. You can create a thread by passing a `Runnable` object to its constructor. The `start()` method of the `Thread` class is crucial—it allocates resources for the thread at the OS level and schedules it to run, which eventually leads to the execution of the `run()` method. Calling `run()` directly does not create a new thread; it executes the method in the current thread, like any ordinary method call.

## Example: Creating Two Threads

Let's create two threads that count from 1 to 5. We'll demonstrate the preferred method using the `Runnable` interface.