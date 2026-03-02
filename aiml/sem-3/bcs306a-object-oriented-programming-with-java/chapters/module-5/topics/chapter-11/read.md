# **Chapter 11: Multithreaded Programming - The Java Thread Model**

### Introduction

---

Multithreaded programming is a programming paradigm that allows a program to execute multiple threads or flows of execution concurrently. This is particularly useful in modern computing where processors can execute multiple instructions in parallel, improving the overall performance and responsiveness of a program.

Java provides a rich thread model that allows developers to create and manage threads efficiently. In this chapter, we will explore the Java Thread Model, the main thread, creating threads, and other essential concepts.

### The Java Thread Model

---

The Java Thread Model is a fundamental concept in multithreaded programming. It provides a framework for creating, managing, and synchronizing threads.

- **Thread**: A thread is the basic execution unit of a program. A thread can execute a block of code in parallel with other threads.
- **Thread Group**: A thread group is a collection of threads that are related to each other.
- **Thread State**: A thread can be in one of the following states:
  - **New**: The thread is created but has not started execution yet.
  - **Runnable**: The thread is ready to execute and is waiting for the CPU to become available.
  - **Blocked**: The thread is waiting for some resource to become available.
  - **Waiting**: The thread is waiting for another thread to notify it.
  - **Timed Waiting**: The thread is waiting for a specified amount of time to pass before continuing execution.
  - **Terminated**: The thread has completed its execution.

### The Main Thread

---

The main thread is the primary thread of a Java application. It is created automatically by the Java Virtual Machine (JVM) when a Java program is executed.

- **Main Method**: The main method is the entry point of a Java application.
- **Main Thread**: The main thread executes the main method.

### Creating Threads

---

There are several ways to create threads in Java.

### 1. Extending the Thread Class

---

You can create a thread by extending the Thread class and overriding the `run()` method.

```java
public class MyThread extends Thread {
    public void run() {
        System.out.println("Hello from MyThread!");
    }
}
```

### 2. Implementing the Runnable Interface

---

You can create a thread by implementing the Runnable interface and providing an implementation for the `run()` method.

```java
public class MyRunnable implements Runnable {
    public void run() {
        System.out.println("Hello from MyRunnable!");
    }
}
```

### Creating a Thread

---

To create a thread, you need to create an instance of the Thread class and pass an instance of the Runnable interface or a subclass of the Thread class as a constructor argument.

```java
public class Main {
    public static void main(String[] args) {
        Thread myThread = new Thread(new MyRunnable());
        myThread.start();
    }
}
```

### Synchronizing Threads

---

Synchronizing threads is crucial to prevent data inconsistencies and ensure thread safety.

- **Synchronized Methods**: You can use the `synchronized` keyword to synchronize methods.
- **Synchronized Blocks**: You can use the `synchronized` keyword to synchronize blocks of code.

```java
public class MyThread extends Thread {
    private int count = 0;

    public void run() {
        synchronized (this) {
            while (count < 10) {
                System.out.println("Hello from MyThread!");
                count++;
                try {
                    Thread.sleep(1000);
                } catch (InterruptedException e) {
                    Thread.currentThread().interrupt();
                }
            }
        }
    }
}
```

### Thread Pooling

---

Thread pooling is a technique that allows you to reuse existing threads instead of creating new ones.

- **ExecutorService**: You can use the `ExecutorService` interface to create a thread pool.
- **RunnableTask**: You can use a `RunnableTask` to execute tasks in the thread pool.

```java
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class Main {
    public static void main(String[] args) {
        ExecutorService executor = Executors.newFixedThreadPool(5);
        for (int i = 0; i < 10; i++) {
            executor.submit(new RunnableTask(i));
        }
        executor.shutdown();
    }
}

class RunnableTask implements Runnable {
    private int id;

    public RunnableTask(int id) {
        this.id = id;
    }

    public void run() {
        System.out.println("Hello from RunnableTask " + id + "!");
    }
}
```
