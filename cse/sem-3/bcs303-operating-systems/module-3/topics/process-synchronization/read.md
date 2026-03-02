# Process Synchronization: Introduction

## 1. Background: Why Synchronization is Needed

In a modern operating system, multiple processes (or threads) execute **concurrently**. Concurrency arises from:

- **Multiprogramming**: Multiple processes in memory, CPU switches between them
- **Multiprocessing**: Multiple CPUs executing processes truly in parallel
- **Time-sharing**: Rapid context switching giving the illusion of parallelism

Concurrent processes can be classified as:

| Type            | Description                                      | Synchronization Needed? |
| --------------- | ------------------------------------------------ | ----------------------- |
| **Independent** | Do not share data with other processes           | No                      |
| **Cooperating** | Share data (memory, files, messages) with others | Yes                     |

**Cooperating processes** need synchronization because concurrent access to shared data can lead to **data inconsistency**. The fundamental challenge is ensuring that cooperating processes operate on shared data in an orderly fashion so that the final result is correct and predictable.

This topic corresponds to **Section 6.1** of Silberschatz (Operating System Concepts).

## 2. The Producer-Consumer Problem: Motivation

The **producer-consumer problem** is a classic example that motivates the need for synchronization. It models many real-world scenarios: a compiler (producer) generating assembly code consumed by an assembler (consumer), a web server (producer) generating log entries consumed by a log analyzer (consumer), etc.

### 2.1 Bounded Buffer Setup

```c
#define BUFFER_SIZE 10

int buffer[BUFFER_SIZE];
int in = 0; // next free position (producer writes here)
int out = 0; // first full position (consumer reads here)
int count = 0; // number of items in buffer
```

### 2.2 Producer Code

```c
// Producer process
while (true) {
 /* produce an item in next_produced */

 while (count == BUFFER_SIZE)
 ; // do nothing -- buffer is full

 buffer[in] = next_produced;
 in = (in + 1) % BUFFER_SIZE;
 count++;
}
```

### 2.3 Consumer Code

```c
// Consumer process
while (true) {
 while (count == 0)
 ; // do nothing -- buffer is empty

 next_consumed = buffer[out];
 out = (out + 1) % BUFFER_SIZE;
 count--;

 /* consume the item in next_consumed */
}
```

### 2.4 The Problem

Although the producer and consumer code looks correct individually, when they execute **concurrently**, the shared variable `count` can become inconsistent. The statement `count++` and `count--` are not **atomic** -- they each involve multiple machine-level instructions, and interleaving can cause errors.

## 3. Race Condition

A **race condition** occurs when the outcome of execution depends on the particular **order of interleaving** of instructions from concurrent processes that access shared data.

### 3.1 Why count++ and count-- Are Not Atomic

The high-level statement `count++` is implemented in machine language as:

```
register1 = count // Load count into register
register1 = register1 + 1 // Increment register
count = register1 // Store back to memory
```

Similarly, `count--` is implemented as:

```
register2 = count // Load count into register
register2 = register2 - 1 // Decrement register
count = register2 // Store back to memory
```

### 3.2 The Classic Race Condition Example

**Initial value**: `count = 5`

Consider the following interleaving of instructions:

```
Step | Process | Instruction | register1 | register2 | count
-----|-----------|-------------------------------|-----------|-----------|------
T0 | Producer | register1 = count | 5 | - | 5
T1 | Producer | register1 = register1 + 1 | 6 | - | 5
T2 | Consumer | register2 = count | 6 | 5 | 5
T3 | Consumer | register2 = register2 - 1 | 6 | 4 | 5
T4 | Producer | count = register1 | 6 | 4 | 6
T5 | Consumer | count = register2 | 6 | 4 | 4
```

**Expected result**: `count = 5` (one increment and one decrement should cancel out)
**Actual result**: `count = 4` (INCORRECT!)

If the order were reversed (consumer stores first, then producer):

```
Step | Process | Instruction | register1 | register2 | count
-----|-----------|-------------------------------|-----------|-----------|------
T0 | Producer | register1 = count | 5 | - | 5
T1 | Producer | register1 = register1 + 1 | 6 | - | 5
T2 | Consumer | register2 = count | 6 | 5 | 5
T3 | Consumer | register2 = register2 - 1 | 6 | 4 | 5
T4 | Consumer | count = register2 | 6 | 4 | 4
T5 | Producer | count = register1 | 6 | 4 | 6
```

