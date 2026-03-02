# **Textbook 1: Chapter – 6 (6.1-6.6) - Operating Systems**

## **6.1: Process Scheduling**

### Overview

Process scheduling is the discipline of scheduling and allocating system resources to processes. It involves choosing the best process to execute next and allocating the necessary resources.

### Process Scheduling Algorithms

The following are some common process scheduling algorithms:

- **First-Come-First-Served (FCFS)**: This algorithm executes the process that arrived first.
- **Shortest Job First (SJF)**: This algorithm executes the process with the shortest job.
- **Round Robin (RR)**: This algorithm divides the CPU time into equal intervals, called time slices, and assigns the CPU to the next process in the queue.
- **Priority Scheduling**: This algorithm assigns a priority to each process, and the process with the highest priority is executed first.

### Process Scheduling Advantages

- **Improved System Utilization**: Process scheduling algorithms can optimize system utilization by allocating resources to the most deserving processes.
- **Increased Responsiveness**: Process scheduling algorithms can improve the responsiveness of a system by executing the most urgent processes first.

### Process Scheduling Disadvantages

- **Increased Complexity**: Process scheduling algorithms can increase the complexity of a system by adding additional overhead.
- **Increased Resource Utilization**: Process scheduling algorithms can increase resource utilization, leading to decreased system performance.

### Example

Suppose we have the following processes:

| Process ID | Arrival Time | Burst Time |
| ---------- | ------------ | ---------- |
| P1         | 0            | 10         |
| P2         | 2            | 5          |
| P3         | 4            | 8          |

Using the SJF algorithm, the order of execution is:

1.  P2
2.  P1
3.  P3

## **6.2: Process Control Structures**

### Overview

Process control structures are used to manage processes and allocate system resources.

### Process Control Structures

The following are some common process control structures:

- **Process Table**: A process table is a data structure that stores information about each process, including its process ID, arrival time, burst time, and execution time.
- **Process Queue**: A process queue is a data structure that stores processes waiting to be executed.
- **Process Status**: Process status refers to the current state of a process, including whether it is running, waiting, or terminated.

### Process Control Structures Advantages

- **Improved Process Management**: Process control structures can improve process management by providing a centralized location for storing and managing process information.
- **Improved Resource Allocation**: Process control structures can improve resource allocation by allocating resources to the most deserving processes.

### Process Control Structures Disadvantages

- **Increased Complexity**: Process control structures can increase the complexity of a system by adding additional overhead.
- **Increased Resource Utilization**: Process control structures can increase resource utilization, leading to decreased system performance.

### Example

Suppose we have the following process control structure:

| Process ID | Arrival Time | Burst Time | Execution Time |
| ---------- | ------------ | ---------- | -------------- |
| P1         | 0            | 10         | 10             |
| P2         | 2            | 5          | 5              |
| P3         | 4            | 8          | 8              |

## **6.3: Deadlocks**

### Overview

A deadlock is a situation in which two or more processes are blocked indefinitely, each waiting for the other to release a resource.

### Deadlock Detection Algorithms

The following are some common deadlock detection algorithms:

- **Wright's Algorithm**: This algorithm uses a graph traversal approach to detect deadlocks.
- **Banker's Algorithm**: This algorithm uses a bank account approach to detect deadlocks.
- **Dinitz's Algorithm**: This algorithm uses a graph traversal approach to detect deadlocks.

### Deadlock Prevention Algorithms

The following are some common deadlock prevention algorithms:

- **Avoid Starvation Algorithm**: This algorithm avoids starvations by always allocating resources to the most deserving processes.
- **Avoid Deadlocks Algorithm**: This algorithm avoids deadlocks by always allocating resources to the most deserving processes.
- **Avoid Livelocks Algorithm**: This algorithm avoids livelocks by always allocating resources to the most deserving processes.

### Example

Suppose we have the following deadlock scenario:

Process P1 holds resource R1 and is waiting for resource R2.
Process P2 holds resource R2 and is waiting for resource R1.

Using Wright's algorithm, we can detect the deadlock scenario.

## **6.4: Starvation**

### Overview

Starvation is a situation in which a process is denied access to a resource for an extended period of time.

### Starvation Detection Algorithms

The following are some common starvation detection algorithms:

- **Avoid Starvation Algorithm**: This algorithm avoids starvations by always allocating resources to the most deserving processes.
- **Avoid Livelocks Algorithm**: This algorithm avoids livelocks by always allocating resources to the most deserving processes.

### Starvation Prevention Algorithms

The following are some common starvation prevention algorithms:

- **Round Robin Algorithm**: This algorithm divides the CPU time into equal intervals, called time slices, and assigns the CPU to the next process in the queue.
- **Priority Scheduling Algorithm**: This algorithm assigns a priority to each process, and the process with the highest priority is executed first.

### Example

Suppose we have the following starvation scenario:

Process P1 is waiting for resource R1, while process P2 has been holding the resource for an extended period of time.

Using the Avoid Starvation algorithm, we can prevent the starvation scenario.

## **6.5: Resource Allocation**

### Overview

Resource allocation is the process of allocating system resources to processes.

### Resource Allocation Algorithms

The following are some common resource allocation algorithms:

- **First-Come-First-Served (FCFS)**: This algorithm allocates resources to the process that arrived first.
- **Shortest Job First (SJF)**: This algorithm allocates resources to the process with the shortest job.
- **Round Robin (RR)**: This algorithm divides the CPU time into equal intervals, called time slices, and assigns the CPU to the next process in the queue.

### Resource Allocation Advantages

- **Improved System Utilization**: Resource allocation algorithms can optimize system utilization by allocating resources to the most deserving processes.
- **Increased Responsiveness**: Resource allocation algorithms can improve the responsiveness of a system by executing the most urgent processes first.

### Resource Allocation Disadvantages

- **Increased Complexity**: Resource allocation algorithms can increase the complexity of a system by adding additional overhead.
- **Increased Resource Utilization**: Resource allocation algorithms can increase resource utilization, leading to decreased system performance.

### Example

Suppose we have the following resource allocation scenario:

Process P1 is waiting for resource R1, while process P2 has been holding the resource for an extended period of time.

Using the Round Robin algorithm, we can allocate the resource to the process with the highest priority.

## **6.6: Resource Preemption**

### Overview

Resource preemption is the process of forcibly taking away a resource from a process.

### Resource Preemption Algorithms

The following are some common resource preemption algorithms:

- **Time Slicing Algorithm**: This algorithm divides the CPU time into equal intervals, called time slices, and assigns the CPU to the next process in the queue.
- **Priority Scheduling Algorithm**: This algorithm assigns a priority to each process, and the process with the highest priority is executed first.

### Resource Preemption Advantages

- **Improved System Utilization**: Resource preemption algorithms can optimize system utilization by allocating resources to the most deserving processes.
- **Increased Responsiveness**: Resource preemption algorithms can improve the responsiveness of a system by executing the most urgent processes first.

### Resource Preemption Disadvantages

- **Increased Complexity**: Resource preemption algorithms can increase the complexity of a system by adding additional overhead.
- **Increased Resource Utilization**: Resource preemption algorithms can increase resource utilization, leading to decreased system performance.

### Example

Suppose we have the following resource preemption scenario:

Process P1 is running on a CPU with a limited time slice.

Using the Time Slicing algorithm, we can preempt the resource from process P1 and allocate it to process P2.

This concludes the study material for Textbook 1: Chapter – 6 (6.1-6.6) on Operating Systems.
