# Synchronization

## Introduction

In modern computing systems, multiple processes and threads execute concurrently, sharing system resources such as CPU time, memory, and I/O devices. While concurrency improves system throughput and responsiveness, it introduces significant challenges related to data consistency and coordination. Synchronization is the mechanism by which processes coordinate their activities to ensure mutually exclusive access to shared resources and maintain system correctness.

The importance of synchronization in operating systems cannot be overstated. Without proper synchronization, concurrent access to shared data can lead to race conditions, where the final outcome depends on the unpredictable order of execution. Consider a bank account scenario where two transactions simultaneously withdraw money from the same account—without synchronization, both transactions might read the same balance, perform their calculations, and write back values, resulting in incorrect final balance. Such data corruption can have severe consequences in mission-critical applications.

This topic builds directly upon the critical section problem and synchronization hardware discussed earlier in this module. We will explore the fundamental concepts of process synchronization, examine various synchronization mechanisms including semaphores and monitors, and analyze classical synchronization problems that have shaped operating system design. Understanding these concepts is essential for developing robust concurrent programs and for comprehending how operating systems manage resource sharing efficiently.

## Key Concepts

### Race Conditions

A race condition occurs when the correctness of a program depends on the relative timing of events such as the order in which threads are scheduled. The program produces incorrect results when threads execute in certain sequences. Race conditions typically arise when multiple processes access and modify shared data concurrently without proper coordination.

Consider two processes P1 and P2 sharing a variable `counter`. If P1 reads the value 10, increments it to 11, and P2 reads the value 10 before P1 writes back 11, both processes will write 11 to `counter`, resulting in the final value of 11 instead of the correct value 12. ThisLost Update problem exemplifies a race condition.

### Critical Section

The critical section is a code segment that accesses shared variables or resources and must not be concurrently executed by more than one process. The critical section problem requires designing a protocol that ensures mutual exclusion, progress, and bounded waiting—the three fundamental requirements discussed in the preceding topic on the critical section problem.

Any synchronization solution must ensure that only one process can be inside its critical section at any given time. The entry section precedes the critical section where processes request permission to enter, and the exit section follows where processes indicate they are leaving the critical section.

### Synchronization Mechanisms

Operating systems provide various synchronization primitives to coordinate process activities. Software-based solutions like Peterson's algorithm and hardware-based solutions like test-and-set and compare-and-swap have been discussed previously. This section focuses on higher-level abstractions.

**Semaphores:** A semaphore is an integer variable with two atomic operations: wait() and signal(). The wait operation (also called P or down) decrements the semaphore value, blocking the process if the value becomes negative. The signal operation (also called V or up) increments the semaphore value, waking up a waiting process if any exist.

Binary semaphores (mutex locks) take only values 0 and 1, providing mutual exclusion. Counting semaphores can take any non-negative integer, representing the number of available resources. Semaphores solve the critical section problem elegantly and are widely used in operating systems.

**Monitors:** A monitor is a high-level synchronization construct that combines data abstraction with condition variables. Monitors encapsulate shared data and the procedures that operate on them, ensuring that only one process can be active inside the monitor at any time. Condition variables allow processes to wait for specific conditions to become true within the monitor.

The monitor concept provides inherent mutual exclusion—programmers need not explicitly implement synchronization within monitor procedures. This abstraction significantly reduces synchronization errors and improves program modularity.

### Classical Synchronization Problems

Several canonical problems have shaped the study of process synchronization, serving as benchmarks for evaluating synchronization solutions.

The Producer-Consumer problem involves processes that produce data items (producers) and processes that consume these items (consumers). A bounded buffer (the classic circular buffer implementation) stores produced items for consumption. Producers must wait when the buffer is full, and consumers must wait when the buffer is empty. The solution requires tracking buffer state with counting semaphores for empty and full slots, plus a binary semaphore for mutual exclusion.

The Readers-Writers problem concerns a shared data object accessed by multiple reader and writer processes. Multiple readers can access the object simultaneously, but writers require exclusive access. Various reader-writer lock implementations prioritize readers, writers, or employ fair scheduling to prevent starvation.

The Dining Philosophers problem represents resource allocation among competing processes. Five philosophers sit around a circular table with five forks, each philosopher needing two forks to eat. The challenge is designing a deadlock-free solution where philosophers can eat without permanently blocking each other.

### Deadlock

Deadlock occurs when a set of processes are permanently blocked because each process is waiting for resources held by other processes in the set. The four necessary conditions for deadlock are mutual exclusion (resources are non-sharable), hold and wait (processes hold resources while waiting for others), no preemption (resources cannot be forcibly taken), and circular wait (a circular chain of processes exists where each process waits for a resource held by the next).

