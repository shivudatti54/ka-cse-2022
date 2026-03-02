# Chapter 11

## Object Oriented Programming with JAVA

### 11.1 Introduction to Multithreading

Multithreading is a fundamental concept in Java that enables a single thread of execution to handle multiple tasks concurrently. This allows for efficient use of system resources, improved responsiveness, and enhanced overall system performance.

### 11.2 Historical Context

The concept of multithreading dates back to the early days of computing, where operating systems implemented context switching to switch between different tasks. Java's multithreading capabilities were introduced in the Java 1.0 release in 1995, building upon the concept of the "Green Threads" developed by Richard Kurzmann in 1992.

### 11.3 The Java Thread Model

The Java Thread Model is based on the following principles:

- **Lightweight threads**: Java threads are lightweight, meaning they are much lighter in weight than native threads.
- **First-in-first-out (FIFO) scheduling**: Java uses a FIFO scheduling algorithm to allocate threads, ensuring that the thread that was created first is executed first.
- **No preemption**: Java does not support preemption, which means that a thread will not be interrupted or interrupted by another thread while it is executing.

### 11.4 The Main Thread

The main thread is the primary thread that is started when a Java application is launched. The main thread is responsible for bootstrapping the application and executing the `main` method.

### 11.5 Creating a Thread

In Java, a thread can be created using one of the following methods:

- **Extending the Thread class**: This method involves creating a new class that extends the `Thread` class and overriding the `run` method.
- **Implementing the Runnable interface**: This method involves creating a new class that implements the `Runnable` interface and provides an implementation for the `run` method.
- **Using the Thread constructor**: This method involves creating a new `Thread` object and passing a `Runnable` object to its constructor.

### 11.6 Thread Life Cycle

A thread has a life cycle that consists of the following phases:

- **Created**: A new thread is created and added to the thread pool.
- **Running**: The thread is executing and performing its assigned task.
- **Blocked**: The thread is waiting for some resource or event to occur.
- **Waiting**: The thread is waiting for some other thread to perform some action.
- **Sleeping**: The thread is intentionally suspended for a specified amount of time.
- **Dead**: The thread terminates and is removed from the thread pool.

### 11.7 Synchronization

Synchronization is a mechanism that allows multiple threads to access shared resources safely and efficiently. In Java, synchronization is achieved using the `synchronized` keyword.

### 11.8 Locks and Audits

Locks and audits are used to manage access to shared resources. In Java, locks and audits are achieved using the `Lock` interface and the `ReentrantLock` class.

### 11.9 Thread Pool

A thread pool is a group of worker threads that are used to execute tasks concurrently. In Java, thread pools are achieved using the `ExecutorService` interface and the `ThreadPoolExecutor` class.

### 11.10 Case Study: Multithreaded Banking System

A multithreaded banking system is a classic example of multithreading in action. In this system, multiple threads are used to perform different tasks concurrently, such as:

- **Customer transactions**: One thread is used to handle customer transactions, such as depositing and withdrawing funds.
- **Transaction processing**: Another thread is used to process transactions, such as updating account balances and sending notifications.
- **System monitoring**: A third thread is used to monitor the system for any errors or exceptions.

### 11.11 Applications of Multithreading

Multithreading has numerous applications in various fields, including:

- **Gaming**: Multithreading is used in games to improve performance and responsiveness.
- **Scientific simulations**: Multithreading is used in scientific simulations to speed up computation and improve accuracy.
- **Web servers**: Multithreading is used in web servers to handle multiple requests concurrently.

### 11.12 Further Reading

- "Java Threads" by Joseph Choontoo
- "Multiprocessing in Java" by J. Arne Birkeland
- "Java Concurrency in Practice" by Brian Goetz

### 11.13 Code Examples

#### 11.13.1 Creating a Thread

```java
// Creating a thread using the Thread class
public class MyThread extends Thread {
    @Override
    public void run() {
        System.out.println("Hello from thread!");
    }
}

public class Main {
    public static void main(String[] args) {
        MyThread thread = new MyThread();
        thread.start();
    }
}
```

#### 11.13.2 Creating a Thread using the Runnable interface

```java
// Creating a thread using the Runnable interface
public class MyRunnable implements Runnable {
    @Override
    public void run() {
        System.out.println("Hello from thread!");
    }
}

public class Main {
    public static void main(String[] args) {
        MyRunnable runnable = new MyRunnable();
        Thread thread = new Thread(runnable);
        thread.start();
    }
}
```

#### 11.13.3 Creating a Thread using the ExecutorService interface

```java
// Creating a thread using the ExecutorService interface
public class MyTask implements Runnable {
    @Override
    public void run() {
        System.out.println("Hello from thread!");
    }
}

public class Main {
    public static void main(String[] args) {
        ExecutorService executor = Executors.newSingleThreadExecutor();
        executor.submit(new MyTask());
    }
}
```

#### 11.13.4 Synchronization using the synchronized keyword

```java
// Synchronization using the synchronized keyword
public class Counter {
    private int count = 0;

    public synchronized void increment() {
        count++;
    }

    public synchronized int getCount() {
        return count;
    }
}

public class Main {
    public static void main(String[] args) {
        Counter counter = new Counter();
        Thread thread1 = new Thread(new Runnable() {
            @Override
            public void run() {
                for (int i = 0; i < 10000; i++) {
                    counter.increment();
                }
            }
        });

        Thread thread2 = new Thread(new Runnable() {
            @Override
            public void run() {
                for (int i = 0; i < 10000; i++) {
                    counter.increment();
                }
            }
        });

        thread1.start();
        thread2.start();

        try {
            thread1.join();
            thread2.join();
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }

        System.out.println(counter.getCount());
    }
}
```

#### 11.13.5 Locks using the ReentrantLock class

```java
// Locks using the ReentrantLock class
public class Counter {
    private int count = 0;
    private final ReentrantLock lock = new ReentrantLock();

    public void increment() {
        lock.lock();
        try {
            count++;
        } finally {
            lock.unlock();
        }
    }

    public int getCount() {
        lock.lock();
        try {
            return count;
        } finally {
            lock.unlock();
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Counter counter = new Counter();
        Thread thread1 = new Thread(new Runnable() {
            @Override
            public void run() {
                for (int i = 0; i < 10000; i++) {
                    counter.increment();
                }
            }
        });

        Thread thread2 = new Thread(new Runnable() {
            @Override
            public void run() {
                for (int i = 0; i < 10000; i++) {
                    counter.increment();
                }
            }
        });

        thread1.start();
        thread2.start();

        try {
            thread1.join();
            thread2.join();
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }

        System.out.println(counter.getCount());
    }
}
```

#### 11.13.6 Thread Pool using the ExecutorService interface

```java
// Thread Pool using the ExecutorService interface
public class MyTask implements Runnable {
    @Override
    public void run() {
        System.out.println("Hello from thread!");
    }
}

public class Main {
    public static void main(String[] args) {
        ExecutorService executor = Executors.newFixedThreadPool(5);
        for (int i = 0; i < 10; i++) {
            executor.submit(new MyTask());
        }

        executor.shutdown();

        try {
            executor.awaitTermination(1, TimeUnit.MINUTES);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }
}
```
