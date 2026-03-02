# Semaphores


## Table of Contents

- [Semaphores](#semaphores)
- [What is a Semaphore?](#what-is-a-semaphore)
- [Types of Semaphores](#types-of-semaphores)
  - [Binary Semaphore (Mutex)](#binary-semaphore-mutex)
  - [Counting Semaphore](#counting-semaphore)
- [Semaphore Operations](#semaphore-operations)
  - [Wait (P, down, acquire)](#wait-p-down-acquire)
  - [Signal (V, up, release)](#signal-v-up-release)
  - [Without Busy Waiting](#without-busy-waiting)
- [Usage Patterns](#usage-patterns)
  - [Mutual Exclusion](#mutual-exclusion)
  - [Synchronization (Ordering)](#synchronization-ordering)
  - [Resource Counting](#resource-counting)
- [Important Properties](#important-properties)
- [Common Pitfalls](#common-pitfalls)
- [Semaphore vs Mutex](#semaphore-vs-mutex)

## What is a Semaphore?

A synchronization primitive consisting of:

- An integer value
- Two atomic operations: wait (P) and signal (V)

## Types of Semaphores

### Binary Semaphore (Mutex)

- Value: 0 or 1
- Used for mutual exclusion
- Like a lock

### Counting Semaphore

- Value: 0 to N
- Used for resource counting
- Controls access to pool of resources

## Semaphore Operations

### Wait (P, down, acquire)

```c
wait(S) {
 while (S <= 0); // Busy wait
 S--;
}
```

### Signal (V, up, release)

```c
signal(S) {
 S++;
}
```

### Without Busy Waiting

```c
typedef struct {
 int value;
 struct process *list;
} semaphore;

wait(semaphore *S) {
 S->value--;
 if (S->value < 0) {
 add this process to S->list;
 block();
 }
}

signal(semaphore *S) {
 S->value++;
 if (S->value <= 0) {
 remove process P from S->list;
 wakeup(P);
 }
}
```

## Usage Patterns

### Mutual Exclusion

```c
semaphore mutex = 1;

// Process
wait(mutex);
 // Critical section
signal(mutex);
```

### Synchronization (Ordering)

```c
// Ensure S2 executes after S1
semaphore sync = 0;

Process A: Process B:
 S1; wait(sync);
 signal(sync); S2;
```

### Resource Counting

```c
semaphore resources = N; // N available

wait(resources); // Acquire one
 // Use resource
signal(resources); // Release one
```

## Important Properties

| Property       | Description                          |
| -------------- | ------------------------------------ |
| Atomicity      | wait and signal are atomic           |
| No busy wait   | With blocking implementation         |
| Negative value | Absolute value = # waiting processes |

## Common Pitfalls

1. **Deadlock**: wait(A); wait(B); in one process, wait(B); wait(A); in another
2. **Incorrect order**: signal before wait
3. **Missing signal**: Process never releases
4. **Missing wait**: No synchronization

## Semaphore vs Mutex

| Aspect    | Semaphore           | Mutex            |
| --------- | ------------------- | ---------------- |
| Value     | 0 to N              | 0 or 1           |
| Ownership | No owner            | Has owner        |
| Use       | Resources, ordering | Mutual exclusion |
| Release   | Any thread          | Only owner       |
