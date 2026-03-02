# **Threading Issues Summary**

## **Definition and Concepts**

- Threading refers to the scheduling of threads in a multi-core CPU environment.
- A thread is a lightweight process that shares the same memory space as other threads in the same process.
- Threading issues arise due to the complexity of scheduling threads and managing shared resources.

## **Types of Threading Issues**

- **Starvation**: A thread is unable to access shared resources due to other threads holding onto them for an extended period.
- **Livelock**: Multiple threads are unable to make progress due to an infinite loop of context switches.
- **Deadlock**: Two or more threads are blocked indefinitely, each waiting for the other to release a resource.
- **Priority Inversion**: A low-priority thread is able to access shared resources due to a high-priority thread holding onto them.

## **Synchronization and Communication**

- **Synchronization primitives**:
  - Locks (e.g., mutex, semaphore)
  - Monitors
  - Condition variables
- **Communication primitives**:
  - Shared variables
  - Message passing
  - Remote procedure calls (RPCs)

## **Formulas and Theorems**

- **Friedman's Theorem**: A deadlock occurs if and only if there exists a cycle in the thread execution graph.
- **Banker's Theorem**: A starvation-free system can be achieved if the number of resources is increased or decreased by the same amount for all threads.

## **Important Algorithms and Techniques**

- **Round-Robin Scheduling**: A scheduling algorithm that assigns equal time slices to all threads.
- **Priority Scheduling**: A scheduling algorithm that assigns priority to threads based on their priority values.
- **Pipeline Scheduling**: A scheduling algorithm that schedules threads in a pipeline fashion to optimize performance.

## **Best Practices and Troubleshooting**

- **Avoid busy-waiting**: Use synchronization primitives to avoid busy-waiting and reduce thread context switching.
- **Use synchronization primitives**: Use locks, monitors, and condition variables to synchronize threads and ensure data consistency.
- **Monitor thread execution**: Use profiling tools to monitor thread execution and identify potential threading issues.
