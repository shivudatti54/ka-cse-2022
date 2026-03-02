# Multithreading Models and Libraries

## Introduction to Multithreading

Multithreading is a fundamental concept in modern operating systems that allows a single process to execute multiple threads concurrently. Each thread represents an independent flow of execution within the same process, sharing the process's resources like memory space, code, and open files while having its own stack, registers, and program counter.

**Key benefits of multithreading:**

- Responsiveness: Applications remain responsive even when part of the program is blocked
- Resource sharing: Threads share process resources efficiently
- Economy: Thread creation is faster and cheaper than process creation
- Scalability: Better utilization of multiprocessor architectures

## Thread Concepts

### User Threads vs Kernel Threads

Threads can be implemented at two different levels:

**User Threads:** Managed entirely by user-level libraries without kernel support. The operating system sees only the process, not the individual threads.

```
+-----------------------+
| Application |
+-----------------------+
| User Thread Library |← Manages user threads
+-----------------------+
| Kernel |← Sees only one process
+-----------------------+
```

**Kernel Threads:** Supported and managed directly by the operating system kernel. The kernel is aware of all threads and schedules them individually.

```
+-----------------------+
| Application |
+-----------------------+
| Kernel |← Manages and schedules kernel threads
+-----------------------+
```

### Comparison Table: User vs Kernel Threads

| Aspect     | User Threads                                           | Kernel Threads                      |
| ---------- | ------------------------------------------------------ | ----------------------------------- |
| Management | User-level library                                     | Operating System                    |
| Speed      | Fast creation/context switch                           | Slower creation/context switch      |
| Blocking   | Entire process blocks if one thread blocks             | Other threads can run if one blocks |
| Scheduling | User library schedules threads                         | OS schedules threads                |
| Examples   | POSIX Pthreads, Java threads (in some implementations) | Windows threads, Linux threads      |

## Multithreading Models

The relationship between user threads and kernel threads is defined by multithreading models, which determine how user-level threads are mapped to kernel-level threads.

### 1. Many-to-One Model

In this model, many user-level threads are mapped to a single kernel thread. Thread management is done by the thread library in user space.

```
User Space: [UT1] [UT2] [UT3] [UT4] → Many user threads
 ↓ ↓ ↓ ↓
Kernel Space: [KT1] → Single kernel thread
```

**Characteristics:**

- Efficient since thread management occurs in user space
- Entire process blocks if any thread makes a blocking system call
- Cannot take advantage of multiprocessing (runs on only one CPU)
- **Example:** Green threads in older Java versions

### 2. One-to-One Model

Each user-level thread maps to a separate kernel thread. This provides true concurrency.

```
User Space: [UT1] [UT2] [UT3] [UT4] → Multiple user threads
 ↓ ↓ ↓ ↓
Kernel Space: [KT1] [KT2] [KT3] [KT4] → Multiple kernel threads
```

**Characteristics:**

- Provides better concurrency since blocking calls don't affect other threads
- Can leverage multiple processors effectively
- Overhead of creating kernel threads may be significant
- **Examples:** Windows NT/XP, Linux, modern Java implementations

### 3. Many-to-Many Model

Multiple user threads are multiplexed to a smaller or equal number of kernel threads. This model offers the best of both approaches.

```
User Space: [UT1] [UT2] [UT3] [UT4] [UT5] [UT6] → Many user threads
 ↓ ↓ ↓ ↓ ↓ ↓
Kernel Space: [KT1] [KT2] [KT3] → Fewer kernel threads
```

**Characteristics:**

- Developers can create as many user threads as necessary
- Kernel threads can run in parallel on multiprocessors
- Operating system can adjust the number of kernel threads
- **Examples:** Solaris, IRIX, HP-UX

### Two-Level Model (Hybrid Model)

A variation of the Many-to-Many model that allows some user threads to be bound to specific kernel threads (one-to-one relationship) while others are multiplexed (many-to-many).

```
User Space: [UT1] [UT2] [UT3] [UT4] [UT5] [UT6]
 ↓ ↓ ↓ ↓ ↓ ↓
Kernel Space: [KT1] [KT2] [KT3] [KT4]
```

**Characteristics:**

- Combines benefits of one-to-one and many-to-many models
- Allows critical threads to have dedicated kernel resources
- **Examples:** Solaris 2.x, Windows 7/8/10 with thread pools

## Thread Libraries

Thread libraries provide programmers with an API for creating and managing threads. There are three main approaches to implementing thread libraries.

### 1. User-Level Thread Libraries

Implemented entirely in user space with no kernel support. The library contains code for creating, destroying, scheduling, and managing threads.

**Advantages:**

- Fast thread operations (no system calls needed)
- Portable across different operating systems
- Customizable scheduling algorithms

**Disadvantages:**

- Blocking system calls block all threads in the process
- Cannot utilize multiple processors

**Examples:**

- POSIX Pthreads (in user-mode implementations)
- Earlier Java thread implementations

### 2. Kernel-Level Thread Libraries

Implemented with direct kernel support. The library API invokes system calls for thread operations.

**Advantages:**

- True parallelism on multiprocessor systems
- Blocking calls don't affect other threads
- OS can schedule threads intelligently

**Disadvantages:**

- Thread operations are slower due to system call overhead
- Less portable across different operating systems

