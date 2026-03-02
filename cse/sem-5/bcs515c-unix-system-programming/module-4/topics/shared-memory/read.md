# Shared Memory Inter-Process Communication

## Introduction

Shared memory is one of the most efficient mechanisms for Inter-Process Communication (IPC) in operating systems. Unlike other IPC methods such as pipes or message queues, shared memory allows multiple processes to access a common memory region directly, without involving the kernel for data transfer. This direct access capability makes shared memory the fastest form of IPC available in modern operating systems.

In the context of 's Operating Systems curriculum, shared memory represents a fundamental concept that demonstrates how processes can cooperate and exchange data efficiently. The mechanism is particularly important because it enables processes to share large amounts of data with minimal overhead. Understanding shared memory is essential for developing concurrent applications and solving critical synchronization problems in multi-process systems.

This topic builds upon the foundational concepts of processes, threads, and basic IPC mechanisms. It introduces both the theoretical principles and practical implementation aspects using System V shared memory and POSIX shared memory interfaces that are widely used in Unix/Linux environments.

## Key Concepts

### Fundamentals of Shared Memory

Shared memory is a memory region that is mapped into the address spaces of two or more processes. When a process writes data to this shared region, other processes can immediately read that data without any additional system calls for data transfer. The operating system only intervenes to establish the shared memory mapping and manage the memory protection attributes.

The basic workflow involves:

1. Creating or opening a shared memory segment
2. Attaching the shared memory segment to the process's address space
3. Reading from or writing to the shared memory
4. Detaching the shared memory segment from the address space
5. Removing the shared memory segment when no longer needed

### System V Shared Memory

System V IPC provides a standardized interface for shared memory operations in Unix systems. The following system calls are used:

**shmget()** - Creates or accesses a shared memory segment

```c
int shmget(key_t key, size_t size, int shmflg);
```

- `key`: Unique identifier for the shared memory segment (can be generated using ftok())
- `size`: Size of the shared memory segment in bytes
- `shmflg`: Permissions (IPC_CREAT, IPC_EXCL, mode flags)

**shmat()** - Attaches shared memory to the process address space

```c
void *shmat(int shmid, const void *shmaddr, int shmflg);
```

- `shmid`: Shared memory identifier returned by shmget()
- `shmaddr`: Specific address (usually set to NULL for automatic placement)
- `shmflg`: Attachment flags (SHM_RDONLY for read-only)

**shmdt()** - Detaches shared memory from the process address space

```c
int shmdt(const void *shmaddr);
```

**shmctl()** - Performs control operations on shared memory

```c
int shmctl(int shmid, int cmd, struct shmid_ds *buf);
```

- Common commands: IPC_STAT (get status), IPC_SET (set parameters), IPC_RMID (remove segment)

### POSIX Shared Memory

POSIX shared memory provides a more modern and simpler interface using file-based operations:

**shm_open()** - Creates or opens a shared memory object

```c
int shm_open(const char *name, int oflag, mode_t mode);
```

**ftruncate()** - Sets the size of the shared memory object

```c
int ftruncate(int fd, off_t length);
```

**mmap()** - Maps the shared memory object into memory

```c
void *mmap(void *addr, size_t len, int prot, int flags, int fd, off_t offset);
```

**shm_unlink()** - Removes the shared memory object

```c
int shm_unlink(const char *name);
```

### Synchronization in Shared Memory

Since multiple processes can access shared memory concurrently, synchronization becomes critical to prevent race conditions and ensure data consistency. The following mechanisms are used:

**Semaphores**: System V semaphores (semget, semop, semctl) or POSIX semaphores (sem_init, sem_wait, sem_post) provide atomic operations for synchronization.

**Mutexes**: POSIX mutexes can be used within threaded processes or memory-mapped files for mutual exclusion.

**File Locks**: flock() can be used for simple locking mechanisms.

### Producer-Consumer Problem with Shared Memory

This classic synchronization problem demonstrates shared memory usage:

- Producer process creates data and stores it in shared buffer
- Consumer process reads and processes data from shared buffer
- Circular buffer implementation with count tracking
- Empty and full conditions managed using semaphores

## Examples

### Example 1: System V Shared Memory Implementation

**Server Process (Writer):**

```c
#include <stdio.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <string.h>

int main() {
 key_t key = ftok("/tmp", 'A'); // Generate unique key
 int shmid = shmget(key, 1024, IPC_CREAT | 0666); // Create shared memory

 char *str = (char*) shmat(shmid, NULL, 0); // Attach to memory
 strcpy(str, "Hello from Server Process!"); // Write data

 printf("Data written to shared memory: %s\n", str);

 sleep(10); // Keep data available for client
 shmdt(str); // Detach from memory

 shmctl(shmid, IPC_RMID, NULL); // Remove shared memory
 return 0;
}
```

