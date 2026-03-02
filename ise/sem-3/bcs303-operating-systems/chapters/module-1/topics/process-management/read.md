# Process Management

## Introduction

Process management is one of the fundamental responsibilities of any operating system. A process is a program in execution, representing the fundamental unit of work in a computer system. Understanding how operating systems create, schedule, execute, and terminate processes is essential for comprehending how modern computing systems achieve multitasking and resource sharing.

In the early days of computing, only one program could run at a time, making inefficient use of expensive hardware resources. Modern operating systems support hundreds or thousands of simultaneous processes, enabling users to run multiple applications concurrently while the system maintains responsiveness and efficiency. The operating system must manage processes fairly, ensure proper synchronization when processes share resources, and protect against processes interfering with each other.

This topic covers the complete lifecycle of processes—from their creation to termination—along with the data structures and algorithms that operating systems employ to manage them effectively. These concepts are critical not only for understanding operating system design but also for writing efficient concurrent programs and debugging performance issues in real-world applications.

## Key Concepts

### Process Definition

A process is an instance of a program in execution. It is more than just the program code (often called the text section); it includes the current activity represented by values in the program counter, processor registers, stack, heap, and data sections. In other words, a process is a dynamic entity, while a program is a static entity.

A process can be formally defined as: A program that is currently executing along with its associated resources, including memory, I/O devices, file descriptors, and processor state. Each process has its own address space, which the operating system protects from other processes to ensure isolation and security.

### Process State

As a process executes, it moves through various states. The operating system maintains information about each process's current state, which can include:

1. **New (Created)**: The process is being created. The operating system has allocated memory and initialized the process control block but has not yet admitted it to the ready queue.

2. **Running**: The process's instructions are currently being executed by the CPU. In a uniprocessor system, only one process can be in the running state at any given time.

3. **Ready**: The process is waiting to be assigned to a processor. It is in the ready queue waiting for the scheduler to select it for execution.

4. **Waiting (Blocked)**: The process is waiting for some event to occur, such as I/O completion, a signal, or availability of a resource. It cannot proceed until the event occurs.

5. **Terminated**: The process has finished execution. The operating system releases its resources and removes the process control block.

The transition between these states is managed by the operating system's process management subsystem. For example, a running process may be preempted and moved to the ready state by the scheduler, or it may voluntarily give up the CPU by issuing a blocking system call.

### Process Control Block (PCB)

The Process Control Block is the kernel data structure that stores all information about a process. It serves as the "brain" of the process from the operating system's perspective. The PCB typically contains:

- **Process Identification**: Unique process ID (PID), parent process ID (PPID), user ID, and group ID.

- **Processor State Information**: This includes the program counter, CPU registers, CPU scheduling information (priority, scheduling queue pointers), and memory management information (page tables, segment tables, base and limit registers).

- **Process Control Information**: Process state, accounting information (CPU time used, time limits, account numbers), I/O status information (list of open files, outstanding I/O requests), and pointer to parent and child processes.

The operating system maintains a collection of PCBs, often organized in process tables or linked lists, allowing the scheduler to quickly access and modify process information during context switches.

### Process Scheduling

Process scheduling is the mechanism by which the operating system decides which process should execute on the CPU at any given time. The scheduler must balance competing goals: maximizing CPU utilization, minimizing wait time, ensuring fairness, and maintaining system throughput.

**Long-term Scheduler** (Admission Scheduler): Decides which processes are admitted to the system from the pool of new processes. It controls the degree of multiprogramming. In batch systems, this scheduler admits processes in batches, while in interactive systems, it typically admits most or all new processes immediately.

**Short-term Scheduler** (CPU Scheduler): Selects which process from the ready queue should execute next on the CPU. This scheduler runs frequently (milliseconds) and must be extremely fast. It implements a specific scheduling algorithm to determine the order of process execution.

**Medium-term Scheduler**: Introduced in systems with virtual memory, this scheduler can temporarily remove processes from memory (swapping) to reduce the degree of multiprogramming and improve system performance. Swapped-out processes reside in secondary storage and can be brought back to memory later.

### Scheduling Algorithms

**First-Come, First-Served (FCFS)**: Processes are served in the order they arrive in the ready queue. This is simple but can lead to the convoy effect, where short processes wait behind long ones.

**Shortest Job First (SJF)**: The process with the smallest burst time is selected first. This algorithm provides minimum average waiting time but requires knowledge of future CPU burst times, making it impractical in interactive systems.

**Priority Scheduling**: Each process is assigned a priority, and the highest-priority process is selected first. Priority can be static (fixed) or dynamic (changing based on behavior). This can lead to starvation of low-priority processes.

**Round Robin (RR)**: Each process gets a fixed time slice (quantum) in cyclic order. This is ideal for time-sharing systems as it ensures no process starves and provides good response time.

**Multilevel Queue Scheduling**: Multiple ready queues are maintained for different process types (system, interactive, batch), each with its own scheduling algorithm.

### Process Creation

Processes can create other processes, forming a parent-child hierarchy. In Unix/Linux, the fork() system call creates a new process. The child process gets a copy of the parent's address space (including all open file descriptors), and both processes continue execution from the point of fork().

After forking, processes typically use exec() to replace their memory space with a new program. This two-step process (fork + exec) is the standard way to create new programs in Unix systems. The parent process can wait for the child to complete using the wait() system call, retrieving the child's exit status.