**Examples:**

- Windows Thread API
- Linux threads (via clone() system call)
- Modern POSIX Pthreads implementations

### 3. Hybrid Approach

Combines user-level and kernel-level approaches, typically using kernel threads but implementing some functionality in user space.

## Popular Thread Libraries

### POSIX Threads (Pthreads)

A standardized programming interface for thread manipulation available on most UNIX-like systems.

**Key Functions:**

- `pthread_create()`: Create a new thread
- `pthread_join()`: Wait for a thread to terminate
- `pthread_exit()`: Terminate the calling thread
- `pthread_mutex_init()`: Initialize a mutex for synchronization

**Example:**

```c
#include <pthread.h>
#include <stdio.h>

void* print_message(void* message) {
 printf("%s\n", (char*)message);
 return NULL;
}

int main() {
 pthread_t thread1, thread2;
 char* message1 = "Thread 1";
 char* message2 = "Thread 2";

 pthread_create(&thread1, NULL, print_message, (void*)message1);
 pthread_create(&thread2, NULL, print_message, (void*)message2);

 pthread_join(thread1, NULL);
 pthread_join(thread2, NULL);

 return 0;
}
```

### Windows Thread API

Microsoft's native threading API for Windows systems.

**Key Functions:**

- `CreateThread()`: Create a new thread
- `WaitForSingleObject()`: Wait for a thread to complete
- `ExitThread()`: Terminate the calling thread
- `CloseHandle()`: Close thread handle

**Example:**

```c
#include <windows.h>
#include <stdio.h>

DWORD WINAPI ThreadFunction(LPVOID lpParam) {
 printf("Thread executed with parameter: %s\n", (char*)lpParam);
 return 0;
}

int main() {
 HANDLE hThread;
 DWORD threadId;
 char* data = "Hello from thread";

 hThread = CreateThread(NULL, 0, ThreadFunction, data, 0, &threadId);
 WaitForSingleObject(hThread, INFINITE);
 CloseHandle(hThread);

 return 0;
}
```

### Java Threads

Java provides built-in support for multithreading through the `java.lang.Thread` class and `Runnable` interface.

**Two approaches to create threads:**

1. Extending the Thread class
2. Implementing the Runnable interface

**Example using Runnable:**

```java
class MyRunnable implements Runnable {
 public void run() {
 System.out.println("Thread is running");
 }
}

public class ThreadExample {
 public static void main(String[] args) {
 Thread thread = new Thread(new MyRunnable());
 thread.start();

 try {
 thread.join();
 } catch (InterruptedException e) {
 e.printStackTrace();
 }
 }
}
```

## Threading Issues

### 1. The fork() and exec() System Calls

The behavior of these system calls in multithreaded programs requires special consideration:

- **fork()**: Should it duplicate all threads or only the calling thread?
- **exec()**: Typically replaces the entire process, including all threads

Most UNIX systems provide two versions of fork():

- `fork()`: Duplicates only the calling thread
- `fork_all()`: Duplicates all threads in the process

### 2. Signal Handling

Signals are used in UNIX systems to notify processes of events. In multithreaded environments, questions arise:

- Which thread should handle the signal?
- Should signals be delivered to all threads or specific ones?

Common approaches:

- Deliver the signal to the thread to which it applies
- Deliver the signal to every thread in the process
- Deliver the signal to certain threads only
- Assign a specific thread to receive all signals

### 3. Thread Cancellation

Terminating a thread before it has completed is called thread cancellation. Two types:

1. **Asynchronous cancellation**: Immediately terminates the target thread
2. **Deferred cancellation**: Allows the target thread to periodically check if it should cancel

Deferred cancellation is generally safer as it allows the thread to release resources properly.

### 4. Thread-Local Storage

Thread-local storage (TLS) allows each thread to have its own copy of data. Useful when data should not be shared between threads.

**Example in Pthreads:**

```c
pthread_key_t key;

void* thread_function(void* arg) {
 int* data = malloc(sizeof(int));
 *data = 42;
 pthread_setspecific(key, data);
 // ... use thread-specific data ...
 free(data);
 return NULL;
}
```

## Thread Scheduling

Thread scheduling involves deciding which threads to execute and when. The approach varies based on the threading model:

### User-Level Thread Scheduling

- The thread library schedules user threads
- The kernel is unaware of user threads
- Scheduling algorithm is implemented in user space

### Kernel-Level Thread Scheduling

- The kernel schedules kernel threads
- Can use standard CPU scheduling algorithms
- Aware of thread priorities and relationships

## Exam Tips

1. **Remember the mapping patterns**: Focus on understanding how many-to-one, one-to-one, and many-to-many models differ in their user-to-kernel thread mappings.

2. **Compare advantages/disadvantages**: Be prepared to discuss trade-offs between different threading models and libraries, especially regarding performance, blocking behavior, and multiprocessor utilization.

3. **Know the APIs**: Familiarize yourself with basic functions of major thread libraries (Pthreads, Windows, Java), but you won't need to memorize exact syntax.

4. **Understand threading issues**: Be able to explain challenges like fork/exec behavior, signal handling, and thread cancellation in multithreaded environments.

5. **Focus on practical implications**: Think about how different models affect real-world application performance and design decisions.
