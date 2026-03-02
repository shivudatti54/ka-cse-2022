# **Chapter 11: Multithreaded Programming in Java**

## **Introduction**

Multithreaded programming is a technique where a single program can execute multiple threads of execution concurrently. In Java, multithreaded programming is achieved using the Java Thread model, which provides a way to create and manage threads.

## **Java Thread Model**

The Java Thread model consists of the following components:

- **Thread**: A thread is a separate flow of execution in a program. It is a separate entity from the main program, and it can execute independently.
- **Main Thread**: The main thread is the thread that starts the program and executes the main method.
- **Java Virtual Machine (JVM)**: The JVM is responsible for creating and managing threads.

## **Creating a Thread in Java**

To create a thread in Java, you need to extend the `Thread` class or implement the `Runnable` interface. Here's an example of how to create a thread using the `Thread` class:

```java
public class MyThread extends Thread {
    public void run() {
        System.out.println("Hello from thread!");
    }
}
```

To create a thread using the `Runnable` interface, you need to create a separate class that implements the `Runnable` interface and override the `run()` method. Here's an example:

```java
public class MyRunnable implements Runnable {
    public void run() {
        System.out.println("Hello from runnable!");
    }
}
```

## **Creating a Thread Programmatically**

You can create a thread programmatically using the `Thread` constructor. Here's an example:

```java
public class Main {
    public static void main(String[] args) {
        Thread thread = new Thread(new MyRunnable());
        thread.start();
    }
}
```

## **Thread States**

Threads can be in one of the following states:

- **New**: A new thread is created.
- **Runnable**: A thread is waiting for the CPU to execute it.
- **Running**: A thread is currently executing.
- **Blocked**: A thread is waiting for a resource that is not available.
- **Waiting**: A thread is waiting for an event to occur.
- **Timed Waiting**: A thread is waiting for a specific amount of time to pass.
- **Dead**: A thread has finished executing and is no longer running.

## **Thread Methods**

Here are some common thread methods:

- `start()`: Starts the thread.
- `run()`: Executes the code in the thread.
- `join()`: Waits for the thread to finish executing.
- `interrupt()`: Interrupts the thread.
- `isAlive()`: Returns true if the thread is still alive.

## **Thread Methods Example**

Here's an example of using some of the thread methods:

```java
public class Main {
    public static void main(String[] args) throws InterruptedException {
        Thread thread = new Thread(new MyRunnable());
        thread.start();
        thread.join();
        System.out.println("Thread finished!");
    }
}
```

## **Synchronization**

Synchronization is a mechanism that allows multiple threads to access shared resources without conflicts. Here's how to synchronize using the `synchronized` keyword:

```java
public class Main {
    public static void main(String[] args) {
        Object obj = new Object();
        Thread thread1 = new Thread(() -> {
            synchronized (obj) {
                System.out.println("Thread 1 accessed the object!");
            }
        });
        Thread thread2 = new Thread(() -> {
            synchronized (obj) {
                System.out.println("Thread 2 accessed the object!");
            }
        });
        thread1.start();
        thread2.start();
    }
}
```

## **Thread Pool**

A thread pool is a group of threads that are reused to execute tasks. Here's how to create a thread pool using the `Executor` interface:

```java
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

public class Main {
    public static void main(String[] args) {
        ExecutorService executor = Executors.newFixedThreadPool(5);
        for (int i = 0; i < 10; i++) {
            executor.execute(() -> System.out.println("Hello from thread!");
        }
    }
}
```

## **Conclusion**

In this chapter, we learned about multithreaded programming in Java, including the Java Thread model, creating threads, and thread states. We also learned about synchronization and thread pools. With this knowledge, you can write multithreaded programs that can execute multiple threads of execution concurrently.
