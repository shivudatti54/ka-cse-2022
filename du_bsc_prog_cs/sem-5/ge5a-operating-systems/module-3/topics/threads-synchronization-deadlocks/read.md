# Threads Synchronization and Deadlocks

## Comprehensive Study Material for Ge5A Operating Systems

---

## 1. Introduction and Real-World Relevance

### What is Thread Synchronization?

Thread synchronization is a fundamental concept in operating systems that deals with coordinating multiple threads to ensure correct and predictable behavior when accessing shared resources. In modern computing, almost all non-trivial applications involve multiple threads executing concurrently. Without proper synchronization, threads can interfere with each other, leading to data corruption, race conditions, and unpredictable results.

### Real-World Relevance

Consider a banking application where multiple ATM machines access the same bank account simultaneously. If two users try to withdraw money from the same account at the same time without synchronization, both might read the same balance, both might withdraw their amounts, and the final balance could be incorrect. This is precisely the type of problem that thread synchronization addresses.

In Delhi University's BSc Physical Science (CS) curriculum under NEP 2024, this topic forms a critical component of Ge5A Operating Systems. Understanding synchronization and deadlocks is essential for developing robust multi-threaded applications and for careers in systems programming, embedded systems, and cloud computing.

---

## 2. Thread Synchronization Fundamentals

### 2.1 The Critical Section Problem

The **critical section** is a portion of code that accesses shared resources (such as shared variables, files, or databases) and must not be concurrently accessed by more than one thread. The critical section problem requires three fundamental conditions to be satisfied:

1. **Mutual Exclusion**: Only one thread can be in the critical section at any given time.
2. **Progress**: If no thread is in the critical section and there are threads waiting to enter, one of the waiting threads must be allowed to enter.
3. **Bounded Waiting**: There must be a limit on the number of times other threads are allowed to enter the critical section after a thread has requested entry.

### 2.2 Synchronization Primitives

#### 2.2.1 Mutex (Mutual Exclusion Lock)

A mutex is the simplest synchronization primitive that provides mutual exclusion. It has two states: locked and unlocked. When a thread locks a mutex, other threads attempting to lock the same mutex will block until it is unlocked.

```c
#include <pthread.h>
#include <stdio.h>
#include <unistd.h>

pthread_mutex_t mutex;
int shared_counter = 0;

void* increment_counter(void* arg) {
    for (int i = 0; i < 100000; i++) {
        pthread_mutex_lock(&mutex);
        shared_counter++;  // Critical section
        pthread_mutex_unlock(&mutex);
    }
    return NULL;
}

int main() {
    pthread_t thread1, thread2;
    pthread_mutex_init(&mutex, NULL);
    
    pthread_create(&thread1, NULL, increment_counter, NULL);
    pthread_create(&thread2, NULL, increment_counter, NULL);
    
    pthread_join(thread1, NULL);
    pthread_join(thread2, NULL);
    
    printf("Final counter value: %d\n", shared_counter);
    pthread_mutex_destroy(&mutex);
    return 0;
}
```

#### 2.2.2 Semaphores

A **semaphore** is a generalized lock that maintains a count and allows multiple threads to access a resource simultaneously up to a specified limit. Semaphores have two operations:
- **wait()** (or P()): Decrements the semaphore count; blocks if count is 0
- **signal()** (or V()): Increments the semaphore count

```c
#include <semaphore.h>
#include <pthread.h>
#include <stdio.h>

sem_t sem;
#define NUM_THREADS 5

void* thread_function(void* arg) {
    int thread_id = *(int*)arg;
    
    printf("Thread %d waiting...\n", thread_id);
    sem_wait(&sem);  // Decrement semaphore
    
    printf("Thread %d entered critical section\n", thread_id);
    sleep(1);  // Simulate work
    
    printf("Thread %d leaving critical section\n", thread_id);
    sem_post(&sem);  // Increment semaphore
    
    return NULL;
}

int main() {
    pthread_t threads[NUM_THREADS];
    int ids[NUM_THREADS];
    
    sem_init(&sem, 0, 2);  // Binary semaphore (count = 2)
    
    for (int i = 0; i < NUM_THREADS; i++) {
        ids[i] = i;
        pthread_create(&threads[i], NULL, thread_function, &ids[i]);
    }
    
    for (int i = 0; i < NUM_THREADS; i++) {
        pthread_join(threads[i], NULL);
    }
    
    sem_destroy(&sem);
    return 0;
}
```

