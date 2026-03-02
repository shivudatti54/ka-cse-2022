# Thread Libraries


## Table of Contents

- [Thread Libraries](#thread-libraries)
- [Introduction](#introduction)
- [Key Concepts](#key-concepts)
  - [Thread Library Fundamentals](#thread-library-fundamentals)
  - [POSIX Threads (Pthreads)](#posix-threads-pthreads)
  - [Windows Threading API](#windows-threading-api)
  - [Java Threads](#java-threads)
  - [Thread Synchronization Mechanisms](#thread-synchronization-mechanisms)
  - [Thread Pools](#thread-pools)
  - [Thread Safety and Reentrant Code](#thread-safety-and-reentrant-code)
- [Examples](#examples)
  - [Example 1: Creating Threads with Pthreads](#example-1-creating-threads-with-pthreads)
  - [Example 2: Thread Synchronization with Mutex](#example-2-thread-synchronization-with-mutex)
  - [Example 3: Thread Pool in Java](#example-3-thread-pool-in-java)
- [Exam Tips](#exam-tips)

## Introduction

Thread libraries provide programmers with a standardized interface for creating and managing multiple threads of execution within a single process. In modern operating systems, threads have become the fundamental unit of execution, enabling concurrent programming that maximizes CPU utilization and improves application responsiveness. A thread library abstracts the complex low-level operations required for thread management, allowing developers to focus on application logic rather than dealing with system-specific implementation details.

The importance of thread libraries in contemporary computing cannot be overstated. With the advent of multi-core and multi-processor architectures, single-threaded applications fail to harness the full computational power available in modern hardware. Thread libraries enable developers to create applications that can execute multiple tasks simultaneously, making optimal use of available processing resources. From web servers handling thousands of concurrent requests to scientific simulations performing parallel computations, thread libraries form the backbone of concurrent software development. Understanding thread libraries is essential for any computer science professional, as concurrency has become a fundamental paradigm in software architecture.

## Key Concepts

### Thread Library Fundamentals

A thread library is an application programming interface (API) that provides functions for creating, managing, and synchronizing threads. Thread libraries typically offer primitives for thread creation, thread termination, thread join (waiting for thread completion), thread identification, and thread scheduling control. The library implements these primitives either through system calls to the operating system kernel or through user-space implementations that manage threads entirely in application code.

Thread libraries can be categorized based on their implementation approach: user-level thread libraries and kernel-level thread libraries. User-level thread libraries implement all thread management functionality entirely in user space, without requiring operating system support for threading. These libraries are portable across different operating systems but cannot take advantage of multiple processors because the operating system sees only a single thread. Kernel-level thread libraries, on the other hand, rely on operating system support for thread management, allowing the kernel to schedule threads across multiple processors. Most modern thread libraries use a hybrid approach that combines the benefits of both approaches.

### POSIX Threads (Pthreads)

POSIX Threads, commonly known as Pthreads, is the standardized thread programming interface for UNIX and POSIX systems. Defined by the IEEE POSIX 1003.1c standard, Pthreads provides a portable API that is supported across virtually all UNIX-like operating systems including Linux, macOS, and BSD variants. The Pthreads API includes approximately 100 functions covering thread management, synchronization, and thread-specific data.

The fundamental thread creation function in Pthreads is pthread_create(), which takes four parameters: a pointer to a thread identifier, thread attributes, the start routine function, and an argument to pass to that routine. Threads are terminated either by returning from the start routine or by explicitly calling pthread_exit(). The pthread_join() function allows one thread to wait for the completion of another thread, similar to the process wait() system call. Thread synchronization in Pthreads is provided through mutexes (mutual exclusion locks), condition variables, read-write locks, and spin locks.

### Windows Threading API

The Windows operating system provides the Windows Threading API as its native threading mechanism. The primary functions include CreateThread() for thread creation, WaitForSingleObject() and WaitForMultipleObjects() for thread synchronization, and various synchronization primitives such as critical sections, mutexes, semaphores, and events. The Windows API is kernel-level, meaning the Windows kernel manages thread scheduling and can distribute threads across multiple processors.

Windows threads support thread-local storage through the Thread Local Storage (TLS) API, allowing each thread to have its own copy of global variables. The Windows API also provides fiber support, which implements user-level scheduling of threads within a process. Fibers are lightweight threads that are scheduled explicitly by the application rather than by the operating system, useful for implementing cooperative multitasking or converting existing single-threaded code to use concurrency.

### Java Threads

Java provides built-in thread support through the java.lang.Thread class and the java.util.concurrent package introduced in Java 5. Java threads are unique in that they map directly to kernel threads on the underlying operating system, making them true kernel-level threads. This design allows Java applications to benefit from multi-processor systems while maintaining platform independence.

Java offers two approaches for creating threads: extending the Thread class and implementing the Runnable interface. The Runnable interface is generally preferred because Java does not support multiple inheritance, and implementing Runnable allows the class to extend other classes. The java.util.concurrent package provides higher-level concurrency utilities including thread pools (ExecutorService), concurrent collections, synchronization aids (CountDownLatch, CyclicBarrier, Semaphore), and the Fork/Join framework for recursive parallel processing.

### Thread Synchronization Mechanisms

Thread synchronization is critical in multi-threaded programs because multiple threads often access shared resources simultaneously. Without proper synchronization, race conditions occur where the final outcome depends on the unpredictable timing of thread execution. Thread libraries provide various synchronization primitives to ensure correct program behavior.

Mutexes (mutual exclusion locks) are the most fundamental synchronization primitive, ensuring that only one thread can access a protected resource at any given time. A thread acquires the mutex before accessing the shared resource and releases it afterward. If another thread attempts to acquire a mutex that is already held, it blocks until the owning thread releases it. Condition variables allow threads to wait for specific conditions to become true, typically used in conjunction with mutexes. Semaphores are generalized counting synchronization primitives that maintain a count and allow multiple threads to access a resource up to a specified limit.

### Thread Pools

Thread pools represent a critical optimization pattern in thread-based programming. Instead of creating a new thread for each task (which incurs significant overhead), a thread pool maintains a collection of pre-created worker threads that are reused to execute multiple tasks. When a task needs to be executed, it is submitted to the pool, and an available worker thread processes it. Thread pools dramatically improve performance in scenarios where many short-lived tasks need to be executed, such as web servers handling HTTP requests.

The ThreadPoolExecutor class in Java provides a configurable thread pool implementation with options for controlling the minimum and maximum number of threads, thread idle timeout, task queue characteristics, and thread factory. Similarly, Pthreads and Windows APIs support thread pool implementations. Modern thread pool implementations also provide hooks for monitoring, performance tuning, and graceful shutdown.

### Thread Safety and Reentrant Code

Thread safety refers to the property of a function or code segment that ensures correct behavior when called from multiple threads simultaneously. A thread-safe function protects its shared state through proper synchronization and does not rely on any state that might be modified by other threads in unpredictable ways. Many standard library functions in C and C++ exist in both thread-safe and non-thread-safe versions, with the thread-safe versions typically having "_r" suffix.

Reentrant code is a stricter property than thread safety. A reentrant function can be safely called again even while a previous call is still executing, because it does not rely on any shared state or modifies only local variables. Reentrant functions are inherently thread-safe but thread-safe functions are not necessarily reentrant. Understanding these concepts is crucial for writing correct concurrent programs and debugging race conditions.

## Examples

### Example 1: Creating Threads with Pthreads

Consider a program that needs to perform two independent computational tasks concurrently. Using Pthreads, we can create two threads to execute these tasks in parallel.

```c
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

void* task1(void* arg) {
    int n = *(int*)arg;
    long sum = 0;
    for (int i = 1; i <= n; i++) {
        sum += i;
    }
    printf("Task 1: Sum of 1 to %d = %ld\n", n, sum);
    return NULL;
}

void* task2(void* arg) {
    int n = *(int*)arg;
    long factorial = 1;
    for (int i = 2; i <= n; i++) {
        factorial *= i;
    }
    printf("Task 2: Factorial of %d = %ld\n", n, factorial);
    return NULL;
}

int main() {
    pthread_t thread1, thread2;
    int n = 10;
    
    // Create first thread for summation
    if (pthread_create(&thread1, NULL, task1, &n) != 0) {
        perror("pthread_create failed");
        exit(1);
    }
    
    // Create second thread for factorial
    if (pthread_create(&thread2, NULL, task2, &n) != 0) {
        perror("pthread_create failed");
        exit(1);
    }
    
    // Wait for both threads to complete
    pthread_join(thread1, NULL);
    pthread_join(thread2, NULL);
    
    printf("Both tasks completed.\n");
    return 0;
}
```

In this example, pthread_create() spawns two independent threads that execute task1() and task2() concurrently. The pthread_join() calls in main() ensure that the main thread waits for both worker threads to complete before terminating the program. The actual output order may vary between runs due to thread scheduling, demonstrating the non-deterministic nature of concurrent execution.

### Example 2: Thread Synchronization with Mutex

When multiple threads access shared data, synchronization becomes essential. This example demonstrates a correct implementation using a mutex to protect a shared counter.

```c
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int shared_counter;
    pthread_mutex_t mutex;
} SharedData;

void* increment_counter(void* arg) {
    SharedData* data = (SharedData*)arg;
    
    for (int i = 0; i < 100000; i++) {
        pthread_mutex_lock(&data->mutex);
        data->shared_counter++;
        pthread_mutex_unlock(&data->mutex);
    }
    
    return NULL;
}

int main() {
    SharedData data = {.shared_counter = 0};
    pthread_mutex_init(&data.mutex, NULL);
    
    pthread_t threads[5];
    
    // Create 5 threads, each incrementing counter 100000 times
    for (int i = 0; i < 5; i++) {
        pthread_create(&threads[i], NULL, increment_counter, &data);
    }
    
    // Wait for all threads
    for (int i = 0; i < 5; i++) {
        pthread_join(threads[i], NULL);
    }
    
    printf("Final counter value: %d (expected: 500000)\n", 
           data.shared_counter);
    
    pthread_mutex_destroy(&data.mutex);
    return 0;
}
```

Without the mutex, the final counter value would be unpredictable due to race conditions. With proper mutex protection, each thread atomically increments the counter, guaranteeing the correct result of 500000. This demonstrates why synchronization primitives are essential for correct multi-threaded programming.

### Example 3: Thread Pool in Java

Java's ExecutorService provides a convenient thread pool implementation for managing concurrent tasks.

```java
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.TimeUnit;

class Task implements Runnable {
    private final int taskId;
    
    public Task(int id) {
        this.taskId = id;
    }
    
    @Override
    public void run() {
        System.out.println("Task " + taskId + " started by " + 
                           Thread.currentThread().getName());
        try {
            // Simulate some work
            Thread.sleep((long)(Math.random() * 1000));
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
        System.out.println("Task " + taskId + " completed");
    }
}

public class ThreadPoolExample {
    public static void main(String[] args) throws InterruptedException {
        // Create a fixed thread pool with 3 worker threads
        ExecutorService executor = Executors.newFixedThreadPool(3);
        
        // Submit 10 tasks to the pool
        for (int i = 1; i <= 10; i++) {
            executor.submit(new Task(i));
        }
        
        // Shutdown the executor (no new tasks accepted)
        executor.shutdown();
        
        // Wait for all tasks to complete (max 30 seconds)
        if (executor.awaitTermination(30, TimeUnit.SECONDS)) {
            System.out.println("All tasks completed successfully");
        } else {
            System.out.println("Timeout - forcing shutdown");
            executor.shutdownNow();
        }
    }
}
```

The thread pool efficiently manages the 10 submitted tasks using only 3 worker threads. Tasks are executed as worker threads become available, demonstrating how thread pools limit resource consumption while maintaining throughput. The executor.shutdown() and awaitTermination() pattern ensures graceful shutdown with proper completion of in-progress tasks.

## Exam Tips

For the University of Delhi operating systems examination, candidates should focus on the following aspects of thread libraries:

1. DISTINGUISH BETWEEN USER-LEVEL AND KERNEL-LEVEL THREADS: Understand the fundamental difference, including performance implications, portability, and the ability to utilize multiple processors. Remember that user-level threads map to a single kernel thread.

2. MEMORIZE KEY PTHREADS FUNCTIONS: pthread_create(), pthread_join(), pthread_exit(), pthread_mutex_lock(), pthread_mutex_unlock(), and pthread_cond_wait() are essential. Know their signatures and purposes.

3. UNDERSTAND THREAD SYNCHRONIZATION PRIMITIVES: Be able to explain mutexes, semaphores, condition variables, and their appropriate use cases. Understand the difference between blocking (mutex) and non-blocking (spinlock) synchronization.

4. KNOW THE DIFFERENCE BETWEEN THREAD SAFETY AND REENTRANCY: Thread-safe code protects against concurrent access while reentrant code can be safely called recursively. Reentrant code is always thread-safe but the converse is not true.

5. THREAD POOL ADVANTAGES: Remember that thread pools reduce overhead by reusing threads, provide control over maximum concurrency, and help prevent resource exhaustion from creating too many threads.

6. RACE CONDITIONS: Understand what causes race conditions and how synchronization prevents them. Be prepared to identify race conditions in code examples.

7. JAVA THREAD CREATION: Remember the two approaches—extending Thread class and implementing Runnable interface—and explain why Runnable is generally preferred.

8. SCHEDULING CONSIDERATIONS: Understand thread scheduling models including preemptive versus cooperative multitasking and how thread priorities affect execution order.