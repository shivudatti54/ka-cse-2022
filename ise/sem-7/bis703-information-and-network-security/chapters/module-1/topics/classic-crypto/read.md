# Classic Synchronization Problems

## Overview

Classic synchronization problems demonstrate common concurrent programming challenges and their solutions using semaphores and monitors.

## 1. Producer-Consumer Problem

### Problem Statement

- **Producer**: Creates items, places in buffer
- **Consumer**: Removes items from buffer
- **Constraints**: Buffer is bounded (fixed size)

### Solution with Semaphores

```c
semaphore mutex = 1;    // Buffer access
semaphore empty = N;    // Empty slots
semaphore full = 0;     // Filled slots

Producer:
    while (true) {
        item = produce();
        wait(empty);      // Wait for empty slot
        wait(mutex);      // Enter critical section
        buffer[in] = item;
        in = (in + 1) % N;
        signal(mutex);    // Exit critical section
        signal(full);     // Signal item available
    }

Consumer:
    while (true) {
        wait(full);       // Wait for item
        wait(mutex);      // Enter critical section
        item = buffer[out];
        out = (out + 1) % N;
        signal(mutex);    // Exit critical section
        signal(empty);    // Signal slot available
        consume(item);
    }
```

## 2. Readers-Writers Problem

### Problem Statement

- Multiple readers can read simultaneously
- Writers need exclusive access
- No reader should wait if no writer is writing

### First Readers-Writers Solution (Readers Preference)

```c
semaphore mutex = 1;      // Protect read_count
semaphore wrt = 1;        // Writer access
int read_count = 0;       // Active readers

Writer:
    wait(wrt);            // Get exclusive access
    // Write
    signal(wrt);

Reader:
    wait(mutex);
    read_count++;
    if (read_count == 1)
        wait(wrt);        // First reader locks writer
    signal(mutex);

    // Read

    wait(mutex);
    read_count--;
    if (read_count == 0)
        signal(wrt);      // Last reader unlocks writer
    signal(mutex);
```

**Problem**: Writers may starve

### Second Solution (Writers Preference)

- Writers have priority
- Readers may starve

## 3. Dining Philosophers Problem

### Problem Statement

- 5 philosophers sit at round table
- 5 chopsticks (one between each pair)
- Philosopher needs 2 chopsticks to eat
- Must avoid deadlock and starvation

### Naive Solution (DEADLOCK!)

```c
Philosopher i:
    wait(chopstick[i]);
    wait(chopstick[(i+1) % 5]);
    // Eat
    signal(chopstick[i]);
    signal(chopstick[(i+1) % 5]);
```

**Problem**: All pick left chopstick → deadlock

### Solutions

**Solution 1: Asymmetric**

- Odd philosophers: pick left first
- Even philosophers: pick right first
- Breaks circular wait

**Solution 2: Limit Philosophers**

- Allow only 4 philosophers at table
- Guarantees at least one can eat

**Solution 3: Pick Both or None**

```c
semaphore mutex = 1;

Philosopher i:
    wait(mutex);
    wait(chopstick[i]);
    wait(chopstick[(i+1) % 5]);
    signal(mutex);
    // Eat
    signal(chopstick[i]);
    signal(chopstick[(i+1) % 5]);
```

## 4. Sleeping Barber Problem

### Problem Statement

- Barber sleeps if no customers
- Customer wakes barber or waits if busy
- Waiting room has N chairs
- Customer leaves if no waiting chairs

### Solution

```c
semaphore customers = 0;  // Waiting customers
semaphore barber = 0;     // Barber ready
semaphore mutex = 1;      // Protect waiting
int waiting = 0;          // Customers waiting

Barber:
    while (true) {
        wait(customers);  // Sleep until customer
        wait(mutex);
        waiting--;
        signal(barber);   // Ready to cut
        signal(mutex);
        cut_hair();
    }

Customer:
    wait(mutex);
    if (waiting < N) {
        waiting++;
        signal(customers);  // Wake barber
        signal(mutex);
        wait(barber);       // Wait for barber
        get_haircut();
    } else {
        signal(mutex);
        leave();            // No chairs
    }
```

## Summary Table

| Problem             | Key Challenge       | Key Insight               |
| ------------------- | ------------------- | ------------------------- |
| Producer-Consumer   | Bounded buffer      | Count empty/full slots    |
| Readers-Writers     | Shared vs exclusive | Track reader count        |
| Dining Philosophers | Circular deadlock   | Break symmetry            |
| Sleeping Barber     | Rendezvous          | Customer/barber signaling |
