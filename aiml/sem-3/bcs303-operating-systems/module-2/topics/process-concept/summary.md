# Process Concept - Summary

## Key Definitions

- **Process**: An instance of a program in execution; a dynamic entity representing a unit of work in a computer system
- **Process Control Block (PCB)**: The kernel data structure that stores all information necessary to manage and control a process, including PID, state, program counter, registers, and scheduling information
- **Context Switching**: The mechanism of saving the state of the currently running process and restoring the state of another process
- **Fork**: A Unix system call that creates a new process by duplicating the parent process
- **Exec**: A family of system calls that replace the current process image with a new program
- **Process State**: The current condition of a process indicating what it is doing or waiting for

## Important Formulas

- **CPU Utilization**: Not directly calculated from process concepts alone, but context switching overhead reduces effective CPU utilization
- **Turnaround Time**: Completion Time - Arrival Time (related to process scheduling)
- **Waiting Time**: Actual execution time begins after waiting in ready queue

## Key Points

1. A process is an active entity representing a program in execution, while a program is a passive entity stored on disk

2. The PCB is the kernel data structure that maintains all process information and enables context switching

3. Processes exist in exactly one of five states: New, Ready, Running, Waiting, or Terminated

4. Only one process can be in Running state on a single CPU at any instant; others wait in Ready or Waiting queues

5. The fork() system call creates a new process by duplicating the parent; exec() replaces the process image

6. Context switching involves significant overhead by saving/restoring complete CPU state

7. Every process (except init) has a parent, creating a hierarchical process tree in the system

8. Process termination returns an exit status to the parent, which must call wait() to retrieve it

9. Processes own resources (memory, files, devices) that are freed upon termination

10. The operating system uses queues (ready queue, waiting queues) to manage process scheduling

## Common Mistakes

1. **Confusing program and process**: A program is static code; a process is dynamic execution. Multiple processes can run the same program simultaneously.

2. **Thinking only one state transition is possible**: A running process can transition to ready (preemption), waiting (I/O request), or terminated directly.

3. **Ignoring context switching cost**: Students often forget that switching between processes consumes CPU cycles without doing useful work.

4. **Forgetting that fork() returns twice**: The fork() call returns the child's PID to the parent and 0 to the child process - understanding this is crucial for process control.

5. **Not understanding when processes wait**: A process in Running state moves to Waiting only when it requests I/O or waits for an event; it doesn't wait when other processes are running.