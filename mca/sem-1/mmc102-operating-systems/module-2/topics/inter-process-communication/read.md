# Inter Process Communication


## Table of Contents

- [Inter Process Communication](#inter-process-communication)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [1. Need for Inter Process Communication](#1-need-for-inter-process-communication)
  - [2. Shared Memory Model](#2-shared-memory-model)
  - [3. Message Passing Model](#3-message-passing-model)
  - [4. Pipes and FIFOs](#4-pipes-and-fifos)
  - [5. Sockets](#5-sockets)
  - [6. Signals](#6-signals)
  - [7. Semaphores and Mutexes](#7-semaphores-and-mutexes)
  - [8. Message Queues](#8-message-queues)
- [Examples](#examples)
  - [Example 1: Shared Memory Implementation](#example-1-shared-memory-implementation)
  - [Example 2: Pipe Communication Between Parent and Child](#example-2-pipe-communication-between-parent-and-child)
  - [Example 3: Producer-Consumer Problem Using Semaphores](#example-3-producer-consumer-problem-using-semaphores)
- [Exam Tips](#exam-tips)

## Introduction

Inter Process Communication (IPC) is a fundamental mechanism in operating systems that allows processes to communicate with each other and synchronize their activities. In modern computing environments, no process operates in complete isolation. Applications ranging from web servers handling concurrent requests to database systems managing transactions rely heavily on IPC mechanisms to coordinate between multiple processes. The ability to exchange data and control information between processes is essential for building robust, efficient, and scalable software systems.

Operating systems provide various IPC mechanisms to facilitate this communication. The choice of IPC mechanism depends on factors such as the relationship between processes (related or unrelated), the volume of data to be exchanged, the required speed of communication, and whether the processes reside on the same machine or different machines. Understanding these mechanisms is crucial for system programmers and software developers who design concurrent applications.

This topic covers the essential IPC mechanisms including shared memory, message passing, pipes, sockets, and synchronization primitives like semaphores and mutexes. Each mechanism has its own advantages and trade-offs, and a thorough understanding of these concepts is essential for effective system programming and for succeeding in operating system examinations.

## Key Concepts

### 1. Need for Inter Process Communication

Processes in an operating system have their own separate address spaces, which provides memory protection and isolation. However, this isolation also means that processes cannot directly access each other's memory. When processes need to share data or coordinate their actions, they must use IPC mechanisms provided by the operating system. Common scenarios requiring IPC include client-server architectures where a server process handles requests from multiple client processes, producer-consumer problems where one process generates data and another consumes it, and parallel computing where multiple processes work together to solve a problem.

### 2. Shared Memory Model

Shared memory is one of the fastest IPC mechanisms because it allows processes to access the same region of memory directly. In this model, a process creates a shared memory segment, and other processes attach this segment to their address space. Once attached, processes can read from and write to the shared memory as if it were their own memory, eliminating the overhead of data copying between address spaces.

The producer-consumer problem illustrates shared memory effectively. A producer process writes data to a shared buffer, and a consumer process reads from the same buffer. The operating system provides functions like shmget(), shmat(), shmdt(), and shmctl() in UNIX systems for creating and managing shared memory segments. However, shared memory alone does not provide synchronization; processes must use additional synchronization primitives like semaphores to prevent race conditions.

### 3. Message Passing Model

Message passing is another fundamental IPC mechanism where processes communicate by sending and receiving messages through a communication channel. Unlike shared memory, message passing involves copying data from the sender's address space to the receiver's address space through the kernel. While this introduces additional overhead, message passing provides better isolation between processes and is easier to use correctly.

Message passing can be implemented using direct or indirect communication. In direct communication, processes must explicitly name the recipient or sender of messages. In indirect communication, messages are sent to mailboxes or ports, and any process can retrieve messages from a mailbox. POSIX message queues provide a standardized interface for message passing in UNIX systems, with functions like mq_open(), mq_send(), mq_receive(), and mq_close().

### 4. Pipes and FIFOs

Pipes are one of the oldest and simplest IPC mechanisms in UNIX systems. A pipe is a unidirectional communication channel where one end is used for writing and the other end for reading. When a pipe is created, it exists only between the creating process and its child processes, making it ideal for parent-child communication.

FIFOs (First In First Out), also known as named pipes, extend the functionality of regular pipes by allowing unrelated processes to communicate. A FIFO appears as a special file in the file system, and any process can open it for reading or writing. FIFO creation is done using the mkfifo() system call, and operations are performed using standard file I/O functions like read() and write().

### 5. Sockets

Sockets provide a versatile IPC mechanism that supports both local and network communication. Originally designed for network communication between machines, sockets have become a universal endpoint for communication. UNIX domain sockets allow processes on the same machine to communicate using socket API, providing an alternative to pipes and shared memory with better abstraction.

Socket communication can be connection-oriented (using TCP) or connectionless (using UDP). TCP sockets provide reliable, ordered, error-checked delivery with flow control, while UDP sockets offer faster transmission without reliability guarantees. The socket API includes functions like socket(), bind(), listen(), accept(), connect(), send(), and recv() for establishing connections and exchanging data.

### 6. Signals

Signals are software interrupts that notify processes of specific events. While not primarily designed for data transfer, signals are essential for inter-process synchronization and control. Processes can send signals to other processes to indicate events like timer expiration, user pressing Ctrl+C, or child process termination.

Common signals include SIGTERM for graceful termination, SIGKILL for immediate termination, SIGCHLD for child process status change, and SIGALRM for timer expiration. Processes can handle signals by ignoring them, using default handlers, or installing custom signal handlers using the signal() or sigaction() system calls.

### 7. Semaphores and Mutexes

Semaphores are synchronization primitives that control access to shared resources by multiple processes. A semaphore is a counter that represents the number of available resources, and the wait() and signal() operations atomically decrement and increment this counter respectively. When the counter reaches zero, subsequent wait() operations block until another process signals the semaphore.

Mutexes (mutual exclusion locks) are a special type of semaphore restricted to binary values (0 or 1), making them ideal for protecting critical sections. Unlike semaphores, the process that locks a mutex must be the one to unlock it. POSIX semaphores provide both named and unnamed semaphore variants, with functions like sem_init(), sem_wait(), sem_post(), and sem_destroy() for unnamed semaphores.

### 8. Message Queues

Message queues allow processes to send and receive messages asynchronously. Unlike pipes which are byte-oriented, message queues support structured messages with priorities. Each message has a type that helps in selective message retrieval, and messages are stored in the queue until a receiving process retrieves them.

POSIX message queues provide a more flexible interface than traditional System V message queues. Functions like mq_open(), mq_send(), mq_receive(), and mq_close() manage message queues, while mq_getattr() and mq_setattr() allow querying and modifying queue attributes. Message queues are particularly useful in producer-consumer scenarios where the producer and consumer operate at different rates.

## Examples

### Example 1: Shared Memory Implementation

Consider a scenario where two processes need to share a counter. The producer process increments the counter, and the consumer process reads and displays it.

```
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/shm.h>
#include <sys/stat.h>

#define SHM_SIZE 1024

int main() {
    int shm_id;
    char *shm_ptr;
    key_t key = ftok("/tmp", 'A');
    
    // Create shared memory segment
    shm_id = shmget(key, SHM_SIZE, IPC_CREAT | 0666);
    if (shm_id < 0) {
        perror("shmget failed");
        exit(1);
    }
    
    // Attach to shared memory
    shm_ptr = (char *)shmat(shm_id, NULL, 0);
    if (shm_ptr == (char *)-1) {
        perror("shmat failed");
        exit(1);
    }
    
    // Write data to shared memory
    sprintf(shm_ptr, "Hello from shared memory");
    
    // Detach from shared memory
    shmdt(shm_ptr);
    
    return 0;
}
```

This example demonstrates the basic operations of shared memory: creation with shmget(), attachment with shmat(), data exchange, and detachment with shmdt(). The key generated by ftok() ensures that processes can access the same shared memory segment.

### Example 2: Pipe Communication Between Parent and Child

A classic example of pipe usage is connecting the output of one command to the input of another, similar to the shell pipe operator.

```
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

int main() {
    int pipefd[2];
    pid_t pid;
    char buffer[128];
    
    // Create pipe
    if (pipe(pipefd) == -1) {
        perror("pipe failed");
        exit(1);
    }
    
    pid = fork();
    
    if (pid < 0) {
        perror("fork failed");
        exit(1);
    }
    
    if (pid == 0) {
        // Child process - reads from pipe
        close(pipefd[1]);  // Close write end
        
        read(pipefd[0], buffer, sizeof(buffer));
        printf("Child received: %s\n", buffer);
        
        close(pipefd[0]);
    } else {
        // Parent process - writes to pipe
        close(pipefd[0]);  // Close read end
        
        const char *message = "Hello from parent";
        write(pipefd[1], message, strlen(message) + 1);
        
        close(pipefd[1]);
        wait(NULL);  // Wait for child to finish
    }
    
    return 0;
}
```

This example demonstrates how pipes enable parent-child communication. The parent writes to the write end of the pipe, and the child reads from the read end. Closing unused ends is crucial to ensure proper EOF handling when the writer closes the pipe.

### Example 3: Producer-Consumer Problem Using Semaphores

The producer-consumer problem demonstrates the use of semaphores for synchronization. Two semaphores control access to a shared buffer: one for empty slots and one for filled slots.

```
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>

#define BUFFER_SIZE 5

int buffer[BUFFER_SIZE];
int in = 0, out = 0;

sem_t empty;
sem_t full;
pthread_mutex_t mutex;

void *producer(void *arg) {
    int item;
    for (int i = 0; i < 10; i++) {
        item = rand() % 100;
        
        sem_wait(&empty);      // Wait for empty slot
        pthread_mutex_lock(&mutex);
        
        buffer[in] = item;
        printf("Producer produced: %d\n", item);
        in = (in + 1) % BUFFER_SIZE;
        
        pthread_mutex_unlock(&mutex);
        sem_post(&full);       // Signal filled slot
        
        sleep(1);
    }
    return NULL;
}

void *consumer(void *arg) {
    int item;
    for (int i = 0; i < 10; i++) {
        sem_wait(&full);       // Wait for filled slot
        pthread_mutex_lock(&mutex);
        
        item = buffer[out];
        printf("Consumer consumed: %d\n", item);
        out = (out + 1) % BUFFER_SIZE;
        
        pthread_mutex_unlock(&mutex);
        sem_post(&empty);      // Signal empty slot
        
        sleep(1);
    }
    return NULL;
}

int main() {
    pthread_t prod, cons;
    
    sem_init(&empty, 0, BUFFER_SIZE);
    sem_init(&full, 0, 0);
    pthread_mutex_init(&mutex, NULL);
    
    pthread_create(&prod, NULL, producer, NULL);
    pthread_create(&cons, NULL, consumer, NULL);
    
    pthread_join(prod, NULL);
    pthread_join(cons, NULL);
    
    sem_destroy(&empty);
    sem_destroy(&full);
    pthread_mutex_destroy(&mutex);
    
    return 0;
}
```

This example shows how semaphores coordinate access to a shared buffer. The empty semaphore counts available slots, initialized to BUFFER_SIZE. The full semaphore counts filled slots, initialized to 0. The mutex provides mutual exclusion for buffer access. This pattern ensures that the producer never overwrites the buffer and the consumer never reads from an empty buffer.

## Exam Tips

Understanding the theoretical concepts and practical implementation details of IPC mechanisms is essential for examination success. The following points highlight frequently examined concepts and common pitfalls.

FIVE marks questions frequently ask for comparisons between IPC mechanisms. Be prepared to contrast shared memory with message passing, highlighting that shared memory provides faster data transfer but requires explicit synchronization, while message passing is slower but safer due to kernel mediation. Explain the scenarios where pipes are preferred over sockets and vice versa.

SEMAPHORE operations are always examined. Remember that wait() (or P() operation) decrements the semaphore value and blocks if the value becomes negative. The signal() (or V() operation) increments the value and wakes up a waiting process if any. The atomic nature of these operations is crucial for preventing race conditions.

BLOCKING versus non-blocking operations frequently appear in exams. Read operations on pipes and sockets block until data is available. Write operations block if the buffer is full. Understanding when operations block and how to make them non-blocking using flags like O_NONBLOCK is important.

DEADLOCK prevention is a key concept in IPC design. Remember the necessary conditions for deadlock: mutual exclusion, hold and wait, no preemption, and circular wait. The producer-consumer and reader-writer problems illustrate how proper semaphore usage prevents deadlock.

KERNEL involvement varies among IPC mechanisms. In message passing, the kernel copies data from sender to receiver. In shared memory, the kernel only sets up the shared region; actual data transfer happens directly between processes. This explains why shared memory is faster for large data transfers.

SYNCHRONIZATION primitives differ in their use cases. Mutexes are for protecting critical sections within a single process or between threads. Semaphores are for resource counting and coordination between processes. Condition variables are for waiting until a certain state is reached.

The DIRECTION of communication matters. Pipes and message queues are inherently unidirectional. For bidirectional communication, two pipes or a socket pair is needed. FIFOs can be opened in read-write mode for bidirectional but this approach has complications.

SIGNAL handling is asynchronous. Remember that signal handlers should be simple and async-signal-safe. The sigaction() structure should be used instead of signal() for portable signal handling. Not all functions are safe to call from signal handlers.