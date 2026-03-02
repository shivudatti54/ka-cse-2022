# System V IPC: Message Queues, Semaphores, and Shared Memory

## Introduction to System V IPC

System V IPC (Inter-Process Communication) refers to a set of three inter-process communication mechanisms originally developed for AT&T's Unix System V. These mechanisms provide powerful ways for processes to communicate and synchronize with each other, even if they are not related through a parent-child relationship.

The three types of System V IPC are:

1. **Message Queues**: Allow processes to exchange data in the form of messages
2. **Semaphores**: Used for synchronizing processes and controlling access to shared resources
3. **Shared Memory**: Enables processes to share a segment of memory for high-speed communication

Unlike pipes and FIFOs which are byte-stream oriented, System V IPC provides structured communication methods that persist beyond the lifetime of the creating process unless explicitly removed.

## Key Concepts and Structure

### IPC Identifiers and Keys

Each IPC object (message queue, semaphore, or shared memory segment) is identified by a unique **IPC identifier** assigned by the kernel. To create or access an IPC object, processes use a **key** of type `key_t`.

```c
#include <sys/ipc.h>

// Common way to generate a key
key_t ftok(const char *pathname, int proj_id);
```

The `ftok()` function generates a key based on a pathname and project identifier. It uses the file's inode number and device number to create a unique key.

### IPC Permissions

Each IPC object has a data structure that contains permission information similar to file permissions:

```
struct ipc_perm {
    uid_t uid;   // Owner's user ID
    gid_t gid;   // Owner's group ID
    uid_t cuid;  // Creator's user ID
    gid_t cgid;  // Creator's group ID
    mode_t mode; // Permission bits
    // ...
};
```

The permission bits use the same format as file permissions: 0644 would give read/write to owner and read to group and others.

### Common IPC Operations

All three IPC mechanisms share similar system calls for control operations:

| Operation          | Message Queue | Semaphore  | Shared Memory   |
| ------------------ | ------------- | ---------- | --------------- |
| Create/Get         | `msgget()`    | `semget()` | `shmget()`      |
| Control Operations | `msgctl()`    | `semctl()` | `shmctl()`      |
| Send/Operation     | `msgsnd()`    | `semop()`  | (Memory access) |
| Receive/Operation  | `msgrcv()`    | `semop()`  | (Memory access) |

## Message Queues

Message queues allow processes to exchange data in structured messages. Each message has a type and content.

### Creating/Accessing a Message Queue

```c
#include <sys/msg.h>

int msgget(key_t key, int msgflg);
```

- `key`: IPC key or `IPC_PRIVATE` for a new queue
- `msgflg`: Permission flags combined with `IPC_CREAT` and/or `IPC_EXCL`

### Message Structure

```c
struct msgbuf {
    long mtype;     // Message type (>0)
    char mtext[1];  // Message data (variable length)
};
```

### Sending and Receiving Messages

```c
int msgsnd(int msqid, const void *msgp, size_t msgsz, int msgflg);
ssize_t msgrcv(int msqid, void *msgp, size_t msgsz, long msgtyp, int msgflg);
```

Example:

```c
// Sending a message
struct message {
    long mtype;
    char text[100];
} msg;

msg.mtype = 1;
strcpy(msg.text, "Hello World");
msgsnd(msgid, &msg, sizeof(msg.text), 0);

// Receiving a message
msgrcv(msgid, &msg, sizeof(msg.text), 1, 0);
```

### Message Queue Control

```c
int msgctl(int msqid, int cmd, struct msqid_ds *buf);
```

Common commands:

- `IPC_STAT`: Get status information
- `IPC_SET`: Set parameters
- `IPC_RMID`: Remove the message queue

## Semaphores

System V semaphores are actually **sets** of semaphores rather than individual semaphores. A semaphore set can contain multiple semaphores that are manipulated atomically.

### Creating/Accessing a Semaphore Set

```c
#include <sys/sem.h>

int semget(key_t key, int nsems, int semflg);
```

- `key`: IPC key
- `nsems`: Number of semaphores in the set
- `semflg`: Permission flags and creation options

### Semaphore Operations

```c
int semop(int semid, struct sembuf *sops, size_t nsops);
```

The `sembuf` structure:

```c
struct sembuf {
    unsigned short sem_num;  // Semaphore number in set
    short sem_op;           // Operation
    short sem_flg;          // Flags (IPC_NOWAIT, SEM_UNDO)
};
```

Common operations:

- `sem_op > 0`: Add to semaphore value (V operation)
- `sem_op == 0`: Wait for semaphore to become 0
- `sem_op < 0`: Subtract from semaphore (P operation)

### Semaphore Control

```c
int semctl(int semid, int semnum, int cmd, ... /* union semun arg */);
```

Common commands:

- `IPC_STAT`, `IPC_SET`, `IPC_RMID`: Similar to message queues
- `GETVAL`, `SETVAL`: Get/Set individual semaphore value
- `GETALL`, `SETALL`: Get/Set all semaphore values

