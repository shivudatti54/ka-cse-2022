# File Sharing - Summary

## Key Definitions and Concepts

- **File Sharing**: Mechanisms enabling multiple processes or users to access the same file concurrently without data corruption or inconsistent results.

- **Race Condition**: Unpredictable behavior arising from non-deterministic ordering of operations when multiple processes access shared resources simultaneously.

- **File Locking**: Synchronization mechanism controlling access to files by allowing only authorized processes to access files at specific times.

- **Mandatory Locks**: Operating system-enforced locks that prevent all processes from accessing locked files, regardless of whether they check for locks.

- **Advisory Locks**: Cooperative locking where processes voluntarily check for locks before accessing files; operating system provides primitives but does not enforce compliance.

- **Shared Lock (Read Lock)**: Lock allowing multiple processes to read a file simultaneously; incompatible with exclusive locks.

- **Exclusive Lock (Write Lock)**: Lock permitting only one process to access a file; incompatible with any other lock.

## Important Formulas and Techniques

- **flock()**: UNIX system call for whole-file advisory locking with LOCK_EX (exclusive), LOCK_SH (shared), and LOCK_UN (unlock) flags.

- **fcntl()**: POSIX function for record-level locking using F_SETLK (non-blocking), F_SETLKW (blocking), F_GETLK operations with F_RDLCK and F_WRLCK lock types.

- **Lock Ordering for Deadlock Prevention**: Always acquire multiple locks in a consistent global order to prevent circular wait conditions.

## Key Points

- Concurrent file access without synchronization leads to data corruption through interleaved writes and inconsistent reads.

- Operating systems provide file locking mechanisms at both whole-file and record-level granularity.

- Shared locks allow multiple simultaneous readers; exclusive locks ensure single-writer access.

- Advisory locks require process cooperation but are more efficient; mandatory locks provide stronger guarantees but consume more system resources.

- Record locking enables finer concurrency than whole-file locking by allowing different processes to modify different portions of the same file.

- UNIX provides flock for simple whole-file locking and fcntl for more sophisticated record-level locking.

- Windows uses LockFileEx with LOCKFILE_EXCLUSIVE_FLAG for exclusive locks and separate functions for shared access.

## Common Mistakes to Avoid

- Assuming file operations are atomic at the application level when they may involve multiple system calls.

- Using non-blocking locks (F_SETLK) without proper error handling for EACCES/EAGAIN return values.

- Forgetting to release locks, especially in error handling code paths; always use goto-based cleanup or similar patterns.

- Acquiring locks in different orders in different code paths, creating potential for deadlock.

- Confusing advisory locks with mandatory locks; advisory locks do not protect against uncooperative processes.

## Revision Tips

- Practice writing code using both flock and fcntl to understand their differences and appropriate use cases.

- Review the POSIX specification for fcntl locking to understand the struct flock structure and its fields.

- Work through deadlock scenarios with lock ordering to internalize the prevention technique.

- Compare file locking approaches across operating systems (UNIX vs Windows) to understand common patterns and differences.

- Re-read the classic UNIX file locking article by John Lion for deeper insights into the design philosophy.