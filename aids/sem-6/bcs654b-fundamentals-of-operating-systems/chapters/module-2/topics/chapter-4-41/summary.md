# Process Management

### Chapter 4: 4.1

#### Key Concepts

- **Process**: A program in execution, including its memory image and program counter.
- **Process Scheduling**: The discipline of allocating the necessary resources to a process and scheduling the process.
- **Process States**:
  - **Ready State**: The process is ready to be executed.
  - **Running State**: The process is being executed.
  - **Waiting State**: The process is waiting for some resource.
  - **Zombie State**: The process has terminated but its parent process has not yet recognized the termination.
  - **Dead State**: The process has terminated and its parent process has recognized the termination.

#### Process Scheduling Algorithms

- **First-Come-First-Served (FCFS)**:
  - The process with the highest priority in the ready queue is executed first.
- **Shortest Job First (SJF)**:
  - The process with the shortest burst time in the ready queue is executed first.
- **Priority Scheduling**:
  - The process with the highest priority is executed first.
- **Round Robin (RR)**:
  - Each process is given a fixed time slice (time quantum) to execute.
  - The process with the highest priority is executed for the time quantum.
- **Multilevel Feedback Queue (MLFQ)**:
  - A combination of priority scheduling and round robin scheduling.

#### Process Operations

- **Process Creation**:
  - A new process is created by duplicating an existing process.
  - The new process has its own memory space and program counter.
- **Process Termination**:
  - A process terminates when it completes its execution.
  - The operating system sends a termination signal to the process.

#### Important Formulas and Definitions

- **Burst Time (BT)**: The time taken by a process to complete its execution.
- **Turnaround Time (TT)**: The time taken by a process to complete its execution, including waiting time.
- **Waiting Time (WT)**: The time a process spends waiting in the ready queue.
- **Response Time (RT)**: The time taken by the operating system to execute a process.
- **Turnaround Time (TT) = BT + WT**

#### Important Theorems

- **Lagrange's Law**: The average waiting time of a process in a queue is equal to the average burst time of the processes in the queue.
- **Little's Law**: The average number of processes in a system is equal to the average arrival rate of processes multiplied by the average waiting time of a process in the system.