Example of using a binary semaphore:

```c
// Initialize semaphore to 1 (unlocked)
union semun arg;
arg.val = 1;
semctl(semid, 0, SETVAL, arg);

// P operation (lock)
struct sembuf op = {0, -1, 0};
semop(semid, &op, 1);

// V operation (unlock)
op.sem_op = 1;
semop(semid, &op, 1);
```

## Shared Memory

Shared memory allows multiple processes to share a segment of memory, providing the fastest form of IPC since it avoids data copying between processes.

### Creating/Accessing Shared Memory

```c
#include <sys/shm.h>

int shmget(key_t key, size_t size, int shmflg);
```

- `key`: IPC key
- `size`: Size of shared memory segment
- `shmflg`: Permission flags and creation options

### Attaching and Detaching Shared Memory

```c
void *shmat(int shmid, const void *shmaddr, int shmflg);
int shmdt(const void *shmaddr);
```

- `shmaddr`: Usually NULL to let system choose address
- `shmflg`: `SHM_RDONLY` for read-only access

### Shared Memory Control

```c
int shmctl(int shmid, int cmd, struct shmid_ds *buf);
```

Commands are similar to other IPC mechanisms.

Example of using shared memory:

```c
// Create or get shared memory
int shmid = shmget(key, sizeof(struct data), 0644 | IPC_CREAT);

// Attach to shared memory
struct data *shared_data = shmat(shmid, NULL, 0);

// Use shared memory
shared_data->value = 42;

// Detach from shared memory
shmdt(shared_data);
```

## Comparison of IPC Mechanisms

| Feature            | Message Queues           | Semaphores               | Shared Memory            | Pipes/FIFOs       |
| ------------------ | ------------------------ | ------------------------ | ------------------------ | ----------------- |
| Relationship       | Unrelated processes      | Unrelated processes      | Unrelated processes      | Related processes |
| Communication Type | Structured messages      | Synchronization          | Raw memory access        | Byte stream       |
| Persistence        | Until explicitly removed | Until explicitly removed | Until explicitly removed | Process lifetime  |
| Speed              | Medium                   | Fast                     | Very fast                | Slow to medium    |
| Complexity         | Medium                   | High                     | Medium                   | Low               |

## IPC Status Commands

Unix provides command-line tools to examine IPC objects:

- `ipcs`: Show status of IPC facilities
- `ipcrm`: Remove IPC objects

```
$ ipcs -a  # Show all IPC objects
------ Message Queues --------
key        msqid      owner      perms      used-bytes   messages

------ Shared Memory Segments --------
key        shmid      owner      perms      bytes      nattch     status

------ Semaphore Arrays --------
key        semid      owner      perms      nsems
```

## Example: Producer-Consumer with System V IPC

```c
// Producer process
#include <stdio.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <sys/sem.h>

#define SHM_SIZE 1024

union semun {
    int val;
    struct semid_ds *buf;
    unsigned short *array;
};

int main() {
    key_t key = ftok("progfile", 65);

    // Create semaphore
    int semid = semget(key, 2, 0666 | IPC_CREAT);
    union semun arg;

    // Initialize semaphores
    arg.val = 1; // mutex
    semctl(semid, 0, SETVAL, arg);

    arg.val = 0; // empty
    semctl(semid, 1, SETVAL, arg);

    // Create shared memory
    int shmid = shmget(key, SHM_SIZE, 0666 | IPC_CREAT);
    char *str = shmat(shmid, NULL, 0);

    // Producer writes data
    sprintf(str, "Hello Consumer!");

    // Signal consumer
    struct sembuf op = {1, 1, 0}; // V operation on sem 1
    semop(semid, &op, 1);

    shmdt(str);
    return 0;
}
```

## Advantages and Disadvantages

**Advantages of System V IPC:**

- Persistence beyond process lifetime
- Can be accessed by unrelated processes
- Structured communication (message queues)
- High performance (shared memory)
- Flexible synchronization (semaphores)

**Disadvantages:**

- More complex API than pipes
- No inherent synchronization (except for message queues)
- Potential for resource leaks if not properly managed
- Limited to single system (not network transparent)

## Exam Tips

1. **Remember the common pattern**: All three mechanisms use `xxxget()`, `xxxctl()`, and operation-specific functions
2. **Key distinction**: Message queues provide structured communication, semaphores provide synchronization, shared memory provides raw speed
3. **Persistence**: System V IPC objects persist until explicitly removed or system reboot, unlike pipes
4. **Permission management**: Always set appropriate permissions (like 0644) to prevent unauthorized access
5. **Error handling**: Always check return values of IPC system calls as they can fail
6. **Cleanup**: Remember to remove IPC objects when they're no longer needed to avoid resource leaks
7. **Synchronization**: When using shared memory, you must use semaphores or other mechanisms for synchronization
8. **ftok() behavior**: Understand that `ftok()` uses inode information, so file modifications can affect key generation