**Actual result**: `count = 6` (ALSO INCORRECT!)

### 3.3 Key Insight

The problem occurs because both processes manipulate `count` concurrently without any coordination. The **correct result depends on which process finishes last**, making the outcome unpredictable. This is the essence of a race condition.

```
 Race Condition Visualization:

 Producer Consumer
 -------- --------
 register1 = count ----+
 register1 = register1 + 1| +---- register2 = count
 count = register1 ----+ | register2 = register2 - 1
 \ | count = register2
 \ |
 INTERLEAVING
 of these steps
 causes incorrect
 results!
```

## 4. The Need for Atomic Operations

An operation is **atomic** if it completes entirely without interruption, or does not execute at all. There is no intermediate state visible to other processes.

### 4.1 Why Atomicity Matters

| Without Atomicity                 | With Atomicity                             |
| --------------------------------- | ------------------------------------------ |
| Instructions can be interleaved   | Operation executes as one indivisible unit |
| Intermediate states are visible   | Only final state is visible                |
| Results depend on execution order | Results are always correct                 |
| Race conditions are possible      | Race conditions are prevented              |

### 4.2 What Needs Protection

The section of code where shared variables are accessed and modified is called the **critical section**. To prevent race conditions, we need mechanisms that ensure:

- Only **one process** can execute its critical section at a time (**mutual exclusion**)
- The mechanism does not cause indefinite delays (**progress** and **bounded waiting**)

## 5. The Critical Section Problem: Formal Definition

Consider a system of n processes {P0, P1, ..., Pn-1}. Each process has a segment of code called its **critical section** where it accesses shared resources.

### 5.1 Structure of a Process

```c
do {
 +---------------------------+
 | ENTRY SECTION | // Request permission to enter
 +---------------------------+

 +---------------------------+
 | CRITICAL SECTION | // Access shared resource
 +---------------------------+

 +---------------------------+
 | EXIT SECTION | // Announce leaving
 +---------------------------+

 +---------------------------+
 | REMAINDER SECTION | // Non-critical code
 +---------------------------+
} while (true);
```

### 5.2 Three Requirements for a Solution

Any valid solution to the critical section problem must satisfy all three conditions:

```
+---------------------+------------------------------------------------+
| Requirement | Description |
+---------------------+------------------------------------------------+
| 1. Mutual Exclusion | If Pi is in its critical section, no other |
| | process Pj can be in its critical section. |
+---------------------+------------------------------------------------+
| 2. Progress | If no process is in its critical section and |
| | some processes wish to enter, then only those |
| | processes NOT in their remainder section can |
| | participate in deciding who enters next. This |
| | selection cannot be postponed indefinitely. |
+---------------------+------------------------------------------------+
| 3. Bounded Waiting | There exists a bound on the number of times |
| | other processes can enter their critical section |
| | after a process has made a request and before |
| | that request is granted. |
+---------------------+------------------------------------------------+
```

## 6. Overview of Synchronization Mechanisms

The operating system and hardware provide several approaches to solve the critical section problem:

### 6.1 Software-Based Solutions

| Solution            | Key Idea                                   | Limitation                                              |
| ------------------- | ------------------------------------------ | ------------------------------------------------------- |
| Peterson's Solution | Turn variable + flag array for 2 processes | Only works for 2 processes; assumes atomic loads/stores |
| Bakery Algorithm    | Ticket-based ordering for n processes      | Complex; busy waiting                                   |

### 6.2 Hardware-Based Solutions

| Solution             | Key Idea                                         | Limitation                    |
| -------------------- | ------------------------------------------------ | ----------------------------- |
| Disabling Interrupts | Prevent context switches during critical section | Only for uniprocessors; risky |
| test_and_set()       | Atomic instruction to test and modify a variable | Busy waiting (spinlock)       |
| compare_and_swap()   | Atomic compare-and-swap instruction              | Busy waiting (spinlock)       |

### 6.3 OS-Provided Synchronization Tools

| Solution    | Key Idea                                        | Advantage                   |
| ----------- | ----------------------------------------------- | --------------------------- |
| Mutex Locks | Simple binary lock (acquire/release)            | Easy to use                 |
| Semaphores  | Integer variable with atomic wait()/signal()    | Versatile; counting support |
| Monitors    | High-level abstraction with condition variables | Less error-prone            |

### 6.4 Progression of Topics in Module 3

