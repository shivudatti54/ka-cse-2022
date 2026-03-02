# **Thread Libraries Textbook 1: Chapter 3: 3.1-3.4**

## **3.1: Introduction to Threads**

### Definition

A thread is a lightweight process that shares the same memory space as other threads in the same process.

### Characteristics

- **Lightweight**: Threads have lower overhead compared to processes.
- **Sharing**: Threads share the same memory space.
- **Independent Execution**: Threads can execute concurrently.

### Example

Suppose we have a web browser with multiple tabs. Each tab is an independent process, but they all share the same memory space.

### Advantages

- **Efficient Resource Utilization**: Multiple threads can perform different tasks simultaneously.
- **Improved Responsiveness**: Threads can respond to user input quickly.

### Disadvantages

- **Complexity**: Thread management can be complex.
- **Security Risks**: Shared memory can pose security risks if not managed properly.

## **3.2: Synchronization**

### Definition

Synchronization is the process of coordinating access to shared resources by multiple threads.

### Importance

- **Ensures Data Integrity**: Synchronization prevents data corruption.
- **Prevents Deadlocks**: Synchronization prevents deadlocks.

### Techniques

- **Mutual Exclusion**: Only one thread can access the shared resource at a time.
- **Semaphore**: A semaphore is a variable that controls the access to a shared resource.
- **Monitors**: A monitor is an object that provides synchronized access to a shared resource.

### Example

Consider a bank account with multiple threads trying to withdraw money concurrently. Synchronization ensures that only one thread can access the account balance at a time.

### Code Example (C)

```c
#include <pthread.h>
#include <semaphore.h>

sem_t sem;
int balance = 1000;

void* withdrawMoney(void* arg) {
    sem_wait(&sem);
    balance -= 100;
    printf("Withdrawal successful. Balance: %d\n", balance);
    sem_post(&sem);
    return NULL;
}

int main() {
    sem_init(&sem, 0, 1); // Initialize semaphore with value 1
    pthread_t thread1, thread2;
    pthread_create(&thread1, NULL, withdrawMoney, NULL);
    pthread_create(&thread2, NULL, withdrawMoney, NULL);
    pthread_join(thread1, NULL);
    pthread_join(thread2, NULL);
    sem_destroy(&sem);
    return 0;
}
```

## **3.3: Communication between Threads**

### Definition

Communication between threads refers to the exchange of data between threads.

### Techniques

- **Shared Variables**: Shared variables can be used to communicate between threads.
- **Message Passing**: Message passing involves passing data between threads using a message.
- **Synchronization primitives**: Synchronization primitives such as semaphores and monitors can be used to coordinate communication between threads.

### Example

Consider two threads, thread1 and thread2, that need to communicate with each other. They can use shared variables or message passing to exchange data.

### Code Example (C)

```c
#include <pthread.h>
#include <semaphore.h>

sem_t sem;
int data = 0;

void* thread1Function(void* arg) {
    data = 10;
    sem_post(&sem);
    return NULL;
}

void* thread2Function(void* arg) {
    sem_wait(&sem);
    printf("Received data: %d\n", data);
    return NULL;
}

int main() {
    sem_init(&sem, 0, 0); // Initialize semaphore with value 0
    pthread_t thread1, thread2;
    pthread_create(&thread1, NULL, thread1Function, NULL);
    pthread_create(&thread2, NULL, thread2Function, NULL);
    pthread_join(thread1, NULL);
    pthread_join(thread2, NULL);
    sem_destroy(&sem);
    return 0;
}
```

## **3.4: Thread Creation and Management**

### Definition

Thread creation and management refer to the process of creating and managing threads.

### Techniques

- **Thread creation**: Threads can be created using the `pthread_create` function.
- **Thread management**: Threads can be managed using synchronization primitives such as semaphores and monitors.

### Example

Consider two threads, thread1 and thread2, that need to be created and managed. They can use synchronization primitives to coordinate their execution.

### Code Example (C)

```c
#include <pthread.h>
#include <semaphore.h>

sem_t sem;
int counter = 0;

void* thread1Function(void* arg) {
    for (int i = 0; i < 5; i++) {
        sem_wait(&sem);
        counter++;
        printf("Thread 1: Counter = %d\n", counter);
        sem_post(&sem);
    }
    return NULL;
}

void* thread2Function(void* arg) {
    for (int i = 0; i < 5; i++) {
        sem_post(&sem);
        counter++;
        printf("Thread 2: Counter = %d\n", counter);
        sem_wait(&sem);
    }
    return NULL;
}

int main() {
    sem_init(&sem, 0, 0); // Initialize semaphore with value 0
    pthread_t thread1, thread2;
    pthread_create(&thread1, NULL, thread1Function, NULL);
    pthread_create(&thread2, NULL, thread2Function, NULL);
    pthread_join(thread1, NULL);
    pthread_join(thread2, NULL);
    sem_destroy(&sem);
    return 0;
}
```

This study material covers the fundamentals of threads, synchronization, communication, and thread creation and management. It provides definitions, explanations, and examples to help students understand these concepts.
