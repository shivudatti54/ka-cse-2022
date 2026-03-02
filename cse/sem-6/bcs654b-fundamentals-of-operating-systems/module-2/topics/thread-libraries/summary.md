# Thread Libraries - Summary

## Key Definitions and Concepts

- **Thread Library**: API for creating/managing threads (e.g., Pthreads, Windows API, Java Threads)
- **User-Level Threads (ULT)**: Managed entirely by user-space library (lightweight, OS-unaware)
- **Kernel-Level Threads (KLT)**: Managed by OS kernel (slower but enables true parallelism)
- **Pthreads**: POSIX standard thread library (implemented as ULT or KLT)
- **Mutex**: Synchronization primitive to prevent race conditions (`pthread_mutex_lock()`)
- **Joinable Thread**: Thread whose exit status can be collected via `pthread_join()`

## Important Formulas and Theorems

1. **Thread Creation (Pthreads)**

```c
int pthread_create(pthread_t *thread, const pthread_attr_t *attr,
                   void *(*start_routine)(void*), void *arg);
```

2. **Thread Termination**

```c
void pthread_exit(void *retval);
```

3. **Mutex Operations**

```c
pthread_mutex_lock(&mutex);  // Enter critical section
pthread_mutex_unlock(&mutex); // Exit critical section
```

## Key Points

1. Two main thread library types: User-level (e.g., GNU Portable Threads) vs Kernel-level (e.g., Windows Threads)
2. Pthreads uses 1:1 model (each user thread maps to kernel thread) in Linux
3. Four essential thread operations: Create, Terminate, Join, Synchronize
4. Thread synchronization requires mutexes/semaphores to protect shared resources
5. Java threads are implemented using native OS thread libraries (JVM abstraction)
6. Advantages of ULT: Faster context switching, Custom scheduling
7. Advantages of KLT: Better multiprocessor utilization, OS awareness
8. Thread pools pattern improves performance by reusing existing threads
9. Thread-safe code avoids global variables and uses reentrant functions
10. Common threading issues: Race conditions, Deadlocks, Priority inversion

## Common Mistakes to Avoid

1. **Assuming thread execution order** (OS scheduler determines order)
2. **Forgetting to join threads** → Zombie threads & resource leaks
3. **Inadequate synchronization** → Race conditions in shared data access
4. **Mixing ULT and KLT** → Can lead to "many-to-many" model complexities

## Revision Tips

1. **Code Practice**: Write 3 programs using pthreads:
   - Basic thread creation
   - Shared counter with mutex
   - Producer-consumer with semaphores
2. **Comparison Tables**: Create ULT vs KLT and Pthreads vs Windows Threads comparison charts
3. **Synchronization Focus**: Memorize mutex/semaphore functions and their usage patterns
4. **Model Diagrams**: Draw 1:1 (Pthreads), N:1 (ULT), and M:N (hybrid) threading models