```
 Process Synchronization Topics Flow:

 Background & Race Conditions (this topic)
 |
 v
 Critical Section Problem
 |
 v
 Peterson's Solution (software)
 |
 v
 Synchronization Hardware (test_and_set, compare_and_swap)
 |
 v
 Semaphores (OS-level tool)
 |
 v
 Classical Problems (Producer-Consumer, Readers-Writers,
 Dining Philosophers)
```

## 7. Cooperating Processes: Benefits and Challenges

### 7.1 Why Allow Cooperation?

Processes cooperate for several reasons:

- **Information sharing**: Multiple users need access to the same data
- **Computation speedup**: Break tasks into subtasks that run in parallel
- **Modularity**: Divide system functions into separate processes
- **Convenience**: A user may work on many tasks at the same time

### 7.2 Challenges of Cooperation

```
 Shared Data Access Without Synchronization:

 Process A Shared Memory Process B
 +---------+ +------------+ +---------+
 | Read |---------->| count = 5 |<------------| Read |
 | Modify | | | | Modify |
 | Write |---------->| count = ? |<------------| Write |
 +---------+ +------------+ +---------+

 Without coordination, the final value of 'count'
 is UNPREDICTABLE -- it depends on timing!
```

## 8. Another Race Condition Example: Shared Linked List

Consider two processes inserting into a shared linked list where `next_available_pid` tracks the next process ID:

```c
// Process A // Process B
pid_A = next_available_pid; pid_B = next_available_pid;
next_available_pid++; next_available_pid++;
```

If `next_available_pid = 100`:

```
Possible interleaving:
T0: Process A reads next_available_pid (gets 100)
T1: Process B reads next_available_pid (gets 100) <-- SAME VALUE!
T2: Process A sets next_available_pid = 101
T3: Process B sets next_available_pid = 101 <-- Should be 102!

Result: Both A and B get pid = 100 (DUPLICATE PID!)
 next_available_pid = 101 instead of 102
```

This is a race condition. Two processes end up with the **same PID**, which would cause system errors.

## 9. Formal Definition of Race Condition

A **race condition** is a situation where:

1. Multiple processes/threads access **shared data** concurrently
2. The final result **depends on the order** of execution (scheduling)
3. The outcome is **non-deterministic** and may differ between runs

The term "race" refers to the processes "racing" to access shared data, with the final result depending on who "wins" (executes last).

## 10. Summary

| Concept               | Key Point                                                   |
| --------------------- | ----------------------------------------------------------- |
| Concurrent processes  | Multiple processes executing with overlapping time periods  |
| Cooperating processes | Processes that share data and affect each other's execution |
| Critical section      | Code segment accessing shared resources                     |
| Race condition        | Outcome depends on unpredictable interleaving of operations |
| Atomic operation      | Executes completely without interruption                    |
| Mutual exclusion      | Only one process in critical section at a time              |
| Progress              | Selection of next process cannot be postponed indefinitely  |
| Bounded waiting       | Finite limit on how long a process waits to enter CS        |

## Exam Tips

1. **Race condition example is a must-know**: The `count++` / `count--` interleaving example with the register-level trace table appears in nearly every exam. Practice writing it from memory with the correct T0-T5 steps.

2. **Know the three requirements**: Mutual Exclusion, Progress, and Bounded Waiting. Be able to explain each clearly and give an example of what happens when one is violated.

3. **Producer-Consumer setup**: Be prepared to write the bounded-buffer code with `in`, `out`, `count`, and explain why `count++` and `count--` cause problems.

4. **Distinguish "concurrent" from "parallel"**: Concurrent means overlapping in time (possible on a single CPU). Parallel means executing at the same instant (requires multiple CPUs). sometimes tests this distinction.

5. **Process structure diagram**: Draw the entry section / critical section / exit section / remainder section structure. This is a simple diagram that earns easy marks.

6. **Link topics together**: When answering a question on synchronization background, briefly mention that solutions include Peterson's, hardware support, and semaphores. This shows breadth of understanding and often earns extra marks.

7. **Common 5-mark question**: "What is a race condition? Explain with an example." Answer with the counter++ / counter-- example, the register-level trace, and conclude with why synchronization is needed.

8. **Common 10-mark question**: "Explain the background of process synchronization including the producer-consumer problem and race conditions." Cover sections 2, 3, and 4 of this topic for a complete answer.
