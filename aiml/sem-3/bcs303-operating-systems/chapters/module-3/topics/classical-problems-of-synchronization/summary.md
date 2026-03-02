# Classical Problems of Synchronization - Summary

## Key Definitions and Concepts

- PRODUCER-CONSUMER PROBLEM: A synchronization problem where producers add items to a bounded buffer and consumers remove items, requiring coordination to prevent buffer overflow and underflow

- READERS-WRITERS PROBLEM: A synchronization problem where multiple readers can access shared data concurrently but writers require exclusive access

- DINING PHILOSOPHERS PROBLEM: A resource allocation problem where five philosophers must acquire two shared forks to eat, illustrating deadlock and starvation issues

- SLEEPING BARBER PROBLEM: A service scheduling problem modeling a barber shop where customers arrive for service and the barber sleeps when idle

## Important Formulas and Theorems

- Producer-consumer initial semaphores: mutex = 1, full = 0, empty = buffer_size
- Readers count synchronization: readcount tracks active readers; first reader acquires resource lock, last reader releases it
- Dining philosophers: Forks represented as semaphores initialized to 1; state array tracks thinking, hungry, eating states
- Sleeping barber: customer semaphore tracks available customers; barber semaphore tracks barber availability

## Key Points

- The producer-consumer problem requires three semaphores: mutex (mutual exclusion), full (count of filled slots), and empty (count of empty slots)

- In readers-writers, readers can execute concurrently but writers need exclusive access; readers-preference may cause writer starvation while writers-preference may cause reader starvation

- Dining philosophers deadlock occurs when each philosopher picks up their left fork simultaneously; solutions include asymmetric pickup, centralized coordinator, or state-based testing

- The sleeping barber uses barber and customer semaphores to coordinate service; customers wait if chairs full or barber busy

- All classical problems demonstrate the four necessary conditions for deadlock: mutual exclusion, hold and wait, no preemption, and circular wait

- Semaphore solutions require correct initial values; incorrect initialization leads to race conditions or deadlock

- The test-and-set approach in dining philosophers guarantees freedom from starvation by checking neighbor states before allowing eating

## Common Mistakes to Avoid

- Forgetting to initialize semaphores with correct values; this causes immediate synchronization failures

- Neglecting to release mutex after critical section operations, leading to mutual exclusion violations

- Confusing full and empty semaphore roles; full counts available items, empty counts available slots

- Not distinguishing between readers-preference and writers-preference in readers-writers problem analysis

- Overlooking the bounded waiting requirement when analyzing solutions for correctness

## Revision Tips

- Practice tracing through semaphore operations with specific initial values to understand execution flow

- Draw state diagrams for dining philosophers and sleeping barber to visualize process transitions

- Memorize the initial semaphore values for each classical problem as this frequently appears in exams

- Compare solutions by analyzing tradeoffs between throughput, fairness, and implementation complexity

- Review the conditions for deadlock and identify which conditions each solution breaks