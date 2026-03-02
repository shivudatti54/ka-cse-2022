# **Multiple-Processor Scheduling**

## **Introduction**

In this study material, we will explore the concept of multiple-processor scheduling, which is a crucial aspect of operating systems. Multiple-processor scheduling is the process of allocating tasks to multiple processors in a system to improve system performance and efficiency.

## **Chapter 3: Single-Processor Scheduling (3.1-3.4)**

### 3.1: Process Scheduling

Process scheduling is the allocation of a set of resources to a process and the allocation of time to the process. In a single-processor system, only one process can execute at a time.

- **Types of Process Scheduling:**
  - **First-Come-First-Served (FCFS):** The process that arrives first is executed first.
  - **Shortest Job First (SJF):** The process with the shortest execution time is executed first.
  - **Priority Scheduling:** The process with the highest priority is executed first.
- **Advantages and Disadvantages of Single-Processor Scheduling:**
  - Advantages:
    - Simple to implement
    - Low overhead
  - Disadvantages:
    - Poor performance due to constant context switching

### 3.2: Process Characteristics

Processes have several characteristics that affect their scheduling needs.

- **Process Arrival Time:** The time at which a process arrives in the system.
- **Process Burst Time:** The amount of time a process takes to complete its execution.
- **Priority:** The level of importance assigned to a process.
- **Resource Requirements:** The resources required by a process, such as CPU time, memory, and I/O devices.

### 3.3: Scheduling Algorithms

Scheduling algorithms are used to schedule processes in a system.

- **Round Robin Scheduling:** Each process is assigned a fixed time slice (called a time quantum) to execute.
- **Multilevel Feedback Queue (MLFQ) Scheduling:** A queue of processes is divided into multiple levels based on their characteristics.
- **Earliest Deadline First (EDF) Scheduling:** The process with the earliest deadline is executed first.

### 3.4: Scheduling Criteria

Scheduling criteria are used to evaluate the performance of a scheduling algorithm.

- **Throughput:** The number of processes completed by the system per unit time.
- **Turnaround Time:** The time taken by a process to complete its execution.
- **Waiting Time:** The time a process spends waiting in the queue.
- **Response Time:** The time taken by a process to become ready to execute.

## **Chapter 4: Multiple-Processor Scheduling (4.1-4.4)**

### 4.1: Introduction to Multiple-Processor Scheduling

Multiple-processor scheduling is a technique used to improve system performance and efficiency by allocating tasks to multiple processors.

- **Types of Multiple-Processor Scheduling:**
  - **Load Balancing:** Distributing the workload evenly across multiple processors.
  - **Resource Sharing:** Sharing resources among multiple processors.
  - **Task Partitioning:** Dividing tasks into smaller subtasks and assigning them to multiple processors.

### 4.2: Load Balancing

Load balancing is a technique used to distribute the workload evenly across multiple processors.

- **Load Balancing Algorithms:**
  - **Round Robin Load Balancing:** Each processor is assigned a fixed time slice to execute tasks.
  - **Dynamic Load Balancing:** The workload is dynamically adjusted based on processor availability.

### 4.3: Resource Sharing

Resource sharing is a technique used to share resources among multiple processors.

- **Resource Sharing Algorithms:**
  - **Priority-Based Resource Sharing:** Resources are allocated based on processor priority.
  - **Time-Shared Resource Sharing:** Resources are allocated for a fixed time period.

### 4.4: Task Partitioning

Task partitioning is a technique used to divide tasks into smaller subtasks and assign them to multiple processors.

- **Task Partitioning Algorithms:**
  - **Dynamic Task Partitioning:** Tasks are dynamically partitioned based on processor availability.
  - **Static Task Partitioning:** Tasks are statically partitioned based on processor capabilities.

## **Chapter 5: Scheduling Algorithms for Multiple Processors (5.1-5.5)**

### 5.1: Round Robin Scheduling for Multiple Processors

Round Robin scheduling is a technique used to schedule tasks on multiple processors.

- **Round Robin Scheduling Algorithm:**
  - Each processor is assigned a fixed time slice to execute tasks.
  - The processor with the highest priority is executed first.

### 5.2: Multilevel Feedback Queue (MLFQ) Scheduling for Multiple Processors

Multilevel feedback queue (MLFQ) scheduling is a technique used to schedule tasks on multiple processors.

- **MLFQ Scheduling Algorithm:**
  - A queue of processes is divided into multiple levels based on their characteristics.
  - The process with the highest priority is executed first.

### 5.3: Earliest Deadline First (EDF) Scheduling for Multiple Processors

Earliest deadline first (EDF) scheduling is a technique used to schedule tasks on multiple processors.

- **EDF Scheduling Algorithm:**
  - The process with the earliest deadline is executed first.
  - The process with the highest priority is executed first if there are multiple processes with the same deadline.

### 5.4: Priority-Based Scheduling for Multiple Processors

Priority-based scheduling is a technique used to schedule tasks on multiple processors.

- **Priority-Based Scheduling Algorithm:**
  - The process with the highest priority is executed first.
  - The process with the next highest priority is executed next.

### 5.5: Dynamic Scheduling for Multiple Processors

Dynamic scheduling is a technique used to schedule tasks on multiple processors.

- **Dynamic Scheduling Algorithm:**
  - The workload is dynamically adjusted based on processor availability.
  - The process with the highest priority is executed first.

## **Key Concepts:**

- **Load Balancing:** Distributing the workload evenly across multiple processors.
- **Resource Sharing:** Sharing resources among multiple processors.
- **Task Partitioning:** Dividing tasks into smaller subtasks and assigning them to multiple processors.
- **Round Robin Scheduling:** Each processor is assigned a fixed time slice to execute tasks.
- **Multilevel Feedback Queue (MLFQ) Scheduling:** A queue of processes is divided into multiple levels based on their characteristics.
- **Earliest Deadline First (EDF) Scheduling:** The process with the earliest deadline is executed first.
- **Priority-Based Scheduling:** The process with the highest priority is executed first.
- **Dynamic Scheduling:** The workload is dynamically adjusted based on processor availability.
