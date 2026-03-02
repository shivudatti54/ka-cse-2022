# Thread Libraries Textbook 1: Chapter 3

### Process Management Fundamentals

- **Process**: A program in execution, running on a computer's processor.
- **Process Scheduling**: The selection and allocation of a process to a processor for execution.
- **Process Operations**: Creating, deleting, and synchronization of processes.

### Key Concepts

- **Process States**:
  - **Ready**: Process waiting for CPU.
  - **Running**: Process currently executing on CPU.
  - **Waiting**: Process waiting for I/O device.
  - **Sleeping**: Process waiting for process to be woken up.
  - **Zombie**: Process that has terminated but still occupies memory.
  - **Dead**: Process that has terminated but is no longer occupying memory.

- **Process Scheduling Algorithms**:
  - **First-Come-First-Served (FCFS)**: Allocates CPU to the first ready process.
  - **Shortest Job First (SJF)**: Allocates CPU to the shortest ready process.
  - **Priority Scheduling**: Allocates CPU based on priority.

- **Process Synchronization**:
  - **Mutex**: Lock to prevent concurrent access.
  - **Semaphore**: Signal to control access to shared resource.
  - **Monitors**: Encapsulation of shared data and synchronization.

### Important Formulas and Definitions

- **CPU Time**: Time spent executing a process.
- **I/O Time**: Time spent waiting for I/O device.

### Theorems

- **Herd's Theorem**: Maximum CPU time of a process is equal to the sum of its I/O times.
- **Lever's Theorem**: Maximum CPU time of a process is equal to the sum of its I/O times plus the time spent in synchronization primitives.
