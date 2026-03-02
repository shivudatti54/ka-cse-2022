# File Sharing

## Introduction

File sharing is a fundamental concept in operating systems that addresses how multiple processes, users, or systems can access and manipulate files concurrently. In modern computing environments, where numerous processes run simultaneously and multiple users may need access to the same data, effective file sharing mechanisms become critical for system reliability and data integrity. Without proper file sharing controls, concurrent access can lead to serious problems including data corruption, inconsistent results, and race conditions that make system behavior unpredictable.

The importance of file sharing extends across various computing scenarios. In a multi-user operating system like UNIX or Windows, multiple users may need to work on the same document or data file. Similarly, in server environments, hundreds or thousands of client processes may simultaneously request access to shared files. Database management systems heavily rely on sophisticated file sharing mechanisms to ensure ACID (Atomicity, Consistency, Isolation, Durability) properties. Even in single-user systems, background processes, applications, and the operating system itself frequently need to share access to system files, configuration data, and log files.

This topic explores the theoretical foundations and practical implementations of file sharing mechanisms in operating systems. We will examine the problems that arise from concurrent file access, the solutions operating systems employ, and the trade-offs involved in different approaches. Understanding these concepts is essential for anyone studying operating system design and implementation, as file sharing touches upon fundamental issues of process synchronization, resource management, and system security.

## Key Concepts

### The File Sharing Problem

When multiple processes access a file concurrently, several problematic scenarios can arise. Consider two processes attempting to write to the same file simultaneously. Without coordination, the final content of the file depends entirely on the timing of these operations, a situation known as a race condition. Process A might write "Hello" while Process B writes "World," and depending on execution order, the file could contain either string, both concatenated in either order, or worse, a corrupted mix of interleaved characters if write operations are not atomic.

Read operations also present challenges. If one process is modifying a file while another reads from it, the reader might obtain partially updated data, a state known as inconsistent read. For instance, if a file contains a database record being updated, a reader might see some fields with old values and others with new values, resulting in logically incorrect data.

The fundamental challenge is that file operations that appear atomic to users (like writing a complete record) often involve multiple底层 operations at the system level. A write operation might involve locating free space, updating file metadata, writing the actual data, and updating directory structures. If another process intervenes between these steps, serious inconsistencies can result.

### Types of File Access

Understanding the nature of access required is crucial for implementing appropriate sharing mechanisms. Operating systems typically distinguish between several types of file access.

Exclusive access, also known as write access or deny-write access, ensures that only one process can access the file at a time. When a process opens a file with exclusive access, all other processes attempting to open the same file receive an error until the first process closes the file. This approach is simple but limits concurrency significantly.

Shared access allows multiple processes to simultaneously open the same file. However, this requires明确规定 how reads and writes interact. Shared read access means multiple processes can read the file simultaneously without interference, as reads do not modify file content. Shared write access, where multiple processes can simultaneously modify the file, requires careful coordination to prevent corruption.

The combination of access types determines the sharing mode. A process might request read-only shared access, write-only shared access, or read-write shared access. The operating system must enforce these access semantics while preventing unauthorized operations.

### File Locking Mechanisms

Operating systems provide file locking mechanisms to coordinate concurrent access. These mechanisms can be classified into two categories: mandatory locks and advisory locks.

Mandatory locks are enforced by the operating system kernel. When a process acquires a mandatory lock on a file, the system prevents any other process from accessing the file in violation of that lock. If Process A holds a mandatory write lock on a file and Process B attempts to write to that file, the operating system blocks Process B's operation or returns an error. Mandatory locks provide strong guarantees but consume system resources and can lead to deadlock if not carefully managed.

Advisory locks are a cooperative mechanism where processes agree to check for locks before accessing files. The operating system provides lock primitives (like flock in UNIX or LockFile in Windows) but does not forcibly prevent access to files that are not locked. Processes must voluntarily check for locks and respect them. While this approach is more flexible and allows for more efficient resource use in well-behaved applications, it provides no protection against uncooperative processes.

