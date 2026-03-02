# The Java Thread Model

## Table of Contents

- [The Java Thread Model](#the-java-thread-model)
- [Introduction](#introduction)
- [Thread States](#thread-states)
- [Creating Threads](#creating-threads)
  - [Method 1: Extending Thread Class](#method-1-extending-thread-class)
  - [Method 2: Implementing Runnable Interface](#method-2-implementing-runnable-interface)
- [Thread Priority](#thread-priority)
- [Thread Synchronization](#thread-synchronization)
- [Main Thread](#main-thread)
- [Benefits of Multithreading](#benefits-of-multithreading)
  - [Example: Multithreaded Program](#example-multithreaded-program)
- [Comparison of Thread Creation Methods](#comparison-of-thread-creation-methods)
- [Interthread Communication](#interthread-communication)
- [Suspending, Resuming, and Stopping Threads](#suspending-resuming-and-stopping-threads)
- [Obtaining a Thread's State](#obtaining-a-threads-state)
- [Enumerations](#enumerations)
- [Type Wrappers](#type-wrappers)
- [Autoboxing](#autoboxing)
- [Exam Tips](#exam-tips)
- [Key Takeaways](#key-takeaways)

## Introduction

Java's thread model provides built-in support for multithreaded programming, allowing multiple threads to execute concurrently within a single program. This enables better CPU utilization, responsive applications, and simplified program structure. In this topic, we will explore the different states of a Java thread, how to create threads, thread priority, synchronization, and the benefits of multithreading.

## Thread States

A Java thread can be in one of the following six states:

1. **New:** Thread is created but not yet started.
2. **Runnable:** Thread is ready to run or currently running.
3. **Blocked:** Thread is waiting for a monitor lock.
4. **Waiting:** Thread is waiting indefinitely for another thread.
5. **Timed Waiting:** Thread is waiting for a specified time.
6. **Terminated:** Thread has completed execution.

## Creating Threads

There are two primary methods for creating threads in Java:

### Method 1: Extending Thread Class

```java
class MyThread extends Thread {
 @Override
 public void run() {
 System.out.println("Thread is running");
 }
}

public class Main {
 public static void main(String[] args) {
 MyThread thread = new MyThread();
 thread.start(); // Start the thread
 }
}
```

### Method 2: Implementing Runnable Interface

```java
class MyRunnable implements Runnable {
 @Override
 public void run() {
 System.out.println("Runnable is running");
 }
}

public class Main {
 public static void main(String[] args) {
 Thread thread = new Thread(new MyRunnable());
 thread.start();
 }
}
```

## Thread Priority

Threads can have priorities from 1 (MIN_PRIORITY) to 10 (MAX_PRIORITY):

```java
thread.setPriority(Thread.MAX_PRIORITY); // Priority 10
thread.setPriority(Thread.NORM_PRIORITY); // Priority 5
thread.setPriority(Thread.MIN_PRIORITY); // Priority 1
```

## Thread Synchronization

To prevent race conditions, Java provides synchronization:

```java
class Counter {
 private int count = 0;

 public synchronized void increment() {
 count++;
 }

 public int getCount() {
 return count;
 }
}
```

## Main Thread

Every Java application has a main thread that executes the `main()` method:

```java
public static void main(String[] args) {
 Thread mainThread = Thread.currentThread();
 System.out.println("Main thread: " + mainThread.getName());
}
```

## Benefits of Multithreading

- Better CPU utilization
- Responsive user interfaces
- Simplified program structure
- Parallel execution of tasks

### Example: Multithreaded Program

```java
class PrintNumbers implements Runnable {
 @Override
 public void run() {
 for (int i = 1; i <= 10; i++) {
 System.out.println(i);
 }
 }
}

class PrintLetters implements Runnable {
 @Override
 public void run() {
 for (char c = 'A'; c <= 'J'; c++) {
 System.out.println(c);
 }
 }
}

public class Main {
 public static void main(String[] args) {
 Thread thread1 = new Thread(new PrintNumbers());
 Thread thread2 = new Thread(new PrintLetters());
 thread1.start();
 thread2.start();
 }
}
```

## Comparison of Thread Creation Methods

| Feature              | Extending Thread Class | Implementing Runnable Interface |
| -------------------- | ---------------------- | ------------------------------- |
| Multiple Inheritance | Not allowed            | Allowed                         |
| Resource Sharing     | Difficult              | Easy via shared object          |
| Flexibility          | Less                   | More                            |
| Preferred Approach   | Rarely                 | Yes                             |

## Interthread Communication

Java provides several methods for interthread communication, including:

- `wait()`: Causes the current thread to wait until it is notified or interrupted.
- `notify()`: Notifies a single thread that is waiting on the object's monitor.
- `notifyAll()`: Notifies all threads that are waiting on the object's monitor.

```java
class SharedObject {
 private boolean ready = false;

 public synchronized void waitUntilReady() {
 while (!ready) {
 try {
 wait();
 } catch (InterruptedException e) {
 Thread.currentThread().interrupt();
 }
 }
 }

 public synchronized void setReady() {
 ready = true;
 notifyAll();
 }
}
```

## Suspending, Resuming, and Stopping Threads

Java provides several methods for suspending, resuming, and stopping threads, including:

- `suspend()`: Suspends the execution of the thread.
- `resume()`: Resumes the execution of the thread.
- `stop()`: Stops the execution of the thread.

```java
class MyThread extends Thread {
 @Override
 public void run() {
 while (true) {
 // Do some work
 try {
 Thread.sleep(1000);
 } catch (InterruptedException e) {
 Thread.currentThread().interrupt();
 }
 }
 }
}

public class Main {
 public static void main(String[] args) {
 MyThread thread = new MyThread();
 thread.start();
 try {
 Thread.sleep(5000);
 } catch (InterruptedException e) {
 Thread.currentThread().interrupt();
 }
 thread.suspend();
 try {
 Thread.sleep(5000);
 } catch (InterruptedException e) {
 Thread.currentThread().interrupt();
 }
 thread.resume();
 }
}
```

## Obtaining a Thread's State

Java provides several methods for obtaining a thread's state, including:

- `isAlive()`: Returns whether the thread is alive.
- `isInterrupted()`: Returns whether the thread has been interrupted.
- `isDaemon()`: Returns whether the thread is a daemon thread.

```java
class MyThread extends Thread {
 @Override
 public void run() {
 while (true) {
 // Do some work
 try {
 Thread.sleep(1000);
 } catch (InterruptedException e) {
 Thread.currentThread().interrupt();
 }
 }
 }
}

public class Main {
 public static void main(String[] args) {
 MyThread thread = new MyThread();
 thread.start();
 System.out.println("Is alive: " + thread.isAlive());
 System.out.println("Is interrupted: " + thread.isInterrupted());
 System.out.println("Is daemon: " + thread.isDaemon());
 }
}
```

## Enumerations

Java provides enumerations, which are a way to define a fixed set of named constants.

```java
enum Color {
 RED, GREEN, BLUE
}

public class Main {
 public static void main(String[] args) {
 Color color = Color.RED;
 System.out.println(color);
 }
}
```

## Type Wrappers

Java provides type wrappers, which are classes that wrap primitive types.

```java
class MyInteger {
 private int value;

 public MyInteger(int value) {
 this.value = value;
 }

 public int getValue() {
 return value;
 }
}

public class Main {
 public static void main(String[] args) {
 MyInteger myInteger = new MyInteger(10);
 System.out.println(myInteger.getValue());
 }
}
```

## Autoboxing

Java provides autoboxing, which is the automatic conversion between primitive types and their corresponding type wrappers.

```java
public class Main {
 public static void main(String[] args) {
 int primitiveInt = 10;
 Integer objectInt = primitiveInt; // Autoboxing
 System.out.println(objectInt);
 }
}
```

## Exam Tips

- Remember all 6 thread states in order for state diagram questions.
- Always use `start()` to begin a thread, not `run()` (common mistake).
- Synchronized methods use object-level lock; static synchronized uses class-level lock.
- `Runnable` is preferred over extending `Thread` as Java doesn't support multiple inheritance.
- frequently asks: output of multi-threaded programs and identifying synchronization issues.

## Key Takeaways

- Java's thread model enables multithreaded programming for better CPU utilization and responsive applications.
- Threads can be created by extending the `Thread` class or implementing the `Runnable` interface.
- Thread priority can be set using the `setPriority()` method.
- Synchronization is necessary to prevent race conditions in multithreaded programs.
- The main thread executes the `main()` method in every Java application.
- Multithreading offers several benefits, including better CPU utilization, responsive user interfaces, and simplified program structure.
