# Module 1: Coordinating Processes and Threads

## 1. Introduction to Process and Thread Coordination

In parallel computing, the fundamental objective is to decompose a computationally intensive problem into smaller, independent sub-tasks that can execute concurrently, thereby reducing overall execution time and utilizing multiple processing units effectively. These sub-tasks are realized through **processes**—heavyweight entities possessing independent memory spaces—and **threads**—lightweight entities that share the memory space of their parent process. While these concurrent entities operate with a degree of independence, they frequently require coordination to collaborate on shared tasks, exchange data, or access common resources such as files, databases, or shared variables.

Without proper coordination mechanisms, concurrent execution introduces several critical challenges: **race conditions** occur when multiple entities access shared data concurrently and the final outcome depends on the unpredictable order of execution; **data inconsistency** arises when shared state is modified in an uncoordinated manner; and **deadlock** emerges when entities wait indefinitely for resources held by each other. Consequently, the coordination of processes and threads is essential for ensuring correct, predictable, and efficient execution of parallel programs. This module examines the theoretical foundations and practical mechanisms for achieving effective synchronization and communication in concurrent systems.

## 2. The Critical Section Problem

### 2.1. Formal Problem Definition

The **Critical Section Problem** constitutes the fundamental challenge in process synchronization. Consider a system with _n_ processes (P₀, P₁, ..., Pₙ₋₁), each possessing a **critical section**—a segment of code where the process accesses shared resources such as variables, data structures, printers, or network connections. The critical section problem requires designing a protocol that ensures only one process can execute within its critical section at any given time, while permitting non-critical sections to execute concurrently.

The structure of each process follows the canonical pattern illustrated in Algorithm 1, where processes cyclically execute entry section, critical section, exit section, and remainder section.

```
while (true) {
    entry_section();     // Request permission to enter critical section
    critical_section();  // Access shared resources
    exit_section();      // Perform cleanup and signal completion
    remainder_section(); // Execute non-critical code
}
```

**Algorithm 1:** Canonical structure of a process with critical section

### 2.2. Requirements for a Valid Solution

A correct solution to the critical section problem must satisfy three essential conditions, formally defined as follows:

**Definition 2.1 (Mutual Exclusion):** A solution exhibits mutual exclusion if and only if for any execution, at most one process is executing in its critical section at any instant. Formally: ∀t : |{Pᵢ | Pᵢ is in critical section at time t}| ≤ 1

**Definition 2.2 (Progress):** The progress condition ensures that no process waits indefinitely to enter its critical section when the critical section is vacant. Formally: If no process is executing in its critical section and there exist processes that wish to enter (in their entry sections), then only those processes that are not executing in their remainder sections can participate in the decision of which process enters next. This decision cannot be postponed indefinitely.

**Definition 2.3 (Bounded Waiting):** Bounded waiting prevents starvation by imposing a limit on the number of times other processes can enter their critical sections after a process has requested entry but before that process gains access. Formally: There exists a bound _B_ such that if process Pᵢ has made a request to enter its critical section, then Pᵢ will enter within at most _B_ critical section executions by other processes.

### 2.3. Peterson's Algorithm (Two-Process Mutual Exclusion)

For two processes (P₀ and P₁), **Peterson's Algorithm** provides a software-based solution satisfying all three conditions. The algorithm utilizes two shared variables: `turn` indicates whose turn it is, and `flag[i]` indicates whether process Pᵢ desires to enter its critical section.

```c
// Shared variables
int turn;                 // Indicates whose turn it is
boolean flag[2];          // flag[i] = true indicates Pᵢ is ready to enter

// Process Pᵢ (where i is 0 or 1, and j = 1 - i)
do {
    flag[i] = TRUE;       // Pᵢ indicates desire to enter
    turn = j;             // Give priority to Pⱼ
    while (flag[j] && turn == j)  // Wait while Pⱼ wants to enter
        ;                 // and it's Pⱼ's turn
    critical_section();
    flag[i] = FALSE;      // Pᵢ exits critical section
    remainder_section();
} while (TRUE);
```

**Algorithm 2:** Peterson's Algorithm for two processes

