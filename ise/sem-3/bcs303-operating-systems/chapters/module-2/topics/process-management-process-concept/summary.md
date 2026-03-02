# **Process Management: Process Concept**

## **Key Concepts**

### Definitions

- **Process**: A sequence of operations performed on one or more objects
- **Process Scheduling**: The selection of a process to be executed next by the CPU
- **Process Control**: The management of a process's execution, including scheduling, context switching, and termination

### Process States

- **Ready**: Process waits for CPU to become available
- **Running**: Process executes on CPU
- **Waiting**: Process waits for input/output operation to complete
- **Zombie**: Process terminates, but parent process still exists
- **Dead**: Process terminates, and resources are released

### Process Characteristics

- **Priority**: Determines the order in which processes are executed
- **Wait Time**: Time spent waiting for CPU or I/O operations
- **Turnaround Time**: Time spent in all states (ready, running, waiting, etc.)
- **Response Time**: Time taken to complete a request
- **Throughput**: Number of processes executed per unit time

### Process Scheduling Theorems

- **First-Come-First-Served (FCFS)**: Processes are executed in the order they arrive
- **Shortest Job First (SJF)**: Processes with the shortest execution time are executed first
- **Priority Scheduling**: Processes are executed based on their priority

### Process Management Formulas

- **Average Response Time**: `T_r = T_w + T_i + T_e / n`
- **Average Turnaround Time**: `T_t = T_w + T_i + T_e + T_r / n`
- **Throughput**: `T = 1 / W_t`
- **Waiting Time**: `T_w = T_i + T_r`

### Important Concepts

- **Context Switching**: Saving and restoring the state of a process
- **Multiprogramming**: Multiple processes share the CPU
- **Multitasking**: Multiple processes are executed concurrently
