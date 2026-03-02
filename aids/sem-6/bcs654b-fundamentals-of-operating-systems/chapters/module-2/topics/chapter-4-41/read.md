**Chapter 4: 4.1**
**Process Management**
=====================

### 4.1.1 Process Concept

A process is the basic unit of execution in an operating system. It represents a program that is currently being executed and is a separate entity from other programs. Each process has its own program counter, memory space, and system resources.

**Key Characteristics of a Process:**

- **Program Counter (PC):** The program counter stores the memory address of the next instruction to be executed.
- **Memory Space:** Each process has its own memory space where it stores its data and program.
- **System Resources:** Processes require system resources such as CPU time, memory, and I/O devices.

### 4.1.2 Process Scheduling

Process scheduling is the discipline of managing the allocation and deallocation of system resources to processes. The goal of process scheduling is to optimize the utilization of system resources and minimize the response time of the system.

**Types of Process Scheduling:**

- **Shortest Job First (SJF) Scheduling:** This scheduling algorithm allocates the CPU to the process with the shortest execution time first.
- **Round Robin (RR) Scheduling:** In this scheduling algorithm, each process is allocated a fixed time slot (called a time quantum) to execute.
- **Priority Scheduling:** This scheduling algorithm allocates the CPU to the process with the highest priority first.

**Process Scheduling Algorithms:**

- **FCFS (First-Come-First-Served) Scheduling:** This scheduling algorithm allocates the CPU to the process that arrives first.
- **Multilevel Feedback Queue (MLFQ) Scheduling:** This scheduling algorithm divides the processes into multiple queues based on their priority and allocates the CPU to the process with the highest priority first.

### 4.1.3 Operations on Processes

There are several operations that can be performed on processes, including:

- **Creation:** The creation of a new process.
- **Termination:** The termination of a process.
- **Synchronization:** The synchronization of multiple processes to coordinate their actions.
- **Communication:** The exchange of data between multiple processes.

**Process Control Signals:**

- **SIGINT (Interrupt):** This signal is sent to a process when it receives an interrupt signal.
- **SIGTERM (Termination):** This signal is sent to a process when it is terminated.
- **SIGCHLD (Child):** This signal is sent to a process when one of its child processes terminates.

### 4.1.4 Process States

A process can be in one of several states, including:

- **New:** A new process is created and has not yet started execution.
- **Ready:** A process is ready to be executed but has not yet started execution.
- **Running:** A process is executing and has control of the CPU.
- **Sleeping:** A process is waiting for a resource or event to occur.
- **Zombie:** A process has terminated but its parent process has not yet acknowledged its termination.

### 4.1.5 Process Hazard Analysis

A process hazard analysis is a method used to identify potential hazards associated with a process. The goal of a process hazard analysis is to identify and mitigate potential hazards to ensure the safety of the process and the system.

**Key Concepts:**

- **Process Hazard:** A process hazard is a potential hazard associated with a process.
- **Risk Assessment:** A risk assessment is a method used to evaluate the likelihood and impact of a process hazard.
- **Mitigation Strategies:** Mitigation strategies are methods used to mitigate process hazards.

### Key Terms:

- **Process:** A process is the basic unit of execution in an operating system.
- **Process Scheduling:** Process scheduling is the discipline of managing the allocation and deallocation of system resources to processes.
- **Process State:** A process can be in one of several states, including new, ready, running, sleeping, and zombie.
- **Process Hazard Analysis:** A process hazard analysis is a method used to identify potential hazards associated with a process.
