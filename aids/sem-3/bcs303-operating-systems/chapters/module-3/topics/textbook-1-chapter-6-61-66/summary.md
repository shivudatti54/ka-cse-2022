### Operating Systems Revision Notes - Chapter 6

#### 6.1 Process Scheduling

- Process scheduling: assigning time slices to processes
- Types:
  - First-Come-First-Served (FCFS)
  - Shortest Job First (SJF)
  - Priority Scheduling (PS)
- Advantages and Disadvantages of each scheduling algorithm

#### 6.2 Process Synchronization

- Process synchronization: coordinating access to shared resources
- Mutual Exclusion Theorem:
  - If two processes need exclusive access to a resource, only one can access it at a time
- Semaphores:
  - Variables that control access to shared resources
  - Used to synchronize processes

#### 6.3 Deadlocks

- Deadlock: situation where two or more processes are blocked indefinitely
- Four conditions for deadlock:
  - Mutual Exclusion
  - Hold and Wait
  - No Preemption
  - Circular Wait
- Prevention techniques:
  - Banker's Algorithm
  - Resource Allocation Graph (RAG)

#### 6.4 Deadlock Avoidance

- Deadlock avoidance: preventing deadlocks from occurring
- Banker's Algorithm:
  - Maximizes the chances of avoiding deadlocks
  - Uses a resource allocation matrix to avoid deadlocks

#### 6.5 Resource Allocation

- Resource allocation: assigning resources to processes
- Types:
  - Static Paging
  - Dynamic Paging
  - Rolling Allocation
- Advantages and Disadvantages of each resource allocation technique

#### 6.6 I/O Scheduling

- I/O scheduling: managing input/output operations
- Algorithms:
  - FCFS
  - SJF
  - Priority Scheduling
  - C-SCAN (Circular SCAN)
- Advantages and Disadvantages of each I/O scheduling algorithm
