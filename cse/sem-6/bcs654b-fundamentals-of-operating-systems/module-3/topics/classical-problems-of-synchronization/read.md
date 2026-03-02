# Classical Synchronization Problems

## Introduction

In operating systems, synchronization is crucial for coordinating access to shared resources among multiple processes or threads. Classical synchronization problems are abstract scenarios that illustrate common challenges in concurrent programming. These problems serve as fundamental examples for understanding and implementing synchronization mechanisms like semaphores, monitors, and mutex locks.

## The Critical Section Problem Revisited

Before delving into classical problems, recall that the **critical section** is a code segment that accesses shared variables and must not be executed by more than one process at a time. Solutions to synchronization problems must satisfy three conditions:

1. **Mutual Exclusion**: Only one process can be in its critical section at a time
2. **Progress**: If no process is in its critical section, a process requesting entry must be allowed to enter
3. **Bounded Waiting**: There must be a limit on how many times other processes can enter their critical sections after a process has requested entry

## Semaphore Recap

Semaphores are integer variables used to control access to shared resources. They support two atomic operations:

- **wait()** (or P): Decrements the semaphore value; if value becomes negative, the process blocks
- **signal()** (or V): Increments the semaphore value; if processes are waiting, wakes one up

```
Binary semaphore: Value is 0 or 1 (like a mutex lock)
Counting semaphore: Value can range over an unrestricted domain
```

## The Producer-Consumer Problem

### Problem Description

Also known as the **bounded buffer problem**, this involves two types of processes:

- **Producers**: Create data items and add them to a buffer
- **Consumers**: Remove data items from the buffer and process them

The buffer has limited capacity, requiring synchronization to ensure:

1. Producers don't add data when the buffer is full
2. Consumers don't remove data when the buffer is empty
3. Only one process accesses the buffer at a time

### Solution Using Semaphores

We need three semaphores:

- **mutex**: Binary semaphore for mutual exclusion (initialized to 1)
- **full**: Counting semaphore counting number of full slots (initialized to 0)
- **empty**: Counting semaphore counting number of empty slots (initialized to buffer size)

**Producer Process:**

```
do {
 // Produce an item
 wait(empty); // Wait if buffer is full
 wait(mutex); // Enter critical section

 // Add item to buffer

 signal(mutex); // Exit critical section
 signal(full); // Increment count of full slots
} while (true);
```

**Consumer Process:**

```
do {
 wait(full); // Wait if buffer is empty
 wait(mutex); // Enter critical section

 // Remove item from buffer

 signal(mutex); // Exit critical section
 signal(empty); // Increment count of empty slots

 // Consume the item
} while (true);
```

### ASCII Diagram

```
+---------------+ +-------------------+ +---------------+
| | | | | |
| PRODUCER | -> | BUFFER (size N) | -> | CONSUMER |
| | | | | |
+---------------+ +-------------------+ +---------------+
 | | | |
 +---------------------+ +---------------------+
```

## The Readers-Writers Problem

### Problem Description

This problem involves processes that access a shared data area:

- **Readers**: Only read the data; can access concurrently
- **Writers**: Both read and write; require exclusive access

Constraints:

1. Multiple readers can read simultaneously
2. Only one writer can write at a time
3. No reader can read while a writer is writing

Two variations exist:

- **First readers-writers problem**: No reader should wait unless a writer is writing (readers have priority)
- **Second readers-writers problem**: Once a writer is ready, it should perform write ASAP (writers have priority)

### Solution Using Semaphores (First Variation)

We need:

- **mutex**: Binary semaphore for mutual exclusion of read_count (initialized to 1)
- **wrt**: Binary semaphore for mutual exclusion of writing (initialized to 1)
- **read_count**: Integer tracking number of current readers

**Writer Process:**

```
do {
 wait(wrt); // Request exclusive access

 // Writing is performed

 signal(wrt); // Release exclusive access
} while (true);
```

**Reader Process:**

```
do {
 wait(mutex); // Enter critical section for read_count
 read_count++;
 if (read_count == 1) {
 wait(wrt); // First reader blocks writers
 }
 signal(mutex);

 // Reading is performed

 wait(mutex);
 read_count--;
 if (read_count == 0) {
 signal(wrt); // Last reader releases writers
 }
 signal(mutex);
} while (true);
```

## The Dining Philosophers Problem

### Problem Description

Formulated by Edsger Dijkstra, this problem illustrates deadlock and synchronization issues. Five philosophers sit around a circular table with:

