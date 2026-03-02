# Process Concept, States, and Process Control Block (PCB)

## Introduction

An operating system executes a variety of programs, and the fundamental unit of execution in any modern operating system is the **process**. Understanding processes is crucial for grasping how operating systems manage resources and provide services to users. In simple terms, a process is a program in execution — but this definition barely scratches the surface of what truly constitutes a process in operating system theory.

From the perspective of the University of Delhi's Computer Science curriculum, the process model represents a fundamental abstraction that separates the concept of a "program" (a passive entity, a set of instructions stored on disk) from a "process" (an active entity with its own execution context, memory, registers, and system resources). This abstraction is what enables multiprogramming — the ability to run multiple processes concurrently on a single CPU — which dramatically improves system utilization and user productivity.

The **Process Control Block (PCB)** is the kernel data structure that the operating system maintains for every process. It serves as the "brain" or "identity card" of each process, containing all the information the OS needs to manage, schedule, and control that process. Without PCBs, modern multitasking operating systems would be impossible to implement. This topic forms the foundation for understanding process scheduling, context switching, and inter-process communication — all critical concepts for your operating systems examination.

## Key Concepts

### What is a Process?

A process is more than just a program. While a program is a static file containing instructions and data, a process is a dynamic entity with the following components:

1. **Program Code**: The actual executable instructions
2. **Process Stack**: Contains temporary data such as function parameters, return addresses, and local variables
3. **Heap**: Memory dynamically allocated during runtime
4. **Data Section**: Contains global and static variables
5. **Process Control Block**: The kernel data structure storing process metadata

When you double-click an application icon, the operating system creates a new process by loading the program into memory and initializing its execution context. Multiple instances of the same program (e.g., opening multiple Notepad windows) create multiple distinct processes, each with its own memory space and execution state.

### Process States

A process, during its lifetime, goes through various states. The operating system must track these states to properly manage process execution. The five fundamental process states are:

**1. New (Created) State**
- The process is being created
- The program is being loaded into memory
- PCB is being initialized
- Resources are being allocated
- The process has not yet entered the ready queue

**2. Ready State**
- The process is waiting to be assigned to the CPU
- All necessary resources are allocated
- The process is in the ready queue
- Only one process can run at a time on a CPU, so other ready processes wait their turn

**3. Running State**
- The process's instructions are being executed by the CPU
- Only one process can be in running state per CPU core
- The process can be interrupted and moved back to ready state (preemption)
- The running process may voluntarily give up the CPU by making a system call (e.g., I/O request)

**4. Blocked (Waiting) State**
- The process cannot continue execution until some event occurs
- Common triggers: waiting for I/O operation, waiting for a resource, waiting for another process
- The process is moved from running to blocked state
- Once the event occurs, the process moves back to ready state

**5. Terminated (Exit) State**
- The process has finished execution
- All resources (memory, file handles, I/O buffers) are deallocated
- The parent process may read the child's exit status
- The PCB remains in memory briefly for the parent to collect information

### State Transition Diagram

The transitions between these states follow specific patterns:

- **New → Ready**: OS admits the process to the ready queue
- **Ready → Running**: Scheduler dispatches the process (dispatch)
- **Running → Ready**: Time quantum expires or higher priority process arrives (preemption)
- **Running → Blocked**: Process initiates I/O or waits for event (wait)
- **Blocked → Ready**: I/O completion or event occurs (wakeup)
- **Running → Terminated**: Process completes or calls exit

### Process Control Block (PCB)

The PCB is the most important data structure in the process management subsystem. It is a **kernel-mode data structure** that contains all information needed to manage a particular process. The OS maintains a table of PCBs, often called the **Process Table**, with one entry (PCB) per process.

**Components of a PCB:**

1. **Process Identifier (PID)**
   - Unique integer identifying each process
   - Used by the OS to reference processes
   - Parent Process ID (PPID) tracks process hierarchy

2. **Process State**
   - Current state (new, ready, running, blocked, terminated)
   - Updated by the scheduler

3. **Program Counter (PC)**
   - Address of the next instruction to be executed
   - Saved during context switch
   - Enables process resumption from exactly where it stopped

4. **CPU Registers**
   - Accumulator, index registers, stack pointer, general-purpose registers
   - All must be saved when process is preempted
   - Size and number vary by CPU architecture

5. **CPU Scheduling Information**
   - Process priority
   - Pointer to scheduling queue
   - Scheduling parameters (quantum, aging info)

6. **Memory Management Information**
   - Base and limit registers (for base register relocation)
   - Page tables or segment tables
   - Memory allocation details

7. **Accounting Information**
   - CPU time used
   - Time of arrival
   - Time limits
   - Account numbers

8. **I/O Status Information**
   - List of open files
   - I/O devices allocated
   - Outstanding I/O requests

9. **Pointer to Other PCBs**
   - Links to next PCB in queue
   - Forms various scheduling queues

### Context Switching

The process of saving and restoring the state (CPU registers, program counter, etc.) of a process so that execution can be resumed later is called **context switching**. When the CPU switches from one process to another:

1. The current running process's state is saved in its PCB
2. The OS selects the next process from the ready queue
3. The selected process's state is loaded from its PCB into CPU registers
4. Control is transferred to the new process

**Context Switch Time**: The overhead of switching — not useful work. On modern systems, this can take 1-5 microseconds. While this seems small, it adds up in systems with many processes.

