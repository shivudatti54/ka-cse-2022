# Process Concept and Scheduling

## Introduction to Processes

An operating system executes a variety of programs. In a batch system, these are called **jobs**, while in a time-shared system, they are called **user programs** or **tasks**. The term **process** is used almost universally to refer to a program in execution.

A process is more than just the program code (often called the **text section**). It also includes:
*   **Current activity**, represented by the value of the **program counter** and the contents of the processor's registers.
*   The **stack**, which contains temporary data (such as function parameters, return addresses, and local variables).
*   The **data section**, which contains global variables.
*   The **heap**, which is memory that is dynamically allocated during process run time.

A program is a **passive entity** (like a recipe on paper), while a process is an **active entity** (like the act of following that recipe, which has a current step and uses various ingredients and tools).

## The Process Control Block (PCB)

Each process is represented in the operating system by a **Process Control Block (PCB)**, also known as a **task control block**. It is a data structure that contains all the information needed to describe and manage a process.

| Information Category | Details Stored in PCB |
| :--- | :--- |
| **Process State** | The current state of the process (e.g., new, ready, running, waiting, terminated). |
| **Process ID (PID)** | A unique identifier number assigned by the OS to every process. |
| **Program Counter** | The address of the next instruction to be executed for this process. |
| **CPU Registers** | The contents of all processor registers (accumulators, index registers, stack pointers, etc.) must be saved when the process is interrupted so it can be restarted correctly later. |
| **CPU-Scheduling Info** | Process priority, pointers to scheduling queues, and other scheduling parameters. |
| **Memory-Management Info** | Base and limit registers, page tables, or segment tables, depending on the memory system used. |
| **Accounting Info** | Amount of CPU and real time used, time limits, account numbers, job/process numbers. |
| **I/O Status Info** | The list of I/O devices allocated to the process, a list of open files, etc. |

When a process is interrupted, the OS saves the current state of the process (its CPU registers, program counter, etc.) into its PCB. When the process is scheduled to run again, this state is restored from the PCB, allowing the process to continue execution exactly where it left off. This mechanism is fundamental to **context switching**.

## Process States

A process moves through a series of discrete states during its lifetime. The typical states are:

1.  **New:** The process is being created.
2.  **Ready:** The process is loaded into memory and waiting to be assigned to a CPU.
3.  **Running:** Instructions are being executed on the CPU.
4.  **Waiting (or Blocked):** The process is waiting for some event to occur (e.g., I/O completion, reception of a signal).
5.  **Terminated:** The process has finished execution.

The transitions between these states are as follows:

```
  +--------+                    +---------+
  |  New   | --(Admitted)-->    |  Ready  | <-----------------+
  +--------+                    +---------+                   |
                                 |                            |
                                 | (Scheduler Dispatch)       | (Interrupt)
                                 v                            |
                            +---------+    (I/O Request)  +---------+
                            | Running | ----------------> | Waiting |
                            +---------+                   +---------+
                                 | ^                            |
                                 | | (I/O Complete)             |
                                 | +----------------------------+
                                 |
                    (Exit / Terminate)
                                 |
                                 v
                            +------------+
                            | Terminated |
                            +------------+
```

## Process Scheduling

The objective of multiprogramming is to have some process running at all times to maximize **CPU utilization**. The objective of time-sharing is to switch the CPU among processes so frequently that users can interact with each program while it is running. To meet these goals, the **process scheduler** selects an available process for program execution on the CPU.

### Scheduling Queues

The OS maintains several queues to manage processes:
*   **Job Queue:** All processes in the system.
*   **Ready Queue:** Set of all processes residing in main memory that are ready and waiting to execute. This is typically stored as a linked list.
*   **Device (or I/O) Queues:** A set of processes waiting for a particular I/O device. Each device has its own queue.

A common representation of these queues is shown below:

```
+-----------------------------------------------------------------------+
|                        LONG-TERM SCHEDULER (Admit)                    |
|  +-------------+    +---------------------------------------------+   |
|  |    Pool of   | ->|                    Job Queue                 |   |
|  | Processes on |    +---------------------------------------------+   |
|  |   Disk/Swap  |                |                                  |   |
|  +-------------+                 v                                  |   |
|                           +-------------+                           |   |
|                           |   Ready     | <- SHORT-TERM SCHEDULER   |   |
|                           |   Queue     |    (CPU Scheduler)        |   |
|                           +-------------+                           |   |
|                                  |                                  |   |
|                                  v                                  |   |
|                            +---------+                              |   |
|                            | Running |                              |   |
|                            +---------+                              |   |
|                                  |                                  |   |
|             (I/O Request)        |           (I/O Complete)        |   |
|           +----------------------+----------------------+           |   |
|           |                      |                      |           |   |
|           v                      v                      v           |   |
|    +--------------+      +--------------+      +--------------+     |   |
|    | Device Queue |      | Device Queue |      | Device Queue | ... |   |
|    |   (Disk)     |      |  (Keyboard)  |      |   (Printer)  |     |   |
|    +--------------+      +--------------+      +--------------+     |   |
+-----------------------------------------------------------------------+
```