**Theorem 2.1 (Correctness of Peterson's Algorithm):** Peterson's Algorithm satisfies mutual exclusion, progress, and bounded waiting.

_Proof of Mutual Exclusion:_ Process Pᵢ can enter its critical section only when either flag[j] is FALSE (Pⱼ is not interested) or turn equals i (it is Pᵢ's turn). Both conditions cannot hold simultaneously for both processes. Suppose both P₀ and P₁ attempt to enter simultaneously. The last assignment to `turn` determines which process proceeds. If turn = 0, then P₁ waits because the condition (flag[0] && turn == 0) evaluates to TRUE. Conversely, if turn = 1, then P₀ waits. Therefore, at most one process executes in the critical section at any time. ∎

_Proof of Progress:_ If the critical section is vacant and both processes attempt to enter, the last assignment to `turn` determines which process proceeds. The process with turn = i proceeds while the other waits at the while condition. Since the waiting process is not in its remainder section (it is actively attempting to enter), the decision of which process enters next is made solely among the interested processes, satisfying the progress condition. ∎

_Proof of Bounded Waiting:_ Consider Pᵢ requesting entry while Pⱼ is executing in its critical section. When Pⱼ exits, it sets flag[j] = FALSE, allowing Pᵢ to proceed. If Pⱼ wishes to re-enter before Pᵢ gains access, it must set flag[j] = TRUE and turn = i. However, since Pᵢ has already set flag[i] = TRUE and turn = j, the condition (flag[j] && turn == j) evaluates to FALSE for Pⱼ when j = i. Thus, Pᵢ enters before Pⱼ can enter again, ensuring bounded waiting with bound B = 1. ∎

### 2.4. The Bakery Algorithm (N-Process Mutual Exclusion)

For _n_ processes, **Lamport's Bakery Algorithm** provides a lock-free solution based on a customer service model where processes obtain a "ticket number" before entering their critical section. The algorithm ensures fairness through lexicographic ordering of ticket numbers.

```c
// Shared variables
boolean choosing[n];  // choosing[i] = true when Pᵢ is selecting a number
int number[n];        // ticket number for each process

// Process Pᵢ
do {
    choosing[i] = TRUE;
    number[i] = max(number[0], number[1], ..., number[n-1]) + 1;
    choosing[i] = FALSE;

    for (int j = 0; j < n; j++) {
        while (choosing[j]) ;  // Wait for Pⱼ to finish choosing
        while (number[j] != 0 &&
               (number[j] < number[i] ||
                (number[j] == number[i] && j < i))) ;
    }

    critical_section();
    number[i] = 0;  // Reset for next iteration
    remainder_section();
} while (TRUE);
```

**Algorithm 3:** Lamport's Bakery Algorithm for N processes

**Theorem 2.2 (Correctness of Bakery Algorithm):** The Bakery Algorithm satisfies mutual exclusion, progress, and bounded waiting for n processes.

_Proof Sketch:_ Mutual exclusion follows from the observation that if two processes Pᵢ and Pⱼ are in their critical sections simultaneously, they must have been in the for-loop simultaneously. The while conditions ensure that a process waits if another process has a smaller ticket number (or same number with smaller process index). This creates a total ordering preventing simultaneous entry. Progress holds because the choosing[] array ensures processes complete ticket selection before comparison. Bounded waiting follows from the FIFO nature of ticket assignment—once Pᵢ obtains a ticket, only finitely many processes with smaller tickets can enter before Pᵢ. ∎

## 3. Synchronization Hardware and Primitives

### 3.1. Hardware Synchronization Instructions

Modern processor architectures provide atomic hardware instructions that enable efficient implementation of synchronization primitives. **Test-and-Set** atomically reads and modifies a memory location, while **Compare-and-Swap** conditionally updates a value only if it matches an expected value.

```c
// Test-and-Set instruction
boolean TestAndSet(boolean *target) {
    boolean temp = *target;
    *target = TRUE;
    return temp;
}

// Compare-and-Swap instruction
int CompareAndSwap(int *ptr, int expected, int new_value) {
    int actual = *ptr;
    if (actual == expected)
        *ptr = new_value;
    return actual;
}
```

These instructions form the foundation for implementing locks, semaphores, and other synchronization mechanisms in operating systems and concurrent programming frameworks.

### 3.2. Mutex Locks

A **mutex (mutual exclusion lock)** provides exclusive access to a critical section. The lock is acquired before entering the critical section and released upon exiting. Implementation using Test-and-Set ensures atomicity:

```c
typedef struct {
    boolean lock = FALSE;
} Mutex;

void lock(Mutex *m) {
    while (TestAndSet(&m->lock)) ;  // Spin until acquired
}

void unlock(Mutex *m) {
    m->lock = FALSE;
}
```

### 3.3. Semaphores

A **semaphore** is an integer variable with two atomic operations: `wait()` (also called `P()` or `down()`) and `signal()` (also called `V()` or `up()`). Semaphores can function as counting semaphores (allowing multiple concurrent accesses) or binary semaphores (functioning as mutexes).

**Definition 3.1 (Semaphore):** A semaphore S is an integer variable initialized to a non-negative value, operated upon by two atomic operations:

- `wait(S)`: Atomically decrement S; if S < 0, block the calling process
- `signal(S)`: Atomically increment S; if S ≤ 0, wake up a blocked process

**Implementation:**

```c
typedef struct {
    int value;
    struct process *list;  // List of blocked processes
} Semaphore;

void wait(Semaphore *S) {
    S->value--;
    if (S->value < 0) {
        // Block this process and add to S->list
    }
}

void signal(Semaphore *S) {
    S->value++;
    if (S->value <= 0) {
        // Wake up a process from S->list
    }
}
```

**Example 3.1 (Semaphore for Mutual Exclusion):** For mutual exclusion, initialize semaphore S = 1. Each process executes `wait(S)` before entering critical section and `signal(S)` upon exit, ensuring only one process accesses the critical section at any time.

**Example 3.2 (Semaphore for Synchronization):** Consider process P₁ producing data and process P₂ consuming data. Initialize S = 0. P₁ executes: produce data; signal(S). P₂ executes: wait(S); consume data. This ensures P₂ waits until P₁ produces data.

### 3.4. Monitors

A **monitor** is a high-level synchronization construct that encapsulates shared data and procedures operating on that data into a single module. Monitors guarantee mutual exclusion by allowing only one process to execute within the monitor at any time. **Condition variables** within monitors allow processes to wait for specific conditions to be satisfied.

```java
monitor SharedBuffer {
    int buffer[];
    int count = 0;
    condition notFull, notEmpty;

    procedure deposit(int value) {
        if (count == N) wait(notFull);
        buffer[count++] = value;
        signal(notEmpty);
    }

    procedure retrieve() {
        if (count == 0) wait(notEmpty);
        int value = buffer[--count];
        signal(notFull);
        return value;
    }
}
```

### 3.5. Barriers

A **barrier** is a synchronization primitive that blocks processes until all participating processes have reached the barrier. Barriers are essential in parallel algorithms where multiple threads must synchronize after completing their assigned tasks before proceeding to the next phase.

```c
// Simple barrier implementation using semaphores
typedef struct {
    int count;
    int total;
    Semaphore mutex;
    Semaphore barrier;
} Barrier;

void init(Barrier *b, int total) {
    b->count = 0;
    b->total = total;
    sem_init(&b->mutex, 1);
    sem_init(&b->barrier, 0);
}

void wait_barrier(Barrier *b) {
    sem_wait(&b->mutex);
    b->count++;
    sem_signal(&b->mutex);

    if (b->count == b->total)
        sem_signal(&b->barrier);  // Last process releases all

    sem_wait(&b->barrier);
    sem_signal(&b->barrier);  // Allow others to proceed
}
```

## 4. Classic Synchronization Problems

### 4.1. Producer-Consumer Problem

The producer-consumer problem involves bounded buffer management where producers insert items and consumers remove items. The solution requires synchronization for both mutual exclusion and coordination.

```c
Semaphore empty = N;  // Count of empty slots
Semaphore full = 0;   // Count of full slots
Semaphore mutex = 1;  // Mutual exclusion

// Producer
void producer() {
    while (TRUE) {
        item = produce();
        wait(empty);
        wait(mutex);
        add_to_buffer(item);
        signal(mutex);
        signal(full);
    }
}

// Consumer
void consumer() {
    while (TRUE) {
        wait(full);
        wait(mutex);
        item = remove_from_buffer();
        signal(mutex);
        signal(empty);
        consume(item);
    }
}
```

**Numerical Problem 4.1:** Given a buffer of size 5, if the producer produces 3 items before the consumer starts consuming, calculate the values of empty and full semaphores after each operation. (Answer: Initially empty = 5, full = 0. After producing 3: empty = 2, full = 3)

### 4.2. Readers-Writers Problem

The readers-writers problem manages access to a shared database where multiple readers can access concurrently but writers require exclusive access.

```c
Semaphore db = 1;      // Database access
int readers = 0;       // Number of active readers
Semaphore mutex = 1;   // Protects readers count

// Reader
void reader() {
    while (TRUE) {
        wait(mutex);
        readers++;
        if (readers == 1) wait(db);  // First reader locks database
        signal(mutex);

        read_database();

        wait(mutex);
        readers--;
        if (readers == 0) signal(db);  // Last reader releases
        signal(mutex);
    }
}

// Writer
void writer() {
    while (TRUE) {
        wait(db);
        write_database();
        signal(db);
    }
}
```

## 5. Deadlock and Livelock

### 5.1. Deadlock Characterization

A **deadlock** occurs when a set of processes are permanently blocked because each process is waiting for a resource held by another process in the set. Deadlock requires four necessary conditions (Coffman conditions):

1. **Mutual Exclusion:** At least one resource must be held in a non-sharable mode
2. **Hold and Wait:** A process must be holding at least one resource while waiting for others
3. **No Preemption:** Resources cannot be forcibly taken from processes
4. **Circular Wait:** A circular chain of processes exists where each process waits for a resource held by the next

### 5.2. Deadlock Prevention and Avoidance

**Deadlock Prevention** ensures at least one Coffman condition cannot hold:

- **Eliminate Hold and Wait:** Request all resources before execution or release held resources before requesting new ones
- **Allow Preemption:** Enable preemption of抢占资源
- **Impose Ordering:** Establish a total ordering of resource types and require processes to request resources in increasing order

**Deadlock Avoidance** (e.g., Banker's Algorithm) requires knowledge of maximum resource needs and maintains system state safe sequences.

---

## Assessment

### Multiple Choice Questions

**Question 1:** In Peterson's algorithm for two processes, what ensures mutual exclusion?

- (A) The flag array alone
- (B) The turn variable alone
- (C) Both flag and turn variables together
- (D) The test-and-set instruction
- **Answer: (C)** Both flag[i] and turn must satisfy conditions for a process to enter critical section

**Question 2:** In the producer-consumer problem with buffer size N, after producing N items without any consumption, the values of empty and full semaphores are:

- (A) empty = N, full = N
- (B) empty = 0, full = N
- (C) empty = N, full = 0
- (D) empty = 0, full = 0
- **Answer: (B)** Each production decrements empty and increments full

**Question 3:** Which of the following is NOT a Coffman condition for deadlock?

- (A) Mutual Exclusion
- (B) Hold and Wait
- (C) Priority Inversion
- (D) Circular Wait
- **Answer: (C)** Priority Inversion is a scheduling issue, not a deadlock condition

### Flashcards

| Term                 | Definition                                                                      |
| -------------------- | ------------------------------------------------------------------------------- |
| **Critical Section** | Code segment accessing shared resources requiring mutual exclusion              |
| **Race Condition**   | Unpredictable outcome due to non-deterministic order of concurrent operations   |
| **Bounded Waiting**  | Guarantee that a waiting process will enter critical section within finite time |
| **Semaphore**        | Integer variable with atomic wait and signal operations                         |
| **Monitor**          | High-level synchronization construct encapsulating data and procedures          |