#### 2.2.3 Monitors

A **monitor** is a high-level synchronization construct that combines data and procedures into a single unit. Only one thread can execute any method of the monitor at any time. Monitors provide automatic mutual exclusion and use **condition variables** for waiting and signaling.

```java
// Java-style Monitor Example
public class BankAccount {
    private int balance = 0;
    
    public synchronized void deposit(int amount) {
        balance += amount;
        System.out.println("Deposited: " + amount + ", Balance: " + balance);
        notifyAll();  // Signal waiting threads
    }
    
    public synchronized void withdraw(int amount) throws InterruptedException {
        while (balance < amount) {
            wait();  // Wait until sufficient balance
        }
        balance -= amount;
        System.out.println("Withdrawn: " + amount + ", Balance: " + balance);
    }
    
    public synchronized int getBalance() {
        return balance;
    }
}
```

#### 2.2.4 Condition Variables

Condition variables allow threads to wait for certain conditions to become true. They are always used with a mutex and provide three operations:
- **wait()**: Releases the mutex and blocks until signaled
- **signal()**: Wakes up one waiting thread
- **broadcast()**: Wakes up all waiting threads

---

## 3. Deadlock: Definition and Conditions

### 3.1 What is a Deadlock?

A **deadlock** is a situation where two or more processes are unable to proceed because each is waiting for resources held by the other. Neither process can complete, and the system comes to a standstill.

### 3.2 Coffman Conditions

For a deadlock to occur, all four Coffman conditions must be present:

1. **Mutual Exclusion**: At least one resource must be held in a non-sharable mode.
2. **Hold and Wait**: A process must be holding at least one resource while waiting for other resources.
3. **No Preemption**: Resources cannot be preempted; they can only be released voluntarily.
4. **Circular Wait**: There must be a circular chain of processes, each waiting for a resource held by the next process in the chain.

### 3.3 Resource Allocation Graph (RAG)

A Resource Allocation Graph is a directed graph that depicts which resources are allocated to which processes and which processes are waiting for which resources.

- **Request Edge**: Process → Resource (indicates request)
- **Assignment Edge**: Resource → Process (indicates allocation)

A **cycle** in the RAG indicates a potential deadlock.

---

## 4. Deadlock Handling Strategies

### 4.1 Deadlock Prevention

Prevention ensures that at least one of the Coffman conditions cannot hold:

1. **Eliminate Hold and Wait**: Require processes to request all resources before starting (or release all held resources before requesting new ones).
2. **Eliminate No Preemption**: Allow preemption of resources (not always feasible for all resource types).
3. **Eliminate Circular Wait**: Impose a total ordering of resource types and require processes to request resources in increasing order.

### 4.2 Deadlock Avoidance

Avoidance requires the system to have prior knowledge of resource requirements. The most famous algorithm is the **Banker's Algorithm**.

#### Banker's Algorithm (Detailed Explanation)

The Banker's Algorithm, developed by Edsger Dijkstra, avoids deadlocks by ensuring that the system always remains in a **safe state**. A safe state is one where there exists a sequence of process executions (a safe sequence) that allows all processes to complete without deadlock.

**Key Data Structures:**

1. **MAX[i][j]**: Maximum demand of process i for resource j
2. **allocation[i][j]**: Currently allocated resources to process i
3. **need[i][j]**: Remaining need of process i (MAX - allocation)
4. **available[j]**: Available resources of type j

**Safety Algorithm:**

```
1. Work = Available
2. Finish[i] = false for all processes
3. Find an i such that:
   a. Finish[i] = false
   b. Need[i] <= Work
   If no such i exists, go to step 4
4. Work = Work + Allocation[i]
   Finish[i] = true
   Go to step 3
5. If Finish[i] = true for all i, system is in safe state
```

**Resource Request Algorithm:**

When process P[i] requests resource R[k]:
1. If Request[i] <= Need[i], proceed; else error
2. If Request[i] <= Available, proceed; else process must wait
3. Pretend to allocate:
   Available = Available - Request[i]
   Allocation[i] = Allocation[i] + Request[i]
   Need[i] = Need[i] - Request[i]
4. Run Safety Algorithm
5. If safe, commit the allocation; otherwise, revert

**Example:**

Consider a system with 5 processes (P0-P4) and 3 resource types (A=10, B=5, C=7):

