# Thread Libraries

## Introduction

Thread libraries are programming interfaces that provide developers with tools to create and manage threads in applications. They abstract the complexity of direct system calls, offering standardized functions for thread operations across different operating systems. In modern computing, where concurrency and parallelism are essential for performance, understanding thread libraries is critical for building efficient software systems.

Thread libraries exist at two primary levels: user-level (managed entirely by user-space runtime libraries) and kernel-level (managed by the operating system kernel). Popular implementations include POSIX Threads (Pthreads), Windows API threads, and Java's Thread class. These libraries enable tasks like web server request handling, real-time data processing, and responsive GUI applications by allowing concurrent execution within a process.

The importance of thread libraries stems from their role in implementing multithreading models (many-to-one, one-to-one, many-to-many). They directly impact application performance, scalability, and resource utilization. For students, mastering this topic provides the foundation for advanced operating system concepts like synchronization, deadlock handling, and distributed computing.

## Key Concepts

### User-Level vs Kernel-Level Thread Libraries

| Feature              | User-Level (e.g., Pthreads)    | Kernel-Level (e.g., Windows API) |
| -------------------- | ------------------------------ | -------------------------------- |
| Management           | Runtime library                | OS Kernel                        |
| Context Switch Speed | Faster (no kernel mode switch) | Slower (requires syscall)        |
| Scalability          | Limited by process resources   | Limited by kernel resources      |
| Blocking Operations  | Blocks entire process          | Blocks only calling thread       |
| Examples             | GNU Portable Threads           | Windows Thread API               |

### Common Thread Operations

1. **Thread Creation**:

- `pthread_create()` in Pthreads
- `CreateThread()` in Windows API
- `Thread.start()` in Java

2. **Thread Termination**:

- Implicit (return from thread function)
- Explicit (`pthread_exit()`, `TerminateThread()`)

3. **Synchronization**:

- Mutexes (`pthread_mutex_lock()`)
- Condition Variables (`pthread_cond_wait()`)
- Semaphores (`sem_wait()`)

4. **Thread Joining**:

- `pthread_join()` blocks until target thread completes
- `WaitForSingleObject()` in Windows

### Multithreading Models

1. **Many-to-One Model**:

- Multiple user threads map to single kernel thread
- Drawback: No true parallelism

2. **One-to-One Model**:

- Each user thread maps to separate kernel thread
- Used in Windows and Linux (via Pthreads)

3. **Many-to-Many Model**:

- Multiplexes user threads to kernel threads
- Balances concurrency and efficiency

## Thread Libraries in Practice

### POSIX Threads (Pthreads)

```c
#include <pthread.h>
// Compile with: gcc -pthread file.c

void* task(void* arg) {
 printf("Thread ID: %lu\n", (unsigned long)pthread_self());
 return NULL;
}

int main() {
 pthread_t t1, t2;
 pthread_create(&t1, NULL, task, NULL);
 pthread_create(&t2, NULL, task, NULL);
 pthread_join(t1, NULL);
 pthread_join(t2, NULL);
}
```

### Windows Thread API

```c
#include <windows.h>

DWORD WINAPI ThreadFunc(LPVOID lpParam) {
 printf("Thread ID: %lu\n", GetCurrentThreadId());
 return 0;
}

int main() {
 HANDLE hThread = CreateThread(NULL, 0, ThreadFunc, NULL, 0, NULL);
 WaitForSingleObject(hThread, INFINITE);
 CloseHandle(hThread);
}
```

### Java Threads

```java
class MyThread implements Runnable {
 public void run() {
 System.out.println("Thread ID: " + Thread.currentThread().getId());
 }
}

public class Main {
 public static void main(String[] args) {
 Thread t1 = new Thread(new MyThread());
 Thread t2 = new Thread(new MyThread());
 t1.start();
 t2.start();
 }
}
```

## Examples

### Example 1: Basic Thread Creation (Pthreads)

**Problem**: Create two threads that print even and odd numbers respectively.

**Solution**:

```c
#include <pthread.h>
#include <stdio.h>

void* print_even(void* arg) {
 for(int i=0; i<=10; i+=2)
 printf("Even: %d\n", i);
 return NULL;
}

void* print_odd(void* arg) {
 for(int i=1; i<=10; i+=2)
 printf("Odd: %d\n", i);
 return NULL;
}

int main() {
 pthread_t t1, t2;
 pthread_create(&t1, NULL, print_even, NULL);
 pthread_create(&t2, NULL, print_odd, NULL);
 pthread_join(t1, NULL);
 pthread_join(t2, NULL);
 return 0;
}
```

**Output**:

```
Even: 0
Odd: 1
Even: 2
Odd: 3
... (interleaved based on scheduler)
```

### Example 2: Synchronization with Mutex

**Problem**: Implement a thread-safe counter shared between two threads.

**Solution**:

```c
#include <pthread.h>

int counter = 0;
pthread_mutex_t lock = PTHREAD_MUTEX_INITIALIZER;

void* increment(void* arg) {
 for(int i=0; i<100000; i++) {
 pthread_mutex_lock(&lock);
 counter++;
 pthread_mutex_unlock(&lock);
 }
 return NULL;
}

int main() {
 pthread_t t1, t2;
 pthread_create(&t1, NULL, increment, NULL);
 pthread_create(&t2, NULL, increment, NULL);
 pthread_join(t1, NULL);
 pthread_join(t2, NULL);
 printf("Final counter: %d\n", counter); // Correctly prints 200000
}
```

## Diagrams (Textual Description)

**Figure 1**: User-Level vs Kernel-Level Threads

```
+-------------------+ +-------------------+
| User Process | | Kernel Space |
| +---------------+ | | +---------------+ |
| | Thread Library | | | | Kernel Threads| |
| +---------------+ | | +---------------+ |
| | Thread 1 | | | | Thread 1 | |
| | Thread 2 | | | | Thread 2 | |
| +---------------+ | | +---------------+ |
+-------------------+ +-------------------+
 User-Level Kernel-Level
```

**Figure 2**: Thread Lifecycle States

```
New → Runnable ↔ Running → Terminated
 ↑ |
 | ↓
 +------ Blocked
```

## Exam Tips

1. **Key Differences**: Memorize 3 differences between user-level and kernel-level threads (management, speed, scalability).

2. **Pthread Functions**:

- `pthread_create()`: 4 parameters (thread ID, attributes, function, args)
- `pthread_join()`: Blocks until specified thread terminates

3. **Synchronization**: Always pair mutex locks with unlocks. Forgetting to unlock causes deadlocks.

4. **Model Identification**: Many-to-one model can't leverage multicore, one-to-one provides true parallelism.

5. **Real-World Use**: Web servers (Apache), databases (MySQL connection threads), GUI applications.

6. **Error Handling**: Check return values of thread functions - `pthread_create()` returns 0 on success.

7. **Portability**: Java threads are platform-independent, while Pthreads and Windows API are OS-specific.
