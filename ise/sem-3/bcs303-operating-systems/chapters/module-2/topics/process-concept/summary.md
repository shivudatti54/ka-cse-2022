# Process Concept - Summary

## Key Definitions and Concepts

- **PROCESS:** A program in execution; a dynamic entity consisting of program code, data, stack, PCB, and allocated resources. Unlike a static program file, a process has a current state and activity.

- **PROCESS CONTROL BLOCK (PCB):** The kernel data structure that stores all information about a process, including PID, parent PID, processor state (registers, program counter), memory management information, scheduling information, I/O status, and accounting data.

- **CONTEXT SWITCH:** The procedure of saving the state of one running process and restoring the state of another, involving complete PCB manipulation.

- **PROCESS STATE:** The current condition of a process (new, ready, running, waiting, terminated) that determines its eligibility for CPU execution.

## Important Formulas and Theorems

There are no specific formulas in the process concept topic, but the following relationships are fundamental:

- Process = Program + Execution Context + Resources
- Each process has ONE PCB but may have MULTIPLE threads
- The OS maintains ONE ready queue and MAY have MULTIPLE wait queues
- Process states follow a finite state machine model with deterministic transitions

## Key Points

1. A PROCESS IS NOT THE SAME AS A PROGRAM—multiple processes can execute the same program simultaneously with separate memory spaces

2. THE FIVE PROCESS STATES are: NEW (being created), READY (waiting for CPU), RUNNING (executing on CPU), WAITING (blocked on event), TERMINATED (finished)

3. THE PCB IS THE HEART OF PROCESS MANAGEMENT—without PCB, the OS cannot manage, schedule, or resume processes

4. IN UNIX, FORK() CREATES A CHILD PROCESS that is a copy of the parent, while in Windows, CreateProcess() creates a new process running a specified program

5. CONTEXT SWITCHING IS EXPENSIVE—it involves saving/restoring CPU registers, updating memory management structures, and flushing CPU caches

6. DAEMON PROCESSES run in background without terminal connection, typically started at system boot

7. ZOMBIE PROCESSES occur when a child terminates but the parent hasn't collected its exit status via wait()

## Common Mistakes to Avoid

- CONFUSING PROCESS WITH PROGRAM: A program is just code stored on disk; a process is an executing instance with its own resources

- THINKING ONLY ONE PROCESS CAN BE READY: The ready queue can hold hundreds of processes waiting for CPU time

- IGNORING THE IMPORTANCE OF PCB: The PCB is not just a data structure—it is the complete execution context of a process

- BELIEVING PROCESS TERMINATION IS IMMEDIATE: Resources are freed, but the PCB remains until the parent collects exit status

## Revision Tips

1. DRAW THE PROCESS STATE DIAGRAM repeatedly until you can reproduce it from memory, labeling all transitions

2. MEMORIZE THE PCB COMPONENTS by grouping them logically: identification, state, control, and accounting information

3. PRACTICE WITH CODE EXAMPLES: trace the execution of fork() programs to understand process creation and state transitions

4. COMPARE OPERATING SYSTEMS: create a comparison table for process creation in Unix versus Windows

5. READ LINUX KERNEL SOURCE or use process monitoring tools (ps, top) to observe real processes on your system