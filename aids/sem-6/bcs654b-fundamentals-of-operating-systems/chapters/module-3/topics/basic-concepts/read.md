# Basic Concepts of Process Synchronization

## Introduction

Process synchronization is a fundamental concept in operating systems that deals with coordinating the execution of multiple processes to ensure orderly access to shared resources and prevent anomalous behavior. In modern computing environments, where multiple processes execute concurrently on multi-core processors, understanding process synchronization is critical for developing robust and reliable software systems.

The need for synchronization arises because processes frequently need to share data, resources, or communicate with each other. When multiple processes access shared data concurrently without proper coordination, the final outcome becomes unpredictable and depends on the relative timing of their executions. This unpredictability can lead to data inconsistency, deadlock situations, or starvation, making synchronization mechanisms essential for maintaining system integrity and correctness.

This topic introduces the foundational concepts of process synchronization that form the basis for understanding more advanced synchronization techniques like semaphores, mutexes, and monitors. These concepts are essential for the University of Delhi Computer Science curriculum and have significant practical applications in database systems, distributed computing, and real-time systems.

## Key Concepts

### Cooperating Processes

Processes in an operating system can be classified into two categories based on their relationship:

**Independent Processes:** These processes do not affect or get affected by the execution of other processes. They do not share any data or resources with other processes and can execute in isolation without any coordination.

**Cooperating Processes:** These processes either affect or get affected by the execution of other processes. They share data, resources, or communicate through inter-process communication (IPC) mechanisms. Cooperating processes require synchronization to ensure correct and consistent operation.

### Race Condition

A race condition occurs when the outcome of a program depends on the relative timing of interleaved operations of multiple processes or threads accessing shared resources. The term "race" implies that processes are "racing" to access or modify the shared data, and the final result depends on which process wins the race.

Consider a simple example where two processes both want to increment a shared variable `counter`. If the initial value is 0, the expected final value after both processes complete should be 2. However, due to race conditions, the actual result might be 1 if both processes read the old value before either writes back the updated value.

### Critical Section

The critical section is a part of a program that accesses shared variables or shared resources. The critical section problem requires that when one process is executing in its critical section, no other process should be allowed to enter its critical section. This ensures mutual exclusion and prevents race conditions.

A solution to the critical section problem must satisfy three fundamental requirements:

1. **Mutual Exclusion:** At any time, at most one process can be in its critical section. If process P1 is in its critical section, no other process P2 can enter its critical section until P1 exits.

2. **Progress:** If no process is in its critical section and there are processes that wish to enter it, only those processes that are not in their remainder section can participate in the decision of which process will enter next. This selection cannot be postponed indefinitely.

3. **Bounded Waiting:** There exists a limit on the number of times other processes can enter their critical sections after a process has indicated its desire to enter and before that process gets to enter its critical section. This prevents starvation.

### Synchronization Hardware

Many modern processors provide atomic hardware instructions that can lock the memory bus or perform test-and-set operations atomically. These hardware-level mechanisms form the foundation for building software synchronization primitives.

**Test-and-Set Instruction:** This atomic instruction tests the value of a boolean variable and sets it to true in a single indivisible operation. It can be used to implement mutual exclusion locks.

**Swap Instruction:** This atomic instruction swaps the values of two variables. It can be used to implement mutual exclusion in a similar manner to test-and-set.

These hardware instructions solve the critical section problem for two processes but become complex to implement for multiple processes at the software level.

### Synchronization Tools

Higher-level synchronization constructs are built upon hardware instructions:

**Mutex (Mutual Exclusion Lock):** A synchronization primitive that allows only one thread to access a shared resource at a time. It provides two operations: lock() to acquire the lock and unlock() to release it.

**Semaphore:** An integer variable with two atomic operations: wait() and signal(). It was introduced by Edsger Dijkstra and provides a more general synchronization mechanism than mutexes.

**Monitor:** A high-level synchronization construct that combines mutual exclusion with condition variables, allowing processes to wait for certain conditions to be satisfied.

### Deadlock and Starvation

**Deadlock:** A situation where two or more processes are unable to proceed because each is waiting for resources held by the other. For deadlock to occur, four necessary conditions must be satisfied: mutual exclusion, hold and wait, no preemption, and circular wait.

**Starvation:** A situation where a process is perpetually denied access to resources it needs because other processes are continuously granted access to those same resources. Unlike deadlock, starvation can be resolved if the system scheduler gives the starving process higher priority or modifies its scheduling policy.

## Examples

### Example 1: Demonstrating Race Condition

**Problem:** Consider two processes P1 and P2 both executing the following code concurrently:

```
Shared variable: int counter = 0;

Process P1:
    for i = 1 to 1000:
        x = counter
        x = x + 1
        counter = x

Process P2:
    for i = 1 to 1000:
        y = counter
        y = y + 1
        counter = y
```

What are the possible final values of counter? What is the expected value?

**Solution:**

