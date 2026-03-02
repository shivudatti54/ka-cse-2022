# Threads and Multithreading Models

## Introduction
Modern operating systems leverage threads as fundamental units of CPU utilization. A thread is a lightweight process that shares memory space with other threads in the same process, enabling efficient concurrent execution. Multithreading improves application responsiveness, resource utilization, and performance on multi-core systems.

The importance of threads stems from their ability to:
1. Reduce context-switching overhead compared to processes
2. Enable parallel execution in data-intensive applications
3. Simplify complex server architectures (e.g., web servers handling concurrent requests)

Multithreading models define relationships between user-level threads and kernel-level threads. Three primary models (many-to-one, one-to-one, many-to-many) balance flexibility and efficiency based on application requirements and OS capabilities.

## Key Concepts
1. **User Threads**: Managed entirely in user space via thread libraries (Pthreads, Java Threads)
2. **Kernel Threads**: OS-managed threads with direct scheduler awareness
3. **Multithreading Models**:
   - **Many-to-One**: Multiple user threads map to single kernel thread (lightweight but no true parallelism)
   - **One-to-One**: Each user thread maps to kernel thread (true parallelism, higher overhead)
   - **Many-to-Many**: Multiplexes user threads to kernel threads (balance concurrency and efficiency)
4. **Thread Libraries**:
   - POSIX Threads (pthreads): C-based, OS-independent
   - Java Threads: Platform-independent using JVM
   - Windows Thread API: Kernel-level threads with rich synchronization
5. **Thread States**: Ready, Running, Blocked, Terminated
6. **Synchronization**: Mutexes, semaphores, and condition variables to prevent race conditions

## Examples

**Example 1: Web Server Thread Pool**
```java
class WebServer {
    public static void main(String[] args) {
        ExecutorService pool = Executors.newFixedThreadPool(100);
        while (true) {
            Socket connection = serverSocket.accept();
            pool.execute(new RequestHandler(connection));
        }
    }
}
```
*Step-by-Step:*
1. Creates thread pool with 100 worker threads (many-to-many model)
2. Accepts incoming HTTP connections
3. Assigns each request to available thread
4. Reuses threads to avoid creation/destruction overhead

**Example 2: Matrix Multiplication Using Threads**
```c
void *multiply(void *arg) {
    int core = (int)arg;
    for (int i = core * rows_per_thread; i < (core+1)*rows_per_thread; i++) 
        for (int j = 0; j < COLS; j++)
            result[i][j] = mat1[i][k] * mat2[k][j];
}

int main() {
    pthread_t threads[NUM_CORES];
    for (int i = 0; i < NUM_CORES; i++)
        pthread_create(&threads[i], NULL, multiply, (void*)i);
    // Join threads
}
```
*Step-by-Step:*
1. Divide matrix rows among available CPU cores
2. Create kernel-level threads (one-to-one model)
3. Each thread computes portion of result matrix
4. Combine results after thread completion

**Example 3: Producer-Consumer Problem**
```python
from threading import Thread, Semaphore

buffer = []
mutex = Semaphore(1)
empty = Semaphore(10)
full = Semaphore(0)

def producer():
    while True:
        item = produce_item()
        empty.acquire()
        mutex.acquire()
        buffer.append(item)
        mutex.release()
        full.release()

def consumer():
    while True:
        full.acquire()
        mutex.acquire()
        item = buffer.pop(0)
        mutex.release()
        empty.release()
        consume(item)
```
*Step-by-Step:*
1. Use counting semaphores for buffer slots
2. Mutex ensures atomic buffer access
3. Producers block when buffer full
4. Consumers block when buffer empty

## Exam Tips
1. Always mention **Amdahl's Law** when discussing multithreading benefits
2. Compare thread models using parameters: scalability, parallelism, overhead
3. For synchronization questions, distinguish between mutex (binary semaphore) and counting semaphore
4. In numerical problems, calculate optimal thread count using:  
   `Optimal Threads = Number of Cores × (1 + Wait Time/Compute Time)`
5. Remember Windows uses one-to-one model; Solaris uses many-to-many
6. When asked about context switching: thread switching is 5-100x faster than process switching
7. For "zombie threads" questions: emphasize proper join()/detach() handling