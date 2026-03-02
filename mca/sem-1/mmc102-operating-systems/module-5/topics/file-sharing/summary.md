# File Sharing in Operating Systems - Summary

## Key Definitions

- **File Sharing**: Concurrent access to files by multiple users or processes in a computer system
- **File Locking**: Synchronization mechanism controlling access to files by preventing conflicting operations
- **Advisory Lock**: A cooperative lock that requires processes to voluntarily check for locks before accessing files
- **Mandatory Lock**: A lock enforced by the operating system kernel that actively prevents conflicting access
- **Shared Lock (Read Lock)**: Lock type that permits multiple processes to read a file simultaneously
- **Exclusive Lock (Write Lock)**: Lock type that permits only one process to access the file for writing
- **Race Condition**: Undesirable situation where system behavior depends on timing of concurrent events

## Important Formulas

- **Lock Compatibility Matrix**:
- Shared + Shared = Compatible (both can read)
- Shared + Exclusive = Incompatible (write blocks reads)
- Exclusive + Exclusive = Incompatible (only one writer)

## Key Points

1. File sharing enables collaboration and resource efficiency in multi-process systems but requires careful synchronization to maintain data integrity.

2. File locking is the primary mechanism for controlling concurrent file access, with two main variants: mandatory (kernel-enforced) and advisory (cooperative).

3. The readers-writers problem models file sharing scenarios where multiple readers can access concurrently but writers need exclusive access.

4. Race conditions in file operations can lead to data corruption, lost updates, and inconsistent file states.

5. Operating systems use various techniques to prevent race conditions including atomic operations, file leasing, and transactional semantics.

6. Access control mechanisms (permissions, ACLs) regulate which users can access files and in what modes.

7. Deadlock can occur in file locking scenarios when processes acquire locks in different orders on multiple files.

8. Network file systems like NFS extend file sharing across distributed systems, introducing additional challenges related to consistency and lock management.

## Common Mistakes

1. **Confusing file sharing with access methods**: Students often mistake sequential vs. direct access (access methods) for concurrent access (file sharing). They are distinct concepts.

2. **Assuming locks always prevent corruption**: Advisory locks only work if all processes check locks; a non-compliant process can still cause corruption.

3. **Ignoring deadlock possibilities**: When locking multiple files, always acquire locks in a consistent global order to prevent circular wait conditions.

4. **Overlooking lock granularity**: Locking entire files for small updates reduces concurrency unnecessarily. Record-level or byte-level locking provides finer control.

5. **Forgetting to release locks**: Failing to release locks (especially in error conditions) can cause other processes to wait indefinitely, leading to starvation or system-wide deadlocks.
