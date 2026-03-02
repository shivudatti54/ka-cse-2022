# **Multiple Threads, Using isAlive() and join(), Thread Priorities, Synchronization, Interthread Communication, Suspending, Resuming, and Stopping Thread**

## **Key Points**

- **Multiple Threads**: Java allows multiple threads to execute concurrently.
- **Creating Threads**: Use `Thread` class or `Runnable` interface to create threads.
- **Main Thread**: The main thread is the thread that starts the program execution.
- **Thread Priorities**: Set thread priority using `Thread` constructor or `setPriority()` method.
  - `MIN_PRIORITY` (1)
  - `NORM_PRIORITY` (5)
  - `MAX_PRIORITY` (10)

- **Synchronization**: Use `synchronized` keyword to synchronize thread access to shared resources.
- **Interthread Communication**: Use `wait()`, `notify()`, and `notifyAll()` methods for communication between threads.
- **Suspending and Resuming**: Use `suspend()` and `resume()` methods to suspend or resume a thread.
- **Stopping a Thread**: Use `stop()` method to stop a thread.

## **Important Formulas and Definitions**

- **Thread State**:
  - `NEW`: New thread object created.
  - `RUNNABLE`: Thread is executing.
  - `BLOCKED`: Thread is blocked due to synchronization.
  - `WAITING`: Thread is waiting for another thread to notify it.
  - `TIMED_WAITING`: Thread is waiting for a specified time.
  - `TERMINATED`: Thread has finished execution.
- **Thread Life Cycle**:
  - Creation
  - Start
  - Run
  - Stop
  - Termination

## **Theorems**

- **Liveness Theorem**: A thread will eventually run if it is not blocked indefinitely.
- **Termination Theorem**: A program will eventually terminate if it is not blocked indefinitely.

## **Formulas**

- `Thread priority = Thread.MIN_PRIORITY + (int)(Thread.MAX_PRIORITY - Thread.MIN_PRIORITY) * (priority / (double)Thread.MAX_PRIORITY)`
- `Thread 영향을(int priority)`
- `Thread.getPriority()`
