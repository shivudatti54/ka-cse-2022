# **Threading Issues**

## **Table of Contents**

1. [Introduction](#introduction)
2. [Types of Threading Issues](#types-of-threading-issues)
3. [Deadlock](#deadlock)
4. [Livelock](#livelock)
5. [Starvation](#starvation)
6. [Prioritization and Scheduling](#prioritization-and-scheduling)
7. [Example of Threading Issues](#example-of-threading-issues)

## **Introduction**

Threading issues are problems that can arise when multiple threads are executed concurrently in a multi-threaded program. These issues can lead to inefficient use of system resources, crashes, and even security vulnerabilities. In this section, we will discuss the different types of threading issues and their causes.

## **Types of Threading Issues**

- **Deadlock**: A deadlock occurs when two or more threads are blocked indefinitely, each waiting for the other to release a resource.
- **Livelock**: A livelock occurs when two or more threads are busy-waiting for each other to release a resource, resulting in a cycle of no progress.
- **Starvation**: Starvation occurs when a thread is unable to access a shared resource due to other threads holding onto it for an extended period.
- **Prioritization and Scheduling**: Poorly designed thread priorities and scheduling can lead to unfair treatment of threads and inefficient use of system resources.

## **Deadlock**

### Definition

A deadlock is a situation where two or more threads are blocked indefinitely, each waiting for the other to release a resource.

### Causes

- Mutual Exclusion (Mutual Exclusion is a situation where two or more threads require exclusive access to a shared resource.)
- Hold and Wait (A thread is holding onto a resource and waiting for another resource, but that resource is held by another thread.)
- No Preemption (The operating system does not preempt a thread's execution to release a resource.)
- Circular Wait (A thread is waiting for a resource that is held by another thread, which is waiting for the first thread to release a resource.)

### Example

Suppose we have two threads, T1 and T2, that need to access two shared resources, R1 and R2.

|     | T1  | T2  |
| --- | --- | --- |
| R1  | 1   | 2   |
| R2  | 2   | 1   |

Initially, T1 has R1 and T2 has R2. T1 wants to access R2, but T2 is holding onto it. Similarly, T2 wants to access R1, but T1 is holding onto it.

|     | T1  | T2  |
| --- | --- | --- |
| R1  | 2   | 1   |
| R2  | 1   | 2   |

T1 and T2 are now deadlocked, each waiting for the other to release the resource.

## **Livelock**

### Definition

A livelock is a situation where two or more threads are busy-waiting for each other to release a resource, resulting in a cycle of no progress.

### Causes

- Mutual Exclusion (Mutual Exclusion is a situation where two or more threads require exclusive access to a shared resource.)
- No Preemption (The operating system does not preempt a thread's execution to release a resource.)
- Circular Wait (A thread is waiting for a resource that is held by another thread, which is waiting for the first thread to release a resource.)

### Example

Suppose we have two threads, T1 and T2, that need to access two shared resources, R1 and R2.

|     | T1  | T2  |
| --- | --- | --- |
| R1  | 1   | 1   |
| R2  | 2   | 2   |

T1 and T2 are now in a livelock, each waiting for the other to release the resource.

## **Starvation**

### Definition

Starvation occurs when a thread is unable to access a shared resource due to other threads holding onto it for an extended period.

### Causes

- Priority Inversion (A thread with a lower priority is unable to access a shared resource due to a thread with a higher priority holding onto it.)
- Resource Starvation (A thread is unable to access a shared resource due to other threads holding onto it for an extended period.)

### Example

Suppose we have three threads, T1, T2, and T3, that need to access a shared resource, R.

|     | T1  | T2  | T3  |
| --- | --- | --- | --- |
| R   | 1   | 2   | 3   |

T1 and T2 have priority over T3. However, T3 is holding onto R for an extended period. T1 and T2 are now starved of the resource.

## **Prioritization and Scheduling**

### Definition

Poorly designed thread priorities and scheduling can lead to unfair treatment of threads and inefficient use of system resources.

### Causes

- Priority Inversion (A thread with a lower priority is unable to access a shared resource due to a thread with a higher priority holding onto it.)
- Context Switching Overhead (The operating system spends more time switching between threads than executing them.)
- Thread Creation Overhead (The operating system spends more time creating threads than executing them.)

### Example

Suppose we have two threads, T1 and T2, that need to access two shared resources, R1 and R2.

|     | T1  | T2  |
| --- | --- | --- |
| R1  | 1   | 2   |
| R2  | 2   | 1   |

T1 has a higher priority than T2. However, the operating system spends more time switching between the threads than executing them. T1 and T2 are now experiencing poor performance due to the prioritization and scheduling.

## **Example of Threading Issues**

Suppose we have a multi-threaded program that simulates a bank with multiple customers. The program uses two shared resources, the ATM and the cashier.

|         | T1  | T2  | T3  |
| ------- | --- | --- | --- |
| ATM     | 1   | 2   | 1   |
| Cashier | 2   | 1   | 2   |

T1 and T2 are customers who need to access the ATM and the cashier. T3 is the cashier who needs to access the ATM and the cash register.

|               | T1  | T2  | T3  |
| ------------- | --- | --- | --- |
| ATM           | 1   | 2   | 1   |
| Cashier       | 2   | 1   | 2   |
| Cash Register | 3   | 3   | 3   |

T1 and T2 are now in a deadlock situation, each waiting for the other to release the resources. T3 is also waiting for T1 and T2 to release the resources, resulting in a livelock situation.

In conclusion, threading issues are problems that can arise when multiple threads are executed concurrently in a multi-threaded program. These issues can lead to inefficient use of system resources, crashes, and even security vulnerabilities. By understanding the different types of threading issues and their causes, developers can design and implement more efficient and effective multi-threaded programs.
