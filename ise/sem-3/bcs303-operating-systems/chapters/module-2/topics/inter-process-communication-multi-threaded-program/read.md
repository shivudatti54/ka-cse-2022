# **Inter Process Communication Multi-threaded Programming: Overview**

## **Introduction**

In this module, we will explore the concepts of inter-process communication (IPC) and multi-threaded programming. IPC allows different processes to communicate with each other, while multi-threaded programming is a technique to improve the efficiency of a program by using multiple threads of execution.

## **Inter-Process Communication (IPC)**

### Definition

Inter-process communication (IPC) is a mechanism by which different processes can exchange data and communicate with each other.

### Types of IPC

- **Synchronous IPC**: The sending process waits for the receiving process to respond before proceeding.
- **Asynchronous IPC**: The sending process does not wait for the receiving process to respond.
- **Message Passing IPC**: Processes send messages to each other.
- **Shared Memory IPC**: Processes share a common memory space.

### Advantages of IPC

- **Improved System Resource Utilization**: Multiple processes can be executed concurrently.
- **Improved Fault Tolerance**: If one process fails, other processes can continue execution.

### Disadvantages of IPC

- **Increased Complexity**: IPC adds complexity to the program.
- **Increased Communication Overhead**: Processes need to spend time exchanging data.

### Example of IPC

Suppose we have two processes, `process1` and `process2`. `Process1` wants to send a message to `process2`.

- `process1` creates a message and sends it to `process2` using a pipe.
- `process2` receives the message and processes it.
- `process2` sends a response back to `process1` using the same pipe.
- `process1` receives the response and processes it.

### IPC Mechanisms

- **Pipe**: A pipe is a unidirectional communication channel between two processes.
- **Message Queue**: A message queue is a data structure that stores messages from multiple processes.
- **Shared Memory**: Shared memory is a region of memory shared by multiple processes.
- **Sockets**: Sockets are used for inter-process communication over a network.

### Example of IPC using Pipe

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main() {
    int pipefd[2];
    pid_t pid;
    char message[] = "Hello, world!";

    // Create a pipe
    if (pipe(pipefd) == -1) {
        perror("pipe");
        exit(EXIT_FAILURE);
    }

    // Create a child process
    pid = fork();
    if (pid == -1) {
        perror("fork");
        exit(EXIT_FAILURE);
    }

    if (pid == 0) {
        // Child process
        close(pipefd[1]);
        read(pipefd[0], message, 100);
        printf("Received message: %s\n", message);
        close(pipefd[0]);
        exit(EXIT_SUCCESS);
    } else {
        // Parent process
        close(pipefd[0]);
        write(pipefd[1], message, 100);
        close(pipefd[1]);
        exit(EXIT_SUCCESS);
    }
}
```

## **Multi-Threaded Programming**

### Definition

Multi-threaded programming is a technique to improve the efficiency of a program by using multiple threads of execution.

### Advantages of Multi-Threaded Programming

- **Improved System Resource Utilization**: Multiple threads can be executed concurrently.
- **Improved Responsiveness**: Threads can be used to improve the responsiveness of a program.

### Disadvantages of Multi-Threaded Programming

- **Increased Complexity**: Multi-threaded programs are more complex.
- **Increased Risk of Deadlocks**: Threads can deadlock if not managed properly.

### Types of Threads

- **User-Level Threads**: Threads are created at the user level.
- **Kernel-Level Threads**: Threads are created at the kernel level.

### Synchronization in Multi-Threaded Programming

- **Mutex Locks**: Mutex locks are used to synchronize access to shared resources.
- **Semaphores**: Semaphores are used to control the access to shared resources.
- **Monitors**: Monitors are used to synchronize access to shared resources.

### Example of Multi-Threaded Programming

Suppose we have a program that needs to perform two tasks concurrently. We can use multiple threads to achieve this.

- We create two threads, `thread1` and `thread2`.
- `Thread1` performs task A.
- `Thread2` performs task B.
- Both threads execute concurrently.

### Example of Multi-Threaded Programming using POSIX Threads

```c
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

void* task1(void* arg) {
    printf("Task 1 started\n");
    // Perform task A
    printf("Task 1 completed\n");
    return NULL;
}

void* task2(void* arg) {
    printf("Task 2 started\n");
    // Perform task B
    printf("Task 2 completed\n");
    return NULL;
}

int main() {
    pthread_t thread1, thread2;
    int rc;

    // Create threads
    rc = pthread_create(&thread1, NULL, task1, NULL);
    if (rc != 0) {
        perror("pthread_create");
        exit(EXIT_FAILURE);
    }

    rc = pthread_create(&thread2, NULL, task2, NULL);
    if (rc != 0) {
        perror("pthread_create");
        exit(EXIT_FAILURE);
    }

    // Wait for threads to finish
    pthread_join(thread1, NULL);
    pthread_join(thread2, NULL);

    return 0;
}
```

This study material covers the basics of inter-process communication (IPC) and multi-threaded programming. It explains the different IPC mechanisms, advantages and disadvantages of IPC, and synchronization techniques used in multi-threaded programming.
