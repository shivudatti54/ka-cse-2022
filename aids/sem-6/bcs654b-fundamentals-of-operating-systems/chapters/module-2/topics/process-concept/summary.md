# Process Concept - Summary

## Key Definitions and Concepts

- **Process**: A program in execution; the fundamental unit of work in a computer system. It is an active entity with its own address space, program counter, register values, and stack.
- **Program**: A passive entity consisting of instructions and data stored on disk; the blueprint from which processes are created.
- **Process Control Block (PCB)**: The kernel data structure that stores all information about a process, including its state, program counter, CPU registers, memory management information, accounting data, and I/O status.
- **Process State**: The current condition of a process—New, Ready, Running, Waiting, or Terminated.

## Important Formulas and Theorems

The process concept does not rely on formulas but on understanding relationships:

- One Program → Multiple Processes (each execution creates a new process)
- Process = Program + Execution Context (PCB, registers, memory)
- Process State Transitions: New → Ready → Running → Waiting → Ready → Terminated

## Key Points

1. A process is the basic unit of resource allocation and scheduling in operating systems
2. The PCB is the kernel data structure that represents a process; it contains all process information
3. A process exists in one of five states: New, Ready, Running, Waiting, or Terminated
4. Processes provide isolation—each process has its own address space, ensuring one process cannot directly access another's memory
5. The fork() system call creates a new process; exec() replaces the process image; exit() terminates a process
6. Multiple processes can execute the same program simultaneously, each with independent execution contexts
7. Processes can be independent (no sharing) or cooperative (communicate and share data)
8. In Unix/Linux, processes form a hierarchical tree with init (PID 1) as the root

## Common Mistakes to Avoid

1. **Confusing program and process**: Remember—a program is static (code on disk), while a process is dynamic (program in execution)
2. **Thinking only one process can run at a time**: On multi-core systems, multiple processes genuinely execute in parallel; on single-core systems, time-sharing creates the illusion of concurrency
3. **Ignoring process isolation**: Each process has its own address space; this is fundamental to system stability and security
4. **Overlooking the role of PCB**: The PCB is not just metadata—it is the complete representation of a process in the operating system kernel

## Revision Tips

1. Draw the process state diagram repeatedly until you can reproduce it from memory
2. Practice explaining the process lifecycle using the terminal example (typing a command)
3. Make a table comparing program vs process with at least five distinguishing characteristics
4. Review how fork() and exec() work together to create and run new processes
5. Solve previous year DU questions on process concepts to understand the exam pattern