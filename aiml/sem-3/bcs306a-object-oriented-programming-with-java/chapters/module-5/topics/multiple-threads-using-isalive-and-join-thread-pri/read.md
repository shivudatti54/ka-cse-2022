# **Multiple Threads, Using isAlive() and join(), Thread Priorities, Synchronization, Interthread Communication, Suspending, Resuming, and Stopping Thread**

## **Introduction**

In Java, a thread is a separate flow of execution within a program. Threads are used to improve the performance and responsiveness of a program by allowing it to execute multiple tasks concurrently. In this topic, we will explore the concepts of multiple threads, using `isAlive()` and `join()`, thread priorities, synchronization, interthread communication, suspending, resuming, and stopping threads.

## **Multiple Threads**

A multiple thread program is a program that can execute multiple threads of execution concurrently. Each thread has its own program counter, stack, and local variables. Threads are independent, but they can communicate with each other using synchronization mechanisms.

## **Why Multiple Threads?**

Multiple threads are useful for:

- Improving performance: Multiple threads can execute tasks concurrently, improving the overall performance of a program.
- Improving responsiveness: Multiple threads can improve the responsiveness of a program by allowing it to execute tasks in the background while still responding to user input.
- Handling concurrent tasks: Multiple threads can handle concurrent tasks, such as network requests, database queries, and file I/O operations.

## **Creating Multiple Threads**

There are four ways to create multiple threads in Java:

- Using the `Thread` class: This is the most common way to create multiple threads.
- Using the `Runnable` interface: This is another way to create multiple threads.
- Using the `ExecutorService` interface: This is a more modern way to create multiple threads.
- Using the `Future` interface: This is a way to create multiple threads that can return a future result.

## **Using `isAlive()` and `join()`**

The `isAlive()` method returns `true` if the thread is alive and `false` otherwise. The `join()` method blocks the current thread until the specified thread terminates.

- Example:
  ```java
  public class MultipleThreads {
  public static void main(String[] args) {
  Thread thread = new Thread(new Runnable() {
  public void run() {
  System.out.println("Thread is running...");
  }
  });
  thread.start();
  while (thread.isAlive()) {
  System.out.println("Thread is still alive...");
  }
  }
  }

````

**Thread Priorities**
---------------------

Thread priorities are used to determine the order in which threads are executed. The main thread has the highest priority.

*   Example:
    ```java
public class ThreadPriorities {
    public static void main(String[] args) {
        Thread highPriorityThread = new Thread(new Runnable() {
            public void run() {
                System.out.println("High priority thread is running...");
            }
        });
        Thread lowPriorityThread = new Thread(new Runnable() {
            public void run() {
                System.out.println("Low priority thread is running...");
            }
        });
        highPriorityThread.setPriority(Thread.MAX_PRIORITY);
        lowPriorityThread.setPriority(Thread.MIN_PRIORITY);
        highPriorityThread.start();
        lowPriorityThread.start();
    }
}
````

## **Synchronization**

Synchronization is used to coordinate access to shared resources. Synchronization is necessary to prevent data corruption and to ensure that multiple threads access shared resources safely.

- Example:
  ```java
  public class Synchronization {
  public static void main(String[] args) {
  int count = 0;
  synchronized (Synchronization.class) {
  for (int i = 0; i < 10; i++) {
  count++;
  System.out.println("Count: " + count);
  }
  }
  }
  }

````

**Interthread Communication**
-----------------------------

Interthread communication is used to exchange data between threads. There are several ways to communicate between threads, including:

*   Using synchronization mechanisms
*   Using queues
*   Using semaphores
*   Using locks

*   Example:
    ```java
public class InterthreadCommunication {
    public static void main(String[] args) {
        int count = 0;
        Thread thread = new Thread(new Runnable() {
            public void run() {
                for (int i = 0; i < 10; i++) {
                    count++;
                    System.out.println("Count from thread: " + count);
                    try {
                        Thread.sleep(100);
                    } catch (InterruptedException e) {
                        Thread.currentThread().interrupt();
                    }
                }
            }
        });
        thread.start();
        for (int i = 0; i < 10; i++) {
            System.out.println("Count from main thread: " + count);
            try {
                Thread.sleep(100);
            } catch (InterruptedException e) {
                Thread.currentThread().interrupt();
            }
        }
    }
}
````

## **Suspending and Resuming Threads**

Threads can be suspended and resumed using the `suspend()` and `resume()` methods.

- Example:
  ```java
  public class SuspendingAndResumingThreads {
  public static void main(String[] args) {
  Thread thread = new Thread(new Runnable() {
  public void run() {
  while (true) {
  System.out.println("Thread is running...");
  try {
  Thread.sleep(1000);
  } catch (InterruptedException e) {
  Thread.currentThread().interrupt();
  }
  }
  }
  });
  thread.start();
  try {
  Thread.sleep(2000);
  } catch (InterruptedException e) {
  Thread.currentThread().interrupt();
  }
  thread.suspend();
  try {
  Thread.sleep(2000);
  } catch (InterruptedException e) {
  Thread.currentThread().interrupt();
  }
  thread.resume();
  }
  }

````

**Stopping Threads**
---------------------

Threads can be stopped using the `stop()` method. However, the `stop()` method is deprecated in Java 5 and later versions. Instead, use the `interrupt()` method to interrupt the thread.

*   Example:
    ```java
public class StoppingThreads {
    public static void main(String[] args) {
        Thread thread = new Thread(new Runnable() {
            public void run() {
                while (true) {
                    System.out.println("Thread is running...");
                    try {
                        Thread.sleep(1000);
                    } catch (InterruptedException e) {
                        Thread.currentThread().interrupt();
                    }
                }
            }
        });
        thread.start();
        try {
            Thread.sleep(2000);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
        thread.interrupt();
    }
}
````
