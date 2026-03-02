# Classical Problems of Synchronization

## Introduction

The classical problems of synchronization represent fundamental challenges in concurrent programming that every computer science student must understand. These problems were identified and formalized over decades of operating system research to illustrate the complexities that arise when multiple processes or threads attempt to access shared resources simultaneously. In the context of the University of Delhi's Computer Science curriculum, these problems form the practical foundation for understanding how synchronization primitives work in real-world scenarios.

The importance of these classical problems extends far beyond academic exercises. Modern operating systems, database management systems, and concurrent applications constantly face the same fundamental issues that these problems describe. The producer-consumer problem models scenarios like web servers handling requests, the readers-writers problem represents database access patterns, the dining philosophers problem illustrates resource allocation in distributed systems, and the sleeping barber problem demonstrates service scheduling in multi-server environments. Understanding these problems and their solutions equips students with the analytical tools necessary to design and implement robust concurrent systems.

This topic requires a solid understanding of process synchronization concepts including critical sections, mutual exclusion, and synchronization primitives like semaphores and mutexes. The classical problems serve as comprehensive exercises that integrate all these concepts into practical, solvable frameworks.

## Key Concepts

### Producer-Consumer Problem (Bounded Buffer Problem)

The producer-consumer problem is perhaps the most fundamental synchronization problem. It describes a scenario where one or more producer processes generate data and place it into a shared buffer, while one or more consumer processes remove and process this data. The buffer has a fixed size, creating two critical synchronization requirements: producers must not add data to a full buffer, and consumers must not remove data from an empty buffer.

The shared buffer acts as a bounded queue with two essential operations: produce (insert item) and consume (remove item). Without proper synchronization, multiple producers could overwrite each other's data, and consumers could read invalid data. The solution requires maintaining two count variables: the number of items in the buffer (count) and the positions for producers (in) and consumers (out). Three semaphores are typically used: mutex for mutual exclusion, full to count available items, and empty to count available slots.

The solution uses semaphores where "full" is initialized to 0 (no items initially), "empty" is initialized to buffer size (all slots available), and "mutex" is initialized to 1. The producer waits for an empty slot, acquires mutex, adds the item, releases mutex, and signals that an item is available. The consumer waits for a full slot, acquires mutex, removes the item, releases mutex, and signals that a slot is available.

### Readers-Writers Problem

The readers-writers problem deals with access to a shared database or resource where multiple readers can access the data simultaneously, but writers require exclusive access. Multiple readers can read the data at the same time because reading does not modify the data. However, when a writer wants to write, no other reader or writer must be accessing the resource simultaneously to prevent data corruption or inconsistent reads.

This problem introduces a subtle distinction between read operations and write operations. A read operation is idempotent and can proceed concurrently with other reads. A write operation modifies the shared resource and must have exclusive access. The challenge lies in implementing a solution that prevents writer starvation while allowing reasonable read throughput.

The readers-preference solution uses three semaphores: mutex to protect the read count, readTry to coordinate reader entry, and write to ensure writer exclusivity. A read lock is acquired by incrementing a reader count and releasing mutex. When the first reader arrives, it acquires the write semaphore to block writers. The last reader releases the write semaphore to allow writers. Writers must acquire both the write semaphore and the resource lock, ensuring exclusive access.

The writers-preference solution gives priority to writers by having readers check if a writer is waiting. If a writer is waiting, new readers block themselves, allowing the waiting writer to proceed. This prevents writer starvation at the cost of potentially lower read throughput.

### Dining Philosophers Problem

The dining philosophers problem is a classic illustration of resource allocation and deadlock. Five philosophers sit around a circular table with a fork between each pair. Each philosopher alternates between thinking and eating. To eat, a philosopher needs both the fork on their left and the fork on their right. The challenge is to design a protocol that allows all philosophers to eat eventually without creating deadlock or starvation.

This problem demonstrates several critical synchronization concepts. Deadlock occurs if each philosopher picks up their left fork simultaneously, waiting indefinitely for the right fork. Starvation can occur if a philosopher never gets both forks. The solution must ensure progress, bounded waiting, and mutual exclusion.

The solution using semaphores implements a butler (centralized coordinator) who allows only four philosophers to attempt eating simultaneously. This guarantees that at least one philosopher can acquire both forks. Each fork is represented by a semaphore initialized to 1. Each philosopher follows a sequence: think, acquire left fork, acquire right fork, eat, release both forks, repeat. The butler semaphore limits concurrent fork acquisition attempts.

Another elegant solution uses a state array where each philosopher can be in thinking, hungry, or eating states. A test function checks if a philosopher can eat (neither neighbor is eating). This solution is starvation-free because it allows a philosopher to eat only when both forks are available, and the circular waiting is broken by the test sequence.

