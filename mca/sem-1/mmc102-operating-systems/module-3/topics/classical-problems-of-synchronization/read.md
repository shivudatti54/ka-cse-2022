# Classical Problems of Synchronization


## Table of Contents

- [Classical Problems of Synchronization](#classical-problems-of-synchronization)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Producer-Consumer Problem](#producer-consumer-problem)
  - [Readers-Writers Problem](#readers-writers-problem)
  - [Dining Philosophers Problem](#dining-philosophers-problem)
  - [Sleeping Barber Problem](#sleeping-barber-problem)
- [Examples](#examples)
  - [Example 1: Producer-Consumer with Semaphores](#example-1-producer-consumer-with-semaphores)
  - [Example 2: Readers-Writers with Writer Priority](#example-2-readers-writers-with-writer-priority)
  - [Example 3: Dining Philosophers with Resource Hierarchy](#example-3-dining-philosophers-with-resource-hierarchy)
- [Exam Tips](#exam-tips)

## Introduction

Process synchronization is a fundamental concept in operating systems that addresses the challenges of coordinating multiple processes that share resources and data. When multiple processes execute concurrently, they often need to access shared resources such as files, databases, or memory regions. Without proper synchronization, race conditions can occur, leading to inconsistent or incorrect results. The classical problems of synchronization provide canonical examples that illustrate these challenges and demonstrate the solutions using various synchronization primitives like semaphores, monitors, and condition variables.

These problems have been studied extensively since the early days of operating system design and remain highly relevant in modern computing environments. Understanding these problems is essential for any computer scientist or software engineer, as they form the foundation for building reliable concurrent systems. The producer-consumer problem demonstrates bounded buffer management, the readers-writers problem addresses priority-based resource access, the dining philosophers problem illustrates deadlock and starvation concerns in resource allocation, and the sleeping barber problem showcases synchronization in service scenarios. Each problem highlights different aspects of concurrent programming and requires careful design of synchronization mechanisms to ensure correctness, fairness, and efficiency.

## Key Concepts

### Producer-Consumer Problem

The producer-consumer problem, also known as the bounded buffer problem, is one of the most fundamental synchronization problems. In this scenario, one or more producer processes generate data items and place them into a shared buffer, while one or more consumer processes remove and process these items. The buffer has a fixed capacity, which means producers must wait when the buffer is full, and consumers must wait when the buffer is empty.

The solution requires maintaining two counting semaphores: "full" tracks the number of items in the buffer, and "empty" tracks the number of available slots. A binary semaphore "mutex" ensures mutual exclusion when accessing the buffer. Producers first wait on the "empty" semaphore to check for available space, then acquire the mutex to safely add an item, and finally signal the "full" semaphore. Consumers perform the inverse operation: wait on "full" to check for available items, acquire the mutex to remove an item, signal "empty" to indicate a freed slot, and then process the item. This approach ensures that producers and consumers never access the buffer simultaneously and that neither process blocks unnecessarily.

### Readers-Writers Problem

The readers-writers problem deals with access to a shared database or resource where multiple readers can access the data concurrently, but writers require exclusive access. This problem models scenarios like database systems, file servers, and cached data structures where read operations are far more frequent than write operations.

The basic solution uses two semaphores: "readcount" to track the number of readers currently accessing the resource, and "rw_mutex" to provide mutual exclusion for writers. When a reader wants to access the database, it first increments "readcount." If this is the first reader, it acquires "rw_mutex" to block writers. Subsequent readers simply proceed without additional locking. When a reader finishes, it decrements "readcount," and if this is the last reader, it releases "rw_mutex" to allow writers to proceed. Writers must acquire "rw_mutex" exclusively, which ensures no reader or other writer can access the resource simultaneously.

Different variations of this problem exist with varying priority schemes. The first readers-writers problem gives priority to readers, potentially causing writer starvation. The second readers-writers problem gives priority to writers, which may cause reader starvation. The third solution ensures that no thread waits indefinitely, providing fair access to both readers and writers.

### Dining Philosophers Problem

The dining philosophers problem is a classic illustration of deadlock and resource allocation in concurrent systems. Five philosophers sit around a circular table, with each philosopher thinking or eating. Between each pair of philosophers is a fork, and a philosopher needs both forks to eat. The challenge is to design a protocol that allows all philosophers to eat without deadlocking or starving.

A naive solution where each philosopher picks up the fork on their left and then the fork on their right can lead to deadlock if all philosophers pick up their left forks simultaneously, waiting forever for the right fork. Several solutions exist to address this problem. The resource hierarchy solution assigns a unique number to each fork, and philosophers always pick up the lower-numbered fork first, breaking the circular wait condition. Another solution uses a waiter or arbiter who allows at most four philosophers to sit at the table simultaneously, preventing the deadlock scenario. The asymmetric solution has odd-numbered philosophers pick up the left fork first, while even-numbered philosophers pick up the right fork first.

### Sleeping Barber Problem

The sleeping barber problem describes a barber shop with a limited number of chairs for waiting customers. The barber sleeps when there are no customers and wakes up when a customer arrives. If the barber is busy, customers either wait in available chairs or leave if all chairs are occupied. This problem models scenarios like task scheduling, job queues, and resource pooling in computer systems.

The solution uses three semaphores: "customers" counts waiting customers, "barbers" tracks the number of available barbers (initially zero), and "mutex" provides mutual exclusion for shared variables. Additionally, a "waiting" counter tracks the number of customers in the waiting room. The barber process waits on the "customers" semaphore, and when awakened, calls the customer service function. The customer process first acquires the mutex, checks if there is room in the waiting area, and either leaves or waits depending on availability. If space exists, the customer increments the waiting count, signals the "customers" semaphore to wake the barber, and waits on the "barbers" semaphore to receive service.

## Examples

### Example 1: Producer-Consumer with Semaphores

Consider a producer-consumer problem with a buffer of size 5. Initially, full = 0, empty = 5, and mutex = 1.

Producer process:
```
wait(empty)      // empty becomes 4
wait(mutex)      // mutex becomes 0, enter critical section
// add item to buffer
signal(mutex)    // mutex becomes 1, exit critical section
signal(full)     // full becomes 1
```

Consumer process:
```
wait(full)       // full becomes 0
wait(mutex)      // mutex becomes 0, enter critical section
// remove item from buffer
signal(mutex)    // mutex becomes 1, exit critical section
signal(empty)    // empty becomes 5
```

When the buffer is full (5 items), the producer will block on wait(empty), unable to add more items until the consumer removes one. When the buffer is empty, the consumer will block on wait(full). The mutex ensures that only one process accesses the buffer at a time, preventing race conditions.

### Example 2: Readers-Writers with Writer Priority

In a system with writer priority, the solution modifies the basic readers-writers algorithm to prevent writer starvation. The key modification is that writers must wait even if readers are accessing the resource.

```
Writer:
wait(writer_mutex)      // Acquire exclusive lock
// Perform write operation
signal(writer_mutex)

Reader:
wait(mutex)
readcount = readcount + 1
if readcount == 1:
    wait(writer_mutex)  // First reader locks out writers
signal(mutex)

// Perform read operation

wait(mutex)
readcount = readcount - 1
if readcount == 0:
    signal(writer_mutex) // Last reader allows writers
signal(mutex)
```

This solution ensures that once a writer is waiting, no new readers can enter, allowing the writer to proceed after the current readers finish.

### Example 3: Dining Philosophers with Resource Hierarchy

Using four philosophers and four forks with unique IDs (0-3), philosopher i picks up fork i first, then fork (i+1) mod 4:

Philosopher 0: picks fork 0 (lower ID), then fork 1
Philosopher 1: picks fork 1 (lower ID), then fork 2
Philosopher 2: picks fork 2 (lower ID), then fork 3
Philosopher 3: picks fork 3 (lower ID), then fork 0

This solution prevents circular wait because philosopher 3 picks fork 0 (ID 0) before fork 3 (ID 3), breaking the circular dependency. The philosopher with the highest-numbered fork (philosopher 3) picks up the lowest-numbered fork first, ensuring no two philosophers wait for the same fork in a circular manner.

## Exam Tips

For the University of Delhi Operating Systems examinations, focus on understanding the core synchronization mechanisms rather than memorizing code. Examiners frequently ask students to explain why synchronization is necessary and to identify race conditions in given code segments. Practice drawing timeline diagrams showing interleaving of processes that lead to incorrect behavior without proper synchronization.

The relationship between semaphores and their initial values is crucial. Remember that binary semaphores used for mutual exclusion are initialized to 1, while counting semaphores representing available resources are initialized to the number of those resources. The order of wait operations matters significantly; in the producer-consumer problem, always wait on the counting semaphore before the mutex to avoid deadlock scenarios.

Understanding the conditions required for deadlock is essential. The dining philosophers problem is particularly important for demonstrating how each of the four necessary conditions for deadlock (mutual exclusion, hold and wait, no preemption, and circular wait) can be violated. Be prepared to analyze proposed solutions and identify which deadlock condition they address.

The readers-writers problem frequently appears in exams with questions about modifying priority schemes. Know the differences between reader priority, writer priority, and fair solutions, and be able to implement or analyze each variant. The trade-off between throughput and fairness is a common examination topic.

When answering descriptive questions, use proper terminology: critical section refers to the code segment accessing shared resources, while mutual exclusion ensures only one process enters the critical section at a time. Progress and bounded waiting are properties that a good synchronization solution must satisfy.

For numerical problems, be prepared to trace through semaphore operations. Given initial values and a sequence of process operations, determine the final state or identify when processes block. Draw state diagrams showing which processes are in ready, blocked, or running states.