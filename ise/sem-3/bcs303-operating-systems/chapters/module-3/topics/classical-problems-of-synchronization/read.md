# Classical Problems of Synchronization

## Introduction

The classical problems of synchronization represent foundational challenges in concurrent programming that every computer science student must master. These problems emerge when multiple processes or threads attempt to access shared resources simultaneously, leading to race conditions, data inconsistency, and unpredictable behavior. The University of Delhi curriculum recognizes these problems as essential for understanding how operating systems manage concurrent access to shared resources.

The significance of these synchronization problems extends far beyond academic exercises. Modern operating systems, database management systems, and distributed applications constantly grapple with these same issues. When multiple users access a banking database, when web servers handle simultaneous requests, or when multi-threaded applications process shared data, the solutions to these classical problems are at work behind the scenes. Understanding these problems provides the theoretical foundation for designing robust, efficient, and correct concurrent systems.

This topic covers four major classical synchronization problems: the Producer-Consumer Problem (also known as the Bounded Buffer Problem), the Readers-Writers Problem, the Dining Philosophers Problem, and the Sleeping Barber Problem. Each problem illustrates different aspects of process coordination and requires specific synchronization strategies to resolve.

## Key Concepts

### The Producer-Consumer Problem

The Producer-Consumer problem represents one of the most fundamental synchronization challenges. In this scenario, there exists a bounded buffer (a fixed-size array or queue) that is shared between producer processes and consumer processes. Producers generate data items and place them into the buffer, while consumers remove items from the buffer for processing. The buffer has a limited capacity, which creates two critical synchronization requirements.

First, producers must not add items to a full buffer—they must wait until a consumer removes an item and creates space. Second, consumers must not remove items from an empty buffer—they must wait until a producer adds an item. This problem demonstrates the concept of condition synchronization, where processes must wait for specific conditions (buffer not full, buffer not empty) before proceeding.

The solution typically uses two counting semaphores: "empty" (count of empty slots) initialized to the buffer size N, and "full" (count of filled slots) initialized to 0. A mutex semaphore ensures mutual exclusion for buffer access. The producer waits on "empty" before producing, signals "full" after producing, while the consumer waits on "full" before consuming and signals "empty" after consuming.

### The Readers-Writers Problem

The Readers-Writers Problem addresses a different synchronization scenario where multiple readers can access a shared resource simultaneously, but writers require exclusive access. This situation arises frequently in database systems and file management, where read operations are common and non-destructive, while write operations modify the shared data.

The key insight is that multiple readers do not interfere with each other—a shared variable can be safely read by many processes concurrently. However, any writer must have exclusive access to prevent data corruption or inconsistent reads during modifications. This creates a tension between allowing concurrent reads and ensuring exclusive writes.

Solutions to this problem can prioritize readers or writers. A reader-preference solution allows readers to proceed immediately if no writer is waiting, which may cause writer starvation. A writer-preference solution grants writers immediate access when available, ensuring no reader or writer starvation. The readcount variable tracks the number of active readers, and the rw_mutex semaphore controls access to the resource itself.

### The Dining Philosophers Problem

The Dining Philosophers Problem, formulated by Edsger Dijkstra, provides an elegant illustration of deadlock and resource allocation challenges. Five philosophers sit around a circular table, with each philosopher thinking or eating. Between each pair of philosophers lies a fork, and a philosopher needs both adjacent forks to eat. The table has five forks total.

This problem demonstrates how deadlock can occur when processes compete for limited resources. If each philosopher picks up their left fork simultaneously, all forks are acquired, but no philosopher can pick up their right fork—deadlock results. The problem also illustrates starvation, where a philosopher might never get both forks if neighbors continuously alternate between thinking and eating.

Solutions range from simple to sophisticated. A centralized solution uses a butler (arbitrator) that allows at most four philosophers to sit at once, preventing deadlock. An asymmetric solution assigns different picking orders to odd and even philosophers. Modern solutions often use a semaphore to represent each fork, with additional synchronization to prevent circular wait conditions.

### The Sleeping Barber Problem

The Sleeping Barber Problem models a barber shop with a limited number of chairs for waiting customers. The barber sleeps when there are no customers, wakes up when a customer arrives, and cuts hair for a fixed duration. Customers arrive at random intervals and leave if all waiting chairs are occupied.

This problem demonstrates inter-process communication and signaling. The barber process must wait (sleep) until a customer arrives. When a customer arrives, they must signal the barber to wake up. If waiting chairs are available, the customer sits and waits; otherwise, the customer leaves. After cutting hair, the barber checks for more waiting customers.

The solution uses three semaphores: customers (count of waiting customers), barbers (availability of barber), and mutex (mutual exclusion for shared variables). A waiting room with a finite number of chairs is represented by the customer count. The barber waits on the customers semaphore, customers signal on customers semaphore after sitting, and mutex protects the critical section where customer count is modified.

