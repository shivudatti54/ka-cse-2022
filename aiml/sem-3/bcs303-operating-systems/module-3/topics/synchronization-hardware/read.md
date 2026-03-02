# Synchronization Hardware


## Table of Contents

- [Synchronization Hardware](#synchronization-hardware)
- [Introduction](#introduction)
- [Disabling Interrupts](#disabling-interrupts)
- [The test_and_set Instruction](#the-testandset-instruction)
  - [Definition](#definition)
  - [Mutual Exclusion with test_and_set](#mutual-exclusion-with-testandset)
  - [Properties](#properties)
  - [Bounded-Waiting test_and_set](#bounded-waiting-testandset)
- [The compare_and_swap Instruction](#the-compareandswap-instruction)
  - [Definition](#definition)
  - [Mutual Exclusion with compare_and_swap](#mutual-exclusion-with-compareandswap)
- [Comparison of Hardware Instructions](#comparison-of-hardware-instructions)
- [Spinlocks](#spinlocks)
- [Summary](#summary)
- [Exam Tips](#exam-tips)

## Introduction

Software-based solutions to the critical section problem (like Peterson's solution) are limited — they work only for two processes and are vulnerable to instruction reordering on modern processors. To provide robust synchronization, modern computer architectures offer special **hardware instructions** that execute **atomically** (as a single, uninterruptible unit).

These hardware instructions form the building blocks on which OS synchronization primitives (spinlocks, mutexes, semaphores) are implemented. This topic covers the key hardware mechanisms: disabling interrupts, the test-and-set instruction, and the compare-and-swap instruction.

## Disabling Interrupts

The simplest hardware approach to mutual exclusion on a **single-processor** system is to disable interrupts while a process is in its critical section.

```
Process Pi:
 disable_interrupts();
 // === CRITICAL SECTION ===
 enable_interrupts();
 // === REMAINDER SECTION ===
```

**How it works:** On a single-processor system, processes alternate via interrupts (timer interrupt causes context switch). If interrupts are disabled, no context switch can occur, so no other process can interfere.

| Advantage                        | Disadvantage                                                              |
| :------------------------------- | :------------------------------------------------------------------------ |
| Simple to implement              | Does NOT work on multiprocessor systems (other CPUs still execute)        |
| Works well for the kernel itself | Dangerous if a user process disables interrupts and never re-enables them |
| No busy waiting                  | Reduces system responsiveness while interrupts are disabled               |

**Conclusion:** Disabling interrupts is used internally by the OS kernel for short critical sections, but it is not a general solution.

## The test_and_set Instruction

The **test_and_set** (also called **test-and-set lock**, or TAS) instruction is a hardware-provided atomic instruction. It reads a value, sets it to TRUE, and returns the old value — all in one atomic (uninterruptible) step.

### Definition

```c
// This entire function executes ATOMICALLY (hardware guarantee)
boolean test_and_set(boolean *target) {
 boolean rv = *target; // Save the old value
 *target = TRUE; // Set the value to TRUE
 return rv; // Return the old value
}
```

**Key property:** Even if two processors call `test_and_set` on the same variable simultaneously, the hardware ensures they execute one at a time. One will see `FALSE` (and enter), the other will see `TRUE` (and wait).

### Mutual Exclusion with test_and_set

```c
// Shared variable
boolean lock = FALSE;

// Process Pi
do {
 while (test_and_set(&lock) == TRUE)
 ; // Busy wait (spin) — lock was already held

 // === CRITICAL SECTION ===

 lock = FALSE; // Release the lock

 // === REMAINDER SECTION ===
} while (TRUE);
```

**How it works:**

```
Initially: lock = FALSE

P1 calls test_and_set(&lock):
 → Returns FALSE (old value), sets lock = TRUE
 → P1 exits while loop, enters critical section

P2 calls test_and_set(&lock):
 → Returns TRUE (lock is held), sets lock = TRUE (no change)
 → P2 stays in while loop, spinning

P1 finishes: lock = FALSE

P2 calls test_and_set(&lock):
 → Returns FALSE, sets lock = TRUE
 → P2 exits while loop, enters critical section
```

### Properties

| Property         | Satisfied? | Explanation                                                                 |
| :--------------- | :--------- | :-------------------------------------------------------------------------- |
| Mutual exclusion | Yes        | Only the process that finds lock=FALSE can enter                            |
| Progress         | Yes        | If no one is in CS, lock is FALSE, so next requester enters                 |
| Bounded waiting  | **No**     | A process could spin forever if other processes keep getting the lock first |

### Bounded-Waiting test_and_set

To achieve bounded waiting, we use an additional array `waiting[]`:

```c
// Shared variables
boolean lock = FALSE;
boolean waiting[n]; // All initialized to FALSE

// Process Pi
do {
 waiting[i] = TRUE;
 boolean key = TRUE;

 while (waiting[i] == TRUE && key == TRUE)
 key = test_and_set(&lock);

 waiting[i] = FALSE;

 // === CRITICAL SECTION ===

 // Find next waiting process (circular scan)
 int j = (i + 1) % n;
 while (j != i && waiting[j] == FALSE)
 j = (j + 1) % n;

 if (j == i)
 lock = FALSE; // No one waiting — release lock
 else
 waiting[j] = FALSE; // Pass entry to process j

 // === REMAINDER SECTION ===
} while (TRUE);
```

This ensures bounded waiting because the exiting process scans circularly to find the next waiting process, guaranteeing each process waits at most n-1 turns.

## The compare_and_swap Instruction

The **compare-and-swap** (CAS) instruction is another atomic hardware instruction, used widely in modern processors (x86: `CMPXCHG`, ARM: `LDREX/STREX`).

### Definition

```c
// This entire function executes ATOMICALLY
int compare_and_swap(int *value, int expected, int new_value) {
 int temp = *value; // Save the current value
 if (*value == expected) // If current value matches expected
 *value = new_value; // Set to new value
 return temp; // Return the old value
}
```

### Mutual Exclusion with compare_and_swap

```c
// Shared variable
int lock = 0;

// Process Pi
do {
 while (compare_and_swap(&lock, 0, 1) != 0)
 ; // Busy wait — lock was not 0 (already held)

 // === CRITICAL SECTION ===

 lock = 0; // Release the lock

 // === REMAINDER SECTION ===
} while (TRUE);
```

**How it works:** A process can enter the critical section only when CAS finds `lock == 0` (expected), atomically sets it to `1`, and returns `0`. If lock is already `1`, CAS returns `1` and the process spins.

## Comparison of Hardware Instructions

| Aspect                   | test_and_set          | compare_and_swap                              |
| :----------------------- | :-------------------- | :-------------------------------------------- |
| **Parameters**           | 1 (target pointer)    | 3 (pointer, expected, new value)              |
| **Operation**            | Read old, set to TRUE | Read old, conditionally set to new            |
| **Flexibility**          | Less flexible         | More flexible (conditional update)            |
| **Modern usage**         | Older architectures   | Widely used (x86 CMPXCHG, Java AtomicInteger) |
| **Lock-free algorithms** | Limited               | Enables lock-free data structures             |

## Spinlocks

A **spinlock** is a lock implemented using busy waiting (spinning) with hardware atomic instructions. The term "spin" comes from the while loop that continuously tests the lock.

```
Spinlock behavior:
 acquire(lock): while (test_and_set(&lock)); // spin until acquired
 release(lock): lock = FALSE;
```

| Advantage                                                   | Disadvantage                                     |
| :---------------------------------------------------------- | :----------------------------------------------- |
| No context switch needed (fast for short critical sections) | Wastes CPU cycles while spinning                 |
| Useful on multiprocessor systems where wait times are short | On single-processor, spinning is always wasteful |
| Simple to implement                                         | Not suitable for long critical sections          |

**Key insight:** Spinlocks are effective on multiprocessor systems when the expected wait time is short (less than the cost of two context switches). On a single-processor system, spinlocks waste the entire time quantum.

## Summary

| Mechanism           | Type                 | Atomic? | Busy Wait?     | Works on Multiprocessor? |
| :------------------ | :------------------- | :------ | :------------- | :----------------------- |
| Disable interrupts  | Hardware             | N/A     | No             | No (single CPU only)     |
| test_and_set        | Hardware instruction | Yes     | Yes (spinlock) | Yes                      |
| compare_and_swap    | Hardware instruction | Yes     | Yes (spinlock) | Yes                      |
| Bounded-waiting TAS | Software + hardware  | Yes     | Yes            | Yes                      |

## Exam Tips

1. **Write the test_and_set definition** — This is very commonly asked. Memorize the 3-line atomic function: save old value, set to TRUE, return old value.
2. **Write the compare_and_swap definition** — Similarly common. Know the 3 parameters and the conditional update.
3. **Show mutual exclusion using TAS** — Be able to write the complete while-loop spinlock and explain how it works step by step.
4. **Bounded waiting** — Know why basic test_and_set does NOT satisfy bounded waiting, and how the `waiting[]` array version fixes this.
5. **Why not disable interrupts?** — Two key reasons: doesn't work on multiprocessor systems, and dangerous to give user processes this power.
6. **Spinlock trade-off** — Know when spinlocks are good (multiprocessor, short critical sections) vs bad (single-processor, long critical sections).