**Client Process (Reader):**

```c
#include <stdio.h>
#include <sys/ipc.h>
#include <sys/shm.h>

int main() {
 key_t key = ftok("/tmp", 'A'); // Same key as server
 int shmid = shmget(key, 1024, 0666); // Access existing memory

 char *str = (char*) shmat(shmid, NULL, SHM_RDONLY); // Read-only attach

 printf("Data read from shared memory: %s\n", str);

 shmdt(str); // Detach from memory
 return 0;
}
```

### Example 2: POSIX Shared Memory with Memory Mapping

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <sys/mman.h>
#include <unistd.h>

#define SHM_NAME "/my_shared_memory"
#define SHM_SIZE 256

int main() {
 // Create shared memory object
 int shm_fd = shm_open(SHM_NAME, O_CREAT | O_RDWR, 0666);
 if (shm_fd == -1) {
 perror("shm_open");
 exit(1);
 }

 // Set the size of the shared memory object
 ftruncate(shm_fd, SHM_SIZE);

 // Map the shared memory object into memory
 void *ptr = mmap(0, SHM_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, shm_fd, 0);
 if (ptr == MAP_FAILED) {
 perror("mmap");
 exit(1);
 }

 // Write data to shared memory
 sprintf((char*)ptr, "POSIX Shared Memory Example - Process ID: %d", getpid());
 printf("Written to shared memory: %s\n", (char*)ptr);

 // Clean up
 munmap(ptr, SHM_SIZE);
 close(shm_fd);
 shm_unlink(SHM_NAME);

 return 0;
}
```

### Example 3: Shared Memory with Semaphore Synchronization

```c
#include <stdio.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <sys/sem.h>
#include <unistd.h>

union semun {
 int val;
 struct semid_ds *buf;
 unsigned short *array;
};

void sem_lock(int semid) {
 struct sembuf sb = {0, -1, 0};
 semop(semid, &sb, 1);
}

void sem_unlock(int semid) {
 struct sembuf sb = {0, 1, 0};
 semop(semid, &sb, 1);
}

int main() {
 // Create shared memory
 int shmid = shmget(IPC_PRIVATE, sizeof(int), IPC_CREAT | 0666);
 int *counter = (int*) shmat(shmid, NULL, 0);
 *counter = 0;

 // Create semaphore for synchronization
 int semid = semget(IPC_PRIVATE, 1, IPC_CREAT | 0666);
 union semun arg;
 arg.val = 1;
 semctl(semid, 0, SETVAL, arg);

 // Fork child process
 pid_t pid = fork();

 if (pid == 0) {
 // Child process
 for (int i = 0; i < 1000; i++) {
 sem_lock(semid);
 (*counter)++;
 sem_unlock(semid);
 }
 shmdt(counter);
 } else {
 // Parent process
 for (int i = 0; i < 1000; i++) {
 sem_lock(semid);
 (*counter)++;
 sem_unlock(semid);
 }
 wait(NULL);
 printf("Final counter value: %d\n", *counter);
 shmdt(counter);
 shmctl(shmid, IPC_RMID, NULL);
 semctl(semid, 0, IPC_RMID);
 }

 return 0;
}
```

## Exam Tips

1. **Know the difference between System V and POSIX shared memory**: System V uses shmget/shmat/shmdt/shmctl, while POSIX uses shm_open/mmap. Understand when to use each approach.

2. **Understand key generation using ftok()**: Remember that ftok() generates a unique key from a pathname and project identifier, essential for related processes to access the same shared memory segment.

3. **Remember the attachment flags**: SHM_RDONLY makes the memory read-only, and shmaddr can be NULL for automatic address selection by the system.

4. **Always detach and remove shared memory**: Failing to call shmdt() can cause memory leaks, and not removing shared memory with IPC_RMID leaves orphan segments in the system.

5. **Synchronization is mandatory**: In exams, always mention using semaphores or mutexes when multiple processes access shared memory to prevent race conditions.

6. **Understand the difference between IPC_PRIVATE and public keys**: IPC_PRIVATE creates a private segment, while public keys allow unrelated processes to share memory.

7. **Know the advantages of shared memory**: Highest performance among IPC mechanisms, direct data access without copying, suitable for large data transfers.

8. **Common exam question patterns**: Be prepared to write code for creating/accessing shared memory, explain the working of shmget() and shmat(), and solve producer-consumer problems using shared memory with semaphores.

9. **Memory mapping benefits**: Understand how mmap() provides memory-mapped I/O and its advantages over traditional file read/write operations.

10. **Practice diagram-based questions**: Be able to draw and explain the process of shared memory attachment and detachment in the address space.
