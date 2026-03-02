# Process Management - Summary

## Key Definitions and Concepts

- **Process**: A program in execution—a dynamic entity consisting of program code, data, stack, heap, and process control information
- **Process Control Block (PCB)**: The data structure that stores all information about a process, including state, program counter, registers, memory management info, and accounting data
- **Context Switch**: The procedure of saving the state of one process and loading the state of another when switching CPU execution
- **Scheduler**: Operating system component that decides which process gets CPU time—long-term (controls multiprogramming), short-term (CPU allocation), and medium-term (swapping)
- **Dispatching**: The act of moving a process from ready state to running state

## Important Formulas and Techniques

- **CPU Utilization**: Percentage of time the CPU is actively executing processes
- **Throughput**: Number of processes completed per unit time
- **Turnaround Time**: Time from process submission to completion (waiting time + execution time)
- **Waiting Time**: Total time a process spends in the ready queue
- **Response Time**: Time from request submission to first response

## Key Points

1. A process differs from a program: the program is passive (stored on disk), while the process is active (in execution)

2. Five process states exist: NEW, READY, RUNNING, WAITING, and TERMINATED—transitions between these states are controlled by the OS

3. The PCB is central to process management—every process has exactly one PCB, created at process creation and destroyed at termination

4. Context switching involves saving program counter, CPU registers, stack pointer, and updating memory management information

5. Process creation uses fork() which creates an identical copy of the parent, followed by exec() to replace the child's program

6. Long-term scheduler admits processes to memory, short-term scheduler selects from ready queue for CPU execution

7. The degree of multiprogramming is controlled by the long-term scheduler—too many processes causes thrashing, too few wastes CPU time

8. Context switching overhead increases with more frequent switches and more state information to save

## Common Mistakes to Avoid

1. Confusing program and process—they are NOT the same; a program can have multiple process instances

2. Thinking only one process can exist in memory at a time—modern OS supports multiprogramming with many processes in memory simultaneously

3. Believing context switching is productive work—it is pure overhead that consumes CPU time without advancing any process

4. Mixing up scheduler types—long-term controls which processes enter the system, short-term controls CPU allocation

5. Forgetting that waiting state occurs when a process requests I/O or waits for an event—the CPU cannot be used during this time

## Revision Tips

1. Draw the process state diagram multiple times until you can do it from memory—state transitions are frequently asked in exams

2. Memorize all PCB components—write them out repeatedly until automatic

3. Practice with real examples: trace what happens when you open an application, save a file, or run a command in terminal

4. Understand the relationship between fork() and exec()—this is classic exam material for process creation

5. Time yourself answering previous years' questions on process management to improve speed and accuracy