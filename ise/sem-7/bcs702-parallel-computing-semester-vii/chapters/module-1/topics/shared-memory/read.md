# Semaphores and Shared Memory in System V IPC

## Introduction to Interprocess Communication (IPC)

Interprocess Communication (IPC) refers to the mechanisms an operating system provides to allow processes to communicate with each other and synchronize their actions. This is essential for processes that need to share data or coordinate their activities. In the context of UNIX System Programming, two of the most powerful and commonly used System V IPC mechanisms are **Semaphores** and **Shared Memory**.

System V IPC provides three types of IPC facilities:

1. **Message Queues**: For passing messages between processes.
2. **Semaphores**: For synchronizing processes.
3. **Shared Memory**: For allowing multiple processes to access the same memory segment.

This study material focuses on the latter two: Semaphores and Shared Memory, which are often used together to solve complex synchronization problems.

## Understanding Shared Memory

### What is Shared Memory?

Shared memory is an IPC mechanism that enables multiple processes to access the same segment of memory. This is the **fastest form of IPC** available because it avoids copying data between process address spaces and the kernel. Once the shared memory segment is established, processes can read from and write to it directly, just like any other part of their memory.

However, this speed comes with a significant challenge: **synchronization**. Since multiple processes can access the memory simultaneously, there is a high risk of race conditions, where the final outcome depends on the non-deterministic order of execution. This is where semaphores come into play.

### Key Concepts of Shared Memory

- **Segment**: A shared memory segment is a block of memory that can be attached to the address space of multiple processes.
- **Key (`key_t`)**: A System V IPC key (often created with `ftok()`) is used to identify the shared memory segment. Different processes using the same key will access the same segment.
- **Identifier (`shmid`)**: The kernel returns a unique identifier when a segment is created. This identifier is used in subsequent calls.
- **Attachment**: A process must "attach" a shared memory segment to its address space using `shmat()` before it can use it.
- **Detachment**: A process detaches the segment from its address space using `shmdt()` when it's done.
- **Control**: The `shmctl()` function is used for various control operations, such as deleting a segment.

### System Calls for Shared Memory

1.  **`ftok()` - Convert a Pathname to a Key**

    ```c
    #include <sys/ipc.h>
    key_t ftok(const char *pathname, int proj_id);
    ```

    Generates a key based on a file path and a project identifier. Not strictly necessary, as you can use `IPC_PRIVATE`, but it's the standard way for unrelated processes to agree on a key.

