# Critical Section Problem

## The Problem

When multiple processes access shared resources concurrently, race conditions can occur leading to inconsistent data.

### Race Condition Example

```
// Shared variable: counter = 5
Process P1: counter++ Process P2: counter--
// Expected: 5, Actual: Could be 4, 5, or 6
```

## Critical Section

A code segment where shared resources are accessed. Only one process should execute in its critical section at a time.

### Structure of Process

```
do {
 entry section // Request permission
 CRITICAL SECTION // Access shared resource
 exit section // Release permission
 remainder section // Non-critical code
} while(true);
```

## Requirements for Solution

### 1. Mutual Exclusion

Only one process in critical section at a time.

### 2. Progress

If no process is in CS, and some wish to enter, only those not in remainder section can participate in decision, and decision cannot be postponed indefinitely.

### 3. Bounded Waiting

A bound must exist on the number of times other processes enter CS after a process requests and before that request is granted.

## Software Solutions

### Peterson's Solution (2 processes)

```c
// Shared variables
int turn;
bool flag[2];

// Process Pi
flag[i] = true;
turn = j;
while (flag[j] && turn == j); // Entry
 // Critical Section
flag[i] = false; // Exit
```

### Bakery Algorithm (n processes)

Each process takes a "ticket number". Process with lowest number enters CS. If tie, lower process ID wins.

## Hardware Solutions

### Test-and-Set

```c
bool TestAndSet(bool *target) {
 bool rv = *target;
 *target = true;
 return rv;
}

// Usage
while (TestAndSet(&lock)); // Entry
 // Critical Section
lock = false; // Exit
```

### Compare-and-Swap (CAS)

```c
int CompareAndSwap(int *value, int expected, int new_value) {
 int temp = *value;
 if (*value == expected)
 *value = new_value;
 return temp;
}
```

## Comparison

| Solution     | Pros                    | Cons                     |
| ------------ | ----------------------- | ------------------------ |
| Peterson's   | Simple, software only   | Only 2 processes         |
| Bakery       | N processes             | Complex, high overhead   |
| Test-and-Set | Fast, simple            | Busy waiting             |
| CAS          | Foundation of lock-free | Complex to use correctly |
