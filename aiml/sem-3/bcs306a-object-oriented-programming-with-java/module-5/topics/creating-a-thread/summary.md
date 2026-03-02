# Creating a Thread in Java

## Overview

In Java, a thread can be created by extending the **Thread class** and overriding its **run() method** or by implementing the **Runnable interface**. The run() method contains the code that executes concurrently when the thread is started. Threads enable parallel execution of tasks within a single process.

## Key Points

- **Extend Thread class**: Create a subclass of Thread to define custom thread behavior
- **Implement Runnable interface**: Create a class that implements Runnable for more flexibility
- **Override run()**: The entry point for thread execution; contains the code to run concurrently
- **Call start(), not run()**: Using start() creates a new thread and invokes run(); directly calling run() executes it in the current thread
- **Thread.sleep(ms)**: Pauses the thread for specified milliseconds; throws InterruptedException
- **Concurrent execution**: Main thread and custom thread run simultaneously
- **Thread states**: New → Runnable → Running → Blocked → Terminated
- **Thread priorities**: Determine the order in which threads are executed

## Important Definitions

- **Thread**: A lightweight subprocess that allows multiple operations to run concurrently within a single program
- **start()**: Method that initializes a new thread of execution and calls the run() method
- **run()**: Method that contains the code executed in the thread; override this to define thread behavior
- **Thread.sleep()**: Static method that causes the currently executing thread to pause for specified milliseconds
- **isAlive()**: Method that checks if a thread is alive
- **join()**: Method that waits for a thread to terminate

## Key Formulas / Syntax

```java
class MyThread extends Thread {
 @Override
 public void run() {
 for (int i = 0; i < 5; i++) {
 System.out.println("Thread: " + i);
 try {
 Thread.sleep(500);
 } catch (InterruptedException e) {}
 }
 }
}

class MyRunnable implements Runnable {
 @Override
 public void run() {
 for (int i = 0; i < 5; i++) {
 System.out.println("Runnable: " + i);
 try {
 Thread.sleep(500);
 } catch (InterruptedException e) {}
 }
 }
}

public class ThreadDemo {
 public static void main(String[] args) {
 MyThread t = new MyThread();
 t.start(); // Always use start(), not run()

 Thread r = new Thread(new MyRunnable());
 r.start();
 }
}
```

## Comparisons

| Feature              | Extending Thread | Implementing Runnable |
| -------------------- | ---------------- | --------------------- |
| Flexibility          | Limited          | More flexible         |
| Code Reusability     | No               | Yes                   |
| Multiple Inheritance | No               | Yes                   |

## Exam Tips

- **Common mistake**: Remember that calling **run() directly does not create a new thread**; always use **start()**
- ** focus**: Know the difference between Thread class and Runnable interface (also implement Runnable for flexibility)
- **Remember**: sleep() is static and throws checked InterruptedException
- **Question pattern**: "What happens if you call thread.run() instead of thread.start()?" — Answer: Runs in main thread, no concurrent execution
