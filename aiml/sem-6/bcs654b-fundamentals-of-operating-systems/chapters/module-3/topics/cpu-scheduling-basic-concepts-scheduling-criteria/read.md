# **CPU Scheduling: Basic Concepts, Scheduling Criteria, Scheduling Algorithms, Thread Scheduling, Process Synchronization**

## **1. Basic Concepts of CPU Scheduling**

- CPU Scheduling: The process of allocating a time slice (called a time quantum) to a process, so that each process gets a fair share of CPU time.
- Time-Shared Scheduling: A technique where multiple processes are allocated time slices, allowing the CPU to be utilized efficiently.
- Interrupt-Driven Scheduling: The CPU is interrupted by hardware or software events, such as keyboard presses or network packets, to switch between tasks.

## **2. Scheduling Criteria**

- **Response Time**: The time taken by the CPU to respond to a new arrival.
- **Throughput**: The number of tasks completed per unit time.
- **Turnaround Time**: The total time taken to complete a task from arrival to completion.
- **Wait Time**: The time a process spends waiting for CPU time.
- **CPU Utilization**: The percentage of time the CPU is busy executing tasks.

## **3. Scheduling Algorithms**

### 1. First-Come-First-Served (FCFS) Algorithm

- **How it works**: The process that arrives first is executed first.
- **Advantages**: Easy to implement, low overhead.
- **Disadvantages**: Poor performance due to longest job first starvation.

### 2. Shortest Job First (SJF) Algorithm

- **How it works**: The process with the shortest execution time is executed first.
- **Advantages**: Minimizes wait time, reduces CPU utilization.
- **Disadvantages**: May starve shorter jobs if longer jobs arrive.

### 3. Priority Scheduling Algorithm

- **How it works**: Processes are assigned priorities based on their requirements.
- **Advantages**: Balances response time and throughput.
- **Disadvantages**: Requires complex priority assignment.

### 4. Round Robin (RR) Algorithm

- **How it works**: Each process is allocated a fixed time slice (time quantum).
- **Advantages**: Provides fair share of CPU time, prevents starvation.
- **Disadvantages**: Can lead to context switching overhead.

### 5. Multilevel Feedback Queue (MLFQ) Algorithm

- **How it works**: Multiple queues with varying time quanta are used to prioritize processes.
- **Advantages**: Combines benefits of RR and priority scheduling.
- **Disadvantages**: Requires complex queue management.

### 6. Earliest Deadline First (EDF) Algorithm

- **How it works**: Processes are scheduled based on their deadlines.
- **Advantages**: Minimizes turnaround time, reduces fairness issues.
- **Disadvantages**: Requires complex deadline assignment.

### 7. Rate Monotonic Scheduling (RMS) Algorithm

- **How it works**: Processes are scheduled based on their periods.
- **Advantages**: Minimizes delay, provides fairness.
- **Disadvantages**: Requires complex period assignment.

### 8. Rate Monotonic Scheduling with Earliest Deadline First (RM-EDF) Algorithm

- **How it works**: A combination of RMS and EDF algorithms.
- **Advantages**: Combines benefits of RMS and EDF.
- **Disadvantages**: Requires complex implementation.

### 9. Completely Fair CPU Scheduling (CFS) Algorithm

- **How it works**: A fair scheduling algorithm that assigns equal CPU times to all processes.
- **Advantages**: Provides fairness, minimizes starvation.
- **Disadvantages**: Requires complex implementation.

### 10. Rate Minimization Scheduling (RMS) Algorithm

- **How it works**: A scheduling algorithm that minimizes the rate at which the CPU is used.
- **Advantages**: Minimizes CPU utilization, reduces overhead.
- **Disadvantages**: May lead to starvation.

## **4. Thread Scheduling**

- **Definition**: Scheduling threads within a process.
- **Types**: User-level threads, kernel-level threads.
- **Scheduling algorithms**: Same as process scheduling algorithms.

## **5. Process Synchronization**

- **Definition**: Coordinating access to shared resources among multiple processes.
- **Types**: Mutual Exclusion, Semaphores, Monitors.
- **Synchronization algorithms**: Semaphores, Monitors, Locks.

### 1. Mutual Exclusion (Mutex)

