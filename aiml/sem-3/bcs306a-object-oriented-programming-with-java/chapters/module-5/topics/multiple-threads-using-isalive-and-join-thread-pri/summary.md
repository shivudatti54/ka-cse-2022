# Multiple Threads

### Introduction

- Multiple threads are the core concept of multithreaded programming in Java.
- A Java program can have multiple threads of execution, improving responsiveness and system utilization.

### Creating Threads

- **Thread Class**: Extends the `Runnable` interface or implements the `Runnable` interface.
- **Runnable Interface**: Defines the `run()` method that contains the code to be executed by the thread.

### Using `isAlive()` and `join()`

- `isAlive()`: Returns `true` if the thread is alive, `false` otherwise.
- `join()`: Waits for the specified thread to die, or the time to wait to expire, whichever comes first.

### Thread Priorities

- **ThreadPriority**: Defines the priority of the thread.
- **Priority Levels**:
  - MIN_PRIORITY (1)
  - NORM_PRIORITY (5)
  - MAX_PRIORITY (10)

### Synchronization

- **Synchronized Methods**: Ensure that only one thread can execute a method at a time.
- **Synchronized Blocks**: Ensure that only one thread can access a block of code at a time.

### Interthread Communication

- **Variables**: Shared between threads using variables.
- **Locks**: Used to synchronize access to shared variables.
- **Semaphores**: Used to limit the number of threads that can access shared resources.

### Suspending, Resuming, and Stopping Thread

- **suspend() and resume()**: Pause and resume the execution of a thread.
- **stop()**: Immediately stops the execution of a thread.

## Key Formulas/Definitions/Theorems

- **Thread Priority Inversion**: If two threads have the same priority, the one that arrives first gets the CPU.
- **Starvation**: When a thread is consistently denied the CPU and is never able to run.

Hence, these formulas/definitions/theorems help in understanding the behavior of threads and how to design efficient multithreaded programs.
