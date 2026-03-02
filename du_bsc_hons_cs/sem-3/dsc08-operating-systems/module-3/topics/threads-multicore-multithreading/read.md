# Threads, Multicore Systems, and Multithreading

## Introduction

Modern computing has undergone a revolutionary transformation with the advent of multicore processors and multithreading technologies. In today's computing landscape, single-core processors have become obsolete, replaced by powerful multicore architectures that enable true parallel execution. Understanding threads and multithreading is no longer optional for computer science students—it is essential knowledge for developing high-performance applications and understanding how modern operating systems function.

Threads represent the fundamental unit of CPU utilization, serving as the backbone of concurrent programming. Unlike processes, which are heavyweight entities with separate memory spaces, threads share critical resources within a process, making them lighter and more efficient for concurrent operations. The University of Delhi's Computer Science curriculum emphasizes this topic because it bridges the gap between theoretical operating system concepts and practical software development skills required in the industry.

This module explores the intricate relationship between threads, multicore processors, and multithreading paradigms. You will learn how modern operating systems leverage these technologies to maximize throughput, improve responsiveness, and utilize hardware resources effectively. Whether you are preparing for semester examinations or building real-world applications, mastering these concepts is crucial for success in your programming career.

## Key Concepts

### Understanding Threads

A **thread** is the smallest unit of CPU execution within a process. It consists of a thread ID, program counter, register set, and stack, while sharing code section, data section, and other operating system resources with other threads in the same process. This shared nature makes threads incredibly efficient for simultaneous operations.

**Key characteristics of threads include:**
- **Lightweight Creation**: Thread creation takes significantly less time than process creation (typically 10-100 times faster)
- **Shared Resources**: Threads share memory, file descriptors, and other resources within their parent process
- **Independent Execution**: Each thread can execute independently, following its own control flow
- **Quick Termination**: Threads terminate faster than processes, releasing fewer resources

### Types of Threads

**User-Level Threads (ULT)**:
User-level threads are managed entirely by user-space libraries without kernel intervention. The operating system is unaware of these threads, treating the entire process as a single execution entity. Libraries like POSIX Pthreads (pthread) and Java threads often implement user-level threading. The primary advantage is superior performance—thread management requires no context switches to kernel mode. However, if any user-level thread performs a blocking system call, the entire process blocks, preventing other user-level threads from executing.

**Kernel-Level Threads (KLT)**:
Kernel-level threads are managed directly by the operating system kernel. The kernel handles thread creation, scheduling, and management entirely within kernel space. Since the kernel controls thread scheduling, this approach provides better concurrency—if one thread blocks, others can continue executing. Examples include Windows NT and OS/2 kernel threads. The drawback is that thread operations require kernel mode transitions, adding overhead to thread management.

### Multithreading Models

The relationship between user-level and kernel-level threads defines various threading models:

**Many-to-One Model**: Maps multiple user-level threads to a single kernel thread. Only one thread can access the kernel at a time, limiting parallelism on multiprocessor systems. This model is used by GNU Portable Threads and Solaris Green Threads.

**One-to-One Model**: Creates a one-to-one mapping between user and kernel threads. This provides maximum concurrency but restricts the number of threads due to kernel resource constraints. Windows NT, Linux, and OS/2 use this model.

**Many-to-Many Model**: Multiplexes many user-level threads to equal or fewer kernel threads. This provides both flexibility and concurrency, allowing developers to create as many user threads as needed. This was implemented in early versions of Solaris and IRIX.

**Two-Level Model**: A variation of many-to-many that allows mixing bound (dedicated to specific kernel threads) and unbound threads. Used by IRIX, HP-UX, and Tru64 UNIX.

### Multicore Systems and Parallelism

**Multicore processors** integrate multiple processing units (cores) on a single chip, enabling true parallel execution. Each core can execute instructions independently, dramatically improving computational throughput. Modern processors from Intel, AMD, and ARM feature anywhere from 2 to 64+ cores.

**Challenges in Multicore Programming**:
1. **Amdahl's Law**: States that the speedup of a program is limited by the sequential portion of the code. If 10% of the code must execute sequentially, maximum speedup is limited to 10x regardless of core count.

2. **Cache Coherence**: In multicore systems, each core typically has its own cache. Ensuring all caches have consistent data requires complex hardware protocols (MESI protocol), adding latency to memory operations.

3. **False Sharing**: When different threads modify variables that reside on the same cache line, cache coherency protocols force unnecessary synchronization, degrading performance.

4. **Load Balancing**: Distributing work evenly across cores to maximize utilization requires careful algorithmic design.

### Thread Synchronization

When multiple threads access shared resources, synchronization becomes critical to prevent race conditions and data inconsistencies.

**Mutex (Mutual Exclusion Lock)**: Provides exclusive access to shared resources. Only one thread can hold a mutex at a time, blocking other threads until released.

**Semaphore**: A signaling mechanism with an integer counter. Binary semaphores (count = 1) function like mutexes, while counting semaphores allow multiple simultaneous resource accesses.

**Condition Variables**: Allow threads to wait until specific conditions are met, enabling sophisticated synchronization patterns like producer-consumer scenarios.

**Reader-Writer Locks**: Optimize access patterns where reads are more frequent than writes, allowing multiple simultaneous readers but exclusive writer access.

### Benefits and Challenges of Multithreading

**Advantages**:
- **Responsiveness**: GUI applications remain responsive while performing background tasks
- **Resource Sharing**: Threads share memory and resources, reducing overhead
- **Economy**: Creating and switching threads is cheaper than processes
- **Scalability**: Multicore systems can utilize threads for parallel execution

