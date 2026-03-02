# Process Identifiers

## Introduction

Process Identifiers (PIDs) are fundamental to the management of processes in modern operating systems. In the context of the CSE curriculum, understanding process identifiers is essential for grasping how operating systems track, manage, and coordinate multiple processes executing concurrently on a computer system. A process identifier is a unique numeric value assigned by the operating system kernel to each process running in the system. This identifier serves as the primary mechanism through which the OS can reference, control, and communicate with individual processes.

The concept of process identifiers becomes particularly important when we consider that modern operating systems must handle hundreds or even thousands of processes simultaneously. Each process requires its own identity for proper management, resource allocation, and inter-process communication. Without unique identifiers, the operating system would be unable to distinguish between different processes, leading to chaos in process scheduling, memory management, and I/O operations. This topic forms the backbone of process management in operating systems and is crucial for understanding advanced concepts like process scheduling, interprocess communication, and parent-child process relationships.

## Key Concepts

### Process Control Block (PCB)

The Process Control Block is a data structure maintained by the operating system kernel that contains all the information about a process. Each process in the system has its own PCB, and the PIDs are used to index these blocks. The PCB contains critical information including:

- **Process Identification**: Contains the unique PID, Parent PID (PPID), and User ID (UID)
- **Process State**: Current state of the process (new, ready, running, waiting, or terminated)
- **Program Counter**: Address of the next instruction to be executed
- **CPU Registers**: Current values of processor registers
- **Memory Management Information**: Page tables, segment tables, and memory limits
- **Accounting Information**: CPU usage, time limits, and resource usage statistics
- **I/O Status Information**: List of open files and pending I/O operations

### Process Identifier (PID)

The Process Identifier is a positive integer value assigned by the kernel when a new process is created. In Unix/Linux systems, PID 0 is reserved for the swapper (idle process) and PID 1 is reserved for the init process, which is the first user-space process. PIDs are typically assigned sequentially, and when the maximum value is reached, the counter wraps around to find the lowest available PID. The maximum PID value can be found using the command `cat /proc/sys/kernel/pid_max` on Linux systems.

### Parent Process Identifier (PPID)

Every process (except the init process) has a Parent Process from which it was created. The PPID stores the PID of the creating process, which is typically the shell or parent application. This relationship creates the process hierarchy or process tree. When a parent process terminates before its child processes, the orphaned children have their PPID reassigned to the init process (PID 1), which then becomes their adoptive parent through the wait system call.

### User and Group Identifiers

Each process is associated with a User ID (UID) and Group ID (GID) that determine its privileges and access rights in the system. The real UID represents the actual user who started the process, while the effective UID is used for permission checking during file operations and system calls. This distinction allows processes to run with elevated privileges (like setuid programs) while maintaining knowledge of the original user.

### Process Creation and Termination

When a new process is created using the fork system call in Unix/Linux, the child process receives a new unique PID while inheriting the parent's PPID. The parent process receives the child's PID as the return value of fork, allowing it to manage the child process. Upon process termination using exit or \_exit, the process becomes a zombie until the parent collects its exit status using wait. If the parent terminates first, the child becomes an orphan and is adopted by init.

### Special Process States Related to Identifiers

- **Zombie Process**: A terminated process whose PCB still exists because the parent hasn't collected its exit status via wait
- **Orphan Process**: A running process whose parent has terminated, now adopted by init
- **Daemon Process**: A background process with PPID set to 1 (init), typically used for system services

## Examples

### Example 1: Viewing Process Identifiers in Linux

Consider the following C program to understand process identifiers:

```c
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>

int main {
 pid_t pid, ppid, uid, gid;

 pid = getpid; // Get current process ID
 ppid = getppid; // Get parent process ID
 uid = getuid; // Get user ID
 gid = getgid; // Get group ID

 printf("Process ID (PID): %d\n", pid);
 printf("Parent Process ID (PPID): %d\n", ppid);
 printf("User ID (UID): %d\n", uid);
 printf("Group ID (GID): %d\n", gid);

 return 0;
}
```

**Step-by-step execution:**

1. The process calls getpid which returns the unique PID assigned by the kernel
2. getppid returns the PID of the shell that launched this program
3. getuid and getgid return the numeric user and group identifiers
4. When executed, you'll typically see output where PID is a unique number and PPID matches the shell's PID

### Example 2: Parent-Child Process Relationship

```c
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main {
 pid_t pid;

 pid = fork;

 if (pid < 0) {
 printf("Fork failed\n");
 return 1;
 }
 else if (pid == 0) {
 // Child process
 printf("Child: My PID = %d, Parent PID = %d\n", getpid, getppid);
 printf("Child: Exiting now\n");
 _exit(0);
 }
 else {
 // Parent process
 printf("Parent: My PID = %d, Child PID = %d\n", getpid, pid);
 wait(NULL); // Wait for child to terminate
 printf("Parent: Child has terminated\n");
 }

 return 0;
}
```

**Step-by-step execution:**

1. fork creates a new process
2. In child process (pid == 0): prints its unique PID and parent's PID
3. In parent process: prints its own PID and the child's PID (returned by fork)
4. Parent calls wait to collect child's exit status, preventing zombie creation

### Example 3: Process Hierarchy Demonstration

Using the `ps` command with process status flags:

```bash
# View detailed process information
ps -eo pid,ppid,uid,gid,stat,cmd

# View processes for a specific user
ps -U username

# View process tree
pstree -p
```

The output shows columns for PID, PPID, UID, GID, state, and command. Notice how the PPID of user processes typically matches the shell's PID, creating the hierarchical structure.

## Exam Tips

1. **Remember the reserved PIDs**: PID 0 is the swapper/idle process, and PID 1 is the init process in Unix/Linux systems.

2. **Difference between PID and PPID**: PID is the process's own identifier, while PPID identifies the parent process that created it.

3. **Zombie vs Orphan**: A zombie process has terminated but parent hasn't called wait; an orphan process has lost its parent and been adopted by init.

4. **UID types**: Know the difference between real UID (actual user), effective UID (used for permissions), and saved set-user-ID.

5. **fork return values**: Remember that fork returns 0 to the child process and returns the child's PID to the parent.

6. **PCB is indexed by PID**: The operating system uses PID as the key to access the Process Control Block in the kernel.

7. **Maximum PID**: Understand that PIDs wrap around after reaching the maximum value (typically 32768 or can be through /proc/sys/kernel/pid_max).

8. **Daemon processes**: These are background processes with PPID = 1, meaning their parent has terminated and init has adopted them.
