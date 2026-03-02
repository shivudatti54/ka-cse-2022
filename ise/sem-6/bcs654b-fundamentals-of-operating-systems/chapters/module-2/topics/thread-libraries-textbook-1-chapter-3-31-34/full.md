# Thread Libraries Textbook 1: Chapter 3: 3.1-3.4

=====================================================

## 3.1: Process Scheduling

---

Process scheduling is the discipline of scheduling and managing processes on a computer system. The goal of process scheduling is to optimize the utilization of system resources, such as CPU time, memory, and I/O devices, while ensuring that processes are executed as efficiently as possible.

### Types of Process Scheduling Algorithms

1. **First-Come-First-Served (FCFS)**: In FCFS scheduling, the process that arrives first is executed first. This algorithm is simple to implement but can lead to poor system performance due to the fact that the process that is most likely to require the most resources is executed first.
2. **Shortest Job First (SJF)**: In SJF scheduling, the process with the shortest execution time is executed first. This algorithm is more efficient than FCFS but can still lead to poor system performance due to the fact that processes with long execution times are not executed first.
3. **Priority Scheduling**: In priority scheduling, processes are assigned priorities based on their characteristics, such as the priority of the process's user or the level of importance of the process. The process with the highest priority is executed first.
4. **Round Robin (RR)**: In RR scheduling, each process is allocated a time slice, called a quantum, and the process that is currently executing is given the quantum for a fixed time period. The process then yields control to the next process in the ready queue. RR scheduling is more efficient than FCFS and SJF scheduling as it prevents processes from starving.

### Process Scheduling Parameters

- **Process Arrival Time**: The time at which a process arrives at the ready queue.
- **Process Burst Time**: The amount of CPU time required by a process to complete its execution.
- **Process Priority**: The priority assigned to a process based on its characteristics.
- **Process Quantum**: The time slice allocated to a process for execution.

### Examples

- Consider a system with two processes, P1 and P2, that arrive at the ready queue at times t=0 and t=2 respectively. P1 requires 10 units of CPU time to complete its execution, while P2 requires 5 units of CPU time. If the quantum is 2 units, P1 will execute for 2 units and then yield control to P2, which will execute for 2 units and then yield control back to P1.
- Consider a system with three processes, P1, P2, and P3, that arrive at the ready queue at times t=0, t=2, and t=4 respectively. P1 requires 10 units of CPU time, P2 requires 5 units of CPU time, and P3 requires 15 units of CPU time. If the quantum is 3 units, P1 will execute for 3 units, P2 will execute for 3 units, and P3 will execute for 3 units.

## 3.2: Process Synchronization

---

Process synchronization is the process of coordinating the actions of multiple processes to ensure that they access shared resources in a safe and efficient manner.

### Types of Process Synchronization

1.  **Mutual Exclusion**: Mutual exclusion ensures that only one process can access a shared resource at a time.
2.  **Mutual Exclusion with Priority**: Mutual exclusion with priority ensures that the process with the highest priority can access a shared resource first.
3.  **Critical Section**: A critical section is a section of code that accesses a shared resource.
4.  **Semaphore**: A semaphore is a variable that is used to control the access to a shared resource.

### Process Synchronization Algorithms

1.  **Monitors**: Monitors are a synchronization mechanism that uses a combination of semaphores and conditional statements to synchronize processes.
2.  **Peterson's Algorithm**: Peterson's algorithm is a synchronization algorithm that uses a combination of semaphores and conditional statements to synchronize processes.
3.  **Dekker's Token Ring**: Dekker's token ring is a synchronization algorithm that uses a combination of semaphores and conditional statements to synchronize processes.

### Examples

- Consider a system with two processes, P1 and P2, that want to access a shared resource. If the shared resource is a light switch, P1 can turn the light switch on and P2 can turn the light switch off.
- Consider a system with three processes, P1, P2, and P3, that want to access a shared resource. If the shared resource is a parking spot, P1 can park in the parking spot, P2 can park in another parking spot, and P3 can park in yet another parking spot.

## 3.3: Process Communication

---

Process communication is the process of exchanging information between multiple processes.

### Types of Process Communication

1.  **Synchronous Communication**: Synchronous communication is a type of communication where the sender and receiver must be in the same state before the message can be sent or received.
2.  **Asynchronous Communication**: Asynchronous communication is a type of communication where the sender and receiver do not need to be in the same state before the message can be sent or received.
3.  **Message Passing**: Message passing is a type of communication where a process sends a message to another process.
4.  **Shared Memory**: Shared memory is a type of communication where multiple processes share a common memory space.

### Process Communication Algorithms

1.  **Producer-Consumer Algorithm**: The producer-consumer algorithm is a synchronization algorithm that uses a combination of semaphores and conditional statements to synchronize processes.
2.  **Dining Philosophers Algorithm**: The dining philosophers algorithm is a synchronization algorithm that uses a combination of semaphores and conditional statements to synchronize processes.
3.  **Reader-Writer Algorithm**: The reader-writer algorithm is a synchronization algorithm that uses a combination of semaphores and conditional statements to synchronize processes.

### Examples

- Consider a system with two processes, P1 and P2, that want to exchange information. If the information is a message, P1 can send the message to P2.
- Consider a system with three processes, P1, P2, and P3, that want to share a common memory space. If the memory space is a parking lot, P1 can park in the parking lot, P2 can park in another parking lot, and P3 can park in yet another parking lot.

## 3.4: Process Implementation

---

Process implementation is the process of creating and executing processes on a computer system.

### Types of Process Implementation

1.  **User-Level Process Implementation**: User-level process implementation is the process of creating and executing processes at the user level.
2.  **Kernel-Level Process Implementation**: Kernel-level process implementation is the process of creating and executing processes at the kernel level.
3.  **Multitasking**: Multitasking is a process implementation technique that allows multiple processes to run concurrently on a single processor.

### Process Implementation Algorithms

1.  **Process Creation**: Process creation is the process of creating a new process.
2.  **Process Execution**: Process execution is the process of executing a process.
3.  **Process Synchronization**: Process synchronization is the process of synchronizing processes to ensure that they access shared resources in a safe and efficient manner.

### Examples

- Consider a system with two processes, P1 and P2, that want to create a new process. If the system uses user-level process implementation, P1 can create a new process by calling a system call.
- Consider a system with three processes, P1, P2, and P3, that want to execute a process concurrently. If the system uses multitasking, P1, P2, and P3 can execute concurrently on a single processor.

## Further Reading

---

- "Operating System Concepts" by Abraham Silberschatz, Peter Baer Galvin, and Greg Gagne
- "Operating System Engineering" by John L. Hennessy and David A. Patterson
- "The Art of Computer Programming" by Donald E. Knuth
- "Introduction to Algorithms" by Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein
- "Operating System Internals" by Andrew S. Tanenbaum and Maarten van Steen
