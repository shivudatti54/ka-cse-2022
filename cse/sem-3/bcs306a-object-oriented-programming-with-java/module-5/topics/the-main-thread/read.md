# The Main Thread

## Table of Contents

- [The Main Thread](#the-main-thread)
- [Introduction](#introduction)
- [The Main Thread Lifecycle](#the-main-thread-lifecycle)
  - [Creation](#creation)
  - [Execution](#execution)
  - [Termination](#termination)
- [Controlling the Main Thread](#controlling-the-main-thread)
  - [Setting Priority](#setting-priority)
  - [Setting Name](#setting-name)
- [Using Thread Class Methods](#using-thread-class-methods)
  - [currentThread()](#currentthread)
  - [getName()](#getname)
  - [getPriority()](#getpriority)
  - [sleep()](#sleep)
  - [getId()](#getid)
- [Comparison with Other Threads](#comparison-with-other-threads)
- [Creating and Starting Additional Threads](#creating-and-starting-additional-threads)
- [Exam Tips](#exam-tips)
- [Key Takeaways](#key-takeaways)

=====================================

## Introduction

---

In Java, the main thread is the first thread that begins execution when a Java program starts. It is automatically created by the JVM and executes the `main()` method. Understanding the main thread is fundamental to Java multithreading as all other threads are spawned from it. In this topic, we will explore the main thread, its lifecycle, and how to control it.

## The Main Thread Lifecycle

---

The main thread is created by the JVM when a Java program starts. It executes the `main()` method, which is the entry point of the program. The main thread continues to execute until the `main()` method completes or an exception is thrown.

### Creation

The main thread is created automatically by the JVM when a Java program starts. It is not necessary to explicitly create the main thread.

### Execution

The main thread executes the `main()` method, which is the entry point of the program.

### Termination

The main thread terminates when the `main()` method completes or an exception is thrown.

## Controlling the Main Thread

---

The main thread can be controlled using various methods, including setting its priority and name.

### Setting Priority

The priority of the main thread can be set using the `setPriority()` method. The priority of a thread determines the order in which it is executed by the JVM. Threads with higher priority are executed before threads with lower priority.

```java
public class MainThreadDemo {
 public static void main(String[] args) {
 // Get a reference to the currently executing thread (the main thread)
 Thread mainThread = Thread.currentThread();
 // Set the priority of the main thread
 mainThread.setPriority(Thread.MAX_PRIORITY);
 System.out.println("Priority: " + mainThread.getPriority());
 }
}
```

### Setting Name

The name of the main thread can be set using the `setName()` method. The name of a thread is used to identify it in the JVM.

```java
public class MainThreadDemo {
 public static void main(String[] args) {
 // Get a reference to the currently executing thread (the main thread)
 Thread mainThread = Thread.currentThread();
 // Set the name of the main thread
 mainThread.setName("MyMainThread");
 System.out.println("Thread name: " + mainThread.getName());
 }
}
```

## Using Thread Class Methods

---

The `Thread` class provides various methods that can be used to manipulate the main thread.

### currentThread()

The `currentThread()` method returns a reference to the currently executing thread.

```java
public class MainThreadDemo {
 public static void main(String[] args) {
 // Get a reference to the currently executing thread (the main thread)
 Thread mainThread = Thread.currentThread();
 System.out.println("Current Thread: " + mainThread.getName());
 }
}
```

### getName()

The `getName()` method returns the name of the thread.

```java
public class MainThreadDemo {
 public static void main(String[] args) {
 // Get a reference to the currently executing thread (the main thread)
 Thread mainThread = Thread.currentThread();
 System.out.println("Thread name: " + mainThread.getName());
 }
}
```

### getPriority()

The `getPriority()` method returns the priority of the thread.

```java
public class MainThreadDemo {
 public static void main(String[] args) {
 // Get a reference to the currently executing thread (the main thread)
 Thread mainThread = Thread.currentThread();
 System.out.println("Priority: " + mainThread.getPriority());
 }
}
```

### sleep()

The `sleep()` method pauses the execution of the thread for a specified period of time.

```java
public class MainThreadDemo {
 public static void main(String[] args) {
 try {
 // Let the thread sleep for 2 seconds
 Thread.sleep(2000);
 System.out.println("Slept for 2 seconds");
 } catch (InterruptedException e) {
 System.out.println("Main thread interrupted");
 }
 }
}
```

### getId()

The `getId()` method returns the unique identifier of the thread.

```java
public class MainThreadDemo {
 public static void main(String[] args) {
 // Get a reference to the currently executing thread (the main thread)
 Thread mainThread = Thread.currentThread();
 System.out.println("Thread ID: " + mainThread.getId());
 }
}
```

## Comparison with Other Threads

---

The main thread is unique in that it is the first thread to execute when a Java program starts. It is also the thread that executes the `main()` method.

| Thread       | Description                                                                              |
| ------------ | ---------------------------------------------------------------------------------------- |
| Main Thread  | First thread to execute when a Java program starts. Executes the `main()` method.        |
| Child Thread | Created by the main thread or other threads. Executes concurrently with the main thread. |

## Creating and Starting Additional Threads

---

The main thread can create and start additional threads using the `Thread` class or the `Runnable` interface.

```java
public class MainThreadDemo {
 public static void main(String[] args) {
 // Create a new thread
 Thread childThread = new Thread(new Runnable() {
 public void run() {
 System.out.println("Child thread running");
 }
 });
 // Start the child thread
 childThread.start();
 }
}
```

## Exam Tips

---

- Remember that `Thread.sleep()` is a static method that always affects the currently executing thread, regardless of which `Thread` object reference calls it.
- The default priority of the main thread is 5 (`Thread.NORM_PRIORITY`).
- exams commonly ask about the difference between `getName()` and `setName()`.
- Always handle `InterruptedException` when using `sleep()`, as it is a checked exception.
- The main thread is the first thread to execute when a Java program starts, and it executes the `main()` method.

## Key Takeaways

---

- The main thread is the first thread to execute when a Java program starts.
- The main thread executes the `main()` method.
- The main thread can be controlled using various methods, including setting its priority and name.
- The `Thread` class provides various methods that can be used to manipulate the main thread.
- The main thread is unique in that it is the first thread to execute when a Java program starts, and it executes the `main()` method.
