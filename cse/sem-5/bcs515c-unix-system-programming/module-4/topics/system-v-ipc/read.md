# System V IPC (Inter-Process Communication)

## Introduction

System V IPC is a fundamental concept in Unix System Programming that provides mechanisms for processes to communicate and synchronize with each other. Developed by AT&T's System V, this IPC framework offers three primary mechanisms: Message Queues, Shared Memory, and Semaphores. These mechanisms enable multiple processes to exchange data, share resources, and coordinate their activities in a controlled manner.

In modern computing, where multi-process applications are common, understanding System V IPC is crucial for developing robust and efficient Unix-based applications. Whether it's a client-server architecture, producer-consumer problem, or multi-threaded application requiring synchronization, System V IPC provides the primitives needed to implement these solutions. This topic carries significant weight in university examinations, with practical questions frequently appearing in both theory and lab components.

## Key Concepts

### 1. IPC Keys and Identifiers

Every System V IPC object is identified by a unique key (key_t), which is a positive integer. The `ftok` function generates a key from a pathname and a project identifier:

```c
key_t ftok(const char *pathname, int proj_id);
```

Each IPC mechanism uses a different type of identifier:

- Message Queues: `msgqid` (message queue identifier)
- Shared Memory: `shmid` (shared memory identifier)
- Semaphores: `semid` (semaphore identifier)

### 2. Message Queues

Message queues allow processes to send and receive messages organized by type. They provide a buffered communication mechanism where messages are stored in a queue until retrieved.

**Data Structures:**

The `msgbuf` structure must be defined by the programmer with the first field being `long mtype`:

```c
struct msgbuf {
 long mtype; /* Message type */
 char mtext[256]; /* Message data */
};
```

**Key Functions:**

- `msgget`: Creates or accesses a message queue

```c
int msgget(key_t key, int msgflg);
```

Flags: IPC_CREAT, IPC_EXCL, 0666 (permissions)

- `msgsnd`: Sends a message to the queue

```c
int msgsnd(int msqid, const void *msgp, size_t msgsz, int msgflg);
```

Flags: IPC_NOWAIT (non-blocking)

- `msgrcv`: Receives a message from the queue

```c
ssize_t msgrcv(int msqid, void *msgp, size_t msgsz, long msgtyp, int msgflg);
```

msgtyp: 0 (first message), >0 (first of type), <0 (type <= |msgtyp|)

- `msgctl`: Performs control operations

```c
int msgctl(int msqid, int cmd, struct msqid_ds *buf);
```

Commands: IPC_STAT, IPC_SET, IPC_RMID

### 3. Shared Memory

Shared memory provides the fastest IPC mechanism by allowing multiple processes to access the same memory region directly. It avoids the overhead of data copying.

**Key Functions:**

- `shmget`: Creates or accesses shared memory

```c
int shmget(key_t key, size_t size, int shmflg);
```

- `shmat`: Attaches shared memory to process address space

```c
void *shmat(int shmid, const void *shmaddr, int shmflg);
```

Flags: SHM_RDONLY (read-only), SHM_RND (round to page boundary)

- `shmdt`: Detaches shared memory

```c
int shmdt(const void *shmaddr);
```

- `shmctl`: Performs control operations

```c
int shmctl(int shmid, int cmd, struct shmid_ds *buf);
```

Commands: IPC_STAT, IPC_SET, IPC_RMID, SHM_LOCK, SHM_UNLOCK

### 4. Semaphores

Semaphores are synchronization primitives that control access to shared resources. System V semaphores are more complex than POSIX semaphores, offering semaphore arrays.

**Data Structures:**

The `sembuf` structure specifies semaphore operations:

```c
struct sembuf {
 unsigned short sem_num; /* Semaphore number */
 short sem_op; /* Operation: -1 (wait), +1 (signal) */
 short sem_flg; /* Flags: IPC_NOWAIT, SEM_UNDO */
};
```

**Key Functions:**

- `semget`: Creates or accesses semaphore array

```c
int semget(key_t key, int nsems, int semflg);
```

- `semop`: Performs semaphore operations

```c
int semop(int semid, struct sembuf *sops, size_t nsops);
```

- `semctl`: Performs control operations

```c
int semctl(int semid, int semnum, int cmd, ...);
```

Commands: GETVAL, SETVAL, GETPID, GETNCNT, GETZCNT, GETALL, SETALL, IPC_RMID

### 5. IPC Control Operations

All three IPC mechanisms support common operations through their respective control functions:

- **IPC_STAT**: Retrieve status information
- **IPC_SET**: Set ownership, permissions, and limits
- **IPC_RMID**: Remove the IPC object

The `ipcs` command displays information about IPC objects:

```bash
ipcs -q # Message queues
ipcs -m # Shared memory
ipcs -s # Semaphores
ipcs -a # All IPC objects
```

The `ipcrm` command removes IPC objects:

```bash
ipcrm -q <msgqid>
ipcrm -m <shmid>
ipcrm -s <semid>
```

## Examples

### Example 1: Message Queue - Sender Process

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/msg.h>

struct msgbuf {
 long mtype;
 char mtext[100];
};

int main {
 key_t key;
 int msgqid;
 struct msgbuf message;

 // Generate key using ftok
 key = ftok("/tmp", 'A');
 if (key == -1) {
 perror("ftok");
 exit(1);
 }

 // Create message queue
 msgqid = msgget(key, 0666 | IPC_CREAT);
 if (msgqid == -1) {
 perror("msgget");
 exit(1);
 }

 // Send messages
 printf("Enter messages (type, text):\n");
 while (scanf("%ld %s", &message.mtype, message.mtext) == 2) {
 if (msgsnd(msgqid, &message, strlen(message.mtext) + 1, 0) == -1) {
 perror("msgsnd");
 exit(1);
 }
 }

 // Remove message queue
 msgctl(msgqid, IPC_RMID, NULL);
 return 0;
}
```

### Example 2: Shared Memory - Producer-Consumer

```c
#include <stdio.h>
#include <stdlib.h>
#include <sys/shm.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <string.h>

#define SHM_SIZE 1024

int main {
 key_t key = ftok("/tmp", 'B');
 int shmid;
 char *shm_ptr;

 // Create shared memory segment
 shmid = shmget(key, SHM_SIZE, 0666 | IPC_CREAT);
 if (shmid == -1) {
 perror("shmget");
 exit(1);
 }

 // Attach to shared memory
 shm_ptr = (char *)shmat(shmid, NULL, 0);
 if (shm_ptr == (char *)-1) {
 perror("shmat");
 exit(1);
 }

 // Write data to shared memory
 printf("Enter data to write to shared memory: ");
 fgets(shm_ptr, SHM_SIZE, stdin);

 // Wait for consumer to read
 while (*shm_ptr != '\0') {
 sleep(1);
 }

 // Detach from shared memory
 shmdt(shm_ptr);

 // Remove shared memory
 shmctl(shmid, IPC_RMID, NULL);

 return 0;
}
```

### Example 3: Semaphore - Process Synchronization

```c
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/sem.h>
#include <unistd.h>

union semun {
 int val;
 struct semid_ds *buf;
 unsigned short *array;
};

int main {
 key_t key = ftok("/tmp", 'C');
 int semid;
 union semun arg;
 struct sembuf sop;

 // Create semaphore set with 1 semaphore
 semid = semget(key, 1, 0666 | IPC_CREAT);
 if (semid == -1) {
 perror("semget");
 exit(1);
 }

 // Initialize semaphore to 1
 arg.val = 1;
 if (semctl(semid, 0, SETVAL, arg) == -1) {
 perror("semctl");
 exit(1);
 }

 // Perform wait operation (P operation)
 sop.sem_num = 0;
 sop.sem_op = -1;
 sop.sem_flg = 0;

 printf("Process %d: Waiting on semaphore...\n", getpid);
 if (semop(semid, &sop, 1) == -1) {
 perror("semop");
 exit(1);
 }
 printf("Process %d: Acquired semaphore! Critical section...\n", getpid);

 // Critical section
 sleep(2);

 // Perform signal operation (V operation)
 sop.sem_op = 1;
 if (semop(semid, &sop, 1) == -1) {
 perror("semop");
 exit(1);
 }
 printf("Process %d: Released semaphore!\n", getpid);

 // Remove semaphore
 semctl(semid, 0, IPC_RMID);

 return 0;
}
```

## Exam Tips

1. **Key Generation**: Remember that `ftok` generates IPC keys from pathname and project ID. The same pathname and project ID always produce the same key.

2. **Message Queue Behavior**: For `msgrcv`, understand how msgtype affects message retrieval: 0 gets first message, positive gets first of that type, negative gets first message with type ≤ |msgtype|.

3. **Shared Memory Attachment**: The `shmat` function returns -1 on failure (cast to void*). Always check for `(void*)-1`, not NULL.

4. **Semaphore Operations**: The sem_op value determines the operation: negative for wait (P), positive for signal (V). The operation is atomic.

5. **IPC Cleanup**: Always remember to remove IPC objects using `IPC_RMID` when no longer needed to prevent resource leaks.

6. **Permission Format**: IPC permission format is similar to file permissions (owner/group/others) with read/write bits.

7. **Blocking vs Non-blocking**: Use IPC_NOWAIT flag to make operations non-blocking. Without this flag, operations may block indefinitely.

8. **Common Flags**: Remember key flags - IPC_CREAT (create if not exists), IPC_EXCL (fail if exists), 0666 (default permissions).

9. **Structure Requirements**: For message queues, the message structure must have `long mtype` as the first field.

10. **Viewing IPC Objects**: The `ipcs` command is essential for debugging and viewing active IPC objects in the system.
