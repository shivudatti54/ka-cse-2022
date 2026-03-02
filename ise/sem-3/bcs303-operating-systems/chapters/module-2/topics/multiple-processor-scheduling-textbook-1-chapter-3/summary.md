# **Multiple-Processor Scheduling Revision Notes**

## **Overview**

Multiple-processor scheduling refers to the scheduling of tasks on multiple processors in a computer system. This topic is crucial in operating systems, as it deals with the allocation and execution of tasks on multiple processors.

### Chapter 3: Scheduling Algorithms

- **FCFS (First-Come-First-Served)**:
  - Each process is executed in the order it arrives.
  - No priority is given to any process.
- **SJF (Shortest Job First)**:
  - The process with the shortest burst time is executed first.
- **Priority Scheduling**:
  - Each process is assigned a priority.
  - The process with the highest priority is executed first.

### Chapter 4: Multiprocessing

- **Multiprocessing**:
  - Multiple processors are used to execute multiple tasks simultaneously.
  - Each processor executes a separate task.
- **Multiprogramming**:
  - Multiple tasks are executed on a single processor.
  - Context switching is involved.

### Chapter 5: Operating System Structure

- **OS Structure**:
  - Kernel: The core part of the operating system that manages hardware resources.
  - System Libraries: Provide functions for interacting with hardware resources.
  - Application Programs: User-level programs that use operating system services.
- **Process Scheduling**:
  - Process creation, execution, and termination.
  - Process synchronization and communication.

### Important Formulas and Definitions

- **Burst Time** (BT): The time taken by a process to complete its execution.
- **CPU Time** (CT): The time a process spends executing on the CPU.
- **Context Switching** (CS): The process of switching from one process to another.
- **Gantt Chart**: A graphical representation of the execution of tasks.

### Important Theorems

- **Amdahl's Law**:
  - The maximum theoretical speedup of a parallel program is limited by the fraction of the program that cannot be parallelized.
- **Theorem of Efficiency**:
  - The efficiency of a scheduling algorithm is determined by its ability to minimize the average response time.

### Key Concepts

- **Multiple-processor scheduling algorithms**:
  - FCFS
  - SJF
  - Priority Scheduling
- **Multiprocessing and multiprogramming**:
  - Multiple processors vs. multiple tasks
  - Context switching and synchronization
- **Operating system structure**:
  - Kernel, system libraries, and application programs
  - Process creation, execution, and termination