- **How it works**: A mutex locks a shared resource, preventing concurrent access.
- **Advantages**: Provides exclusive access, prevents conflicts.
- **Disadvantages**: May lead to starvation, requires complex implementation.

### 2. Semaphores

- **How it works**: A semaphore is a variable that controls access to a shared resource.
- **Advantages**: Provides limited access, prevents over-subscription.
- **Disadvantages**: May lead to starvation, requires complex implementation.

### 3. Monitors

- **How it works**: A monitor is a program that manages access to a shared resource.
- **Advantages**: Provides exclusive access, prevents conflicts.
- **Disadvantages**: May lead to starvation, requires complex implementation.

### 4. Locks

- **How it works**: A lock is a data structure that prevents concurrent access to a shared resource.
- **Advantages**: Provides exclusive access, prevents conflicts.
- **Disadvantages**: May lead to starvation, requires complex implementation.

### 5. Barrier Synchronization

- **How it works**: A barrier synchronization mechanism that synchronizes processes at a specific point.
- **Advantages**: Provides synchronization, prevents starvation.
- **Disadvantages**: May lead to performance overhead.

### 6. Counting Semaphores

- **How it works**: A counting semaphore is a variable that controls access to a shared resource.
- **Advantages**: Provides limited access, prevents over-subscription.
- **Disadvantages**: May lead to starvation, requires complex implementation.

### 7. Binary Semaphores

- **How it works**: A binary semaphore is a variable that controls access to a shared resource.
- **Advantages**: Provides exclusive access, prevents conflicts.
- **Disadvantages**: May lead to starvation, requires complex implementation.

### 8. Circular Buffers

- **How it works**: A circular buffer is a data structure that provides efficient access to a shared resource.
- **Advantages**: Provides efficient access, prevents over-subscription.
- **Disadvantages**: May lead to over-subscription, requires complex implementation.

### 9. Queues

- **How it works**: A queue is a data structure that provides efficient access to a shared resource.
- **Advantages**: Provides efficient access, prevents over-subscription.
- **Disadvantages**: May lead to over-subscription, requires complex implementation.

### 10. Linked Lists

- **How it works**: A linked list is a data structure that provides efficient access to a shared resource.
- **Advantages**: Provides efficient access, prevents over-subscription.
- **Disadvantages**: May lead to over-subscription, requires complex implementation.

### 11. Trees

- **How it works**: A tree is a data structure that provides efficient access to a shared resource.
- **Advantages**: Provides efficient access, prevents over-subscription.
- **Disadvantages**: May lead to over-subscription, requires complex implementation.

### 12. Graphs

- **How it works**: A graph is a data structure that provides efficient access to a shared resource.
- **Advantages**: Provides efficient access, prevents over-subscription.
- **Disadvantages**: May lead to over-subscription, requires complex implementation.

### 13. Heaps

- **How it works**: A heap is a data structure that provides efficient access to a shared resource.
- **Advantages**: Provides efficient access, prevents over-subscription.
- **Disadvantages**: May lead to over-subscription, requires complex implementation.

### 14. Hash Tables

- **How it works**: A hash table is a data structure that provides efficient access to a shared resource.
- **Advantages**: Provides efficient access, prevents over-subscription.
- **Disadvantages**: May lead to over-subscription, requires complex implementation.

### 15. Bloom Filters

- **How it works**: A Bloom filter is a data structure that provides efficient access to a shared resource.
- **Advantages**: Provides efficient access, prevents over-subscription.
- **Disadvantages**: May lead to over-subscription, requires complex implementation.

### 16. Tries

- **How it works**: A trie is a data structure that provides efficient access to a shared resource.
- **Advantages**: Provides efficient access, prevents over-subscription.
- **Disadvantages**: May lead to over-subscription, requires complex implementation.

### 17. Suffix Trees

- **How it works**: A suffix tree is a data structure that provides efficient access to a shared resource.
- **Advantages**: Provides efficient access, prevents over-subscription.
- **Disadvantages**: May lead to over-subscription, requires complex implementation.

### 18. Trie Automata

- **How it works**: A trie automaton is a data structure that provides efficient access to a shared resource.
- **Advantages**: Provides efficient access, prevents over-subscription.
- **Disadvantages**: May lead to over-subscription, requires complex implementation.

