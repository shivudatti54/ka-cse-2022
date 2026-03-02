# Operations on Processes

==========================

### Overview

Operations on processes refer to the creation, suspension, termination, and synchronization of processes in an operating system.

### Key Concepts

- **Process Creation**: Creating a new process by duplicating an existing process, using the `fork()` system call.
  - Formula: `pid = fork()` where `pid` is the process ID of the new process.
- **Process Termination**: Termination of a process using the `exit()` system call.
  - Formula: `exit(status)`, where `status` is the exit status of the process.
- **Process Synchronization**: Waiting for a process to complete its execution using synchronization primitives such as `wait()`, `waitpid()`, and `join()`.
  - Formula: `wait(pid)`, `waitpid(pid, statusp, options)`, or `join(pid)`, where `pid` is the process ID and `statusp` is the status buffer.
- **Process Suspension**: Suspending a process using the `suspend()` system call.
  - Formula: `suspend(pid)`, where `pid` is the process ID.
- **Process Resumption**: Resuming a suspended process using the `resume()` system call.
  - Formula: `resume(pid)`.

### Theories

- **Mellor-Crummey's Theorem**: A theorem explaining the visibility of data in shared memory.
  - Formula: "If two processes access a shared memory location, and one process writes to the location after reading from it, then the other process will be able to see the changes made by the first process."
- **Dekker's Token Ring Protocol**: A protocol for synchronizing access to shared resources.
  - Formula: "A token is passed from one process to the next, with each process holding the token for a fixed time period."

### Important Definitions

- **Process**: A program in execution, which can be thought of as a separate flow of execution.
- **Process ID (PID)**: A unique identifier assigned to each process.
- **Parent-Child Process Relationship**: A process that creates a new process is called the parent, and the new process is called the child.

### Important Formulas

- `pid = fork()`
- `exit(status)`
- `wait(pid)`
- `waitpid(pid, statusp, options)`
- `join(pid)`
- `suspend(pid)`
- `resume(pid)`