Process creation involves:
- Allocating a unique PID
- Creating and initializing the PCB
- Allocating memory for the process's address space
- Setting up the process's environment (working directory, file descriptors, resource limits)
- Adding the process to the appropriate scheduling queues

### Process Termination

A process terminates when it completes execution normally (via exit() system call) or abnormally (due to an unhandled exception or receiving a signal). The termination process involves:

- Closing all open files and releasing resources
- Removing the process from all queues
- Updating the parent process's status (via wait())
- Deallocating the PCB and memory
- In Unix, the process becomes a zombie until the parent reads its exit status via wait(); if the parent dies first, the process becomes an orphan and is adopted by init (PID 1)

### Interprocess Communication (IPC)

Processes often need to communicate and coordinate their activities. The operating system provides various IPC mechanisms:

**Pipes**: Unidirectional channels that allow data flow between related processes (created by pipe() system call). Named pipes (FIFOs) allow communication between unrelated processes.

**Message Queues**: Kernel-managed message buffers that processes can send and receive messages through. They support message prioritization and asynchronous communication.

**Shared Memory**: Multiple processes can share a region of memory. This is the fastest IPC mechanism since no data copying is required, but processes must synchronize access explicitly.

**Semaphores**: Integer variables used for signaling and synchronization between processes. They help prevent race conditions when processes access shared resources.

**Signals**: Asynchronous notifications sent to processes to indicate events. They are software interrupts that can cause processes to terminate, pause, or execute specific handler functions.

**Sockets**: Endpoints for network communication that can also be used for local interprocess communication between processes on the same or different machines.

## Examples

### Example 1: Process State Transition

Consider a word processor process that is currently running (state: Running) and needs to read a large file from disk.

**Step 1**: The process issues a read() system call for the file.

**Step 2**: Since the I/O operation cannot complete immediately, the operating system changes the process state from Running to Waiting (Blocked).

**Step 3**: The scheduler selects another ready process to run.

**Step 4**: When the disk I/O completes, the operating system receives an interrupt and updates the I/O device status.

**Step 5**: The operating system moves the word processor process from the Waiting state to the Ready state.

**Step 6**: When the scheduler considers the word processor next (based on its scheduling algorithm), the process transitions from Ready to Running and continues execution.

### Example 2: Calculating Average Waiting Time with FCFS

Three processes arrive at time 0 with the following CPU burst times:
- Process P1: 24 milliseconds
- Process P2: 3 milliseconds
- Process P3: 3 milliseconds

Using FCFS scheduling:
- P1 executes first (0-24), waiting time = 0
- P2 executes second (24-27), waiting time = 24
- P3 executes third (27-30), waiting time = 27

Average waiting time = (0 + 24 + 27) / 3 = 17 ms

Now using SJF (Shortest Job First):
- P2 and P3 both have burst time 3; either can run first
- If P2 runs first (0-3), waiting for P2 = 0
- P3 runs second (3-6), waiting for P3 = 3
- P1 runs last (6-30), waiting for P1 = 6

Average waiting time = (0 + 3 + 6) / 3 = 3 ms

This demonstrates that SJF significantly reduces average waiting time compared to FCFS.

### Example 3: Round Robin Time Quantum Impact

Consider four processes with burst times: P1=10, P2=5, P3=8, P4=12. Time quantum = 4 ms.

**First round**:
- P1 runs (0-4), remaining = 6
- P2 runs (4-8), remaining = 1
- P3 runs (8-12), remaining = 4
- P4 runs (12-16), remaining = 8

**Second round**:
- P1 runs (16-20), remaining = 2
- P2 runs (20-21), remaining = 0 (completes)
- P3 runs (21-25), remaining = 0 (completes)
- P4 runs (25-29), remaining = 4

**Third round**:
- P1 runs (29-31), remaining = 0 (completes)
- P4 runs (31-35), remaining = 0 (completes)

Completion order: P2 → P3 → P1 → P4. This shows how Round Robin ensures fairness by giving each process equal CPU time slices, preventing any single process from monopolizing the CPU.

## Exam Tips

1. **Understand the difference between program and process**: A program is static (code), while a process is dynamic (program in execution with all its resources).

2. **Remember all five process states and their transitions**: Know exactly what causes each state transition (e.g., I/O request causes Running → Waiting, time slice expiration causes Running → Ready).

3. **PCB contents are frequently tested**: Be able to list and explain what information is stored in the Process Control Block.

4. **Scheduling algorithm comparison**: Know the advantages and disadvantages of each algorithm. FCFS suffers from convoy effect, SJF minimizes average waiting time but may cause starvation, RR provides good response time for interactive systems.

5. **Calculate waiting time and turnaround time**: Practice numerical problems involving FCFS, SJF, and Round Robin scheduling.

6. **Understand fork() and exec()**: These are fundamental Unix process creation system calls. Remember that fork() creates a child process that is a copy of the parent, and exec() replaces the child's program.

7. **IPC mechanisms**: Know at least three IPC methods and understand when each is appropriate. Shared memory is fastest but requires synchronization; message passing is safer but slower.

8. **Context switch concept**: Understand that a context switch involves saving the state of the currently running process and loading the state of the next process. This is pure overhead—no useful work is accomplished during the switch.