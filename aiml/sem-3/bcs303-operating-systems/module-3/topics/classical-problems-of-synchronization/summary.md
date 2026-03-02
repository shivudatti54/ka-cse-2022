# Classical Problems of Synchronization - Summary

## Key Definitions

- **Producer-Consumer Problem:** A synchronization problem where producers generate data items and place them in a bounded buffer, while consumers remove and process items.

- **Readers-Writers Problem:** A problem where multiple readers can access shared data concurrently, but writers require exclusive access to prevent data inconsistency.

- **Dining Philosophers Problem:** A classic deadlock prevention problem involving five philosophers who need two forks to eat, sitting between each pair.

- **Sleeping Barber Problem:** A synchronization problem modeling a barbershop where customers arrive randomly and the barber sleeps when idle.

- **Bounded Buffer:** A fixed-size buffer with capacity constraints, requiring producers to wait when full and consumers to wait when empty.

## Important Formulas

- Buffer indices: `in = (in + 1) % BUFFER_SIZE` and `out = (out + 1) % BUFFER_SIZE`
- Dining Philosophers fork indices: `LEFT = (i + N - 1) % N`, `RIGHT = (i + 1) % N`
- Three semaphores for Producer-Consumer: `mutex`, `empty`, `full`
- Reader count synchronization requires: `wait(mutex)` and `wait(db)` for first reader

## Key Points

1. The Producer-Consumer problem requires three semaphores: one for mutual exclusion and two for counting (empty and full slots).

2. In the Readers-Writers problem, only the first reader needs to acquire the database lock, and only the last reader releases it.

3. The Dining Philosophers problem can be solved by breaking circular wait - either through even-odd philosopher numbering or state-based testing.

4. The Sleeping Barber problem requires coordination of barber state (sleeping/working) and customer queue management.

5. Classical solutions use semaphores, monitors, or condition variables to achieve process synchronization.

6. Deadlock prevention in Dining Philosophers requires ensuring not all philosophers can pick up forks simultaneously.

7. Starvation can occur in synchronization solutions if fairness mechanisms are not implemented.

8. The choice between readers-preference and writers-preference in Readers-Writers has significant performance implications.

9. Monitor-based solutions provide better encapsulation of shared variables and synchronization logic.

10. These classical problems form the foundation for understanding real-world concurrent programming challenges.

## Common Mistakes

1. **Incorrect semaphore ordering:** Acquiring mutex before condition semaphores can lead to deadlock.

2. **Forgetting to signal:** Failing to signal appropriate semaphores after critical sections, causing processes to remain blocked indefinitely.

3. **Race conditions on counters:** Not protecting shared counters like `readcount` with mutex semaphores.

4. **Not initializing semaphores correctly:** Initial values of counting semaphores are crucial - empty should equal buffer size, full should be zero.

5. **Busy-waiting inefficiency:** Using while loops with continuous checking instead of proper blocking synchronization wastes CPU cycles.

6. **Incomplete mutual exclusion:** Some solutions protect buffer access but forget to protect shared variables like indices.

7. **Ignoring starvation:** Solutions that work correctly but may cause starvation of certain processes are incomplete.

8. **Forgetting bounded buffer constraints:** Not checking buffer capacity leads to buffer overflow in producer-consumer solutions.