# Suspending, Resuming, and Stopping Threads in Java


## Table of Contents

- [Suspending, Resuming, and Stopping Threads in Java](#suspending-resuming-and-stopping-threads-in-java)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [The Thread Lifecycle and Control Methods](#the-thread-lifecycle-and-control-methods)
  - [Why These Methods Were Deprecated](#why-these-methods-were-deprecated)
  - [Modern Approaches to Thread Control](#modern-approaches-to-thread-control)
  - [Using Flag Variables](#using-flag-variables)
- [Examples](#examples)
  - [Example 1: Demonstrating Deprecated suspend() and resume()](#example-1-demonstrating-deprecated-suspend-and-resume)
  - [Example 2: Producer-Consumer using wait() and notify()](#example-2-producer-consumer-using-wait-and-notify)
  - [Example 3: Thread Control using interrupt()](#example-3-thread-control-using-interrupt)
- [Exam Tips](#exam-tips)

## Introduction

Thread synchronization and control are fundamental concepts in Java multithreading. In concurrent programming, managing the lifecycle of threads is crucial for building responsive and efficient applications. The ability to suspend, resume, and stop threads allows developers to control the execution flow of concurrent tasks, pause long-running operations, and gracefully terminate threads when they are no longer needed.

In Java, the Thread class originally provided three deprecated methods: suspend(), resume(), and stop() for controlling thread execution. However, these methods were deprecated due to serious design flaws that could lead to deadlocks and system instability. Despite their deprecation, understanding these methods is essential for examination purposes and for comprehending why modern alternatives were developed.

This topic explores the traditional approaches to thread control, their limitations, and the recommended modern techniques using wait(), notify(), notifyAll(), and interrupt() methods. Understanding these concepts is vital for CSE students as multithreading is a critical topic in Java programming and forms the basis for building concurrent applications.

## Key Concepts

### The Thread Lifecycle and Control Methods

Threads in Java transition through various states: New, Runnable, Blocked, Waiting, Timed Waiting, and Terminated. The ability to move threads between these states is fundamental to thread control.

The original Thread class provided the following control methods:

1. **suspend()**: This method was used to pause the execution of a thread. When called on a Thread object, it would move the thread from the Runnable state to the Suspended state. The thread would not execute until its resume() method was called.

2. **resume()**: This method was designed to resume the execution of a suspended thread. It would move the thread back to the Runnable state, allowing it to compete for CPU time again.

3. **stop()**: This method was used to forcibly terminate a thread. When called, it would throw a ThreadDeath exception, effectively stopping the thread's execution.

### Why These Methods Were Deprecated

The suspend(), resume(), and stop() methods were deprecated in JDK 1.2 due to several critical issues:

**Deadlock Problem**: The suspend() method acquires the monitor lock on the suspended thread but does not release it. If another thread attempts to access synchronized resources held by the suspended thread, a deadlock occurs because the suspended thread cannot release the lock.

**Resource Leakage**: When a thread is suspended while holding critical resources like database connections, file handles, or locks, those resources remain locked indefinitely, leading to resource leakage.

**Inconsistent State**: The stop() method abruptly terminates a thread without allowing it to complete cleanup operations or release resources properly. This can leave objects in an inconsistent state.

**ThreadDeath Exception**: The stop() method throws a ThreadDeath exception, which can be caught but often leads to unpredictable behavior if not handled properly.

### Modern Approaches to Thread Control

#### Using wait() and notify() Methods

The recommended approach for thread synchronization and control uses the wait(), notify(), and notifyAll() methods defined in the Object class. These methods work on the monitor lock of an object.

**wait()**: Causes the current thread to wait until another thread invokes the notify() or notifyAll() method on the same object. The thread releases the monitor lock and enters the Waiting state.

**notify()**: Wakes up a single thread that is waiting on this object's monitor. The choice of which thread to wake is arbitrary and depends on the JVM implementation.

**notifyAll()**: Wakes up all threads that are waiting on this object's monitor. The threads will compete for the monitor lock.

Example demonstrating wait() and notify():

```java
class Message {
 private String message;
 private boolean available = false;

 public synchronized String read() {
 while (!available) {
 try {
 wait(); // Release lock and wait
 } catch (InterruptedException e) {
 Thread.currentThread().interrupt();
 }
 }
 available = false;
 notifyAll();
 return message;
 }

 public synchronized void write(String msg) {
 while (available) {
 try {
 wait();
 } catch (InterruptedException e) {
 Thread.currentThread().interrupt();
 }
 }
 message = msg;
 available = true;
 notifyAll();
 }
}
```

#### Using interrupt() Method

The interrupt() method is the recommended way to stop or control thread execution. It does not forcibly terminate the thread but sets an interrupt flag that the thread can check and respond to appropriately.

**How interrupt() works**:

- Sets the interrupt status flag of the thread to true
- If the thread is blocked in wait(), sleep(), or join() method, it throws an InterruptedException and clears the interrupt flag

**Thread.interrupted()**: Static method that returns the interrupt status of the current thread and clears the flag.

**isInterrupted()**: Instance method that returns the interrupt status without clearing the flag.

Example demonstrating interrupt():

```java
class InterruptDemo extends Thread {
 public void run() {
 try {
 while (!Thread.currentThread().isInterrupted()) {
 // Perform task
 System.out.println("Thread running...");
 Thread.sleep(1000);
 }
 } catch (InterruptedException e) {
 // Thread was interrupted during sleep
 System.out.println("Thread interrupted during sleep");
 }
 System.out.println("Thread exiting gracefully");
 }

 public static void main(String[] args) throws InterruptedException {
 InterruptDemo thread = new InterruptDemo();
 thread.start();
 Thread.sleep(5000);
 thread.interrupt();
 }
}
```

### Using Flag Variables

Another modern approach is to use a boolean flag variable that the thread periodically checks. This provides a clean way to signal a thread to stop.

```java
class ControlledThread extends Thread {
 private volatile boolean running = true;

 public void run() {
 while (running) {
 // Perform task
 System.out.println("Working...");
 try {
 Thread.sleep(100);
 } catch (InterruptedException e) {
 break;
 }
 }
 System.out.println("Thread stopped");
 }

 public void stopThread() {
 running = false;
 }
}
```

The volatile keyword ensures that the flag value is immediately visible to all threads.

## Examples

### Example 1: Demonstrating Deprecated suspend() and resume()

Although deprecated, let's understand how they worked:

```java
class OldSuspendResume extends Thread {
 public void run() {
 for (int i = 1; i <= 5; i++) {
 System.out.println("Thread: " + i);
 try {
 Thread.sleep(1000);
 } catch (InterruptedException e) {
 e.printStackTrace();
 }
 }
 }

 public static void main(String[] args) {
 OldSuspendResume t = new OldSuspendResume();
 t.start();

 try {
 Thread.sleep(2000);
 t.suspend(); // Pause the thread (DEPRECATED)
 System.out.println("Thread suspended");
 Thread.sleep(2000);
 t.resume(); // Resume the thread (DEPRECATED)
 System.out.println("Thread resumed");
 } catch (InterruptedException e) {
 e.printStackTrace();
 }
 }
}
```

**Output**:

```
Thread: 1
Thread: 2
Thread suspended
Thread resumed
Thread: 3
Thread: 4
Thread: 5
```

### Example 2: Producer-Consumer using wait() and notify()

```java
class Q {
 int n;
 boolean valueSet = false;

 synchronized void put(int n) {
 while (valueSet) {
 try { wait(); } catch (InterruptedException e) {}
 }
 this.n = n;
 valueSet = true;
 System.out.println("Produced: " + n);
 notify();
 }

 synchronized int get() {
 while (!valueSet) {
 try { wait(); } catch (InterruptedException e) {}
 }
 System.out.println("Consumed: " + n);
 valueSet = false;
 notify();
 return n;
 }
}

class Producer implements Runnable {
 Q q;
 Producer(Q q) { this.q = q; }

 public void run() {
 int i = 0;
 while (i < 5) {
 q.put(i++);
 try { Thread.sleep(500); } catch (InterruptedException e) {}
 }
 }
}

class Consumer implements Runnable {
 Q q;
 Consumer(Q q) { this.q = q; }

 public void run() {
 while (true) {
 q.get();
 try { Thread.sleep(1000); } catch (InterruptedException e) {}
 }
 }
}

class PC {
 public static void main(String[] args) {
 Q q = new Q();
 new Thread(new Producer(q)).start();
 new Thread(new Consumer(q)).start();
 }
}
```

### Example 3: Thread Control using interrupt()

```java
class PrimeSearch extends Thread {
 public void run() {
 long num = 2;
 while (!Thread.currentThread().isInterrupted()) {
 if (isPrime(num)) {
 System.out.println("Prime found: " + num);
 }
 num++;
 // Check interrupt status
 if (Thread.currentThread().isInterrupted()) {
 System.out.println("Thread interrupted, exiting...");
 return;
 }
 }
 }

 boolean isPrime(long n) {
 if (n < 2) return false;
 for (long i = 2; i <= Math.sqrt(n); i++) {
 if (n % i == 0) return false;
 }
 return true;
 }

 public static void main(String[] args) throws InterruptedException {
 PrimeSearch thread = new PrimeSearch();
 System.out.println("Starting prime search...");
 thread.start();
 Thread.sleep(3000);
 thread.interrupt();
 thread.join();
 System.out.println("Main thread finished");
 }
}
```

## Exam Tips

1. **Remember the deprecated methods**: The suspend(), resume(), and stop() methods were deprecated in JDK 1.2 due to deadlock and resource leakage issues. This is a frequently asked question in university exams.

2. **Know why deprecation occurred**: Understand that suspend() causes deadlocks because it holds locks, stop() leaves objects in inconsistent states, and these methods are inherently unsafe.

3. **Modern alternatives**: Be familiar with wait(), notify(), notifyAll() for synchronization and interrupt() for thread termination. These are the recommended approaches.

4. **volatile keyword**: When using flag variables to stop threads, remember to declare the flag as volatile to ensure visibility across threads.

5. **interrupt() behavior**: Remember that interrupt() does not forcibly stop a thread; it sets an interrupt flag. The thread must check this flag and respond appropriately using isInterrupted() or by catching InterruptedException.

6. **Thread states**: Understand how threads transition between states when these methods are called. suspend() moves to Suspended, resume() returns to Runnable, and stop() moves to Terminated.

7. **Synchronization requirement**: wait(), notify(), and notifyAll() must be called from within a synchronized context (synchronized method or block).

8. **Difference between isInterrupted() and Thread.interrupted()**: isInterrupted() returns the interrupt status without clearing it, while Thread.interrupted() is a static method that returns and clears the interrupt status.
