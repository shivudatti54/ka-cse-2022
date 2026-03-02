# Process Synchronization and Critical Section Problem

## Introduction

In modern operating systems, multiple processes execute concurrently, sharing system resources such as CPU, memory, and I/O devices. This concurrent execution introduces a fundamental challenge: **process synchronization** — the coordination of multiple processes to ensure orderly access to shared resources and prevent race conditions. Without proper synchronization, processes can interfere with each other's execution, leading to inconsistent or erroneous results.

The **Critical Section Problem** is the cornerstone of process synchronization theory. It addresses the question: how can we allow multiple processes to access shared data concurrently while maintaining data consistency? This problem was first formalized by Dijkstra in 1965 and remains highly relevant in contemporary computing, from multithreaded applications to distributed systems.

Understanding process synchronization is essential for DU Computer Science students because:
- It forms the theoretical foundation for modern concurrency control
- It is a frequent topic in competitive examinations and campus placements
- Real-world applications (databases, operating systems, cloud computing) rely heavily on these concepts

## Key Concepts

### 1. The Critical Section

A **critical section** is a code segment that accesses shared variables or resources and must not be concurrently executed by more than one process. Consider a simple example: two processes simultaneously attempting to withdraw money from the same bank account. Both might read the current balance, calculate new balances, and write back — potentially leading to lost updates.

Each process has the general structure:
```
do {
    entry section      // Request permission to enter
    critical section   // Access shared resources
    exit section       // Perform cleanup
    remainder section  // Other work
} while (TRUE);
```

### 2. Requirements for a Valid Solution

A solution to the critical section problem must satisfy three fundamental conditions:

**Mutual Exclusion**: No two processes can be in their critical sections simultaneously. If process P₁ is executing in its critical section, no other process can enter its critical section until P₁ exits.

**Progress**: If no process is executing in its critical section and there exist some processes that wish to enter their critical sections, then only those processes that are not in their remainder sections can participate in the decision on which process will enter next. This selection cannot be postponed indefinitely.

**Bounded Waiting** (or First-Come-First-Served): There exists a bound on the number of times other processes are allowed to enter their critical sections after a process has made a request to enter its critical section and before that request is granted.

### 3. Race Condition

A **race condition** occurs when the outcome of execution depends on the relative timing of processes. The system exhibits non-deterministic behavior because multiple processes access and modify shared data concurrently without proper synchronization.

Consider two processes updating a shared variable `counter`:

```
Process P1:              Process P2:
read counter: 5         read counter: 5
counter = counter + 1   counter = counter + 1
write counter: 6        write counter: 6
```

Expected final value: 7 | Actual final value: 6 (lost update)

### 4. Peterson's Algorithm (Software Solution)

Peterson's Algorithm is a classic software-based solution for two processes, proposed by Gary Peterson in 1981. It uses only shared memory variables and requires no special hardware instructions.

```c
// Shared variables
boolean flag[2] = {false, false};
int turn;

 // Process i (where i is 0 or 1)
do {
    flag[i] = true;          // Indicate desire to enter
    turn = 1 - i;            // Give priority to other process
    
    while (flag[1-i] && turn == 1-i)
        ;   // Busy wait (spinlock)
    
    // Critical Section
    critical_section();
    
    flag[i] = false;         // Exit critical section
    remainder_section();
    
} while (true);
```

**Proof of Correctness**:
- **Mutual Exclusion**: Both processes cannot be in the critical section simultaneously. For both to enter, both `flag[0]` and `flag[1]` must be true, and both `turn == 0` and `turn == 1` must hold simultaneously — impossible.
- **Progress**: If the other process is not in its critical section and doesn't wish to enter, the waiting process proceeds.
- **Bounded Waiting**: A process can be prevented from entering at most once before it gets its turn.

### 5. Hardware Solutions

#### TestAndSet Instruction
Atomic operation that reads and modifies a variable in a single uninterruptible step:

```c
boolean TestAndSet(boolean *target) {
    boolean rv = *target;
    *target = true;
    return rv;
}
```

Solution using TestAndSet:
```c
boolean lock = false;

do {
    while (TestAndSet(&lock))
        ;   // Wait until lock is free
    
    // Critical Section
    critical_section();
    
    lock = false;            // Release lock
    remainder_section();
} while (true);
```

#### Swap Instruction
Atomically exchanges values of two variables:

```c
void Swap(boolean *a, boolean *b) {
    boolean temp = *a;
    *a = *b;
    *b = temp;
}
```

### 6. Semaphores

A **semaphore** is a synchronization primitive introduced by Dijkstra in 1965. It is an integer variable accessed through two atomic operations: `wait()` (also called `P()` or `down()`) and `signal()` (also called `V()` or `up()`).

**Binary Semaphore (Mutex)**: Takes only values 0 and 1, used for mutual exclusion.

```c
// Semaphore structure
typedef struct {
    int value;
    struct process *list;
} semaphore;

wait(semaphore *S) {
    S->value--;
    if (S->value < 0) {
        // Add process to S->list
        block();             // Block the process
    }
}

signal(semaphore *S) {
    S->value++;
    if (S->value <= 0) {
        // Remove process P from S->list
        wakeup(P);           // Wake up a waiting process
    }
}
```

**Counting Semaphore**: Can take non-negative integer values, useful for controlling access to multiple identical resources.

### 7. Classical Synchronization Problems

#### Producer-Consumer Problem
A bounded buffer problem where producers create items and consumers consume them. The buffer has limited capacity.

