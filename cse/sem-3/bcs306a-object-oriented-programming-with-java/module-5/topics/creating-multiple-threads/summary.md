# Creating Multiple Threads in Java

## Overview

Java supports multithreading to execute multiple tasks concurrently. Threads are lightweight subprocesses that share the same memory space, allowing efficient parallel execution. This topic covers creating threads using the **Runnable interface**, which is the preferred approach over extending the Thread class.

## Key Points

- **Runnable interface** should be implemented to define the task that a thread will execute
- The **run() method** contains the code that runs in the new thread - it does not start the thread itself
- **Thread class** wraps the Runnable object; creating a Thread object doesn't create a new execution thread
- The **start() method** creates a new thread and executes run() in that thread - never call run() directly
- **join() method** blocks the calling thread until the referenced thread completes execution
- Multiple threads run concurrently - output order may vary between executions
- **Thread.sleep()** pauses the current thread for specified milliseconds; throws InterruptedException
- **Thread Priorities** determine the order in which threads are executed
- **Synchronization** is the process of coordinating the execution of multiple threads to prevent data inconsistencies

## Important Definitions

- **Thread**: A lightweight subprocess that can execute concurrently with other threads
- **Runnable**: Interface with a single method run() that defines the task to be executed
- **Multithreading**: Executing multiple threads simultaneously to improve program efficiency
- **join()**: Method that waits for a thread to terminate before continuing execution
- **Thread Priority**: The priority of a thread that determines its execution order
- **Synchronization**: The process of coordinating the execution of multiple threads

## Key Formulas / Syntax

```java
// Step 1: Implement Runnable
class MyTask implements Runnable {
    @Override
    public void run() {
        // task code here
    }
}

// Step 2: Create Runnable and Thread objects
Runnable task = new MyTask();
Thread t = new Thread(task);

// Step 3: Start the thread
t.start();

// Step 4: Wait for completion
t.join();
```

## Comparisons

| Feature     | Runnable Interface                      | Extending Thread Class     |
| ----------- | --------------------------------------- | -------------------------- |
| Inheritance | Can extend another class                | Cannot extend other class  |
| Reusability | Task can be reused                      | Thread cannot be reused    |
| Memory      | Preferred - less memory                 | Less preferred             |
| Flexibility | Better separation of task and execution | Task and execution coupled |

## Exam Tips

- Remember: always call **start()**, never **run()** - calling run() executes in main thread, not a new thread
- The **join()** method is commonly asked in exams for synchronizing thread completion
- Be prepared to predict output - threads may execute in any order due to concurrency
- Runnable is preferred over Thread extension because Java supports single inheritance
- Don't forget to handle **InterruptedException** when using sleep() or join()
- Understand the importance of **Thread Priorities** and **Synchronization** in multithreaded programming.