2.  **`shmget()` - Get a Shared Memory Segment**

    ```c
    #include <sys/shm.h>
    int shmget(key_t key, size_t size, int shmflg);
    ```

    - `key`: IPC key (`IPC_PRIVATE` or from `ftok()`).
    - `size`: The size of the segment in bytes.
    - `shmflg`: Permissions (e.g., `0666`) combined with flags like `IPC_CREAT` (create if it doesn't exist) or `IPC_EXCL` (fail if it exists).
    - Returns a shared memory identifier (`shmid`) on success.

3.  **`shmat()` - Attach Shared Memory Segment**

    ```c
    void *shmat(int shmid, const void *shmaddr, int shmflg);
    ```

    - `shmid`: The identifier from `shmget()`.
    - `shmaddr`: Suggested address (usually `NULL` to let OS choose).
    - `shmflg`: Flags (e.g., `SHM_RDONLY` for read-only attachment).
    - Returns the address of the attached segment on success.

4.  **`shmdt()` - Detach Shared Memory Segment**

    ```c
    int shmdt(const void *shmaddr);
    ```

    - `shmaddr`: The address returned by `shmat()`.

5.  **`shmctl()` - Control Shared Memory Segment**
    ```c
    int shmctl(int shmid, int cmd, struct shmid_ds *buf);
    ```

    - `shmid`: The shared memory identifier.
    - `cmd`: Command (e.g., `IPC_RMID` to remove the segment).
    - `buf`: A pointer to a `shmid_ds` structure for info/stat commands.

### Lifecycle of a Shared Memory Segment

```
+---------+      shmget()      +----------------------+
| Process |------------------->| Kernel creates/shared|
| 1       | (key, size, flags) | Memory Segment       |
+---------+                    +----------------------+
                                     | shmat()
                                     | (returns addr)
                                     v
+---------+                    +----------------------+
| Process |<-------------------| Segment attached to  |
| 1       | (shared mem addr) | Process 1's addr space|
+---------+                    +----------------------+
                                     | shmat() for Process 2
                                     v
+---------+                    +----------------------+
| Process |<-------------------| Segment attached to  |
| 2       | (shared mem addr) | Process 2's addr space|
+---------+                    +----------------------+
                                     | shmdt() by all processes
                                     | then shmctl(IPC_RMID)
                                     v
                               [Segment is destroyed]
```

## Understanding Semaphores

### What is a Semaphore?

A semaphore is a synchronization primitive used to control access to a shared resource (like a shared memory segment) in a multi-process environment. Conceptually, a semaphore is a non-negative integer value on which two atomic operations can be performed:

1.  **Wait (P Operation)**: Decrements the semaphore value. If the value becomes negative, the process is blocked until it becomes non-negative again.
2.  **Signal (V Operation)**: Increments the semaphore value. If there are processes blocked waiting on this semaphore, one of them is awakened.

In System V IPC, semaphores are implemented as sets (arrays) of semaphores, not just single values. This allows you to manage multiple resources with a single semaphore set.

### Key Concepts of Semaphores

- **Set**: A collection of one or more semaphores.
- **Key (`key_t`)**: Similar to shared memory, used to identify the semaphore set.
- **Identifier (`semid`)**: The kernel returns a unique identifier for the set.
- **Operations**: Performed on individual semaphores within a set using `semop()`.
- **Control**: The `semctl()` function is used for control operations like initializing values or removing the set.

### System Calls for Semaphores

1.  **`semget()` - Get a Semaphore Set**

    ```c
    #include <sys/sem.h>
    int semget(key_t key, int nsems, int semflg);
    ```

    - `key`: IPC key.
    - `nsems`: The number of semaphores in the set.
    - `semflg`: Permissions and flags (`IPC_CREAT`, `IPC_EXCL`).
    - Returns a semaphore set identifier (`semid`) on success.

2.  **`semop()` - Perform Semaphore Operations**

    ```c
    int semop(int semid, struct sembuf *sops, size_t nsops);
    ```

    - `semid`: The semaphore set identifier.
    - `sops`: A pointer to an array of operations.
    - `nsops`: The number of operations in the array.
      The `sembuf` structure defines an operation:

    ```c
    struct sembuf {
        unsigned short sem_num;  // semaphore index in set
        short          sem_op;   // operation (e.g., -1, +1)
        short          sem_flg;  // flags (e.g., IPC_NOWAIT, SEM_UNDO)
    };
    ```

3.  **`semctl()` - Control Semaphore Set**
    ```c
    int semctl(int semid, int semnum, int cmd, ... /* union semun arg */);
    ```

    - `semid`: The semaphore set identifier.
    - `semnum`: The semaphore number within the set for specific commands.
    - `cmd`: Command (e.g., `SETVAL` to set a value, `IPC_RMID` to remove).
    - `arg`: A union of type `semun` is required for many commands. This is a pain point in System V semaphores.

### Common Use Pattern: Mutual Exclusion (Mutex)

A binary semaphore (value 0 or 1) can be used as a mutex lock to ensure only one process accesses a critical section (e.g., the shared memory) at a time.

**Process entering critical section:**

```c
struct sembuf sop = {0, -1, 0}; // Wait (Lock) on semaphore 0
semop(semid, &sop, 1);
// ... CRITICAL SECTION: Access shared memory ...
```

**Process leaving critical section:**

```c
struct sembuf sop = {0, +1, 0}; // Signal (Unlock) semaphore 0
semop(semid, &sop, 1);
```

## Putting It All Together: A Producer-Consumer Example

A classic problem demonstrating the combined use of shared memory and semaphores is the Producer-Consumer problem.

- **Shared Memory**: Holds a fixed-size buffer.
- **Semaphores**:
  - `mutex`: A binary semaphore for mutual exclusion when accessing the buffer (always 1).
  - `empty`: Counts the number of empty slots in the buffer (initialized to `BUFFER_SIZE`).
  - `full`: Counts the number of full slots in the buffer (initialized to `0`).

**Producer Process:**

1.  Wait(`empty`); // Wait for an empty slot
2.  Wait(`mutex`); // Lock the buffer
3.  Produce an item and put it in the buffer.
4.  Signal(`mutex`); // Unlock the buffer
5.  Signal(`full`); // Increment count of full slots

**Consumer Process:**

1.  Wait(`full`); // Wait for a full slot
2.  Wait(`mutex`); // Lock the buffer
3.  Consume an item from the buffer.
4.  Signal(`mutex`); // Unlock the buffer
5.  Signal(`empty`); // Increment count of empty slots

This ensures the producer doesn't overflow the buffer and the consumer doesn't try to consume from an empty buffer, all while preventing race conditions during buffer access.

## Comparison of IPC Mechanisms

| Mechanism          | Data Passing  | Synchronization                | Complexity | Performance   |
| :----------------- | :------------ | :----------------------------- | :--------- | :------------ |
| **Pipes**          | Byte Stream   | Built-in                       | Low        | Medium        |
| **FIFOs**          | Byte Stream   | Built-in                       | Medium     | Medium        |
| **Message Queues** | Messages      | Built-in                       | Medium     | Low-Medium    |
| **Shared Memory**  | Direct Access | **None** (Requires Semaphores) | High       | **Very High** |
| **Semaphores**     | N/A           | Explicit                       | High       | High          |

## Exam Tips

1.  **Understand the "Why"**: Always be prepared to explain why synchronization is necessary when using shared memory. The answer always involves preventing race conditions.
2.  **Know the System Calls**: Memorize the names, parameters, and return values of `shmget()`, `shmat()`, `shmdt()`, `shmctl()`, `semget()`, `semop()`, and `semctl()`. Be able to write their function prototypes.
3.  **Key vs. ID**: Clearly distinguish between the `key_t` key (used to _find/create_ an IPC object) and the integer ID (used to _reference_ it in subsequent calls).
4.  **Permission Bits**: Remember that IPC calls use the same permission bits as files (e.g., `0666` for read/write for user, group, and others).
5.  **Producer-Consumer**: Be able to draw the diagram and write the pseudocode for the producer-consumer problem using semaphores. This is a very common exam question.
6.  **Atomicity**: Remember that the operations performed by `semop()` are atomic. If you specify multiple operations in the `sops` array, they will all be performed atomically (all or nothing), which is a powerful feature.
7.  **Persistence**: System V IPC objects (shared memory, semaphores) have kernel persistence. They remain in the system until explicitly deleted (e.g., `shmctl(IPC_RMID)`) or the system reboots, even if no processes are attached to them. Use the `ipcs` and `ipcrm` commands to view and remove them.
