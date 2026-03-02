# Thread Libraries


## Table of Contents

- [Thread Libraries](#thread-libraries)
- [Introduction](#introduction)
- [Core Concepts of Thread Libraries](#core-concepts-of-thread-libraries)
  - [1. User-Level Threads (ULT)](#1-user-level-threads-ult)
  - [2. Kernel-Level Threads (KLT)](#2-kernel-level-threads-klt)
- [Prominent Thread Libraries](#prominent-thread-libraries)
  - [1. POSIX Pthreads](#1-posix-pthreads)
  - [2. Windows Threads](#2-windows-threads)
  - [3. Java Threads](#3-java-threads)
- [Comparison of Thread Libraries](#comparison-of-thread-libraries)
- [Implicit vs Explicit Threading](#implicit-vs-explicit-threading)
  - [Thread Pools](#thread-pools)
- [Summary](#summary)
- [Exam Tips](#exam-tips)

## Introduction

In the context of operating systems, a **thread** is a lightweight process—a basic unit of CPU utilization that shares the code section, data section, and other OS resources with other threads of the same process. While the OS provides the underlying support for threads (e.g., the Windows or Linux kernel), the application programmer needs an interface to create and manage these threads. This interface is provided by a **Thread Library**. A thread library offers an API for creating, synchronizing, and managing threads, abstracting the underlying implementation details.

---

## Core Concepts of Thread Libraries

Thread libraries can be implemented in two primary ways:

### 1. User-Level Threads (ULT)

The library is implemented entirely in user space, without kernel support. The kernel is unaware of these threads and sees only a single process. The library code contains all the code for thread creation, scheduling, and management.

- **Example:** The original POSIX **Pthreads** library on Linux systems.
- **Advantages:**
- Fast: Thread switching does not require a mode switch to the kernel.
- Portable: Can run on any OS that supports the library.
- **Disadvantage:**
- The major drawback is that if one user-level thread makes a blocking system call (e.g., I/O request), the entire process is blocked, as the kernel sees only one single-threaded process.

### 2. Kernel-Level Threads (KLT)

The library is implemented with direct support from the operating system. The kernel itself is aware of and manages the threads. The thread library API is essentially a wrapper around system calls provided by the OS.

- **Example:** The Windows thread API.
- **Advantages:**
- The kernel can schedule multiple threads from the same process on multiple CPUs (true parallelism).
- If one thread blocks, the kernel can schedule another thread from the same process.
- **Disadvantage:**
- Slower: Creating and managing threads requires making costly system calls (mode switch to kernel).

Many modern systems use a hybrid approach, combining both ULT and KLT.

## Prominent Thread Libraries

### 1. POSIX Pthreads

Pthreads refers to the POSIX standard (IEEE 1003.1c) defining an API for thread creation and synchronization. It is available on most UNIX-like systems, including Linux and macOS. The implementation can be either user-level or kernel-level.

**Key Pthreads Functions:**

- `pthread_create()`: Creates a new thread.
- `pthread_join()`: Waits for a specified thread to terminate.
- `pthread_exit()`: Terminates the calling thread.
- `pthread_mutex_init()`, `pthread_mutex_lock()`, `pthread_mutex_unlock()`: For synchronization using mutex locks.

**Example — Pthreads program to sum numbers:**

```c
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

int sum; /* shared data between threads */

void *runner(void *param); /* thread function */

int main(int argc, char *argv[]) {
 pthread_t tid; /* thread identifier */
 pthread_attr_t attr; /* thread attributes */

 pthread_attr_init(&attr); /* get default attributes */

 /* create the thread */
 pthread_create(&tid, &attr, runner, argv[1]);

 /* wait for the thread to finish */
 pthread_join(tid, NULL);

 printf("sum = %d\n", sum);
 return 0;
}

/* The thread will execute this function */
void *runner(void *param) {
 int i, upper = atoi(param);
 sum = 0;
 for (i = 1; i <= upper; i++)
 sum += i;
 pthread_exit(0);
}
```

**How this works:**

1. `pthread_create()` creates a new thread that runs the `runner()` function
2. The main thread calls `pthread_join()` to wait for the child thread to finish
3. The child thread computes the sum of 1 to N and stores it in the shared variable `sum`
4. After the child exits, the main thread prints the result

**Compilation:** `gcc -pthread program.c -o program`

### 2. Windows Threads

The Windows API provides a thread library for creating and managing threads on Windows systems. It is a **kernel-level** library — every thread created is known to the kernel.

**Key Windows Thread Functions:**

- `CreateThread()`: Creates a new thread
- `WaitForSingleObject()`: Waits for a thread to finish (similar to `pthread_join`)
- `ExitThread()`: Terminates the calling thread
- `CloseHandle()`: Closes the thread handle

**Example — Windows thread program to sum numbers:**

```c
#include <windows.h>
#include <stdio.h>

DWORD sum; /* shared data */

DWORD WINAPI Summation(LPVOID param) {
 DWORD upper = *(DWORD*)param;
 sum = 0;
 for (DWORD i = 1; i <= upper; i++)
 sum += i;
 return 0;
}

int main(int argc, char *argv[]) {
 DWORD threadId;
 HANDLE threadHandle;
 DWORD upper = atoi(argv[1]);

 /* create the thread */
 threadHandle = CreateThread(
 NULL, /* default security attributes */
 0, /* default stack size */
 Summation, /* thread function */
 &upper, /* parameter to thread function */
 0, /* default creation flags */
 &threadId /* returns the thread identifier */
 );

 /* wait for the thread to finish */
 WaitForSingleObject(threadHandle, INFINITE);

 /* close the thread handle */
 CloseHandle(threadHandle);

 printf("sum = %d\n", sum);
 return 0;
}
```

### 3. Java Threads

Java provides built-in support for threads at the language level. Every Java program has at least one thread (the `main` thread). New threads can be created in two ways:

**Method 1: Extending the `Thread` class**

```java
class Summation extends Thread {
 private int upper;
 private int sum = 0;

 public Summation(int upper) {
 this.upper = upper;
 }

 public void run() {
 for (int i = 1; i <= upper; i++)
 sum += i;
 }

 public int getSum() { return sum; }
}

public class Driver {
 public static void main(String[] args) {
 Summation thread = new Summation(Integer.parseInt(args[0]));
 thread.start(); // start the thread (calls run())
 try {
 thread.join(); // wait for thread to finish
 } catch (InterruptedException e) { }
 System.out.println("sum = " + thread.getSum());
 }
}
```

**Method 2: Implementing the `Runnable` interface**

```java
class Summation implements Runnable {
 private int upper;
 private int sum = 0;

 public Summation(int upper) {
 this.upper = upper;
 }

 public void run() {
 for (int i = 1; i <= upper; i++)
 sum += i;
 }

 public int getSum() { return sum; }
}

public class Driver {
 public static void main(String[] args) {
 Summation task = new Summation(Integer.parseInt(args[0]));
 Thread thread = new Thread(task);
 thread.start();
 try {
 thread.join();
 } catch (InterruptedException e) { }
 System.out.println("sum = " + task.getSum());
 }
}
```

**Key difference:**

- `extends Thread` — simpler but the class cannot extend any other class (Java has single inheritance)
- `implements Runnable` — more flexible, preferred approach since the class can still extend another class

---

## Comparison of Thread Libraries

| Feature             | Pthreads             | Windows Threads         | Java Threads                     |
| :------------------ | :------------------- | :---------------------- | :------------------------------- |
| **Platform**        | UNIX/Linux/macOS     | Windows                 | Any (JVM)                        |
| **Language**        | C/C++                | C/C++                   | Java                             |
| **Implementation**  | User or kernel level | Kernel level            | JVM-managed (maps to OS threads) |
| **Create thread**   | `pthread_create()`   | `CreateThread()`        | `thread.start()`                 |
| **Wait for thread** | `pthread_join()`     | `WaitForSingleObject()` | `thread.join()`                  |
| **Exit thread**     | `pthread_exit()`     | `ExitThread()`          | `run()` returns                  |
| **Portability**     | POSIX systems only   | Windows only            | Cross-platform                   |

---

## Implicit vs Explicit Threading

As multicore systems become common, applications may contain hundreds or thousands of threads. Managing them explicitly becomes difficult. **Implicit threading** transfers the creation and management of threads from the programmer to compilers and runtime libraries.

| Approach                         | Description                                                                                   | Example                                         |
| :------------------------------- | :-------------------------------------------------------------------------------------------- | :---------------------------------------------- |
| **Thread pools**                 | Create a pool of threads at startup; assign tasks to idle threads from the pool               | Java `ExecutorService`, Windows thread pool API |
| **OpenMP**                       | Compiler directives identify parallel regions; compiler generates threaded code automatically | `#pragma omp parallel` in C/C++                 |
| **Grand Central Dispatch (GCD)** | macOS/iOS runtime library that manages thread pools and task scheduling                       | `dispatch_async()`                              |

### Thread Pools

Instead of creating a new thread for every request (expensive), a **thread pool** creates a fixed number of threads at process startup. When a request arrives, it is submitted to the pool. An available thread picks it up. When the thread finishes, it returns to the pool.

```
Requests: Thread Pool:
 R1 ------> [T1] [T2] [T3] [T4] (fixed size)
 R2 ------> T1 picks R1, T2 picks R2
 R3 ------> When T1 finishes R1, it picks R3
```

**Advantages:**

- Faster than creating a new thread for each request (thread already exists)
- Limits the total number of threads (prevents resource exhaustion)
- Separates task creation from task execution (cleaner design)

---

## Summary

| Concept              | Key Point                                                        |
| :------------------- | :--------------------------------------------------------------- |
| Thread library       | API for creating and managing threads                            |
| User-level threads   | Fast switching, but one blocking call blocks the whole process   |
| Kernel-level threads | True parallelism, but slower creation (system call overhead)     |
| Pthreads             | POSIX standard; `pthread_create`, `pthread_join`, `pthread_exit` |
| Windows Threads      | Kernel-level; `CreateThread`, `WaitForSingleObject`              |
| Java Threads         | `extends Thread` or `implements Runnable`; `start()`, `join()`   |
| Thread pools         | Reuse pre-created threads; faster, bounded resource usage        |
| Implicit threading   | Compiler/runtime manages threads (OpenMP, GCD, thread pools)     |

---

## Exam Tips

1. **Write the Pthreads example** — frequently asks you to write a Pthreads program. Memorize the summation example: `pthread_create`, `pthread_join`, shared variable, `runner` function.
2. **Compare all three libraries** — Know the key functions for Pthreads, Windows, and Java threads. Use a comparison table.
3. **`extends Thread` vs `implements Runnable`** — This is a common Java-specific question. Know that `Runnable` is preferred because Java supports single inheritance only.
4. **User-level vs kernel-level** — Classic comparison question. Key trade-off: ULT is fast but blocks entirely on system calls; KLT supports true parallelism but is slower to create.
5. **Thread pools** — Know the three advantages: faster than per-request creation, bounds the number of threads, and separates task from execution.
6. **Implicit threading** — Be able to list and briefly explain thread pools, OpenMP, and GCD as implicit threading approaches.
