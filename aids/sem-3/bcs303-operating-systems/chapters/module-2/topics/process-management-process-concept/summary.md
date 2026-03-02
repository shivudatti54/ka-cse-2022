# Process Management: Process Concept

## **Definition**

- A process is a sequence of instructions used to perform a specific task or set of tasks in a computer system.

## **Key Concepts**

- **Process Creation**: The process of creating a new process in the operating system, which involves allocating system resources and creating a new process image.
- **Process Scheduling**: The process of allocating the CPU to a process for execution.
- **Process Communication**: The process of exchanging data between processes, such as through inter-process communication (IPC) mechanisms.

## **Process States**

- **New**: A process that is waiting to be scheduled for execution.
- **Running**: A process that is currently executing on the CPU.
- **Waiting**: A process that is waiting for a resource, such as I/O completion or a signal.
- **Zombie**: A process that has finished execution but still occupies system resources.
- **Dead**: A process that has finished execution and has been removed from the system.

## **Process Control**

- **Process Control Block (PCB)**: A data structure that contains information about a process, such as its memory space, CPU registers, and status.
- **Scheduler**: A program that manages the allocation of the CPU to processes.
- **Context Switching**: The process of switching from one process to another, which involves saving and restoring the CPU registers and memory context.

## **Important Formulas and Theorems**

- **CPU Utilization Formula**: CPU utilization = (Number of processes running) / (Total number of processes)
- **Turnaround Time Formula**: Turnaround time = Waiting time + Execution time
- **Waiting Time Formula**: Waiting time = (Number of context switches) x (Average execution time)

## **Important Definitions**

- **Process**: A sequence of instructions used to perform a specific task or set of tasks in a computer system.
- **Thread**: A lightweight process that shares the same memory space and resources as the parent process.
- **Process Image**: A complete copy of a process's memory space and CPU registers, which is used to create a new process.