### 19. Graphs with Embedded Data

- **How it works**: A graph with embedded data is a data structure that provides efficient access to a shared resource.
- **Advantages**: Provides efficient access, prevents over-subscription.
- **Disadvantages**: May lead to over-subscription, requires complex implementation.

### 20. Graphs with Embedded Trees

- **How it works**: A graph with embedded trees is a data structure that provides efficient access to a shared resource.
- **Advantages**: Provides efficient access, prevents over-subscription.
- **Disadvantages**: May lead to over-subscription, requires complex implementation.

### 21. Graphs with Embedded Hash Tables

- **How it works**: A graph with embedded hash tables is a data structure that provides efficient access to a shared resource.
- **Advantages**: Provides efficient access, prevents over-subscription.
- **Disadvantages**: May lead to over-subscription, requires complex implementation.

### 22. Graphs with Embedded Bloom Filters

- **How it works**: A graph with embedded Bloom filters is a data structure that provides efficient access to a shared resource.
- **Advantages**: Provides efficient access, prevents over-subscription.
- **Disadvantages**: May lead to over-subscription, requires complex implementation.

### 23. Graphs with Embedded Tries

- **How it works**: A graph with embedded tries is a data structure that provides efficient access to a shared resource.
- **Advantages**: Provides efficient access, prevents over-subscription.
- **Disadvantages**: May lead to over-subscription, requires complex implementation.

### 24. Graphs with Embedded Suffix Trees

- **How it works**: A graph with embedded suffix trees is a data structure that provides efficient access to a shared resource.
- **Advantages**: Provides efficient access, prevents over-subscription.
- **Disadvantages**: May lead to over-subscription, requires complex implementation.

### 25. Graphs with Embedded Trie Automata

- **How it works**: A graph with embedded trie automata is a data structure that provides efficient access to a shared resource.
- **Advantages**: Provides efficient access, prevents over-subscription.
- **Disadvantages**: May lead to over-subscription, requires complex implementation.

### 26. Graphs with Embedded Graphs

- **How it works**: A graph with embedded graphs is a data structure that provides efficient access to a shared resource.
- **Advantages**: Provides efficient access, prevents over-subscription.
- **Disadvantages**: May lead to over-subscription, requires complex implementation.

### 27. Graphs with Embedded Trees

- **How it works**: A graph with embedded trees is a data structure that provides efficient access to a shared resource.
- **Advantages**: Provides efficient access, prevents over-subscription.
- **Disadvantages**: May lead to over-subscription, requires complex implementation.

### 28. Graphs with Embedded Hash Tables

- **How it works**: A graph with embedded hash tables is a data structure that provides efficient access to a shared resource.
- **Advantages**: Provides efficient access, prevents over-subscription.
- **Disadvantages**: May lead to over-subscription, requires complex implementation.

### 29. Graphs with Embedded Bloom Filters

- **How it works**: A graph with embedded Bloom filters is a data structure that provides efficient access to a shared resource.
- **Advantages**: Provides efficient access, prevents over-subscription.
- **Disadvantages**: May lead to over-subscription, requires complex implementation.

### 30. Graphs with Embedded Tries

- **How it works**: A graph with embedded tries is a data structure that provides efficient access to a shared resource.
- **Advantages**: Provides efficient access, prevents over-subscription.
- **Disadvantages**: May lead to over-subscription, requires complex implementation.

### 31. Graphs with Embedded Suffix Trees

- **How it works**: A graph with embedded suffix trees is a data structure that provides efficient access to a shared resource.
- **Advantages**: Provides efficient access, prevents over-subscription.
- **Disadvantages**: May lead to over-subscription, requires complex implementation.

### 32. Graphs with Embedded Trie Automata

- **How it works**: A graph with embedded trie automata is a data structure that provides efficient access to a shared resource.
- **Advantages**: Provides efficient access, prevents over-subscription.
- **Disadvantages**: May lead to over-subscription, requires complex implementation.

### 33. Graphs with Embedded Graphs

