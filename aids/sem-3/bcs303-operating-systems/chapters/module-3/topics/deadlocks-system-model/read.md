# **Deadlocks: System Model**

## **Introduction**

In an operating system, a deadlock is a situation where two or more processes are blocked indefinitely, each waiting for a resource held by another process. Deadlocks can occur in a system where there is a circular wait, where each process is waiting for a resource that is held by another process, which in turn is waiting for a resource held by the first process.

## **Definition**

A deadlock is a situation where:

- Each process is waiting for a resource held by another process.
- Each process is holding a resource that is required by another process.
- No process can proceed because each process is waiting for a resource held by another process.

## **Deadlock Detection**

To detect a deadlock, we need to identify the resources being held by each process and the order in which they are waiting for each resource.

### Deadlock Detection Algorithm

One common algorithm used to detect deadlocks is the Banker's Algorithm.

1.  **Resource Allocation Matrix**: Create a resource allocation matrix that shows which processes are holding which resources.
2.  **Available Resources Matrix**: Create an available resources matrix that shows which resources are available.
3.  **Finish Time Matrix**: Create a finish time matrix that shows when each process will finish using all its resources.
4.  **Need Matrix**: Create a need matrix that shows how much each process needs each resource.
5.  **Deadlock Detection**: Check if any process is holding all its resources and waiting for a resource held by another process.

## **Types of Deadlocks**

There are two types of deadlocks:

- **Multiprocess Deadlock**: A deadlock that occurs when multiple processes are involved.
- **Uniprocess Deadlock**: A deadlock that occurs when only one process is involved.

## **Deadlock Prevention**

To prevent deadlocks, we can use the following strategies:

- **Avoid Nested Locks**: Avoid acquiring multiple locks in a nested manner.
- **Avoid Circular Dependencies**: Avoid situations where a process needs a resource held by another process, which needs a resource held by the first process.
- **Use Resource Pooling**: Use resource pooling to ensure that resources are always available.
- **Use Priority Scheduling**: Use priority scheduling to ensure that high-priority processes are executed before low-priority processes.

## **Deadlock Recovery**

In case of a deadlock, we can recover by:

- **Killing the Deadlocked Process**: Kill the process that is holding the most resources.
- **Rolling Back Transactions**: Roll back transactions to a previous point.
- **Abort and Restart**: Abort the current process and restart it.

## **Example**

Suppose we have three processes, P1, P2, and P3, each requiring two resources, R1 and R2.

| Process | R1 Required | R2 Required |
| ------- | ----------- | ----------- |
| P1      | 2           | 1           |
| P2      | 1           | 2           |
| P3      | 2           | 1           |

If P1 acquires R1 and P2 acquires R2, a deadlock occurs.

## **Key Concepts**

- **Resource**: A resource is something that can be used by a process.
- **Lock**: A lock is a mechanism that allows a process to acquire a resource exclusively.
- **Deadlock**: A deadlock is a situation where two or more processes are blocked indefinitely, each waiting for a resource held by another process.
- **Resource Allocation Matrix**: A resource allocation matrix shows which processes are holding which resources.
- **Available Resources Matrix**: An available resources matrix shows which resources are available.
- **Finish Time Matrix**: A finish time matrix shows when each process will finish using all its resources.
- **Need Matrix**: A need matrix shows how much each process needs each resource.
- **Deadlock Detection Algorithm**: A deadlock detection algorithm is used to detect deadlocks.

## **Study Questions**

1.  What is a deadlock?
2.  How can we detect deadlocks?
3.  What are the two types of deadlocks?
4.  How can we prevent deadlocks?
5.  How can we recover from a deadlock?

## **Answers**

1.  A deadlock is a situation where two or more processes are blocked indefinitely, each waiting for a resource held by another process.
2.  We can detect deadlocks using a deadlock detection algorithm, such as the Banker's Algorithm.
3.  There are two types of deadlocks: multiprocess deadlock and uniprocess deadlock.
4.  We can prevent deadlocks by avoiding nested locks, avoiding circular dependencies, using resource pooling, and using priority scheduling.
5.  We can recover from a deadlock by killing the deadlocked process, rolling back transactions, or aborting and restarting the process.
