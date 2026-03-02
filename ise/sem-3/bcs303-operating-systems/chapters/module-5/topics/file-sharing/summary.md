# File Sharing - Summary

## Key Definitions and Concepts

- **File Sharing**: The capability of multiple users or processes to access the same file simultaneously for reading or modification

- **Race Condition**: A situation where the final outcome depends on the timing sequence of competing processes, leading to unpredictable and often incorrect results

- **File Locking**: A synchronization mechanism that controls concurrent access to files by allowing or denying access to locked files

- **Shared Lock (Read Lock)**: A lock that permits multiple processes to read a file simultaneously but prevents any process from modifying it

- **Exclusive Lock (Write Lock)**: A lock that grants sole access to one process, preventing all other processes from reading or writing until released

- **Mandatory Locking**: Lock enforcement by the operating system where any access to a locked file is automatically blocked

- **Advisory Locking**: Locking that relies on processes voluntarily checking and respecting locks before file access

## Important Formulas and Theorems

- **Lock Compatibility Matrix**:
  - Shared + Shared = COMPATIBLE (concurrent read allowed)
  - Shared + Exclusive = INCOMPATIBLE (write blocks readers)
  - Exclusive + Exclusive = INCOMPATIBLE (only one writer at a time)

- **Basic Lock Acquisition Sequence**: Open File → Acquire Lock → Perform Operations → Release Lock → Close File

## Key Points

- File sharing enables collaboration and multi-user application support but requires synchronization mechanisms to maintain data integrity

- Race conditions can cause lost updates when multiple processes modify the same file without coordination

- Deadlock occurs when processes hold resources while waiting for other resources held by waiting processes

- Shared locks maximize read concurrency while exclusive locks ensure complete control for modifications

- Record-level locking provides finer granularity than file-level locking, enabling greater concurrency

- Distributed file sharing introduces additional complexity related to network latency and cache coherence

- The operating system provides system calls like flock() and fcntl() (UNIX) or LockFile() (Windows) for implementing file locks

## Common Mistakes to Avoid

1. Confusing shared locks with exclusive locks - remember shared allows concurrent reading, exclusive allows only one accessor

2. Assuming that file locking automatically solves all concurrency problems - improper lock implementation can still lead to race conditions

3. Forgetting to release locks after use, which can cause resource leaks and block other processes indefinitely

4. Overlooking the difference between advisory and mandatory locking - not all systems enforce advisory locks

5. Assuming that locking at one level (file) automatically provides protection at other levels (record), which is not true

## Revision Tips

1. Practice drawing lock compatibility tables to quickly determine which lock combinations are allowed

2. Solve previous year DU examination questions on file sharing to understand the exam pattern and important topics

3. Create simple programs demonstrating file locking to gain practical understanding of the concepts

4. Remember that the key to solving concurrency problems is identifying the critical section where shared resources are accessed

5. Focus on understanding why race conditions occur rather than just memorizing definitions - exam questions often present scenarios requiring analysis