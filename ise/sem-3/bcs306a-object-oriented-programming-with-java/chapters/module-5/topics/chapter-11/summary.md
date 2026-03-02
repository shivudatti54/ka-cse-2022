# **Chapter 11: Multithreaded Programming in Java**

### Key Concepts

- **Thread**: A separate flow of execution within a program.
- **Main Thread**: The primary thread that starts the program.
- **Thread Creation**: Using `Thread` class and `Runnable` interface to create threads.
- **Thread States**: New, Runnable, Running, Blocked, Waiting, Timed Waiting, Dead.
- **Thread Synchronization**: Using `synchronized` keyword and `Lock` objects to access shared resources.

### Important Formulas and Definitions

- **Thread ID**: Unique identifier for each thread.
- **Thread Priority**: Priority level assigned to a thread, ranging from 1 (lowest) to 10 (highest).
- **Thread Join**: Waiting for a thread to finish execution before continuing.
- **Thread Yield**: Giving up the current thread's execution time to other threads.

### Important Theorems and Principles

- **Multithreading**: The ability of a program to execute multiple threads concurrently.
- **Context Switching**: The process of switching between threads to allocate resources.
- **Deadlock**: A situation where two or more threads are blocked, waiting for each other to release resources.

### Key Methods and Classes

- **`Thread` class**: Allows creating threads using the `Thread` constructor.
- **`Runnable` interface**: Defines a thread's behavior using a single method `run()`.
- **`synchronized` keyword**: Synchronizes access to shared resources using a lock object.
- **`Lock` objects**: Implement a lock mechanism to control access to shared resources.

### Key Terms

- **Thread Pool**: A group of threads that can be reused to improve performance.
- **Thread Local Storage**: A mechanism to store data specific to each thread.
- **Daemon Thread**: A thread that runs in the background, without preventing the program from exiting.
