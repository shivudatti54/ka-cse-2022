# The Main Thread

## Overview

The main thread is the first thread that begins execution when a Java program starts. It is automatically created by the JVM and executes the main() method. Understanding the main thread is fundamental to Java multithreading as all other threads are spawned from it.

## Key Points

- **Thread.currentThread()** - static method returns reference to currently executing thread
- Every thread has a **unique thread ID** assigned by the JVM
- Default thread name is "main" with priority 5 (NORM_PRIORITY)
- Thread name can be changed using **setName()** method
- **Thread.sleep(long ms)** pauses the current thread for specified milliseconds
- Thread priorities range from 1 (MIN_PRIORITY) to 10 (MAX_PRIORITY)
- **InterruptedException** must be handled when using sleep()
- **getId()** method returns the unique identifier of the thread
- **isAlive()** method checks if the thread is alive

## Important Definitions

- **Main Thread**: First thread that starts execution; executes the main() method
- **Thread.currentThread()**: Static method returning reference to the thread currently in execution
- **Thread.sleep()**: Static method that suspends thread execution for a specified time
- **InterruptedException**: Checked exception thrown when sleeping thread is interrupted
- **Thread Priority**: An integer value that determines the order in which threads are executed

## Key Formulas / Syntax

```java
Thread mainThread = Thread.currentThread(); // Get reference to main thread
mainThread.getName(); // Returns: "main"
mainThread.setName("MyThread"); // Change thread name
mainThread.getPriority(); // Returns: 5 (default)
mainThread.getId(); // Returns unique long ID
Thread.sleep(2000); // Pause for 2000ms
```

## Comparisons

| Feature   | Main Thread                           | Child Thread                                                         |
| --------- | ------------------------------------- | -------------------------------------------------------------------- |
| Creation  | Automatically created by JVM          | Created by main thread or other threads                              |
| Execution | Executes main() method                | Executes concurrently with main thread                               |
| Priority  | Default priority is 5 (NORM_PRIORITY) | Can have any priority between 1 (MIN_PRIORITY) and 10 (MAX_PRIORITY) |

## Exam Tips

- Remember Thread.sleep() is static—it always affects the currently executing thread regardless of which Thread object reference calls it
- Default priority of main thread is 5 (Thread.NORM_PRIORITY)
- exams commonly ask about the difference between getName() and setName()
- Always handle InterruptedException when using sleep() - it's a checked exception
- Understand the concept of thread priorities and how they affect thread execution.
