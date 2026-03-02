# The Java Thread Model

## Overview

Java's thread model enables multithreaded programming, allowing concurrent execution of multiple threads within a single program for better CPU utilization and responsive applications.

## Key Points

- **Thread States**: New → Runnable → Blocked/Waiting/Timed Waiting → Terminated
- **Two ways to create threads**: Extend Thread class or implement Runnable interface
- **Thread Priority**: Range from 1 (MIN_PRIORITY) to 10 (MAX_PRIORITY), default is 5 (NORM_PRIORITY)
- **Thread Synchronization**: Use `synchronized` keyword to prevent race conditions on shared resources
- **Main Thread**: Every Java application starts execution from the main thread running `main()` method
- **Thread Lifecycle**: Use `start()` to begin execution, not `run()` directly
- **Interthread Communication**: Use `wait()`, `notify()`, and `notifyAll()` methods
- **Thread State Methods**: Use `isAlive()`, `isInterrupted()`, and `isDaemon()` methods

## Important Definitions

- **Thread**: Lightweight subprocess that allows concurrent execution within a program
- **Race Condition**: Occurs when multiple threads access shared data concurrently causing unpredictable results
- **Synchronization**: Mechanism to control access to shared resources ensuring only one thread accesses at a time
- **Monitor Lock**: Intrinsic lock acquired when entering a synchronized block or method
- **Daemon Thread**: A thread that runs in the background and is not waited for on exit

## Key Formulas / Syntax

```java
// Method 1: Extend Thread class
class MyThread extends Thread {
    public void run() { /* task */ }
}
new MyThread().start();

// Method 2: Implement Runnable
class MyRunnable implements Runnable {
    public void run() { /* task */ }
}
new Thread(new MyRunnable()).start();

// Priority setting
thread.setPriority(Thread.MAX_PRIORITY); // 10

// Synchronized method
public synchronized void method() { /* code */ }

// Interthread communication
public synchronized void waitUntilReady() {
    while (!ready) {
        try {
            wait();
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }
}
```

## Comparisons

| Feature              | Extend Thread | Implement Runnable     |
| -------------------- | ------------- | ---------------------- |
| Multiple inheritance | Not allowed   | Allowed                |
| Resource sharing     | Difficult     | Easy via shared object |
| Flexibility          | Less          | More                   |
| Preferred approach   | Rarely        | Yes                    |

## Exam Tips

- Remember all 6 thread states in order for state diagram questions
- Always use `start()` to begin a thread, not `run()` (common mistake)
- Synchronized methods use object-level lock; static synchronized uses class-level lock
- `Runnable` is preferred over extending `Thread` as Java doesn't support multiple inheritance
- frequently asks: output of multi-threaded programs and identifying synchronization issues
- Be prepared to answer questions on thread state methods and interthread communication
