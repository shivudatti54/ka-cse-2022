# File Sharing - Summary

## Key Definitions

- **File Sharing**: The capability of multiple users or processes to access the same file concurrently
- **Advisory Locking**: Locking mechanism where processes are expected to check for locks but system does not enforce compliance
- **Mandatory Locking**: Locking mechanism enforced by the operating system at the kernel level
- **Shared Lock (Read Lock)**: Lock allowing multiple processes to read simultaneously but preventing writes
- **Exclusive Lock (Write Lock)**: Lock allowing only one process to access the file, preventing both reads and writes
- **Race Condition**: A situation where the outcome depends on the relative timing of concurrent operations
- **Deadlock**: A state where two or more processes are waiting indefinitely for each other to release resources

## Important Formulas

- **Reference Count**: Maintained in inode to track active file references; file resources freed when count reaches zero
- **Lock Compatibility Matrix**: 
  - Shared + Shared = Compatible
  - Shared + Exclusive = Incompatible
  - Exclusive + Exclusive = Incompatible

## Key Points

1. File sharing enables collaboration in multi-user systems but requires synchronization to maintain data consistency.

2. The inode structure in Unix systems uses reference counting to track file descriptors pointing to shared files.

3. Shared locks maximize read concurrency while exclusive locks ensure write serialization.

4. Advisory locking (Unix) relies on programmer cooperation, while mandatory locking (Windows) provides enforcement.

5. Unix semantics provides immediate visibility of writes, while session semantics delays visibility until file closure.

6. Race conditions occur when concurrent operations interleave in ways that produce incorrect results.

7. Deadlock requires four conditions: mutual exclusion, hold and wait, no preemption, and circular wait.

8. Proper lock ordering prevents circular wait and eliminates most deadlock scenarios in file sharing.

9. Priority inversion occurs when low-priority holders block high-priority requesters, requiring priority inheritance protocols.

10. File locking can be applied at various granularities: entire files, records, or byte ranges.

## Common Mistakes

1. **Assuming locks are always enforced**: In advisory locking systems, processes can ignore locks if they don't explicitly check for them.

2. **Neglecting lock release in error conditions**: Failing to release locks in exception handlers can cause deadlocks and resource leaks.

3. **Overusing exclusive locks**: Using exclusive locks for read operations unnecessarily reduces concurrency and system performance.

4. **Ignoring deadlock possibilities**: Not considering lock ordering when acquiring multiple locks can lead to circular wait conditions.