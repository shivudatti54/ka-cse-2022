# System V IPC - Summary

## Key Definitions and Concepts

- **IPC (Inter-Process Communication)**: Mechanisms allowing processes to communicate and synchronize
- **System V IPC**: AT&T's standardized IPC framework with three primary mechanisms
- **IPC Key (key_t)**: Unique identifier for IPC objects, generated using ftok()
- **IPC Identifier**: Unique handle returned by IPC creation functions (msgqid, shmid, semid)

## Important Formulas and Functions

**Message Queues:**

- `key_t ftok(const char *pathname, int proj_id)` - Generate IPC key
- `int msgget(key_t key, int msgflg)` - Create/access queue
- `int msgsnd(int msqid, const void *msgp, size_t msgsz, int msgflg)` - Send message
- `ssize_t msgrcv(int msqid, void *msgp, size_t msgsz, long msgtyp, int msgflg)` - Receive message
- `int msgctl(int msqid, int cmd, struct msqid_ds *buf)` - Control operations

**Shared Memory:**

- `int shmget(key_t key, size_t size, int shmflg)` - Create/access shared memory
- `void *shmat(int shmid, const void *shmaddr, int shmflg)` - Attach memory
- `int shmdt(const void *shmaddr)` - Detach memory
- `int shmctl(int shmid, int cmd, struct shmid_ds *buf)` - Control operations

**Semaphores:**

- `int semget(key_t key, int nsems, int semflg)` - Create semaphore array
- `int semop(int semid, struct sembuf *sops, size_t nsops)` - Perform operations
- `int semctl(int semid, int semnum, int cmd, ...)` - Control operations

## Key Points

- Message queues enable asynchronous message passing with message types
- Shared memory provides fastest IPC by avoiding data copying
- Semaphores synchronize process access to shared resources
- ftok() generates consistent keys from same pathname and proj_id
- IPC_NOWAIT flag makes operations non-blocking
- IPC_RMID command removes IPC objects permanently
- IPC_CREAT creates object if it doesn't exist; IPC_EXCL fails if it exists
- Message structure must have `long mtype` as first field
- shmat() returns (void\*)-1 on failure, not NULL
- sem_op negative = wait(P), positive = signal(V)

## Common Mistakes to Avoid

1. Forgetting to check return values of IPC system calls for errors
2. Not removing IPC objects after use, leading to resource leaks
3. Using wrong message type in msgrcv() causing wrong message retrieval
4. Confusing shared memory attachment and detachment operations
5. Not initializing semaphores before use in semget()

## Revision Tips

1. Practice writing complete sender-receiver programs using message queues
2. Memorize the function signatures and purpose of all 10 IPC functions
3. Understand the flags: IPC_CREAT, IPC_EXCL, IPC_NOWAIT, SEM_UNDO
4. Use `ipcs` command to verify IPC objects in system
5. Review semaphore operations for process synchronization scenarios
