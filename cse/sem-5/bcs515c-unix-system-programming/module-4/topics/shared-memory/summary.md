# Shared Memory IPC - Summary

## Key Definitions and Concepts

- **Shared Memory**: A region of physical memory that is mapped into the address spaces of multiple processes, allowing direct data exchange without kernel intervention.
- **IPC (Inter-Process Communication)**: Mechanisms that allow processes to communicate and synchronize their actions.
- **Memory Mapping**: Technique where file contents are mapped to process address space using mmap().
- **Race Condition**: Occurs when multiple processes access shared data concurrently without proper synchronization.

## Important Formulas and Theorems

- **ftok()**: key = ftok(pathname, project_id) - Generates unique System V IPC key
- **shmget()**: Creates shared memory segment with permissions
- **shmat()**: Attaches shared memory, returns pointer to attached address
- **shmctl()**: Controls shared memory operations (status, removal)
- **shm_open()**: POSIX function to create/open shared memory object
- **mmap()**: Maps files or shared memory objects into process address space

## Key Points

- Shared memory is the fastest form of IPC as data is transferred directly between processes without kernel mediation.
- System V shared memory uses integer identifiers (shmid), while POSIX uses file-based names.
- Always use synchronization (semaphores/mutexes) when multiple processes access shared memory to prevent data inconsistency.
- shmdt() must be called before process termination to detach from shared memory.
- shmctl(shmid, IPC_RMID, NULL) removes the shared memory segment permanently.
- The ftok() function requires an existing file path to generate a consistent key across processes.
- Shared memory is suitable for large data transfers where performance is critical.
- Memory protection can be set using PROT_READ, PROT_WRITE, PROT_EXEC flags in mmap().

## Common Mistakes to Avoid

1. **Forgetting to detach memory**: Always call shmdt() or munmap() before process exits to prevent memory leaks.
2. **Not using synchronization**: Accessing shared memory without semaphores causes undefined behavior due to race conditions.
3. **Incorrect key generation**: Using different paths in ftok() results in different keys, preventing process communication.
4. **Ignoring return values**: Checking return values helps catch errors like permission denied or invalid identifiers.
5. **Creating memory with wrong size**: Allocating insufficient size leads to buffer overflow when writing data.

## Revision Tips

1. Practice writing complete producer-consumer code using shared memory and semaphores.
2. Memorize the sequence: create → attach → use → detach → remove.
3. Compare System V vs POSIX shared memory in tabular format for quick recall.
4. Understand how ftok() generates keys from path and character.
5. Review previous year exam questions on shared memory IPC.
6. Draw memory layout diagrams showing shared memory attachment in process address space.
