# **Multiple Threads, Using `isAlive()` and `join()`, Thread Priorities, Synchronization, Interthread Communication, Suspending, Resuming, and Stopping Thread**

## **Introduction**

In object-oriented programming with Java, threads are lightweight processes that can run concurrently with other threads or the main thread. Multiple threads can be used to improve the efficiency and responsiveness of a program. In this section, we will explore how to work with multiple threads, using `isAlive()` and `join()`, thread priorities, synchronization, interthread communication, suspending, resuming, and stopping threads.

## **Creating Multiple Threads**

Java provides two ways to create multiple threads:

- **Extending the `Thread` class**: By extending the `Thread` class and overriding the `run()` method, you can create a new thread.
- **Implementing the `Runnable` interface**: By implementing the `Runnable` interface and providing a `run()` method, you can create a new thread.

## **Using `isAlive()` and `join()`**

- **`isAlive()` method**: This method returns a boolean value indicating whether the thread is alive or not. A thread is alive if it has not been terminated.
- **`join()` method**: This method blocks the calling thread until the thread being joined terminates. This method is used to wait for a thread to finish its execution.

## **Thread Priorities**

Java threads have a priority level that determines the order in which they are executed. The priority level ranges from 1 (highest priority) to 10 (lowest priority). The main thread always has the highest priority.

| Priority Level | Thread Priority      |
| -------------- | -------------------- |
| 1              | Highest priority     |
| 2-5            | Medium-high priority |
| 6-9            | Medium-low priority  |
| 10             | Lowest priority      |

## **Synchronization**

Synchronization is a mechanism that allows multiple threads to access shared resources without conflicts. There are two types of synchronization:

- **Synchronization using locks**: This method involves acquiring a lock on a shared resource before accessing it.
- **Synchronization using atomic variables**: This method involves using atomic variables to ensure that shared resources are accessed in a thread-safe manner.

## **Interthread Communication**

Interthread communication is the exchange of data between threads. There are several ways to communicate between threads:

- **Using shared variables**: This method involves using shared variables to pass data between threads.
- **Using queues**: This method involves using queues to pass data between threads.
- **Using locks**: This method involves using locks to synchronize access to shared resources.

## **Suspending, Resuming, and Stopping Threads**

Java threads can be suspended, resumed, or stopped using the following methods:

- **`suspend()` method**: This method suspends the execution of a thread.
- **`resume()` method**: This method resumes the execution of a thread.
- **`stop()` method**: This method stops the execution of a thread.

## **Example Code**

```java
// Example 1: Creating multiple threads using `Thread` class
class MyThread extends Thread {
    @Override
    public void run() {
        System.out.println("Thread 1 is running");
        try {
            Thread.sleep(2000);
        } catch (InterruptedException e) {
            System.out.println("Thread 1 interrupted");
        }
        System.out.println("Thread 1 finished");
    }
}

class MyThread2 extends Thread {
    @Override
    public void run() {
        System.out.println("Thread 2 is running");
        try {
            Thread.sleep(3000);
        } catch (InterruptedException e) {
            System.out.println("Thread 2 interrupted");
        }
        System.out.println("Thread 2 finished");
    }
}

public class Main {
    public static void main(String[] args) {
        MyThread thread1 = new MyThread();
        MyThread2 thread2 = new MyThread2();

        thread1.start();
        thread2.start();
    }
}

// Example 2: Using `isAlive()` and `join()`
class MyThreadExtends extends Thread {
    @Override
    public void run() {
        System.out.println("Thread is running");
        try {
            Thread.sleep(2000);
        } catch (InterruptedException e) {
            System.out.println("Thread interrupted");
        }
        System.out.println("Thread finished");
    }
}

public class Main {
    public static void main(String[] args) {
        MyThreadExtends thread = new MyThreadExtends();

        System.out.println("Is thread alive? " + thread.isAlive());
        thread.join();
        System.out.println("Is thread alive? " + thread.isAlive());
    }
}

// Example 3: Thread priorities
class MyThreadHigh extends Thread {
    @Override
    public void run() {
        System.out.println("Thread with high priority is running");
        try {
            Thread.sleep(2000);
        } catch (InterruptedException e) {
            System.out.println("Thread interrupted");
        }
        System.out.println("Thread with high priority finished");
    }
}

class MyThreadLow extends Thread {
    @Override
    public void run() {
        System.out.println("Thread with low priority is running");
        try {
            Thread.sleep(3000);
        } catch (InterruptedException e) {
            System.out.println("Thread interrupted");
        }
        System.out.println("Thread with low priority finished");
    }
}

public class Main {
    public static void main(String[] args) {
        MyThreadHigh threadHigh = new MyThreadHigh();
        MyThreadLow threadLow = new MyThreadLow();

        threadHigh.setPriority(Thread.MAX_PRIORITY);
        threadLow.setPriority(Thread.MIN_PRIORITY);

        threadHigh.start();
        threadLow.start();
    }
}

// Example 4: Synchronization using locks
class MyThreadSynchronized extends Thread {
    private Object lock = new Object();

    @Override
    public void run() {
        synchronized (lock) {
            System.out.println("Thread is accessing shared resource");
            try {
                Thread.sleep(2000);
            } catch (InterruptedException e) {
                System.out.println("Thread interrupted");
            }
            System.out.println("Thread is finished accessing shared resource");
        }
    }
}

public class Main {
    public static void main(String[] args) {
        MyThreadSynchronized thread = new MyThreadSynchronized();

        thread.start();
    }
}
```

## **Key Concepts**

- **Multiple threads**: Lightweight processes that can run concurrently with other threads or the main thread.
- **`isAlive()` method**: Returns a boolean value indicating whether the thread is alive or not.
- **`join()` method**: Blocks the calling thread until the thread being joined terminates.
- **Thread priorities**: Priority levels that determine the order in which threads are executed.
- **Synchronization**: Mechanism that allows multiple threads to access shared resources without conflicts.
- **Interthread communication**: Exchange of data between threads.
- **Suspending, resuming, and stopping threads**: Methods that allow threads to be suspended, resumed, or stopped.

## **Practice Exercises**

1.  Create multiple threads using the `Thread` class and the `Runnable` interface.
2.  Use `isAlive()` and `join()` to wait for a thread to finish its execution.
3.  Modify the thread priorities using the `setPriority()` method.
4.  Use synchronization using locks to ensure thread-safe access to shared resources.
5.  Implement interthread communication using shared variables, queues, or locks.
6.  Suspend, resume, and stop threads using the `suspend()`, `resume()`, and `stop()` methods.
