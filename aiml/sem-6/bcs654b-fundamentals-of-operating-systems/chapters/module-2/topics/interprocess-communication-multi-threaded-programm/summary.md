# **Interprocess Communication and Multi-threaded Programming: Overview**

## **Key Concepts**

- **Interprocess Communication (IPC)**: The ability of different processes to exchange data and coordinate with each other.
- **Inter-thread Communication**: The ability of different threads within a process to exchange data and coordinate with each other.

## **Types of IPC**

- **Synchronous Communication**: Process waits for a response before proceeding (e.g., `fork()`).
- **Asynchronous Communication**: Process continues execution without waiting for a response (e.g., `pipe()`).

## **Methods of IPC**

- **Shared Memory**: Processes share a common memory space (e.g., ` mmap()`).
- **Message Passing**: Processes exchange messages (e.g., `socket()`).
- **Semaphore**: Processes use semaphores to coordinate access to shared resources (e.g., `sem_open()`).
- **Monitors**: Processes use monitors to coordinate access to shared resources (e.g., `pthread_mutex_t`).

## **Multi-threaded Programming**

- **Thread-Safety**: Code that can be executed concurrently by multiple threads without compromising correctness.
- **Synchronization**: Mechanisms used to coordinate access to shared resources (e.g., `pthread_mutex_t`, `semaphores`).

## **Important Formulas and Definitions**

- **Pipe()**: `int pipe(fd[2], mode_t flags);`
- **Socket()**: `int socket(int domain, int type, int protocol);`
- **Sem_open()**: `int sem_open(const char *name, int flags);`
- **Monitor**: A synchronization primitive that allows one thread to execute a sequence of statements while other threads wait.

## **Theorems**

- **Derrida's Theorem**: A process can only communicate with its parent process.
- **Hartmanis's Theorem**: A process can only execute concurrently with its own children.
