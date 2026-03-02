# Thread Priorities in Java

## Overview

Thread priority in Java determines the relative scheduling priority of threads. Higher priority threads get more CPU time, but this is platform-dependent. The JVM schedules threads based on their priority, though the actual behavior varies across operating systems.

## Key Points

- **Thread priorities** range from 1 (MIN_PRIORITY) to 10 (MAX_PRIORITY)
- Default priority is 5 (NORM_PRIORITY)
- Set priority using **setPriority(int priority)** method
- Get priority using **getPriority()** method
- Higher priority doesn't guarantee execution order—it's a hint to the scheduler
- The **volatile** keyword ensures the running flag is read from main memory by all threads
- Use **start()** to begin thread execution, **sleep()** to pause, **join()** to wait for completion
- Daemon threads are low-priority background threads that don't prevent JVM from exiting

## Important Definitions

- **Thread Priority**: Integer value (1-10) indicating relative importance to the thread scheduler
- **volatile**: Keyword ensuring visibility of changes across threads immediately
- **Daemon Thread**: Low-priority background thread that doesn't prevent JVM from exiting

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

## Comparison Table

| Priority Level | Value | Usage              |
| -------------- | ----- | ------------------ |
| MIN_PRIORITY   | 1     | Lowest importance  |
| NORM_PRIORITY  | 5     | Default priority   |
| MAX_PRIORITY   | 10    | Highest importance |

## Exam Tips

- Remember the three constants: MIN=1, NORM=5, MAX=10
- Higher priority doesn't always mean faster execution—OS scheduler behavior varies
- **volatile** is crucial for shared variables accessed by multiple threads
- In the given example, high priority thread typically counts more than low priority
- exam questions often ask: "What is the range of thread priorities?" (Answer: 1-10)
- Understand the concept of daemon threads and their usage in Java.
