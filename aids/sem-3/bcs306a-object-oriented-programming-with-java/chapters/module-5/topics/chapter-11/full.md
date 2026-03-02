# Chapter 11: Multithreaded Programming in Java

=====================================================

## Table of Contents

---

1. [Introduction](#introduction)
2. [History of Multithreading](#history-of-multithreading)
3. [The Java Thread Model](#the-java-thread-model)
   - [1.1 The Main Thread](#11-1-1-the-main-thread)
   - [1.2 Thread Creation](#11-1-2-thread-creation)
4. [Creating a Thread](#creating-a-thread)
   - [4.1 Extending the Thread Class](#411-extending-the-thread-class)
   - [4.2 Creating a Thread Object](#412-creating-a-thread-object)
5. [Thread States](#thread-states)
   - [5.1 New](#511-new)
   - [5.2 Runnable](#512-runnable)
   - [5.3 Running](#513-running)
   - [5.4 Dead](#514-dead)
6. [Thread Methods](#thread-methods)
   - [6.1 Start](#611-start)
   - [6.2 Run](#612-run)
   - [6.3 Interrupt](#613-interrupt)
   - [6.4 Join](#614-join)
7. [Thread Daemon Threads](#thread-daemon-threads)
8. [Thread Synchronization](#thread-synchronization)
   - [8.1 Synchronization Methods](#811-synchronization-methods)
   - [8.2 Locks](#812-locks)
9. [Case Study: A Simple Calculator Program](#case-study-a-simple-calculator-program)
10. [Conclusion](#conclusion)
11. [Further Reading](#further-reading)

## Introduction

---

Multithreading is a fundamental concept in Java that allows a program to execute multiple threads of execution concurrently. This enables a program to perform multiple tasks simultaneously, improving responsiveness, efficiency, and overall system performance. In this chapter, we will delve into the world of multithreading in Java, covering the basics, thread creation, synchronization, and synchronization methods.

## History of Multithreading

---

The concept of multithreading dates back to the 1960s, when the first multi-user operating system, Multics, was developed. However, it wasn't until the advent of the Internet and the need for high-performance servers that multithreading became a crucial aspect of computer science.

The Java platform was first released in 1995, and it inherited the concept of multithreading from its predecessor, C++. The Java Thread class was introduced in the 1.0 release, and since then, Java has become one of the most popular programming languages for multithreading.

## The Java Thread Model

---

### 1.1 The Main Thread

The main thread is the default thread created when a Java application starts. It is responsible for executing the main method of the program.

```java
public class Main {
    public static void main(String[] args) {
        // Code to be executed
    }
}
```

### 1.2 Thread Creation

A thread can be created using the `Thread` class in Java. There are two ways to create a thread:

- **Extending the Thread Class**: A thread can be created by extending the `Thread` class and overriding the `run()` method.

```java
public class MyThread extends Thread {
    public void run() {
        // Code to be executed
    }
}
```

- **Creating a Thread Object**: A thread can be created by creating an object of the `Thread` class and setting the `run()` method.

```java
public class Main {
    public static void main(String[] args) {
        Thread thread = new Thread(new Runnable() {
            public void run() {
                // Code to be executed
            }
        });
        thread.start();
    }
}
```

## Creating a Thread

---

### 4.1 Extending the Thread Class

When extending the `Thread` class, the `Thread` class's constructor is called automatically, and the `run()` method is set as the thread's target method.

```java
public class MyThread extends Thread {
    public void run() {
        System.out.println("Thread is running");
    }
}
```

### 4.2 Creating a Thread Object

When creating a thread object using the `Thread` class, the `run()` method must be set explicitly.

```java
public class Main {
    public static void main(String[] args) {
        Thread thread = new Thread(new Runnable() {
            public void run() {
                System.out.println("Thread is running");
            }
        });
        thread.start();
    }
}
```

## Thread States

---

### 5.1 New

A newly created thread is in the `NEW` state. It has been created but not yet started.

### 5.2 Runnable

A thread that is ready to run is in the `RUNNABLE` state. It has been started and is waiting for CPU time.

### 5.3 Running

A thread that is currently executing is in the `RUNNING` state. It has CPU time allocated and is executing the `run()` method.

### 5.4 Dead

A thread that has finished execution is in the `DEAD` state. It has released any CPU time and is no longer running.

## Thread Methods

---

### 6.1 Start

The `start()` method is used to start a thread. It does not guarantee that the thread will start immediately.

```java
public class MyThread extends Thread {
    public void run() {
        System.out.println("Thread is running");
    }

    public void start() {
        super.start();
    }
}
```

### 6.2 Run

The `run()` method is the target method of a thread. It is where the thread's execution begins.

```java
public class MyThread extends Thread {
    public void run() {
        System.out.println("Thread is running");
    }
}
```

### 6.3 Interrupt

The `interrupt()` method is used to interrupt a thread. It sets the thread's interrupt flag to true.

```java
public class Main {
    public static void main(String[] args) throws InterruptedException {
        Thread thread = new Thread(new Runnable() {
            public void run() {
                while (true) {
                    System.out.println("Thread is running");
                    try {
                        Thread.sleep(1000);
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
            }
        });
        thread.start();
        Thread.sleep(2000);
        thread.interrupt();
    }
}
```

### 6.4 Join

The `join()` method is used to wait for a thread to finish execution. It blocks the current thread until the specified thread finishes.

```java
public class Main {
    public static void main(String[] args) throws InterruptedException {
        Thread thread = new Thread(new Runnable() {
            public void run() {
                System.out.println("Thread is running");
                try {
                    Thread.sleep(2000);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
                System.out.println("Thread is finished");
            }
        });
        thread.start();
        thread.join();
        System.out.println("Main thread is finished");
    }
}
```

## Thread Daemon Threads

---

Thread daemon threads are background threads that run in the background. They do not stop the JVM when they finish execution.

```java
public class Main {
    public static void main(String[] args) {
        Thread thread = new Thread(new Runnable() {
            public void run() {
                while (true) {
                    System.out.println("Thread is running");
                }
            }
        });
        thread.setDaemon(true);
        thread.start();
    }
}
```

## Thread Synchronization

---

Thread synchronization is the process of ensuring that multiple threads access shared resources safely.

### 8.1 Synchronization Methods

There are two synchronization methods in Java:

- **Synchronized Methods**: A method can be declared as synchronized, which means that only one thread can execute the method at a time.

```java
public class Main {
    public static synchronized void main(String[] args) {
        // Code to be executed
    }
}
```

- **Synchronized Blocks**: A block of code can be declared as synchronized, which means that only one thread can execute the block at a time.

```java
public class Main {
    public static void main(String[] args) {
        synchronized (this) {
            // Code to be executed
        }
    }
}
```

### 8.2 Locks

A lock is used to synchronize access to shared resources. There are two types of locks in Java:

- **Reentrant Lock**: A reentrant lock is a lock that can be acquired multiple times by the same thread.

```java
import java.util.concurrent.locks.ReentrantLock;

public class Main {
    public static void main(String[] args) {
        ReentrantLock lock = new ReentrantLock();
        lock.lock();
        // Code to be executed
        lock.unlock();
    }
}
```

- **Read-Write Lock**: A read-write lock is a lock that allows multiple threads to read a shared resource simultaneously, but only one thread can write to the resource at a time.

```java
import java.util.concurrent.locks.ReentrantReadWriteLock;

public class Main {
    public static void main(String[] args) {
        ReentrantReadWriteLock lock = new ReentrantReadWriteLock();
        lock.readLock().lock();
        // Code to be executed
        lock.readLock().unlock();
    }
}
```

## Case Study: A Simple Calculator Program

---

A simple calculator program can be designed using multithreading to perform calculations concurrently.

```java
public class Calculator {
    public static void main(String[] args) {
        Thread thread1 = new Thread(new CalculatorTask("Addition"));
        Thread thread2 = new Thread(new CalculatorTask("Subtraction"));
        thread1.start();
        thread2.start();
    }
}

class CalculatorTask implements Runnable {
    private String task;

    public CalculatorTask(String task) {
        this.task = task;
    }

    public void run() {
        if (task.equals("Addition")) {
            System.out.println("Performing addition...");
            for (int i = 1; i <= 10; i++) {
                System.out.println("i: " + i);
                try {
                    Thread.sleep(100);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        } else if (task.equals("Subtraction")) {
            System.out.println("Performing subtraction...");
            for (int i = 1; i <= 10; i++) {
                System.out.println("i: " + i);
                try {
                    Thread.sleep(100);
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}
```

## Conclusion

---

Multithreading is a fundamental concept in Java that allows a program to execute multiple threads of execution concurrently. This enables a program to perform multiple tasks simultaneously, improving responsiveness, efficiency, and overall system performance.

In this chapter, we covered the basics of multithreading, including thread creation, thread states, synchronization, and synchronization methods. We also designed a simple calculator program using multithreading to perform calculations concurrently.

## Further Reading

---

- Java API Documentation: [https://docs.oracle.com/javase/8/docs/api/](https://docs.oracle.com/javase/8/docs/api/)
- Java Multithreading Tutorial: [https://docs.oracle.com/javase/tutorial/essential/concurrency/](https://docs.oracle.com/javase/tutorial/essential/concurrency/)
- Java Concurrency in Practice: [https://www.amazon.com/Java-Concurrency-Practice-William-Keith-Fowler/dp/0596009208](https://www.amazon.com/Java-Concurrency-Practice-William-Keith-Fowler/dp/0596009208)