### Sleeping Barber Problem

The sleeping barber problem describes a barber shop with a limited number of chairs for waiting customers. The barber sleeps when there are no customers. When a customer arrives and finds the barber sleeping, they wake the barber and get a haircut. If customers arrive while the barber is busy, they either wait in a chair or leave if all chairs are occupied. This problem models real-world scenarios like CPU task scheduling and resource pooling.

The solution requires coordinating three entities: customers, the barber, and the shop chairs. Semaphores track the barber's state (asleep or working), customer availability, and chair availability. A mutex protects shared variables like the waiting customer count.

The solution uses three semaphores: customers (initialized to 0), barbers (initialized to 0), and mutex (initialized to 1). Additional variables track the number of waiting customers and total chairs. The barber process waits for a customer, acquires mutex to check for waiting customers, serves them, and repeats. The customer process checks if chairs are available, increments the waiting count, signals the barber, and waits for their turn.

## Examples

### Example 1: Producer-Consumer with Semaphores

Consider a producer-consumer system with buffer size 5. Initially, full = 0, empty = 5, and mutex = 1. Trace the execution when producer produces two items and consumer consumes one item.

For the first producer operation: The producer checks if empty > 0 (5 > 0 is true), decrements empty to 4, acquires mutex, produces item at buffer[in] where in = 0, sets buffer[0] = item1, increments in to 1, releases mutex, and increments full to 1.

For the second producer operation: empty = 4 > 0, decrements to 3, acquires mutex, produces at buffer[1], sets buffer[1] = item2, increments in to 2, releases mutex, increments full to 2.

For the consumer operation: full = 2 > 0, decrements to 1, acquires mutex, consumes item from buffer[out] where out = 0, reads item1, increments out to 1, releases mutex, increments empty to 4.

This trace demonstrates how semaphores coordinate access without race conditions. The empty semaphore tracks available slots, full tracks filled slots, and mutex ensures atomic buffer modifications.

### Example 2: Readers-Writers with Writer Priority

In a database system with readers-preference, assume two readers R1 and R2 arrive, followed by a writer W. R1 arrives, sets readcount to 1, sees no writer, acquires write lock indirectly, reads database, does not release write lock. R2 arrives, sets readcount to 2, reads database concurrently with R1. R1 finishes, decrements readcount to 1, still holds read access. R2 finishes, decrements readcount to 0, releases write lock. Now W can acquire write lock and proceed with exclusive access.

In a writers-preference system with the same arrival pattern: R1 arrives and reads. R2 arrives and reads. W arrives and waits. When R1 and R2 finish, W proceeds immediately without allowing new readers to start. This prevents writer starvation at the cost of read throughput.

### Example 3: Dining Philosophers State-Based Solution

In the state-based solution with five philosophers numbered 0 to 4, each philosopher i has neighbors at (i + 4) % 5 and (i + 1) % 5. Initially, all philosophers are in THINKING state. When philosopher 0 becomes hungry, it tests if neighbors 4 and 1 are not eating. If both are not eating, philosopher 0 transitions to EATING. The test function ensures that at most two adjacent philosophers eat simultaneously, preventing deadlock while allowing concurrency.

## Exam Tips

For DU semester examinations, several key points deserve special attention. First, remember that the producer-consumer problem requires three semaphores: mutex for mutual exclusion, full for tracking filled slots, and empty for tracking empty slots. The initial values are critical—full starts at 0, empty at buffer size, and mutex at 1.

Second, in the readers-writers problem, distinguish between readers-preference and writers-preference solutions. Readers-preference can cause writer starvation, while writers-preference can cause reader starvation. Always mention the tradeoffs when explaining solutions.

Third, the dining philosophers problem demonstrates deadlock when each philosopher picks up their left fork simultaneously. Solutions include breaking circular wait (asymmetric pickup), using a centralized coordinator (butler), or using a state-based approach with testing.

Fourth, always specify initial semaphore values when writing solutions. This is a common exam question asking students to trace execution or identify synchronization failures.

Fifth, understand the difference between blocking and non-blocking solutions. Semaphore-based solutions are blocking (processes wait), while hardware-based solutions might use busy-waiting.

Sixth, for the sleeping barber problem, remember that customers wait for the barber (customer semaphore) and the barber waits for customers (barber semaphore). The mutual exclusion semaphore protects shared variables like waiting count.

Seventh, when analyzing solutions, consider the four requirements: mutual exclusion (no two processes in critical section), progress (processes outside critical section cannot block others), bounded waiting (limit on entry attempts), and no deadlock (system eventually proceeds).

Eighth, practice drawing timeline diagrams showing process interleaving. These help identify race conditions and verify that solutions maintain correctness under all possible execution sequences.