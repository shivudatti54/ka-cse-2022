# Process Concept - Summary

## Key Definitions and Concepts

- **Process:** A program in execution—a dynamic, active entity that includes the program code, current activity (CPU registers, program counter), stack, data section, and heap
- **Program:** A passive entity consisting of instructions and data stored on disk; the blueprint that becomes a process when executed
- **Process Control Block (PCB):** Kernel data structure containing process identification, state, program counter, CPU registers, memory management information, accounting information, and I/O status
- **Context Switch:** The process of saving the state of one process and restoring the state of another
- **Parent Process:** A process that creates another process using fork()
- **Child Process:** A new process created by the parent process

## Important Formulas and Theorems

- Process states: NEW → READY → RUNNING → WAITING → TERMINATED
- Memory layout (typical): Stack (grows down) → Heap (grows up) → Data → Text
- fork() return values: 0 for child process, child's PID for parent, -1 for failure

## Key Points

- A process is the fundamental unit of work in an operating system and represents a program in execution
- The five process states are: New, Ready, Running, Waiting (Blocked), and Terminated
- The PCB stores all information needed by the OS to manage and control a process
- Each process has its own isolated address space, providing memory protection
- The fork() system call creates a new process by duplicating the parent's address space
- Process state transitions are triggered by events such as CPU scheduling, I/O requests, and program completion
- Multiple processes can execute the same program simultaneously, each as an independent process

## Common Mistakes to Avoid

- Confusing a program with a process—they are fundamentally different entities
- Forgetting that fork() returns different values in parent and child processes
- Assuming processes share memory by default—they have isolated address spaces
- Overlooking that only one process can be in running state on a single-processor system at any instant

## Revision Tips

- Draw and label the process state diagram multiple times until you can reproduce it from memory
- Practice writing simple fork() examples and trace through the execution to understand parent-child relationship
- Memorize all components of the PCB and explain why each is necessary
- Review the differences between text, data, heap, and stack segments in process memory layout