### Schedulers

*   **Long-Term Scheduler (Job Scheduler):** Selects processes from the mass-storage pool (disk) and loads them into memory (the ready queue). It controls the **degree of multiprogramming** (the number of processes in memory). It is important to select a good **mix of I/O-bound and CPU-bound processes**.
*   **Short-Term Scheduler (CPU Scheduler):** Selects from among the processes that are ready to execute and allocates the CPU to one of them. This scheduler must be very fast, as it is invoked frequently (e.g., every 100ms).
*   **Medium-Term Scheduler:** Used in systems that support swapping. It can remove a process from memory (and its state from the CPU) and later reintroduce it. This helps manage the degree of multiprogramming and manage processes that are waiting for a long time for an event.

### Context Switch

A **context switch** is the mechanism of switching the CPU from one process to another. It involves:
1.  Saving the state of the old process (into its PCB).
2.  Loading the saved state of the new process (from its PCB).

Context switch time is pure overhead, as the system does no useful work while switching. Its speed depends heavily on hardware support (e.g., multiple register sets). Typical speeds range from 1 to 1000 microseconds.

## Operations on Processes

Processes can create other processes, forming a **process tree**. The creating process is termed the **parent process**, and the new process is the **child process**. Children can inherit resources from their parent (e.g., open files). The primary process creation mechanism is the `fork()` system call in UNIX/Linux, which creates a duplicate of the calling process. This is often followed by an `exec()` system call, which replaces the process's memory space with a new program.

```
+----------------+      fork()       +----------------+
|   Parent       | ----------------> |     Child      |
| Process (bash) |                   | Process (bash) |
| PID: 100       |                   | PID: 101       |
+----------------+                   +----------------+
         |                                  |
         |                                  | execvp("ls", ...)
         |                                  v
         |                           +----------------+
         |                           |   Child        |
         |                           | Process (ls)   |
         |                           | PID: 101       |
         |                           +----------------+
         |
         | waitpid(101, ...)
         v
(Resumes after child terminates)
```

Processes terminate either normally (via `exit()`) or abnormally (due to an error or killed by another process via a signal, e.g., `kill()`). When a process terminates, it returns an exit status to its parent. The parent can retrieve this status using the `wait()` or `waitpid()` system call.

## Interprocess Communication (IPC)

Processes executing concurrently may be either:
*   **Independent Processes:** Cannot affect or be affected by other processes. They do not share data.
*   **Cooperating Processes:** Can affect or be affected by other processes. They can share data and must use **Interprocess Communication (IPC)**.

There are two fundamental models of IPC:
1.  **Shared Memory:** A region of memory is mapped into the address spaces of the cooperating processes. Processes can then read and write to this shared region. This is **faster** as it requires no kernel intervention after the initial setup, but it requires synchronization (e.g., using semaphores) to avoid race conditions.
    ```
    +---------+     Shared Memory     +---------+
    | Process |<-------------------->| Process |
    |    A    |      Region           |    B    |
    +---------+                      +---------+
    ```
2.  **Message Passing:** Communication is done by exchanging messages through the kernel. This is **slower** due to system call overhead but is easier to implement and less prone to complex synchronization issues.
    ```
    +---------+      send()       +----------+      receive()    +---------+
    | Process |------------------>|  Kernel  |----------------->| Process |
    |    A    |                   |          |                  |    B    |
    +---------+    <-----------   +----------+   <-----------   +---------+
                   receive()                      send()
    ```

## Exam Tips

1.  **PCB is Key:** Remember that the PCB is the OS's representation of a process. Be able to list its major components and explain why each is necessary.
2.  **State Transitions:** Draw the state transition diagram and explain what causes each transition (e.g., what event moves a process from Running to Waiting? From Waiting to Ready?).
3.  **Scheduler Roles:** Clearly distinguish the roles of the long-term and short-term schedulers. The long-term controls multiprogramming, the short-term controls CPU allocation.
4.  **Context Switch Overhead:** Understand that context switching is costly. The more frequent the switches, the higher the overhead and the lower the useful work done.
5.  **Fork/Exec:** For creation, know that `fork()` creates a copy and `exec()` overlays a new program. This is a common interview and exam question.
6.  **IPC Models:** Contrast shared memory (fast, needs sync) and message passing (slow, simpler). Be prepared to give an example of when you might use each.