**Disadvantages**:
- **Complexity**: Synchronization adds significant programming complexity
- **Debugging Difficulty**: Race conditions and deadlocks are hard to detect and reproduce
- **Platform Dependence**: Threading APIs vary across operating systems
- **Resource Limits**: Each process has limits on maximum thread count

## Examples

### Example 1: Creating Threads in C (POSIX Threads)

```c
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

void* thread_function(void* arg) {
    int thread_num = *(int*)arg;
    printf("Thread %d is running\n", thread_num);
    sleep(1);
    printf("Thread %d completed\n", thread_num);
    return NULL;
}

int main() {
    pthread_t threads[3];
    int thread_args[3];
    
    // Create 3 threads
    for (int i = 0; i < 3; i++) {
        thread_args[i] = i + 1;
        if (pthread_create(&threads[i], NULL, thread_function, &thread_args[i]) != 0) {
            perror("Thread creation failed");
            exit(1);
        }
    }
    
    // Wait for all threads to complete
    for (int i = 0; i < 3; i++) {
        pthread_join(threads[i], NULL);
    }
    
    printf("All threads completed\n");
    return 0;
}
```

**Step-by-step explanation**:
1. Define the thread function that receives a void pointer argument
2. Create three threads using pthread_create(), passing unique identifiers
3. The main thread waits for each thread using pthread_join()
4. All threads execute concurrently, demonstrating parallel execution

### Example 2: Thread Synchronization with Mutex

```c
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

int shared_counter = 0;
pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;

void* increment_counter(void* arg) {
    int iterations = *(int*)arg;
    
    for (int i = 0; i < iterations; i++) {
        pthread_mutex_lock(&mutex);    // Acquire lock
        shared_counter++;              // Critical section
        pthread_mutex_unlock(&mutex);  // Release lock
    }
    return NULL;
}

int main() {
    pthread_t t1, t2;
    int iterations = 100000;
    
    pthread_create(&t1, NULL, increment_counter, &iterations);
    pthread_create(&t2, NULL, increment_counter, &iterations);
    
    pthread_join(t1, NULL);
    pthread_join(t2, NULL);
    
    printf("Final counter value: %d (expected: %d)\n", 
           shared_counter, iterations * 2);
    
    return 0;
}
```

**Without mutex**: Race condition causes lost increments; final value would be less than 200,000.

**With mutex**: Proper synchronization ensures the final value is exactly 200,000, demonstrating mutual exclusion.

### Example 3: Producer-Consumer Problem

```c
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

#define BUFFER_SIZE 5

int buffer[BUFFER_SIZE];
int count = 0;
int in = 0, out = 0;

pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;
pthread_cond_t full = PTHREAD_COND_INITIALIZER;
pthread_cond_t empty = PTHREAD_COND_INITIALIZER;

void* producer(void* arg) {
    for (int i = 0; i < 10; i++) {
        pthread_mutex_lock(&mutex);
        
        while (count == BUFFER_SIZE)
            pthread_cond_wait(&empty, &mutex);
        
        buffer[in] = i;
        printf("Produced: %d\n", i);
        in = (in + 1) % BUFFER_SIZE;
        count++;
        
        pthread_cond_signal(&full);
        pthread_mutex_unlock(&mutex);
    }
    return NULL;
}

void* consumer(void* arg) {
    for (int i = 0; i < 10; i++) {
        pthread_mutex_lock(&mutex);
        
        while (count == 0)
            pthread_cond_wait(&full, &mutex);
        
        int item = buffer[out];
        printf("Consumed: %d\n", item);
        out = (out + 1) % BUFFER_SIZE;
        count--;
        
        pthread_cond_signal(&empty);
        pthread_mutex_unlock(&mutex);
    }
    return NULL;
}

int main() {
    pthread_t prod, cons;
    pthread_create(&prod, NULL, producer, NULL);
    pthread_create(&cons, NULL, consumer, NULL);
    pthread_join(prod, NULL);
    pthread_join(cons, NULL);
    return 0;
}
```

**Key synchronization mechanisms**:
- **Mutex**: Protects access to shared buffer and count variables
- **Condition variable 'full'**: Signals consumer when items are available
- **Condition variable 'empty'**: Signals producer when buffer has space
- **while loops**: Recheck conditions after waking (prevents spurious wakeups)

## Exam Tips

1. **Distinguish between Process and Thread**: In exams, clearly state that processes have separate address spaces while threads share memory within a process. This distinction frequently appears in 2-3 mark questions.

2. **Remember Multithreading Models**: Be prepared to draw diagrams comparing many-to-one, one-to-one, and many-to-many models. Know real-world examples of each (Solaris Green Threads uses many-to-one, Windows uses one-to-one).

3. **Understand Kernel vs User Threads**: The trade-off between performance (user threads) and reliability (kernel threads) is a common examination topic. Explain how blocking system calls affect both types.

4. **Amdahl's Law Calculation**: Be prepared to calculate maximum speedup using the formula: Speedup = 1 / (S + (1-S)/N), where S is sequential fraction and N is number of processors.

5. **Synchronization Mechanisms**: Know when to use mutexes versus semaphores. Mutex provides ownership (only the thread locking it can unlock), while semaphores are more general signaling mechanisms.

6. **Thread Creation Overhead**: Remember that thread creation is faster than process creation because threads share most resources. This is why multithreading is preferred for concurrent operations.

7. **Race Conditions**: Be able to identify and prevent race conditions in code examples. The critical section concept and mutual exclusion requirements are frequently tested.

8. **Deadlock Conditions**: Remember the four Coffman conditions necessary for deadlock: mutual exclusion, hold and wait, no preemption, and circular wait. Be prepared to explain how to prevent each.