# **Operations on Processes**

### Overview

- Operations on processes refer to the actions taken on processes, such as creating, deleting, suspending, and terminating them.
- Understanding operations on processes is crucial for managing system resources and optimizing system performance.

### Key Concepts and Formulas

- **Process Creation**: `fork()` system call in Unix-based systems
  - `pid = fork()`
    - `pid == 0`: Child process
    - `pid > 0`: Parent process
- **Process Termination**:
  - `exit()`: Terminate a process
  - `wait()`: Wait for a child process to terminate
- **Process Suspension**:
  - `pause()`: Suspend a process
  - `resume()`: Resume a suspended process
- **Process Switching**:
  - **Round Robin Scheduling**: Switch between processes in a circular manner
    - `time quantum`: Time slice allocated to each process
  - **Priority Scheduling**: Schedule processes based on their priority
    - **Priority**: Measure of how urgently a process needs to be executed

### Important Theorems and Definitions

- **Resource Allocation Theorem**: A process cannot allocate more resources than are available in the system.
- **Resource Utilization Theorem**: A process can utilize a resource only if it has been allocated to it.

### Revision Tips

- Understand the differences between `fork()`, `vfork()`, and `exec()`.
- Be familiar with process states (running, sleeping, waiting, zombie).
- Practice simulating process creation, termination, suspension, and resumption.
- Review the trade-offs between different process scheduling algorithms (e.g., round Robin, Priority).
