# Synchronization Hardware


## Table of Contents

- [Synchronization Hardware](#synchronization-hardware)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [The Need for Hardware Synchronization](#the-need-for-hardware-synchronization)
  - [Test-and-Set Instruction](#test-and-set-instruction)
  - [Swap Instruction](#swap-instruction)
  - [Compare-and-Swap (CAS)](#compare-and-swap-cas)
  - [Fetch-and-Add](#fetch-and-add)
  - [Load-Linked and Store-Conditional](#load-linked-and-store-conditional)
  - [Memory Barriers and Ordering](#memory-barriers-and-ordering)
- [Examples](#examples)
  - [Example 1: Implementing a Spin Lock with Test-and-Set](#example-1-implementing-a-spin-lock-with-test-and-set)
  - [Example 2: Lock-Free Counter with Compare-and-Swap](#example-2-lock-free-counter-with-compare-and-swap)
  - [Example 3: Ticket Lock with Fetch-and-Add](#example-3-ticket-lock-with-fetch-and-add)
- [Exam Tips](#exam-tips)

## Introduction

Process synchronization in operating systems becomes essential when multiple processes compete for shared resources. While software-based solutions like Peterson's algorithm and semaphores provide elegant theoretical approaches to the critical section problem, they rely on specific assumptions about the underlying hardware, particularly memory access ordering. In practice, modern multiprocessor systems present significant challenges: memory consistency models vary across architectures, compiler optimizations can reorder instructions, and processor caches introduce additional complexity. These factors make pure software solutions unreliable without hardware support.

Synchronization hardware refers to special machine instructions provided by the CPU architecture that perform atomic operations—operations that execute without interruption as a single, indivisible unit. These hardware primitives form the foundation upon which operating systems build higher-level synchronization mechanisms like mutex locks, semaphores, and monitors. Understanding these hardware instructions is crucial because they represent the lowest level of the synchronization hierarchy, and all software synchronization constructs ultimately depend on their correctness and atomicity.

The evolution of synchronization hardware reflects the evolution of multiprocessor computing itself. Early uniprocessor systems relied on disabling interrupts to achieve atomicity, but this approach fails in multiprocessor environments where other processors continue executing concurrently. Modern processors provide increasingly sophisticated atomic instructions—compare-and-swap (CAS), fetch-and-add, load-linked/store-conditional—each designed for specific synchronization patterns. This module examines these hardware primitives, their implementations, and how operating systems utilize them to construct reliable synchronization mechanisms.

## Key Concepts

### The Need for Hardware Synchronization

The critical section problem requires that only one process can access shared resources at any given time. Software solutions achieve this through carefully constructed protocols, but these protocols assume atomic memory operations. In reality, even a simple operation like "read-modify-write" involves multiple memory accesses that can be interleaved with accesses from other processors. For instance, when incrementing a shared counter, a processor must read the current value, increment it in a register, and write it back—another processor might modify the value between the read and write operations, causing lost updates.

Hardware synchronization instructions solve this problem by bundling multiple memory operations into a single atomic instruction that the processor guarantees will execute without interruption. The processor implements this guarantee through various mechanisms: memory buses can be locked during the instruction execution, caches can be held exclusively, or special hardware paths can ensure serialization. The key characteristic is that no other processor can observe or interfere with the intermediate states—the instruction appears to complete instantaneously from all other processors' perspectives.

### Test-and-Set Instruction

The Test-and-Set instruction represents one of the fundamental synchronization primitives. It operates on a binary variable (typically a lock) and performs two operations atomically: it reads the current value and sets the variable to a new value (conventionally 1 or "locked"). The instruction returns the old value, allowing the calling process to determine whether the lock was available.

The formal specification is: boolean TestAndSet(boolean *lock). It atomically executes: boolean old = *lock; *lock = true; return old;. When a process executes Test-and-Set on a lock variable, it receives the previous value. If the previous value was false (0, indicating unlocked), the process acquired the lock and can proceed into the critical section. If the previous value was true (1, indicating locked), the process must wait.

Implementing a mutual exclusion lock using Test-and-Set requires a shared boolean variable initialized to false. A process entering its critical section executes Test-and-Set in a loop until it returns false, indicating successful lock acquisition. This approach, called spin waiting or busy waiting, keeps the processor occupied checking the lock repeatedly. While seemingly wasteful, spin locks prove efficient when the critical section executes quickly and the lock-holding period is short—the overhead of context switching would exceed the cost of busy waiting.

### Swap Instruction

The Swap instruction exchanges the values of two variables atomically. For synchronization purposes, one variable typically resides in each process's address space (or is private to the process), while the other represents a shared lock. The formal operation: Swap(boolean *a, boolean *b) { temp = *a; *a = *b; *b = temp; }.

To implement mutual exclusion using Swap, processes share a lock variable initialized to false. Each process maintains a private variable (localKey) also initialized to false. The process repeatedly executes: Swap(&localKey, &sharedLock) until localKey becomes true. When Swap exchanges the shared lock (false) with the process's local variable (false), the process receives false and continues waiting. When the lock becomes available and another process performs Swap, it exchanges false with true, receiving false while setting sharedLock to true—the process that received true in its local variable now holds the lock.

Both Test-and-Set and Swap implementations suffer from busy waiting, consuming CPU cycles unnecessarily. However, they provide valuable building blocks. Modern operating systems often combine these primitives with operating system scheduling—after a certain number of failed attempts, a process may voluntarily yield the processor or sleep, reducing wasted CPU time.

### Compare-and-Swap (CAS)

Compare-and-Swap represents a more flexible and powerful synchronization primitive found in most modern processors, including x86 (as CMPXCHG), ARM (as LDREX/STREX), and IBM Power architectures. CAS operates on three operands: a memory location, an expected value, and a new value. The instruction atomically checks whether the memory location contains the expected value; if so, it replaces it with the new value and returns success. If the values differ, the operation fails without modifying the memory location.

The formal specification: int CompareAndSwap(int *ptr, int expected, int newValue). It atomically executes: int actual = *ptr; if (actual == expected) *ptr = newValue; return actual;. The return value indicates whether the swap occurred, allowing the caller to retry with updated expectations if another process modified the location.

CAS enables sophisticated synchronization patterns beyond simple mutual exclusion. It supports lock-free data structures where updates proceed by reading the current state, computing the new state, and attempting to replace the old state with the new one using CAS. If another process modified the state in the meantime, CAS fails, and the operation retries with the updated state. This approach underlies most modern concurrent data structures, from lock-free queues to non-blocking linked lists.

### Fetch-and-Add

Fetch-and-Add atomically increments a memory location and returns its previous value. The operation: int FetchAndAdd(int *ptr, int increment). It executes: int old = *ptr; *ptr = old + increment; return old;. This primitive proves particularly useful for implementing ticket locks and counters in concurrent systems.

Ticket locks represent an improvement over basic spin locks. Instead of a single boolean lock, they maintain two counters: a next ticket number (representing which process should acquire the lock) and a turn number (representing whose turn it is). When a process wants the lock, it atomically fetches and increments the next ticket counter, receiving its ticket number. It then spins, waiting until the turn counter matches its ticket number. This ensures fair, first-come-first-served ordering regardless of how quickly processes attempt to acquire the lock—unlike basic Test-and-Set where a faster processor might repeatedly acquire the lock, causing starvation.

Fetch-and-Add also serves parallel counting applications where multiple processes must increment a shared counter. By returning the previous value, each increment operation can determine which "slot" or identifier belongs to it, useful in parallel prefix computation and distributed algorithms.

### Load-Linked and Store-Conditional

Modern ARM and PowerPC processors implement a different synchronization model through paired instructions: Load-Linked (LL) and Store-Conditional (SC). These instructions work together to provide flexible atomic operations. Load-Linked loads a value from memory and marks the memory address for tracking. Store-Conditional attempts to store a new value to that address but succeeds only if no other process has modified the location since the corresponding Load-Linked.

The key advantage of LL/SC over CAS is its ability to implement more complex atomic sequences. A process can perform multiple calculations between LL and SC, only validating the final result. If another process modified the location, SC fails automatically, and the operation retries. This enables lock-free algorithms that would be impossible with simple CAS, as the operation can involve arbitrary computation between loading and storing.

For example, incrementing a counter using LL/SC: do { old = LL(counter); new = old + 1; } while (!SC(counter, new));. This pattern—load, compute, attempt store—retrying on failure—represents the standard lock-free programming idiom.

### Memory Barriers and Ordering

Hardware synchronization instructions typically include implicit or explicit memory ordering guarantees. In weakly ordered memory models (like ARM and PowerPC), processors may reorder memory accesses for performance, and writes from other processors may not be immediately visible. Synchronization instructions serve as memory barriers that enforce ordering constraints.

A full memory barrier ensures that all memory accesses before the barrier complete before any memory accesses after the barrier begin. Store barriers ensure all preceding writes become visible to other processors before subsequent writes proceed. Load barriers ensure all subsequent loads see writes that occurred before the barrier. Understanding these ordering requirements is essential for correct synchronization code—using atomic primitives without appropriate barriers can lead to subtle, hard-to-debug concurrency bugs.

## Examples

### Example 1: Implementing a Spin Lock with Test-and-Set

Consider a multiprocessor system where multiple processes need exclusive access to a shared data structure, such as a print queue. Using Test-and-Set, we implement a spin lock:

```
bool lock = false;

void acquire_lock() {
    while (TestAndSet(&lock)) {
        // Lock is held; busy wait
    }
    // Lock acquired; proceed to critical section
}

void release_lock() {
    lock = false;
}
```

Step-by-step execution: Process P1 calls acquire_lock(). TestAndSet(&lock) reads lock (false), sets lock to true, and returns false. The while loop exits because the return value is false. P1 enters the critical section. Meanwhile, Process P2 calls acquire_lock(). TestAndSet(&lock) reads lock (true), keeps lock as true, and returns true. The while loop continues because true is non-zero. P2 busy-waits, repeatedly executing TestAndSet. When P1 finishes, it calls release_lock() setting lock to false. P2's next TestAndSet now reads lock (false), sets it to true, and returns false. P2 acquires the lock.

This implementation ensures mutual exclusion—only one process can hold the lock at any time—and progress is guaranteed because the lock eventually becomes available when the holder releases it.

### Example 2: Lock-Free Counter with Compare-and-Swap

Suppose multiple threads must increment a shared counter representing available seats in a theater booking system. Using CAS, we implement an increment operation that never loses updates:

```
int increment_seats(int *seats, int num_seats) {
    int current, new_value;
    do {
        current = *seats;
        new_value = current + num_seats;
        // If seats changed between read and write, CAS fails
    } while (CompareAndSwap(seats, current, new_value) != current);
    return new_value;
}
```

Execution trace: Initial seats = 100. Thread T1 calls increment_seats(seats, 5). It reads current = 100, computes new_value = 105. Before T1 executes CAS, Thread T2 also reads current = 100 and computes new_value = 105. T1 executes CAS: seats equals 100 (the expected value), so CAS sets seats to 105 and returns 100. Since return equals current (100), the loop exits. T2 then executes CAS: seats now equals 105, not the expected 100. CAS returns 105 (the actual value) without modifying seats. The return (105) does not equal current (100), so the loop repeats. T2 reads current = 105, computes new_value = 110, and attempts CAS again—this time it succeeds. The final count correctly reflects both increments: 110.

This demonstrates how CAS prevents lost updates without requiring locks, enabling high-performance concurrent systems.

### Example 3: Ticket Lock with Fetch-and-Add

A server handling multiple client requests uses a ticket lock to ensure fair servicing:

```
int next_ticket = 0;
int turn = 0;

void acquire_fair_lock() {
    int my_ticket = FetchAndAdd(&next_ticket, 1);
    while (turn != my_ticket) {
        // Not my turn; yield processor briefly
        yield();
    }
}

void release_fair_lock() {
    FetchAndAdd(&turn, 1);
}
```

Scenario: Three clients A, B, and C arrive simultaneously. Client A calls acquire_fair_lock() first. FetchAndAdd returns 0 (my_ticket = 0) and increments next_ticket to 1. The while condition (turn(0) != my_ticket(0)) is false, so A enters immediately. Client B arrives, gets my_ticket = 1 from FetchAndAdd, next_ticket becomes 2. B waits because turn(0) != 1. Client C gets my_ticket = 2, next_ticket becomes 3. C also waits. When A finishes, release_fair_lock() calls FetchAndAdd(&turn, 1), incrementing turn from 0 to 1. Now B's condition (turn(1) == my_ticket(1)) becomes true, and B enters. This ensures strict FIFO ordering regardless of arrival timing or processor speed.

## Exam Tips

Synchronization hardware questions in DU semester exams typically require understanding both the mechanism and application of these primitives.

UNDERSTAND THE ATOMICITY GUARANTEE: The core concept is that hardware instructions execute without interruption. When explaining Test-and-Set or CAS, emphasize that the entire operation appears instantaneous to other processors—this atomicity is what enables correct synchronization.

KNOW THE DIFFERENCE BETWEEN SPIN LOCKS AND BLOCKING LOCKS: Hardware primitives like Test-and-Set implement spin locks where processes busy-wait. Distinguish this from blocking locks where processes sleep. Explain when each approach is appropriate—spin locks for short critical sections, blocking locks for longer waits.

COMPARE PRIMITIVES EFFECTIVELY: Exam questions often ask to compare Test-and-Set with Swap, or CAS with Fetch-and-Add. Prepare a comparison table covering operation type, return value, use cases, and advantages. CAS is more flexible than Test-and-Set; Fetch-and-Add supports fair locking.

ANALYZE ADVANTAGES AND DISADVANTAGES: Hardware synchronization is simple, efficient for short waits, and universally available. However, busy-wasting CPU cycles, potential starvation in basic implementations, and complexity in building complete solutions are limitations. OS-level support can address some disadvantages.

MEMORY ORDERING MATTERS: In exam answers involving multiprocessors, mention that atomic instructions implicitly or explicitly enforce memory ordering. Weakly ordered architectures may require explicit barriers for correct operation.

CONNECT TO HIGHER-LEVEL CONSTRUCTS: Explain how operating systems build semaphores and monitors using these hardware primitives. Understanding this hierarchy demonstrates comprehensive knowledge.

WORK THROUGH EXAMPLE TRACES: Practice tracing execution sequences with multiple processes. Understand exactly how CAS handles concurrent updates and why retry loops are necessary.