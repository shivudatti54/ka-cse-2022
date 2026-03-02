## Chapter 8: Process Control

### UNIX SYSTEM PROGRAMMING

#### Key Points

- **Process Control**: The process control mechanism allows a process to interact with the operating system.
- **Process Identifiers**: Each process has a unique identifier, represented by the process ID (PID).
- **fork()**: Creates a new process by duplicating the existing process.
  - **vfork()**: Similar to fork(), but also inherits the parent's environment.
- **exit()**: Terminates a process and returns to the parent process.
- **wait()**: Blocks the parent process until the child process terminates.
  - **waitpid()**: Allows the parent process to specify the process ID to wait for.
  - **wait3()**: Similar to waitpid(), but also returns the process ID of the terminated child process.

#### Important Formulas and Definitions

- **Process Status**:
  - R: Running
  - Z: Zombie (terminates, but parent hasn't waited)
  - T: Stopped
  - S: Sleeping
  - D: Disk sleep
  - W: Waiting
  - I: Interruptible sleep
  - X: Dead
- **Process Priority**:
  - Normal priority: 0-19
  - Nice priority: -20 to 19

#### Theorems and Concepts

- **Process Scheduling**: The operating system schedules processes based on their priority and availability of resources.
- **Context Switching**: The process of switching from one process to another to allocate system resources.

#### Quick Revision

- Identify processes using `ps` or `who`.
- Create a new process using `fork()`.
- Inherit the parent's environment using `vfork()`.
- Terminate a process using `exit()`.
- Wait for a child process to terminate using `wait()` or `waitpid()`.