| Process | Allocation (A,B,C) | Max (A,B,C) | Need (A,B,C) |
|---------|-------------------|-------------|--------------|
| P0      | 0,1,0             | 7,5,3       | 7,4,3        |
| P1      | 2,0,0             | 3,2,2       | 1,2,2        |
| P2      | 3,0,2             | 9,0,2       | 6,0,0        |
| P3      | 2,1,1             | 2,2,2       | 0,1,1        |
| P4      | 0,0,2             | 4,3,3       | 4,3,1        |

Available = (3,3,2)

**Finding Safe Sequence:**
- P1 needs (1,2,2) <= Available (3,3,2) ✓ → P1 completes → Available = (5,3,2)
- P3 needs (0,1,1) <= Available (5,3,2) ✓ → P3 completes → Available = (7,4,3)
- P4 needs (4,3,1) <= Available (7,4,3) ✓ → P4 completes → Available = (7,4,5)
- P0 needs (7,4,3) <= Available (7,4,5) ✓ → P0 completes → Available = (7,5,5)
- P2 needs (6,0,0) <= Available (7,5,5) ✓ → P2 completes → Available = (10,5,7)

**Safe Sequence: P1 → P3 → P4 → P0 → P2**

### 4.3 Deadlock Detection and Recovery

**Detection:** Systems can periodically run detection algorithms (similar to Banker's algorithm but without resource requests) to identify deadlocks.

**Recovery Strategies:**
1. **Process Termination**: Abort one or more processes to break the circular wait
2. **Resource Preemption**: Preempt resources from processes (may cause starvation)

---

## 5. Classical Synchronization Problems

### 5.1 Producer-Consumer Problem (Bounded Buffer)

Also known as the **bounded-buffer problem**, this scenario involves producer threads that generate data and consumer threads that consume data, with a shared buffer of finite size.

**Solution using Semaphores:**

```c
#include <semaphore.h>
#include <pthread.h>
#include <stdio.h>
#include <unistd.h>

#define BUFFER_SIZE 5

int buffer[BUFFER_SIZE];
int in = 0, out = 0;

sem_t empty, full;
pthread_mutex_t mutex;

void* producer(void* arg) {
    int item;
    for (int i = 0; i < 10; i++) {
        item = i + 1;  // Produce item
        sem_wait(&empty);  // Wait for empty slot
        pthread_mutex_lock(&mutex);
        
        buffer[in] = item;
        printf("Produced: %d at index %d\n", item, in);
        in = (in + 1) % BUFFER_SIZE;
        
        pthread_mutex_unlock(&mutex);
        sem_post(&full);  // Signal full slot
        sleep(1);
    }
    return NULL;
}

void* consumer(void* arg) {
    int item;
    for (int i = 0; i < 10; i++) {
        sem_wait(&full);  // Wait for full slot
        pthread_mutex_lock(&mutex);
        
        item = buffer[out];
        printf("Consumed: %d from index %d\n", item, out);
        out = (out + 1) % BUFFER_SIZE;
        
        pthread_mutex_unlock(&mutex);
        sem_post(&empty);  // Signal empty slot
        sleep(2);
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

### 5.2 Reader-Writer Problem

Multiple readers can access data simultaneously, but writers need exclusive access.

```c
#include <pthread.h>
#include <semaphore.h>
#include <stdio.h>

int read_count = 0;
pthread_mutex_t read_mutex;
sem_t db;

void* reader(void* arg) {
    int id = *(int*)arg;
    
    pthread_mutex_lock(&read_mutex);
    read_count++;
    if (read_count == 1)
        sem_wait(&db);  // First reader locks database
    pthread_mutex_unlock(&read_mutex);
    
    printf("Reader %d is reading\n", id);
    sleep(1);  // Simulate reading
    
    pthread_mutex_lock(&read_mutex);
    read_count--;
    if (read_count == 0)
        sem_post(&db);  // Last reader unlocks database
    pthread_mutex_unlock(&read_mutex);
    
    return NULL;
}

void* writer(void* arg) {
    int id = *(int*)arg;
    
    sem_wait(&db);  // Exclusive access
    printf("Writer %d is writing\n", id);
    sleep(1);  // Simulate writing
    sem_post(&db);
    
    return NULL;
}
```

### 5.3 Dining Philosophers Problem

Five philosophers sit at a round table, each thinking or eating. They need two forks to eat, but only five forks are available.

**Solution using Semaphores (Hierarchical):**

```c
#include <pthread.h>
#include <semaphore.h>
#include <stdio.h>

#define N 5
#define LEFT (i + N - 1) % N
#define RIGHT (i + 1) % N
#define THINKING 0
#define HUNGRY 1
#define EATING 2

sem_t mutex;
sem_t S[N];
int state[N];

void test(int i) {
    if (state[i] == HUNGRY && 
        state[LEFT] != EATING && 
        state[RIGHT] != EATING) {
        state[i] = EATING;
        sem_post(&S[i]);
    }
}

void pickup(int i) {
    sem_wait(&mutex);
    state[i] = HUNGRY;
    test(i);
    sem_post(&mutex);
    sem_wait(&S[i]);
}

void putdown(int i) {
    sem_wait(&mutex);
    state[i] = THINKING;
    test(LEFT);
    test(RIGHT);
    sem_post(&mutex);
}

void* philosopher(void* arg) {
    int i = *(int*)arg;
    
    while (1) {
        printf("Philosopher %d is thinking\n", i);
        sleep(1);
        pickup(i);
        printf("Philosopher %d is eating\n", i);
        sleep(2);
        putdown(i);
    }
    return NULL;
}

int main() {
    pthread_t threads[N];
    int ids[N];
    
    sem_init(&mutex, 0, 1);
    for (int i = 0; i < N; i++) {
        sem_init(&S[i], 0, 0);
    }
    
    for (int i = 0; i < N; i++) {
        ids[i] = i;
        pthread_create(&threads[i], NULL, philosopher, &ids[i]);
    }
    
    for (int i = 0; i < N; i++) {
        pthread_join(threads[i], NULL);
    }
    
    return 0;
}
```

---

## 6. Application-Level Questions

### Challenging Questions

1. **Question 1**: Consider a system with 4 processes P1, P2, P3, P4 and 3 resource types A(3), B(2), C(2). Given the following snapshot:
   - Max: P1(2,1,1), P2(3,1,2), P3(1,2,1), P4(2,1,1)
   - Allocation: P1(1,0,0), P2(1,1,0), P3(0,1,1), P4(1,1,0)
   
   Using Banker's Algorithm, determine if the system is in a safe state. If yes, find a safe sequence.

2. **Question 2**: In the Dining Philosophers problem, what happens if a philosopher picks up the left fork but finds the right fork unavailable? How does this lead to deadlock, and how does the provided solution prevent this?

3. **Question 3**: Explain why the read-write problem is more complex than the mutual exclusion problem. What are the different priority schemes (readers-preference, writers-preference, fair) and their trade-offs?

4. **Question 4**: A system uses a strict hierarchical ordering of resources (R1 → R2 → R3 → R4) to prevent circular wait. Process P1 requests R1, R3 in that order, while Process P2 requests R2, R4. Can deadlock occur? Justify your answer.

5. **Question 5**: Design a solution to the cigarette smokers problem where three smokers each have infinite supplies of one ingredient (tobacco, paper, matches), and a broker provides the other two ingredients randomly. Only the smoker with the needed ingredient can pick up all three and roll a cigarette.

---

## 7. Multiple Choice Questions (MCQs)

### Select the correct option:

1. **Which of the following is NOT a Coffman condition for deadlock?**
   - a) Mutual Exclusion
   - b) Hold and Wait
   - c) Starvation
   - d) Circular Wait
   
   **Answer: c) Starvation**

2. **In Banker's Algorithm, which data structure represents the remaining resource needs of processes?**
   - a) Allocation Matrix
   - b) Maximum Matrix
   - c) Need Matrix
   - d) Available Vector
   
   **Answer: c) Need Matrix**

3. **What is the primary disadvantage of deadlock prevention?**
   - a) Requires additional hardware
   - b) May lead to low resource utilization
   - c) Is impossible to implement
   - d) Cannot handle all resource types
   
   **Answer: b) May lead to low resource utilization**

4. **In the Producer-Consumer problem with a bounded buffer, which semaphores are typically used?**
   - a) Only mutex
   - b) Binary semaphores for mutual exclusion
   - c) Counting semaphores for empty and full slots
   - d) No semaphores needed
   
   **Answer: c) Counting semaphores for empty and full slots**

5. **A monitor in concurrent programming provides:**
   - a) Only mutual exclusion
   - b) Only condition variables
   - c) Automatic mutual exclusion with condition variables
   - d) No synchronization
   
   **Answer: c) Automatic mutual exclusion with condition variables**

6. **Which of the following is a deadlock avoidance algorithm?**
   - a) Round Robin
   - b) Banker's Algorithm
   - c) FIFO
   - d) LRU
   
   **Answer: b) Banker's Algorithm**

7. **In the Reader-Writer problem, if readers-preference is implemented:**
   - a) Writers may starve
   - b) Readers may starve
   - c) Both may starve equally
   - d) Neither will starve
   
   **Answer: a) Writers may starve**

8. **What is the time complexity of Banker's Algorithm safety check?**
   - O(n²m)
   - O(nm²)
   - O(n + m)
   - O(nm)
   
   **Answer: O(nm)**

9. **A deadlock is a situation where:**
   - a) Processes wait for CPU time
   - b) Processes are blocked waiting for each other
   - c) The system crashes
   - d) Processes complete successfully
   
   **Answer: b) Processes are blocked waiting for each other**

10. **The critical section problem requires:**
    - a) Only mutual exclusion
    - b) Only progress
    - c) Mutual exclusion, progress, and bounded waiting
    - d) No conditions
    
    **Answer: c) Mutual exclusion, progress, and bounded waiting**

---

## 8. Flashcards for Quick Review

### Flashcard 1
**Term:** Critical Section
**Definition:** A portion of code that accesses shared resources and must not be concurrently accessed by more than one thread.

### Flashcard 2
**Term:** Mutual Exclusion
**Definition:** The property that ensures only one thread can be in the critical section at any given time.

### Flashcard 3
**Term:** Deadlock
**Definition:** A state where two or more processes are unable to proceed because each is waiting for resources held by the other.

### Flashcard 4
**Term:** Coffman Conditions
**Definition:** Four necessary conditions for deadlock: Mutual Exclusion, Hold and Wait, No Preemption, and Circular Wait.

### Flashcard 5
**Term:** Banker's Algorithm
**Definition:** A deadlock avoidance algorithm that ensures the system always remains in a safe state by checking resource requests against available resources.

### Flashcard 6
**Term:** Safe State
**Definition:** A state where there exists a sequence of process executions that allows all processes to complete without deadlock.

### Flashcard 7
**Term:** Semaphore
**Definition:** A synchronization primitive with an integer value and two atomic operations: wait() and signal().

### Flashcard 8
**Term:** Monitor
**Definition:** A high-level synchronization construct combining data and procedures where only one thread can execute any method at a time.

### Flashcard 9
**Term:** Race Condition
**Definition:** A situation where the behavior of a program depends on the relative timing of interleaved operations.

### Flashcard 10
**Term:** Bounded Waiting
**Definition:** The requirement that there must be a limit on the number of times other processes can enter the critical section after a process has requested entry.

### Flashcard 11
**Term:** Condition Variable
**Definition:** A synchronization primitive that allows threads to wait for certain conditions to become true, used with mutexes.

### Flashcard 12
**Term:** Resource Allocation Graph
**Definition:** A directed graph depicting resource allocation to processes, used for deadlock detection.

---

## 9. Key Takeaways

1. **Thread Synchronization** is essential for correct multi-threaded programming, ensuring that shared resources are accessed safely through **mutual exclusion**.

2. **Synchronization Primitives** include:
   - **Mutex**: Binary lock for mutual exclusion
   - **Semaphore**: Counting lock allowing multiple concurrent accesses
   - **Monitor**: High-level construct with automatic mutual exclusion
   - **Condition Variables**: For thread waiting and signaling

3. **Deadlock** occurs when all four Coffman conditions are satisfied: Mutual Exclusion, Hold and Wait, No Preemption, and Circular Wait.

4. **Deadlock Handling Strategies**:
   - **Prevention**: Eliminate one of the Coffman conditions
   - **Avoidance**: Use Banker's Algorithm to maintain safe states
   - **Detection and Recovery**: Periodically check for deadlocks and recover

5. **Banker's Algorithm** is a fundamental deadlock avoidance algorithm that requires knowledge of maximum resource needs and maintains the system in a safe state.

6. **Classical Problems** like Producer-Consumer, Reader-Writer, and Dining Philosophers illustrate the practical challenges of synchronization.

7. **Code Examples** demonstrate how synchronization primitives are used in real programs to prevent race conditions and deadlocks.

8. For the **Delhi University Ge5A Operating Systems** syllabus, focus on understanding the theoretical foundations and being able to apply algorithms like Banker's Algorithm to determine system states.

---

*Generated for BSc Physical Science (CS) - Delhi University, NEP 2024*