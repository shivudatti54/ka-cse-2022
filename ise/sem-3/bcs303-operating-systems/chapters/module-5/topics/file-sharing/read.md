# File Sharing

## Introduction

File sharing is a fundamental concept in operating systems that enables multiple users or processes to access and work with the same file simultaneously. In modern computing environments, where collaboration and multi-user systems are ubiquitous, file sharing has become an essential feature of any robust file system. The ability to share files efficiently and safely among multiple users directly impacts system productivity, data consistency, and overall system performance.

In the context of University of Delhi's Computer Science curriculum, understanding file sharing mechanisms is crucial for comprehending how operating systems manage concurrent access to shared resources. This topic builds upon earlier concepts like file concepts, access methods, and protection mechanisms. File sharing goes beyond simple read operations; it encompasses complex issues of synchronization, access control, and maintaining data integrity when multiple entities attempt to manipulate the same file concurrently.

The importance of file sharing extends far beyond academic considerations. In real-world scenarios, organizations rely on file sharing mechanisms to enable collaboration among employees, facilitate distributed computing, and support multi-user applications. Whether it is a team of programmers working on the same source code repository or multiple users accessing a database, the underlying principles of file sharing remain consistent and critical for system reliability.

## Key Concepts

### Definition and Need for File Sharing

File sharing refers to the capability of multiple users or processes to access the same file simultaneously, either for reading or modification. The need for file sharing arises from several practical requirements in computing environments. First, collaborative work often requires different users to work on the same set of documents or data files. Second, many applications are designed to serve multiple users concurrently, requiring access to shared configuration or data files. Third, inter-process communication sometimes utilizes files as a medium for exchanging information.

Without proper file sharing mechanisms, each user would need a separate copy of the file, leading to data redundancy, inconsistency problems, and wasted storage space. Operating systems provide various mechanisms to enable controlled file sharing while maintaining data integrity and system security.

### Multi-User File Access

In multi-user operating systems, file sharing becomes a critical functionality. When multiple users attempt to access the same file, the operating system must implement access control mechanisms to determine which operations are permitted. The access control typically follows the protection model discussed in earlier sections, where each file has associated permissions specifying what operations different users or groups can perform.

The three primary types of file access in a multi-user context are:

**Exclusive Access**: Only one user can access the file at a time. This approach is simple but limits productivity and concurrency.

**Shared Read**: Multiple users can read the file simultaneously, but writes require exclusive access. This is the most common approach for documents that are primarily read-only but occasionally modified.

**Concurrent Access**: Multiple users can read and write simultaneously, requiring sophisticated synchronization mechanisms to maintain consistency.

### Concurrent Access Problems

When multiple processes or users share access to the same file, several problems can arise if proper synchronization is not implemented:

**Race Conditions**: This occurs when the outcome of operations depends on the timing and sequence of competing processes. For example, if two users simultaneously attempt to update the same record in a file, the final result may depend on which user completes their operation first, potentially leading to lost updates.

**Inconsistent State**: Without proper locking mechanisms, a file may be left in an inconsistent state if a process crashes while modifying it. Other processes reading the file during this period may encounter corrupted or partial data.

**Deadlock**: This occurs when two or more processes are waiting for each other to release resources. For instance, if Process A holds File 1 and needs File 2, while Process B holds File 2 and needs File 1, neither can proceed.

**Starvation**: A process may be perpetually denied access to a file because other processes continuously access it before it can obtain the required lock.

### File Locking Mechanisms

File locking is a synchronization mechanism that controls access to files in a concurrent environment. It ensures that only authorized processes can access a file at any given time, preventing conflicts and maintaining data integrity.

**Mandatory Locking**: The operating system enforces the locks, and any process attempting to access a locked file will be blocked until the lock is released. This provides strong guarantees but may reduce system performance.

**Advisory Locking**: Processes are expected to check for locks before accessing the file, but the operating system does not enforce these locks. This approach relies on cooperation among processes and is less reliable but offers more flexibility.

**Shared Locks (Read Locks)**: Multiple processes can hold shared locks simultaneously, as they only permit reading. This allows concurrent read access while preventing any modifications.

**Exclusive Locks (Write Locks)**: Only one process can hold an exclusive lock at a time, and no other locks (shared or exclusive) can be granted until the exclusive lock is released. This ensures complete control over the file for modification purposes.

### Implementing File Locks

Operating systems provide system calls for file locking. The UNIX operating system offers the flock() system call for advisory locking and fcntl() for more sophisticated locking operations including mandatory locks. Windows provides the LockFile() and LockFileEx() functions for similar purposes.

