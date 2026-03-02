# Thread Priorities in Java

## Table of Contents

- [Thread Priorities in Java](#thread-priorities-in-java)
- [Overview](#overview)
- [Importance of Thread Priorities](#importance-of-thread-priorities)
- [Thread Priority Constants](#thread-priority-constants)
- [Setting Thread Priorities](#setting-thread-priorities)
- [Getting Thread Priorities](#getting-thread-priorities)
- [Impact of Thread Priorities on Scheduling](#impact-of-thread-priorities-on-scheduling)
- [Example: Thread Priorities in Action](#example-thread-priorities-in-action)
- [Comparison of Thread Priority Levels](#comparison-of-thread-priority-levels)
- [Daemon Threads](#daemon-threads)
- [Volatile Keyword](#volatile-keyword)
- [Key Formulas / Syntax](#key-formulas--syntax)
- [Exam Tips](#exam-tips)
- [Key Takeaways](#key-takeaways)

## Overview

Thread priority in Java determines the relative scheduling priority of threads. Higher priority threads get more CPU time, but this is platform-dependent. The JVM schedules threads based on their priority, though the actual behavior varies across operating systems.

## Importance of Thread Priorities

Thread priorities are essential in multithreaded programming as they allow developers to control the execution order of threads. By assigning higher priorities to critical threads, developers can ensure that these threads receive more CPU time, resulting in better performance and responsiveness.

## Thread Priority Constants

The `Thread` class provides three constants for setting thread priorities:

- `MIN_PRIORITY`: The minimum priority value, which is 1.
- `NORM_PRIORITY`: The default priority value, which is 5.
- `MAX_PRIORITY`: The maximum priority value, which is 10.

## Setting Thread Priorities

To set the priority of a thread, you can use the `setPriority(int priority)` method. This method takes an integer value between 1 and 10, representing the desired priority level.

```java
// Setting priorities
thread.setPriority(Thread.MIN_PRIORITY); // 1
thread.setPriority(Thread.NORM_PRIORITY); // 5
thread.setPriority(Thread.MAX_PRIORITY); // 10
```

## Getting Thread Priorities

To retrieve the current priority of a thread, you can use the `getPriority()` method.

```java
// Getting priority
int priority = thread.getPriority();
```

## Impact of Thread Priorities on Scheduling

The JVM interprets thread priority values and uses them to determine the execution order of threads. However, the actual behavior varies across operating systems. In general, higher priority threads receive more CPU time, but this is not guaranteed.

## Example: Thread Priorities in Action

The following example demonstrates the effect of thread priorities on the execution order of threads.

```java
class PriorityDemo extends Thread {
 private long counter = 0;
 private volatile boolean running = true; // Flag to control the loop

 public void run() {
 while (running) {
 counter++;
 }
 }

 public void stopCounting() {
 running = false;
 }

 public long getCounter() {
 return counter;
 }
}

public class ThreadPriorityExample {
 public static void main(String[] args) throws InterruptedException {
 PriorityDemo lowPriorityThread = new PriorityDemo();
 PriorityDemo highPriorityThread = new PriorityDemo();

 // Set Thread Priorities
 lowPriorityThread.setPriority(Thread.MIN_PRIORITY); // Priority 1
 highPriorityThread.setPriority(Thread.MAX_PRIORITY); // Priority 10

 // Start the threads
 lowPriorityThread.start();
 highPriorityThread.start();

 // Let them run for a short time
 Thread.sleep(100); // Main thread sleeps for 100ms

 // Stop the threads
 lowPriorityThread.stopCounting();
 highPriorityThread.stopCounting();

 // Wait for them to finish
 lowPriorityThread.join();
 highPriorityThread.join();

 // Print the results
 System.out.println("Low Priority Thread counted: " + lowPriorityThread.getCounter());
 System.out.println("High Priority Thread counted: " + highPriorityThread.getCounter());
 }
}
```

## Comparison of Thread Priority Levels

The following table summarizes the thread priority levels and their usage:

| Priority Level | Value | Usage              |
| -------------- | ----- | ------------------ |
| MIN_PRIORITY   | 1     | Lowest importance  |
| NORM_PRIORITY  | 5     | Default priority   |
| MAX_PRIORITY   | 10    | Highest importance |

## Daemon Threads

A daemon thread is a low-priority background thread that doesn't prevent the JVM from exiting. Daemon threads are used for tasks that don't require user interaction, such as monitoring or logging.

## Volatile Keyword

The `volatile` keyword ensures that changes to a variable are visible across threads immediately. This is crucial for shared variables accessed by multiple threads.

## Key Formulas / Syntax

```java
// Setting priorities
thread.setPriority(Thread.MIN_PRIORITY); // 1
thread.setPriority(Thread.NORM_PRIORITY); // 5
thread.setPriority(Thread.MAX_PRIORITY); // 10

// Thread control methods
thread.start(); // Begin execution
Thread.sleep(100); // Pause for 100ms
thread.join(); // Wait for thread to die
```

## Exam Tips

- Remember the three constants: MIN=1, NORM=5, MAX=10
- Higher priority doesn't always mean faster execution—OS scheduler behavior varies
- `volatile` is crucial for shared variables accessed by multiple threads
- In the given example, high priority thread typically counts more than low priority
- exam questions often ask: "What is the range of thread priorities?" (Answer: 1-10)

## Key Takeaways

- Thread priorities determine the relative scheduling priority of threads.
- Higher priority threads receive more CPU time, but this is platform-dependent.
- The `Thread` class provides three constants for setting thread priorities: `MIN_PRIORITY`, `NORM_PRIORITY`, and `MAX_PRIORITY`.
- The `setPriority(int priority)` method sets the priority of a thread, and the `getPriority()` method retrieves the current priority.
- Thread priorities impact the execution order of threads, but the actual behavior varies across operating systems.