The POSIX standard defines the fcntl (file control) system call for advisory locking, with flock for simpler whole-file locking. Windows provides LockFileEx for exclusive locks and shared locks through the CreateFile function with specific flags.

### Concurrency Control in File Systems

Modern file systems employ various techniques to manage concurrent access at different levels of granularity.

Record locking provides fine-grained control over portions of a file. Rather than locking the entire file, processes can lock specific byte ranges or logical records within the file. This allows greater concurrency when different processes need to modify different parts of the same file. Record locks are particularly important in database systems where different transactions might modify different database rows within the same file.

Timestamp-based concurrency control records when files were last modified. Some systems use timestamps to detect whether files have changed since they were last accessed, though this approach has limitations in high-concurrency environments where changes might occur between checking and using the file.

Optimistic concurrency control assumes conflicts are rare and allows operations to proceed. If a conflict is detected when committing changes (such as another process modifying the file), the operation fails and must be retried. This approach works well when contention is low but can lead to repeated failures under heavy load.

Pessimistic concurrency control assumes conflicts are likely and obtains necessary locks before beginning operations. While this approach prevents conflicts, it can reduce throughput and requires careful deadlock prevention.

### Issues in File Sharing

Several specific issues arise in file sharing implementations that system designers must address.

Deadlock occurs when two or more processes each hold locks that the other needs. For example, if Process A holds a lock on File 1 and requests a lock on File 2, while Process B holds a lock on File 2 and requests a lock on File 1, both processes wait indefinitely. Operating systems address deadlock through prevention (ensuring at least one necessary condition for deadlock cannot occur), avoidance (carefully scheduling lock acquisition order), detection (periodically checking for deadlock states), and recovery (forcing lock release).

Starvation occurs when a process indefinitely waits for a lock because other processes continually acquire the lock first. Fair lock implementations ensure that waiting processes eventually obtain the lock, typically through queue-based lock management.