## Examples

### Example 1: Producer-Consumer Solution Using Semaphores

Consider a producer-consumer problem with buffer size N=5. Trace the execution:

INITIAL STATE:
- empty = 5 (five empty slots)
- full = 0 (no items produced)
- mutex = 1 (unlocked)

STEP 1: Producer P1 produces first item
- P1 waits(empty): empty becomes 4, proceeds
- P1 enters critical section (mutex lock)
- P1 adds item to buffer
- P1 exits critical section (mutex unlock)
- P1 signals(full): full becomes 1

STATE: empty=4, full=1, buffer=[item1, -, -, -, -]

STEP 2: Consumer C1 consumes first item
- C1 waits(full): full becomes 0, proceeds
- C1 enters critical section
- C1 removes item from buffer
- C1 exits critical section
- C1 signals(empty): empty becomes 5

STEP 3: Producer P2 produces, Consumer C1 consumes simultaneously
If P2 executes wait(empty) before C1 signals(empty):
- P2: empty becomes 3, produces item2
- C1: full was 0, waits (cannot proceed until P2 signals)

This demonstrates how semaphores coordinate execution and prevent race conditions.

### Example 2: Readers-Writers Problem Solution

Given a shared database with multiple readers and writers, illustrate a reader-preference solution:

SHARED VARIABLES:
- readcount = 0 (number of active readers)
- db = 1 (semaphore for database access)
- mutex = 1 (semaphore for readcount protection)

READER PROCESS:
```
wait(mutex);
readcount = readcount + 1;
if (readcount == 1)
    wait(db);  // First reader locks database
signal(mutex);

// ... reading database ...

wait(mutex);
readcount = readcount - 1;
if (readcount == 0)
    signal(db);  // Last reader releases database
signal(mutex);
```

WRITER PROCESS:
```
wait(db);  // Exclusive access
// ... writing database ...
signal(db);
```

With this solution, if multiple readers are active, subsequent readers can join without blocking. However, a waiting writer may starve if readers continuously arrive.

### Example 3: Dining Philosophers with Asymmetric Solution

For five philosophers, implement an asymmetric solution where odd philosophers pick left fork first, then right fork, while even philosophers pick right fork first, then left fork:

PHILOSOPHER i (where i is odd):
```
while (true) {
    think;
    wait(fork[i]);      // Pick up left fork
    wait(fork[(i+1)%5]); // Pick up right fork
    eat;
    signal(fork[i]);    // Put down left fork
    signal(fork[(i+1)%5]); // Put down right fork
}
```

PHILOSOPHER i (where i is even):
```
while (true) {
    think;
    wait(fork[(i+1)%5]); // Pick up right fork first
    wait(fork[i]);      // Pick up left fork
    eat;
    signal(fork[(i+1)%5]); // Put down right fork
    signal(fork[i]);    // Put down left fork
}
```

This asymmetric approach prevents circular wait—the necessary condition for deadlock. Philosopher 0 picks fork 1 first, Philosopher 1 picks fork 2 first, breaking the circular dependency.

## Exam Tips

1. UNDERSTAND THE CORE MECHANISM: For each classical problem, clearly identify what is being synchronized (buffer slots, database access, forks, customers) and which synchronization primitives (semaphores, mutexes, condition variables) are required.

2. INITIALIZATION MATTERS: Always remember the initial values for semaphores. For Producer-Curor: empty=N, full=0, mutex=1. For Readers-Writers: readcount=0, rw_mutex=1, mutex=1. Missing or incorrect initialization leads to deadlock or incorrect behavior.

3. IDENTIFY RACE CONDITIONS: Be able to spot potential race conditions in synchronization problems. The producer-consumer problem has races on buffer modifications, readers-writers has races on readcount, and dining philosophers has races on fork acquisition.

4. DEADLOCK ANALYSIS: For the Dining Philosophers problem, analyze why certain solutions cause deadlock. Four conditions must hold: mutual exclusion, hold and wait, no preemption, and circular wait.

5. SOLUTION TRACING: Practice tracing through execution with sample values. Draw timeline diagrams showing which process executes which operation at each step to verify correctness.

6. DIFFERENTIATE PROBLEM TYPES: Producer-Consumer is about COUNTING synchronization (how many slots/items). Readers-Writers is about MUTEX with multiple readers. Dining Philosophers is about RESOURCE ALLOCATION. Sleeping Barber is about SIGNALLING between processes.

7. SEMAPHORE OPERATIONS: Remember that wait() (or P() or down()) decrements the semaphore value and blocks if the result is negative. Signal() (or V() or up()) increments the value and wakes up a waiting process if any.

8. WRITER STARVATION: In the Readers-Writers problem, understand the difference between reader-preference and writer-preference solutions and analyze which processes may starve under each approach.