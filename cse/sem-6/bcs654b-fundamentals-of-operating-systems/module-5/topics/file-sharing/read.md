# File Sharing in Operating Systems

## Introduction

File sharing is a fundamental concept in operating systems that enables multiple users or processes to access and manipulate the same file concurrently. In multi-user and multi-tasking environments, the ability to share files among different processes is essential for efficient collaboration and data management. Without proper file sharing mechanisms, operating systems would force users to work in isolation, significantly reducing productivity and increasing data redundancy.

The importance of file sharing extends beyond simple read operations. Modern computing environments require sophisticated mechanisms that allow concurrent read and write access while maintaining data consistency and integrity. This becomes particularly critical in database systems, web servers, and distributed applications where multiple users may attempt to modify the same data simultaneously. Operating systems provide various primitives and techniques to handle these scenarios, including file locking, semaphores, and different consistency models.

This topic explores the theoretical foundations and practical implementations of file sharing mechanisms in operating systems, examining the challenges of concurrent access and the solutions that have been developed to address them.

## Key Concepts

### Definition and Need for File Sharing

File sharing refers to the capability of multiple users or processes to access the same file simultaneously. The need for file sharing arises in several scenarios: multiple users working on a common project, several processes communicating through shared files, and applications requiring persistent data storage accessible by different components.

In Unix-based systems, file sharing is implemented through the concept of file descriptors and the inode structure. Each process maintains its own file descriptor table, but multiple descriptors can point to the same inode, representing shared file access. The kernel maintains reference counts to track how many descriptors reference each inode, ensuring proper cleanup when all references are closed.

### Simultaneous Access and Concurrency

When multiple processes access a file concurrently, the operating system must handle two primary types of access: read operations and write operations. Read-read access presents no problems since data is not modified. However, read-write and write-write access can lead to inconsistencies if not properly synchronized.

The fundamental challenge lies in maintaining data consistency when concurrent modifications occur. Consider two processes reading and modifying the same file: if both read the same initial value, perform their computations, and write back their results, one process's changes may overwrite the other's, leading to lost updates. This phenomenon is known as a "race condition" and represents a critical issue in file sharing.

### File Locking Mechanisms

File locking is the primary mechanism used to control concurrent access to files. There are two main approaches to file locking:

**Advisory Locking**: In this approach, processes are expected to check for locks before accessing the file, but the system does not enforce lock compliance. If a process ignores the lock and proceeds with its operation, the system will allow it. Unix systems traditionally use advisory locking through the flock() system call. This approach relies on programmer cooperation and is suitable for applications where cooperating processes share a common understanding.

**Mandatory Locking**: In mandatory locking, the operating system enforces lock compliance at the kernel level. Even if a process attempts to access a locked file, the system will block the operation or return an error. Windows NT-based systems implement mandatory locking by default. This approach provides stronger guarantees but may impact performance due to the overhead of enforcement.

### Types of File Locks

**Shared Locks (Read Locks)**: Multiple processes can hold shared locks simultaneously, as long as no process holds an exclusive lock. Shared locks allow concurrent reading, which improves performance in read-heavy workloads.

**Exclusive Locks (Write Locks)**: Only one process can hold an exclusive lock at a time, and no other locks (shared or exclusive) can be held by other processes. Exclusive locks serialize write operations, ensuring that only one process modifies the file at any given time.

### Semantics of File Sharing

Different operating systems implement different semantics for file sharing, which defines the behavior when multiple processes access the same file:

**Unix Semantics**: Every read operation sees the result of all previous write operations. This provides strong consistency guarantees but may have performance implications due to the need for immediate visibility of writes.

**Session Semantics**: Changes made by a process are visible only to that process until the file is closed. Upon closing, the changes become visible to other processes. This model is simpler to implement and is used in some distributed file systems.

**Immutable Files**: Once a file is created, it cannot be modified. Any modification requires creating a new file. This approach eliminates concurrency issues entirely but limits flexibility.

**Transaction Semantics**: Operations are grouped into atomic transactions, either all succeeding or all failing. This provides the strongest consistency guarantees and is commonly used in database systems.

### Issues in File Sharing

**Deadlock**: When processes acquire locks in different orders, they may end up waiting indefinitely for each other. For example, if Process A holds Lock 1 and waits for Lock 2 while Process B holds Lock 2 and waits for Lock 1, both processes are deadlocked.

**Starvation**: A process may be perpetually denied access to a file due to continuous contention from other processes. This can occur in systems with unfair scheduling or poorly designed locking algorithms.

**Priority Inversion**: A low-priority process holding a lock may be preempted by higher-priority processes, causing a higher-priority process waiting for the lock to be indirectly blocked. This can lead to system-wide performance degradation.

## Examples

### Example 1: Banking Transaction

Consider a simple banking application where two ATM processes attempt to update the same account balance. The initial balance is $1000.

Process A reads the balance ($1000), calculates new balance ($1000 + $100 = $1100)
Process B reads the balance ($1000), calculates new balance ($1000 + $50 = $1050)
Process A writes $1100
Process B writes $1050

Without synchronization, the final balance is $1050, and the $100 deposit is lost. Using file locking:

1. Process A acquires an exclusive lock on the account file
2. Process A reads, computes, and writes the new balance ($1100)
3. Process A releases the lock
4. Process B acquires the exclusive lock
5. Process B reads ($1100), computes ($1150), and writes
6. Final balance is correctly $1150

### Example 2: Database Record Update

In a multi-user database system, two users attempt to update the same record:

User 1: UPDATE users SET age = 25 WHERE id = 1
User 2: UPDATE users SET name = 'John' WHERE id = 1

With proper record-level locking:
1. Database acquires lock on row 1 for User 1's transaction
2. User 1's update is applied
3. Lock is released
4. Database acquires lock on row 1 for User 2's transaction
5. User 2's update is applied
6. Both updates are applied successfully

### Example 3: File Append Operations

Two processes appending to a log file:

Process A: Append "Event A\n" to log.txt
Process B: Append "Event B\n" to log.txt

Using exclusive locking ensures:
1. Process A acquires exclusive lock
2. Process A appends "Event A\n"
3. Process A releases lock
4. Process B acquires exclusive lock
5. Process B appends "Event B\n"
6. File contains both entries in correct order

Without locking, the events might interleave, resulting in corrupted output like "Event AEvent B\n\n".

## Exam Tips

1. **Understand the difference between advisory and mandatory locking**: Advisory locking relies on programmer cooperation while mandatory locking is enforced by the operating system.

2. **Remember the types of file locks**: Shared locks allow concurrent reads, while exclusive locks serialize all access.

3. **Know the various file sharing semantics**: Unix semantics provides strongest consistency, while session semantics is simpler and used in distributed systems.

4. **Be aware of deadlock conditions**: Circular wait is one of the four conditions required for deadlock; proper lock ordering can prevent this.

5. **Understand reference counting in Unix**: The kernel uses reference counts in the inode structure to track how many processes are using a file.

6. **Differentiate between file locking and record locking**: File locking applies to entire files, while record locking (used in databases) applies to specific portions of a file.

7. **Know when to use which lock type**: Use shared locks for read-only operations to maximize concurrency, and exclusive locks only when modifying data.

8. **Understand the relationship between file sharing and process communication**: Files can serve as an IPC mechanism when properly synchronized.