- A bowl of rice in the center
- One chopstick between each pair of philosophers

Each philosopher alternates between thinking and eating. To eat, a philosopher needs both adjacent chopsticks.

### Solution Using Semaphores

We need an array of semaphores (one per chopstick), all initialized to 1.

**Philosopher Process (Naive Approach):**

```
do {
 wait(chopstick[i]); // Pick up left chopstick
 wait(chopstick[(i+1)%5]); // Pick up right chopstick

 // Eat

 signal(chopstick[i]); // Put down left chopstick
 signal(chopstick[(i+1)%5]); // Put down right chopstick

 // Think
} while (true);
```

This naive solution can lead to **deadlock** if all philosophers pick up their left chopstick simultaneously.

### Deadlock Avoidance Solutions

**Solution 1: Allow at most 4 philosophers to sit simultaneously**

```
semaphore limit = 4; // Allow only 4 philosophers

do {
 wait(limit);
 wait(chopstick[i]);
 wait(chopstick[(i+1)%5]);

 // Eat

 signal(chopstick[i]);
 signal(chopstick[(i+1)%5]);
 signal(limit);
} while (true);
```

**Solution 2: Asymmetric picking (odd/even rule)**
Odd-numbered philosophers pick left then right; even-numbered pick right then left.

**Solution 3: Use a mutex to make picking both chopsticks atomic**

```
semaphore mutex = 1;

do {
 wait(mutex);
 wait(chopstick[i]);
 wait(chopstick[(i+1)%5]);
 signal(mutex);

 // Eat

 signal(chopstick[i]);
 signal(chopstick[(i+1)%5]);
} while (true);
```

### ASCII Diagram

```
 P0
 / \
 C5 C1
 / \
 P4 P1
 \ /
 C4 C2
 \ /
 P2
```

## The Sleeping Barber Problem

### Problem Description

A barber shop has:

- One barber
- One barber chair
- N waiting chairs

Rules:

1. If no customers, barber sleeps
2. When customer arrives:

- If barber is asleep, wake him
- If barber is busy but chairs available, sit and wait
- If no chairs available, leave

### Solution Using Semaphores

We need:

- **customers**: Counting semaphore for customers waiting (initialized to 0)
- **barber**: Semaphore for barber availability (initialized to 0)
- **mutex**: Binary semaphore for mutual exclusion (initialized to 1)
- **waiting**: Integer count of waiting customers

**Barber Process:**

```
do {
 wait(customers); // Sleep if no customers
 wait(mutex);
 waiting--; // Decrement count of waiting customers
 signal(barber); // Barber is ready to cut hair
 signal(mutex);

 // Cut hair
} while (true);
```

**Customer Process:**

```
wait(mutex);
if (waiting < CHAIRS) {
 waiting++; // Increment count of waiting customers
 signal(customers); // Wake barber if sleeping
 signal(mutex);
 wait(barber); // Wait for barber to be available

 // Get haircut
} else {
 signal(mutex); // Leave if no chairs available
}
```

## Comparison of Classical Problems

| Problem             | Key Challenge                          | Synchronization Requirements                       |
| ------------------- | -------------------------------------- | -------------------------------------------------- |
| Producer-Consumer   | Buffer management                      | Mutual exclusion, empty/full condition tracking    |
| Readers-Writers     | Data access patterns                   | Multiple readers allowed, writers need exclusivity |
| Dining Philosophers | Deadlock avoidance                     | Resource allocation without circular wait          |
| Sleeping Barber     | Resource scheduling with waiting queue | Customer notification, queue management            |

## Modern Synchronization Constructs

While semaphores are fundamental, modern programming often uses higher-level constructs:

**Monitors**: Abstract data types that encapsulate shared data and procedures, with built-in mutual exclusion.

**Condition Variables**: Used with monitors for signaling and waiting, providing more structured synchronization.

## Exam Tips

1. **Understand the core constraints** of each problem before attempting solutions
2. **Always initialize semaphores correctly** - this is a common mistake
3. **Watch for deadlock possibilities** - especially in Dining Philosophers
4. **Remember semaphore operations are atomic** - no interrupts during wait/signal
5. **For readers-writers**, be clear about which variation you're solving
6. **Practice implementing solutions** with pseudocode to build intuition
7. **Consider edge cases** - what happens when buffer is full/empty, or all philosophers try to eat simultaneously
