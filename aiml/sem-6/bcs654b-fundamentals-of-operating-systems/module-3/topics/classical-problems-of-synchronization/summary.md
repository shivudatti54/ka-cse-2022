# Classical Problems of Synchronization

## Overview

Classical synchronization problems are abstract scenarios illustrating common concurrent programming challenges. The main problems are Producer-Consumer (buffer management), Readers-Writers (data access patterns), Dining Philosophers (deadlock avoidance), and Sleeping Barber (resource scheduling), all solved using semaphores.

## Key Points

- **Producer-Consumer**: Producers add to buffer, consumers remove; semaphores: mutex=1 (buffer access), empty=BUFFER_SIZE, full=0
- **Readers-Writers**: Multiple readers allowed, writers need exclusive access; semaphores: mutex=1 (read_count), wrt=1 (writer exclusion)
- **Dining Philosophers**: 5 philosophers, 5 chopsticks, need both adjacent to eat; naive solution causes deadlock if all pick left simultaneously
- **Deadlock Avoidance**: Allow max 4 philosophers, asymmetric picking (odd left-right, even right-left), or mutex for atomic picking
- **Sleeping Barber**: Barber sleeps if no customers, customers wait if chairs available; semaphores: customers=0, barber=0, mutex=1
- **Mutual Exclusion**: Only one process in critical section at a time
- **Progress**: Process requesting entry must be allowed if no process in critical section
- **Bounded Waiting**: Limit on times other processes enter CS after request

## Important Concepts

- Order of wait() calls crucial - swapping in Producer-Consumer causes deadlock
- Readers-Writers two variations: first (readers priority), second (writers priority)
- Dining Philosophers demonstrates circular wait leading to deadlock
- Modern constructs: Monitors (encapsulate shared data), Condition Variables (structured synchronization)

## Notes

- Understand core constraints of each problem before attempting solutions
- Always initialize semaphores correctly (common mistake)
- Watch for deadlock possibilities especially in Dining Philosophers
- Practice pseudocode implementations to build intuition
- Consider edge cases: full/empty buffer, all philosophers eating simultaneously