Priority inversion happens when a high-priority process waits for a lock held by a low-priority process, while medium-priority processes preempt the low-priority process, preventing it from releasing the lock. Solutions include priority inheritance (temporarily elevating the low-priority process's priority) and priority ceiling protocols.

## Examples

### Example 1: Implementing a Write Lock in UNIX

Consider a scenario where multiple processes need to write to a shared log file. We can implement exclusive write access using the flock system call.

```c
#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/file.h>

void write_to_log(const char *filename, const char *message) {
    int fd = open(filename, O_WRONLY | O_CREAT | O_APPEND, 0644);
    if (fd == -1) {
        perror("Failed to open log file");
        return;
    }
    
    // Acquire exclusive lock
    if (flock(fd, LOCK_EX) == -1) {
        perror("Failed to acquire lock");
        close(fd);
        return;
    }
    
    // Write message (safe from interference)
    write(fd, message, strlen(message));
    
    // Release lock
    flock(fd, LOCK_UN);
    close(fd);
}
```

The LOCK_EX flag requests an exclusive lock, blocking until the lock becomes available. The lock is automatically released when the file descriptor is closed, but explicitly releasing with LOCK_UN before closing is good practice.

### Example 2: Shared Read with Record Locking

In a database scenario, multiple processes might need to read different records while one process updates a specific record. Using POSIX fcntl for record locking:

```c
#include <fcntl.h>
#include <unistd.h>
#include <sys/file.h>

struct Record {
    int id;
    char data[256];
};

void read_record(int fd, int record_number, struct Record *buf) {
    struct flock lock;
    off_t offset = record_number * sizeof(struct Record);
    
    // Set up shared lock for reading
    lock.l_type = F_RDLCK;    // Shared lock
    lock.l_whence = SEEK_SET;
    lock.l_start = offset;
    lock.l_len = sizeof(struct Record);
    lock.l_pid = getpid();
    
    // Acquire read lock
    if (fcntl(fd, F_SETLKW, &lock) == -1) {
        perror("Failed to acquire read lock");
        return;
    }
    
    // Perform read
    pread(fd, buf, sizeof(struct Record), offset);
    
    // Release lock
    lock.l_type = F_UNLCK;
    fcntl(fd, F_SETLK, &lock);
}

void update_record(int fd, int record_number, const struct Record *buf) {
    struct flock lock;
    off_t offset = record_number * sizeof(struct Record);
    
    // Set up exclusive lock for writing
    lock.l_type = F_WRLCK;    // Exclusive lock
    lock.l_whence = SEEK_SET;
    lock.l_start = offset;
    lock.l_len = sizeof(struct Record);
    lock.l_pid = getpid();
    
    // Acquire write lock
    if (fcntl(fd, F_SETLKW, &lock) == -1) {
        perror("Failed to acquire write lock");
        return;
    }
    
    // Perform write
    pwrite(fd, buf, sizeof(struct Record), offset);
    
    // Release lock
    lock.l_type = F_UNLCK;
    fcntl(fd, F_SETLK, &lock);
}
```

This implementation allows multiple simultaneous readers but ensures exclusive access for writers, preventing readers from seeing partially updated records.

### Example 3: Handling Lock Conflicts Gracefully

A robust file sharing implementation should handle lock failures gracefully rather than blocking indefinitely:

```c
#include <fcntl.h>
#include <unistd.h>
#include <errno.h>
#include <time.h>

int acquire_write_lock_with_timeout(int fd, int timeout_seconds) {
    struct flock lock;
    lock.l_type = F_WRLCK;
    lock.l_whence = SEEK_SET;
    lock.l_start = 0;
    lock.l_len = 0;  // Entire file
    lock.l_pid = getpid();
    
    time_t start_time = time(NULL);
    
    while (1) {
        // Try to acquire lock (non-blocking)
        int result = fcntl(fd, F_SETLK, &lock);
        
        if (result != -1) {
            return 0;  // Lock acquired successfully
        }
        
        if (errno != EACCES && errno != EAGAIN) {
            return -1;  // Unexpected error
        }
        
        // Check for timeout
        if (time(NULL) - start_time >= timeout_seconds) {
            return -2;  // Timeout
        }
        
        // Wait before retrying
        sleep(1);
    }
}
```

This function attempts non-blocking lock acquisition and retries until either the lock is obtained or a timeout expires. The calling code can then handle timeout situations appropriately, perhaps by returning an error to the user or queuing the request for later processing.

## Exam Tips

For DU semester examinations on operating systems, the following points are essential for the file sharing topic.

Understanding the difference between mandatory and advisory locks is crucial. Mandatory locks are enforced by the operating system kernel and prevent all access to locked files, while advisory locks are cooperative and require processes to voluntarily check and respect locks. In exam questions, if a scenario involves potentially misbehaving processes, mandatory locks provide stronger guarantees.

The concept of race conditions in file access is frequently tested. Be prepared to explain how concurrent writes can corrupt file content and how file locking prevents such corruption. Understand that even seemingly atomic operations like writing a record might involve multiple底层 system calls that another process could interleave with.

Be familiar with the types of file locks: shared locks (read locks) and exclusive locks (write locks). Multiple processes can hold shared locks simultaneously, but no exclusive lock can be granted while any shared lock exists. Conversely, an exclusive lock prevents any other lock from being granted.

The problems of deadlock, starvation, and priority inversion in the context of file locking are important. Understand how lock ordering can prevent deadlock (acquire locks in a consistent global order) and how priority inheritance solves priority inversion.

The difference between whole-file locking (flock) and record-level locking (fcntl with fcntl) is worth knowing. Whole-file locking is simpler but limits concurrency; record locking allows finer-grained access but is more complex to implement correctly.

Know the POSIX system calls for file locking: flock for whole-file advisory locks, fcntl for record-level advisory locks, and the lock types F_RDLCK, F_WRLCK, and F_UNLCK. Windows equivalents like LockFileEx and CreateFile might appear in questions about cross-platform systems.

The concept of access modes in file opening (O_RDONLY, O_WRONLY, O_RDWR) relates to file sharing because these modes determine what operations are permitted on an open file descriptor, which interacts with locking mechanisms.