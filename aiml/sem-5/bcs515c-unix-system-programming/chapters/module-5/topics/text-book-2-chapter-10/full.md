# UNIX SYSTEM PROGRAMMING

## Module: 2

## Topic: Text Book 2: Chapter 10

### Table of Contents

1. [Overview of Chapter 10](#overview-of-chapter-10)
2. [Process Synchronization](#process-synchronization)
3. [Process Communication](#process-communication)
4. [Thread Synchronization](#thread-synchronization)
5. [Thread Communication](#thread-communication)
6. [Deadlocks and Livelocks](#deadlocks-and-livelocks)
7. [Starvation and Priority Inversion](#starvation-and-priority-inversion)
8. [Resource Sharing](#resource-sharing)
9. [Interrupt Handling](#interrupt-handling)
10. [Conclusion](#conclusion)
11. [Further Reading](#further-reading)

### Overview of Chapter 10

Chapter 10 of the UNIX System Programming textbook focuses on the synchronization and communication aspects of process and thread programming. This chapter is crucial for understanding how multiple processes and threads can interact with each other in a coordinated manner.

### Process Synchronization

Process synchronization refers to the mechanisms used to coordinate the actions of multiple processes. These mechanisms ensure that processes access shared resources in a consistent and predictable manner.

#### Semaphores

A semaphore is a variable that controls the access to a shared resource by multiple processes. It is used to synchronize the access to a resource and prevent multiple processes from accessing it simultaneously.

**Example:** Implementing a semaphore using a shared variable and a counter.

```c
#include <stdio.h>
#include <stdlib.h>

int semaphore = 1; // Initialize the semaphore with a value of 1
int count = 0;

void *producer(void *arg) {
    while (1) {
        printf("Producer: Waiting for semaphore...\n");
        sem_wait(&semaphore); // Wait for the semaphore to be available
        count++;
        printf("Producer: Acquired semaphore, count = %d\n", count);
        // Simulate some work
        sleep(1);
    }
    return NULL;
}

void *consumer(void *arg) {
    while (1) {
        printf("Consumer: Waiting for semaphore...\n");
        sem_wait(&semaphore); // Wait for the semaphore to be available
        count--;
        printf("Consumer: Released semaphore, count = %d\n", count);
        // Simulate some work
        sleep(1);
    }
    return NULL;
}

int main() {
    sem_t semaphore; // Create a semaphore
    sem_init(&semaphore, 0, 1); // Initialize the semaphore with a value of 1

    pthread_t producer_thread, consumer_thread;

    pthread_create(&producer_thread, NULL, producer, NULL);
    pthread_create(&consumer_thread, NULL, consumer, NULL);

    pthread_join(producer_thread, NULL);
    pthread_join(consumer_thread, NULL);

    sem_destroy(&semaphore); // Destroy the semaphore

    return 0;
}
```

#### Monitors

A monitor is a higher-level synchronization construct than a semaphore. It is a combination of a semaphore and a protected region of memory.

**Example:** Implementing a monitor using a semaphore and a protected region of memory.

```c
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

sem_t semaphore; // Create a semaphore
int count = 0; // Initialize the shared variable

void *producer(void *arg) {
    while (1) {
        printf("Producer: Waiting for monitor...\n");
        sem_wait(&semaphore); // Wait for the monitor to be available
        count++;
        printf("Producer: Acquired monitor, count = %d\n", count);
        // Simulate some work
        sleep(1);
        sem_post(&semaphore); // Release the monitor
    }
    return NULL;
}

void *consumer(void *arg) {
    while (1) {
        printf("Consumer: Waiting for monitor...\n");
        sem_wait(&semaphore); // Wait for the monitor to be available
        count--;
        printf("Consumer: Released monitor, count = %d\n", count);
        // Simulate some work
        sleep(1);
        sem_post(&semaphore); // Release the monitor
    }
    return NULL;
}

int main() {
    sem_init(&semaphore, 0, 1); // Initialize the semaphore with a value of 1

    pthread_t producer_thread, consumer_thread;

    pthread_create(&producer_thread, NULL, producer, NULL);
    pthread_create(&consumer_thread, NULL, consumer, NULL);

    pthread_join(producer_thread, NULL);
    pthread_join(consumer_thread, NULL);

    sem_destroy(&semaphore); // Destroy the semaphore

    return 0;
}
```

### Process Communication

Process communication refers to the mechanisms used to exchange information between multiple processes. These mechanisms can be classified into two categories: synchronous and asynchronous.

#### Synchronous Communication

Synchronous communication involves the use of a message passing mechanism to exchange information between processes.

**Example:** Implementing synchronous communication using pipes.

```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main() {
    int pipefd[2]; // Create a pipe

    // Create a pipe
    if (pipe(pipefd) == -1) {
        perror("pipe");
        exit(1);
    }

    // Fork a new process
    pid_t child = fork();

    if (child == -1) {
        perror("fork");
        exit(1);
    }

    if (child == 0) {
        // Child process
        close(pipefd[0]); // Close the read end of the pipe
        write(pipefd[1], "Hello, world!", 13); // Write to the pipe
        close(pipefd[1]); // Close the write end of the pipe
        read(pipefd[0], NULL, 0); // Read from the pipe
        close(pipefd[0]); // Close the read end of the pipe
    } else {
        // Parent process
        close(pipefd[1]); // Close the write end of the pipe
        char buffer[13]; // Initialize a buffer to receive the message
        read(pipefd[0], buffer, 13); // Read from the pipe
        printf("Received message: %s\n", buffer);
        close(pipefd[0]); // Close the read end of the pipe
    }

    return 0;
}
```

#### Asynchronous Communication

Asynchronous communication involves the use of a message passing mechanism with a queue to exchange information between processes.

**Example:** Implementing asynchronous communication using a shared queue.

```c
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>

sem_t semaphore; // Create a semaphore
int queue[10]; // Initialize the queue
int front = 0; // Initialize the front of the queue
int rear = 0; // Initialize the rear of the queue

// Function to add an element to the queue
void add_to_queue(int element) {
    queue[rear] = element;
    rear = (rear + 1) % 10;
}

// Function to remove an element from the queue
int remove_from_queue() {
    int element = queue[front];
    front = (front + 1) % 10;
    return element;
}

void *producer(void *arg) {
    for (int i = 0; i < 10; i++) {
        add_to_queue(i); // Add an element to the queue
        printf("Producer: Added element %d to the queue\n", i);
    }
    return NULL;
}

void *consumer(void *arg) {
    for (int i = 0; i < 10; i++) {
        int element = remove_from_queue(); // Remove an element from the queue
        printf("Consumer: Removed element %d from the queue\n", element);
    }
    return NULL;
}

int main() {
    sem_init(&semaphore, 0, 1); // Initialize the semaphore with a value of 1

    pthread_t producer_thread, consumer_thread;

    pthread_create(&producer_thread, NULL, producer, NULL);
    pthread_create(&consumer_thread, NULL, consumer, NULL);

    pthread_join(producer_thread, NULL);
    pthread_join(consumer_thread, NULL);

    sem_destroy(&semaphore); // Destroy the semaphore

    return 0;
}
```

### Thread Synchronization

Thread synchronization refers to the mechanisms used to coordinate the actions of multiple threads. These mechanisms are similar to those used for process synchronization.

#### Monitors

A monitor is a higher-level synchronization construct than a semaphore or a mutex.

**Example:** Implementing a monitor using a mutex and a protected region of memory.

```c
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>

sem_t semaphore; // Create a semaphore
int count = 0; // Initialize the shared variable
pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER; // Initialize the mutex

void *thread_func(void *arg) {
    while (1) {
        pthread_mutex_lock(&mutex); // Lock the mutex
        count++;
        printf("Thread: Acquired mutex, count = %d\n", count);
        // Simulate some work
        sleep(1);
        pthread_mutex_unlock(&mutex); // Unlock the mutex
    }
    return NULL;
}

int main() {
    sem_init(&semaphore, 0, 1); // Initialize the semaphore with a value of 1

    pthread_t thread;

    pthread_create(&thread, NULL, thread_func, NULL);

    pthread_join(thread, NULL);

    sem_destroy(&semaphore); // Destroy the semaphore

    return 0;
}
```

#### Condition Variables

A condition variable is a synchronization construct that allows threads to wait for specific conditions to occur.

**Example:** Implementing a condition variable using a mutex and a condition.

```c
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>

sem_t semaphore; // Create a semaphore
int count = 0; // Initialize the shared variable
pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER; // Initialize the mutex
pthread_cond_t cond = PTHREAD_COND_INITIALIZER; // Initialize the condition variable

void *thread_func(void *arg) {
    while (1) {
        pthread_mutex_lock(&mutex); // Lock the mutex
        while (count == 0) { // Wait for the condition to occur
            pthread_cond_wait(&cond, &mutex);
        }
        count++;
        printf("Thread: Acquired mutex, count = %d\n", count);
        // Simulate some work
        sleep(1);
        pthread_mutex_unlock(&mutex); // Unlock the mutex
    }
    return NULL;
}

int main() {
    sem_init(&semaphore, 0, 1); // Initialize the semaphore with a value of 1

    pthread_t thread;

    pthread_create(&thread, NULL, thread_func, NULL);

    // Signal the condition
    pthread_mutex_lock(&mutex);
    count = 1;
    pthread_cond_signal(&cond);
    pthread_mutex_unlock(&mutex);

    pthread_join(thread, NULL);

    sem_destroy(&semaphore); // Destroy the semaphore

    return 0;
}
```

### Deadlocks and Livelocks

A deadlock is a situation where two or more threads are blocked indefinitely, waiting for each other to release resources.

**Example:** Implementing a deadlock using two threads and two locks.

```c
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

pthread_mutex_t mutex1 = PTHREAD_MUTEX_INITIALIZER; // Initialize the first mutex
pthread_mutex_t mutex2 = PTHREAD_MUTEX_INITIALIZER; // Initialize the second mutex

void *thread1_func(void *arg) {
    pthread_mutex_lock(&mutex1); // Lock the first mutex
    printf("Thread 1: Acquired mutex 1\n");
    pthread_mutex_lock(&mutex2); // Lock the second mutex
    printf("Thread 1: Acquired mutex 2\n");
    // Simulate some work
    sleep(1);
    return NULL;
}

void *thread2_func(void *arg) {
    pthread_mutex_lock(&mutex2); // Lock the second mutex
    printf("Thread 2: Acquired mutex 2\n");
    pthread_mutex_lock(&mutex1); // Lock the first mutex
    printf("Thread 2: Acquired mutex 1\n");
    // Simulate some work
    sleep(1);
    return NULL;
}

int main() {
    pthread_t thread1, thread2;

    pthread_create(&thread1, NULL, thread1_func, NULL);
    pthread_create(&thread2, NULL, thread2_func, NULL);

    pthread_join(thread1, NULL);
    pthread_join(thread2, NULL);

    return 0;
}
```

A livelock is a situation where two or more threads are unable to make progress, but are not blocked indefinitely.

**Example:** Implementing a livelock using two threads and two locks.

```c
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

pthread_mutex_t mutex1 = PTHREAD_MUTEX_INITIALIZER; // Initialize the first mutex
pthread_mutex_t mutex2 = PTHREAD_MUTEX_INITIALIZER; // Initialize the second mutex

void *thread1_func(void *arg) {
    pthread_mutex_lock(&mutex1); // Lock the first mutex
    printf("Thread 1: Acquired mutex 1\n");
    pthread_mutex_lock(&mutex2); // Lock the second mutex
    printf("Thread 1: Acquired mutex 2\n");
    // Simulate some work
    sleep(1);
    pthread_mutex_unlock(&mutex2); // Unlock the second mutex
    pthread_mutex_unlock(&mutex1); // Unlock the first mutex
    return NULL;
}

void *thread2_func(void *arg) {
    pthread_mutex_lock(&mutex2); // Lock the second mutex
    printf("Thread 2: Acquired mutex 2\n");
    pthread_mutex_lock(&mutex1); // Lock the first mutex
    printf("Thread 2: Acquired mutex 1\n");
    // Simulate some work
    sleep(1);
    pthread_mutex_unlock(&mutex1); // Unlock the first mutex
    pthread_mutex_unlock(&mutex2); // Unlock the second mutex
    return NULL;
}

int main() {
    pthread_t thread1, thread2;

    pthread_create(&thread1, NULL, thread1_func, NULL);
    pthread_create(&thread2, NULL, thread2_func, NULL);

    pthread_join(thread1, NULL);
    pthread_join(thread2, NULL);

    return 0;
}
```

### Starvation and Priority Inversion

Starvation occurs when a process is unable to access a shared resource because other processes are holding onto it for an extended period.

**Example:** Implementing starvation using two threads and two locks.

```c
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

pthread_mutex_t mutex1 = PTHREAD_MUTEX_INITIALIZER; // Initialize the first mutex
pthread_mutex_t mutex2 = PTHREAD_MUTEX_INITIALIZER; // Initialize the second mutex

void *thread1_func(void *arg) {
    pthread_mutex_lock(&mutex1); // Lock the first mutex
    printf("Thread 1: Acquired mutex 1\n");
    // Simulate some work
    sleep(1);
    pthread_mutex_unlock(&mutex1); // Unlock the first mutex
    return NULL;
}

void *thread2_func(void *arg) {
    pthread_mutex_lock(&mutex2); // Lock the second mutex
    printf("Thread 2: Acquired mutex 2\n");
    // Simulate some work
    sleep(1);
    pthread_mutex_unlock(&mutex2); // Unlock the second mutex
    return NULL;
}

int main() {
    pthread_t thread1, thread2;

    pthread_create(&thread1, NULL, thread1_func, NULL);
    pthread_create(&thread2, NULL, thread2_func, NULL);

    pthread_join(thread1, NULL);
    pthread_join(thread2, NULL);

    return 0;
}
```

Priority inversion occurs when a process with a lower priority is unable to access a shared resource because a process with a higher priority is holding onto it.

**Example:** Implementing priority inversion using two threads and two locks.

```c
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

pthread_mutex_t mutex1 = PTHREAD_MUTEX_INITIALIZER; // Initialize the first mutex
pthread_mutex_t mutex2 = PTHREAD_MUTEX_INITIALIZER; // Initialize the second mutex

void *thread1_func(void *arg) {
    pthread_mutex_lock(&mutex1); // Lock the first mutex
    printf("Thread 1: Acquired mutex 1\n");
    // Simulate some work
    sleep(1);
    pthread_mutex_unlock(&mutex1); // Unlock the first mutex
    return NULL;
}

void *thread2_func(void *arg) {
    pthread_mutex_lock(&mutex2); // Lock the second mutex
    printf("Thread 2: Acquired mutex 2\n");
    // Simulate some work
    sleep(1);
    pthread_mutex_unlock(&mutex2); // Unlock the second mutex
    return NULL;
}

int main() {
    pthread_t thread1, thread2;

    pthread_create(&thread1, NULL, thread1_func, NULL);
    pthread_create(&thread2, NULL, thread2_func, NULL);

    pthread_setprioritythread(&thread1, PTHREAD_PRIORITY_LOWEST);
    pthread_setprioritythread(&thread2, PTHREAD_PRIORITY Highest);

    pthread_join(thread1, NULL);
    pthread_join(thread2, NULL);

    return 0;
}
```

### Resource Sharing

Resource sharing refers to the mechanisms used to divide and manage shared resources among multiple processes or threads.

#### Semaphores

A semaphore is a variable that controls the access to a shared resource by multiple processes or threads.

**Example:** Implementing a semaphore to share a resource among multiple threads.

```c
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>

sem_t semaphore; // Create a semaphore
int count = 0; // Initialize the shared variable

void *thread_func(void *arg) {
    while (1) {
        sem_wait(&semaphore); // Wait for the semaphore to be available
        count++;
        printf("Thread: Acquired semaphore, count = %d\n", count);
        // Simulate some work
        sleep(1);
        sem_post(&semaphore); // Release the semaphore
    }
    return NULL;
}

int main() {
    sem_init(&semaphore, 0, 1); // Initialize the semaphore with a value of 1

    pthread_t thread;

    pthread_create(&thread, NULL, thread_func, NULL);

    pthread_join(thread, NULL);

    sem_destroy(&semaphore); // Destroy the semaphore

    return 0;
}
```

#### Monitors

A monitor is a higher-level synchronization construct than a semaphore.

**Example:** Implementing a monitor to share a resource among multiple threads.

```c
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>

sem_t semaphore; // Create a semaphore
int count = 0; // Initialize the shared variable
pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER; // Initialize the mutex

void *thread_func(void *arg) {
    while (1) {
        pthread_mutex_lock(&mutex); // Lock the mutex
        while (count ==
```