The typical sequence for accessing a file with locking involves:
1. Opening the file to obtain a file descriptor
2. Acquiring the appropriate lock (shared or exclusive)
3. Performing the required read or write operations
4. Releasing the lock
5. Closing the file

### File Sharing in Distributed Systems

In distributed computing environments, file sharing becomes more complex as files may be located on different machines connected through a network. Distributed file systems like NFS (Network File System), SMB (Server Message Block), and cloud storage solutions implement file sharing across network boundaries.

Distributed file sharing introduces additional challenges:
- Network latency affecting lock acquisition and release
- Need for cache coherence to ensure all clients see consistent file contents
- Handling network partitions and communication failures
- Security concerns in transmitting file data over networks

## Examples

### Example 1: Bank Account Update Problem

Consider a banking system where two tellers simultaneously process withdrawals from the same account file containing a balance of Rs. 10,000. Both tellers read the balance, calculate the new balance after their respective withdrawals (Rs. 8,000 and Rs. 7,000), and write back the result.

WITHOUT proper file locking:
1. Teller 1 reads balance: Rs. 10,000
2. Teller 2 reads balance: Rs. 10,000 (before Teller 1 writes)
3. Teller 1 writes new balance: Rs. 8,000
4. Teller 2 writes new balance: Rs. 7,000

The final balance is Rs. 7,000 instead of the correct Rs. 6,000 (Rs. 10,000 - Rs. 2,000 - Rs. 2,000). The first withdrawal of Rs. 2,000 has been lost due to the race condition.

WITH proper file locking (exclusive lock):
1. Teller 1 acquires exclusive lock on account file
2. Teller 1 reads balance: Rs. 10,000
3. Teller 1 writes new balance: Rs. 8,000
4. Teller 1 releases lock
5. Teller 2 acquires exclusive lock (now available)
6. Teller 2 reads balance: Rs. 8,000
7. Teller 2 writes new balance: Rs. 6,000
8. Teller 2 releases lock

The final balance is correctly Rs. 6,000, demonstrating how file locking prevents lost updates.

### Example 2: Read-Write Lock Implementation

A text editor application allows multiple users to view a document simultaneously, but only one user should be able to edit it at a time. The file system implements read-write locks to achieve this:

```
Process A (User 1 wants to view):
  Acquire shared lock on document.txt
  Read contents
  Release shared lock

Process B (User 2 wants to view):
  Acquire shared lock on document.txt (SUCCESS - shared locks allow concurrent readers)
  Read contents
  Release shared lock

Process C (User 3 wants to edit):
  Acquire exclusive lock on document.txt
  (BLOCKED - shared locks are still held by A and B)
  
Process A and B finish reading, release shared locks
  
Process C (now acquires exclusive lock):
  Modify contents
  Release exclusive lock
```

This example demonstrates how shared locks enable concurrent read access while exclusive locks serialize write access, ensuring that only one user can modify the document at a time.

### Example 3: Database Record Locking

In a student records system, suppose the administrator needs to update a student's email address while a faculty member needs to read the same student's grade record. Since these operations access different parts of the file (email field vs. grade field), the system could implement record-level locking instead of file-level locking for better concurrency.

However, if both operations attempted to update the same field (e.g., both trying to modify the grade), the record lock would ensure serialized access. Record locking provides finer granularity control compared to file locking, allowing more concurrent access in scenarios where processes access different portions of the same file.

## Exam Tips

For DU semester examinations, the following points are essential for the File Sharing topic:

1. Understand the fundamental difference between shared locks and exclusive locks. Shared locks allow concurrent reading but prevent writing, while exclusive locks prevent both reading and writing by other processes.

2. Be able to explain why file sharing is necessary in multi-user operating systems and the problems that arise without proper synchronization mechanisms.

3. Know the definitions and consequences of race conditions, deadlock, and starvation in the context of file access. The examiner frequently asks for definitions with examples.

4. Understand the distinction between mandatory and advisory locking, including their advantages and disadvantages. Mandatory locking provides stronger guarantees but at the cost of flexibility.

5. Be familiar with the typical sequence of operations when implementing file locking: open, lock, access, unlock, close. This sequence is often asked in practical scenarios.

6. Know how file sharing differs in distributed systems compared to single-machine systems, particularly regarding cache coherence and network-related issues.

7. Understand the concept of granularity in locking - file-level locks versus record-level locks - and explain when each is appropriate.

8. Be prepared to solve problems involving concurrent file access, such as determining the final state of a file after multiple operations or identifying potential race conditions in given scenarios.