```c
// Shared variables
int n;
semaphore mutex = 1;         // Controls access to buffer
semaphore empty = n;         // Count of empty slots
semaphore full = 0;          // Count of filled slots

// Producer
do {
    // Produce an item
    wait(empty);
    wait(mutex);
    // Add item to buffer
    signal(mutex);
    signal(full);
} while (true);

// Consumer
do {
    wait(full);
    wait(mutex);
    // Remove item from buffer
    signal(mutex);
    signal(empty);
    // Consume item
} while (true);
```

#### Readers-Writers Problem
Multiple readers can access data simultaneously, but writers need exclusive access.

```c
semaphore rw_mutex = 1;
semaphore mutex = 1;
int read_count = 0;

// Writer
do {
    wait(rw_mutex);
    // Writing is performed
    signal(rw_mutex);
} while (true);

// Reader
do {
    wait(mutex);
    read_count++;
    if (read_count == 1)
        wait(rw_mutex);     // First reader locks writers
    signal(mutex);
    
    // Reading is performed
    
    wait(mutex);
    read_count--;
    if (read_count == 0)
        signal(rw_mutex);   // Last reader releases writers
    signal(mutex);
} while (true);
```

#### Dining Philosophers Problem
Five philosophers sit around a table with five chopsticks. Each philosopher alternates between thinking and eating, requiring two chopsticks to eat.

```c
#define N 5
#define LEFT (i + N - 1) % N
#define RIGHT (i + 1) % N
#define THINKING 0
#define HUNGRY 1
#define EATING 2

semaphore state[N];
semaphore mutex = 1;

void philosopher(int i) {
    while (true) {
        think();
        take_chopsticks(i);
        eat();
        put_chopsticks(i);
    }
}

void take_chopsticks(int i) {
    wait(mutex);
    state[i] = HUNGRY;
    test(i);
    signal(mutex);
    wait(state[i]);          // Block if chopsticks unavailable
}

void test(int i) {
    if (state[i] == HUNGRY && 
        state[LEFT] != EATING && 
        state[RIGHT] != EATING) {
        state[i] = EATING;
        signal(state[i]);
    }
}
```

## Examples

### Example 1: Demonstrating Race Condition

**Problem**: Two processes increment a shared counter 10,000 times each. What is the expected final value?

**Solution**:
```
Shared variable: counter = 0

Process P1: counter = counter + 1 (repeated 10000 times)
Process P2: counter = counter + 1 (repeated 10000 times)

Expected final value: 20000
Actual value without synchronization: May be less than 20000

Explanation: The increment operation involves:
1. Read counter into register
2. Increment register
3. Write back to counter

If both processes read 5 before either writes back, both write 6, 
losing one increment — this is a race condition.
```

### Example 2: Peterson's Algorithm Verification

**Problem**: Show that Peterson's Algorithm satisfies mutual exclusion for two processes.

**Solution**:
```
For mutual exclusion to be violated, both processes must be in 
their critical sections simultaneously.

Assume P0 is in critical section. Then:
- flag[0] = true
- P0 passed the while loop, meaning either flag[1] = false 
  or turn = 0

If P1 is also in critical section, then:
- flag[1] = true
- turn must be 1 (for P1 to pass while loop)

But turn can only have one value at a time! If turn = 1, P0 
cannot be in critical section. Contradiction.

Therefore, mutual exclusion is guaranteed.
```

### Example 3: Semaphore for Resource Allocation

**Problem**: Implement a solution for the Readers-Writers problem with writer preference using semaphores.

**Solution**:
```
semaphore mutex = 1;         // Protects read_count
semaphore wrt = 1;           // Writers have exclusive access
int read_count = 0;

// Writer Process
do {
    wait(wrt);
    // Perform write
    signal(wrt);
} while (true);

// Reader Process
do {
    wait(mutex);
    read_count++;
    if (read_count == 1)
        wait(wrt);           // First reader locks out writers
    signal(mutex);
    
    // Perform read
    
    wait(mutex);
    read_count--;
    if (read_count == 0)
        signal(wrt);         // Last reader releases writers
    signal(mutex);
} while (true);
```

## Exam Tips

1. **Know the three conditions**: Memorize Mutual Exclusion, Progress, and Bounded Waiting. Questions frequently ask you to explain how a solution satisfies these conditions.

2. **Difference between semaphores and mutex**: A binary semaphore can be used as a mutex, but they're not identical — semaphores can be signaled by any process, while mutex should only be released by the process that acquired it.

3. **Peterson's Algorithm limitations**: Remember it works only for two processes and requires atomic read/write operations on shared variables.

4. **Busy waiting vs. blocking**: Software solutions (Peterson's) use busy waiting (spinlocks), consuming CPU cycles. Hardware and semaphore solutions can block processes, freeing CPU.

5. **Deadlock vs. Starvation**: Deadlock occurs when processes wait indefinitely for each other; starvation occurs when a process is perpetually denied resources. Know the difference.

6. **Writer preference in Readers-Writers**: The solution shown gives preference to writers — once a writer is waiting, no new readers can enter, preventing writer starvation.

7. **Atomic operations**: Understand that `TestAndSet` and `Swap` are atomic hardware instructions — they execute without interruption, which is crucial for synchronization.

8. **Priority inversion problem**: If a low-priority process holds a lock required by a high-priority process, and a medium-priority process preempts the low-priority one, the high-priority process starves. This is a real OS issue (occurred in Mars Pathfinder).

9. **Bounded buffer**: The producer-consumer problem with a buffer of size n uses three semaphores: mutex (1), empty (n), and full (0).

10. **Atomicity in semaphores**: The wait() and signal() operations must be atomic. In practice, OS kernels disable interrupts or use hardware atomic instructions to ensure this.