Deadlock handling strategies include prevention (ensuring at least one condition cannot hold), avoidance (dynamically allocating resources using algorithms like Banker's Algorithm), detection (periodically checking for deadlock existence), and recovery (terminating processes or preempting resources).

## Examples

### Example 1: Solving the Producer-Consumer Problem with Semaphores

**Problem:** Implement synchronization for a bounded buffer with capacity N using semaphores.

**Solution:**

```c
#define N 100
semaphore mutex = 1;      // Controls access to critical section
semaphore empty = N;      // Counts empty buffer slots
semaphore full = 0;       // Counts filled buffer slots

void producer() {
    while(true) {
        item = produce();
        wait(empty);
        wait(mutex);
        // Add item to buffer
        put(item);
        signal(mutex);
        signal(full);
    }
}

void consumer() {
    while(true) {
        wait(full);
        wait(mutex);
        item = get();
        signal(mutex);
        signal(empty);
        consume(item);
    }
}
```

**Step-by-step explanation:**
1. The `empty` semaphore tracks available slots, initialized to N
2. The `full` semaphore tracks filled slots, initialized to 0
3. The `mutex` provides mutual exclusion for buffer operations
4. Producer waits for empty slot, acquires mutex, adds item, releases mutex, signals full
5. Consumer waits for full slot, acquires mutex, removes item, releases mutex, signals empty

### Example 2: Analyzing a Race Condition

**Problem:** Identify and fix the race condition in the following code where two threads increment a shared variable.

**Problematic Code:**
```c
int shared_counter = 0;

void increment() {
    int temp = shared_counter;  // Read
    temp = temp + 1;            // Modify
    shared_counter = temp;      // Write
}
// Two threads call increment() simultaneously
```

**Analysis:**
If both threads execute in interleaved fashion:
1. Thread 1 reads shared_counter (0), Thread 2 reads shared_counter (0)
2. Thread 1 computes temp+1 (1), Thread 2 computes temp+1 (1)
3. Thread 1 writes 1, Thread 2 writes 1
Result: shared_counter = 1 (incorrect, should be 2)

**Fixed Code using Semaphore:**
```c
int shared_counter = 0;
semaphore sem = 1;

void increment() {
    wait(sem);
    shared_counter++;
    signal(sem);
}
```

### Example 3: Banker's Algorithm for Deadlock Avoidance

**Problem:** Determine if the following state is safe using Banker's Algorithm.

**Current State (processes P0, P1, P2):**

| Process | Allocation | Maximum | Available |
|---------|------------|---------|-----------|
| P0      | 1 0 1      | 3 2 2   |           |
| P1      | 2 0 0      | 2 2 2   |           |
| P2      | 1 1 0      | 3 1 1   | 2 1 1     |

**Solution:**
Step 1: Calculate Need = Maximum - Allocation

| Process | Need    |
|---------|---------|
| P0      | 2 2 1   |
| P1      | 0 2 2   |
| P2      | 2 0 1   |

Step 2: Find safe sequence
- Available = (2,1,1)
- Can P1 execute? Need = (0,2,2) — No
- Can P0 execute? Need = (2,2,1) — No
- Can P2 execute? Need = (2,0,1) — Yes (2≥2, 1≥1, 1≥1)

Execute P2, Available = (2,1,1) + (1,1,0) = (3,2,1)

- Can P1 execute? Need = (0,2,2) — No (2≤3, 2≤2 ✓, 2≤1 ✗)
- Can P0 execute? Need = (2,2,1) — Yes (2≤3, 2≤2 ✓, 1≤1 ✓)

Execute P0, Available = (3,2,1) + (1,0,1) = (4,3,2)

- P1 can now execute: Need = (0,2,2), Available = (4,3,2) ✓

Safe sequence: P2 → P0 → P1

The state is SAFE since a safe sequence exists.

## Exam Tips

For DU semester examinations, master these essential points:

1. **Semaphore Operations:** Remember that wait() and signal() must be atomic. The wait operation checks the semaphore value and blocks the process if necessary—all in one uninterruptible step.

2. **Critical Section Requirements:** Ensure you can explain and distinguish between mutual exclusion (only one process in critical section), progress (processes not in entry or exit sections can participate in decision), and bounded waiting (limit on number of times other processes can enter critical section after a process requests entry).

3. **Deadlock Conditions:** The four Coffman conditions must be understood thoroughly—mutual exclusion, hold and wait, no preemption, and circular wait. All four must hold simultaneously for deadlock to occur.

4. **Difference between Prevention and Avoidance:** Deadlock prevention removes at least one necessary condition statically. Deadlock avoidance uses dynamic resource allocation analysis (Banker's Algorithm) to ensure safe states.

5. **Classical Problems:** Be prepared to write semaphore solutions for Producer-Consumer, Readers-Writers, and Dining Philosophers problems. Understand the specific constraints of each problem.

6. **Monitor Implementation:** In exam questions, monitors provide automatic mutual exclusion. Only condition variables (wait and signal operations) require explicit synchronization handling.

7. **Starvation vs Deadlock:** Distinguish clearly—deadlock involves permanent blocking, while starvation means a process waits indefinitely but may eventually get the resource (often due to unfair scheduling).

8. **Banker's Algorithm:** Practice computing Need matrices, determining safe sequences, and evaluating resource request safety using the Banker's Algorithm—classic questions in DU examinations.