**Factors affecting context switch time:**
- Number of registers to save/restore
- Memory architecture and cache effects
- OS design (lazy saving of registers)
- Hardware support (multiple register sets)

### Process Scheduling Queues

The OS maintains several queues to manage process execution:

1. **Job Queue**: Contains all processes in the system
2. **Ready Queue**: Contains all processes waiting in main memory for CPU
3. **Device Queues**: Contains processes waiting for I/O devices

Processes move between these queues based on their state and scheduling decisions.

## Examples

### Example 1: Tracing Process State Transitions

**Problem**: Consider a text editor process that a user opens, types some content, saves the file, and then closes. Trace the state transitions.

**Solution**:

1. **New → Ready**: User double-clicks the text editor icon. OS loads the program, creates PCB, adds to ready queue.
2. **Ready → Running**: Scheduler dispatches the editor. It enters running state and displays the window.
3. **Running → Ready**: User pauses typing. Another higher-priority process (e.g., antivirus scan) preempts the editor.
4. **Running → Blocked**: User initiates "Save" operation. The editor requests disk I/O and enters blocked state.
5. **Blocked → Ready**: Disk I/O completes. OS moves editor back to ready queue.
6. **Ready → Running**: Editor gets CPU again to finish save operation.
7. **Running → Terminated**: User closes the editor. Process exits, resources are deallocated.

### Example 2: PCB Contents After Context Switch

**Problem**: A process P with PID 1001 is running. Its PCB contains PC = 0x0045A120 and registers: AX=50, BX=25, CX=100. After a context switch to process Q, what happens to P's PCB? Show what gets saved.

**Solution**:

When context switch occurs from P to Q:

```
PCB of P (before switch):
  PID: 1001
  State: Running
  PC: 0x0045A120
  Registers: AX=50, BX=25, CX=100
  ...

Context Switch (OS actions):
1. Save current CPU state into P's PCB:
   - PC: 0x0045A120 → PCB[P].ProgramCounter
   - AX=50 → PCB[P].Registers.AX
   - BX=25 → PCB[P].Registers.BX
   - CX=100 → PCB[P].Registers.CX

2. Change state:
   PCB[P].State = Ready

3. Load Q's state from PCB[Q]:
   - PCB[Q].ProgramCounter → PC
   - PCB[Q].Registers → CPU registers

PCB of P (after switch):
  PID: 1001
  State: Ready
  PC: 0x0045A120 (preserved for next execution)
  Registers: AX=50, BX=25, CX=100 (safely stored)
```

### Example 3: Calculating Average Turnaround Time

**Problem**: Three processes arrive in ready queue at time 0:
- P1: Burst time = 10 units, Priority = 2
- P2: Burst time = 5 units, Priority = 1
- P3: Burst time = 8 units, Priority = 3

Using FCFS (First-Come-First-Served) scheduling, calculate turnaround time and waiting time for each process.

**Solution**:

**Gantt Chart:**
```
| P1(0-10) | P2(10-15) | P3(15-23) |
0         10         15         23
```

**Turnaround Time = Completion Time - Arrival Time**

- P1: 10 - 0 = 10 units
- P2: 15 - 0 = 15 units
- P3: 23 - 0 = 23 units

Average Turnaround Time = (10 + 15 + 23) / 3 = 48/3 = **16 units**

**Waiting Time = Turnaround Time - Burst Time**

- P1: 10 - 10 = 0 units
- P2: 15 - 5 = 10 units
- P3: 23 - 8 = 15 units

Average Waiting Time = (0 + 10 + 15) / 3 = 25/3 = **8.33 units**

## Exam Tips

1. **Distinguish between Program and Process**: This is a classic exam question. Remember: a program is passive (instructions on disk), while a process is active (program in execution with its own resources).

2. **Know all Five Process States**: Be able to draw the state transition diagram from memory. Understand exactly what causes each transition (dispatch, preemption, wait, wakeup, admit, exit).

3. **PCB is the Key Data Structure**: In every exam, expect questions on PCB components. Focus on understanding why each component is necessary, not just memorizing the list.

4. **Context Switching is Overhead**: Remember that context switching consumes CPU time but performs no useful user work. It's a necessary evil for multiprogramming.

5. **Ready vs. Blocked Queue**: Processes in the ready queue need only the CPU; processes in blocked state are waiting for I/O or events. This distinction is important for scheduling algorithms.

6. **State Transitions are Caused By**: Understand the triggers — interrupt (Ready→Running), I/O request (Running→Blocked), I/O completion (Blocked→Ready), time slice expiry (Running→Ready).

7. **PCB Implementation**: The OS maintains a Process Table (array of PCB pointers). Maximum number of processes = size of Process Table. Know that PCB is stored in kernel memory.

8. **Real-World Connection**: Relate concepts to what you see — when a program "hangs," it's likely stuck in Blocked state waiting for I/O or a resource that will never arrive.

9. **Understand Preemption**: Not all OSs preempt processes. In non-preemptive scheduling, a running process runs to completion or until it voluntarily yields. In preemptive, the OS can forcibly take the CPU.

10. **Practice Numerical Problems**: Questions on turnaround time, waiting time, and throughput are common. Practice drawing Gantt charts and computing these metrics for FCFS, SJF, and Round Robin.