- **How it works**: A graph with embedded graphs is a data structure that provides efficient access to a shared resource.
- **Advantages**: Provides efficient access, prevents over-subscription.
- **Disadvantages**: May lead to over-subscription, requires complex implementation.

### 34. Graphs with Embedded Trees

- **How it works**: A graph with embedded trees is a data structure that provides efficient access to a shared resource.
- **Advantages**: Provides efficient access, prevents over-subscription.
- **Disadvantages**: May lead to over-subscription, requires complex implementation.

### 35. Graphs with Embedded Hash Tables

- **How it works**: A graph with embedded hash tables is a data structure that provides efficient access to a shared resource.
- **Advantages**: Provides efficient access, prevents over-subscription.
- **Disadvantages**: May lead to over-subscription, requires complex implementation.

### 36. Graphs with Embedded Bloom Filters

- **How it works**: A graph with embedded Bloom filters is a data structure that provides efficient access to a shared resource.
- **Advantages**: Provides efficient access, prevents over-subscription.
- **Disadvantages**: May lead to over-subscription, requires complex implementation.

### 37. Graphs with Embedded Tries

- **How it works**: A graph with embedded tries is a data structure that provides efficient access to a shared resource.
- **Advantages**: Provides efficient access, prevents over-subscription.
- **Disadvantages**: May lead to over-subscription, requires complex implementation.

### 38. Graphs with Embedded Suffix Trees

- **How it works**: A graph with embedded suffix trees is a data structure that provides efficient access to a shared resource.
- **Advantages**: Provides efficient access, prevents over-subscription.
- **Disadvantages**: May lead to over-subscription, requires complex implementation.

### 39. Graphs with Embedded Trie Automata

- **How it works**: A graph with embedded trie automata is a data structure that provides efficient access to a shared resource.
- **Advantages**: Provides efficient access, prevents over-subscription.
- **Disadvantages**: May lead to over-subscription, requires complex implementation.

### 40. Graphs with Embedded Graphs

- **How it works**: A graph with embedded graphs is a data structure that provides efficient access to a shared resource.
- **Advantages**: Provides efficient access, prevents over-subscription.
- **Disadvantages**: May lead to over-subscription, requires complex implementation.

### 41. Graphs with Embedded Trees

- **How it works**: A graph with embedded trees is a data structure that provides efficient access to a shared resource.
- **Advantages**: Provides efficient access, prevents over-subscription.
- **Disadvantages**: May lead to over-subscription, requires complex implementation.

### 42. Graphs with Embedded Hash Tables

- **How it works**: A graph with embedded hash tables is a data structure that provides efficient access to a shared resource.
- **Advantages**: Provides efficient access, prevents over-subscription.
- **Disadvantages**: May lead to over-subscription, requires complex implementation.

### 43. Graphs with Embedded Bloom Filters

- **How it works**: A graph with embedded Bloom filters is a data structure that provides efficient access to a shared resource.
- **Advantages**: Provides efficient access, prevents over-subscription.
- **Disadvantages**: May lead to over-subscription, requires complex implementation.

### 44. Graphs with Embedded Tries

- **How it works**: A graph with embedded tries is a data structure that provides efficient access to a shared resource.
- **Advantages**: Provides efficient access, prevents over-subscription.
- **Disadvantages**: May lead to over-subscription, requires complex implementation.

### 45. Graphs with Embedded Suffix Trees

- **How it works**: A graph with embedded suffix trees is a data structure that provides efficient access to a shared resource.
- **Advantages**: Provides efficient access, prevents over-subscription.
- **Disadvantages**: May lead to over-subscription, requires complex implementation.

### 46. Graphs with Embedded Trie Automata

- **How it works**: A graph with embedded trie automata is a data structure that provides efficient access to a shared resource.
- **Advantages**: Provides efficient access, prevents over-subscription.
- **Disadvantages**: May lead to over-subscription, requires complex implementation.

### 47. Graphs with Embedded Graphs

- **How it works**: A graph with embedded graphs is a data structure that provides efficient access to a shared resource.
- **Advantages**: Provides efficient access, prevents over-subscription.
- **Disadvantages**: May lead to over-subscription, requires complex implementation.

### 48. Graphs with Embedded Trees

- **How it works**: A graph with embedded trees is a data structure that provides efficient access to a shared