The expected final value of counter should be 2000 (1000 increments from P1 + 1000 increments from P2). However, due to race conditions, the actual value can be anywhere between 1 and 2000.

This happens because when both processes read the value of counter simultaneously, they might read the same value. For example:
- Initial counter = 100
- P1 reads counter into x: x = 100
- P2 reads counter into y: y = 100 (before P1 writes)
- P1 writes: counter = 101
- P2 writes: counter = 101

Both processes incremented, but counter only shows 101 instead of 102. This is the essence of a race condition where the timing of operations affects the final outcome unpredictably.

### Example 2: Peterson's Solution for Two Processes

**Problem:** Explain how Peterson's solution provides mutual exclusion for two processes.

**Solution:**

Peterson's solution is a software-based solution to the critical section problem for two processes. It uses two shared variables:

```
boolean flag[2] = {false, false};
int turn;

Process P0:
    while (true) {
        flag[0] = true;
        turn = 1;
        while (flag[1] && turn == 1)
            ; // busy wait
        // Critical Section
        // ...
        flag[0] = false;
        // Remainder Section
    }

Process P1:
    while (true) {
        flag[1] = true;
        turn = 0;
        while (flag[0] && turn == 0)
            ; // busy wait
        // Critical Section
        // ...
        flag[1] = false;
        // Remainder Section
    }
```

**How it works:**

1. When P0 wants to enter its critical section, it sets flag[0] = true and gives priority to P1 by setting turn = 1.

2. P0 then checks if P1 wants to enter (flag[1] is true) and if it's P1's turn. If both conditions are true, P0 waits.

3. If either flag[1] is false (P1 is not interested) or turn is 0 (it's P0's turn), P0 proceeds to its critical section.

4. After exiting the critical section, P0 sets flag[0] = false, allowing P1 to enter if it wishes.

The solution satisfies all three requirements:
- **Mutual Exclusion:** Both processes cannot be in their critical sections simultaneously because if both flags are true, only the process with turn value matching itself will proceed.
- **Progress:** The busy wait exits when the other process is not interested or it's the current process's turn.
- **Bounded Waiting:** A process can be overtaken at most once because after the other process enters its critical section, it must set its flag to false before the first process can enter again.

### Example 3: Bounded Buffer Problem

**Problem:** Explain the bounded buffer (producer-consumer) problem in the context of process synchronization.

**Solution:**

The bounded buffer problem involves a fixed-size buffer that can hold a limited number of items. There are two types of processes:

- **Producer:** Produces items and stores them in the buffer
- **Consumer:** Removes items from the buffer and consumes them

The synchronization requirements are:
1. The producer should not insert items into a full buffer
2. The consumer should not remove items from an empty buffer
3. Only one process should access the buffer at a time to prevent race conditions

**Solution using semaphores:**

```c
Semaphore mutex = 1;      // Mutual exclusion for buffer
Semaphore empty = n;      // Count of empty slots (n = buffer size)
Semaphore full = 0;       // Count of filled slots

Producer:
    while (true) {
        // Produce item
        wait(empty);
        wait(mutex);
        // Add item to buffer
        signal(mutex);
        signal(full);
    }

Consumer:
    while (true) {
        wait(full);
        wait(mutex);
        // Remove item from buffer
        signal(mutex);
        signal(empty);
        // Consume item
    }
```

This solution ensures that the producer waits when the buffer is full, the consumer waits when the buffer is empty, and only one process accesses the buffer at a time, preventing race conditions.

## Exam Tips

1. **Understand the three requirements of the critical section problem thoroughly.** Questions frequently ask students to explain or prove whether a given solution satisfies mutual exclusion, progress, and bounded waiting.

2. **Be able to identify race conditions in code examples.** examiners often present code snippets and ask whether race conditions exist and how they can be prevented.

3. **Know the differences between semaphores and mutexes.** A mutex provides mutual exclusion and can only be locked by the process that unlocks it, while semaphores can be signaled by any process.

4. **Remember the four necessary conditions for deadlock.** These are mutual exclusion, hold and wait, no preemption, and circular wait. Questions often ask which condition can be broken to prevent deadlock.

5. **Be familiar with classical synchronization problems.** The bounded buffer (producer-consumer), readers-writers, and dining philosophers problems are frequently asked in exams.

6. **Understand the difference between busy-waiting and blocking synchronization.** Busy-waiting (spinlocks) wastes CPU cycles while waiting, whereas blocking synchronization puts processes to sleep.

7. **Practice writing pseudocode for synchronization solutions.** Exam questions often require demonstrating how semaphores or monitors solve specific synchronization problems.

8. **Know the difference between starvation and deadlock.** Starvation can be resolved by the system, while deadlock is a permanent blocking situation requiring external intervention.

9. **Understand the concept of atomic operations.** Synchronization primitives must be atomic (indivisible) to work correctly; otherwise, they themselves can become sources of race conditions.

10. **Be prepared to analyze solutions for correctness.** You may be asked to determine whether a given synchronization solution satisfies the critical section requirements or identify its limitations.