# **Multiple Threads, Using `isAlive()` and `join()`, Thread Priorities, Synchronization, Interthread Communication, Suspending, Resuming, and Stopping Thread**

### Key Concepts

- **Multiple Threads**:
  - Java provides support for multiple threads within a single program.
  - Threads share the same memory space and resources.
- **`isAlive()` Method**:
  - Returns `true` if the thread is alive (i.e., running) and `false` otherwise.
  - Used to check the status of a thread.
- **`join()` Method**:
  - Waits for the specified thread to die.
  - Used to wait for a thread to finish its execution.
- **Thread Priorities**:
  - Threads with higher priorities will be executed before threads with lower priorities.
  - Priorities are assigned using the `setPriority()` method.
- **Synchronization**:
  - Ensures that only one thread can access shared resources at a time.
  - Used to prevent concurrency-related issues.
  - Can be achieved using `synchronized` blocks, `Lock` objects, or `ReentrantLock`.
- **Interthread Communication**:
  - Used to exchange data between threads.
  - Can be achieved using `wait()`, `notify()`, and `notifyAll()` methods.
- **Suspending and Resuming Threads**:
  - Threads can be suspended using the `suspend()` method.
  - Threads can be resumed using the `resume()` method.
- **Stopping Threads**:
  - Threads can be stopped using the `stop()` method.
  - However, this method is deprecated and should not be used.

### Important Formulas and Definitions

- **Thread State**:
  - `NEW`: The thread is in the initial state.
  - `RUNNABLE`: The thread is running or waiting to run.
  - `WAITING`: The thread is waiting for some resource.
  - `TIMED_WAITING`: The thread is waiting for some resource and has a deadline.
- **Priority Inversion**:
  - A situation where a lower-priority thread is given higher priority than a higher-priority thread.

### Theorems

- **Fairness Theorem**:
  - States that if a thread is given a priority inversion, the priority of the higher-priority thread will increase, and the priority of the lower-priority thread will decrease.

### Quick Revision Guide

- To create multiple threads, use the `Thread` class or the `Runnable` interface.
- Use `isAlive()` to check the status of a thread.
- Use `join()` to wait for a thread to finish its execution.
- Use `setPriority()` to assign a priority to a thread.
- Use synchronization mechanisms to ensure thread safety.
- Use interthread communication mechanisms to exchange data between threads.
