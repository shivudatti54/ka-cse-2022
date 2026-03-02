# Operations on Processes

## Introduction to Process Operations

In an operating system, a **process** is a program in execution. It is the fundamental unit of work that the OS schedules and manages. Process management involves creating, scheduling, terminating, and controlling processes. This section focuses specifically on the **operations** that can be performed on processes, which are the mechanisms by which the operating system and the processes themselves can create, manage, and destroy other processes.

## Key Concepts in Process Operations

### 1. Process Creation

Process creation is the operation of instantiating a new process. This is a fundamental capability in modern operating systems, enabling complex applications and multitasking environments.

**Mechanism of Creation:**
A new process is created by an existing process, known as the **parent process**. The new process is called the **child process**. This relationship forms a **process tree** (or hierarchy), where all processes in a typical UNIX/Linux system trace their ancestry back to the `init` process (PID 1).

**Reasons for Process Creation:**

- **New User Request:** A user starts a program from a shell.
- **System Initialization:** The OS creates processes during boot-up for system services.
- **Batch Job Initiation:** In batch processing systems, a job scheduler creates processes for queued jobs.
- **Execution of a System Call:** A running program requests the OS to create a new process (e.g., a web server creating a new process to handle an incoming client request).

**Steps Involved in Process Creation:**

1. **Allocate Resources:** The OS allocates a unique Process Identifier (PID) and a new Process Control Block (PCB) for the child process.
2. **Initialize PCB:** The child's PCB is populated. Most of its attributes are inherited from the parent process.
3. **Address Space Handling:**

- **Option 1: The child is a duplicate of the parent.** The child gets a copy of the parent's address space, containing the same program and data. This is common in UNIX/Linux systems using the `fork()` system call.
- **Option 2: The child loads a new program.** After being created as a duplicate, the child process often uses a system call like `exec()` to replace its memory space with a brand new program.

4. **Place in Ready Queue:** The new child process is placed in the ready queue, waiting to be scheduled by the CPU scheduler.

**Primary System Calls for Creation:**

- **`fork()`:** Creates a child process that is an exact duplicate of the parent process. Both processes continue execution from the instruction after the `fork()` call. The return value of `fork()` distinguishes parent from child: it returns the new PID to the parent and returns 0 to the child.
- **`exec()`:** After a `fork()`, `exec()` is often called by the child process. It replaces the current process's memory space (code, data, heap, stack) with a new program loaded from an executable file. The PID remains the same, but the program changes completely.

**Example of Process Creation in C (UNIX/Linux):**

```c
#include <stdio.h>
#include <unistd.h>

int main() {
 pid_t pid;

 /* fork a child process */
 pid = fork();

 if (pid < 0) { /* error occurred */
 fprintf(stderr, "Fork Failed");
 return 1;
 }
 else if (pid == 0) { /* child process */
 execlp("/bin/ls", "ls", NULL); // Child replaces itself with the 'ls' program
 }
 else { /* parent process */
 wait(NULL); /* parent will wait for the child to complete */
 printf("Child Complete\n");
 }
 return 0;
}
```

**ASCII Diagram: Process Creation via `fork()` and `exec()`**

```
+---------------------+ fork() +---------------------+
| Parent Process | -----------------> | Child Process |
| (Running Program A) | | (Copy of Program A) |
+---------------------+ +---------------------+
 | |
 | wait(NULL) | execlp("/bin/ls",...)
 | |
 v v
+---------------------+ +---------------------+
| Parent Waits | | Child Process |
| | | (Now Running ls) |
+---------------------+ +---------------------+
 | |
 | <-- Child Terminates --------------------/
 |
 v
+---------------------+
| Parent Resumes & |
| prints "Complete" |
+---------------------+
```

### 2. Process Termination

Process termination occurs when a process completes its execution and the OS reclaims all resources allocated to it.

**Reasons for Termination:**

1. **Normal Exit (Voluntary):** Most processes terminate because they have finished their work. A program calls `exit()` (a system call) to request the OS to terminate it.
2. **Error Exit (Voluntary):** The process encounters an error and chooses to terminate (e.g., a syntax error in user input).
3. **Fatal Error (Involuntary):** The process causes an error (e.g., attempting to access forbidden memory, division by zero), and the OS terminates it.
4. **Killed by Another Process (Involuntary):** A parent process typically has the authority to terminate any of its children. This is done via a system call like `kill()` or `abort()`. The parent might terminate a child if:

- The task assigned to the child is no longer required.
- The child has exceeded the resources it was allocated.
- The user requests termination (e.g., pressing `Ctrl+C` in a terminal).

**Steps Involved in Process Termination:**

1. The terminating process's status is saved for potential parent inspection.
2. All resources allocated to the process are deallocated by the OS (memory, open files, I/O buffers, etc.).
3. The process's entry in the process table (its PCB) is freed.
4. The parent process is informed via the `wait()` system call, receiving the child's exit status.

**Cascading Termination:** In some systems, if a parent process terminates, all of its children are also automatically terminated by the OS. This is called cascading termination. Modern systems like UNIX often reparent orphaned children to the `init` process instead.

### 3. Process Waiting and Synchronization

The `wait()` system call (and its variants like `waitpid()`) is crucial for process synchronization. It allows a parent process to suspend its own execution until one of its child processes terminates.

**Purpose of `wait()`:**

- **Synchronization:** To ensure the parent does not finish before its children, which could leave "zombie" processes.
- **Information Retrieval:** To obtain the exit status of the child process.
- **Resource Cleanup:** The `wait()` call allows the OS to finally deallocate the PCB of the terminated child. A terminated child that has not been `wait()`ed for by its parent is known as a **zombie process**.

### 4. Interprocess Communication (IPC)

While a broader topic, operations for setting up and managing IPC are key process operations. Processes frequently need to communicate and synchronize their actions. There are two primary models:

- **Shared Memory:** Processes map a region of memory into both of their address spaces. They can then read and write to this region directly. Faster, but requires synchronization mechanisms (semaphores) to avoid race conditions.
- **Message Passing:** Processes exchange messages through an OS-managed communication link. Slower due to kernel involvement, but easier to implement and less prone to synchronization errors.

**Key System Calls:** `shmget()`, `shmat()` (shared memory), `pipe()`, `msgget()`, `msgsnd()`, `msgrcv()` (message passing).

## Comparison of Key Process Operations

| Operation     | System Call (Typical) | Description                                                     | Key Effect                                |
| :------------ | :-------------------- | :-------------------------------------------------------------- | :---------------------------------------- |
| **Create**    | `fork()`              | Creates a new child process as a copy of the parent.            | Adds a new process to the system.         |
| **Execute**   | `exec()`              | Replaces the current process's memory space with a new program. | Changes the program a process is running. |
| **Terminate** | `exit()`              | Ends the calling process and returns an exit status.            | Removes a process from the system.        |
| **Wait**      | `wait()`              | Suspends the caller until a child process terminates.           | Synchronizes parent and child processes.  |
| **Kill**      | `kill()`              | Sends a signal to another process, often to terminate it.       | Forces another process to end.            |

## Process States and Operations

Process operations cause transitions between the standard process states. Understanding this relationship is critical.

**ASCII Diagram: Process State Transition with Operations**

```
 [Start] --> NEW --> [Admitted] --> READY <-----------------------+
 ^ |
 | | (Scheduled)
 | v
 (Terminate) RUNNING
 | (I/O or Event Wait) |
 | --------------------------+ | (I/O or Event Complete)
 v v |
 EXIT/ZOMBIE <----------+ WAITING -----------------------------+
 | |
 |(Parent waits) |(Parent waits)
 v |
 [PCB Deallocated] |
 |
 [Orphan Process] ---->+
```

- The `fork()` system call moves a process from the **Running** state to the **Ready** state (for the parent, as it may continue) and creates a new process in the **New** state, which is quickly moved to **Ready**.
- The `exit()` system call moves a process from **Running** to **Terminated/Zombie**.
- The `wait()` system call can move a parent process from **Running** to **Waiting**.

## Exam Tips

1. **Understand `fork()` and `exec()` Deeply:** Be able to trace code involving `fork()`. Remember the return values and the concept of copying the address space. Know that `exec()` replaces the current image; it does not create a new process.
2. **Distinguish Creation from Execution:** `fork()` creates, `exec()` executes a new program. They are often used together but are separate operations.
3. **Know the Fate of the Child:** Be clear on what happens when a parent terminates before its children (orphans) and when a child terminates before its parent `wait()`s for it (zombies).
4. **Relate Operations to States:** Be prepared to draw a process state diagram and label the transitions caused by specific operations like `fork()`, `exit()`, and `wait()`.
5. **Compare IPC Methods:** Understand the trade-offs between shared memory (speed) and message passing (ease of use, safety).
